# -*- coding: utf-8 -*-
DESC = "gaap-2018-05-29"
INFO = {
  "DescribeProxyGroupList": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. The default value is 20. The maximum value is 100."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID. Value range:\n-1: all projects of this user\n0: default project\nOther values: specified project"
      },
      {
        "name": "TagSet",
        "desc": "Tag list. If this field exists, the list of the resources with the tag will be pulled.\nIt supports up to 5 tags. If there are two or more tags, the connection groups tagged any of them will be pulled."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions.   \nThe limit on Filter.Values of each request is 5.\nRealServerRegion - String - Required: No - Filter by origin server region; Refer to the RegionId in the results returned by DescribeDestRegions API."
      }
    ],
    "desc": "This API (DescribeProxyGroupList) is used to pull the list of connection groups and the basic information of each connection group."
  },
  "OpenSecurityPolicy": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "ID of the connections requiring enabled security policies."
      }
    ],
    "desc": "This API is used to enable security policies."
  },
  "DescribeCertificates": {
    "params": [
      {
        "name": "CertificateType",
        "desc": "Certificate type. Where:\n0: basic authentication configuration;\n1: client CA certificate;\n2: server SSL certificate;\n3: origin server CA certificate;\n4: connection SSL certificate.\n-1: all types.\nThe default value is -1."
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Quantity limit. The default value is 20."
      }
    ],
    "desc": "This API (DescribeCertificates) is used to query the list of available certificates."
  },
  "CreateSecurityRules": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Security policy ID"
      },
      {
        "name": "RuleList",
        "desc": "List of access rules"
      }
    ],
    "desc": "This API is used to add security policy rules."
  },
  "RemoveRealServers": {
    "params": [
      {
        "name": "RealServerIds",
        "desc": "List of origin server IDs"
      }
    ],
    "desc": "This API is used to delete the added origin server (server) IP or domain name."
  },
  "DescribeHTTPSListeners": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "Filter condition. Connection ID."
      },
      {
        "name": "ListenerId",
        "desc": "Filter condition. Exact query by listener IDs."
      },
      {
        "name": "ListenerName",
        "desc": "Filter condition. Exact query by listener names."
      },
      {
        "name": "Port",
        "desc": "Filter condition. Exact query by listener ports."
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0"
      },
      {
        "name": "Limit",
        "desc": "Quantity limit. The default value is 20."
      },
      {
        "name": "SearchValue",
        "desc": "Filter condition. It supports fuzzy query by ports or listener names."
      }
    ],
    "desc": "This API (DescribeHTTPSListeners) is used to query HTTPS listener information."
  },
  "CreateHTTPSListener": {
    "params": [
      {
        "name": "ListenerName",
        "desc": "Listener name"
      },
      {
        "name": "Port",
        "desc": "Listener port, which is based on the listeners of same transport layer protocol (TCP or UDP). The port must be unique."
      },
      {
        "name": "CertificateId",
        "desc": "Server certificate ID"
      },
      {
        "name": "ForwardProtocol",
        "desc": "Protocol types of the forwarding from acceleration connection to origin server: HTTP | HTTPS"
      },
      {
        "name": "ProxyId",
        "desc": "Connection ID"
      },
      {
        "name": "AuthType",
        "desc": "Authentication type, where:\n0: one-way authentication;\n1: mutual authentication.\nThe one-way authentication is used by default."
      },
      {
        "name": "ClientCertificateId",
        "desc": "Client CA certificate ID, which is required only when the mutual authentication is adopted."
      },
      {
        "name": "PolyClientCertificateIds",
        "desc": "IDs of multiple new client CA certificates. This field or the `ClientCertificateId` field is required for mutual authentication only."
      }
    ],
    "desc": "This API (CreateHTTPListener) is used to create an HTTPS listener in the connection instance."
  },
  "DeleteSecurityPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      }
    ],
    "desc": "This API is used to delete security policies."
  },
  "SetAuthentication": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID."
      },
      {
        "name": "Domain",
        "desc": "The domain name requiring advanced configuration, i.e., the domain name of the listener’s forwarding rules."
      },
      {
        "name": "BasicAuth",
        "desc": "Whether to enable the basic authentication:\n0: disable basic authentication;\n1: enable basic authentication.\nThe default value is 0."
      },
      {
        "name": "GaapAuth",
        "desc": "Whether to enable the connection authentication, which is for the origin server to authenticate GAAP.\n0: disable;\n1: enable.\nThe default value is 0."
      },
      {
        "name": "RealServerAuth",
        "desc": "Whether to enable the origin server authentication, which is for GAAP to authenticate the server.\n0: disable;\n1: enable.\nThe default value is 0."
      },
      {
        "name": "BasicAuthConfId",
        "desc": "Basic authentication configuration ID, which is obtained from the certificate management page."
      },
      {
        "name": "GaapCertificateId",
        "desc": "Connection SSL certificate ID, which is obtained from the certificate management page."
      },
      {
        "name": "RealServerCertificateId",
        "desc": "CA certificate ID of the origin server, which is obtained from the certificate management page. When authenticating the origin server, enter this parameter or the `RealServerCertificateIds` parameter."
      },
      {
        "name": "RealServerCertificateDomain",
        "desc": "Domain name of the origin server certificate."
      },
      {
        "name": "PolyRealServerCertificateIds",
        "desc": "CA certificate IDs of multiple origin servers, which are obtained from the certificate management page. When authenticating the origin servers, enter this parameter or the `RealServerCertificateId` parameter."
      }
    ],
    "desc": "This API (SetAuthentication) is used for the advanced authentication configuration of connections, including authentication methods and their certificates. If only supports connections of version 3.0."
  },
  "DeleteRule": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Layer-7 listener ID"
      },
      {
        "name": "RuleId",
        "desc": "Forwarding rule ID"
      },
      {
        "name": "Force",
        "desc": "Whether to make a forced deletion of forwarding rules that have been bound to origin servers. 0: no; 1: yes."
      }
    ],
    "desc": "This API (DeleteRule) is used to delete the forwarding rules of HTTP/HTTPS listeners."
  },
  "DeleteDomainErrorPageInfo": {
    "params": [
      {
        "name": "ErrorPageId",
        "desc": "Unique ID of a custom error page. For more information, please see the response to CreateDomainErrorPageInfo."
      }
    ],
    "desc": "This API is used to delete a custom error code for a domain name."
  },
  "ModifyCertificate": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener instance ID"
      },
      {
        "name": "Domain",
        "desc": "Domain name whose certificate needs to be modified"
      },
      {
        "name": "CertificateId",
        "desc": "New server certificate ID:\nIf CertificateId=default, using the listener certificate."
      },
      {
        "name": "ClientCertificateId",
        "desc": "New client certificate ID:\nIf ClientCertificateId=default, using the listener certificate.\nThis parameter is required only when the mutual authentication is adopted."
      },
      {
        "name": "PolyClientCertificateIds",
        "desc": "List of new IDs of multiple client certificates, where:\nThis parameter or the `ClientCertificateId` parameter is required for mutual authentication only."
      }
    ],
    "desc": "This API (ModifyCertificate) is used to modify a domain name certificate of a listener. domain name certificate. This API is only applicable to connections of version 3.0."
  },
  "DescribeProxyStatistics": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "Connection ID"
      },
      {
        "name": "StartTime",
        "desc": "Start time (2019-03-25 12:00:00)"
      },
      {
        "name": "EndTime",
        "desc": "End time (2019-03-25 12:00:00)"
      },
      {
        "name": "MetricNames",
        "desc": "Statistical metric name list. Values: InBandwidth (inbound bandwidth); OutBandwidth (outbound bandwidth); Concurrent (concurrence); InPackets (inbound packets); OutPackets (outbound packets); PacketLoss (packet loss rate); Latency (latency)."
      },
      {
        "name": "Granularity",
        "desc": "Monitoring granularity. It currently supports: 60, 300, 3,600, and 86,400. Unit: seconds.\nTime range: ≤ 1 day, supported minimum granularity: 60 seconds;\nTime range: ≤ 7 days, supported minimum granularity: 3,600 seconds;\nTime range: ≤ 30 days, supported minimum granularity: 86,400 seconds;"
      }
    ],
    "desc": "This API is used to query listener statistics, including inbound/outbound bandwidth, inbound/outbound packets, concurrence, packet loss, and latency data. It supports granularities of 300, 3,600, and 86,400. Default value is the highest within the granularity range."
  },
  "CreateRule": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Layer-7 listener ID"
      },
      {
        "name": "Domain",
        "desc": "Domain name of the forwarding rule"
      },
      {
        "name": "Path",
        "desc": "Path of the forwarding rule"
      },
      {
        "name": "RealServerType",
        "desc": "The origin server type of the forwarding rule, which supports IP and DOMAIN types."
      },
      {
        "name": "Scheduler",
        "desc": "Forwarding rules of origin server, which supports round robin (rr), weighted round robin (wrr), and least connections (lc)."
      },
      {
        "name": "HealthCheck",
        "desc": "Whether the health check is enabled for rules. 1: enabled; 0: disabled."
      },
      {
        "name": "CheckParams",
        "desc": "Parameters related to origin server health check"
      },
      {
        "name": "ForwardProtocol",
        "desc": "Protocol types of the forwarding from acceleration connection to origin server, which supports HTTP or HTTPS.\nIf this field is not passed in, it indicates that the ForwardProtocol of the corresponding listener will be used."
      },
      {
        "name": "ForwardHost",
        "desc": "Remote host to which the acceleration connection forwards. If this parameter is not specified, the default host will be used, i.e., the host with which the client initiates HTTP requests."
      }
    ],
    "desc": "This API (CreateRule) is used to create the forwarding rules of HTTP/HTTPS listeners."
  },
  "DescribeDestRegions": {
    "params": [],
    "desc": "This API (DescribeDestRegions) is used to query an origin server region (i.e., the region in which the origin server locates)."
  },
  "CreateDomainErrorPageInfo": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "Domain",
        "desc": "Domain name"
      },
      {
        "name": "ErrorNos",
        "desc": "Original error code"
      },
      {
        "name": "Body",
        "desc": "New response packet"
      },
      {
        "name": "NewErrorNo",
        "desc": "New error code"
      },
      {
        "name": "ClearHeaders",
        "desc": "Response header to be deleted"
      },
      {
        "name": "SetHeaders",
        "desc": "Response header to be set"
      }
    ],
    "desc": "This API is used to customize the error code of an error response to the specified domain name."
  },
  "DescribeProxyGroupStatistics": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Connection group ID"
      },
      {
        "name": "StartTime",
        "desc": "Start time"
      },
      {
        "name": "EndTime",
        "desc": "End time"
      },
      {
        "name": "MetricNames",
        "desc": "Statistical metric name list. Values: InBandwidth (inbound bandwidth); OutBandwidth (outbound bandwidth); Concurrent (concurrence); InPackets (inbound packets); OutPackets (outbound packets)."
      },
      {
        "name": "Granularity",
        "desc": "Monitoring granularity. It currently supports: 60, 300, 3,600, 86,400. Unit: seconds.\nTime range: ≤ 1 day, supported minimum granularity: 60 seconds;\nTime range: ≤ 7 days, supported minimum granularity: 3,600 seconds;\nTime range: ≤ 30 days, supported minimum granularity: 86,400 seconds;"
      }
    ],
    "desc": "This API is used to query listener statistics, including inbound/outbound bandwidth, inbound/outbound packets, and concurrence data. It supports granularities of 300, 3,600, and 86,400. Default value is the highest within the granularity range."
  },
  "DescribeSecurityPolicyDetail": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Security policy ID"
      }
    ],
    "desc": "This API is used to obtain security policy details."
  },
  "ModifyDomain": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Layer-7 listener ID"
      },
      {
        "name": "OldDomain",
        "desc": "Original domain name information"
      },
      {
        "name": "NewDomain",
        "desc": "New domain name information"
      },
      {
        "name": "CertificateId",
        "desc": "Server SSL certificate ID. It’s only applicable to the connections of version 3.0:\nIf this field is not passed in, the original certificate will be used;\nIf this field is passed in, and CertificateId=default, the listener certificate will be used;\nFor other cases, the certificate specified by CertificateId will be used."
      },
      {
        "name": "ClientCertificateId",
        "desc": "Client CA certificate ID. It’s only applicable to the connections of version 3.0:\nIf this field is not passed in, the original certificate will be used;\nIf this field is passed in, and ClientCertificateId=default, the listener certificate will be used;\nFor other cases, the certificate specified by ClientCertificateId will be used."
      },
      {
        "name": "PolyClientCertificateIds",
        "desc": "Client CA certificate ID. It is only applicable to connections on version 3.0, where:\nIf this field and `ClientCertificateId` are not included, the original certificate will be used;\nIf this field is included, and ClientCertificateId=default, then the listener certificate will be used;\nIn other cases, the certificate specified by `ClientCertificateId` or `PolyClientCertificateIds` will be used."
      }
    ],
    "desc": "This API (ModifyDomain) is used to modify domain names of listeners. For connections of version 3.0, it supports modifying certificates of the domain names."
  },
  "ModifyCertificateAttributes": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "Certificate ID."
      },
      {
        "name": "CertificateAlias",
        "desc": "Certificate name. Up to 50 characters."
      }
    ],
    "desc": "This API (ModifyCertificateAttributes) is used to modify certificates, including identification name and certificate content."
  },
  "CloseProxies": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Connection instance ID; It’s an old parameter, please switch to ProxyIds."
      },
      {
        "name": "ClientToken",
        "desc": "A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.\nFor more information, please see How to Ensure Idempotence."
      },
      {
        "name": "ProxyIds",
        "desc": "Connection instance ID; It’s a new parameter."
      }
    ],
    "desc": "This API (CloseProxies) is used to disable connections. If disabled, no traffic will be generated, but the basic configuration fee will still be incurred."
  },
  "OpenProxies": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "List of connection instance IDs; It’s an old parameter, please switch to ProxyIds."
      },
      {
        "name": "ClientToken",
        "desc": "A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.\nFor more information, please see How to Ensure Idempotence."
      },
      {
        "name": "ProxyIds",
        "desc": "List of connection instance IDs; It’s a new parameter."
      }
    ],
    "desc": "This API (OpenProxies) is used to enable one or more connections."
  },
  "ModifyRealServerName": {
    "params": [
      {
        "name": "RealServerName",
        "desc": "Origin server name"
      },
      {
        "name": "RealServerId",
        "desc": "Origin server ID"
      }
    ],
    "desc": "This API (ModifyRealServerName) is used to modify origin server names."
  },
  "DescribeHTTPListeners": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "Connection ID"
      },
      {
        "name": "ListenerId",
        "desc": "Filter condition. Exact query by listener IDs."
      },
      {
        "name": "ListenerName",
        "desc": "Filter condition. Exact query by listener names."
      },
      {
        "name": "Port",
        "desc": "Filter condition. Exact query by listener ports."
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Quantity limit. The default value is 20."
      },
      {
        "name": "SearchValue",
        "desc": "Filter condition. It supports fuzzy query by ports or listener names. This parameter cannot be used with `ListenerName` or `Port`."
      }
    ],
    "desc": "This API (DescribeHTTPListeners) is used to query HTTP listener information."
  },
  "CheckProxyCreate": {
    "params": [
      {
        "name": "AccessRegion",
        "desc": "Access (acceleration) region of the connection. The value can be obtained via the DescribeAccessRegionsByDestRegion API."
      },
      {
        "name": "RealServerRegion",
        "desc": "Origin server region of the connection. The value can be obtained via the DescribeDestRegions API."
      },
      {
        "name": "Bandwidth",
        "desc": "Connection bandwidth cap. Unit: Mbps."
      },
      {
        "name": "Concurrent",
        "desc": "Connection concurrence cap, which indicates the maximum number of simultaneous online connections. Unit: 10,000 connections."
      }
    ],
    "desc": "This API (CheckProxyCreate) is used to query whether an acceleration connection with the specified configuration can be created."
  },
  "DescribeRules": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Layer-7 listener ID."
      }
    ],
    "desc": "This API (DescribeRules) is used to query all rule information of a listener, including the domain names, paths, and list of bound origin servers. For version 3.0 connections, this API returns the advanced authentication configuration information of the domain name."
  },
  "DescribeAccessRegions": {
    "params": [],
    "desc": "This API (DescribeAccessRegions) is used to query acceleration region (client access region)."
  },
  "DeleteSecurityRules": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "Security policy ID"
      },
      {
        "name": "RuleIdList",
        "desc": "List of access rule IDs"
      }
    ],
    "desc": "This API is used to delete security policy rules."
  },
  "DescribeProxyGroupDetails": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Connection group ID."
      }
    ],
    "desc": "This API (DescribeProxyGroupDetails) is used to query connection group details."
  },
  "CreateProxy": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "Project ID of connection."
      },
      {
        "name": "ProxyName",
        "desc": "Connection name."
      },
      {
        "name": "AccessRegion",
        "desc": "Access region."
      },
      {
        "name": "Bandwidth",
        "desc": "Connection bandwidth cap. Unit: Mbps."
      },
      {
        "name": "Concurrent",
        "desc": "Connection concurrence cap, which indicates the maximum number of simultaneous online connections. Unit: 10,000 connections."
      },
      {
        "name": "RealServerRegion",
        "desc": "Origin server region. If GroupId exists, the origin server region is the one of connection group, and this field is not required. If GroupId does not exist, this field is reuqired."
      },
      {
        "name": "ClientToken",
        "desc": "A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.\nFor more information, please see How to Ensure Idempotence."
      },
      {
        "name": "GroupId",
        "desc": "Connection group ID. This parameter is required when the connection is created in the connection group. Otherwise, this field is ignored."
      },
      {
        "name": "TagSet",
        "desc": "List of tags to be added for connection."
      },
      {
        "name": "ClonedProxyId",
        "desc": "ID of the replicated connection. Only a running connection can be replicated.\nThe connection is to be replicated if this parameter is set."
      },
      {
        "name": "BillingType",
        "desc": "Billing mode (0: bill-by-bandwidth, 1: bill-by-traffic. Default value: bill-by-bandwidth)"
      }
    ],
    "desc": "This API (CreateProxy) is used to create an acceleration connection with specified configuration."
  },
  "DeleteCertificate": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "ID of the certificate to be deleted."
      }
    ],
    "desc": "This API (DeleteCertificate) is used to delete certificates."
  },
  "CreateSecurityPolicy": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "Acceleration connection ID"
      },
      {
        "name": "DefaultAction",
        "desc": "Default policy: ACCEPT or DROP"
      }
    ],
    "desc": "This API is used to create security policies."
  },
  "DescribeProxies": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Queries by one or multiple instance IDs. The upper limit on the number of instances for each request is 100. This parameter does not support specifying InstanceIds and Filters at the same time. It’s an old parameter, please switch to ProxyIds."
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. The default value is 20, and the maximum value is 100."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions.   \nThe upper limit on Filters for each request is 10, and the upper limit on Filter.Values is 5. This parameter does not support specifying InstanceIds and Filters at the same time. \nProjectId - String - Required: No - Filter by a project ID.    \nAccessRegion - String - Required: No - Filter by an access region.    \nRealServerRegion - String - Required: No - Filter by an origin server region.\nGroupId - String - Required: No - Filter by a connection group ID."
      },
      {
        "name": "ProxyIds",
        "desc": "Queries by one or multiple instance IDs. The upper limit on the number of instances for each request is 100. This parameter does not support specifying InstanceIds and Filters at the same time. It’s a new parameter, and replaces InstanceIds."
      },
      {
        "name": "TagSet",
        "desc": "Tag list. If this field exists, the list of the resources with the tag will be pulled.\nIt supports up to 5 tags. If there are two or more tags, the connections tagged any of them will be pulled."
      },
      {
        "name": "Independent",
        "desc": "When this field is 1, only not-grouped connections are pulled.\nWhen this field is 0, only grouped connections are pulled.\nWhen this field does not exist, all connections are pulled, including both not-grouped and grouped connections."
      }
    ],
    "desc": "This API (DescribeProxies) is used to query the connection instance list."
  },
  "ModifyHTTPListenerAttribute": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID to be modified"
      },
      {
        "name": "ListenerName",
        "desc": "New listener name"
      },
      {
        "name": "ProxyId",
        "desc": "Connection ID"
      }
    ],
    "desc": "This API (ModifyHTTPListenerAttribute) is used to modify the HTTP listener configuration information of a connection. Currently only supports modifying listener name.\nNote: Grouped connections currently do not support HTTP/HTTPS listeners."
  },
  "ModifyProxiesProject": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "The target project ID."
      },
      {
        "name": "InstanceIds",
        "desc": "ID of one or multiple connections to be operated; It’s an old parameter, please switch to ProxyIds."
      },
      {
        "name": "ClientToken",
        "desc": "A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.\nFor more information, please see How to Ensure Idempotence."
      },
      {
        "name": "ProxyIds",
        "desc": "ID of one or multiple connections to be operated; It’s a new parameter."
      }
    ],
    "desc": "This API (ModifyProxiesProject) is used to modify the project to which a connection belongs."
  },
  "DescribeGroupDomainConfig": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Connection group ID."
      }
    ],
    "desc": "This API (DescribeGroupDomainConfig) is used to obtain the domain name resolution configuration details of a connection group."
  },
  "BindRuleRealServers": {
    "params": [
      {
        "name": "RuleId",
        "desc": "Forwarding rule ID"
      },
      {
        "name": "RealServerBindSet",
        "desc": "An information list of the origin servers to bind.\nIf there are origin servers bound already, they will be replaced by this new origin server list.\nIf this field is empty, it indicates unbinding all origin servers of this rule.\nIf the origin server scheduling policy type of this rule is weighted round robin, you need to enter `RealServerWeight`, i.e., the origin server weight. If this field is left empty or for other scheduling types, the default origin server weight is 1."
      }
    ],
    "desc": "This API is used to bind an origin server to the forwarding rules of layer-7 listeners. Note: This API unbinds all previously bound origin servers before binding those selected."
  },
  "DeleteProxyGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "ID of the connection group to be deleted."
      }
    ],
    "desc": "This API (DeleteProxyGroup) is used to delete a connection group."
  },
  "DescribeAccessRegionsByDestRegion": {
    "params": [
      {
        "name": "DestRegion",
        "desc": "Origin server region: the DescribeDestRegions API returns the value of `RegionId` field of `DestRegionSet`."
      }
    ],
    "desc": "This API (DescribeAccessRegionsByDestRegion) is used to query the list of the available acceleration regions based on the origin server region."
  },
  "ModifyHTTPSListenerAttribute": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "ProxyId",
        "desc": "Connection ID. This field is required if using a single connection listener."
      },
      {
        "name": "ListenerName",
        "desc": "New listener name"
      },
      {
        "name": "ForwardProtocol",
        "desc": "Type of the protocol used in the forwarding from connections to origin servers"
      },
      {
        "name": "CertificateId",
        "desc": "New listener server certificate ID"
      },
      {
        "name": "ClientCertificateId",
        "desc": "New listener client certificate ID"
      },
      {
        "name": "PolyClientCertificateIds",
        "desc": "Client certificate ID of the listener after modification, which is a new field."
      }
    ],
    "desc": "This API (ModifyHTTPSListenerAttribute) is used to modify HTTPS listener configurations. It currently do not support connection groups and connections of version 1.0."
  },
  "CreateDomain": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID."
      },
      {
        "name": "Domain",
        "desc": "Domain name to be created. Each listener supports up to 100 domain names."
      },
      {
        "name": "CertificateId",
        "desc": "Server certificate, which is used for the HTTPS interaction between client and GAAP."
      },
      {
        "name": "ClientCertificateId",
        "desc": "Client CA certificate, which is used for the HTTPS interaction between client and GAAP.\nThis field is required only when the mutual authentication method is adopted."
      },
      {
        "name": "PolyClientCertificateIds",
        "desc": "Client CA certificate, which is used for the HTTPS interaction between the client and GAAP.\nThis field or the `ClientCertificateId` field is required for mutual authentication only."
      }
    ],
    "desc": "This API (CreateDomain) is used to create the access domain name for the HTTP/HTTPS listener. Clients request the backend data by accessing this domain.\nThis API only supports connections of version 3.0."
  },
  "ModifyRuleAttribute": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "RuleId",
        "desc": "Forwarding rule ID"
      },
      {
        "name": "Scheduler",
        "desc": "Scheduling policy:\nrr: round robin;\nwrr: weighted round robin;\nlc: least connections."
      },
      {
        "name": "HealthCheck",
        "desc": "Whether to enable the origin server health check:\n1: enable;\n0: disable."
      },
      {
        "name": "CheckParams",
        "desc": "Health check configuration parameters"
      },
      {
        "name": "Path",
        "desc": "Forwarding rule path"
      },
      {
        "name": "ForwardProtocol",
        "desc": "Protocol types of the forwarding from acceleration connection to origin server, which supports default, HTTP and HTTPS.\nIf `ForwardProtocol=default`, the `ForwardProtocol` of the listener will be used."
      },
      {
        "name": "ForwardHost",
        "desc": "The ‘host’ carried in the request forwarded from the acceleration connection to the origin server.\nIf `ForwardHost=default`, the domain name of rule will be used. For other cases, the value set in this field will be used."
      }
    ],
    "desc": "This API (ModifyRuleAttribute) is used to modify forwarding rule information, including health check configuration and forwarding policies."
  },
  "DescribeCertificateDetail": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "Certificate ID."
      }
    ],
    "desc": "This API (DescribeCertificateDetail) is used to query certificate details, including the certificate ID, name, type, content, key, and other information."
  },
  "CloseSecurityPolicy": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "Connection ID"
      }
    ],
    "desc": "This API is used to disable security policies."
  },
  "ModifyGroupDomainConfig": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Connection group ID."
      },
      {
        "name": "DefaultDnsIp",
        "desc": "Default access IP or domain name of domain name resolution"
      },
      {
        "name": "AccessRegionList",
        "desc": "Nearest access region configuration."
      }
    ],
    "desc": "This API (ModifyGroupDomainConfig) is used to configure the nearest access domain name of a connection group."
  },
  "DescribeTCPListeners": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "Connection ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "ListenerId",
        "desc": "Filter condition. Exact query by listener IDs."
      },
      {
        "name": "ListenerName",
        "desc": "Filter condition. Exact query by listener names."
      },
      {
        "name": "Port",
        "desc": "Filter condition. Exact query by listener ports."
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Quantity limit. The default value is 20."
      },
      {
        "name": "GroupId",
        "desc": "Connection group ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "SearchValue",
        "desc": "Filter condition. It supports fuzzy query by ports or listener names. This parameter cannot be used with `ListenerName` or `Port`."
      }
    ],
    "desc": "This API (DescribeTCPListeners) is used to query the TCP listener information of a single connection or connection group."
  },
  "DescribeDomainErrorPageInfo": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "Domain",
        "desc": "Domain name"
      }
    ],
    "desc": "This API is used to query the custom error response to a domain name."
  },
  "DescribeRealServers": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "Queries the project ID to which the origin server belongs. -1: all projects."
      },
      {
        "name": "SearchValue",
        "desc": "Origin server IP or domain name to be queried. The fuzzy match is supported."
      },
      {
        "name": "Offset",
        "desc": "Offset, which is 0 by default."
      },
      {
        "name": "Limit",
        "desc": "Quantity of values to return. The default value is 20 and the maximum value is 50."
      },
      {
        "name": "TagSet",
        "desc": "Tag list. If this field exists, the list of the resources with the tag will be pulled.\nIt supports up to 5 tags. If there are two or more tags, the origin servers tagged any of them will be pulled."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions. The value of the `name` of the `filter` (RealServerName, RealServerIP)"
      }
    ],
    "desc": "This API (DescribeRealServers) is used to query origin server information. It can query all origin server information by project names, and supports fuzzy query by specified IPs or domain names."
  },
  "ModifyUDPListenerAttribute": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "GroupId",
        "desc": "Connection group ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "ProxyId",
        "desc": "Connection ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "ListenerName",
        "desc": "Listener name"
      },
      {
        "name": "Scheduler",
        "desc": "Origin server scheduling policy of listeners"
      }
    ],
    "desc": "This API (ModifyUDPListenerAttribute) is used to modify the UDP listener configuration of a connection instance, including modification of listener names and scheduling policies."
  },
  "DescribeProxyAndStatisticsListeners": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "Project ID"
      }
    ],
    "desc": "This is an internal API. It is used to query the information of connections and listeners from which the statistics can be derived."
  },
  "CreateHTTPListener": {
    "params": [
      {
        "name": "ListenerName",
        "desc": "Listener name"
      },
      {
        "name": "Port",
        "desc": "Listener port, which is based on the listeners of same transport layer protocol (TCP or UDP). The port must be unique."
      },
      {
        "name": "ProxyId",
        "desc": "Connection ID"
      }
    ],
    "desc": "This API (CreateHTTPListener) is used to create an HTTP listener in the connection instance."
  },
  "DescribeUDPListeners": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "Connection ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "ListenerId",
        "desc": "Filter condition. Exact query by listener IDs."
      },
      {
        "name": "ListenerName",
        "desc": "Filter condition. Exact query by listener names."
      },
      {
        "name": "Port",
        "desc": "Filter condition. Exact query by listener ports."
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Quantity limit. The default value is 20."
      },
      {
        "name": "GroupId",
        "desc": "Connection group ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "SearchValue",
        "desc": "Filter condition. It supports fuzzy query by ports or listener names. This parameter cannot be used with `ListenerName` or `Port`."
      }
    ],
    "desc": "This API (DescribeUDPListeners) is used to query the UDP listener information of a single connection or connection group."
  },
  "ModifyProxyConfiguration": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Connection instance ID; It’s an old parameter, please switch to ProxyId."
      },
      {
        "name": "Bandwidth",
        "desc": "Target bandwidth. Unit: Mbps.\nBandwidth or Concurrent must be set. Use the DescribeAccessRegionsByDestRegion API to obtain the value range."
      },
      {
        "name": "Concurrent",
        "desc": "Target concurrence value. Unit: 10,000 connections.\nBandwidth or Concurrent must be set. Use the DescribeAccessRegionsByDestRegion API to obtain the value range."
      },
      {
        "name": "ClientToken",
        "desc": "A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.\nFor more information, please see How to Ensure Idempotence."
      },
      {
        "name": "ProxyId",
        "desc": "Connection instance ID; It’s a new parameter."
      },
      {
        "name": "BillingType",
        "desc": "Billing mode (0: bill-by-bandwidth, 1: bill-by-traffic. Default value: bill-by-bandwidth)"
      }
    ],
    "desc": "This API (ModifyProxyConfiguration) is used to modify connection configurations. You can expand or reduce the capacity based on current business requirements. It only supports connections with a Scalarable of 1. Scalarable can be obtained via DescribeProxies API."
  },
  "ModifyTCPListenerAttribute": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "GroupId",
        "desc": "Connection group ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "ProxyId",
        "desc": "Connection ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "ListenerName",
        "desc": "Listener name"
      },
      {
        "name": "Scheduler",
        "desc": "Origin server scheduling policy of listeners, which supports round robin (rr), weighted round robin (wrr), and least connections (lc)."
      },
      {
        "name": "DelayLoop",
        "desc": "Time interval of origin server health check (unit: seconds). Value range: [5, 300]."
      },
      {
        "name": "ConnectTimeout",
        "desc": "Response timeout of origin server health check (unit: seconds). Value range: [2, 60]. The timeout value shall be less than the time interval for health check DelayLoop."
      },
      {
        "name": "HealthCheck",
        "desc": "Whether to enable health check. 1: enable; 0: disable."
      }
    ],
    "desc": "This API (ModifyTCPListenerAttribute) is used to modify the TCP listener configuration of a connection instance, including health check configuration and scheduling policies."
  },
  "ModifyProxyGroupAttribute": {
    "params": [
      {
        "name": "GroupId",
        "desc": "ID of the connection group to be modified."
      },
      {
        "name": "GroupName",
        "desc": "New connection group name. Up to 30 characters. The extra characters will be truncated."
      }
    ],
    "desc": "This API (ModifyProxyGroupAttribute) is used to modify connection group attributes. It currently only supports modifying connection group name."
  },
  "DescribeGroupAndStatisticsProxy": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "Project ID"
      }
    ],
    "desc": "This is an internal API. It is used to query the information of connections and connection groups from which the statistics can be derived."
  },
  "DescribeRealServerStatistics": {
    "params": [
      {
        "name": "RealServerId",
        "desc": "Origin server ID"
      },
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "WithinTime",
        "desc": "Statistics duration. Unit: hours. It only supports querying statistics for the past 1, 3, 6, 12, and 24 hours."
      },
      {
        "name": "RuleId",
        "desc": "Rule ID"
      }
    ],
    "desc": "This API (DescribeRealServerStatistics) is used to query the statistics of an origin server's health check results. Origin server status displayed as 1: normal, or 0: exceptional. The queried origin server must be bound to a listener or rule. The bound listener or rule ID must be specified when querying. This API supports displaying origin server status statistics for the past 1, 3, 6, 12, and 24 hours, with a granularity of 1 minute."
  },
  "BindListenerRealServers": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "RealServerBindSet",
        "desc": "List of origin servers to be bound. If the origin server scheduling policy type of this listener is weighted round robin, you need to enter the `RealServerWeight`, i.e., the origin server weight. If this field is left empty or for other scheduling types, the default origin server weight is 1."
      }
    ],
    "desc": "This API (BindListenerRealServers) is used for the TCP/UDP listener to bind/unbind the origin server.\nNote: This API unbinds the previously bound origin servers, and binds the origin servers selected for this call. For example, the previously bound origin servers are A, B and C, and the origin servers selected for this call are C, D and E, then the origin servers bound after this call will be C, D and E."
  },
  "CreateProxyGroupDomain": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Connection group ID of the domain name to be enabled."
      }
    ],
    "desc": "This API (CreateProxyGroupDomain) is used to create the connection group domain name, and enable the domain name resolution."
  },
  "CreateProxyGroup": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "Project ID of connection group"
      },
      {
        "name": "GroupName",
        "desc": "Alias of connection group"
      },
      {
        "name": "RealServerRegion",
        "desc": "Origin server region; Reference API: DescribeDestRegions; It returnes the `RegionId` of the parameter `RegionDetail`."
      },
      {
        "name": "TagSet",
        "desc": "Tag list"
      }
    ],
    "desc": "This API (CreateProxyGroup) is used to create a connection group."
  },
  "CreateUDPListeners": {
    "params": [
      {
        "name": "ListenerName",
        "desc": "Listener name"
      },
      {
        "name": "Ports",
        "desc": "List of listener ports"
      },
      {
        "name": "Scheduler",
        "desc": "Origin server scheduling policy of listeners, which supports round robin (rr), weighted round robin (wrr), and least connections (lc)."
      },
      {
        "name": "RealServerType",
        "desc": "Origin server type of listeners, which supports IP or DOMAIN type."
      },
      {
        "name": "ProxyId",
        "desc": "Connection ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "GroupId",
        "desc": "Connection group ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "RealServerPorts",
        "desc": "List of origin server ports, which only supports the listeners of version 1.0 and connection group."
      }
    ],
    "desc": "This API (CreateTCPListeners) is used to batch create UDP listeners of single connections or connection groups."
  },
  "DescribeRegionAndPrice": {
    "params": [],
    "desc": "This API (DescribeRegionAndPrice) is used to obtain the origin server regions and the bandwidth price gradient."
  },
  "ModifySecurityRule": {
    "params": [
      {
        "name": "RuleId",
        "desc": "Rule ID"
      },
      {
        "name": "AliasName",
        "desc": "Rule name: up to 30 characters. The extra characters will be truncated."
      },
      {
        "name": "PolicyId",
        "desc": "Security policy ID"
      }
    ],
    "desc": "This API is used to modify security policy rule names."
  },
  "DescribeProxyDetail": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "Connection ID to be queried."
      }
    ],
    "desc": "This API (DescribeProxyDetail) is used to query connection details."
  },
  "DescribeListenerStatistics": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "StartTime",
        "desc": "Start time"
      },
      {
        "name": "EndTime",
        "desc": "End time"
      },
      {
        "name": "MetricNames",
        "desc": "Statistical metric name list. It supports:[\"InBandwidth\", \"OutBandwidth\", \"Concurrent\", \"InPackets\", \"OutPackets\"]"
      },
      {
        "name": "Granularity",
        "desc": "Monitoring granularity. It currently supports: 300, 3,600, and 86,400. Unit: seconds.\nTime range: ≤ 1 day, supported minimum granularity: 300 seconds;\nTime range：≤ 7 days, supported minimum granularity:3,600 seconds;\nTime range: ＞7 days, supported minimum granularity:86,400 seconds;"
      }
    ],
    "desc": "This API is used to query listener statistics, including inbound/outbound bandwidth, inbound/outbound packets, and concurrence data. It supports granularities of 300, 3,600, and 86,400. Default value is the highest within the granularity range."
  },
  "DescribeRuleRealServers": {
    "params": [
      {
        "name": "RuleId",
        "desc": "Forwarding rule ID"
      }
    ],
    "desc": "This API (DescribeRuleRealServers) is used to query forwarding rules-related origin server information, including information of origin servers that can be bound and have been bound."
  },
  "AddRealServers": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "Project ID corresponding to origin server"
      },
      {
        "name": "RealServerIP",
        "desc": "IP or domain name corresponding to origin server"
      },
      {
        "name": "RealServerName",
        "desc": "Origin server name"
      },
      {
        "name": "TagSet",
        "desc": "Tag list"
      }
    ],
    "desc": "This API is used to add the information of the origin server (server), which supports IP or the domain name."
  },
  "DescribeProxiesStatus": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Connection ID list; It’s an old parameter, please switch to ProxyIds."
      },
      {
        "name": "ProxyIds",
        "desc": "Connection ID list; It’s a new parameter."
      }
    ],
    "desc": "This API (DescribeProxiesStatus) is used to query the connection status list."
  },
  "DescribeSecurityRules": {
    "params": [
      {
        "name": "SecurityRuleIds",
        "desc": "List of security rule IDs. Up to 20 security rules are supported."
      }
    ],
    "desc": "This API is used to query the list of security rules based on security rule ID. It supports querying 1 to 20 security rules at a time."
  },
  "DeleteDomain": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "Domain",
        "desc": "Domain name to be deleted"
      },
      {
        "name": "Force",
        "desc": "Whether to make a forced deletion of forwarding rules that have been bound to origin servers. 0: no; 1: yes.\nWhen not making a forced deletion, if there are rules bound to origin servers, they will not be deleted."
      }
    ],
    "desc": "This API (DeleteDomain) is only applicable to layer-7 listeners. It is used to delete the domain names of this listener, and all the rules under the domain name. All rules bound to the origin server are unbound automatically."
  },
  "CreateCertificate": {
    "params": [
      {
        "name": "CertificateType",
        "desc": "Certificate type. Where:\n0: basic authentication configuration;\n1: indicates client CA certificate;\n2: server SSL certificate;\n3: origin server CA certificate;\n4: connection SSL certificate."
      },
      {
        "name": "CertificateContent",
        "desc": "Certificate content. URL encoding. Where:\nIf the certificate type is basic authentication, enter username/password pair for this parameter. Format: “username:password”, for example, root:FSGdT. The password is `htpasswd` or `openssl`, for example, openssl passwd -crypt 123456.\nWhen the certificate type is CA/SSL certificate, enter the certificate content for this parameter in the format of ‘pem’."
      },
      {
        "name": "CertificateAlias",
        "desc": "Certificate name"
      },
      {
        "name": "CertificateKey",
        "desc": "Key content. URL encoding. This parameter is required only when the certificate type is SSL certificate. The format is ‘pem’."
      }
    ],
    "desc": "This API (CreateCertificate) is used to create the GAAP certificates and configuration files, including basic authentication configuration files, client CA certificates, server SSL certificates, GAAP SSL certificates, and origin server CA certificates."
  },
  "CreateTCPListeners": {
    "params": [
      {
        "name": "ListenerName",
        "desc": "Listener name."
      },
      {
        "name": "Ports",
        "desc": "List of listener ports."
      },
      {
        "name": "Scheduler",
        "desc": "Origin server scheduling policy of listeners, which supports round robin (rr), weighted round robin (wrr), and least connections (lc)."
      },
      {
        "name": "HealthCheck",
        "desc": "Whether origin server has the health check enabled. 1: enabled; 0: disabled. UDP listeners do not support health check."
      },
      {
        "name": "RealServerType",
        "desc": "The origin server type of listeners, supporting IP or DOMAIN type. The DOMAIN origin servers do not support the weighted round robin."
      },
      {
        "name": "ProxyId",
        "desc": "Connection ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "GroupId",
        "desc": "Connection group ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "DelayLoop",
        "desc": "Time interval of origin server health check (unit: seconds). Value range: [5, 300]."
      },
      {
        "name": "ConnectTimeout",
        "desc": "Response timeout of origin server health check (unit: seconds). Value range: [2, 60]. The timeout value shall be less than the time interval for health check DelayLoop."
      },
      {
        "name": "RealServerPorts",
        "desc": "List of origin server ports, which only supports the listeners of version 1.0 and connection group."
      }
    ],
    "desc": "This API (CreateTCPListeners) is used to batch create TCP listeners of single connections or connection groups."
  },
  "ModifyProxiesAttribute": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "ID of one or multiple connections to be operated; It’s an old parameter, please switch to ProxyIds."
      },
      {
        "name": "ProxyName",
        "desc": "Connection name. Up to 30 characters."
      },
      {
        "name": "ClientToken",
        "desc": "A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.\nFor more information, please see How to Ensure Idempotence."
      },
      {
        "name": "ProxyIds",
        "desc": "ID of one or multiple connections to be operated; It’s a new parameter."
      }
    ],
    "desc": "This API (ModifyProxiesAttribute) is used to modify instance attributes (currently only supports modifying connection name)."
  },
  "DestroyProxies": {
    "params": [
      {
        "name": "Force",
        "desc": "The identifier for forced deletion\n1: this connection list is deleted forcibly regardless of whether the origin server has been bound.\n0: this connection list cannot be deleted if the origin server has been bound.\nIf this identifier is 0, the deletion can be performed only when all the connections have not been bound to any origin servers."
      },
      {
        "name": "InstanceIds",
        "desc": "List of connection instance IDs; It’s an old parameter, please switch to ProxyIds."
      },
      {
        "name": "ClientToken",
        "desc": "A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.\nFor more information, please see How to Ensure Idempotence."
      },
      {
        "name": "ProxyIds",
        "desc": "List of connection instance IDs; It’s a new parameter."
      }
    ],
    "desc": "This API (DestroyProxies) is used to terminate a connection. If terminated, no fees will be incurred."
  },
  "DescribeResourcesByTag": {
    "params": [
      {
        "name": "TagKey",
        "desc": "Tag key."
      },
      {
        "name": "TagValue",
        "desc": "Tag value."
      },
      {
        "name": "ResourceType",
        "desc": "Resource type, including:\nProxy (connection);\nProxyGroup (connection group);\nRealServer (origin server).\nIf this field is not specified, all resources with the tag will be queried."
      }
    ],
    "desc": "This API (DescribeResourcesByTag) is used to query corresponding resource information by tags, including connection, connection group, and origin server."
  },
  "DescribeCountryAreaMapping": {
    "params": [],
    "desc": "This API (DescribeCountryAreaMapping) is used to obtain the country/region code mapping table."
  },
  "DescribeListenerRealServers": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      }
    ],
    "desc": "This API (DescribeListenerRealServers) is used to query the origin server list of TCP/UDP listeners, including the list of bound origin servers and origin servers that can be bound."
  },
  "DeleteListeners": {
    "params": [
      {
        "name": "ListenerIds",
        "desc": "ID list of listeners to be deleted"
      },
      {
        "name": "Force",
        "desc": "Whether to allow a forced deletion of listeners that have been bound to origin servers. 1: allowed; 0: not allow."
      },
      {
        "name": "GroupId",
        "desc": "Connection group ID; Either this parameter or `GroupId` must be set, but you cannot set both."
      },
      {
        "name": "ProxyId",
        "desc": "Connection ID; Either this parameter or `GroupId` must be set, but you cannot set both."
      }
    ],
    "desc": "This API (DeleteListeners) is used to batch delete the listeners of a connection or connection group, including layer-4/7 listeners."
  },
  "DescribeRealServersStatus": {
    "params": [
      {
        "name": "RealServerIds",
        "desc": "List of origin server IDs"
      }
    ],
    "desc": "This API (DescribeRealServersStatus) is used to query whether an origin server has been bound to a rule or listener."
  },
  "DescribeRulesByRuleIds": {
    "params": [
      {
        "name": "RuleIds",
        "desc": "List of rule IDs. Up to 10 rules are supported."
      }
    ],
    "desc": "This API is used to pull the list of rules based on rule ID. It supports pulling 1 to 10 rules at a time."
  },
  "InquiryPriceCreateProxy": {
    "params": [
      {
        "name": "AccessRegion",
        "desc": "Acceleration region name."
      },
      {
        "name": "Bandwidth",
        "desc": "Connection bandwidth cap. Unit: Mbps."
      },
      {
        "name": "DestRegion",
        "desc": "Origin server region name. It’s an old parameter, please switch to RealServerRegion."
      },
      {
        "name": "Concurrency",
        "desc": "Upper limit of connection concurrence, which indicates a number of simultaneous online connections. Unit: 10,000 connections. It’s an old parameter, please switch to Concurrent."
      },
      {
        "name": "RealServerRegion",
        "desc": "Origin server region name; It’s a new parameter."
      },
      {
        "name": "Concurrent",
        "desc": "Upper limit of connection concurrence, which indicates a number of simultaneous online connections. Unit: 10,000 connections. It’s a new parameter."
      },
      {
        "name": "BillingType",
        "desc": "Billing mode (0: bill-by-bandwidth, 1: bill-by-traffic. Default value: bill-by-bandwidth)"
      }
    ],
    "desc": "This API (InquiryPriceCreateProxy) is used to create the price inquiries of acceleration connections."
  }
}