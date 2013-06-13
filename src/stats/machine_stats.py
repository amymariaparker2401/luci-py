#!/usr/bin/python2.7
#
# Copyright 2013 Google Inc. All Rights Reserved.

"""Machine Stats.

The model of the Machine Stats, and various helper functions.
"""


import datetime
import logging

from google.appengine.api import app_identity
from google.appengine.ext import db
from server import admin_user


# The number of days that have to pass before a machine is considered dead.
MACHINE_TIMEOUT_IN_DAYS = 3

# The message to use for each dead machine.
_INDIVIDUAL_DEAD_MACHINE_MESSAGE = (
    'Machine %(machine_id)s(%(machine_tag)s) was last seen %(last_seen)s and '
    'is assumed to be dead.')

# The message body of the dead machine message to send admins.
_DEAD_MACHINE_MESSAGE_BODY = """Hello,

The following registered machines haven't been active in %(timeout)s days.

%(death_summary)s

Please revive the machines or remove them from the list of active machines.
"""


class MachineStats(db.Model):
  """A machine's stats."""
  # The tag of the machine polling.
  tag = db.StringProperty(default='')

  # The dimensions of the machine polling.
  dimensions = db.StringProperty(default='')

  # The last day the machine queried for work.
  last_seen = db.DateProperty(auto_now=True, required=True)

  def MachineID(self):
    """Get the machine id of this stat.

    The machine id is stored as the model's key.

    Returns:
      The machine id.
    """
    return self.key().name()


def _GetCurrentDay():
  """Returns the current day.

  This function is defined so it can be mocked out in tests.

  Returns:
    The current day.
  """
  return datetime.date.today()


def FindDeadMachines():
  """Find all dead machines.

  Returns:
    A list of the dead machines.
  """
  dead_machine_cutoff = (_GetCurrentDay() -
                         datetime.timedelta(days=MACHINE_TIMEOUT_IN_DAYS))

  return list(MachineStats.gql('WHERE last_seen < :1', dead_machine_cutoff))


def NotifyAdminsOfDeadMachines(dead_machines):
  """Notify the admins of the dead_machines detected.

  Args:
    dead_machines: The list of the currently dead machines.

  Returns:
    True if the email was successfully sent.
  """
  death_summary = []
  for machine in dead_machines:
    death_summary.append(
        _INDIVIDUAL_DEAD_MACHINE_MESSAGE % {'machine_id': machine.MachineID(),
                                            'machine_tag': machine.tag,
                                            'last_seen': machine.last_seen})

  subject = 'Dead Machines Found on %s' % app_identity.get_application_id()
  body = _DEAD_MACHINE_MESSAGE_BODY % {
      'timeout': MACHINE_TIMEOUT_IN_DAYS,
      'death_summary': '\n'.join(death_summary)}

  return admin_user.EmailAdmins(subject, body)


def RecordMachineQueriedForWork(machine_id, dimensions_str, machine_tag):
  """Records when a machine has queried for work.

  Args:
    machine_id: The machine id of the machine.
    dimensions_str: The string representation of the machines dimensions.
    machine_tag: The tag identifier of the machine.
  """
  machine_stats = MachineStats.get_or_insert(machine_id)

  if (machine_stats.dimensions != dimensions_str or
      machine_stats.last_seen < datetime.date.today() or
      machine_stats.tag != machine_tag):
    machine_stats.dimensions = dimensions_str
    machine_stats.tag = machine_tag
    # Calling put() automatically updates the last_seen value.
    machine_stats.put()


def DeleteMachineStats(key):
  """Delete the machine assignment referenced to by the given key.

  Args:
    key: The key of the machine assignment to delete.

  Returns:
    True if the key was valid and machine assignment was successfully deleted.
  """
  try:
    machine_stats = MachineStats.get(key)
  except (db.BadKeyError, db.BadArgumentError):
    logging.error('Invalid MachineStats key given, %s', str(key))
    return False

  if not machine_stats:
    logging.error('No MachineStats has key %s', str(key))
    return False

  machine_stats.delete()
  return True


def GetAllMachines(sort_by='machine_id'):
  """Get the list of whitelisted machines.

  Args:
    sort_by: The string of the attribute to sort the machines by.

  Returns:
    An iterator of all machines whitelisted.
  """
  # If we recieve an invalid sort_by parameter, just default to machine_id.
  if sort_by not in MachineStats.properties():
    sort_by = 'machine_id'

  return (machine for machine in MachineStats.gql('ORDER BY %s' % sort_by))


def GetMachineTag(machine_id):
  """Get the tag for a given machine id.

  Args:
    machine_id: The machine id to find the tag for

  Returns:
    The machine's tag, or None if the machine id isn't used.
  """
  machine = MachineStats.get_by_key_name(machine_id) if machine_id else None

  return machine.tag if machine else 'Unknown'
