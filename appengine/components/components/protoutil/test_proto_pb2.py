# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_proto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_proto.proto',
  package='multiline_proto',
  syntax='proto3',
  serialized_pb=_b('\n\x10test_proto.proto\x12\x0fmultiline_proto\"\x82\x01\n\x03Msg\x12\x0b\n\x03num\x18\x01 \x01(\x05\x12\x0c\n\x04nums\x18\x02 \x03(\x05\x12\x0b\n\x03str\x18\x03 \x01(\t\x12\x0c\n\x04strs\x18\x04 \x03(\t\x12!\n\x03msg\x18\x05 \x01(\x0b\x32\x14.multiline_proto.Msg\x12\"\n\x04msgs\x18\x06 \x03(\x0b\x32\x14.multiline_proto.Msgb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='multiline_proto.Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='multiline_proto.Msg.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nums', full_name='multiline_proto.Msg.nums', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str', full_name='multiline_proto.Msg.str', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strs', full_name='multiline_proto.Msg.strs', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='multiline_proto.Msg.msg', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msgs', full_name='multiline_proto.Msg.msgs', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=38,
  serialized_end=168,
)

_MSG.fields_by_name['msg'].message_type = _MSG
_MSG.fields_by_name['msgs'].message_type = _MSG
DESCRIPTOR.message_types_by_name['Msg'] = _MSG

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), dict(
  DESCRIPTOR = _MSG,
  __module__ = 'test_proto_pb2'
  # @@protoc_insertion_point(class_scope:multiline_proto.Msg)
  ))
_sym_db.RegisterMessage(Msg)


# @@protoc_insertion_point(module_scope)