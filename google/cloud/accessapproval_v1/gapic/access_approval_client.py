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

"""Accesses the google.cloud.accessapproval.v1 AccessApproval API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import grpc

from google.cloud.accessapproval_v1.gapic import access_approval_client_config
from google.cloud.accessapproval_v1.gapic import enums
from google.cloud.accessapproval_v1.gapic.transports import (
    access_approval_grpc_transport,
)
from google.cloud.accessapproval_v1.proto import accessapproval_pb2
from google.cloud.accessapproval_v1.proto import accessapproval_pb2_grpc
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import timestamp_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-access-approval"
).version


class AccessApprovalClient(object):
    """
    The parent resource. This may be "projects/{project_id}",
    "folders/{folder_id}", or "organizations/{organization_id}".
    """

    SERVICE_ADDRESS = "accessapproval.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.accessapproval.v1.AccessApproval"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AccessApprovalClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.AccessApprovalGrpcTransport,
                    Callable[[~.Credentials, type], ~.AccessApprovalGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = access_approval_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=access_approval_grpc_transport.AccessApprovalGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = access_approval_grpc_transport.AccessApprovalGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def list_approval_requests(
        self,
        parent=None,
        filter_=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists approval requests associated with a project, folder, or organization.
        Approval requests can be filtered by state (pending, active, dismissed).
        The order is reverse chronological.

        Example:
            >>> from google.cloud import accessapproval_v1
            >>>
            >>> client = accessapproval_v1.AccessApprovalClient()
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_approval_requests():
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_approval_requests().pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): The same concept of the ``singular`` field in k8s CRD spec
                https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/
                Such as "project" for the ``resourcemanager.googleapis.com/Project``
                type.
            filter_ (str): An indicator of the behavior of a given field (for example, that a
                field is required in requests, or given as output but ignored as input).
                This **does not** change the behavior in protocol buffers itself; it
                only denotes the behavior and may affect how API tooling handles the
                field.

                Note: This enum **may** receive new values in the future.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.accessapproval_v1.types.ApprovalRequest` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_approval_requests" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_approval_requests"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_approval_requests,
                default_retry=self._method_configs["ListApprovalRequests"].retry,
                default_timeout=self._method_configs["ListApprovalRequests"].timeout,
                client_info=self._client_info,
            )

        request = accessapproval_pb2.ListApprovalRequestsMessage(
            parent=parent, filter=filter_, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_approval_requests"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="approval_requests",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_approval_request(
        self,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        javanano_as_lite

        Example:
            >>> from google.cloud import accessapproval_v1
            >>>
            >>> client = accessapproval_v1.AccessApprovalClient()
            >>>
            >>> response = client.get_approval_request()

        Args:
            name (str): Name of the approval request to retrieve.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.accessapproval_v1.types.ApprovalRequest` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_approval_request" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_approval_request"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_approval_request,
                default_retry=self._method_configs["GetApprovalRequest"].retry,
                default_timeout=self._method_configs["GetApprovalRequest"].timeout,
                client_info=self._client_info,
            )

        request = accessapproval_pb2.GetApprovalRequestMessage(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_approval_request"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def approve_approval_request(
        self,
        name=None,
        expire_time=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        An annotation that describes a resource definition without a
        corresponding message; see ``ResourceDescriptor``.

        Example:
            >>> from google.cloud import accessapproval_v1
            >>>
            >>> client = accessapproval_v1.AccessApprovalClient()
            >>>
            >>> response = client.approve_approval_request()

        Args:
            name (str): Name of the approval request to approve.
            expire_time (Union[dict, ~google.cloud.accessapproval_v1.types.Timestamp]): The expiration time of this approval.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.accessapproval_v1.types.Timestamp`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.accessapproval_v1.types.ApprovalRequest` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "approve_approval_request" not in self._inner_api_calls:
            self._inner_api_calls[
                "approve_approval_request"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.approve_approval_request,
                default_retry=self._method_configs["ApproveApprovalRequest"].retry,
                default_timeout=self._method_configs["ApproveApprovalRequest"].timeout,
                client_info=self._client_info,
            )

        request = accessapproval_pb2.ApproveApprovalRequestMessage(
            name=name, expire_time=expire_time
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["approve_approval_request"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def dismiss_approval_request(
        self,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Approves a request and returns the updated ApprovalRequest.

        Returns NOT_FOUND if the request does not exist. Returns
        FAILED_PRECONDITION if the request exists but is not in a pending state.

        Example:
            >>> from google.cloud import accessapproval_v1
            >>>
            >>> client = accessapproval_v1.AccessApprovalClient()
            >>>
            >>> response = client.dismiss_approval_request()

        Args:
            name (str): Name of the ApprovalRequest to dismiss.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.accessapproval_v1.types.ApprovalRequest` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "dismiss_approval_request" not in self._inner_api_calls:
            self._inner_api_calls[
                "dismiss_approval_request"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.dismiss_approval_request,
                default_retry=self._method_configs["DismissApprovalRequest"].retry,
                default_timeout=self._method_configs["DismissApprovalRequest"].timeout,
                client_info=self._client_info,
            )

        request = accessapproval_pb2.DismissApprovalRequestMessage(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["dismiss_approval_request"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_access_approval_settings(
        self,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets the settings associated with a project, folder, or organization.

        Example:
            >>> from google.cloud import accessapproval_v1
            >>>
            >>> client = accessapproval_v1.AccessApprovalClient()
            >>>
            >>> response = client.get_access_approval_settings()

        Args:
            name (str): Name of the AccessApprovalSettings to retrieve.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.accessapproval_v1.types.AccessApprovalSettings` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_access_approval_settings" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_access_approval_settings"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_access_approval_settings,
                default_retry=self._method_configs["GetAccessApprovalSettings"].retry,
                default_timeout=self._method_configs[
                    "GetAccessApprovalSettings"
                ].timeout,
                client_info=self._client_info,
            )

        request = accessapproval_pb2.GetAccessApprovalSettingsMessage(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_access_approval_settings"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_access_approval_settings(
        self,
        settings=None,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Optional. The historical or future-looking state of the resource
        pattern.

        Example:

        ::

            // The InspectTemplate message originally only supported resource
            // names with organization, and project was added later.
            message InspectTemplate {
              option (google.api.resource) = {
                type: "dlp.googleapis.com/InspectTemplate"
                pattern:
                "organizations/{organization}/inspectTemplates/{inspect_template}"
                pattern: "projects/{project}/inspectTemplates/{inspect_template}"
                history: ORIGINALLY_SINGLE_PATTERN
              };
            }

        Example:
            >>> from google.cloud import accessapproval_v1
            >>>
            >>> client = accessapproval_v1.AccessApprovalClient()
            >>>
            >>> response = client.update_access_approval_settings()

        Args:
            settings (Union[dict, ~google.cloud.accessapproval_v1.types.AccessApprovalSettings]): The new AccessApprovalSettings.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.accessapproval_v1.types.AccessApprovalSettings`
            update_mask (Union[dict, ~google.cloud.accessapproval_v1.types.FieldMask]): Protocol Buffers - Google's data interchange format Copyright 2008
                Google Inc. All rights reserved.
                https://developers.google.com/protocol-buffers/

                Redistribution and use in source and binary forms, with or without
                modification, are permitted provided that the following conditions are
                met:

                ::

                    * Redistributions of source code must retain the above copyright

                notice, this list of conditions and the following disclaimer. \*
                Redistributions in binary form must reproduce the above copyright
                notice, this list of conditions and the following disclaimer in the
                documentation and/or other materials provided with the distribution. \*
                Neither the name of Google Inc. nor the names of its contributors may be
                used to endorse or promote products derived from this software without
                specific prior written permission.

                THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
                IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
                TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
                PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
                OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
                EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
                PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
                PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
                LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
                NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
                SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.accessapproval_v1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.accessapproval_v1.types.AccessApprovalSettings` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_access_approval_settings" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_access_approval_settings"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_access_approval_settings,
                default_retry=self._method_configs[
                    "UpdateAccessApprovalSettings"
                ].retry,
                default_timeout=self._method_configs[
                    "UpdateAccessApprovalSettings"
                ].timeout,
                client_info=self._client_info,
            )

        request = accessapproval_pb2.UpdateAccessApprovalSettingsMessage(
            settings=settings, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("settings.name", settings.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_access_approval_settings"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_access_approval_settings(
        self,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes the settings associated with a project, folder, or organization.
        This will have the effect of disabling Access Approval for the project,
        folder, or organization, but only if all ancestors also have Access
        Approval disabled. If Access Approval is enabled at a higher level of the
        hierarchy, then Access Approval will still be enabled at this level as
        the settings are inherited.

        Example:
            >>> from google.cloud import accessapproval_v1
            >>>
            >>> client = accessapproval_v1.AccessApprovalClient()
            >>>
            >>> client.delete_access_approval_settings()

        Args:
            name (str): Name of the AccessApprovalSettings to delete.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_access_approval_settings" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_access_approval_settings"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_access_approval_settings,
                default_retry=self._method_configs[
                    "DeleteAccessApprovalSettings"
                ].retry,
                default_timeout=self._method_configs[
                    "DeleteAccessApprovalSettings"
                ].timeout,
                client_info=self._client_info,
            )

        request = accessapproval_pb2.DeleteAccessApprovalSettingsMessage(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_access_approval_settings"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
