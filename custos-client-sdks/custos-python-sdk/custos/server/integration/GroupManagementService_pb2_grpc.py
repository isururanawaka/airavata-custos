# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import custos.server.core.IamAdminService_pb2 as IamAdminService__pb2
import custos.server.core.UserProfileService_pb2 as UserProfileService__pb2


class GroupManagementServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createGroups = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/createGroups',
                request_serializer=IamAdminService__pb2.GroupsRequest.SerializeToString,
                response_deserializer=IamAdminService__pb2.GroupsResponse.FromString,
                )
        self.updateGroup = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/updateGroup',
                request_serializer=IamAdminService__pb2.GroupRequest.SerializeToString,
                response_deserializer=IamAdminService__pb2.GroupRepresentation.FromString,
                )
        self.deleteGroup = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/deleteGroup',
                request_serializer=IamAdminService__pb2.GroupRequest.SerializeToString,
                response_deserializer=IamAdminService__pb2.OperationStatus.FromString,
                )
        self.findGroup = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/findGroup',
                request_serializer=IamAdminService__pb2.GroupRequest.SerializeToString,
                response_deserializer=IamAdminService__pb2.GroupRepresentation.FromString,
                )
        self.getAllGroups = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/getAllGroups',
                request_serializer=IamAdminService__pb2.GroupRequest.SerializeToString,
                response_deserializer=IamAdminService__pb2.GroupsResponse.FromString,
                )
        self.addUserToGroup = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/addUserToGroup',
                request_serializer=IamAdminService__pb2.UserGroupMappingRequest.SerializeToString,
                response_deserializer=IamAdminService__pb2.OperationStatus.FromString,
                )
        self.removeUserFromGroup = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/removeUserFromGroup',
                request_serializer=IamAdminService__pb2.UserGroupMappingRequest.SerializeToString,
                response_deserializer=IamAdminService__pb2.OperationStatus.FromString,
                )
        self.addChildGroupToParentGroup = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/addChildGroupToParentGroup',
                request_serializer=UserProfileService__pb2.GroupToGroupMembership.SerializeToString,
                response_deserializer=IamAdminService__pb2.OperationStatus.FromString,
                )
        self.removeChildGroupFromParentGroup = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/removeChildGroupFromParentGroup',
                request_serializer=UserProfileService__pb2.GroupToGroupMembership.SerializeToString,
                response_deserializer=IamAdminService__pb2.OperationStatus.FromString,
                )
        self.getAllGroupsOfUser = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/getAllGroupsOfUser',
                request_serializer=UserProfileService__pb2.UserProfileRequest.SerializeToString,
                response_deserializer=UserProfileService__pb2.GetAllGroupsResponse.FromString,
                )
        self.getAllParentGroupsOfGroup = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/getAllParentGroupsOfGroup',
                request_serializer=UserProfileService__pb2.GroupRequest.SerializeToString,
                response_deserializer=UserProfileService__pb2.GetAllGroupsResponse.FromString,
                )
        self.getAllChildUsers = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/getAllChildUsers',
                request_serializer=UserProfileService__pb2.GroupRequest.SerializeToString,
                response_deserializer=UserProfileService__pb2.GetAllUserProfilesResponse.FromString,
                )
        self.getAllChildGroups = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/getAllChildGroups',
                request_serializer=UserProfileService__pb2.GroupRequest.SerializeToString,
                response_deserializer=UserProfileService__pb2.GetAllGroupsResponse.FromString,
                )
        self.changeUserMembershipType = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/changeUserMembershipType',
                request_serializer=UserProfileService__pb2.GroupMembership.SerializeToString,
                response_deserializer=IamAdminService__pb2.OperationStatus.FromString,
                )
        self.hasAccess = channel.unary_unary(
                '/org.apache.custos.group.management.service.GroupManagementService/hasAccess',
                request_serializer=UserProfileService__pb2.GroupMembership.SerializeToString,
                response_deserializer=IamAdminService__pb2.OperationStatus.FromString,
                )


class GroupManagementServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createGroups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def findGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAllGroups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addUserToGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def removeUserFromGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addChildGroupToParentGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def removeChildGroupFromParentGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAllGroupsOfUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAllParentGroupsOfGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAllChildUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAllChildGroups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def changeUserMembershipType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def hasAccess(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GroupManagementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.createGroups,
                    request_deserializer=IamAdminService__pb2.GroupsRequest.FromString,
                    response_serializer=IamAdminService__pb2.GroupsResponse.SerializeToString,
            ),
            'updateGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.updateGroup,
                    request_deserializer=IamAdminService__pb2.GroupRequest.FromString,
                    response_serializer=IamAdminService__pb2.GroupRepresentation.SerializeToString,
            ),
            'deleteGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteGroup,
                    request_deserializer=IamAdminService__pb2.GroupRequest.FromString,
                    response_serializer=IamAdminService__pb2.OperationStatus.SerializeToString,
            ),
            'findGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.findGroup,
                    request_deserializer=IamAdminService__pb2.GroupRequest.FromString,
                    response_serializer=IamAdminService__pb2.GroupRepresentation.SerializeToString,
            ),
            'getAllGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.getAllGroups,
                    request_deserializer=IamAdminService__pb2.GroupRequest.FromString,
                    response_serializer=IamAdminService__pb2.GroupsResponse.SerializeToString,
            ),
            'addUserToGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.addUserToGroup,
                    request_deserializer=IamAdminService__pb2.UserGroupMappingRequest.FromString,
                    response_serializer=IamAdminService__pb2.OperationStatus.SerializeToString,
            ),
            'removeUserFromGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.removeUserFromGroup,
                    request_deserializer=IamAdminService__pb2.UserGroupMappingRequest.FromString,
                    response_serializer=IamAdminService__pb2.OperationStatus.SerializeToString,
            ),
            'addChildGroupToParentGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.addChildGroupToParentGroup,
                    request_deserializer=UserProfileService__pb2.GroupToGroupMembership.FromString,
                    response_serializer=IamAdminService__pb2.OperationStatus.SerializeToString,
            ),
            'removeChildGroupFromParentGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.removeChildGroupFromParentGroup,
                    request_deserializer=UserProfileService__pb2.GroupToGroupMembership.FromString,
                    response_serializer=IamAdminService__pb2.OperationStatus.SerializeToString,
            ),
            'getAllGroupsOfUser': grpc.unary_unary_rpc_method_handler(
                    servicer.getAllGroupsOfUser,
                    request_deserializer=UserProfileService__pb2.UserProfileRequest.FromString,
                    response_serializer=UserProfileService__pb2.GetAllGroupsResponse.SerializeToString,
            ),
            'getAllParentGroupsOfGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.getAllParentGroupsOfGroup,
                    request_deserializer=UserProfileService__pb2.GroupRequest.FromString,
                    response_serializer=UserProfileService__pb2.GetAllGroupsResponse.SerializeToString,
            ),
            'getAllChildUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.getAllChildUsers,
                    request_deserializer=UserProfileService__pb2.GroupRequest.FromString,
                    response_serializer=UserProfileService__pb2.GetAllUserProfilesResponse.SerializeToString,
            ),
            'getAllChildGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.getAllChildGroups,
                    request_deserializer=UserProfileService__pb2.GroupRequest.FromString,
                    response_serializer=UserProfileService__pb2.GetAllGroupsResponse.SerializeToString,
            ),
            'changeUserMembershipType': grpc.unary_unary_rpc_method_handler(
                    servicer.changeUserMembershipType,
                    request_deserializer=UserProfileService__pb2.GroupMembership.FromString,
                    response_serializer=IamAdminService__pb2.OperationStatus.SerializeToString,
            ),
            'hasAccess': grpc.unary_unary_rpc_method_handler(
                    servicer.hasAccess,
                    request_deserializer=UserProfileService__pb2.GroupMembership.FromString,
                    response_serializer=IamAdminService__pb2.OperationStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.apache.custos.group.management.service.GroupManagementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GroupManagementService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/createGroups',
            IamAdminService__pb2.GroupsRequest.SerializeToString,
            IamAdminService__pb2.GroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/updateGroup',
            IamAdminService__pb2.GroupRequest.SerializeToString,
            IamAdminService__pb2.GroupRepresentation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/deleteGroup',
            IamAdminService__pb2.GroupRequest.SerializeToString,
            IamAdminService__pb2.OperationStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def findGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/findGroup',
            IamAdminService__pb2.GroupRequest.SerializeToString,
            IamAdminService__pb2.GroupRepresentation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAllGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/getAllGroups',
            IamAdminService__pb2.GroupRequest.SerializeToString,
            IamAdminService__pb2.GroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addUserToGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/addUserToGroup',
            IamAdminService__pb2.UserGroupMappingRequest.SerializeToString,
            IamAdminService__pb2.OperationStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def removeUserFromGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/removeUserFromGroup',
            IamAdminService__pb2.UserGroupMappingRequest.SerializeToString,
            IamAdminService__pb2.OperationStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addChildGroupToParentGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/addChildGroupToParentGroup',
            UserProfileService__pb2.GroupToGroupMembership.SerializeToString,
            IamAdminService__pb2.OperationStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def removeChildGroupFromParentGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/removeChildGroupFromParentGroup',
            UserProfileService__pb2.GroupToGroupMembership.SerializeToString,
            IamAdminService__pb2.OperationStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAllGroupsOfUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/getAllGroupsOfUser',
            UserProfileService__pb2.UserProfileRequest.SerializeToString,
            UserProfileService__pb2.GetAllGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAllParentGroupsOfGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/getAllParentGroupsOfGroup',
            UserProfileService__pb2.GroupRequest.SerializeToString,
            UserProfileService__pb2.GetAllGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAllChildUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/getAllChildUsers',
            UserProfileService__pb2.GroupRequest.SerializeToString,
            UserProfileService__pb2.GetAllUserProfilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAllChildGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/getAllChildGroups',
            UserProfileService__pb2.GroupRequest.SerializeToString,
            UserProfileService__pb2.GetAllGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def changeUserMembershipType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/changeUserMembershipType',
            UserProfileService__pb2.GroupMembership.SerializeToString,
            IamAdminService__pb2.OperationStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def hasAccess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.group.management.service.GroupManagementService/hasAccess',
            UserProfileService__pb2.GroupMembership.SerializeToString,
            IamAdminService__pb2.OperationStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)