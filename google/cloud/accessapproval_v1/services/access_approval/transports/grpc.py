# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import gapic_v1  # type: ignore
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.accessapproval_v1.types import accessapproval
from google.protobuf import empty_pb2  # type: ignore
from .base import AccessApprovalTransport, DEFAULT_CLIENT_INFO


class AccessApprovalGrpcTransport(AccessApprovalTransport):
    """gRPC backend transport for AccessApproval.

    This API allows a customer to manage accesses to cloud resources by
    Google personnel. It defines the following resource model:

    -  The API has a collection of
       [ApprovalRequest][google.cloud.accessapproval.v1.ApprovalRequest]
       resources, named ``approvalRequests/{approval_request_id}``
    -  The API has top-level settings per Project/Folder/Organization,
       named ``accessApprovalSettings``

    The service also periodically emails a list of recipients, defined
    at the Project/Folder/Organization level in the
    accessApprovalSettings, when there is a pending ApprovalRequest for
    them to act on. The ApprovalRequests can also optionally be
    published to a Cloud Pub/Sub topic owned by the customer (for Beta,
    the Pub/Sub setup is managed manually).

    ApprovalRequests can be approved or dismissed. Google personel can
    only access the indicated resource or resources if the request is
    approved (subject to some exclusions:
    https://cloud.google.com/access-approval/docs/overview#exclusions).

    Note: Using Access Approval functionality will mean that Google may
    not be able to meet the SLAs for your chosen products, as any
    support response times may be dramatically increased. As such the
    SLAs do not apply to any service disruption to the extent impacted
    by Customer's use of Access Approval. Do not enable Access Approval
    for projects where you may require high service availability and
    rapid response by Google Cloud Support.

    After a request is approved or dismissed, no further action may be
    taken on it. Requests with the requested_expiration in the past or
    with no activity for 14 days are considered dismissed. When an
    approval expires, the request is considered dismissed.

    If a request is not approved or dismissed, we call it pending.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "accessapproval.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "accessapproval.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        self_signed_jwt_kwargs = cls._get_self_signed_jwt_kwargs(host, scopes)

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            **self_signed_jwt_kwargs,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def list_approval_requests(
        self,
    ) -> Callable[
        [accessapproval.ListApprovalRequestsMessage],
        accessapproval.ListApprovalRequestsResponse,
    ]:
        r"""Return a callable for the list approval requests method over gRPC.

        Lists approval requests associated with a project,
        folder, or organization. Approval requests can be
        filtered by state (pending, active, dismissed). The
        order is reverse chronological.

        Returns:
            Callable[[~.ListApprovalRequestsMessage],
                    ~.ListApprovalRequestsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_approval_requests" not in self._stubs:
            self._stubs["list_approval_requests"] = self.grpc_channel.unary_unary(
                "/google.cloud.accessapproval.v1.AccessApproval/ListApprovalRequests",
                request_serializer=accessapproval.ListApprovalRequestsMessage.serialize,
                response_deserializer=accessapproval.ListApprovalRequestsResponse.deserialize,
            )
        return self._stubs["list_approval_requests"]

    @property
    def get_approval_request(
        self,
    ) -> Callable[
        [accessapproval.GetApprovalRequestMessage], accessapproval.ApprovalRequest
    ]:
        r"""Return a callable for the get approval request method over gRPC.

        Gets an approval request. Returns NOT_FOUND if the request does
        not exist.

        Returns:
            Callable[[~.GetApprovalRequestMessage],
                    ~.ApprovalRequest]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_approval_request" not in self._stubs:
            self._stubs["get_approval_request"] = self.grpc_channel.unary_unary(
                "/google.cloud.accessapproval.v1.AccessApproval/GetApprovalRequest",
                request_serializer=accessapproval.GetApprovalRequestMessage.serialize,
                response_deserializer=accessapproval.ApprovalRequest.deserialize,
            )
        return self._stubs["get_approval_request"]

    @property
    def approve_approval_request(
        self,
    ) -> Callable[
        [accessapproval.ApproveApprovalRequestMessage], accessapproval.ApprovalRequest
    ]:
        r"""Return a callable for the approve approval request method over gRPC.

        Approves a request and returns the updated ApprovalRequest.

        Returns NOT_FOUND if the request does not exist. Returns
        FAILED_PRECONDITION if the request exists but is not in a
        pending state.

        Returns:
            Callable[[~.ApproveApprovalRequestMessage],
                    ~.ApprovalRequest]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "approve_approval_request" not in self._stubs:
            self._stubs["approve_approval_request"] = self.grpc_channel.unary_unary(
                "/google.cloud.accessapproval.v1.AccessApproval/ApproveApprovalRequest",
                request_serializer=accessapproval.ApproveApprovalRequestMessage.serialize,
                response_deserializer=accessapproval.ApprovalRequest.deserialize,
            )
        return self._stubs["approve_approval_request"]

    @property
    def dismiss_approval_request(
        self,
    ) -> Callable[
        [accessapproval.DismissApprovalRequestMessage], accessapproval.ApprovalRequest
    ]:
        r"""Return a callable for the dismiss approval request method over gRPC.

        Dismisses a request. Returns the updated ApprovalRequest.

        NOTE: This does not deny access to the resource if another
        request has been made and approved. It is equivalent in effect
        to ignoring the request altogether.

        Returns NOT_FOUND if the request does not exist.

        Returns FAILED_PRECONDITION if the request exists but is not in
        a pending state.

        Returns:
            Callable[[~.DismissApprovalRequestMessage],
                    ~.ApprovalRequest]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "dismiss_approval_request" not in self._stubs:
            self._stubs["dismiss_approval_request"] = self.grpc_channel.unary_unary(
                "/google.cloud.accessapproval.v1.AccessApproval/DismissApprovalRequest",
                request_serializer=accessapproval.DismissApprovalRequestMessage.serialize,
                response_deserializer=accessapproval.ApprovalRequest.deserialize,
            )
        return self._stubs["dismiss_approval_request"]

    @property
    def get_access_approval_settings(
        self,
    ) -> Callable[
        [accessapproval.GetAccessApprovalSettingsMessage],
        accessapproval.AccessApprovalSettings,
    ]:
        r"""Return a callable for the get access approval settings method over gRPC.

        Gets the settings associated with a project, folder,
        or organization.

        Returns:
            Callable[[~.GetAccessApprovalSettingsMessage],
                    ~.AccessApprovalSettings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_access_approval_settings" not in self._stubs:
            self._stubs["get_access_approval_settings"] = self.grpc_channel.unary_unary(
                "/google.cloud.accessapproval.v1.AccessApproval/GetAccessApprovalSettings",
                request_serializer=accessapproval.GetAccessApprovalSettingsMessage.serialize,
                response_deserializer=accessapproval.AccessApprovalSettings.deserialize,
            )
        return self._stubs["get_access_approval_settings"]

    @property
    def update_access_approval_settings(
        self,
    ) -> Callable[
        [accessapproval.UpdateAccessApprovalSettingsMessage],
        accessapproval.AccessApprovalSettings,
    ]:
        r"""Return a callable for the update access approval
        settings method over gRPC.

        Updates the settings associated with a project, folder, or
        organization. Settings to update are determined by the value of
        field_mask.

        Returns:
            Callable[[~.UpdateAccessApprovalSettingsMessage],
                    ~.AccessApprovalSettings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_access_approval_settings" not in self._stubs:
            self._stubs[
                "update_access_approval_settings"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.accessapproval.v1.AccessApproval/UpdateAccessApprovalSettings",
                request_serializer=accessapproval.UpdateAccessApprovalSettingsMessage.serialize,
                response_deserializer=accessapproval.AccessApprovalSettings.deserialize,
            )
        return self._stubs["update_access_approval_settings"]

    @property
    def delete_access_approval_settings(
        self,
    ) -> Callable[
        [accessapproval.DeleteAccessApprovalSettingsMessage], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete access approval
        settings method over gRPC.

        Deletes the settings associated with a project,
        folder, or organization. This will have the effect of
        disabling Access Approval for the project, folder, or
        organization, but only if all ancestors also have Access
        Approval disabled. If Access Approval is enabled at a
        higher level of the hierarchy, then Access Approval will
        still be enabled at this level as the settings are
        inherited.

        Returns:
            Callable[[~.DeleteAccessApprovalSettingsMessage],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_access_approval_settings" not in self._stubs:
            self._stubs[
                "delete_access_approval_settings"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.accessapproval.v1.AccessApproval/DeleteAccessApprovalSettings",
                request_serializer=accessapproval.DeleteAccessApprovalSettingsMessage.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_access_approval_settings"]


__all__ = ("AccessApprovalGrpcTransport",)
