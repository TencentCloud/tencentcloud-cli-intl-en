# -*- coding: utf-8 -*-
DESC = "cam-2019-01-16"
INFO = {
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
        "desc": ""
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
  "DetachRolePolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "DetachRoleId",
        "desc": "Role ID, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`"
      },
      {
        "name": "DetachRoleName",
        "desc": "Role name, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`"
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
  "ConsumeCustomMFAToken": {
    "params": [
      {
        "name": "MFAToken",
        "desc": "Custom multi-factor verification Token"
      }
    ],
    "desc": "This API is used to verify a custom multi-factor Token."
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
  "GetCustomMFATokenInfo": {
    "params": [
      {
        "name": "MFAToken",
        "desc": "Custom multi-factor verification Token"
      }
    ],
    "desc": "This API is used to get information associated with a custom multi-factor Token"
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
      }
    ],
    "desc": "This API is used to list user groups associated with a user."
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
  "GetGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "User Group ID"
      }
    ],
    "desc": "This API is used to query user group details."
  },
  "DeleteUser": {
    "params": [
      {
        "name": "Name",
        "desc": "Sub-user username"
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
  "SetFlag": {
    "params": [
      {
        "name": "OpUin",
        "desc": "Set user UIN"
      },
      {
        "name": "LoginFlag",
        "desc": "Login settings"
      },
      {
        "name": "ActionFlag",
        "desc": "Sensitive operation settings"
      },
      {
        "name": "OffsiteFlag",
        "desc": "Remote login settings"
      },
      {
        "name": "NeedResetMfa",
        "desc": "If MFA requires top-up"
      }
    ],
    "desc": "This API is used to set account verification for login and sensitive operation protection."
  },
  "UpdatePolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "PolicyName",
        "desc": "Policy name"
      },
      {
        "name": "Description",
        "desc": "Policy description"
      },
      {
        "name": "PolicyDocument",
        "desc": "Policy document, such as `{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"cloudaudit.cloud.tencent.com\",\"cls.cloud.tencent.com\"]}}]}`, where `principal` is used to specify the resources that the role is authorized to access. For more information on this parameter, please see the `RoleInfo` output parameter of the [GetRole](https://cloud.tencent.com/document/product/598/36221) API"
      }
    ],
    "desc": "This API (UpdatePolicy) is used to update a policy."
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
  "AttachRolePolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "AttachRoleId",
        "desc": "Role ID, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`"
      },
      {
        "name": "AttachRoleName",
        "desc": "Role name, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`"
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
  "CreatePolicy": {
    "params": [
      {
        "name": "PolicyName",
        "desc": "Policy name"
      },
      {
        "name": "PolicyDocument",
        "desc": "Policy document, such as `{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"cloudaudit.cloud.tencent.com\",\"cls.cloud.tencent.com\"]}}]}`, where `principal` is used to specify the resources that the role is authorized to access. For more information on this parameter, please see the `RoleInfo` output parameter of the [GetRole](https://cloud.tencent.com/document/product/598/36221) API"
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
    "desc": "This API (ListPolicies) is used to query the list of policies."
  }
}