# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tasks.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tasks.proto',
  package='swarming',
  syntax='proto3',
  serialized_pb=_b('\n\x0btasks.proto\x12\x08swarming\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb0\x01\n\x08TaskSpec\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\x12#\n\x06slices\x18\x03 \x03(\x0b\x32\x13.swarming.SliceSpec\x12\"\n\x05state\x18\x04 \x01(\x0e\x32\x13.swarming.TaskState\x12\x0e\n\x06\x62ot_id\x18\x05 \x01(\t\x12\x31\n\renqueued_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1f\n\tSliceSpec\x12\x12\n\ndimensions\x18\x01 \x03(\t*\x98\x01\n\tTaskState\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07RUNNING\x10\x10\x12\x0b\n\x07PENDING\x10 \x12\x0b\n\x07\x45XPIRED\x10\x30\x12\r\n\tTIMED_OUT\x10@\x12\x0c\n\x08\x42OT_DIED\x10P\x12\x0c\n\x08\x43\x41NCELED\x10`\x12\r\n\tCOMPLETED\x10p\x12\x0b\n\x06KILLED\x10\x80\x01\x12\x10\n\x0bNO_RESOURCE\x10\x80\x02\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TASKSTATE = _descriptor.EnumDescriptor(
  name='TaskState',
  full_name='swarming.TaskState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=2, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED', index=3, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_OUT', index=4, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT_DIED', index=5, number=80,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELED', index=6, number=96,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=7, number=112,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KILLED', index=8, number=128,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_RESOURCE', index=9, number=256,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=271,
  serialized_end=423,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATE)

TaskState = enum_type_wrapper.EnumTypeWrapper(_TASKSTATE)
INVALID = 0
RUNNING = 16
PENDING = 32
EXPIRED = 48
TIMED_OUT = 64
BOT_DIED = 80
CANCELED = 96
COMPLETED = 112
KILLED = 128
NO_RESOURCE = 256



_TASKSPEC = _descriptor.Descriptor(
  name='TaskSpec',
  full_name='swarming.TaskSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='swarming.TaskSpec.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='swarming.TaskSpec.tags', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slices', full_name='swarming.TaskSpec.slices', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='swarming.TaskSpec.state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bot_id', full_name='swarming.TaskSpec.bot_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enqueued_time', full_name='swarming.TaskSpec.enqueued_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=235,
)


_SLICESPEC = _descriptor.Descriptor(
  name='SliceSpec',
  full_name='swarming.SliceSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='swarming.SliceSpec.dimensions', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=268,
)

_TASKSPEC.fields_by_name['slices'].message_type = _SLICESPEC
_TASKSPEC.fields_by_name['state'].enum_type = _TASKSTATE
_TASKSPEC.fields_by_name['enqueued_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['TaskSpec'] = _TASKSPEC
DESCRIPTOR.message_types_by_name['SliceSpec'] = _SLICESPEC
DESCRIPTOR.enum_types_by_name['TaskState'] = _TASKSTATE

TaskSpec = _reflection.GeneratedProtocolMessageType('TaskSpec', (_message.Message,), dict(
  DESCRIPTOR = _TASKSPEC,
  __module__ = 'tasks_pb2'
  # @@protoc_insertion_point(class_scope:swarming.TaskSpec)
  ))
_sym_db.RegisterMessage(TaskSpec)

SliceSpec = _reflection.GeneratedProtocolMessageType('SliceSpec', (_message.Message,), dict(
  DESCRIPTOR = _SLICESPEC,
  __module__ = 'tasks_pb2'
  # @@protoc_insertion_point(class_scope:swarming.SliceSpec)
  ))
_sym_db.RegisterMessage(SliceSpec)


# @@protoc_insertion_point(module_scope)