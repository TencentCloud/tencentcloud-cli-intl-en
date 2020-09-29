# -*- coding: utf-8 -*-
DESC = "cam-2019-01-16"
INFO = {
  "SetMfaFlag": {
    "params": [
      {
        "name": "OpUin",
        "desc": "Sets user UIN"
      },
      {
        "name": "LoginFlag",
        "desc": "Sets login protection"
      },
      {
        "name": "ActionFlag",
        "desc": "Sets operation protection"
      }
    ],
    "desc": "This API is used to set account verification for login and sensitive operations for sub-users."
  },
  "ListUsersForGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "User group ID"
      },
      {
        "name": "Page",
        "desc": "Page number; default is 1"
      },
      {
        "name": "Rp",
        "desc": "Number of entries per page; default is 20"
      }
    ],
    "desc": "This API is used to query the list of users associated with a user group."
  },
  "PutRolePermissionsBoundary": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "RoleId",
        "desc": "Role ID (either it or the role name must be entered)"
      },
      {
        "name": "RoleName",
        "desc": "Role name (either it or the role ID must be entered)"
      }
    ],
    "desc": "This API is used to set a role permission boundary."
  },
  "DeleteServiceLinkedRole": {
    "params": [
      {
        "name": "RoleName",
        "desc": "Name of the service-linked role to be deleted."
      }
    ],
    "desc": "This API is used to delete a service-linked role."
  },
  "AddUser": {
    "params": [
      {
        "name": "Name",
        "desc": "Sub-user username"
      },
      {
        "name": "Remark",
        "desc": "Sub-user remarks"
      },
      {
        "name": "ConsoleLogin",
        "desc": "Whether or not the sub-user is allowed to log in to the console. 0: No; 1: Yes."
      },
      {
        "name": "UseApi",
        "desc": "Whether or not to generate keys for sub-users. 0: No; 1: Yes."
      },
      {
        "name": "Password",
        "desc": "Sub-user's console login password. If no password rules have been set, the password must have a minimum of 8 characters containing uppercase letters, lowercase letters, digits, and special characters by default. This parameter will be valid only when the sub-user is allowed to log in to the console. If it is not specified and console login is allowed, the system will automatically generate a random 32-character password that contains uppercase letters, lowercase letters, digits, and special characters."
      },
      {
        "name": "NeedResetPassword",
        "desc": "If the sub-user needs to reset their password when they next log in to the console. 0: No; 1: Yes."
      },
      {
        "name": "PhoneNum",
        "desc": "Mobile number"
      },
      {
        "name": "CountryCode",
        "desc": "Country/Area Code"
      },
      {
        "name": "Email",
        "desc": "Email"
      }
    ],
    "desc": "This API is used to add sub-users."
  },
  "CreateServiceLinkedRole": {
    "params": [
      {
        "name": "QCSServiceName",
        "desc": "Authorized service, i.e., Tencent Cloud service entity with this role attached."
      },
      {
        "name": "CustomSuffix",
        "desc": "Custom suffix. A string you provide, which is combined with the service-provided prefix to form the complete role name."
      },
      {
        "name": "Description",
        "desc": "Role description."
      }
    ],
    "desc": "This API is used to create a service-linked role."
  },
  "GetSAMLProvider": {
    "params": [
      {
        "name": "Name",
        "desc": "SAML identity provider name"
      }
    ],
    "desc": "This API is used to query SAML identity provider details."
  },
  "CreateRole": {
    "params": [
      {
        "name": "RoleName",
        "desc": "Role name"
      },
      {
        "name": "PolicyDocument",
        "desc": "Policy document"
      },
      {
        "name": "Description",
        "desc": "Role description"
      },
      {
        "name": "ConsoleLogin",
        "desc": "Whether login is allowed. 1: yes, 0: no"
      },
      {
        "name": "SessionDuration",
        "desc": "The maximum validity period of the temporary key for creating a role (range: 0-43200)"
      }
    ],
    "desc": "This API (CreateRole) is used to create a role."
  },
  "ListUsers": {
    "params": [],
    "desc": "This API is used to pull sub-users."
  },
  "ListAttachedRolePolicies": {
    "params": [
      {
        "name": "Page",
        "desc": "Page number, beginning from 1"
      },
      {
        "name": "Rp",
        "desc": "Number of lines per page, no more than 200"
      },
      {
        "name": "RoleId",
        "desc": "Role ID, used to specify a role. Input either `RoleId` or `RoleName`"
      },
      {
        "name": "RoleName",
        "desc": "Role name, used to specify a role. Input either `RoleId` or `RoleName`"
      },
      {
        "name": "PolicyType",
        "desc": "Filter according to policy type. `User` indicates querying custom policies only. `QCS` indicates querying preset policies only"
      }
    ],
    "desc": "This API (ListAttachedRolePolicies) is used to obtain the list of the policies associated with a role."
  },
  "DeletePolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Array. Array elements are policy IDs. Policies can be deleted in a batch"
      }
    ],
    "desc": "This API (DeletePolicy) is used to delete a policy."
  },
  "DeleteRolePermissionsBoundary": {
    "params": [
      {
        "name": "RoleId",
        "desc": "Role ID (either it or the role name must be entered)"
      },
      {
        "name": "RoleName",
        "desc": "Role name (either it or the role ID must be entered)"
      }
    ],
    "desc": "This API is used to delete a role permission boundary."
  },
  "DeletePolicyVersion": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "VersionId",
        "desc": "Policy version ID"
      }
    ],
    "desc": "This API is used to delete a policy version of a policy."
  },
  "DetachRolePolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID. Either `PolicyId` or `PolicyName` must be entered"
      },
      {
        "name": "DetachRoleId",
        "desc": "Role ID, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`"
      },
      {
        "name": "DetachRoleName",
        "desc": "Role name, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`"
      },
      {
        "name": "PolicyName",
        "desc": "Policy name. Either `PolicyId` or `PolicyName` must be entered"
      }
    ],
    "desc": "This API (DetachRolePolicy) is used to unassociate a policy and a role."
  },
  "GetPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      }
    ],
    "desc": "This API (GetPolicy) is used to query and view policy details."
  },
  "CreateSAMLProvider": {
    "params": [
      {
        "name": "Name",
        "desc": "SAML identity provider name"
      },
      {
        "name": "Description",
        "desc": "SAML identity provider description"
      },
      {
        "name": "SAMLMetadataDocument",
        "desc": "SAML identity provider metadata document (Base64)"
      }
    ],
    "desc": "This API is used to create a SAML identity provider."
  },
  "DeleteSAMLProvider": {
    "params": [
      {
        "name": "Name",
        "desc": "SAML identity provider name"
      }
    ],
    "desc": "This API is used to delete a SAML identity provider."
  },
  "UpdateUser": {
    "params": [
      {
        "name": "Name",
        "desc": "Sub-user username"
      },
      {
        "name": "Remark",
        "desc": "Sub-user remarks"
      },
      {
        "name": "ConsoleLogin",
        "desc": "Whether or not the sub-user is allowed to log in to the console. 0: No; 1: Yes."
      },
      {
        "name": "Password",
        "desc": "Sub-user's console login password. If no password rules have been set, the password must have a minimum of 8 characters containing uppercase letters, lowercase letters, digits, and special characters by default. This parameter will be valid only when the sub-user is allowed to log in to the console. If it is not specified and console login is allowed, the system will automatically generate a random 32-character password that contains uppercase letters, lowercase letters, digits, and special characters."
      },
      {
        "name": "NeedResetPassword",
        "desc": "If the sub-user needs to reset their password when they next log in to the console. 0: No; 1: Yes."
      },
      {
        "name": "PhoneNum",
        "desc": "Mobile number"
      },
      {
        "name": "CountryCode",
        "desc": "Country/Area Code"
      },
      {
        "name": "Email",
        "desc": "Email"
      }
    ],
    "desc": "This API is used to update a sub-user."
  },
  "DescribeRoleList": {
    "params": [
      {
        "name": "Page",
        "desc": "Page number, beginning from 1"
      },
      {
        "name": "Rp",
        "desc": "Number of lines per page, no greater than 200"
      }
    ],
    "desc": "This API (DescribeRoleList) is used to get the role list under the account."
  },
  "GetCustomMFATokenInfo": {
    "params": [
      {
        "name": "MFAToken",
        "desc": "Custom multi-factor verification Token"
      }
    ],
    "desc": "This API is used to get information associated with a custom multi-factor Token"
  },
  "ListAccessKeys": {
    "params": [
      {
        "name": "TargetUin",
        "desc": "`UIN` of the specified user. If this parameter is left empty, access keys of the current user will be listed by default"
      }
    ],
    "desc": "This API is used to list the access keys associated with a specified CAM user."
  },
  "DeleteGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "User Group ID"
      }
    ],
    "desc": "This API is used to delete a user group."
  },
  "DeleteRole": {
    "params": [
      {
        "name": "RoleId",
        "desc": "Role ID, used to specify a role. Input either `RoleId` or `RoleName`"
      },
      {
        "name": "RoleName",
        "desc": "Role name, used to specify a role. Input either `RoleId` or `RoleName`"
      }
    ],
    "desc": "This API (DeleteRole) is used to delete a specified role."
  },
  "GetUser": {
    "params": [
      {
        "name": "Name",
        "desc": "Sub-user username"
      }
    ],
    "desc": "This API is used to query sub-users."
  },
  "DeleteUserPermissionsBoundary": {
    "params": [
      {
        "name": "TargetUin",
        "desc": "Sub-account `Uin`"
      }
    ],
    "desc": "This API is used to delete a user permission boundary."
  },
  "ListAttachedGroupPolicies": {
    "params": [
      {
        "name": "TargetGroupId",
        "desc": "User group ID"
      },
      {
        "name": "Page",
        "desc": "Page number, which starts from 1. Default is 1"
      },
      {
        "name": "Rp",
        "desc": "Number of entries per page; 20 by default"
      }
    ],
    "desc": "This API (ListAttachedGroupPolicies) is used to query the list of policies associated with a user group."
  },
  "PutUserPermissionsBoundary": {
    "params": [
      {
        "name": "TargetUin",
        "desc": "Sub-account `Uin`"
      },
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      }
    ],
    "desc": "This API is used to set a user permission boundary."
  },
  "GetServiceLinkedRoleDeletionStatus": {
    "params": [
      {
        "name": "DeletionTaskId",
        "desc": "Deletion task ID"
      }
    ],
    "desc": "This API is used to get the status of the service-linked role deletion based on the `TaskId`"
  },
  "ConsumeCustomMFAToken": {
    "params": [
      {
        "name": "MFAToken",
        "desc": "Custom multi-factor verification Token"
      }
    ],
    "desc": "This API is used to verify a custom multi-factor Token."
  },
  "GetGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "User Group ID"
      }
    ],
    "desc": "This API is used to query user group details."
  },
  "CreateGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "User Group name"
      },
      {
        "name": "Remark",
        "desc": "User Group description"
      }
    ],
    "desc": "This API is used to create a user group."
  },
  "UpdateAssumeRolePolicy": {
    "params": [
      {
        "name": "PolicyDocument",
        "desc": "Policy document"
      },
      {
        "name": "RoleId",
        "desc": "Role ID, used to specify a role. Input either `RoleId` or `RoleName`"
      },
      {
        "name": "RoleName",
        "desc": "Role name, used to specify a role. Input either `RoleId` or `RoleName`"
      }
    ],
    "desc": "This API (UpdateAssumeRolePolicy) is used to modify the trust policy of a role."
  },
  "SetDefaultPolicyVersion": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "VersionId",
        "desc": "Policy version ID"
      }
    ],
    "desc": "This API is used to set the operative policy version."
  },
  "DeleteUser": {
    "params": [
      {
        "name": "Name",
        "desc": "Sub-user username"
      },
      {
        "name": "Force",
        "desc": "Whether to forcibly delete the sub-user. The default input parameter is `0`. `0`: do not delete the user if the user has undeleted API keys; `1`: first delete the API keys then delete the user if the user has undeleted API keys. To delete API keys, you need to have cam:DeleteApiKey permission, which enables you to delete both enabled and disabled API keys. If you do not have this permission, you will not be able to delete API keys and the user."
      }
    ],
    "desc": "This API is used to delete a sub-user."
  },
  "AddUserToGroup": {
    "params": [
      {
        "name": "Info",
        "desc": "How sub-user UIDs are associated with the ID of the user group they are added to."
      }
    ],
    "desc": "This API is used to add users to a user group."
  },
  "UpdateSAMLProvider": {
    "params": [
      {
        "name": "Name",
        "desc": "SAML identity provider name"
      },
      {
        "name": "Description",
        "desc": "SAML identity provider description"
      },
      {
        "name": "SAMLMetadataDocument",
        "desc": "SAML identity provider metadata document (Base64)"
      }
    ],
    "desc": "This API is used to update SAML identity provider information."
  },
  "DescribeSafeAuthFlagColl": {
    "params": [
      {
        "name": "SubUin",
        "desc": "Sub-account"
      }
    ],
    "desc": "This API is used to query security settings."
  },
  "UpdatePolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID. Either `PolicyId` or `PolicyName` must be entered"
      },
      {
        "name": "PolicyName",
        "desc": "Policy name. Either `PolicyName` or `PolicyId` must be entered"
      },
      {
        "name": "Description",
        "desc": "Policy description"
      },
      {
        "name": "PolicyDocument",
        "desc": "Policy documentation, for example: `{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"cloudaudit.cloud.tencent.com\",\"cls.cloud.tencent.com\"]}}]}`, where `principal` is used to specify the service that is authorized to use the role. For more information about this parameter, see **RoleInfo** under **Output Parameters** in the [GetRole](https://intl.cloud.tencent.com/document/product/598/36221?from_cn_redirect=1)."
      },
      {
        "name": "Alias",
        "desc": "Preset policy remark"
      }
    ],
    "desc": "This API is used to update a policy.\nThis API will update the default version of an existing policy instead of creating a new one. If no policy exists, a default version will be created."
  },
  "DescribeSafeAuthFlag": {
    "params": [],
    "desc": "This API is used to query security settings."
  },
  "ListEntitiesForPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "Page",
        "desc": "Page number, which starts from 1. Default is 1"
      },
      {
        "name": "Rp",
        "desc": "Number of entries per page; 20 by default"
      },
      {
        "name": "EntityFilter",
        "desc": "Valid values: `All`, `User`, `Group`, and `Role`. `All` means all entity types will be returned; `User` means only sub-accounts will be returned; `Group` means only User Groups will be returned; `Role` means only roles will be returned. `All` is the default value."
      }
    ],
    "desc": "This API (ListEntitiesForPolicy) is used to query the list of entities associated with a policy."
  },
  "GetRole": {
    "params": [
      {
        "name": "RoleId",
        "desc": "Role ID, used to specify role. Input either `RoleId` or `RoleName`"
      },
      {
        "name": "RoleName",
        "desc": "Role name, used to specify role. Input either `RoleId` or `RoleName`"
      }
    ],
    "desc": "This API (GetRole) is used to get the details of a specified role."
  },
  "UpdateRoleDescription": {
    "params": [
      {
        "name": "Description",
        "desc": "Role description"
      },
      {
        "name": "RoleId",
        "desc": "Role ID, used to specify a role. Input either `RoleId` or `RoleName`"
      },
      {
        "name": "RoleName",
        "desc": "Role name, used to specify a role. Input either `RoleId` or `RoleName`"
      }
    ],
    "desc": "This API (UpdateRoleDescription) is used to modify the description of a role."
  },
  "ListAttachedUserPolicies": {
    "params": [
      {
        "name": "TargetUin",
        "desc": "Sub-account UIN"
      },
      {
        "name": "Page",
        "desc": "Page number, which starts from 1. Default is 1"
      },
      {
        "name": "Rp",
        "desc": "Number of entries per page; 20 by default"
      }
    ],
    "desc": "This API (ListAttachedUserPolicies) is used to query the list of policies associated with a sub-account."
  },
  "ListGroups": {
    "params": [
      {
        "name": "Page",
        "desc": "Page number; default is 1"
      },
      {
        "name": "Rp",
        "desc": "Number of entries per page; default is 20"
      },
      {
        "name": "Keyword",
        "desc": "Filter by User Group name"
      }
    ],
    "desc": "This API is used to query the list of user groups."
  },
  "CreatePolicyVersion": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "PolicyDocument",
        "desc": "The policy document to use as the content for the new version"
      },
      {
        "name": "SetAsDefault",
        "desc": "Specifies whether to set this version as the default version"
      }
    ],
    "desc": "This API is used to add a policy version. After creating a policy version, you can easily change the policy by changing the policy version."
  },
  "ListCollaborators": {
    "params": [
      {
        "name": "Limit",
        "desc": "Number of entries per page. Default value: 20"
      },
      {
        "name": "Offset",
        "desc": "Pagination start value. Default value: 0"
      }
    ],
    "desc": "This API is used to get the collaborator list."
  },
  "AttachRolePolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID. Either `PolicyId` or `PolicyName` must be entered"
      },
      {
        "name": "AttachRoleId",
        "desc": "Role ID, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`"
      },
      {
        "name": "AttachRoleName",
        "desc": "Role name, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`"
      },
      {
        "name": "PolicyName",
        "desc": "Policy name. Either `PolicyId` or `PolicyName` must be entered"
      }
    ],
    "desc": "This API (AttachRolePolicy) is used to associate a policy with a role."
  },
  "RemoveUserFromGroup": {
    "params": [
      {
        "name": "Info",
        "desc": "The UID of the user to be deleted and an array corresponding to the User Group IDs"
      }
    ],
    "desc": "This API is used to delete users from a user group."
  },
  "ListSAMLProviders": {
    "params": [],
    "desc": "This API is used to query the list of SAML identity providers."
  },
  "UpdateRoleConsoleLogin": {
    "params": [
      {
        "name": "ConsoleLogin",
        "desc": "Whether login is allowed. 1: yes, 0: no"
      },
      {
        "name": "RoleId",
        "desc": "Role ID"
      },
      {
        "name": "RoleName",
        "desc": "Role name"
      }
    ],
    "desc": "This API is used to modify a role's login permissions."
  },
  "AttachUserPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "AttachUin",
        "desc": "Sub-account UIN"
      }
    ],
    "desc": "This API (AttachUserPolicy) is used to associates a policy with a user."
  },
  "ListPolicyVersions": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      }
    ],
    "desc": "This API is used to get the list of policy versions."
  },
  "ListGroupsForUser": {
    "params": [
      {
        "name": "Uid",
        "desc": "Sub-user UID"
      },
      {
        "name": "Rp",
        "desc": "Number of entries per page; default is 20"
      },
      {
        "name": "Page",
        "desc": "Page number; default is 1"
      },
      {
        "name": "SubUin",
        "desc": "Sub-account UIN"
      }
    ],
    "desc": "This API is used to list user groups associated with a user."
  },
  "AttachGroupPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "AttachGroupId",
        "desc": "User Group ID"
      }
    ],
    "desc": "This API (AttachGroupPolicy) is used to associate a policy with a user group."
  },
  "UpdateGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "User Group ID"
      },
      {
        "name": "GroupName",
        "desc": "User Group name"
      },
      {
        "name": "Remark",
        "desc": "User Group description"
      }
    ],
    "desc": "This API is used to update a user group."
  },
  "GetPolicyVersion": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "VersionId",
        "desc": "Policy version ID"
      }
    ],
    "desc": "This API is used to query policy version details."
  },
  "CreatePolicy": {
    "params": [
      {
        "name": "PolicyName",
        "desc": "Policy name"
      },
      {
        "name": "PolicyDocument",
        "desc": "Policy document, such as `{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"cloudaudit.cloud.tencent.com\",\"cls.cloud.tencent.com\"]}}]}`, where `principal` is used to specify the resources that the role is authorized to access. For more information on this parameter, please see the `RoleInfo` output parameter of the [GetRole](https://intl.cloud.tencent.com/document/product/598/36221?from_cn_redirect=1) API"
      },
      {
        "name": "Description",
        "desc": "Policy description"
      }
    ],
    "desc": "This API (CreatePolicy) is used to create a policy."
  },
  "DetachGroupPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "DetachGroupId",
        "desc": "User Group ID"
      }
    ],
    "desc": "This API (DetachGroupPolicy) is used to unassociate a policy and a user group."
  },
  "DetachUserPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "DetachUin",
        "desc": "Sub-account UIN"
      }
    ],
    "desc": "This API (DetachUserPolicy) is used to unassociate a policy and a user."
  },
  "ListPolicies": {
    "params": [
      {
        "name": "Rp",
        "desc": "Number of entries per page: must be greater than 0 and no greater than 200. Default is 20"
      },
      {
        "name": "Page",
        "desc": "Page number. Starts from 1 and cannot be greater than 200. Default is 1"
      },
      {
        "name": "Scope",
        "desc": "Valid values: `All`, `QCS`, and `Local`. `All` means all policies will be returned; `QCS` means only preset policies will be returned; `Local` means only custom policies will be returned. `All` is the default value"
      },
      {
        "name": "Keyword",
        "desc": "Filter by policy name"
      }
    ],
    "desc": "This API is used to query the policy list."
  }
}