# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: swarming.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='swarming.proto',
  package='swarming',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0eswarming.proto\x12\x08swarming\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa7\x01\n\x10\x42otEventsRequest\x12\x0e\n\x06\x62ot_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12.\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"P\n\x11\x42otEventsResponse\x12\"\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x12.swarming.BotEvent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc9\x01\n\x03\x42ot\x12\x0e\n\x06\x62ot_id\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\'\n\x06status\x18\x03 \x01(\x0e\x32\x17.swarming.BotStatusType\x12\x12\n\nstatus_msg\x18\x04 \x01(\t\x12\x17\n\x0f\x63urrent_task_id\x18\x05 \x01(\t\x12\'\n\ndimensions\x18\x06 \x03(\x0b\x32\x13.swarming.Dimension\x12\x1f\n\x04info\x18\x07 \x01(\x0b\x32\x11.swarming.BotInfo\"o\n\x07\x42otInfo\x12$\n\x03raw\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x13\n\x0b\x65xternal_ip\x18\x03 \x01(\t\x12\x18\n\x10\x61uthenticated_as\x18\x04 \x01(\t\"\x90\x01\n\x08\x42otEvent\x12.\n\nevent_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x03\x62ot\x18\x02 \x01(\x0b\x32\r.swarming.Bot\x12%\n\x05\x65vent\x18\x03 \x01(\x0e\x32\x16.swarming.BotEventType\x12\x11\n\tevent_msg\x18\x04 \x01(\t\"(\n\tDimension\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t*\xdf\x01\n\rBotStatusType\x12\x1a\n\x16\x42OT_STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07MISSING\x10\x01\x12\x19\n\x15QUARANTINED_BY_SERVER\x10\x02\x12\x16\n\x12QUARANTINED_BY_BOT\x10\x03\x12!\n\x1dOVERHEAD_MAINTENANCE_EXTERNAL\x10\x04\x12\x19\n\x15OVERHEAD_BOT_INTERNAL\x10\x05\x12\x12\n\x0eHOST_REBOOTING\x10\x06\x12\x08\n\x04\x42USY\x10\x07\x12\x0c\n\x08RESERVED\x10\x08\x12\x08\n\x04IDLE\x10\t*\xed\x02\n\x0c\x42otEventType\x12\x1e\n\x1a\x42OT_EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x42OT_NEW_SESSION\x10\x01\x12\x18\n\x14\x42OT_INTERNAL_FAILURE\x10\x02\x12\x12\n\x0e\x42OT_HOOK_ERROR\x10\x03\x12\x10\n\x0c\x42OT_HOOK_LOG\x10\x04\x12\x16\n\x12\x42OT_REBOOTING_HOST\x10\x05\x12\x10\n\x0c\x42OT_SHUTDOWN\x10\x06\x12\x11\n\rINSTRUCT_IDLE\x10\n\x12\x17\n\x13INSTRUCT_START_TASK\x10\x0b\x12\x18\n\x14INSTRUCT_RESTART_BOT\x10\x0c\x12\x1c\n\x18INSTRUCT_UPDATE_BOT_CODE\x10\r\x12\x1a\n\x16INSTRUCT_TERMINATE_BOT\x10\x0e\x12\x12\n\x0eTASK_COMPLETED\x10\x14\x12\x19\n\x15TASK_INTERNAL_FAILURE\x10\x15\x12\x0f\n\x0bTASK_KILLED\x10\x16*\xa7\x01\n\tTaskState\x12\x1a\n\x16TASK_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x10\x12\x0b\n\x07PENDING\x10 \x12\x0b\n\x07\x45XPIRED\x10\x30\x12\r\n\tTIMED_OUT\x10@\x12\x0c\n\x08\x42OT_DIED\x10P\x12\x0c\n\x08\x43\x41NCELED\x10`\x12\r\n\tCOMPLETED\x10p\x12\x0b\n\x06KILLED\x10\x80\x01\x12\x10\n\x0bNO_RESOURCE\x10\x80\x02\x32M\n\x06\x42otAPI\x12\x43\n\x06\x45vents\x12\x1a.swarming.BotEventsRequest\x1a\x1b.swarming.BotEventsResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_BOTSTATUSTYPE = _descriptor.EnumDescriptor(
  name='BotStatusType',
  full_name='swarming.BotStatusType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOT_STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUARANTINED_BY_SERVER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUARANTINED_BY_BOT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERHEAD_MAINTENANCE_EXTERNAL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERHEAD_BOT_INTERNAL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOST_REBOOTING', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUSY', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESERVED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDLE', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=850,
  serialized_end=1073,
)
_sym_db.RegisterEnumDescriptor(_BOTSTATUSTYPE)

BotStatusType = enum_type_wrapper.EnumTypeWrapper(_BOTSTATUSTYPE)
_BOTEVENTTYPE = _descriptor.EnumDescriptor(
  name='BotEventType',
  full_name='swarming.BotEventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOT_EVENT_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_NEW_SESSION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_INTERNAL_FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_HOOK_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_HOOK_LOG', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_REBOOTING_HOST', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_SHUTDOWN', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTRUCT_IDLE', index=7, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTRUCT_START_TASK', index=8, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTRUCT_RESTART_BOT', index=9, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTRUCT_UPDATE_BOT_CODE', index=10, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTRUCT_TERMINATE_BOT', index=11, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_COMPLETED', index=12, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_INTERNAL_FAILURE', index=13, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_KILLED', index=14, number=22,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1076,
  serialized_end=1441,
)
_sym_db.RegisterEnumDescriptor(_BOTEVENTTYPE)

BotEventType = enum_type_wrapper.EnumTypeWrapper(_BOTEVENTTYPE)
_TASKSTATE = _descriptor.EnumDescriptor(
  name='TaskState',
  full_name='swarming.TaskState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TASK_STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=2, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED', index=3, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_OUT', index=4, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_DIED', index=5, number=80,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELED', index=6, number=96,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=7, number=112,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KILLED', index=8, number=128,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_RESOURCE', index=9, number=256,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1444,
  serialized_end=1611,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATE)

TaskState = enum_type_wrapper.EnumTypeWrapper(_TASKSTATE)
BOT_STATUS_UNSPECIFIED = 0
MISSING = 1
QUARANTINED_BY_SERVER = 2
QUARANTINED_BY_BOT = 3
OVERHEAD_MAINTENANCE_EXTERNAL = 4
OVERHEAD_BOT_INTERNAL = 5
HOST_REBOOTING = 6
BUSY = 7
RESERVED = 8
IDLE = 9
BOT_EVENT_TYPE_UNSPECIFIED = 0
BOT_NEW_SESSION = 1
BOT_INTERNAL_FAILURE = 2
BOT_HOOK_ERROR = 3
BOT_HOOK_LOG = 4
BOT_REBOOTING_HOST = 5
BOT_SHUTDOWN = 6
INSTRUCT_IDLE = 10
INSTRUCT_START_TASK = 11
INSTRUCT_RESTART_BOT = 12
INSTRUCT_UPDATE_BOT_CODE = 13
INSTRUCT_TERMINATE_BOT = 14
TASK_COMPLETED = 20
TASK_INTERNAL_FAILURE = 21
TASK_KILLED = 22
TASK_STATE_UNSPECIFIED = 0
RUNNING = 16
PENDING = 32
EXPIRED = 48
TIMED_OUT = 64
BOT_DIED = 80
CANCELED = 96
COMPLETED = 112
KILLED = 128
NO_RESOURCE = 256



_BOTEVENTSREQUEST = _descriptor.Descriptor(
  name='BotEventsRequest',
  full_name='swarming.BotEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bot_id', full_name='swarming.BotEventsRequest.bot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='swarming.BotEventsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='swarming.BotEventsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='swarming.BotEventsRequest.start_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='swarming.BotEventsRequest.end_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=92,
  serialized_end=259,
)


_BOTEVENTSRESPONSE = _descriptor.Descriptor(
  name='BotEventsResponse',
  full_name='swarming.BotEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='swarming.BotEventsResponse.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='swarming.BotEventsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=261,
  serialized_end=341,
)


_BOT = _descriptor.Descriptor(
  name='Bot',
  full_name='swarming.Bot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bot_id', full_name='swarming.Bot.bot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='swarming.Bot.session_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='swarming.Bot.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_msg', full_name='swarming.Bot.status_msg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_task_id', full_name='swarming.Bot.current_task_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='swarming.Bot.dimensions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='swarming.Bot.info', index=6,
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
  ],
  serialized_start=344,
  serialized_end=545,
)


_BOTINFO = _descriptor.Descriptor(
  name='BotInfo',
  full_name='swarming.BotInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw', full_name='swarming.BotInfo.raw', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='swarming.BotInfo.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_ip', full_name='swarming.BotInfo.external_ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authenticated_as', full_name='swarming.BotInfo.authenticated_as', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=547,
  serialized_end=658,
)


_BOTEVENT = _descriptor.Descriptor(
  name='BotEvent',
  full_name='swarming.BotEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_time', full_name='swarming.BotEvent.event_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bot', full_name='swarming.BotEvent.bot', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='swarming.BotEvent.event', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_msg', full_name='swarming.BotEvent.event_msg', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=661,
  serialized_end=805,
)


_DIMENSION = _descriptor.Descriptor(
  name='Dimension',
  full_name='swarming.Dimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='swarming.Dimension.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='swarming.Dimension.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=807,
  serialized_end=847,
)

_BOTEVENTSREQUEST.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BOTEVENTSREQUEST.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BOTEVENTSRESPONSE.fields_by_name['events'].message_type = _BOTEVENT
_BOT.fields_by_name['status'].enum_type = _BOTSTATUSTYPE
_BOT.fields_by_name['dimensions'].message_type = _DIMENSION
_BOT.fields_by_name['info'].message_type = _BOTINFO
_BOTINFO.fields_by_name['raw'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BOTEVENT.fields_by_name['event_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BOTEVENT.fields_by_name['bot'].message_type = _BOT
_BOTEVENT.fields_by_name['event'].enum_type = _BOTEVENTTYPE
DESCRIPTOR.message_types_by_name['BotEventsRequest'] = _BOTEVENTSREQUEST
DESCRIPTOR.message_types_by_name['BotEventsResponse'] = _BOTEVENTSRESPONSE
DESCRIPTOR.message_types_by_name['Bot'] = _BOT
DESCRIPTOR.message_types_by_name['BotInfo'] = _BOTINFO
DESCRIPTOR.message_types_by_name['BotEvent'] = _BOTEVENT
DESCRIPTOR.message_types_by_name['Dimension'] = _DIMENSION
DESCRIPTOR.enum_types_by_name['BotStatusType'] = _BOTSTATUSTYPE
DESCRIPTOR.enum_types_by_name['BotEventType'] = _BOTEVENTTYPE
DESCRIPTOR.enum_types_by_name['TaskState'] = _TASKSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BotEventsRequest = _reflection.GeneratedProtocolMessageType('BotEventsRequest', (_message.Message,), dict(
  DESCRIPTOR = _BOTEVENTSREQUEST,
  __module__ = 'swarming_pb2'
  # @@protoc_insertion_point(class_scope:swarming.BotEventsRequest)
  ))
_sym_db.RegisterMessage(BotEventsRequest)

BotEventsResponse = _reflection.GeneratedProtocolMessageType('BotEventsResponse', (_message.Message,), dict(
  DESCRIPTOR = _BOTEVENTSRESPONSE,
  __module__ = 'swarming_pb2'
  # @@protoc_insertion_point(class_scope:swarming.BotEventsResponse)
  ))
_sym_db.RegisterMessage(BotEventsResponse)

Bot = _reflection.GeneratedProtocolMessageType('Bot', (_message.Message,), dict(
  DESCRIPTOR = _BOT,
  __module__ = 'swarming_pb2'
  # @@protoc_insertion_point(class_scope:swarming.Bot)
  ))
_sym_db.RegisterMessage(Bot)

BotInfo = _reflection.GeneratedProtocolMessageType('BotInfo', (_message.Message,), dict(
  DESCRIPTOR = _BOTINFO,
  __module__ = 'swarming_pb2'
  # @@protoc_insertion_point(class_scope:swarming.BotInfo)
  ))
_sym_db.RegisterMessage(BotInfo)

BotEvent = _reflection.GeneratedProtocolMessageType('BotEvent', (_message.Message,), dict(
  DESCRIPTOR = _BOTEVENT,
  __module__ = 'swarming_pb2'
  # @@protoc_insertion_point(class_scope:swarming.BotEvent)
  ))
_sym_db.RegisterMessage(BotEvent)

Dimension = _reflection.GeneratedProtocolMessageType('Dimension', (_message.Message,), dict(
  DESCRIPTOR = _DIMENSION,
  __module__ = 'swarming_pb2'
  # @@protoc_insertion_point(class_scope:swarming.Dimension)
  ))
_sym_db.RegisterMessage(Dimension)



_BOTAPI = _descriptor.ServiceDescriptor(
  name='BotAPI',
  full_name='swarming.BotAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1613,
  serialized_end=1690,
  methods=[
  _descriptor.MethodDescriptor(
    name='Events',
    full_name='swarming.BotAPI.Events',
    index=0,
    containing_service=None,
    input_type=_BOTEVENTSREQUEST,
    output_type=_BOTEVENTSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOTAPI)

DESCRIPTOR.services_by_name['BotAPI'] = _BOTAPI

# @@protoc_insertion_point(module_scope)