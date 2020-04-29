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
          CUSTOMER_INITIATED_SUPPORT (int): Identifies which part of the FileDescriptorProto was defined at this
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
