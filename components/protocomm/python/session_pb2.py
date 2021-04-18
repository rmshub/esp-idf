# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sec0_pb2 as sec0__pb2
import sec1_pb2 as sec1__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='session.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rsession.proto\x1a\nsec0.proto\x1a\nsec1.proto\"v\n\x0bSessionData\x12\"\n\x07sec_ver\x18\x02 \x01(\x0e\x32\x11.SecSchemeVersion\x12\x1c\n\x04sec0\x18\n \x01(\x0b\x32\x0c.Sec0PayloadH\x00\x12\x1c\n\x04sec1\x18\x0b \x01(\x0b\x32\x0c.Sec1PayloadH\x00\x42\x07\n\x05proto*2\n\x10SecSchemeVersion\x12\x0e\n\nSecScheme0\x10\x00\x12\x0e\n\nSecScheme1\x10\x01\x62\x06proto3')
  ,
  dependencies=[sec0__pb2.DESCRIPTOR,sec1__pb2.DESCRIPTOR,])

_SECSCHEMEVERSION = _descriptor.EnumDescriptor(
  name='SecSchemeVersion',
  full_name='SecSchemeVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SecScheme0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SecScheme1', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=161,
  serialized_end=211,
)
_sym_db.RegisterEnumDescriptor(_SECSCHEMEVERSION)

SecSchemeVersion = enum_type_wrapper.EnumTypeWrapper(_SECSCHEMEVERSION)
SecScheme0 = 0
SecScheme1 = 1



_SESSIONDATA = _descriptor.Descriptor(
  name='SessionData',
  full_name='SessionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sec_ver', full_name='SessionData.sec_ver', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sec0', full_name='SessionData.sec0', index=1,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sec1', full_name='SessionData.sec1', index=2,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='proto', full_name='SessionData.proto',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=41,
  serialized_end=159,
)

_SESSIONDATA.fields_by_name['sec_ver'].enum_type = _SECSCHEMEVERSION
_SESSIONDATA.fields_by_name['sec0'].message_type = sec0__pb2._SEC0PAYLOAD
_SESSIONDATA.fields_by_name['sec1'].message_type = sec1__pb2._SEC1PAYLOAD
_SESSIONDATA.oneofs_by_name['proto'].fields.append(
  _SESSIONDATA.fields_by_name['sec0'])
_SESSIONDATA.fields_by_name['sec0'].containing_oneof = _SESSIONDATA.oneofs_by_name['proto']
_SESSIONDATA.oneofs_by_name['proto'].fields.append(
  _SESSIONDATA.fields_by_name['sec1'])
_SESSIONDATA.fields_by_name['sec1'].containing_oneof = _SESSIONDATA.oneofs_by_name['proto']
DESCRIPTOR.message_types_by_name['SessionData'] = _SESSIONDATA
DESCRIPTOR.enum_types_by_name['SecSchemeVersion'] = _SECSCHEMEVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionData = _reflection.GeneratedProtocolMessageType('SessionData', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONDATA,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:SessionData)
  ))
_sym_db.RegisterMessage(SessionData)


# @@protoc_insertion_point(module_scope)
