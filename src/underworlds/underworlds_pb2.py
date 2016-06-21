# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: underworlds.proto

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




DESCRIPTOR = _descriptor.FileDescriptor(
  name='underworlds.proto',
  package='underworlds',
  syntax='proto3',
  serialized_pb=_b('\n\x11underworlds.proto\x12\x0bunderworlds\"\x14\n\x06\x43lient\x12\n\n\x02id\x18\x01 \x01(\t\"\xa5\x01\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12#\n\x04type\x18\x03 \x01(\x0e\x32\x15.underworlds.NodeType\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12\x10\n\x08\x63hildren\x18\x05 \x03(\t\x12\x16\n\x0etransformation\x18\x06 \x03(\x02\x12\x13\n\x0blast_update\x18\x08 \x01(\x02\x12\x0f\n\x07physics\x18\x10 \x01(\x08\"\x14\n\x05Nodes\x12\x0b\n\x03ids\x18\x01 \x03(\t\"(\n\x07\x43ontext\x12\x0e\n\x06\x63lient\x18\x01 \x01(\t\x12\r\n\x05world\x18\x02 \x01(\t\"\x14\n\x04Name\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x14\n\x04Size\x12\x0c\n\x04size\x18\x01 \x01(\x05\"B\n\rNodeInContext\x12%\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x14.underworlds.Context\x12\n\n\x02id\x18\x02 \x01(\t\"G\n\x0cInvalidation\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.underworlds.InvalidationType\x12\n\n\x02id\x18\x02 \x01(\t*;\n\x08NodeType\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06\x45NTITY\x10\x01\x12\x08\n\x04MESH\x10\x02\x12\n\n\x06\x43\x41MERA\x10\x03*<\n\x10InvalidationType\x12\x07\n\x03NOP\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x32\xf3\x02\n\x0bUnderworlds\x12\x30\n\x04helo\x12\x11.underworlds.Name\x1a\x13.underworlds.Client\"\x00\x12\x38\n\x0bgetNodesLen\x12\x14.underworlds.Context\x1a\x11.underworlds.Size\"\x00\x12\x39\n\x0bgetNodesIds\x12\x14.underworlds.Context\x1a\x12.underworlds.Nodes\"\x00\x12\x38\n\x0bgetRootNode\x12\x14.underworlds.Context\x1a\x11.underworlds.Node\"\x00\x12:\n\x07getNode\x12\x1a.underworlds.NodeInContext\x1a\x11.underworlds.Node\"\x00\x12G\n\x10getInvalidations\x12\x14.underworlds.Context\x1a\x19.underworlds.Invalidation\"\x00\x30\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_NODETYPE = _descriptor.EnumDescriptor(
  name='NodeType',
  full_name='underworlds.NodeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTITY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESH', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMERA', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=473,
  serialized_end=532,
)
_sym_db.RegisterEnumDescriptor(_NODETYPE)

NodeType = enum_type_wrapper.EnumTypeWrapper(_NODETYPE)
_INVALIDATIONTYPE = _descriptor.EnumDescriptor(
  name='InvalidationType',
  full_name='underworlds.InvalidationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=534,
  serialized_end=594,
)
_sym_db.RegisterEnumDescriptor(_INVALIDATIONTYPE)

InvalidationType = enum_type_wrapper.EnumTypeWrapper(_INVALIDATIONTYPE)
UNDEFINED = 0
ENTITY = 1
MESH = 2
CAMERA = 3
NOP = 0
NEW = 1
UPDATE = 2
DELETE = 3



_CLIENT = _descriptor.Descriptor(
  name='Client',
  full_name='underworlds.Client',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='underworlds.Client.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=34,
  serialized_end=54,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='underworlds.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='underworlds.Node.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='underworlds.Node.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='underworlds.Node.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent', full_name='underworlds.Node.parent', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='children', full_name='underworlds.Node.children', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transformation', full_name='underworlds.Node.transformation', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_update', full_name='underworlds.Node.last_update', index=6,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='physics', full_name='underworlds.Node.physics', index=7,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=57,
  serialized_end=222,
)


_NODES = _descriptor.Descriptor(
  name='Nodes',
  full_name='underworlds.Nodes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='underworlds.Nodes.ids', index=0,
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
  serialized_start=224,
  serialized_end=244,
)


_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='underworlds.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client', full_name='underworlds.Context.client', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='world', full_name='underworlds.Context.world', index=1,
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
  serialized_start=246,
  serialized_end=286,
)


_NAME = _descriptor.Descriptor(
  name='Name',
  full_name='underworlds.Name',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='underworlds.Name.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=288,
  serialized_end=308,
)


_SIZE = _descriptor.Descriptor(
  name='Size',
  full_name='underworlds.Size',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='underworlds.Size.size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=310,
  serialized_end=330,
)


_NODEINCONTEXT = _descriptor.Descriptor(
  name='NodeInContext',
  full_name='underworlds.NodeInContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='underworlds.NodeInContext.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='underworlds.NodeInContext.id', index=1,
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
  serialized_start=332,
  serialized_end=398,
)


_INVALIDATION = _descriptor.Descriptor(
  name='Invalidation',
  full_name='underworlds.Invalidation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='underworlds.Invalidation.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='underworlds.Invalidation.id', index=1,
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
  serialized_start=400,
  serialized_end=471,
)

_NODE.fields_by_name['type'].enum_type = _NODETYPE
_NODEINCONTEXT.fields_by_name['context'].message_type = _CONTEXT
_INVALIDATION.fields_by_name['type'].enum_type = _INVALIDATIONTYPE
DESCRIPTOR.message_types_by_name['Client'] = _CLIENT
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Nodes'] = _NODES
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
DESCRIPTOR.message_types_by_name['Name'] = _NAME
DESCRIPTOR.message_types_by_name['Size'] = _SIZE
DESCRIPTOR.message_types_by_name['NodeInContext'] = _NODEINCONTEXT
DESCRIPTOR.message_types_by_name['Invalidation'] = _INVALIDATION
DESCRIPTOR.enum_types_by_name['NodeType'] = _NODETYPE
DESCRIPTOR.enum_types_by_name['InvalidationType'] = _INVALIDATIONTYPE

Client = _reflection.GeneratedProtocolMessageType('Client', (_message.Message,), dict(
  DESCRIPTOR = _CLIENT,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Client)
  ))
_sym_db.RegisterMessage(Client)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Node)
  ))
_sym_db.RegisterMessage(Node)

Nodes = _reflection.GeneratedProtocolMessageType('Nodes', (_message.Message,), dict(
  DESCRIPTOR = _NODES,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Nodes)
  ))
_sym_db.RegisterMessage(Nodes)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Context)
  ))
_sym_db.RegisterMessage(Context)

Name = _reflection.GeneratedProtocolMessageType('Name', (_message.Message,), dict(
  DESCRIPTOR = _NAME,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Name)
  ))
_sym_db.RegisterMessage(Name)

Size = _reflection.GeneratedProtocolMessageType('Size', (_message.Message,), dict(
  DESCRIPTOR = _SIZE,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Size)
  ))
_sym_db.RegisterMessage(Size)

NodeInContext = _reflection.GeneratedProtocolMessageType('NodeInContext', (_message.Message,), dict(
  DESCRIPTOR = _NODEINCONTEXT,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.NodeInContext)
  ))
_sym_db.RegisterMessage(NodeInContext)

Invalidation = _reflection.GeneratedProtocolMessageType('Invalidation', (_message.Message,), dict(
  DESCRIPTOR = _INVALIDATION,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Invalidation)
  ))
_sym_db.RegisterMessage(Invalidation)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class UnderworldsStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.helo = channel.unary_unary(
        '/underworlds.Underworlds/helo',
        request_serializer=Name.SerializeToString,
        response_deserializer=Client.FromString,
        )
    self.getNodesLen = channel.unary_unary(
        '/underworlds.Underworlds/getNodesLen',
        request_serializer=Context.SerializeToString,
        response_deserializer=Size.FromString,
        )
    self.getNodesIds = channel.unary_unary(
        '/underworlds.Underworlds/getNodesIds',
        request_serializer=Context.SerializeToString,
        response_deserializer=Nodes.FromString,
        )
    self.getRootNode = channel.unary_unary(
        '/underworlds.Underworlds/getRootNode',
        request_serializer=Context.SerializeToString,
        response_deserializer=Node.FromString,
        )
    self.getNode = channel.unary_unary(
        '/underworlds.Underworlds/getNode',
        request_serializer=NodeInContext.SerializeToString,
        response_deserializer=Node.FromString,
        )
    self.getInvalidations = channel.unary_stream(
        '/underworlds.Underworlds/getInvalidations',
        request_serializer=Context.SerializeToString,
        response_deserializer=Invalidation.FromString,
        )


class UnderworldsServicer(object):

  def helo(self, request, context):
    """Establish the connection to the server, setting a human-friendly name for
    the client.
    The server returns a unique client ID that must be used in every subsequent
    request to the server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getNodesLen(self, request, context):
    """Returns the number of nodes in a given world.

    Accepts a context (client ID and world) and returns the number of existing nodes.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getNodesIds(self, request, context):
    """Returns the list of node IDs present in the given world
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getRootNode(self, request, context):
    """Returns the root node ID of the given world
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getNode(self, request, context):
    """Returns a node from its ID in the given world
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getInvalidations(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UnderworldsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'helo': grpc.unary_unary_rpc_method_handler(
          servicer.helo,
          request_deserializer=Name.FromString,
          response_serializer=Client.SerializeToString,
      ),
      'getNodesLen': grpc.unary_unary_rpc_method_handler(
          servicer.getNodesLen,
          request_deserializer=Context.FromString,
          response_serializer=Size.SerializeToString,
      ),
      'getNodesIds': grpc.unary_unary_rpc_method_handler(
          servicer.getNodesIds,
          request_deserializer=Context.FromString,
          response_serializer=Nodes.SerializeToString,
      ),
      'getRootNode': grpc.unary_unary_rpc_method_handler(
          servicer.getRootNode,
          request_deserializer=Context.FromString,
          response_serializer=Node.SerializeToString,
      ),
      'getNode': grpc.unary_unary_rpc_method_handler(
          servicer.getNode,
          request_deserializer=NodeInContext.FromString,
          response_serializer=Node.SerializeToString,
      ),
      'getInvalidations': grpc.unary_stream_rpc_method_handler(
          servicer.getInvalidations,
          request_deserializer=Context.FromString,
          response_serializer=Invalidation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'underworlds.Underworlds', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaUnderworldsServicer(object):
  def helo(self, request, context):
    """Establish the connection to the server, setting a human-friendly name for
    the client.
    The server returns a unique client ID that must be used in every subsequent
    request to the server.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getNodesLen(self, request, context):
    """Returns the number of nodes in a given world.

    Accepts a context (client ID and world) and returns the number of existing nodes.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getNodesIds(self, request, context):
    """Returns the list of node IDs present in the given world
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getRootNode(self, request, context):
    """Returns the root node ID of the given world
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getNode(self, request, context):
    """Returns a node from its ID in the given world
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getInvalidations(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaUnderworldsStub(object):
  def helo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Establish the connection to the server, setting a human-friendly name for
    the client.
    The server returns a unique client ID that must be used in every subsequent
    request to the server.
    """
    raise NotImplementedError()
  helo.future = None
  def getNodesLen(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Returns the number of nodes in a given world.

    Accepts a context (client ID and world) and returns the number of existing nodes.
    """
    raise NotImplementedError()
  getNodesLen.future = None
  def getNodesIds(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Returns the list of node IDs present in the given world
    """
    raise NotImplementedError()
  getNodesIds.future = None
  def getRootNode(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Returns the root node ID of the given world
    """
    raise NotImplementedError()
  getRootNode.future = None
  def getNode(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Returns a node from its ID in the given world
    """
    raise NotImplementedError()
  getNode.future = None
  def getInvalidations(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()


def beta_create_Underworlds_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('underworlds.Underworlds', 'getInvalidations'): Context.FromString,
    ('underworlds.Underworlds', 'getNode'): NodeInContext.FromString,
    ('underworlds.Underworlds', 'getNodesIds'): Context.FromString,
    ('underworlds.Underworlds', 'getNodesLen'): Context.FromString,
    ('underworlds.Underworlds', 'getRootNode'): Context.FromString,
    ('underworlds.Underworlds', 'helo'): Name.FromString,
  }
  response_serializers = {
    ('underworlds.Underworlds', 'getInvalidations'): Invalidation.SerializeToString,
    ('underworlds.Underworlds', 'getNode'): Node.SerializeToString,
    ('underworlds.Underworlds', 'getNodesIds'): Nodes.SerializeToString,
    ('underworlds.Underworlds', 'getNodesLen'): Size.SerializeToString,
    ('underworlds.Underworlds', 'getRootNode'): Node.SerializeToString,
    ('underworlds.Underworlds', 'helo'): Client.SerializeToString,
  }
  method_implementations = {
    ('underworlds.Underworlds', 'getInvalidations'): face_utilities.unary_stream_inline(servicer.getInvalidations),
    ('underworlds.Underworlds', 'getNode'): face_utilities.unary_unary_inline(servicer.getNode),
    ('underworlds.Underworlds', 'getNodesIds'): face_utilities.unary_unary_inline(servicer.getNodesIds),
    ('underworlds.Underworlds', 'getNodesLen'): face_utilities.unary_unary_inline(servicer.getNodesLen),
    ('underworlds.Underworlds', 'getRootNode'): face_utilities.unary_unary_inline(servicer.getRootNode),
    ('underworlds.Underworlds', 'helo'): face_utilities.unary_unary_inline(servicer.helo),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_Underworlds_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('underworlds.Underworlds', 'getInvalidations'): Context.SerializeToString,
    ('underworlds.Underworlds', 'getNode'): NodeInContext.SerializeToString,
    ('underworlds.Underworlds', 'getNodesIds'): Context.SerializeToString,
    ('underworlds.Underworlds', 'getNodesLen'): Context.SerializeToString,
    ('underworlds.Underworlds', 'getRootNode'): Context.SerializeToString,
    ('underworlds.Underworlds', 'helo'): Name.SerializeToString,
  }
  response_deserializers = {
    ('underworlds.Underworlds', 'getInvalidations'): Invalidation.FromString,
    ('underworlds.Underworlds', 'getNode'): Node.FromString,
    ('underworlds.Underworlds', 'getNodesIds'): Nodes.FromString,
    ('underworlds.Underworlds', 'getNodesLen'): Size.FromString,
    ('underworlds.Underworlds', 'getRootNode'): Node.FromString,
    ('underworlds.Underworlds', 'helo'): Client.FromString,
  }
  cardinalities = {
    'getInvalidations': cardinality.Cardinality.UNARY_STREAM,
    'getNode': cardinality.Cardinality.UNARY_UNARY,
    'getNodesIds': cardinality.Cardinality.UNARY_UNARY,
    'getNodesLen': cardinality.Cardinality.UNARY_UNARY,
    'getRootNode': cardinality.Cardinality.UNARY_UNARY,
    'helo': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'underworlds.Underworlds', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)