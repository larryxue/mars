# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mars/serialize/protos/tensor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mars.serialize.protos import value_pb2 as mars_dot_serialize_dot_protos_dot_value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mars/serialize/protos/tensor.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"mars/serialize/protos/tensor.proto\x1a!mars/serialize/protos/value.proto\"\xb3\x01\n\x0eTensorChunkDef\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\x05index\x18\x02 \x03(\rB\x02\x10\x01\x12\r\n\x05shape\x18\x03 \x03(\x03\x12\x12\n\x02op\x18\x04 \x01(\x0b\x32\x06.Value\x12\x0e\n\x06\x63\x61\x63hed\x18\x05 \x01(\x08\x12\x15\n\x05\x64type\x18\x06 \x01(\x0b\x32\x06.Value\x12\x1c\n\x0c\x65xtra_params\x18\x08 \x01(\x0b\x32\x06.Value\x12\n\n\x02id\x18\t \x01(\t\x12\r\n\x05order\x18\n \x01(\t\"\xc5\x01\n\tTensorDef\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05shape\x18\x02 \x03(\x03\x12\x15\n\x05\x64type\x18\x03 \x01(\x0b\x32\x06.Value\x12\x12\n\x02op\x18\x04 \x01(\x0b\x32\x06.Value\x12\x17\n\x07nsplits\x18\x05 \x01(\x0b\x32\x06.Value\x12\x1f\n\x06\x63hunks\x18\x06 \x03(\x0b\x32\x0f.TensorChunkDef\x12\x1c\n\x0c\x65xtra_params\x18\x07 \x01(\x0b\x32\x06.Value\x12\n\n\x02id\x18\x08 \x01(\t\x12\r\n\x05order\x18\t \x01(\tb\x06proto3')
  ,
  dependencies=[mars_dot_serialize_dot_protos_dot_value__pb2.DESCRIPTOR,])




_TENSORCHUNKDEF = _descriptor.Descriptor(
  name='TensorChunkDef',
  full_name='TensorChunkDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='TensorChunkDef.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='TensorChunkDef.index', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='TensorChunkDef.shape', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='TensorChunkDef.op', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cached', full_name='TensorChunkDef.cached', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='TensorChunkDef.dtype', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra_params', full_name='TensorChunkDef.extra_params', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='TensorChunkDef.id', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='TensorChunkDef.order', index=8,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=74,
  serialized_end=253,
)


_TENSORDEF = _descriptor.Descriptor(
  name='TensorDef',
  full_name='TensorDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='TensorDef.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='TensorDef.shape', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='TensorDef.dtype', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='TensorDef.op', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nsplits', full_name='TensorDef.nsplits', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='TensorDef.chunks', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra_params', full_name='TensorDef.extra_params', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='TensorDef.id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='TensorDef.order', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=256,
  serialized_end=453,
)

_TENSORCHUNKDEF.fields_by_name['op'].message_type = mars_dot_serialize_dot_protos_dot_value__pb2._VALUE
_TENSORCHUNKDEF.fields_by_name['dtype'].message_type = mars_dot_serialize_dot_protos_dot_value__pb2._VALUE
_TENSORCHUNKDEF.fields_by_name['extra_params'].message_type = mars_dot_serialize_dot_protos_dot_value__pb2._VALUE
_TENSORDEF.fields_by_name['dtype'].message_type = mars_dot_serialize_dot_protos_dot_value__pb2._VALUE
_TENSORDEF.fields_by_name['op'].message_type = mars_dot_serialize_dot_protos_dot_value__pb2._VALUE
_TENSORDEF.fields_by_name['nsplits'].message_type = mars_dot_serialize_dot_protos_dot_value__pb2._VALUE
_TENSORDEF.fields_by_name['chunks'].message_type = _TENSORCHUNKDEF
_TENSORDEF.fields_by_name['extra_params'].message_type = mars_dot_serialize_dot_protos_dot_value__pb2._VALUE
DESCRIPTOR.message_types_by_name['TensorChunkDef'] = _TENSORCHUNKDEF
DESCRIPTOR.message_types_by_name['TensorDef'] = _TENSORDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorChunkDef = _reflection.GeneratedProtocolMessageType('TensorChunkDef', (_message.Message,), {
  'DESCRIPTOR' : _TENSORCHUNKDEF,
  '__module__' : 'mars.serialize.protos.tensor_pb2'
  # @@protoc_insertion_point(class_scope:TensorChunkDef)
  })
_sym_db.RegisterMessage(TensorChunkDef)

TensorDef = _reflection.GeneratedProtocolMessageType('TensorDef', (_message.Message,), {
  'DESCRIPTOR' : _TENSORDEF,
  '__module__' : 'mars.serialize.protos.tensor_pb2'
  # @@protoc_insertion_point(class_scope:TensorDef)
  })
_sym_db.RegisterMessage(TensorDef)


_TENSORCHUNKDEF.fields_by_name['index']._options = None
# @@protoc_insertion_point(module_scope)
