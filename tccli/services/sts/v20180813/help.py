# -*- coding: utf-8 -*-
DESC = "sts-2018-08-13"
INFO = {
  "GetFederationToken": {
    "params": [
      {
        "name": "Name",
        "desc": "The customizable name of the caller, consisting of letters"
      },
      {
        "name": "Policy",
        "desc": "Policy description\nNote:\n1. The policy needs to be URL-encoded (if you request a TencentCloud API through the GET method, all parameters must be URL-encoded again in accordance with [Signature v3](https://cloud.tencent.com/document/api/598/33159#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2) before the request is sent).\n2. For the policy syntax, please see CAM’s [Syntax Logic](https://cloud.tencent.com/document/product/598/10603).\n3. The policy cannot contain the `principal` element."
      },
      {
        "name": "DurationSeconds",
        "desc": "Specifies the validity period of credentials in seconds. Default value: 1800. Maximum value: 7200"
      }
    ],
    "desc": "This API is used to get temporary credentials for a federated user."
  },
  "AssumeRoleWithSAML": {
    "params": [
      {
        "name": "SAMLAssertion",
        "desc": "Base64-encoded SAML assertion"
      },
      {
        "name": "PrincipalArn",
        "desc": "Principal access description name"
      },
      {
        "name": "RoleArn",
        "desc": "Role access description name"
      },
      {
        "name": "RoleSessionName",
        "desc": "Session name"
      },
      {
        "name": "DurationSeconds",
        "desc": "Specifies the validity period of credentials in seconds. Default value: 7200. Maximum value: 7200"
      }
    ],
    "desc": "This API is used to request for the temporary credentials for a role that has been authenticated via a SAML assertion."
  },
  "AssumeRole": {
    "params": [
      {
        "name": "RoleArn",
        "desc": "Role resource description, such as qcs::cam::uin/12345678:role/4611686018427397919, qcs::cam::uin/12345678:roleName/testRoleName"
      },
      {
        "name": "RoleSessionName",
        "desc": "User-defined temporary session name"
      },
      {
        "name": "DurationSeconds",
        "desc": "Specifies the validity period of credentials in seconds. Default value: 7200. Maximum value: 43200"
      },
      {
        "name": "Policy",
        "desc": "Policy description\nNote:\n1. The policy needs to be URL-encoded (if you request a TencentCloud API through the GET method, all parameters must be URL-encoded again in accordance with [Signature v3](https://cloud.tencent.com/document/api/598/33159#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2) before the request is sent).\n2. For the policy syntax, please see CAM’s [Syntax Logic](https://cloud.tencent.com/document/product/598/10603).\n3. The policy cannot contain the `principal` element."
      }
    ],
    "desc": "This API is used to request for the temporary security credentials of a role."
  }
}