# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tle.proto

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
  name='tle.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\ttle.proto\"V\n\x07TleList\x12\x19\n\x03tle\x18\x01 \x03(\x0b\x32\x0c.TleList.TLE\x1a\x30\n\x03TLE\x12\x16\n\x0e\x65pochTimestamp\x18\x01 \x01(\t\x12\x11\n\ttleString\x18\x02 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TLELIST_TLE = _descriptor.Descriptor(
  name='TLE',
  full_name='TleList.TLE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='epochTimestamp', full_name='TleList.TLE.epochTimestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tleString', full_name='TleList.TLE.tleString', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=51,
  serialized_end=99,
)

_TLELIST = _descriptor.Descriptor(
  name='TleList',
  full_name='TleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tle', full_name='TleList.tle', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TLELIST_TLE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=99,
)

_TLELIST_TLE.containing_type = _TLELIST
_TLELIST.fields_by_name['tle'].message_type = _TLELIST_TLE
DESCRIPTOR.message_types_by_name['TleList'] = _TLELIST

TleList = _reflection.GeneratedProtocolMessageType('TleList', (_message.Message,), dict(

  TLE = _reflection.GeneratedProtocolMessageType('TLE', (_message.Message,), dict(
    DESCRIPTOR = _TLELIST_TLE,
    __module__ = 'tle_pb2'
    # @@protoc_insertion_point(class_scope:TleList.TLE)
    ))
  ,
  DESCRIPTOR = _TLELIST,
  __module__ = 'tle_pb2'
  # @@protoc_insertion_point(class_scope:TleList)
  ))
_sym_db.RegisterMessage(TleList)
_sym_db.RegisterMessage(TleList.TLE)


# @@protoc_insertion_point(module_scope)
