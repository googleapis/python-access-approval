# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import google.api_core.grpc_helpers

from google.cloud.accessapproval_v1.proto import accessapproval_pb2_grpc


class AccessApprovalGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.accessapproval.v1 AccessApproval API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self,
        channel=None,
        credentials=None,
        address="accessapproval.googleapis.com:443",
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive."
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "access_approval_stub": accessapproval_pb2_grpc.AccessApprovalStub(channel)
        }

    @classmethod
    def create_channel(
        cls, address="accessapproval.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def list_approval_requests(self):
        """Return the gRPC stub for :meth:`AccessApprovalClient.list_approval_requests`.

        Lists approval requests associated with a project, folder, or organization.
        Approval requests can be filtered by state (pending, active, dismissed).
        The order is reverse chronological.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["access_approval_stub"].ListApprovalRequests

    @property
    def get_approval_request(self):
        """Return the gRPC stub for :meth:`AccessApprovalClient.get_approval_request`.

        An annotation that describes a resource reference, see
        ``ResourceReference``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["access_approval_stub"].GetApprovalRequest

    @property
    def approve_approval_request(self):
        """Return the gRPC stub for :meth:`AccessApprovalClient.approve_approval_request`.

        Customer made a request or raised an issue that required the
        principal to access customer data. ``detail`` is of the form ("#####" is
        the issue ID):

        .. raw:: html

            <ol>
              <li>"Feedback Report: #####"</li>
              <li>"Case Number: #####"</li>
              <li>"Case ID: #####"</li>
              <li>"E-PIN Reference: #####"</li>
              <li>"Google-#####"</li>
              <li>"T-#####"</li>
            </ol>

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["access_approval_stub"].ApproveApprovalRequest

    @property
    def dismiss_approval_request(self):
        """Return the gRPC stub for :meth:`AccessApprovalClient.dismiss_approval_request`.

        Identifies which part of the FileDescriptorProto was defined at this
        location.

        Each element is a field number or an index. They form a path from the
        root FileDescriptorProto to the place where the definition. For example,
        this path: [ 4, 3, 2, 7, 1 ] refers to: file.message_type(3) // 4, 3
        .field(7) // 2, 7 .name() // 1 This is because
        FileDescriptorProto.message_type has field number 4: repeated
        DescriptorProto message_type = 4; and DescriptorProto.field has field
        number 2: repeated FieldDescriptorProto field = 2; and
        FieldDescriptorProto.name has field number 1: optional string name = 1;

        Thus, the above path gives the location of a field name. If we removed
        the last element: [ 4, 3, 2, 7 ] this path refers to the whole field
        declaration (from the beginning of the label to the terminating
        semicolon).

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["access_approval_stub"].DismissApprovalRequest

    @property
    def get_access_approval_settings(self):
        """Return the gRPC stub for :meth:`AccessApprovalClient.get_access_approval_settings`.

        Gets the settings associated with a project, folder, or organization.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["access_approval_stub"].GetAccessApprovalSettings

    @property
    def update_access_approval_settings(self):
        """Return the gRPC stub for :meth:`AccessApprovalClient.update_access_approval_settings`.

        ``FieldMask`` represents a set of symbolic field paths, for example:

        ::

            paths: "f.a"
            paths: "f.b.d"

        Here ``f`` represents a field in some root message, ``a`` and ``b``
        fields in the message found in ``f``, and ``d`` a field found in the
        message in ``f.b``.

        Field masks are used to specify a subset of fields that should be
        returned by a get operation or modified by an update operation. Field
        masks also have a custom JSON encoding (see below).

        # Field Masks in Projections

        When used in the context of a projection, a response message or
        sub-message is filtered by the API to only contain those fields as
        specified in the mask. For example, if the mask in the previous example
        is applied to a response message as follows:

        ::

            f {
              a : 22
              b {
                d : 1
                x : 2
              }
              y : 13
            }
            z: 8

        The result will not contain specific values for fields x,y and z (their
        value will be set to the default, and omitted in proto text output):

        ::

            f {
              a : 22
              b {
                d : 1
              }
            }

        A repeated field is not allowed except at the last position of a paths
        string.

        If a FieldMask object is not present in a get operation, the operation
        applies to all fields (as if a FieldMask of all fields had been
        specified).

        Note that a field mask does not necessarily apply to the top-level
        response message. In case of a REST get operation, the field mask
        applies directly to the response, but in case of a REST list operation,
        the mask instead applies to each individual message in the returned
        resource list. In case of a REST custom method, other definitions may be
        used. Where the mask applies will be clearly documented together with
        its declaration in the API. In any case, the effect on the returned
        resource/resources is required behavior for APIs.

        # Field Masks in Update Operations

        A field mask in update operations specifies which fields of the targeted
        resource are going to be updated. The API is required to only change the
        values of the fields as specified in the mask and leave the others
        untouched. If a resource is passed in to describe the updated values,
        the API ignores the values of all fields not covered by the mask.

        If a repeated field is specified for an update operation, new values
        will be appended to the existing repeated field in the target resource.
        Note that a repeated field is only allowed in the last position of a
        ``paths`` string.

        If a sub-message is specified in the last position of the field mask for
        an update operation, then new value will be merged into the existing
        sub-message in the target resource.

        For example, given the target message:

        ::

            f {
              b {
                d: 1
                x: 2
              }
              c: [1]
            }

        And an update message:

        ::

            f {
              b {
                d: 10
              }
              c: [2]
            }

        then if the field mask is:

        paths: ["f.b", "f.c"]

        then the result will be:

        ::

            f {
              b {
                d: 10
                x: 2
              }
              c: [1, 2]
            }

        An implementation may provide options to override this default behavior
        for repeated and message fields.

        In order to reset a field's value to the default, the field must be in
        the mask and set to the default value in the provided resource. Hence,
        in order to reset all fields of a resource, provide a default instance
        of the resource and set all fields in the mask, or do not provide a mask
        as described below.

        If a field mask is not present on update, the operation applies to all
        fields (as if a field mask of all fields has been specified). Note that
        in the presence of schema evolution, this may mean that fields the
        client does not know and has therefore not filled into the request will
        be reset to their default. If this is unwanted behavior, a specific
        service may require a client to always specify a field mask, producing
        an error if not.

        As with get operations, the location of the resource which describes the
        updated values in the request message depends on the operation kind. In
        any case, the effect of the field mask is required to be honored by the
        API.

        ## Considerations for HTTP REST

        The HTTP kind of an update operation which uses a field mask must be set
        to PATCH instead of PUT in order to satisfy HTTP semantics (PUT must
        only be used for full updates).

        # JSON Encoding of Field Masks

        In JSON, a field mask is encoded as a single string where paths are
        separated by a comma. Fields name in each path are converted to/from
        lower-camel naming conventions.

        As an example, consider the following message declarations:

        ::

            message Profile {
              User user = 1;
              Photo photo = 2;
            }
            message User {
              string display_name = 1;
              string address = 2;
            }

        In proto a field mask for ``Profile`` may look as such:

        ::

            mask {
              paths: "user.display_name"
              paths: "photo"
            }

        In JSON, the same mask is represented as below:

        ::

            {
              mask: "user.displayName,photo"
            }

        # Field Masks and Oneof Fields

        Field masks treat fields in oneofs just as regular fields. Consider the
        following message:

        ::

            message SampleMessage {
              oneof test_oneof {
                string name = 4;
                SubMessage sub_message = 9;
              }
            }

        The field mask can be:

        ::

            mask {
              paths: "name"
            }

        Or:

        ::

            mask {
              paths: "sub_message"
            }

        Note that oneof type names ("test_oneof" in this case) cannot be used in
        paths.

        ## Field Mask Verification

        The implementation of any API method which has a FieldMask type field in
        the request should verify the included field paths, and return an
        ``INVALID_ARGUMENT`` error if any path is duplicated or unmappable.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["access_approval_stub"].UpdateAccessApprovalSettings

    @property
    def delete_access_approval_settings(self):
        """Return the gRPC stub for :meth:`AccessApprovalClient.delete_access_approval_settings`.

        Deletes the settings associated with a project, folder, or organization.
        This will have the effect of disabling Access Approval for the project,
        folder, or organization, but only if all ancestors also have Access
        Approval disabled. If Access Approval is enabled at a higher level of the
        hierarchy, then Access Approval will still be enabled at this level as
        the settings are inherited.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["access_approval_stub"].DeleteAccessApprovalSettings
