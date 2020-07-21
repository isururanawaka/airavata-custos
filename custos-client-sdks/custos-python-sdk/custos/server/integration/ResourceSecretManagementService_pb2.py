# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ResourceSecretManagementService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
import custos.server.core.ResourceSecretService_pb2 as ResourceSecretService__pb2
import custos.server.core.IdentityService_pb2 as IdentityService__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ResourceSecretManagementService.proto',
  package='org.apache.custos.resource.secret.management.service',
  syntax='proto3',
  serialized_options=b'P\001',
  serialized_pb=b'\n%ResourceSecretManagementService.proto\x12\x34org.apache.custos.resource.secret.management.service\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1bResourceSecretService.proto\x1a\x15IdentityService.proto2\xf4\x02\n\x1fResourceSecretManagementService\x12\xb6\x01\n\tgetSecret\x12;.org.apache.custos.resource.secret.service.GetSecretRequest\x1a\x39.org.apache.custos.resource.secret.service.SecretMetadata\"1\x82\xd3\xe4\x93\x02+\x12)/resource-secret-management/v1.0.0/secret\x12\x97\x01\n\x07getJWKS\x12\x32.org.apache.custos.identity.service.GetJWKSRequest\x1a\x17.google.protobuf.Struct\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/resource-secret-management/v1.0.0/openid-connect/certsB\x02P\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,ResourceSecretService__pb2.DESCRIPTOR,IdentityService__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_RESOURCESECRETMANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
  name='ResourceSecretManagementService',
  full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=237,
  serialized_end=609,
  methods=[
  _descriptor.MethodDescriptor(
    name='getSecret',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.getSecret',
    index=0,
    containing_service=None,
    input_type=ResourceSecretService__pb2._GETSECRETREQUEST,
    output_type=ResourceSecretService__pb2._SECRETMETADATA,
    serialized_options=b'\202\323\344\223\002+\022)/resource-secret-management/v1.0.0/secret',
  ),
  _descriptor.MethodDescriptor(
    name='getJWKS',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.getJWKS',
    index=1,
    containing_service=None,
    input_type=IdentityService__pb2._GETJWKSREQUEST,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=b'\202\323\344\223\0029\0227/resource-secret-management/v1.0.0/openid-connect/certs',
  ),
])
_sym_db.RegisterServiceDescriptor(_RESOURCESECRETMANAGEMENTSERVICE)

DESCRIPTOR.services_by_name['ResourceSecretManagementService'] = _RESOURCESECRETMANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)