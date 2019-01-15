# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bots.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bots.proto',
  package='swarming',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nbots.proto\x12\x08swarming\"L\n\x07\x42otsCfg\x12\x1a\n\x12trusted_dimensions\x18\x01 \x03(\t\x12%\n\tbot_group\x18\x02 \x03(\x0b\x32\x12.swarming.BotGroup\"Z\n\rDailySchedule\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\x12\x18\n\x10\x64\x61ys_of_the_week\x18\x03 \x03(\x05\x12\x13\n\x0btarget_size\x18\x04 \x01(\x05\"7\n\tLoadBased\x12\x14\n\x0cminimum_size\x18\x01 \x01(\x05\x12\x14\n\x0cmaximum_size\x18\x02 \x01(\x05\"[\n\x08Schedule\x12&\n\x05\x64\x61ily\x18\x01 \x03(\x0b\x32\x17.swarming.DailySchedule\x12\'\n\nload_based\x18\x02 \x03(\x0b\x32\x13.swarming.LoadBased\"\xed\x01\n\x0bMachineType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1a\n\x12\x65\x61rly_release_secs\x18\x03 \x01(\x05\x12\x1d\n\x13lease_duration_secs\x18\x04 \x01(\x05H\x00\x12\x1c\n\x12lease_indefinitely\x18\x08 \x01(\x08H\x00\x12\x15\n\rmp_dimensions\x18\x05 \x03(\t\x12\x13\n\x0btarget_size\x18\x06 \x01(\x05\x12$\n\x08schedule\x18\x07 \x01(\x0b\x32\x12.swarming.ScheduleB\x10\n\x0elease_duration\"\x81\x02\n\x08\x42otGroup\x12\x0e\n\x06\x62ot_id\x18\x01 \x03(\t\x12\x15\n\rbot_id_prefix\x18\x02 \x03(\t\x12+\n\x0cmachine_type\x18\x03 \x03(\x0b\x32\x15.swarming.MachineType\x12\x1f\n\x04\x61uth\x18\x14 \x03(\x0b\x32\x11.swarming.BotAuth\x12\x0e\n\x06owners\x18\x15 \x03(\t\x12\x12\n\ndimensions\x18\x16 \x03(\t\x12\x19\n\x11\x62ot_config_script\x18\x17 \x01(\t\x12!\n\x19\x62ot_config_script_content\x18\x19 \x01(\x0c\x12\x1e\n\x16system_service_account\x18\x18 \x01(\t\"\xb1\x01\n\x07\x42otAuth\x12\"\n\x1arequire_luci_machine_token\x18\x01 \x01(\x08\x12\x1f\n\x17require_service_account\x18\x02 \x03(\t\x12\x33\n\x14require_gce_vm_token\x18\x04 \x01(\x0b\x32\x15.swarming.BotAuth.GCE\x12\x14\n\x0cip_whitelist\x18\x03 \x01(\t\x1a\x16\n\x03GCE\x12\x0f\n\x07project\x18\x01 \x01(\tb\x06proto3')
)




_BOTSCFG = _descriptor.Descriptor(
  name='BotsCfg',
  full_name='swarming.BotsCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trusted_dimensions', full_name='swarming.BotsCfg.trusted_dimensions', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bot_group', full_name='swarming.BotsCfg.bot_group', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=100,
)


_DAILYSCHEDULE = _descriptor.Descriptor(
  name='DailySchedule',
  full_name='swarming.DailySchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='swarming.DailySchedule.start', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='swarming.DailySchedule.end', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='days_of_the_week', full_name='swarming.DailySchedule.days_of_the_week', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_size', full_name='swarming.DailySchedule.target_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=192,
)


_LOADBASED = _descriptor.Descriptor(
  name='LoadBased',
  full_name='swarming.LoadBased',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minimum_size', full_name='swarming.LoadBased.minimum_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximum_size', full_name='swarming.LoadBased.maximum_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=249,
)


_SCHEDULE = _descriptor.Descriptor(
  name='Schedule',
  full_name='swarming.Schedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='daily', full_name='swarming.Schedule.daily', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='load_based', full_name='swarming.Schedule.load_based', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=342,
)


_MACHINETYPE = _descriptor.Descriptor(
  name='MachineType',
  full_name='swarming.MachineType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='swarming.MachineType.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='swarming.MachineType.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='early_release_secs', full_name='swarming.MachineType.early_release_secs', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lease_duration_secs', full_name='swarming.MachineType.lease_duration_secs', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lease_indefinitely', full_name='swarming.MachineType.lease_indefinitely', index=4,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mp_dimensions', full_name='swarming.MachineType.mp_dimensions', index=5,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_size', full_name='swarming.MachineType.target_size', index=6,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schedule', full_name='swarming.MachineType.schedule', index=7,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='lease_duration', full_name='swarming.MachineType.lease_duration',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=345,
  serialized_end=582,
)


_BOTGROUP = _descriptor.Descriptor(
  name='BotGroup',
  full_name='swarming.BotGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bot_id', full_name='swarming.BotGroup.bot_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bot_id_prefix', full_name='swarming.BotGroup.bot_id_prefix', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='machine_type', full_name='swarming.BotGroup.machine_type', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth', full_name='swarming.BotGroup.auth', index=3,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owners', full_name='swarming.BotGroup.owners', index=4,
      number=21, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='swarming.BotGroup.dimensions', index=5,
      number=22, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bot_config_script', full_name='swarming.BotGroup.bot_config_script', index=6,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bot_config_script_content', full_name='swarming.BotGroup.bot_config_script_content', index=7,
      number=25, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_service_account', full_name='swarming.BotGroup.system_service_account', index=8,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=842,
)


_BOTAUTH_GCE = _descriptor.Descriptor(
  name='GCE',
  full_name='swarming.BotAuth.GCE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='swarming.BotAuth.GCE.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1000,
  serialized_end=1022,
)

_BOTAUTH = _descriptor.Descriptor(
  name='BotAuth',
  full_name='swarming.BotAuth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='require_luci_machine_token', full_name='swarming.BotAuth.require_luci_machine_token', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='require_service_account', full_name='swarming.BotAuth.require_service_account', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='require_gce_vm_token', full_name='swarming.BotAuth.require_gce_vm_token', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_whitelist', full_name='swarming.BotAuth.ip_whitelist', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BOTAUTH_GCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=1022,
)

_BOTSCFG.fields_by_name['bot_group'].message_type = _BOTGROUP
_SCHEDULE.fields_by_name['daily'].message_type = _DAILYSCHEDULE
_SCHEDULE.fields_by_name['load_based'].message_type = _LOADBASED
_MACHINETYPE.fields_by_name['schedule'].message_type = _SCHEDULE
_MACHINETYPE.oneofs_by_name['lease_duration'].fields.append(
  _MACHINETYPE.fields_by_name['lease_duration_secs'])
_MACHINETYPE.fields_by_name['lease_duration_secs'].containing_oneof = _MACHINETYPE.oneofs_by_name['lease_duration']
_MACHINETYPE.oneofs_by_name['lease_duration'].fields.append(
  _MACHINETYPE.fields_by_name['lease_indefinitely'])
_MACHINETYPE.fields_by_name['lease_indefinitely'].containing_oneof = _MACHINETYPE.oneofs_by_name['lease_duration']
_BOTGROUP.fields_by_name['machine_type'].message_type = _MACHINETYPE
_BOTGROUP.fields_by_name['auth'].message_type = _BOTAUTH
_BOTAUTH_GCE.containing_type = _BOTAUTH
_BOTAUTH.fields_by_name['require_gce_vm_token'].message_type = _BOTAUTH_GCE
DESCRIPTOR.message_types_by_name['BotsCfg'] = _BOTSCFG
DESCRIPTOR.message_types_by_name['DailySchedule'] = _DAILYSCHEDULE
DESCRIPTOR.message_types_by_name['LoadBased'] = _LOADBASED
DESCRIPTOR.message_types_by_name['Schedule'] = _SCHEDULE
DESCRIPTOR.message_types_by_name['MachineType'] = _MACHINETYPE
DESCRIPTOR.message_types_by_name['BotGroup'] = _BOTGROUP
DESCRIPTOR.message_types_by_name['BotAuth'] = _BOTAUTH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BotsCfg = _reflection.GeneratedProtocolMessageType('BotsCfg', (_message.Message,), dict(
  DESCRIPTOR = _BOTSCFG,
  __module__ = 'bots_pb2'
  # @@protoc_insertion_point(class_scope:swarming.BotsCfg)
  ))
_sym_db.RegisterMessage(BotsCfg)

DailySchedule = _reflection.GeneratedProtocolMessageType('DailySchedule', (_message.Message,), dict(
  DESCRIPTOR = _DAILYSCHEDULE,
  __module__ = 'bots_pb2'
  # @@protoc_insertion_point(class_scope:swarming.DailySchedule)
  ))
_sym_db.RegisterMessage(DailySchedule)

LoadBased = _reflection.GeneratedProtocolMessageType('LoadBased', (_message.Message,), dict(
  DESCRIPTOR = _LOADBASED,
  __module__ = 'bots_pb2'
  # @@protoc_insertion_point(class_scope:swarming.LoadBased)
  ))
_sym_db.RegisterMessage(LoadBased)

Schedule = _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULE,
  __module__ = 'bots_pb2'
  # @@protoc_insertion_point(class_scope:swarming.Schedule)
  ))
_sym_db.RegisterMessage(Schedule)

MachineType = _reflection.GeneratedProtocolMessageType('MachineType', (_message.Message,), dict(
  DESCRIPTOR = _MACHINETYPE,
  __module__ = 'bots_pb2'
  # @@protoc_insertion_point(class_scope:swarming.MachineType)
  ))
_sym_db.RegisterMessage(MachineType)

BotGroup = _reflection.GeneratedProtocolMessageType('BotGroup', (_message.Message,), dict(
  DESCRIPTOR = _BOTGROUP,
  __module__ = 'bots_pb2'
  # @@protoc_insertion_point(class_scope:swarming.BotGroup)
  ))
_sym_db.RegisterMessage(BotGroup)

BotAuth = _reflection.GeneratedProtocolMessageType('BotAuth', (_message.Message,), dict(

  GCE = _reflection.GeneratedProtocolMessageType('GCE', (_message.Message,), dict(
    DESCRIPTOR = _BOTAUTH_GCE,
    __module__ = 'bots_pb2'
    # @@protoc_insertion_point(class_scope:swarming.BotAuth.GCE)
    ))
  ,
  DESCRIPTOR = _BOTAUTH,
  __module__ = 'bots_pb2'
  # @@protoc_insertion_point(class_scope:swarming.BotAuth)
  ))
_sym_db.RegisterMessage(BotAuth)
_sym_db.RegisterMessage(BotAuth.GCE)


# @@protoc_insertion_point(module_scope)