#!/usr/bin/env python
# Copyright 2014 The Swarming Authors. All rights reserved.
# Use of this source code is governed by the Apache v2.0 license that can be
# found in the LICENSE file.

import datetime
import logging
import os
import sys
import unittest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

import test_env

test_env.setup_test_env()

# From tools/third_party/
import webtest

from google.appengine.ext import deferred
from google.appengine.ext import ndb

from components import utils
from server import result_helper
from server import task_common
from server import task_request
from server import task_result
from server import task_to_run
from support import test_case

# pylint: disable=W0212


def _gen_request_data(properties=None, **kwargs):
  base_data = {
    'name': 'Request name',
    'user': 'Jesus',
    'properties': {
      'commands': [[u'command1']],
      'data': [],
      'dimensions': {},
      'env': {},
      'execution_timeout_secs': 24*60*60,
      'io_timeout_secs': None,
    },
    'priority': 50,
    'scheduling_expiration_secs': 60,
  }
  base_data.update(kwargs)
  base_data['properties'].update(properties or {})
  return base_data


def _safe_cmp(a, b):
  # cmp(datetime.datetime.utcnow(), None) throws TypeError. Workaround.
  return cmp(utils.encode_to_json(a), utils.encode_to_json(b))


def get_entities(entity_model):
  return sorted(
      (i.to_dict() for i in entity_model.query().fetch()), cmp=_safe_cmp)


class TaskResultApiTest(test_case.TestCase):
  APP_DIR = ROOT_DIR

  def setUp(self):
    super(TaskResultApiTest, self).setUp()
    self.now = datetime.datetime(2014, 1, 2, 3, 4, 5, 6)
    self.mock_now(self.now)
    self.mock(task_request.random, 'getrandbits', lambda _: 0x88)
    self.app = webtest.TestApp(
        deferred.application,
        extra_environ={
          'REMOTE_ADDR': '1.0.1.2',
          'SERVER_SOFTWARE': os.environ['SERVER_SOFTWARE'],
        })

  def assertEntities(self, expected, entity_model):
    self.assertEqual(expected, get_entities(entity_model))

  def test_all_apis_are_tested(self):
    # Ensures there's a test for each public API.
    module = task_result
    expected = set(
        i for i in dir(module)
        if i[0] != '_' and hasattr(getattr(module, i), 'func_name'))
    missing = expected - set(i[5:] for i in dir(self) if i.startswith('test_'))
    self.assertFalse(missing)

  def test_State(self):
    for i in task_result.State.STATES:
      self.assertTrue(task_result.State.to_string(i))
    with self.assertRaises(ValueError):
      task_result.State.to_string(0)

    self.assertEqual(
        set(task_result.State._NAMES), set(task_result.State.STATES))
    items = (
      task_result.State.STATES_RUNNING + task_result.State.STATES_DONE +
      task_result.State.STATES_ABANDONED)
    self.assertEqual(set(items), set(task_result.State.STATES))
    self.assertEqual(len(items), len(set(items)))
    self.assertEqual(
        task_result.State.STATES_RUNNING + task_result.State.STATES_NOT_RUNNING,
        task_result.State.STATES)

  def test_state_to_string(self):
    # Same code as State.to_string() except that it works for
    # TaskResultSummary too.
    class Foo(ndb.Model):
      state = task_result.StateProperty()
      failure = ndb.BooleanProperty(default=False)
      internal_failure = ndb.BooleanProperty(default=False)

    for i in task_result.State.STATES:
      self.assertTrue(task_result.State.to_string(i))
    for i in task_result.State.STATES:
      self.assertTrue(task_result.state_to_string(Foo(state=i)))

  def test_request_key_to_result_summary_key(self):
    request_key = task_request.id_to_request_key(256)
    result_key = task_result.request_key_to_result_summary_key(
        request_key)
    expected = (
        "Key('TaskRequestShard', 'f71849', 'TaskRequest', 256, "
        "'TaskResultSummary', 1)")
    self.assertEqual(expected, str(result_key))

  def test_result_summary_key_to_request_key(self):
    request_key = task_request.id_to_request_key(0x100)
    result_summary_key = task_result.request_key_to_result_summary_key(
        request_key)
    actual = task_result.result_summary_key_to_request_key(result_summary_key)
    self.assertEqual(request_key, actual)

  def test_result_summary_key_to_run_result_key(self):
    request_key = task_request.id_to_request_key(0x100)
    result_summary_key = task_result.request_key_to_result_summary_key(
        request_key)
    run_result_key = task_result.result_summary_key_to_run_result_key(
        result_summary_key, 1)
    expected = (
        "Key('TaskRequestShard', 'f71849', 'TaskRequest', 256, "
        "'TaskResultSummary', 1, 'TaskRunResult', 1)")
    self.assertEqual(expected, str(run_result_key))

    with self.assertRaises(ValueError):
      task_result.result_summary_key_to_run_result_key(result_summary_key, 0)
    with self.assertRaises(NotImplementedError):
      task_result.result_summary_key_to_run_result_key(result_summary_key, 2)

  def test_run_result_key_to_result_summary_key(self):
    request_key = task_request.id_to_request_key(0x100)
    result_summary_key = task_result.request_key_to_result_summary_key(
        request_key)
    run_result_key = task_result.result_summary_key_to_run_result_key(
        result_summary_key, 1)
    self.assertEqual(
        result_summary_key,
        task_result.run_result_key_to_result_summary_key(run_result_key))

  def test_new_result_summary(self):
    request = task_request.make_request(_gen_request_data())
    actual = task_result.new_result_summary(request)
    expected = {
      'abandoned_ts': None,
      'bot_id': None,
      'completed_ts': None,
      'created_ts': self.now,
      'durations': [],
      'exit_codes': [],
      'failure': False,
      'internal_failure': False,
      'modified_ts': None,
      'name': u'Request name',
      'outputs': [],
      'started_ts': None,
      'state': task_result.State.PENDING,
      'try_number': None,
      'user': u'Jesus',
    }
    self.assertEqual(expected, actual.to_dict())
    self.assertEqual(50, actual.priority)

  def test_new_run_result(self):
    request = task_request.make_request(_gen_request_data())
    actual = task_result.new_run_result(request, 1, 'localhost')
    expected = {
      'abandoned_ts': None,
      'bot_id': 'localhost',
      'completed_ts': None,
      'durations': [],
      'exit_codes': [],
      'failure': False,
      'internal_failure': False,
      'modified_ts': None,
      'outputs': [],
      'started_ts': self.now,
      'state': task_result.State.RUNNING,
      'try_number': 1,
    }
    self.assertEqual(expected, actual.to_dict())
    self.assertEqual(50, actual.priority)

  def test_integration(self):
    # Creates a TaskRequest, along its TaskResultSummary and TaskToRun. Have a
    # bot reap the task, and complete the task. Ensure the resulting
    # TaskResultSummary and TaskRunResult are properly updated.
    request = task_request.make_request(_gen_request_data())
    result_summary = task_result.new_result_summary(request)
    task = task_to_run.new_task_to_run(request)
    ndb.put_multi([result_summary, task])
    expected = {
      'abandoned_ts': None,
      'bot_id': None,
      'durations': [],
      'exit_codes': [],
      'completed_ts': None,
      'created_ts': self.now,
      'internal_failure': False,
      'modified_ts': self.now,
      'name': u'Request name',
      'outputs': [],
      'started_ts': None,
      'failure': False,
      'state': task_result.State.PENDING,
      'try_number': None,
      'user': u'Jesus',
    }
    self.assertEqual(expected, result_summary.to_dict())

    # Nothing changed 2 secs later except latency.
    self.mock_now(self.now, 2)
    self.assertEqual(expected, result_summary.to_dict())

    # Task is reaped after 2 seconds (4 secs total).
    reap_ts = self.now + datetime.timedelta(seconds=4)
    self.mock_now(reap_ts)
    task = task_to_run.is_task_reapable(task.key, None)
    task.queue_number = None
    task.put()
    run_result = task_result.new_run_result(request, 1, 'localhost')
    ndb.put_multi(task_result.prepare_put_run_result(run_result))
    expected = {
      'abandoned_ts': None,
      'bot_id': u'localhost',
      'completed_ts': None,
      'created_ts': self.now,
      'durations': [],
      'exit_codes': [],
      'internal_failure': False,
      'modified_ts': reap_ts,
      'name': u'Request name',
      'outputs': [],
      'started_ts': reap_ts,
      'failure': False,
      'state': task_result.State.RUNNING,
      'try_number': 1,
      'user': u'Jesus',
    }
    self.assertEqual(expected, result_summary.to_dict())

    # Task completed after 2 seconds (6 secs total), the task has been running
    # for 2 seconds.
    complete_ts = self.now + datetime.timedelta(seconds=6)
    self.mock_now(complete_ts)
    run_result.completed_ts = complete_ts
    run_result.exit_codes.append(0)
    run_result.state = task_result.State.COMPLETED
    # This is the old way of storing data. Ensure this works too.
    # https://code.google.com/p/swarming/issues/detail?id=116
    results_key = result_helper.StoreResults('foo').key
    run_result.outputs.append(results_key)
    ndb.put_multi(task_result.prepare_put_run_result(run_result))
    expected = {
      'abandoned_ts': None,
      'bot_id': u'localhost',
      'completed_ts': complete_ts,
      'created_ts': self.now,
      'durations': [],
      'exit_codes': [0],
      'failure': False,
      'internal_failure': False,
      'modified_ts': complete_ts,
      'name': u'Request name',
      'outputs': ['foo'],
      'started_ts': reap_ts,
      'state': task_result.State.COMPLETED,
      'try_number': 1,
      'user': u'Jesus',
    }
    self.assertEqual(expected, result_summary.to_dict())
    self.assertEqual(['foo'], result_summary.get_outputs())
    self.assertEqual(datetime.timedelta(seconds=2), result_summary.duration)
    self.assertEqual(
        datetime.timedelta(seconds=2), result_summary.duration_now())
    self.assertEqual(
        datetime.timedelta(seconds=4), result_summary.pending)
    self.assertEqual(
        datetime.timedelta(seconds=4), result_summary.pending_now())

    self.assertEqual(
        task_common.pack_result_summary_key(result_summary.key),
        result_summary.key_string)
    self.assertEqual(complete_ts, result_summary.ended_ts)
    self.assertEqual(
        task_common.pack_run_result_key(run_result.key),
        run_result.key_string)
    self.assertEqual(complete_ts, run_result.ended_ts)

  def test_yield_run_results_with_dead_bot(self):
    request = task_request.make_request(_gen_request_data())
    result_summary = task_result.new_result_summary(request)
    result_summary.put()
    run_result = task_result.new_run_result(request, 1, 'localhost')
    run_result.completed_ts = self.now
    ndb.put_multi(task_result.prepare_put_run_result(run_result))

    self.mock_now(self.now + task_common.BOT_PING_TOLERANCE)
    self.assertEqual([], list(task_result.yield_run_results_with_dead_bot()))

    self.mock_now(self.now + task_common.BOT_PING_TOLERANCE, 1)
    self.assertEqual(
        [run_result], list(task_result.yield_run_results_with_dead_bot()))

  def test_prepare_put_run_result(self):
    request = task_request.make_request(_gen_request_data())
    result_summary = task_result.new_result_summary(request)
    run_result = task_result.new_run_result(request, 1, 'localhost')
    self.assertTrue(result_summary.need_update_from_run_result(run_result))
    ndb.put_multi((result_summary, run_result))

    self.assertTrue(result_summary.need_update_from_run_result(run_result))
    ndb.put_multi(task_result.prepare_put_run_result(run_result))

    self.assertFalse(result_summary.need_update_from_run_result(run_result))

  def test_run_result_duration(self):
    run_result = task_result.TaskRunResult(
        started_ts=datetime.datetime(2010, 1, 1, 0, 0, 0),
        completed_ts=datetime.datetime(2010, 1, 1, 0, 2, 0))
    self.assertEqual(datetime.timedelta(seconds=120), run_result.duration)
    self.assertEqual(datetime.timedelta(seconds=120), run_result.duration_now())

    run_result = task_result.TaskRunResult(
        started_ts=datetime.datetime(2010, 1, 1, 0, 0, 0),
        abandoned_ts=datetime.datetime(2010, 1, 1, 0, 1, 0))
    self.assertEqual(None, run_result.duration)
    self.assertEqual(None, run_result.duration_now())

  def test_append_output(self):
    # Test that one can stream output and it is returned fine.
    request = task_request.make_request(_gen_request_data())
    result_summary = task_result.new_result_summary(request)
    result_summary.put()
    run_result = task_result.new_run_result(request, 1, 'localhost')
    ndb.put_multi(task_result.prepare_put_run_result(run_result))

    def run(*args):
      entities = run_result.append_output(*args)
      self.assertEqual(1, len(entities))
      ndb.put_multi(entities)
    run(0, 0, 'Part1\n')
    run(1, 0, 'Part2\n')
    run(1, 1, 'Part3\n')
    self.assertEqual(['Part1\n', 'Part2\nPart3\n'], run_result.get_outputs())
    self.assertEqual('Part1\n', run_result.get_command_output(0))
    self.assertEqual('Part2\nPart3\n', run_result.get_command_output(1))
    self.assertEqual(None, run_result.get_command_output(2))

  def test_append_output_out_of_order(self):
    request = task_request.make_request(_gen_request_data())
    result_summary = task_result.new_result_summary(request)
    result_summary.put()
    run_result = task_result.new_run_result(request, 1, 'localhost')
    ndb.put_multi(task_result.prepare_put_run_result(run_result))

    def run(*args):
      entities = run_result.append_output(*args)
      self.assertEqual(1, len(entities))
      ndb.put_multi(entities)
    run(1, 0, 'Part1\n')
    with self.assertRaises(ValueError):
      # It should have been run(1, 1, ...). Duplicate packet #0 is refused.
      run(1, 0, 'Part1(bis)\n')
    with self.assertRaises(ValueError):
      # It should have been run(1, 1, ...). Packet #2 will be refused until #1
      # is received.
      run(1, 2, 'Part2\n')
    run(1, 1, 'Part3\n')
    with self.assertRaises(ValueError):
      # It should have been run(1, 2, ...). Packet #0 was already received.
      run(1, 0, 'Part4\n')
    run(1, 2, 'Part5\n')
    self.assertEqual(['', 'Part1\nPart3\nPart5\n'], run_result.get_outputs())

  def test_append_output_large(self):
    self.mock(logging, 'error', lambda *_: None)
    request = task_request.make_request(_gen_request_data())
    result_summary = task_result.new_result_summary(request)
    result_summary.put()
    run_result = task_result.new_run_result(request, 1, 'localhost')
    ndb.put_multi(task_result.prepare_put_run_result(run_result))

    one_mb = '<3Google' * (1024*1024/8)

    def run(*args):
      entities = run_result.append_output(*args)
      # Asserts at least one entity was created.
      self.assertTrue(entities)
      ndb.put_multi(entities)

    for i in xrange(16):
      run(0, i, one_mb)

    # It can't take it anymore. It ignores the packet number at that point.
    self.assertEqual([], run_result.append_output(0, 16, one_mb))
    self.assertEqual([], run_result.append_output(0, 16, one_mb))
    self.assertEqual([], run_result.append_output(0, 17, one_mb))

    self.assertEqual(
        task_result.TaskOutputChunk.MAX_CONTENT,
        len(run_result.get_command_output(0)))

  def test_append_output_max_chunk(self):
    calls = []
    self.mock(logging, 'error', lambda *args: calls.append(args))
    request = task_request.make_request(_gen_request_data())
    result_summary = task_result.new_result_summary(request)
    result_summary.put()
    run_result = task_result.new_run_result(request, 1, 'localhost')
    ndb.put_multi(task_result.prepare_put_run_result(run_result))
    max_chunk = 'x' * task_result.TaskOutputChunk.MAX_CONTENT
    entities = run_result.append_output(0, 0, max_chunk)
    self.assertEqual(task_result.TaskOutputChunk.MAX_CHUNKS, len(entities))
    ndb.put_multi(entities)
    self.assertEqual([], calls)

    # Try with MAX_CONTENT + 1 bytes, so the last byte is discarded.
    entities = run_result.append_output(1, 0, max_chunk + 'x')
    self.assertEqual(task_result.TaskOutputChunk.MAX_CHUNKS, len(entities))
    ndb.put_multi(entities)
    self.assertEqual(1, len(calls))
    self.assertTrue(calls[0][0].startswith('Dropping '), calls[0][0])
    self.assertEqual(1, calls[0][1])


if __name__ == '__main__':
  if '-v' in sys.argv:
    unittest.TestCase.maxDiff = None
  unittest.main()
