config = {
    "interfaces": {
        "google.cloud.accessapproval.v1.AccessApproval": {
            "retry_codes": {
                "retry_policy_1_codes": ["UNAVAILABLE"],
                "no_retry_codes": [],
                "no_retry_1_codes": [],
            },
            "retry_params": {
                "retry_policy_1_params": {
                    "initial_retry_delay_millis": 100,
                    "retry_delay_multiplier": 1.3,
                    "max_retry_delay_millis": 60000,
                    "initial_rpc_timeout_millis": 600000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 600000,
                    "total_timeout_millis": 600000,
                },
                "no_retry_params": {
                    "initial_retry_delay_millis": 0,
                    "retry_delay_multiplier": 0.0,
                    "max_retry_delay_millis": 0,
                    "initial_rpc_timeout_millis": 0,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 0,
                    "total_timeout_millis": 0,
                },
                "no_retry_1_params": {
                    "initial_retry_delay_millis": 0,
                    "retry_delay_multiplier": 0.0,
                    "max_retry_delay_millis": 0,
                    "initial_rpc_timeout_millis": 600000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 600000,
                    "total_timeout_millis": 600000,
                },
            },
            "methods": {
                "ListApprovalRequests": {
                    "timeout_millis": 600000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
                "GetApprovalRequest": {
                    "timeout_millis": 600000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
                "ApproveApprovalRequest": {
                    "timeout_millis": 600000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                },
                "DismissApprovalRequest": {
                    "timeout_millis": 600000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                },
                "GetAccessApprovalSettings": {
                    "timeout_millis": 600000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
                "UpdateAccessApprovalSettings": {
                    "timeout_millis": 600000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                },
                "DeleteAccessApprovalSettings": {
                    "timeout_millis": 600000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                },
            },
        }
    }
}
