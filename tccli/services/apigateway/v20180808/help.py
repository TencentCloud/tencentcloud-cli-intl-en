# -*- coding: utf-8 -*-
DESC = "apigateway-2018-08-08"
INFO = {
  "CreateService": {
    "params": [
      {
        "name": "ServiceName",
        "desc": "Custom service name. If this parameter is left empty, the system will automatically generate a unique name."
      },
      {
        "name": "Protocol",
        "desc": "Service frontend request type, such as `http`, `https`, and `http&https`."
      },
      {
        "name": "ServiceDesc",
        "desc": "Custom service description."
      },
      {
        "name": "ExclusiveSetName",
        "desc": "Self-deployed cluster name, which is used to specify the self-deployed cluster where the service is to be created."
      },
      {
        "name": "NetTypes",
        "desc": "Network type list, which is used to specify the supported network types. `INNER` indicates access over private network, and `OUTER` indicates access over public network. The default value is `OUTER`."
      },
      {
        "name": "IpVersion",
        "desc": "IP version number. Valid values: IPv4 (default value), IPv6"
      },
      {
        "name": "SetServerName",
        "desc": "Cluster name, which is reserved and used by the `tsf serverless` type."
      },
      {
        "name": "AppIdType",
        "desc": "User type, which is reserved and can be used by `serverless` users."
      }
    ],
    "desc": "This API is used to create a service.\nThe maximum unit in API Gateway is service. Multiple APIs can be created in one service, and each service has a default domain name for users to call. You can also bind your own custom domain name to a service."
  },
  "ModifyApiEnvironmentStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique service ID."
      },
      {
        "name": "Strategy",
        "desc": "Throttling value."
      },
      {
        "name": "EnvironmentName",
        "desc": "Environment name."
      },
      {
        "name": "ApiIds",
        "desc": "API list."
      }
    ],
    "desc": "This API is used to modify an API throttling policy."
  },
  "DeleteUsagePlan": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "Unique ID of the usage plan to be deleted."
      }
    ],
    "desc": "This API is used to delete a usage plan."
  },
  "ModifyApi": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of API's service."
      },
      {
        "name": "ServiceType",
        "desc": "API backend service type. Valid values: HTTP, MOCK, TSF, CLB, SCF, WEBSOCKET, TARGET (in beta test)."
      },
      {
        "name": "RequestConfig",
        "desc": "Request frontend configuration."
      },
      {
        "name": "ApiId",
        "desc": "Unique API ID."
      },
      {
        "name": "ApiName",
        "desc": "Custom API name."
      },
      {
        "name": "ApiDesc",
        "desc": "Custom API description."
      },
      {
        "name": "ApiType",
        "desc": "API type. Valid values: NORMAL (default value), TSF."
      },
      {
        "name": "AuthType",
        "desc": "API authentication type. Valid values: SECRET, NONE (default), OAUTH."
      },
      {
        "name": "AuthRequired",
        "desc": "Whether signature authentication is required. `True` indicates yes while `False` indicates no. This parameter is to be disused."
      },
      {
        "name": "ServiceTimeout",
        "desc": "API backend service timeout period in seconds."
      },
      {
        "name": "Protocol",
        "desc": "API frontend request type, such as HTTP, HTTPS, or HTTP and HTTPS."
      },
      {
        "name": "EnableCORS",
        "desc": "Whether to enable CORS. `True` indicates yes while `False` indicates no."
      },
      {
        "name": "ConstantParameters",
        "desc": "Constant parameters."
      },
      {
        "name": "RequestParameters",
        "desc": "Frontend request parameters."
      },
      {
        "name": "ApiBusinessType",
        "desc": "This field takes effect when `AuthType` is `OAUTH`. NORMAL: business API. OAUTH: authorization API."
      },
      {
        "name": "ServiceMockReturnMessage",
        "desc": "Returned information of API backend mocking. This parameter is required when `ServiceType` is `Mock`."
      },
      {
        "name": "MicroServices",
        "desc": "List of microservices bound to API."
      },
      {
        "name": "ServiceTsfLoadBalanceConf",
        "desc": "Microservice load balancing configuration."
      },
      {
        "name": "ServiceTsfHealthCheckConf",
        "desc": "Microservice health check configuration."
      },
      {
        "name": "TargetServicesLoadBalanceConf",
        "desc": "`target` type load balancing configuration (in beta test)."
      },
      {
        "name": "TargetServicesHealthCheckConf",
        "desc": "`target` health check configuration (in beta test)."
      },
      {
        "name": "ServiceScfFunctionName",
        "desc": "SCF function name. This parameter takes effect when the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketRegisterFunctionName",
        "desc": "SCF WebSocket registration function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketCleanupFunctionName",
        "desc": "SCF WebSocket cleanup function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketTransportFunctionName",
        "desc": "SCF WebSocket transfer function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceScfFunctionNamespace",
        "desc": "SCF function namespace. This parameter takes effect when the backend type is `SCF`."
      },
      {
        "name": "ServiceScfFunctionQualifier",
        "desc": "SCF function version. This parameter takes effect when the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketRegisterFunctionNamespace",
        "desc": "SCF WebSocket registration function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketRegisterFunctionQualifier",
        "desc": "SCF WebSocket transfer function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketTransportFunctionNamespace",
        "desc": "SCF WebSocket transfer function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketTransportFunctionQualifier",
        "desc": "SCF WebSocket transfer function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketCleanupFunctionNamespace",
        "desc": "SCF WebSocket cleanup function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketCleanupFunctionQualifier",
        "desc": "SCF WebSocket cleanup function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceScfIsIntegratedResponse",
        "desc": "Whether to enable response integration. This parameter takes effect when the backend type is `SCF`."
      },
      {
        "name": "IsDebugAfterCharge",
        "desc": "Billing after debugging starts (reserved for marketplace)."
      },
      {
        "name": "TagSpecifications",
        "desc": "Tag."
      },
      {
        "name": "IsDeleteResponseErrorCodes",
        "desc": "Whether to delete the custom response configuration error codes. If the value is left empty or `False`, the error codes will not be deleted. If the value is `True`, all custom response configuration error codes of the API will be deleted."
      },
      {
        "name": "ResponseType",
        "desc": "Return type."
      },
      {
        "name": "ResponseSuccessExample",
        "desc": "Successful response sample of custom response configuration."
      },
      {
        "name": "ResponseFailExample",
        "desc": "Response failure sample of custom response configuration."
      },
      {
        "name": "ServiceConfig",
        "desc": "API backend service configuration."
      },
      {
        "name": "AuthRelationApiId",
        "desc": "Unique ID of associated authorization API. This parameter takes effect only when `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API."
      },
      {
        "name": "ServiceParameters",
        "desc": "API backend service parameters."
      },
      {
        "name": "OauthConfig",
        "desc": "OAuth configuration. This parameter takes effect when `AuthType` is `OAUTH`."
      },
      {
        "name": "ResponseErrorCodes",
        "desc": "Custom error code configuration."
      }
    ],
    "desc": "This API is used to modify an API. You can call this API to edit/modify a configured API. The modified API takes effect only after its service is published to the corresponding environment again."
  },
  "DemoteServiceUsagePlan": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "Usage plan ID."
      },
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be demoted."
      },
      {
        "name": "Environment",
        "desc": "Environment name."
      }
    ],
    "desc": "This API is used to demote a usage plan of a service in an environment to the API level.\nTo make authentication and throttling for a service take effect, you need to bind a usage plan to it. This API is used to query all usage plans bound to the service.\nThis operation will be denied if there are no APIs under a service.\nThis operation will also be denied if the current environment has not been published."
  },
  "DescribeLogSearch": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Log start time"
      },
      {
        "name": "EndTime",
        "desc": "Log end time"
      },
      {
        "name": "ServiceId",
        "desc": "Service ID"
      },
      {
        "name": "Filters",
        "desc": "Exact search by `apiid` or `reqid`"
      },
      {
        "name": "Limit",
        "desc": "Number of logs returned at a time. Up to 100 logs can be returned at a time"
      },
      {
        "name": "ConText",
        "desc": "Subsequent content can be obtained based on the `ConText` returned last time. Up to 10,000 data entries can be obtained"
      },
      {
        "name": "Sort",
        "desc": "Log sorting by time in ascending order (asc) or descending order (desc). The default value is `desc`"
      },
      {
        "name": "Query",
        "desc": "Fuzzy search of logs by keyword"
      }
    ],
    "desc": "This API is used to search for logs."
  },
  "DescribeUsagePlanSecretIds": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "Unique ID of bound usage plan."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to query the list of keys bound to a usage plan.\nIn API Gateway, a usage plan can be bound to multiple key pairs. You can use this API to query the list of keys bound to it."
  },
  "DescribeServiceSubDomains": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique service ID."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to query the list of custom domain names.\nIn API Gateway, you can bind custom domain names to a service for service call. This API is used to query the list of custom domain names bound to a service."
  },
  "ModifyIPStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service of the policy to be modified."
      },
      {
        "name": "StrategyId",
        "desc": "Unique ID of the policy to be modified."
      },
      {
        "name": "StrategyData",
        "desc": "Details of the policy to be modified."
      }
    ],
    "desc": "This API is used to modify a service IP policy."
  },
  "DeleteService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be deleted."
      }
    ],
    "desc": "This API is used to delete a service in API Gateway."
  },
  "UpdateService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be switch to."
      },
      {
        "name": "EnvironmentName",
        "desc": "Name of the environment to be switched to. Valid values: test (testing environment), prepub (pre-publish environment), release (release environment)."
      },
      {
        "name": "VersionName",
        "desc": "Number of the version to be switched to."
      },
      {
        "name": "UpdateDesc",
        "desc": "Switch description."
      }
    ],
    "desc": "This API is used to switch the running version published in an environment of a service to a specified version. After you create a service by using API Gateway and publish it to an environment, multiple versions will be generated during development. In this case, you can call this API to switch versions."
  },
  "UnReleaseService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be deactivated."
      },
      {
        "name": "EnvironmentName",
        "desc": "Name of the environment to be deactivated. Valid values: test (testing environment), prepub (pre-publish environment), release (release environment)."
      },
      {
        "name": "ApiIds",
        "desc": "List of APIs to be deactivated, which is a reserved field."
      }
    ],
    "desc": "This API is used to deactivate a service.\nOnly when a service is published to an environment can its APIs be called by callers. You can call this API to deactivate a service from the release environment. Once deactivated, the service cannot be called."
  },
  "ModifyApiIncrement": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Service ID"
      },
      {
        "name": "ApiId",
        "desc": "API ID"
      },
      {
        "name": "BusinessType",
        "desc": "Authorization type of the API to be modified (you can select `OAUTH`, i.e., authorization API)"
      },
      {
        "name": "PublicKey",
        "desc": "Public key value to be modified of OAuth API"
      },
      {
        "name": "LoginRedirectUrl",
        "desc": "OAuth API redirect address"
      }
    ],
    "desc": "This API is used to incrementally update an API and mainly called by programs (different from `ModifyApi`, which requires full API parameters be passed in and is suitable for being used with the console)."
  },
  "DescribeServiceEnvironmentReleaseHistory": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be queried."
      },
      {
        "name": "EnvironmentName",
        "desc": "Environment name."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to query the release history of a service environment.\nA service can only be used when it is published to an environment after creation. This API is used to query the release history of an environment under a service."
  },
  "DescribeApiUsagePlan": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be queried."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to query the details of API usage plans in a service.\nTo make authentication and throttling for a service takes effect, you need to bind usage plans to it. This API is used to query all usage plans bound to a service and APIs under it."
  },
  "DeleteApi": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of API's service."
      },
      {
        "name": "ApiId",
        "desc": "Unique API ID."
      }
    ],
    "desc": "This API is used to delete a created API."
  },
  "ModifyService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be modified."
      },
      {
        "name": "ServiceName",
        "desc": "Modified service name."
      },
      {
        "name": "ServiceDesc",
        "desc": "Modified service description."
      },
      {
        "name": "Protocol",
        "desc": "Modified service frontend request type, such as `http`, `https`, and `http&https`."
      },
      {
        "name": "NetTypes",
        "desc": "Network type list, which is used to specify the supported network types. `INNER` indicates access over private network, and `OUTER` indicates access over public network. The default value is `OUTER`."
      }
    ],
    "desc": "This API is used to modify the relevant information of a service. After a service is created, its name, description, and service type all can be modified."
  },
  "DescribeServiceUsagePlan": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be queried."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to query the details of usage plans in a service.\nTo make authentication and throttling for a service take effect, you need to bind a usage plan to it. This API is used to query all usage plans bound to the service."
  },
  "ModifyServiceEnvironmentStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique service ID."
      },
      {
        "name": "Strategy",
        "desc": "Throttling value."
      },
      {
        "name": "EnvironmentNames",
        "desc": "Environment list."
      }
    ],
    "desc": "This API is used to modify a service throttling policy."
  },
  "CreateUsagePlan": {
    "params": [
      {
        "name": "UsagePlanName",
        "desc": "Custom usage plan name."
      },
      {
        "name": "UsagePlanDesc",
        "desc": "Custom usage plan description."
      },
      {
        "name": "MaxRequestNum",
        "desc": "Total number of requests allowed. Valid values: -1, [1,99999999]. The default value is `-1`, which indicates no limit."
      },
      {
        "name": "MaxRequestNumPreSec",
        "desc": "Limit of requests per second. Valid values: -1, [1,2000]. The default value is `-1`, which indicates no limit."
      }
    ],
    "desc": "This API is used to create a usage plan.\nTo use API Gateway, you need to create a usage plan and bind it to a service environment."
  },
  "DeleteApiKey": {
    "params": [
      {
        "name": "AccessKeyId",
        "desc": "ID of the key to be deleted."
      }
    ],
    "desc": "This API is used to delete an API key pair."
  },
  "UpdateApiKey": {
    "params": [
      {
        "name": "AccessKeyId",
        "desc": "ID of the key to be updated."
      },
      {
        "name": "AccessKeySecret",
        "desc": "Key to be updated, which is required when a custom key is updated. It can contain 10 to 50 letters, digits, and underscores."
      }
    ],
    "desc": "This API is used to update a created API key pair."
  },
  "ModifyUsagePlan": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "Unique usage plan ID."
      },
      {
        "name": "UsagePlanName",
        "desc": "Modified custom usage plan name."
      },
      {
        "name": "UsagePlanDesc",
        "desc": "Modified custom usage plan description."
      },
      {
        "name": "MaxRequestNum",
        "desc": "Total number of requests allowed. Valid values: -1, [1,99999999]. The default value is `-1`, which indicates no limit."
      },
      {
        "name": "MaxRequestNumPreSec",
        "desc": "Limit of requests per second. Valid values: -1, [1,2000]. The default value is `-1`, which indicates no limit."
      }
    ],
    "desc": "This API is used to modify the name, description, and QPS of a usage plan."
  },
  "BindEnvironment": {
    "params": [
      {
        "name": "UsagePlanIds",
        "desc": "List of unique IDs of the usage plans to be bound."
      },
      {
        "name": "BindType",
        "desc": "Binding type. Valid values: API, SERVICE (default value)."
      },
      {
        "name": "Environment",
        "desc": "Environment to be bound."
      },
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be bound."
      },
      {
        "name": "ApiIds",
        "desc": "Unique API ID array. This parameter will be required when `bindType` is `API`."
      }
    ],
    "desc": "This API is used to bind a usage plan to a service environment.\nAfter you publish a service to an environment, if the API requires authentication and can be called only when it is bound to a usage plan, you can use this API to bind a usage plan to the specified environment.\nCurrently, a usage plan can be bound to an API; however, under the same service, usage plans bound to a service and usage plans bound to an API cannot coexist. Therefore, in an environment to which a service-level usage plan has already been bound, please use the `DemoteServiceUsagePlan` API to demote it."
  },
  "UnBindSecretIds": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "Unique ID of the usage plan to be unbound."
      },
      {
        "name": "AccessKeyIds",
        "desc": "Array of IDs of the keys to be unbound."
      }
    ],
    "desc": "This API is used to unbind a key from a usage plan."
  },
  "BindIPStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service of the IP policy to be bound."
      },
      {
        "name": "StrategyId",
        "desc": "Unique ID of the IP policy to be bound."
      },
      {
        "name": "EnvironmentName",
        "desc": "Environment to be bound to IP policy"
      },
      {
        "name": "BindApiIds",
        "desc": "List of APIs to be bound to IP policy."
      }
    ],
    "desc": "This API is used to bind an IP policy to an API."
  },
  "UnBindIPStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be unbound."
      },
      {
        "name": "StrategyId",
        "desc": "Unique ID of the IP policy to be unbound."
      },
      {
        "name": "EnvironmentName",
        "desc": "Environment to be unbound."
      },
      {
        "name": "UnBindApiIds",
        "desc": "List of APIs to be unbound."
      }
    ],
    "desc": "This API is used to unbind an IP policy from a service."
  },
  "DescribeUsagePlanEnvironments": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "Unique ID of the usage plan to be queried."
      },
      {
        "name": "BindType",
        "desc": "Binding type. Valid values: API, SERVICE (default value)."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to query the list of environments bound to a usage plan.\nAfter binding a usage plan to environments, you can use this API to query all service environments bound to the usage plan."
  },
  "EnableApiKey": {
    "params": [
      {
        "name": "AccessKeyId",
        "desc": "ID of the key to be enabled."
      }
    ],
    "desc": "This API is used to enable a disabled API key pair."
  },
  "CreateIPStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique service ID."
      },
      {
        "name": "StrategyName",
        "desc": "Custom policy name."
      },
      {
        "name": "StrategyType",
        "desc": "Policy type. Valid values: WHITE (whitelist), BLACK (blacklist)."
      },
      {
        "name": "StrategyData",
        "desc": "Policy details."
      }
    ],
    "desc": "This API is used to create a service IP policy."
  },
  "DescribeServiceReleaseVersion": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be queried."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to query the list of all published versions under a service.\nA service is generally published on several versions. This API can be used to query the published versions."
  },
  "CreateApiKey": {
    "params": [
      {
        "name": "SecretName",
        "desc": "Custom key name."
      },
      {
        "name": "AccessKeyType",
        "desc": "Key type. Valid values: auto, manual (custom key). Default value: auto."
      },
      {
        "name": "AccessKeyId",
        "desc": "Custom key ID, which is required when `AccessKeyType` is `manual`. It can contain 5 to 50 letters, digits, and underscores."
      },
      {
        "name": "AccessKeySecret",
        "desc": "Custom key, which is required when `AccessKeyType` is `manual`. It can contain 10 to 50 letters, digits, and underscores."
      }
    ],
    "desc": "This API is used to create an API key pair."
  },
  "ModifySubDomain": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique service ID."
      },
      {
        "name": "SubDomain",
        "desc": "Custom domain name for which the path mapping is to be modified."
      },
      {
        "name": "IsDefaultMapping",
        "desc": "Whether to change to the default path mapping. true: use the default path mapping. false: use the custom path mapping."
      },
      {
        "name": "CertificateId",
        "desc": "Certificate ID, which is required when the HTTPS protocol is included."
      },
      {
        "name": "Protocol",
        "desc": "Modified custom domain name protocol type. Valid values: http, https, http&https."
      },
      {
        "name": "PathMappingSet",
        "desc": "Modified path mapping list."
      },
      {
        "name": "NetType",
        "desc": "Network type. Valid values: INNER, OUTER."
      }
    ],
    "desc": "This API is used to modify the path mapping in the custom domain name settings of the service. The path mapping rule can be modified before it is bound to the custom domain name."
  },
  "DescribeServiceEnvironmentList": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be queried."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to query the list of environments under a service. All environments and their statuses under the queried service will be returned."
  },
  "DisableApiKey": {
    "params": [
      {
        "name": "AccessKeyId",
        "desc": "ID of the key to be disabled."
      }
    ],
    "desc": "This API is used to disable an API key pair."
  },
  "ReleaseService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be published."
      },
      {
        "name": "EnvironmentName",
        "desc": "Name of the environment to be published. Valid values: test (testing environment), prepub (pre-publish environment), release (release environment)."
      },
      {
        "name": "ReleaseDesc",
        "desc": "Release description."
      },
      {
        "name": "ApiIds",
        "desc": "`apiId` list, which is reserved. Full API release is used by default."
      }
    ],
    "desc": "This API is used to publish a service.\nAn API Gateway service can only be called when it is published to an environment and takes effect after creation. This API is used to publish a service to an environment such as the `release` environment."
  },
  "UnBindEnvironment": {
    "params": [
      {
        "name": "BindType",
        "desc": "Binding type. Valid values: API, SERVICE (default value)."
      },
      {
        "name": "UsagePlanIds",
        "desc": "List of unique IDs of the usage plans to be bound."
      },
      {
        "name": "Environment",
        "desc": "Service environment to be unbound."
      },
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be unbound."
      },
      {
        "name": "ApiIds",
        "desc": "Unique API ID array. This parameter will be required when `BindType` is `API`."
      }
    ],
    "desc": "This API is used to unbind a usage plan from a specified environment."
  },
  "DescribeApiEnvironmentStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service of API."
      },
      {
        "name": "EnvironmentNames",
        "desc": "Environment list."
      },
      {
        "name": "ApiId",
        "desc": "Unique API ID."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to display the throttling policies bound to an API."
  },
  "UnBindSubDomain": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique service ID."
      },
      {
        "name": "SubDomain",
        "desc": "Custom domain name to be unbound."
      }
    ],
    "desc": "This API is used to unbind a custom domain name.\nAfter binding a custom domain name to a service using API Gateway, you can use this API to unbind it."
  },
  "DescribeServiceEnvironmentStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique service ID."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to display service throttling policies."
  },
  "DescribeService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service to be queried."
      }
    ],
    "desc": "This API is used to query the details of a service, such as its description, domain name, protocol, creation time, and releases."
  },
  "DeleteServiceSubDomainMapping": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique service ID."
      },
      {
        "name": "SubDomain",
        "desc": "Custom domain name bound to service."
      },
      {
        "name": "Environment",
        "desc": "Name of the environment whose mapping is to be deleted. Valid values: test (testing environment), prepub (pre-publish environment), release (release environment)."
      }
    ],
    "desc": "This API is used to delete a custom domain name mapping in a service environment.\nYou can use this API if you use a custom domain name and custom mapping. Please note that if you delete all mappings in all environments, a failure will be returned when this API is called."
  },
  "DescribeApiKey": {
    "params": [
      {
        "name": "AccessKeyId",
        "desc": "API key ID."
      }
    ],
    "desc": "This API is used to query key details.\nAfter creating an API key, you can query its details using this API which will display its key."
  },
  "DescribeUsagePlan": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "Unique ID of the usage plan to be queried."
      }
    ],
    "desc": "This API is used to query the details of a usage plan, such as its name, QPS, creation time, and bound environment."
  },
  "DescribeApi": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of API's service."
      },
      {
        "name": "ApiId",
        "desc": "Unique API ID."
      }
    ],
    "desc": "This API is used to query the detailed information of an API deployed in API Gateway."
  },
  "BindSubDomain": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique service ID."
      },
      {
        "name": "SubDomain",
        "desc": "Custom domain name to be bound."
      },
      {
        "name": "Protocol",
        "desc": "Protocols supported by service. Valid values: http, https, http&https."
      },
      {
        "name": "NetType",
        "desc": "Network type. Valid values: INNER, OUTER."
      },
      {
        "name": "IsDefaultMapping",
        "desc": "Whether to use the default path mapping. The default value is `true`. If the value is `false`, the custom path mapping will be used and `PathMappingSet` is required."
      },
      {
        "name": "NetSubDomain",
        "desc": "Default domain name."
      },
      {
        "name": "CertificateId",
        "desc": "Unique ID of the certificate of the custom domain name to be bound. The certificate can be uploaded only when `Protocol` is `https` or `http&https`."
      },
      {
        "name": "PathMappingSet",
        "desc": "Custom domain name path mapping. It can contain up to 3 `Environment` parameters which can be set to only `test`, `prepub`, or `release`."
      }
    ],
    "desc": "This API is used to bind a custom domain name to a service.\nEach service in API Gateway provides a default domain name for users to call. If you want to use your own domain name, you can bind a custom domain name to the target service. After getting the ICP filing and configuring the CNAME record between the custom and default domain names, you can directly call the custom domain name."
  },
  "DeleteIPStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of the service of the IP policy to be deleted."
      },
      {
        "name": "StrategyId",
        "desc": "Unique ID of the IP policy to be deleted."
      }
    ],
    "desc": "This API is used to delete a service IP policy."
  },
  "GenerateApiDocument": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique service ID of the document to be created."
      },
      {
        "name": "GenEnvironment",
        "desc": "Environment of the service for which the SDK is to be created."
      },
      {
        "name": "GenLanguage",
        "desc": "Programming language of the SDK to be created. Currently, only Python and JavaScript are supported."
      }
    ],
    "desc": "This API is used to automatically generate API documentation and SDKs. A document and an SDK will be generated for each environment under each service, respectively."
  },
  "BindSecretIds": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "Unique ID of the usage plan to be bound."
      },
      {
        "name": "AccessKeyIds",
        "desc": "Array of IDs of the keys to be bound."
      }
    ],
    "desc": "This API is used to bind a key to a usage plan.\nYou can bind a key to a usage plan and bind the usage plan to an environment where a service is published, so that callers can use the key to call APIs in the service. You can use this API to bind a key to a usage plan."
  },
  "CreateApi": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique ID of API's service."
      },
      {
        "name": "ServiceType",
        "desc": "API backend service type. Valid values: HTTP, MOCK, TSF, CLB, SCF, WEBSOCKET, TARGET (in beta test)."
      },
      {
        "name": "ServiceTimeout",
        "desc": "API backend service timeout period in seconds."
      },
      {
        "name": "Protocol",
        "desc": "API frontend request type, such as HTTP, HTTPS, or HTTP and HTTPS."
      },
      {
        "name": "RequestConfig",
        "desc": "Request frontend configuration."
      },
      {
        "name": "ApiName",
        "desc": "Custom API name."
      },
      {
        "name": "ApiDesc",
        "desc": "Custom API description."
      },
      {
        "name": "ApiType",
        "desc": "API type. Valid values: NORMAL (general API), TSF (microservice API). Default value: NORMAL."
      },
      {
        "name": "AuthType",
        "desc": "API authentication type. Valid values: SECRET (key pair authentication), NONE (no authentication), OAUTH. Default value: NONE."
      },
      {
        "name": "EnableCORS",
        "desc": "Whether to enable CORS."
      },
      {
        "name": "ConstantParameters",
        "desc": "Constant parameters."
      },
      {
        "name": "RequestParameters",
        "desc": "Frontend request parameters."
      },
      {
        "name": "ApiBusinessType",
        "desc": "This field takes effect when `AuthType` is `OAUTH`. NORMAL: business API. OAUTH: authorization API."
      },
      {
        "name": "ServiceMockReturnMessage",
        "desc": "Returned information of API backend mocking. This parameter is required when `ServiceType` is `Mock`."
      },
      {
        "name": "MicroServices",
        "desc": "List of microservices bound to API."
      },
      {
        "name": "ServiceTsfLoadBalanceConf",
        "desc": "Microservice load balancing configuration."
      },
      {
        "name": "ServiceTsfHealthCheckConf",
        "desc": "Microservice health check configuration."
      },
      {
        "name": "TargetServices",
        "desc": "`target` type backend resource information (in beta test)."
      },
      {
        "name": "TargetServicesLoadBalanceConf",
        "desc": "`target` type load balancing configuration (in beta test)."
      },
      {
        "name": "TargetServicesHealthCheckConf",
        "desc": "`target` health check configuration (in beta test)."
      },
      {
        "name": "ServiceScfFunctionName",
        "desc": "SCF function name. This parameter takes effect when the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketRegisterFunctionName",
        "desc": "SCF WebSocket registration function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketCleanupFunctionName",
        "desc": "SCF WebSocket cleanup function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketTransportFunctionName",
        "desc": "SCF WebSocket transfer function. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceScfFunctionNamespace",
        "desc": "SCF function namespace. This parameter takes effect when the backend type is `SCF`."
      },
      {
        "name": "ServiceScfFunctionQualifier",
        "desc": "SCF function version. This parameter takes effect when the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketRegisterFunctionNamespace",
        "desc": "SCF WebSocket registration function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketRegisterFunctionQualifier",
        "desc": "SCF WebSocket transfer function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketTransportFunctionNamespace",
        "desc": "SCF WebSocket transfer function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketTransportFunctionQualifier",
        "desc": "SCF WebSocket transfer function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketCleanupFunctionNamespace",
        "desc": "SCF WebSocket cleanup function namespace. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceWebsocketCleanupFunctionQualifier",
        "desc": "SCF WebSocket cleanup function version. This parameter takes effect when the frontend type is `WEBSOCKET` and the backend type is `SCF`."
      },
      {
        "name": "ServiceScfIsIntegratedResponse",
        "desc": "Whether to enable response integration. This parameter takes effect when the backend type is `SCF`."
      },
      {
        "name": "IsDebugAfterCharge",
        "desc": "Billing after debugging starts (reserved for marketplace)."
      },
      {
        "name": "IsDeleteResponseErrorCodes",
        "desc": "Whether to delete the custom response configuration error codes. If the value is left empty or `False`, the error codes will not be deleted. If the value is `True`, all custom response configuration error codes of the API will be deleted."
      },
      {
        "name": "ResponseType",
        "desc": "Return type."
      },
      {
        "name": "ResponseSuccessExample",
        "desc": "Successful response sample of custom response configuration."
      },
      {
        "name": "ResponseFailExample",
        "desc": "Response failure sample of custom response configuration."
      },
      {
        "name": "ServiceConfig",
        "desc": "API backend service configuration."
      },
      {
        "name": "AuthRelationApiId",
        "desc": "Unique ID of associated authorization API. This parameter takes effect only when `AuthType` is `OAUTH` and `ApiBusinessType` is `NORMAL`. It is the unique ID of the OAuth 2.0 authorization API bound to the business API."
      },
      {
        "name": "ServiceParameters",
        "desc": "API backend service parameters."
      },
      {
        "name": "OauthConfig",
        "desc": "OAuth configuration. This parameter takes effect when `AuthType` is `OAUTH`."
      },
      {
        "name": "ResponseErrorCodes",
        "desc": "Custom error code configuration."
      },
      {
        "name": "TargetNamespaceId",
        "desc": "TSF Serverless namespace ID (in beta test)."
      },
      {
        "name": "UserType",
        "desc": "User type."
      }
    ],
    "desc": "This API is used to create an API. Before creating an API, you need to create a service, as each API belongs to a certain service."
  },
  "DescribeServiceSubDomainMappings": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "Unique service ID."
      },
      {
        "name": "SubDomain",
        "desc": "Custom domain name bound to service."
      }
    ],
    "desc": "This API is used to query the path mappings of a custom domain name.\nIn API Gateway, you can bind a custom domain name to a service and map the paths for it. You can custom different path mappings to up to 3 environments under the service. This API is used to query the list of path mappings of a custom domain name bound to a service."
  }
}