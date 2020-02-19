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

"""Wrappers for protocol buffer enum types."""

import enum


class EnrollmentLevel(enum.IntEnum):
    """
    Represents the type of enrollment for a given service to Access Approval.

    Attributes:
      ENROLLMENT_LEVEL_UNSPECIFIED (int): Default value for proto, shouldn't be used.
      BLOCK_ALL (int): Service is enrolled in Access Approval for all requests
    """

    ENROLLMENT_LEVEL_UNSPECIFIED = 0
    BLOCK_ALL = 1


class AccessReason(object):
    class Type(enum.IntEnum):
        """
        Type of access justification.

        Attributes:
          TYPE_UNSPECIFIED (int): Default value for proto, shouldn't be used.
          CUSTOMER_INITIATED_SUPPORT (int): The plural name used in the resource name, such as 'projects' for
          the name of 'projects/{project}'. It is the same concept of the
          ``plural`` field in k8s CRD spec
          https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/
          GOOGLE_INITIATED_SERVICE (int): The principal accessed customer data in order to diagnose or resolve a
          suspected issue in services or a known outage. Often this access is used
          to confirm that customers are not affected by a suspected service issue
          or to remediate a reversible system issue.
          GOOGLE_INITIATED_REVIEW (int): Google initiated service for security, fraud, abuse, or compliance
          purposes.
        """

        TYPE_UNSPECIFIED = 0
        CUSTOMER_INITIATED_SUPPORT = 1
        GOOGLE_INITIATED_SERVICE = 2
        GOOGLE_INITIATED_REVIEW = 3
