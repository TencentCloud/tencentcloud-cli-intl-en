# -*- coding: utf-8 -*-
DESC = "vpc-2017-03-12"
INFO = {
  "DescribeVpcResourceDashboard": {
    "params": [
      {
        "name": "VpcIds",
        "desc": "Vpc instance ID, e.g. vpc-f1xjkw1b."
      }
    ],
    "desc": "This API is used to query the VPC resource information."
  },
  "DescribeCustomerGateways": {
    "params": [
      {
        "name": "CustomerGatewayIds",
        "desc": "Customer gateway ID, such as `cgw-2wqq41m9`. Each request can have a maximum of 100 instances. `CustomerGatewayIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "The filter condition. For details, see the Instance Filter Conditions Table. The upper limit for `Filters` in each request is 10 and 5 for `Filter.Values`. `CustomerGatewayIds` and `Filters` cannot be specified at the same time.\n<li>customer-gateway-id - String - (Filter condition) The unique ID of the user gateway, such as `cgw-mgp33pll`.</li>\n<li>customer-gateway-name - String - (Filter condition) The name of the user gateway, such as `test-cgw`.</li>\n<li>ip-address - String - (Filter condition) The public IP address, such as `58.211.1.12`.</li>"
      },
      {
        "name": "Offset",
        "desc": "The Offset. The default value is 0. For more information about Offset, see the relevant section in the API Introduction."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      }
    ],
    "desc": "This API (DescribeCustomerGateways) is used to query the customer gateway list."
  },
  "ReplaceSecurityGroupPolicy": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "Security group policy set object."
      }
    ],
    "desc": "This API (ReplaceSecurityGroupPolicy) is used to replace a single security group policy (SecurityGroupPolicy).\nOnly one policy in a single direction can be replaced in each request, and the PolicyIndex parameter must be specified."
  },
  "CreateFlowLog": {
    "params": [
      {
        "name": "VpcId",
        "desc": "ID of the VPC instance"
      },
      {
        "name": "FlowLogName",
        "desc": "The name of the flow log instance."
      },
      {
        "name": "ResourceType",
        "desc": "The type of resources to which the flow log belongs. Valid values: 'VPC', 'SUBNET' and 'NETWORKINTERFACE'."
      },
      {
        "name": "ResourceId",
        "desc": "The unique ID of the resource."
      },
      {
        "name": "TrafficType",
        "desc": "Type of the flow logs to be collected. Valid values: `ACCEPT`, `REJECT` and `ALL`."
      },
      {
        "name": "CloudLogId",
        "desc": "The storage ID of the flow log."
      },
      {
        "name": "FlowLogDescription",
        "desc": "The description of the flow log instance"
      }
    ],
    "desc": "This API is used to create a flow log."
  },
  "ModifyNatGatewayAttribute": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      },
      {
        "name": "NatGatewayName",
        "desc": "The NAT gateway name, such as `test_nat`."
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The maximum outbound bandwidth of the NAT gateway. Unit: Mbps."
      }
    ],
    "desc": "This API (ModifyNatGatewayAttribute) is used to modify the attributes of a NAT gateway."
  },
  "DescribeTaskResult": {
    "params": [
      {
        "name": "TaskId",
        "desc": "Async task ID. Either TaskId or DealName must be entered."
      },
      {
        "name": "DealName",
        "desc": "Billing order No. Either TaskId or DealName must be entered."
      }
    ],
    "desc": "This API is used to query the EIP async job execution results."
  },
  "CreateNetworkAcl": {
    "params": [
      {
        "name": "VpcId",
        "desc": "ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of the DescribeVpcs API."
      },
      {
        "name": "NetworkAclName",
        "desc": "Name of the network ACL. The maximum length is 60 bytes."
      }
    ],
    "desc": "This API is used to create a <a href=\"https://cloud.tencent.com/document/product/215/20088\">network ACL</a>.\n* The inbound and outbound rules for a new network ACL are \"Deny All\" by default. You need to call `ModifyNetworkAclEntries` after creation to set rules for the network ACL as needed."
  },
  "DescribeServiceTemplateGroups": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions.\n<li>service-template-group-name - String - (Filter condition) Protocol port template group name.</li>\n<li>service-template-group-id - String - (Filter condition) Protocol port template group instance ID, such as `ppmg-e6dy460g`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeServiceTemplateGroups) is used to query a protocol port template group."
  },
  "DescribeRouteTables": {
    "params": [
      {
        "name": "RouteTableIds",
        "desc": "The route table instance ID, such as `rtb-azd4dt1c`."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `RouteTableIds` and `Filters` cannot be speified at the same time.\n<li>route-table-id - String - (Filter condition) Route table instance ID.</li>\n<li>route-table-name - String - (Filter condition) Route table name.</li>\n<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>\n<li>association.main - String - (Filter condition) Whether it is the main route table.</li>\n<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>\n<li>tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key is replaced with the specific tag key. For usage, refer to case 2.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset."
      },
      {
        "name": "Limit",
        "desc": "The number of request objects."
      }
    ],
    "desc": " This API (DescribeRouteTables) is used to query route tables."
  },
  "CreateBandwidthPackage": {
    "params": [
      {
        "name": "NetworkType",
        "desc": "The bandwidth package type. Valid values: 'BGP', 'SINGLEISP', and 'ANYCAST'."
      },
      {
        "name": "ChargeType",
        "desc": "The bandwidth package billing mode. Valid values: 'TOP5_POSTPAID_BY_MONTH' and 'PERCENT95_POSTPAID_BY_MONTH'."
      },
      {
        "name": "BandwidthPackageName",
        "desc": "The name of the bandwidth package."
      },
      {
        "name": "BandwidthPackageCount",
        "desc": "The number of bandwidth packages (enter 1 for bill-by-CVM accounts)."
      },
      {
        "name": "InternetMaxBandwidth",
        "desc": "The limit of the bandwidth package in Mbps. The value '-1' indicates there is no limit."
      },
      {
        "name": "Tags",
        "desc": "The list of tags to be bound."
      },
      {
        "name": "Protocol",
        "desc": "The protocol type of the bandwidth package. Valid values: 'ipv4' and 'ipv6'. Default value: 'ipv4'."
      }
    ],
    "desc": "This API is used to create [device bandwidth packages](https://cloud.tencent.com/document/product/684/15246#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85) and [IP bandwidth packages](https://cloud.tencent.com/document/product/684/15246#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85)"
  },
  "DeleteFlowLog": {
    "params": [
      {
        "name": "VpcId",
        "desc": "ID of the VPC instance"
      },
      {
        "name": "FlowLogId",
        "desc": "The unique ID of the flow log."
      }
    ],
    "desc": "This API is used to delete a flow log."
  },
  "CreateRouteTable": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance to be operated on. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "RouteTableName",
        "desc": "The route table name. The maximum length is 60 characters."
      },
      {
        "name": "Tags",
        "desc": "Bound tags, such as [{\"Key\": \"city\", \"Value\": \"shanghai\"}]."
      }
    ],
    "desc": "This API is used to create a route table.\n* After the VPC instance has been created, the system creates a default route table with which all newly created subnets will be associated. By default, you can use this route table to manage your routing policies. If you have multiple routing policies, you can call the API for creating route tables to create more route tables to manage these routing policies.\n* You can bind a tag when creating a route table. The tag list in the response indicates the tags that have been successfully added."
  },
  "AssignIpv6CidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the `VPC`, such as `vpc-f49l6u0z`."
      }
    ],
    "desc": "This API is used to assign IPv6 ranges.\n* To use this API, you must already have a VPC instance. If you do not have a VPC instance yet, use the <a href=\"https://cloud.tencent.com/document/api/215/15774\" title=\"CreateVpc\" target=\"_blank\">CreateVpc</a> API to create one.\n* Each VPC can apply for only one IPv6 range."
  },
  "DeleteNetworkAcl": {
    "params": [
      {
        "name": "NetworkAclId",
        "desc": "Network ACL instance ID. Example: acl-12345678."
      }
    ],
    "desc": "This API is used to delete a network ACL."
  },
  "DescribeNatGatewayDestinationIpPortTranslationNatRules": {
    "params": [
      {
        "name": "NatGatewayIds",
        "desc": "NAT gateway ID."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions:\n`NatGatewayIds` and `Filters` cannot be specified at the same time.\n<li> nat-gateway-id, the NAT gateway ID, such as `nat-0yi4hekt`.</li>\n<li> vpc-id, the VPC ID, such as `vpc-0yi4hekt`.</li>\n<li> public-ip-address, the EIP, such as `139.199.232.238`.</li>\n<li>public-port, the public network port.</li>\n<li>private-ip-address, the private IP, such as `10.0.0.1`.</li>\n<li>private-port, the private network port.</li>\n<li>description, the rule description.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeNatGatewayDestinationIpPortTranslationNatRules) is used to query the array of objects of the port forwarding rules for a NAT gateway."
  },
  "ModifyFlowLogAttribute": {
    "params": [
      {
        "name": "VpcId",
        "desc": "ID of the VPC instance"
      },
      {
        "name": "FlowLogId",
        "desc": "The unique ID of the flow log."
      },
      {
        "name": "FlowLogName",
        "desc": "The name of the flow log."
      },
      {
        "name": "FlowLogDescription",
        "desc": "The description of the flow log."
      }
    ],
    "desc": "This API is used to modify the attributes of a flow log."
  },
  "ModifyServiceTemplateGroupAttribute": {
    "params": [
      {
        "name": "ServiceTemplateGroupId",
        "desc": "The protocol port template group instance ID, such as `ppmg-ei8hfd9a`."
      },
      {
        "name": "ServiceTemplateGroupName",
        "desc": "Protocol port template group name."
      },
      {
        "name": "ServiceTemplateIds",
        "desc": "Instance ID of the protocol port template, such as `ppm-4dw6agho`."
      }
    ],
    "desc": "This API (ModifyServiceTemplateGroupAttribute) is used to modify a protocol port template group."
  },
  "ModifyAddressInternetChargeType": {
    "params": [
      {
        "name": "AddressId",
        "desc": "Unique EIP ID, such as \"eip-xxxx\""
      },
      {
        "name": "InternetChargeType",
        "desc": "The target billing method. It can be `BANDWIDTH_PREPAID_BY_MONTH` or `TRAFFIC_POSTPAID_BY_HOUR`"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The target bandwidth value"
      },
      {
        "name": "AddressChargePrepaid",
        "desc": "Billing details of monthly-subscribed network bandwidth. This parameter is required if the target billing method is `BANDWIDTH_PREPAID_BY_MONTH`."
      }
    ],
    "desc": "This API is used to adjust the network billing mode of an EIP. Please note that it's available to users whose network fees are billed on IPs but not CVMs.\n* The network billing mode can be switched between `BANDWIDTH_PREPAID_BY_MONTH` and `TRAFFIC_POSTPAID_BY_HOUR`.\n* The network billing mode for each EIP be changed for up to twice."
  },
  "DescribeCcnAttachedInstances": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      },
      {
        "name": "Filters",
        "desc": "Filter conditions:\n<li>ccn-id - String - (Filter condition) The CCN instance ID.</li>\n<li>instance-type - String - (Filter condition) The associated instance type.</li>\n<li>instance-region - String - (Filter condition) The associated instance region.</li>\n<li>instance-type - String - (Filter condition) The instance ID of the associated instance.</li>"
      },
      {
        "name": "CcnId",
        "desc": "The ID of the CCN instance"
      },
      {
        "name": "OrderField",
        "desc": "The order field supports `CcnId`, `InstanceType`, `InstanceId`, `InstanceName`, `InstanceRegion`, `AttachedTime`, and `State`."
      },
      {
        "name": "OrderDirection",
        "desc": "Order methods. Ascending: `ASC`, Descending: `DESC`."
      }
    ],
    "desc": "This API (DescribeCcnAttachedInstances) is used to query the network instances associated with the CCN instance."
  },
  "ResetRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "The route table instance ID, such as `rtb-azd4dt1c`."
      },
      {
        "name": "RouteTableName",
        "desc": "The route table name. The maximum length is 60 characters."
      },
      {
        "name": "Routes",
        "desc": "Routing policy."
      }
    ],
    "desc": "This API (ResetRoutes) is used to reset the name of a route table and all its routing policies.<br />\nNote: When this API is called, all routing policies in the current route table are deleted before new routing policies are saved, which may incur network interruption."
  },
  "DescribeNetworkInterfaceLimit": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ID of a CVM instance or ENI to query"
      }
    ],
    "desc": "This API (DescribeNetworkInterfaceLimit) is used to query the ENI quota based on the ID of CVM instance or ENI. It returns the ENI quota to which the CVM instance can be bound and the IP address quota that can be allocated to the ENI."
  },
  "DescribeNetDetects": {
    "params": [
      {
        "name": "NetDetectIds",
        "desc": "The array of network detection instance `IDs`, such as [`netd-12345678`]."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions. `NetDetectIds` and `Filters` cannot be specified at the same time.\n<li>vpc-id - String - (Filter condition) The VPC instance ID, such as vpc-12345678.</li>\n<li>net-detect-id - String - (Filter condition) The network detection instance ID, such as netd-12345678.</li>\n<li>subnet-id - String - (Filter condition) The subnet instance ID, such as subnet-12345678.</li>\n<li>net-detect-name - String - (Filter condition) The network detection name.</li>"
      },
      {
        "name": "Offset",
        "desc": "The offset. Default: 0."
      },
      {
        "name": "Limit",
        "desc": "The number of returned values. Default: 20. Maximum: 100."
      }
    ],
    "desc": "This API (DescribeNetDetects) is used to query the list of network detection instances."
  },
  "ModifyCcnRegionBandwidthLimitsType": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN instance ID."
      },
      {
        "name": "BandwidthLimitType",
        "desc": "CCN bandwidth limit type. INTER_REGION_LIMIT: limit between regions. OUTER_REGION_LIMIT: region egress limit."
      }
    ],
    "desc": "This API is used to modify the bandwidth limit policy of a postpaid CCN instance."
  },
  "DescribeGatewayFlowMonitorDetail": {
    "params": [
      {
        "name": "TimePoint",
        "desc": "The point in time. This indicates details of this minute will be queried. For example, in `2019-02-28 18:15:20`, details at `18:15` will be queried."
      },
      {
        "name": "VpnId",
        "desc": "The instance ID of the VPN gateway, such as `vpn-ltjahce6`."
      },
      {
        "name": "DirectConnectGatewayId",
        "desc": "The instance ID of the Direct Connect gateway, such as `dcg-ltjahce6`."
      },
      {
        "name": "PeeringConnectionId",
        "desc": "The instance ID of the peering connection, such as `pcx-ltjahce6`."
      },
      {
        "name": "NatId",
        "desc": "The instance ID of the NAT gateway, such as `nat-ltjahce6`."
      },
      {
        "name": "Offset",
        "desc": "Offset."
      },
      {
        "name": "Limit",
        "desc": "The returned quantity."
      },
      {
        "name": "OrderField",
        "desc": "The order field supports `InPkg`, `OutPkg`, `InTraffic`, and `OutTraffic`."
      },
      {
        "name": "OrderDirection",
        "desc": "Order methods. Ascending: `ASC`, Descending: `DESC`."
      }
    ],
    "desc": "This API (DescribeGatewayFlowMonitorDetail) is used to query the monitoring details of the gateway traffic.\n* Only querying of a single gateway instance is supported. That is, only one of the `VpnId`, `DirectConnectGatewayId`, `PeeringConnectionId`, or `NatId` input parameters is supported, and one must be used.\n* If the gateway has traffic, but no data is returned when this API is called, please check whether gateway traffic monitoring has been enabled in the corresponding gateway details page in the console."
  },
  "EnableGatewayFlowMonitor": {
    "params": [
      {
        "name": "GatewayId",
        "desc": "Gateway instance ID, which currently supports these types:\nID of Direct Connect gateway instance, e.g. `dcg-ltjahce6`;\nID of NAT gateway instance, e.g. `nat-ltjahce6`;\nID of VPN gateway instance, e.g. `vpn-ltjahce6`."
      }
    ],
    "desc": "This API (EnableGatewayFlowMonitor) is used to enable gateway flow monitor."
  },
  "UnassignIpv6Addresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The `ID` of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "Ipv6Addresses",
        "desc": "The list of specified `IPv6` addresses. A maximum of 10 can be specified each time."
      }
    ],
    "desc": "This API (UnassignIpv6Addresses) is used to release ENI `IPv6` addresses.<br />\nThis API is completed asynchronously. If you need to query the async execution results, use the `RequestId` returned by this API to query the `QueryTask` API."
  },
  "DescribeNetworkAcls": {
    "params": [
      {
        "name": "NetworkAclIds",
        "desc": "Array of network ACL instance IDs, such as [acl-12345678]. Up to 100 instances are allowed for each request. This parameter does not support specifying `NetworkAclIds` and `Filters` at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `NetworkAclIds` and `Filters` cannot be specified at the same time.\n<li>vpc-id - String - (Filter condition) VPC instance ID, such as vpc-12345678.</li>\n<li>network-acl-id - String - (Filter condition) Network ACL instance ID, such as acl-12345678.</li>\n<li>network-acl-name - String - (Filter condition) Network ACL instance name.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default: 0."
      },
      {
        "name": "Limit",
        "desc": "Returned quantity. Default: 20. Value range: 1-100."
      }
    ],
    "desc": "This API is used to query a list of network ACLs."
  },
  "DeleteVpnConnection": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "VpnConnectionId",
        "desc": "The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`."
      }
    ],
    "desc": "This API (DeleteVpnConnection) is used to delete VPN tunnels."
  },
  "DeleteAddressTemplateGroup": {
    "params": [
      {
        "name": "AddressTemplateGroupId",
        "desc": "The IP address template group instance ID, such as `ipmg-90cex8mq`."
      }
    ],
    "desc": "This API (DeleteAddressTemplateGroup) is used to delete an IP address template group."
  },
  "DescribeCustomerGatewayVendors": {
    "params": [],
    "desc": "This API (DescribeCustomerGatewayVendors) is used to query the information of supported customer gateway vendors."
  },
  "DescribeAddresses": {
    "params": [
      {
        "name": "AddressIds",
        "desc": "The list of unique IDs of EIPs, such as `eip-11112222`. `AddressIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "The upper limit for `Filters` in each request is 10 and 5 for `Filter.Values`. `AddressIds` and `Filters` cannot be specified at the same time. Detailed filter conditions are as follows:\n<li> address-id - String - Required: no - (Filter condition) The unique EIP ID, such as `eip-11112222`.</li>\n<li> address-name - String - Required: no - (Filter condition) The EIP name. Fuzzy filtering is not supported.</li>\n<li> address-ip - String - Required: no - (Filter condition) Filters by EIP.</li>\n<li> address-status - String - Required: no - (Filter condition) The EIP state. Possible EIP states are: 'CREATING', 'BINDING', 'BIND', 'UNBINDING', 'UNBIND', 'OFFLINING', and 'BIND_ENI'.</li>\n<li> instance-id - String - Required: no - (Filter condition) The ID of the instance bound to the EIP, such as `ins-11112222`.</li>\n<li> private-ip-address - String - Required: no - (Filter condition) The private IP address bound to the EIP.</li>\n<li> network-interface-id - String - Required: no - (Filter condition) The ID of the ENI bound to the EIP, such as `eni-11112222`.</li>\n<li> is-arrears - String - Required: no - (Filter condition) Whether the EIP is in arrears. (TRUE: the EIP is in arrears | FALSE: the billing status of the EIP is normal)</li>"
      },
      {
        "name": "Offset",
        "desc": "The Offset. The default value is 0. For more information on `Offset`, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/product/11646)."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. The default value is 20. The maximum is 100. For more information on `Limit`, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/product/11646)."
      }
    ],
    "desc": "This API (DescribeAddresses) is used to query the information of one or multiple [Elastic IPs](https://cloud.tencent.com/document/product/213/1941).\n* If the parameter is empty, a number (as specified by the `Limit`, the default value is 20) of EIPs will be returned."
  },
  "DescribeClassicLinkInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions.\n<li>vpc-id - String - (Filter condition) The VPC instance ID.</li>\n<li>vm-ip - String - (Filter condition) The IP address of the CVM on the basic network.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      }
    ],
    "desc": "This API (DescribeClassicLinkInstances) is used to query the Classiclink instances list."
  },
  "DescribeSecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups."
      }
    ],
    "desc": "This API (DescribeSecurityGroupPolicies) is used to query security group policies."
  },
  "ModifyServiceTemplateAttribute": {
    "params": [
      {
        "name": "ServiceTemplateId",
        "desc": "Protocol port template instance ID, such as `ppm-529nwwj8`."
      },
      {
        "name": "ServiceTemplateName",
        "desc": "Protocol port template name."
      },
      {
        "name": "Services",
        "desc": "It supports single port, multiple ports, consecutive ports and all ports. Supported protocols include TCP, UDP, ICMP, and GRE."
      }
    ],
    "desc": "This API (ModifyServiceTemplateAttribute) is used to modify a protocol port template."
  },
  "AssociateNatGatewayAddress": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      },
      {
        "name": "AddressCount",
        "desc": "The number of EIPs you want to apply for. The system will create the same number of EIPs as you require. Either `AddressCount` or `PublicAddresses` must be passed in."
      },
      {
        "name": "PublicIpAddresses",
        "desc": "Array of the EIPs bound to the NAT gateway. Either `AddressCount` or `PublicAddresses` must be passed in."
      },
      {
        "name": "Zone",
        "desc": "The availability zone of the EIP, which is passed in when the EIP is automatically assigned."
      }
    ],
    "desc": "This API is used to bind an EIP to NAT Gateway."
  },
  "CreateVpnConnection": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "CustomerGatewayId",
        "desc": "The ID of the customer gateway, such as `cgw-2wqq41m9`. You can query the customer gateway by using the `DescribeCustomerGateways` API."
      },
      {
        "name": "VpnConnectionName",
        "desc": "Gateway can be named freely, but the maximum length is 60 characters."
      },
      {
        "name": "PreShareKey",
        "desc": "The pre-shared key."
      },
      {
        "name": "SecurityPolicyDatabases",
        "desc": "The SPD policy group, for example: {\"10.0.0.5/24\":[\"172.123.10.5/16\"]}. 10.0.0.5/24 is the VPC internal IP range, and 172.123.10.5/16 is the IDC IP range. The user specifies the IP range in the VPC that can communicate with the IP range in the IDC."
      },
      {
        "name": "IKEOptionsSpecification",
        "desc": "Internet Key Exchange (IKE) configuration. IKE has a self-protection mechanism. The network security protocol is configured by the user."
      },
      {
        "name": "IPSECOptionsSpecification",
        "desc": "IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud."
      }
    ],
    "desc": "This API (CreateVpnConnection) is used to create VPN tunnel."
  },
  "DeleteRouteTable": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "The route table instance ID, such as `rtb-azd4dt1c`."
      }
    ],
    "desc": "This API is used to delete a route table."
  },
  "RemoveBandwidthPackageResources": {
    "params": [
      {
        "name": "BandwidthPackageId",
        "desc": "The unique ID of the bandwidth package, such as `bwp-xxxx`."
      },
      {
        "name": "ResourceType",
        "desc": "The resource type. Valid values: `Address` and `LoadBalance`."
      },
      {
        "name": "ResourceIds",
        "desc": "The resource IP, such as `eip-xxxx` and `lb-xxxx`."
      }
    ],
    "desc": "This API is used to delete a bandwidth package resource, including [Elastic IP](https://cloud.tencent.com/document/product/213/1941), [Cloud Load Balancer](https://cloud.tencent.com/document/product/214/517), and so on."
  },
  "InquiryPriceRenewVpnGateway": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "Specifies the purchased validity period, whether to enable auto-renewal. This parameter is required for monthly-subscription instances."
      }
    ],
    "desc": "This API (InquiryPriceRenewVpnGateway) is used to query the price for VPN gateway renewal. Currently, only querying prices for IPSEC-type gateways is supported."
  },
  "AssignPrivateIpAddresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "The information on private IP addresses, of which you can specify a maximum of 10 at a time. You should provide either this parameter or SecondaryPrivateIpAddressCount, or both."
      },
      {
        "name": "SecondaryPrivateIpAddressCount",
        "desc": "The number of newly-applied private IP addresses. You should provide either this parameter or PrivateIpAddresses, or both. The total number of private IP addresses cannot exceed the quota. For more information, see<a href=\"/document/product/576/18527\">ENI Use Limits</a>."
      }
    ],
    "desc": "This API (AssignPrivateIpAddresses) is used for the ENI to apply for private IPs.\n* An ENI can only be bound with a limited number of IP addresses. For more information about resource limits, see <a href=\"/document/product/576/18527\">ENI Use Limits</a>.\n* You can specify the private IP you want to apply for. It cannot be the primary IP, which already exists and cannot be modified. The private IP must be in the same subnet as the ENI, and cannot be occupied.\n* You can apply for more than one secondary private IP on the ENI. The API will return the specified number of secondary private IPs in the subnet IP range of the ENI."
  },
  "CreateAndAttachNetworkInterface": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the `VpcId` field in the returned result of the `DescribeVpcs` API."
      },
      {
        "name": "NetworkInterfaceName",
        "desc": "The name of the ENI. The maximum length is 60 bytes."
      },
      {
        "name": "SubnetId",
        "desc": "The subnet instance ID of the ENI, such as 'subnet-0ap8nwca'."
      },
      {
        "name": "InstanceId",
        "desc": "The CVM instance ID."
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "The information of the specified private IPs. You can specify a maximum of 10 IPs each time."
      },
      {
        "name": "SecondaryPrivateIpAddressCount",
        "desc": "The number of private IP addresses you can apply for. The total number of private IP addresses cannot exceed the quota."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "The security group to be bound with, such as ['sg-1dd51d']."
      },
      {
        "name": "NetworkInterfaceDescription",
        "desc": "The ENI description. You can enter any information within 60 characters."
      },
      {
        "name": "Tags",
        "desc": "Bound tags, such as [{\"Key\": \"city\", \"Value\": \"shanghai\"}]."
      }
    ],
    "desc": "This API is used to create an ENI and bind it to a CVM.\n* You can specify private IP addresses and a primary IP when creating an ENI. The specified private IP must be idle and in the same subnet as the ENI.\n* When creating an ENI, you can specify the number of private IP addresses that you want to apply for. The system will randomly generate private IP addresses.\n* An ENI can only be bound to a limited number of IP addresses. For more information about resource limits, see <a href=\"/document/product/576/18527\">ENI Use Limits</a>.\n* You can bind an existing security group when creating an ENI.\n* You can bind a tag when creating an ENI. The tag list in the response indicates the tags that have been successfully added."
  },
  "DescribeNatGateways": {
    "params": [
      {
        "name": "NatGatewayIds",
        "desc": "The unified ID of the NAT gateways, such as `nat-123xx454`."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `NatGatewayIds` and `Filters` cannot be specified at the same time.\n<li>nat-gateway-id - String - (Filter condition) The ID of the protocol port template instance, such as `nat-123xx454`.</li>\n<li>vpc-id - String - (Filter condition) The unique ID of the VPC, such as `vpc-123xx454`.</li>\n<li>nat-gateway-name - String - (Filter condition) The ID of the protocol port template instance, such as `test_nat`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeNatGateways) is used to query NAT gateways."
  },
  "CreateSubnets": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the `VPC` instance, such as `vpc-6v2ht8q5`."
      },
      {
        "name": "Subnets",
        "desc": "The subnet object list."
      },
      {
        "name": "Tags",
        "desc": "Bound tags. Note that the collection of tags here is shared by all subnet objects in the list. You cannot specify tags for each subnet. Example: [{\"Key\": \"city\", \"Value\": \"shanghai\"}]."
      }
    ],
    "desc": "This API is used to create subnets in batches.\n* You must create a VPC instance before creating a subnet.\n* After the subnet is successfully created, its IP address range cannot be modified. The subnet IP address range must fall within the VPC IP address range. They can be the same if the VPC has only one subnet. We recommend that you keep the subnet IP address range within the VPC IP address range to reserve IP address ranges for other subnets.\n* The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses).\n* IP address ranges of different subnets cannot overlap with each other within the same VPC instance.\n* A subnet is automatically associated with the default route table once created.\n* You can bind a tag when creating a subnet. The tag list in the response indicates the tags that have been successfully added."
  },
  "ReplaceRouteTableAssociation": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "Subnet instance ID, such as `subnet-3x5lf5q0`. This can be queried using the DescribeSubnets API."
      },
      {
        "name": "RouteTableId",
        "desc": "The route table instance ID, such as `rtb-azd4dt1c`."
      }
    ],
    "desc": "This API (ReplaceRouteTableAssociation) is used to modify the route table associated with a subnet.\n* A subnet can only be associated with one route table."
  },
  "CheckNetDetectState": {
    "params": [
      {
        "name": "DetectDestinationIp",
        "desc": "The array of detection destination IPv4 addresses, which contains at most two IP addresses."
      },
      {
        "name": "NextHopType",
        "desc": "The type of the next hop. Currently supported types are:\nVPN: VPN gateway;\nDIRECTCONNECT: direct connect gateway;\nPEERCONNECTION: peering connection;\nNAT: NAT gateway;\nNORMAL_CVM: normal CVM."
      },
      {
        "name": "NextHopDestination",
        "desc": "The next-hop destination gateway. The value is related to NextHopType.\nIf NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.\nIf NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.\nIf NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.\nIf NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.\nIf NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12."
      },
      {
        "name": "NetDetectId",
        "desc": "ID of a network inspector instance, e.g. netd-12345678. Enter at least one of this parameter, VpcId, SubnetId, and NetDetectName. Use NetDetectId if it is present."
      },
      {
        "name": "VpcId",
        "desc": "ID of a `VPC` instance, e.g. `vpc-12345678`, which is used together with SubnetId and NetDetectName. You should enter either this parameter or NetDetectId, or both. Use NetDetectId if it is present."
      },
      {
        "name": "SubnetId",
        "desc": "ID of a subnet instance, e.g. `subnet-12345678`, which is used together with VpcId and NetDetectName. You should enter either this parameter or NetDetectId, or both. Use NetDetectId if it is present."
      },
      {
        "name": "NetDetectName",
        "desc": "The name of a network inspector, up to 60 bytes in length. It is used together with VpcId and NetDetectName. You should enter either this parameter or NetDetectId, or both. Use NetDetectId if it is present."
      }
    ],
    "desc": "This API is used to verify the network detection status."
  },
  "DescribeVpcs": {
    "params": [
      {
        "name": "VpcIds",
        "desc": "The VPC instance ID, such as `vpc-f49l6u0z`. Each request supports a maximum of 100 instances. `VpcIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `VpcIds` and `Filters` cannot be specified at the same time.\n<li>vpc-name - String - (Filter condition) VPC instance name.</li>\n<li>is-default - String - (Filter condition) Indicates whether it is the default VPC.</li>\n<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>\n<li>cidr-block - String - (Filter condition) VPC CIDR.</li>\n<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>\n<li>tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key is replaced with the specific tag key. For usage, refer to case 2.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      }
    ],
    "desc": "This API (DescribeVpcs) is used to query the VPC list."
  },
  "InquiryPriceResetVpnGatewayInternetMaxBandwidth": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps."
      }
    ],
    "desc": "This API (InquiryPriceResetVpnGatewayInternetMaxBandwidth) is used to query the price for adjusting the bandwidth cap of a VPN gateway."
  },
  "DeleteDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`"
      },
      {
        "name": "RouteIds",
        "desc": "The route ID, such as `ccnr-f49l6u0z`."
      }
    ],
    "desc": "This API (DeleteDirectConnectGatewayCcnRoutes) is used to delete the CCN routes (IDC IP range) of a Direct Connect gateway."
  },
  "RejectAttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "Instances",
        "desc": "The list of instances whose association is rejected."
      }
    ],
    "desc": "This API (RejectAttachCcnInstances) is used to reject association operations when instances are associated across accounts for the CCN owner.\n"
  },
  "DeleteSecurityGroup": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      }
    ],
    "desc": "This API (DeleteSecurityGroup) is used to delete security groups (SecurityGroup).\n* Only security groups under the current account can be deleted.\n* A security group cannot be deleted directly if its instance ID is used in the policy of another security group. You need to modify the policy first and then delete the security group.\n* A security group cannot be recovered after deletion, please proceed with caution."
  },
  "ModifyAddressesBandwidth": {
    "params": [
      {
        "name": "AddressIds",
        "desc": "The unique ID of the EIP, such as 'eip-xxxx'."
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "Target bandwidth value adjustment"
      },
      {
        "name": "StartTime",
        "desc": "The monthly bandwidth start time"
      },
      {
        "name": "EndTime",
        "desc": "The monthly bandwidth end time"
      }
    ],
    "desc": "This API (ModifyAddressesBandwidth) is used to adjust [Elastic IP](https://cloud.tencent.com/document/product/213/1941) bandwidth, including the postpaid EIP, prepaid EIP and bandwidth package EIP."
  },
  "CreateNatGatewayDestinationIpPortTranslationNatRule": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      },
      {
        "name": "DestinationIpPortTranslationNatRules",
        "desc": "The port forwarding rules of the NAT gateway."
      }
    ],
    "desc": "This API (CreateNatGatewayDestinationIpPortTranslationNatRule) is used to create a port forwarding rule for a NAT gateway."
  },
  "CreateSubnet": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance to be operated on. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "SubnetName",
        "desc": "The subnet name. The maximum length is 60 bytes."
      },
      {
        "name": "CidrBlock",
        "desc": "The subnet IP address range. It must be within the VPC IP address range. Subnet IP address ranges cannot overlap with each other within the same VPC."
      },
      {
        "name": "Zone",
        "desc": "The ID of the availability zone in which the subnet resides. You can set up disaster recovery across availability zones by choosing different availability zones for different subnets."
      },
      {
        "name": "Tags",
        "desc": "Bound tags, such as [{\"Key\": \"city\", \"Value\": \"shanghai\"}]."
      }
    ],
    "desc": "This API is used to create a subnet.\n* You must create a VPC instance before creating a subnet.\n* After the subnet is successfully created, its IP address range cannot be modified. The subnet IP address range must fall within the VPC IP address range. They can be the same if the VPC instance has only one subnet. We recommend that you keep the subnet IP address range within the VPC IP address range to reserve IP address ranges for other subnets.\n* The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses).\n* IP address ranges of different subnets cannot overlap with each other within the same VPC instance.\n* A subnet is automatically associated with the default route table once created.\n* You can bind a tag when creating a subnet. The tag list in the response indicates the tags that have been successfully added."
  },
  "ModifyAddressTemplateAttribute": {
    "params": [
      {
        "name": "AddressTemplateId",
        "desc": "IP address template instance ID, such as `ipm-mdunqeb6`."
      },
      {
        "name": "AddressTemplateName",
        "desc": "IP address template name."
      },
      {
        "name": "Addresses",
        "desc": "Address information, including IP, CIDR and IP address range."
      }
    ],
    "desc": "This API (ModifyAddressTemplateAttribute) is used to modify an IP address template."
  },
  "AcceptAttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "Instances",
        "desc": "List of associated instances."
      }
    ],
    "desc": "This API (AcceptAttachCcnInstances) is used to associate instances across accounts. Cloud Connect Network (CCN) owners accept and agree to the operations."
  },
  "DeleteServiceTemplateGroup": {
    "params": [
      {
        "name": "ServiceTemplateGroupId",
        "desc": "The protocol port template group instance ID, such as `ppmg-n17uxvve`."
      }
    ],
    "desc": "This API (DeleteServiceTemplateGroup) is used to delete a protocol port template group."
  },
  "DescribeGatewayFlowQos": {
    "params": [
      {
        "name": "GatewayId",
        "desc": "Gateway instance ID, which currently supports these types:\nID of Direct Connect gateway instance, e.g. `dcg-ltjahce6`;\nID of NAT gateway instance, e.g. `nat-ltjahce6`;\nID of VPN gateway instance, e.g. `vpn-ltjahce6`."
      },
      {
        "name": "IpAddresses",
        "desc": "CVM private IP addresses with limited bandwidth."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      }
    ],
    "desc": "This API (DescribeGatewayFlowQos) is used to query the QoS bandwidth limit of inbound IP flow in a gateway."
  },
  "DisassociateAddress": {
    "params": [
      {
        "name": "AddressId",
        "desc": "The unique ID of the EIP, such as `eip-11112222`."
      },
      {
        "name": "ReallocateNormalPublicIp",
        "desc": "Whether a common public IP is assigned after the EIP is unbound. Value range:<br><li>TRUE: Indicates that after the EIP is unbound, a common public IP is assigned.<br><li>FALSE: Indicates that after the EIP is unbound, a common public IP is not assigned.<br>Default value: FALSE.<br><br>The parameter can be specified only under the following conditions:<br><li>It can only be specified when you unbind an EIP from the primary private IP of the primary ENI.<br><li>After an EIP is unbound, you can assign public IPs to an account up to 10 times per day. For more information, use the [DescribeAddressQuota] (https://cloud.tencent.com/document/api/213/1378) API."
      }
    ],
    "desc": "This API (DisassociateAddress) is used to unbind [Elastic IPs](https://cloud.tencent.com/document/product/213/1941).\n* The unbinding of EIPs from CVM instances and ENIs is supported.\n* The unbinding of EIPs from NATs is not supported. For information about how to unbind an EIP from a NAT, see [EipUnBindNatGateway](https://cloud.tencent.com/document/product/215/4092).\n* You can only unbind EIPs in BIND or BIND_ENI status.\n* Blocked EIPs cannot be unbound."
  },
  "DisassociateNetworkInterfaceSecurityGroups": {
    "params": [
      {
        "name": "NetworkInterfaceIds",
        "desc": "ENI instance ID, e.g. eni-pxir56ns. You can enter up to 100 instances for each request."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups. You can enter up to 100 instances for each request."
      }
    ],
    "desc": "This API (DisassociateNetworkInterfaceSecurityGroups) is used to detach (or fully detach if possible) a security group from an ENI."
  },
  "CreateVpc": {
    "params": [
      {
        "name": "VpcName",
        "desc": "The VPC name. The maximum length is 60 bytes."
      },
      {
        "name": "CidrBlock",
        "desc": "VPC CIDR, which must fall within the following private network IP ranges: 10.0.0.0/16, 172.16.0.0/16, and 192.168.0.0/16."
      },
      {
        "name": "EnableMulticast",
        "desc": "Whether multicast is enabled. `true`: Enabled. `false`: Not enabled."
      },
      {
        "name": "DnsServers",
        "desc": "The DNS address. A maximum of 4 addresses is supported."
      },
      {
        "name": "DomainName",
        "desc": "Domain name"
      },
      {
        "name": "Tags",
        "desc": "Bound tags, such as [{\"Key\": \"city\", \"Value\": \"shanghai\"}]."
      }
    ],
    "desc": "This API is used to create a VPC instance.\n* The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses). For more information, see the corresponding documents about VPC IP address ranges.\n* The number of VPC instances that can be created in a region is limited. For more information, see <a href=\"https://intl.cloud.tencent.com/doc/product/215/537\" title=\"VPC Use Limits\">VPC Use Limits</a>. To request more resources, contact the online customer service.\n* You can bind a tag when creating a VPC instance. The tag list in the response indicates the tags that have been successfully added."
  },
  "AddBandwidthPackageResources": {
    "params": [
      {
        "name": "ResourceIds",
        "desc": "The unique ID of the source, such as 'eip-xxxx' and 'lb-xxxx'. EIP and LB resources are currently supported."
      },
      {
        "name": "BandwidthPackageId",
        "desc": "The unique ID of the bandwidth package, such as 'bwp-xxxx'."
      },
      {
        "name": "NetworkType",
        "desc": "The network type of the bandwidth package. Valid value: `BGP`, indicating that the internal resource is a BGP IP."
      },
      {
        "name": "ResourceType",
        "desc": "The resource type, including `Address` and `LoadBalance`."
      },
      {
        "name": "Protocol",
        "desc": "The protocol type of the bandwidth package. Valid values: `ipv4` and `ipv6`."
      }
    ],
    "desc": "This API is used to add resources to a bandwidth package, including [Elastic IP](https://cloud.tencent.com/document/product/213/1941), [Cloud Load Balancer](https://cloud.tencent.com/document/product/214/517), and so on."
  },
  "AssignIpv6SubnetCidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the VPC where the subnet is located, such as `vpc-f49l6u0z`."
      },
      {
        "name": "Ipv6SubnetCidrBlocks",
        "desc": "The assigned `IPv6` subnet IP range list."
      }
    ],
    "desc": "This API (AssignIpv6SubnetCidrBlock) is used to assign IPv6 subnet IP ranges.\n* To assign an `IPv6` IP range to a subnet, the `VPC` that the subnet belongs to should have obtained the `IPv6` IP range. If this has not been assigned, use the `AssignIpv6CidrBlock` API to assign an `IPv6` IP range to the `VPC` to which the subnet belongs. Otherwise, the `IPv6` subnet IP range cannot be assigned.\n* Each subnet can only be assigned one IPv6 IP range."
  },
  "DescribeVpnGatewayCcnRoutes": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "Offset",
        "desc": "Offset."
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      }
    ],
    "desc": "This API (DescribeVpnGatewayCcnRoutes) is used to query VPN gateway-based CCN routes."
  },
  "AllocateAddresses": {
    "params": [
      {
        "name": "AddressCount",
        "desc": "The number of EIPs. Default: 1."
      },
      {
        "name": "InternetServiceProvider",
        "desc": "The EIP line type. Default: BGP.\n<ul style=\"margin:0\"><li>For a user who has activated the static single-line IP allowlist, possible values are:<ul><li>CMCC: China Mobile</li>\n<li>CTCC: China Telecom</li>\n<li>CUCC: China Unicom</li></ul>Note: Only certain regions support static single-line IP addresses.</li></ul>"
      },
      {
        "name": "InternetChargeType",
        "desc": "The EIP billing method.\n<ul style=\"margin:0\"><li>For a user who has activated bandwidth billing by IP allowlist, possible values are:<ul><li>BANDWIDTH_PACKAGE: paid by the [bandwidth package](https://cloud.tencent.com/document/product/684/15255) (The bandwidth sharing allowlist must be activated additionally.)</li>\n<li>BANDWIDTH_POSTPAID_BY_HOUR: bandwidth postpaid by hour</li>\n<li>TRAFFIC_POSTPAID_BY_HOUR: traffic postpaid by hour</li></ul>Default: TRAFFIC_POSTPAID_BY_HOUR</li>.\n<li>For users who do not use bill-by-bandwidth billing mode, InternetChargeType is consistent with that of the instance bound to the EIP. Therefore, it is unnecessary to pass in this parameter.</li></ul>"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The maximum EIP outbound bandwidth. Unit: Mbps.\n<ul style=\"margin:0\"><li>For a user who has activated bandwidth billing by IP allowlist, the value range is determined by the EIP billing method:<ul><li>BANDWIDTH_PACKAGE: 1 Mbps to 1,000 Mbps</li>\n<li>BANDWIDTH_POSTPAID_BY_HOUR: 1 Mbps to 100 Mbps</li>\n<li>TRAFFIC_POSTPAID_BY_HOUR: 1 Mbps to 100 Mbps</li></ul>Default: 1 Mbps</li>.\n<li>For a user who has not activated bandwidth billing by IP allowlist, InternetMaxBandwidthOut is consistent with that of the instance bound to the EIP. Therefore, it is unnecessary to pass in this parameter.</li></ul>"
      },
      {
        "name": "AddressType",
        "desc": "The EIP type. Default: EIP.\n<ul style=\"margin:0\"><li>For a user who has activated the AIA allowlist, possible values are:<ul><li>AnycastEIP: an Anycast EIP address. For more information, see [Anycast Internet Acceleration](https://cloud.tencent.com/document/product/644).</li></ul>Note: Only certain regions support Anycast EIPs.</li></ul>"
      },
      {
        "name": "AnycastZone",
        "desc": "Anycast publishing region\n<ul style=\"margin:0\"><li>Valid for users who have activated AIA. Values:<ul><li>ANYCAST_ZONE_GLOBAL: global publishing region </li><li>ANYCAST_ZONE_OVERSEAS: overseas publishing region</li><li><b>**[Disused]**</b> ANYCAST_ZONE_A: publishing region A (updated to ANYCAST_ZONE_GLOBAL)</li><li><b>**[Disused]**</b> ANYCAST_ZONE_B: publishing region B (updated to ANYCAST_ZONE_GLOBAL)</li></ul>Default: ANYCAST_ZONE_OVERSEAS.</li></ul>"
      },
      {
        "name": "ApplicableForCLB",
        "desc": "<b>**[Disused]**</b>\nWhether the Anycast EIP can be bound to CLB instances.\n<ul style=\"margin:0\"><li>Valid for users who have activated the AIA. Values:<ul><li>TRUE: the Anycast EIP can be bound to CLB instances.</li>\n<li>FALSE: the Anycast EIP can be bound to CVMs, NAT gateways, and HAVIPs.</li></ul>Default: FALSE.</li></ul>"
      },
      {
        "name": "Tags",
        "desc": "List of tags to be bound."
      },
      {
        "name": "BandwidthPackageId",
        "desc": "The unique ID of a BGP bandwidth package. If you configure this parameter and set InternetChargeType as BANDWIDTH_PACKAGE, the new EIP is added to this package and billed by the bandwidth package mode."
      }
    ],
    "desc": "This API is used to apply for one or more [Elastic IP Addresses](https://cloud.tencent.com/document/product/213/1941) (EIPs for short).\n* An EIP is a static IP address that is dedicated for dynamic cloud computing. You can quickly re-map an EIP to another instance under your account to protect against instance failures.\n* Your EIP is associated with your Tencent Cloud account rather than an instance. It remains associated with your Tencent Cloud account until you choose to explicitly release it or your account is in arrears for more than 24 hours.\n* The maximum number of EIPs that can be applied for a Tencent Cloud account in each region is restricted. For more information, see [EIP Product Introduction](https://cloud.tencent.com/document/product/213/5733). You can get the quota information through the DescribeAddressQuota API."
  },
  "CheckAssistantCidr": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC` instance `ID`, e.g. `vpc-6v2ht8q5`."
      },
      {
        "name": "NewCidrBlocks",
        "desc": "Load CIDR blocks to add. CIDR block set; format: e.g. [\"10.0.0.0/16\", \"172.16.0.0/16\"]"
      },
      {
        "name": "OldCidrBlocks",
        "desc": "Load CIDR blocks to delete. CIDR block set; Format: e.g. [\"10.0.0.0/16\", \"172.16.0.0/16\"]"
      }
    ],
    "desc": "This API (CheckAssistantCidr) is used to check overlapping of a secondary CIDR block with inventory routing, peering connection (opposite VPC CIDR block), and any other resources. If an overlap is present, the overlapped resources are returned. (To use this API that is in Beta, please submit a ticket.)\n* Check whether the secondary CIDR block overlaps with a primary or secondary CIDR block of the current VPC.\n* Check whether the secondary CIDR block overlaps with the routing destination of the current VPC.\n* Check whether the secondary CIDR block is peer-connected to the current VPC, and whether it overlaps with a main or secondary CIDR block of the opposite VPC."
  },
  "DescribeVpcIpv6Addresses": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the `VPC`, such as `vpc-f49l6u0z`."
      },
      {
        "name": "Ipv6Addresses",
        "desc": "The `IP` address list. Each request supports a maximum of `10` batch querying."
      },
      {
        "name": "Offset",
        "desc": "Offset."
      },
      {
        "name": "Limit",
        "desc": "The returned quantity."
      }
    ],
    "desc": "This API (DescribeVpcIpv6Addresses) is used to query `VPC` `IPv6` information.\nThis API is used to query only the information of `IPv6` addresses that are already in use. When querying IPs that have not yet been used, this API will not report an error, but the IPs will not appear in the returned results."
  },
  "DescribeAccountAttributes": {
    "params": [],
    "desc": "This API (DescribeAccountAttributes) is used to query your account attributes."
  },
  "AttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "Instances",
        "desc": "List of associated network instances"
      },
      {
        "name": "CcnUin",
        "desc": "The UIN (root account) of the CCN. By default, the current account belongs to the UIN"
      }
    ],
    "desc": "This API (AttachCcnInstances) is used to load a network instance to a CCN instance. Network instances include VPCs and Direct Connect gateways.<br />\nThe number of network instances that each CCN can be associated with is limited. For more information, see the product documentation. If you need to associate more instances, please contact online customer service."
  },
  "AssociateAddress": {
    "params": [
      {
        "name": "AddressId",
        "desc": "The unique ID of the EIP, such as `eip-11112222`."
      },
      {
        "name": "InstanceId",
        "desc": "The ID of the instance to be bound, such as `ins-11112222`. You can query the instance ID by logging into the [Console](https://console.cloud.tencent.com/cvm). You can also obtain the parameter value from the `InstanceId` field in the returned result of [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API."
      },
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI to be bonud, such as `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. You can query the ENI ID by logging into the [Console](https://console.cloud.tencent.com/vpc/eni). You can also obtain the parameter value from the `networkInterfaceId` field in the returned result of [DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817) API."
      },
      {
        "name": "PrivateIpAddress",
        "desc": "The private IP to be bound. If you specify `NetworkInterfaceId`, then you must also specify `PrivateIpAddress`, indicating the EIP is bound to the specified private IP of the specified ENI. At the same time, you must ensure the specified `PrivateIpAddress` is a private IP on the `NetworkInterfaceId`. You can query the private IP of the specified ENI by logging into the [Console](https://console.cloud.tencent.com/vpc/eni). You can also obtain the parameter value from the `privateIpAddress` field in the returned result of [DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817) API."
      }
    ],
    "desc": "This API (AssociateAddress) is used to bind an [Elastic IP](https://cloud.tencent.com/document/product/213/1941) (EIP for short) to the specified private IP of an instance or ENI.\n* Essentially, binding an EIP to an instance (CVM) means binding an EIP to the primary private IP of the primary ENI on an instance.\n* When you bind an EIP to the primary private IP of the primary ENI, the previously bound public IP is automatically unbound and released.\n* To bind the EIP to the private IP of the specified ENI (not the primary private IP of the primary ENI), you must unbind the EIP before you can bind a new one.\n* To bind the EIP to a NAT gateway, use the API [EipBindNatGateway](https://cloud.tencent.com/document/product/215/4093)\n* EIP that is in arrears or blocked cannot be bound.\n* Only EIP in the UNBIND status can be bound."
  },
  "DeleteCustomerGateway": {
    "params": [
      {
        "name": "CustomerGatewayId",
        "desc": "The ID of the customer gateway, such as `cgw-2wqq41m9`. You can query the customer gateway by using the `DescribeCustomerGateways` API."
      }
    ],
    "desc": "This API (DeleteCustomerGateway) is used to delete customer gateways."
  },
  "DeleteSubnet": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "The ID of the subnet instance. You can obtain the parameter value from the SubnetId field in the returned result of DescribeSubnets API."
      }
    ],
    "desc": "This API (DeleteSubnet) is used to delete subnets.\nBefore deleting a subnet, you need to remove all resources in the subnet, including CVMs, load balancers, cloud data, NoSQL databases, and ENIs."
  },
  "AttachClassicLinkVpc": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC instance ID"
      },
      {
        "name": "InstanceIds",
        "desc": "CVM Instance ID"
      }
    ],
    "desc": "This API is used to create a Classiclink between a VPC instance and a basic network device.\n* The VPC instance and the basic network device must be in the same region.\n* For differences between VPC and basic networks, see <a href=\"https://cloud.tencent.com/document/product/215/30720\">VPC and Basic Networks</a>."
  },
  "DisassociateNatGatewayAddress": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      },
      {
        "name": "PublicIpAddresses",
        "desc": "The array of EIPs bound to the NAT gateway."
      }
    ],
    "desc": "This API (DisassociateNatGatewayAddress) is used to unbind an EIP from a NAT gateway."
  },
  "DescribeFlowLogs": {
    "params": [
      {
        "name": "VpcId",
        "desc": "ID of the VPC instance"
      },
      {
        "name": "FlowLogId",
        "desc": "The unique ID of the flow log."
      },
      {
        "name": "FlowLogName",
        "desc": "The name of the flow log instance."
      },
      {
        "name": "ResourceType",
        "desc": "The resource type of the flow log. Valid values: 'VPC', 'SUBNET', and 'NETWORKINTERFACE'."
      },
      {
        "name": "ResourceId",
        "desc": "The unique ID of the resource."
      },
      {
        "name": "TrafficType",
        "desc": "Type of flow logs to be collected. Valid values: 'ACCEPT', 'REJECT' and 'ALL'."
      },
      {
        "name": "CloudLogId",
        "desc": "The storage ID of the flow log."
      },
      {
        "name": "CloudLogState",
        "desc": "The storage ID status of the flow log."
      },
      {
        "name": "OrderField",
        "desc": "Order by field. Valid values: 'flowLogName' and 'createTime'. Default value: 'createTime'."
      },
      {
        "name": "OrderDirection",
        "desc": "In ascending (`asc`) or descending (`desc`) order. Default value: 'desc'."
      },
      {
        "name": "Offset",
        "desc": "The offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "The number of rows per page. Default value: 10."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `FlowLogIds` and `Filters` cannot be specified at the same time.\n<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>\n<li> tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key should be replaced with a specified tag key.</li>"
      }
    ],
    "desc": "This API is used to query all the flow logs of the current account."
  },
  "DeleteDirectConnectGateway": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "The unique `ID` of the direct connect gateway, such as `dcg-9o233uri`."
      }
    ],
    "desc": "This API is used to delete a direct connect gateway.\n<li>For a NAT gateway, NAT and ACL rules will be cleared upon the deletion of a direct connect gateway.\n<li>After the deletion of a direct connect gateway, the routing policy associated with the gateway in the route table will also be deleted.\nThis API is completed asynchronously. If you need to query the async job execution results, please use the `RequestId` returned by this API to poll the `QueryTask` API."
  },
  "DescribeDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`."
      },
      {
        "name": "CcnRouteType",
        "desc": "The route learning type of the CCN. Available values:\n<li>`BGP` - Automatic learning.</li>\n<li>`STATIC` - Static means user-configured. This is the default value.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset."
      },
      {
        "name": "Limit",
        "desc": "The returned quantity."
      }
    ],
    "desc": "This API (DescribeDirectConnectGatewayCcnRoutes) is used to query the CCN routes (IDC IP range) of the Direct Connect gateway."
  },
  "CreateNetworkInterface": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "NetworkInterfaceName",
        "desc": "The name of the ENI. The maximum length is 60 characters."
      },
      {
        "name": "SubnetId",
        "desc": "The subnet instance ID of the ENI, such as `subnet-0ap8nwca`."
      },
      {
        "name": "NetworkInterfaceDescription",
        "desc": "ENI description can be named freely, but the maximum length is 60 characters."
      },
      {
        "name": "SecondaryPrivateIpAddressCount",
        "desc": "The number of private IP addresses that is newly applied for. The total number of private IP addresses cannot exceed the quota."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "Specifies the security group to be bound with, such as ['sg-1dd51d']."
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "The information of the specified private IPs. You can specify a maximum of 10 each time."
      },
      {
        "name": "Tags",
        "desc": "Bound tags, such as [{\"Key\": \"city\", \"Value\": \"shanghai\"}]."
      }
    ],
    "desc": "This API is used to create one or more ENIs.\n* You can specify private IP addresses and a primary IP when creating an ENI. The specified private IP must be in the same subnet as the ENI and is not occupied.\n* When creating an ENI, you can specify the number of private IP addresses that you want to apply for. The system will randomly generate private IP addresses.\n* An ENI can only be bound with a limited number of IP addresses. For more information about resource limits, see <a href=\"/document/product/576/18527\">ENI Use Limits</a>.\n* You can bind an existing security group when creating an ENI.\n* You can bind a tag when creating an ENI. The tag list in the response indicates the tags that have been successfully added."
  },
  "DeleteBandwidthPackage": {
    "params": [
      {
        "name": "BandwidthPackageId",
        "desc": "The unique ID of the bandwidth package to be deleted."
      }
    ],
    "desc": "This API is used to delete bandwidth packages, including [device bandwidth packages](https://cloud.tencent.com/document/product/684/15246#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85) and [IP bandwidth packages](https://cloud.tencent.com/document/product/684/15246#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85)."
  },
  "DescribeNetDetectStates": {
    "params": [
      {
        "name": "NetDetectIds",
        "desc": "The array of network detection instance `IDs`, such as [`netd-12345678`]."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions. `NetDetectIds` and `Filters` cannot be specified at the same time.\n<li>net-detect-id - String - (Filter condition) The network detection instance ID, such as netd-12345678.</li>"
      },
      {
        "name": "Offset",
        "desc": "The offset. Default: 0."
      },
      {
        "name": "Limit",
        "desc": "The number of returned values. Default: 20. Maximum: 100."
      }
    ],
    "desc": "This API (DescribeNetDetectStates) is used to query the list of network detection verification results."
  },
  "DescribeCcns": {
    "params": [
      {
        "name": "CcnIds",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`. Each request can have a maximum of 100 instances. `CcnIds` and `Filters` cannot be specified at the same time"
      },
      {
        "name": "Filters",
        "desc": "Filter conditions. `CcnIds` and `Filters` cannot be specified at the same time.\n<li>ccn-id - String - (Filter condition) The unique ID of the CCN, such as `vpc-f49l6u0z`.</li>\n<li>ccn-name - String - (Filter condition) The CCN name.</li>\n<li>ccn-description - String - (Filter condition) CCN description.</li>\n<li>state - String - (Filter condition) The instance status. 'ISOLATED': Isolated (the account is in arrears and the service is suspended.) 'AVAILABLE': Running.</li>\n<li>tag-key - String - Required: no - (Filter condition) Filters by tag key.</li>\n<li>`tag:tag-key` - String - Required: no - (Filter condition) Filters by tag key pair. For this parameter, `tag-key` will be replaced with a specific tag key. For more information, see this example: **Querying the list of CCNs bound to tags**.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      },
      {
        "name": "OrderField",
        "desc": "Order fields support `CcnId`, `CcnName`, `CreateTime`, `State`, and `QosLevel`"
      },
      {
        "name": "OrderDirection",
        "desc": "Order methods. Ascending: `ASC`, Descending: `DESC`."
      }
    ],
    "desc": "This API (DescribeCcns) is used to query the CCN list."
  },
  "DeleteCcn": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      }
    ],
    "desc": "This API (DeleteCcn) is used to delete CCNs.\n* After deletion, the routes between all instances associated with the CCN will be deleted, and the network will be interrupted. Please confirm this operation in advance.\n* CCN deletion is an irreversible operation. Please proceed with caution.\n"
  },
  "ModifyNetworkAclEntries": {
    "params": [
      {
        "name": "NetworkAclId",
        "desc": "Network ACL instance ID. Example: acl-12345678."
      },
      {
        "name": "NetworkAclEntrySet",
        "desc": "Network ACL rule set."
      }
    ],
    "desc": "This API is used to modify (add or delete) the inbound and outbound rules of a network ACL."
  },
  "HaVipDisassociateAddressIp": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "The unique `ID` of the `HAVIP`, such as `havip-9o233uri`. This must be an `HAVIP` that has been bound to an `EIP`."
      }
    ],
    "desc": "This API (HaVipDisassociateAddressIp) is used to unbind an EIP which has been bound to an HAVIP.<br />\nThis API is completed asynchronously. If you need to query the async job execution results, please use the `RequestId` returned by this API to query the `QueryTask` API."
  },
  "ModifyVpnGatewayCcnRoutes": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "Routes",
        "desc": "The CCN route (IDC IP range) list."
      }
    ],
    "desc": "This API (ModifyVpnGatewayCcnRoutes) is used to modify VPN gateway-based CCN routes."
  },
  "DetachNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "InstanceId",
        "desc": "The ID of the CVM instance, such as `ins-r8hr2upy`."
      }
    ],
    "desc": "This API (DetachNetworkInterface) is used to unbind an ENI from a CVM."
  },
  "DeleteAssistantCidr": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC` instance `ID`, e.g. `vpc-6v2ht8q5`."
      },
      {
        "name": "CidrBlocks",
        "desc": "CIDR set, e.g. [\"10.0.0.0/16\", \"172.16.0.0/16\"]"
      }
    ],
    "desc": "This API (DeleteAssistantCidr) is used to delete secondary CIDR blocks. (To use this API that is in Beta, please submit a ticket.)"
  },
  "DeleteNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      }
    ],
    "desc": "This API (DeleteNetworkInterface) is used to delete ENIs.\n* An ENI that has been bound to a CVM cannot be deleted.\n* An ENI can be deleted only after being unbound from the server. After the deletion, all private IP addresses associated with the ENI will be released."
  },
  "DescribeVpnConnections": {
    "params": [
      {
        "name": "VpnConnectionIds",
        "desc": "The instance ID of the VPN tunnel, such as `vpnx-f49l6u0z`. Each request can have a maximum of 100 instances. `VpnConnectionIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. In each request, the upper limit for `Filters` is 10 and 5 for `Filter.Values`. `VpnConnectionIds` and `Filters` cannot be specified at the same time.\n<li>vpc-id - String - VPC instance ID, such as `vpc-0a36uwkr`.</li>\n<li>vpn-gateway-id - String - VPN gateway instance ID, such as `vpngw-p4lmqawn`.</li>\n<li>customer-gateway-id - String - Customer gateway instance ID, such as `cgw-l4rblw63`.</li>\n<li>vpn-connection-name - String - Connection name, such as `test-vpn`.</li>\n<li>vpn-connection-id - String - Connection instance ID, such as `vpnx-5p7vkch8\"`.</li>"
      },
      {
        "name": "Offset",
        "desc": "The Offset. The default value is 0. For more information about Offset, see the relevant section in the API Introduction."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": " This API (DescribeVpnConnections) is used to query the VPN tunnel list."
  },
  "DescribeSecurityGroupReferences": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "A set of security group instance IDs, e.g. ['sg-12345678']"
      }
    ],
    "desc": "This API (DescribeSecurityGroupReferences) is used to query referred security groups."
  },
  "DescribeFlowLog": {
    "params": [
      {
        "name": "VpcId",
        "desc": "ID of the VPC instance"
      },
      {
        "name": "FlowLogId",
        "desc": "The unique ID of the flow log."
      }
    ],
    "desc": "This API is used to query the information of a flow log."
  },
  "ModifyGatewayFlowQos": {
    "params": [
      {
        "name": "GatewayId",
        "desc": "Gateway instance ID, which currently supports these types:\nID of Direct Connect gateway instance, e.g. `dcg-ltjahce6`;\nID of NAT gateway instance, e.g. `nat-ltjahce6`;\nID of VPN gateway instance, e.g. `vpn-ltjahce6`."
      },
      {
        "name": "Bandwidth",
        "desc": "Bandwidth limit value in Mbps. Valid values: >0: set the limit to the specified value. 0: block all traffic. -1: no bandwidth limit."
      },
      {
        "name": "IpAddresses",
        "desc": "CVM private IP addresses with limited bandwidth."
      }
    ],
    "desc": "This API (ModifyGatewayFlowQos) is used to adjust the QoS bandwidth limit in a gateway."
  },
  "DeleteNatGateway": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      }
    ],
    "desc": "This API (DeleteNatGateway) is used to delete a NAT gateway.\nAfter the deletion of a NAT gateway, the system will automatically delete the routing entry that contains the NAT gateway from the route table. It will also unbind the Elastic IP."
  },
  "DownloadCustomerGatewayConfiguration": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "VpnConnectionId",
        "desc": "The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`."
      },
      {
        "name": "CustomerGatewayVendor",
        "desc": "Customer gateway vendor information object, which can be obtained through DescribeCustomerGatewayVendors."
      },
      {
        "name": "InterfaceName",
        "desc": "Name of the physical API for tunnel access device."
      }
    ],
    "desc": "This API (DownloadCustomerGatewayConfiguration) is used to download a VPN tunnel configuration."
  },
  "DeleteServiceTemplate": {
    "params": [
      {
        "name": "ServiceTemplateId",
        "desc": "Protocol port template instance ID, such as `ppm-e6dy460g`."
      }
    ],
    "desc": "This API (DeleteServiceTemplate) is used to delete a protocol port template."
  },
  "UnassignPrivateIpAddresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "The information of the specified private IPs. You can specify a maximum of 10 each time."
      }
    ],
    "desc": "This API (UnassignPrivateIpAddresses) is used to return the private IPs of ENI.\n* To return the secondary private IPs of an ENI, the API will automatically unbind the IPs of an ENI. The primary private IP of the ENI cannot be returned."
  },
  "ModifyAddressTemplateGroupAttribute": {
    "params": [
      {
        "name": "AddressTemplateGroupId",
        "desc": "IP address template group instance ID, such as `ipmg-2uw6ujo6`."
      },
      {
        "name": "AddressTemplateGroupName",
        "desc": "IP address template group name."
      },
      {
        "name": "AddressTemplateIds",
        "desc": "IP address template instance ID, such as `ipm-mdunqeb6`."
      }
    ],
    "desc": "This API (ModifyAddressTemplateGroupAttribute) is used to modify an IP address template group."
  },
  "DescribeCcnRoutes": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-gree226l`."
      },
      {
        "name": "RouteIds",
        "desc": "The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `RouteIds` and `Filters` cannot be specified at the same time.\n<li>route-id - String - (Filter condition) Routing policy ID.</li>\n<li>cidr-block - String - (Filter condition) Destination port.</li>\n<li>instance-type - String - (Filter condition) The next hop type.</li>\n<li>instance-region - String - (Filter condition) The next hop region.</li>\n<li>instance-type - String - (Filter condition) The instance ID of the next hop.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      }
    ],
    "desc": "This API (DescribeCcnRoutes) is used to query routes that have been added to a CCN."
  },
  "DescribeBandwidthPackageQuota": {
    "params": [],
    "desc": "This API is used to query the maximum and used number of bandwidth packages under the account in the current region."
  },
  "CreateAssistantCidr": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC` instance `ID`, e.g. `vpc-6v2ht8q5`."
      },
      {
        "name": "CidrBlocks",
        "desc": "CIDR set, e.g. [\"10.0.0.0/16\", \"172.16.0.0/16\"]"
      }
    ],
    "desc": "This API (CreateAssistantCidr) is used to batch create secondary CIDR blocks. (To use this API that is in Beta, please submit a ticket.)"
  },
  "CreateDefaultVpc": {
    "params": [
      {
        "name": "Zone",
        "desc": "The ID of the availability zone in which the subnet resides. The availability zone will be randomly selected if not specified."
      },
      {
        "name": "Force",
        "desc": "Whether to forcibly return a default VPC"
      }
    ],
    "desc": "This API is used to create a default VPC.\n\nThe default VPC is suitable for getting started with and launching public instances, and it can be used like any other VPCs. To create a standard VPC, for which you need to specify a VPC name, VPC IP range, subnet IP range, and subnet availability zone, use the regular CreateVpc API.\n\nUnder normal circumstances, this API may not create a default VPC. It depends on the network attributes (DescribeAccountAttributes) of your account.\n* If both basic network and VPC are supported, the returned VpcId is 0.\n* If only VPC is supported, the default VPC information is returned.\n\nYou can also use the Force parameter to forcibly return a default VPC."
  },
  "AttachNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "InstanceId",
        "desc": "The ID of the CVM instance, such as `ins-r8hr2upy`."
      }
    ],
    "desc": "This API is used to bind an ENI to a CVM.\n* One CVM can be bound to multiple ENIs, but only one primary ENI. For more information on the limits, see <a href=\"https://cloud.tencent.com/document/product/576/18527\">ENI Use Limits</a>.\n* An ENI can only be bound to one CVM at a time.\n* Only CVMs in the running or shutdown state can be bound to an ENI. For more information on CVM states, see <a href=\"https://cloud.tencent.com/document/api/213/9452#InstanceStatus\">Tencent CVM Information</a>.\n* An ENI can only be bound to a CVM in a VPC instance, and the CVM must reside in the same availability zone as the subnet of the ENI."
  },
  "ReplaceDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`"
      },
      {
        "name": "Routes",
        "desc": "The list of IDC IP range that must be connected"
      }
    ],
    "desc": "This API (ReplaceDirectConnectGatewayCcnRoutes) is used to modify the specified route according to the route ID. Batch modification is supported."
  },
  "GetCcnRegionBandwidthLimits": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "Filters",
        "desc": "The filter condition.\n<li>sregion - String - (Filter condition) Filter by the source region, such as 'ap-guangzhou'.</li>\n<li>dregion - String - (Filter condition) Filter by the destination region, such as 'ap-shanghai-bm'.</li>"
      },
      {
        "name": "SortedBy",
        "desc": "The sorting condition. Valid values: `BandwidthLimit` and `ExpireTime`."
      },
      {
        "name": "Offset",
        "desc": "The offset."
      },
      {
        "name": "Limit",
        "desc": "The returned quantity."
      },
      {
        "name": "OrderBy",
        "desc": "In ascending or descending order. Valid values: 'ASC' and 'DESC'."
      }
    ],
    "desc": "This API is used to query the bandwidth limits of a CCN instance. Monthly-subscribed CCNs only support Inter-region Bandwidth Limits, while the pay-as-you-go CCNs support both the Inter-region Bandwidth Limits and Region Outbound Bandwidth Limits. "
  },
  "DeleteSecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "The policy set of the security group. One request can only delete one or more policies in one direction. Both PolicyIndex-matching deletion and security group policy-matching deletion methods are supported. Each request can use only one matching method."
      }
    ],
    "desc": "This API (DeleteSecurityGroupPolicies) is used to delete security group policies (SecurityGroupPolicy).\n* SecurityGroupPolicySet.Version is used to specify the version of the security group you are operating. If the specified Version number differs from the latest version of the current security group, a failure will be returned. If Version is not specified, the policy of the specified PolicyIndex will be deleted directly."
  },
  "DeleteNetDetect": {
    "params": [
      {
        "name": "NetDetectId",
        "desc": "The `ID` of a network detection instance, such as `netd-12345678`."
      }
    ],
    "desc": "This API (DeleteNetDetect) is used to delete a network detection instance."
  },
  "ModifySecurityGroupAttribute": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      },
      {
        "name": "GroupName",
        "desc": "Security group can be named freely, but cannot exceed 60 characters."
      },
      {
        "name": "GroupDescription",
        "desc": "The remarks for the security group. The maximum length is 100 characters."
      }
    ],
    "desc": "This API (ModifySecurityGroupAttribute) is used to modify the attributes of a security group (SecurityGroupPolicy)."
  },
  "DeleteAddressTemplate": {
    "params": [
      {
        "name": "AddressTemplateId",
        "desc": "The IP address template instance ID, such as `ipm-09o5m8kc`."
      }
    ],
    "desc": "This API (DeleteAddressTemplate) is used to delete an IP address template."
  },
  "ModifyAssistantCidr": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC` instance `ID`, e.g. `vpc-6v2ht8q5`."
      },
      {
        "name": "NewCidrBlocks",
        "desc": "Load CIDR blocks to add. CIDR block set; format: e.g. [\"10.0.0.0/16\", \"172.16.0.0/16\"]"
      },
      {
        "name": "OldCidrBlocks",
        "desc": "Load CIDR blocks to delete. CIDR block set; Format: e.g. [\"10.0.0.0/16\", \"172.16.0.0/16\"]"
      }
    ],
    "desc": "This API (ModifyAssistantCidr) is used to batch modify (e.g. add and delete) secondary CIDR blocks. (To use this API that is in Beta, please submit a ticket.)"
  },
  "DeleteVpnGateway": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      }
    ],
    "desc": "This API (DeleteVpnGateway) is used to delete a VPN gateway. Currently, only deletion of pay-as-you-go IPSEC gateway instances in running status is supported."
  },
  "CreateServiceTemplate": {
    "params": [
      {
        "name": "ServiceTemplateName",
        "desc": "Template name of the protocol port"
      },
      {
        "name": "Services",
        "desc": "It supports single port, multiple ports, consecutive ports and all ports. Supported protocols include TCP, UDP, ICMP, and GRE."
      }
    ],
    "desc": "This API (CreateServiceTemplate) is used to create a protocol port template."
  },
  "DeleteRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "Route table instance ID."
      },
      {
        "name": "Routes",
        "desc": "Routing policy object."
      }
    ],
    "desc": "This API (DeleteRoutes) is used to delete routing policies in batches from a route table."
  },
  "ModifySecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "The security group policy set. SecurityGroupPolicySet object must specify new egress and ingress policies at the same time. SecurityGroupPolicy object does not support custom index (PolicyIndex)."
      },
      {
        "name": "SortPolicys",
        "desc": "Whether security group sorting is supported. True indicates that security group sorting is supported. If SortPolicys does not exist or is set to False, the security group policy can be modified."
      }
    ],
    "desc": "This API is used to reset the egress and ingress policies (SecurityGroupPolicy) of a security group.\n\n<ul>\n<li>This API deletes all the existing egress and ingress policies, and then adds Egress and Ingress policies. It does not support custom indexes `PolicyIndex`.</li>\n<li>For parameters of SecurityGroupPolicySet,<ul>\n\t<li>If `SecurityGroupPolicySet.Version` is set to 0, all policies will be cleared, and `Egress` and `Ingress` will be ignored.</li>\n\t<li>If `SecurityGroupPolicySet.Version` is not set to 0, add `Egress` and `Ingress` policies:<ul>\n\t\t<li>`Protocol`: allows TCP, UDP, ICMP, ICMPV6, GRE, or ALL.</li>\n\t\t<li>`CidrBlock`: a CIDR block in the correct format. In a classic network, if a `CidrBlock` contains private IPs on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.</li>\n\t\t<li>`Ipv6CidrBlock`: an IPv6 CIDR block in the correct format. In a classic network, if an `Ipv6CidrBlock` contains private IPv6 addresses on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.</li>\n\t\t<li>`SecurityGroupId`: ID of the security group. It can be the ID of security group to be modified, or the ID of other security group in the same project. All private IPs of all CVMs under the security group will be covered. If this field is used, the policy will automatically change according to the CVM associated with the group ID while being used to match network messages. You don't need to change it manually.</li>\n\t\t<li>`Port`: a single port number such as 80, or a port range in the format of '8000-8010'. You may use this field only if the `Protocol` field takes the value `TCP` or `UDP`.</li>\n\t\t<li>`Action`: only allows ACCEPT or DROP.</li>\n\t\t<li>`CidrBlock`, `Ipv6CidrBlock`, `SecurityGroupId`, and `AddressTemplate` are mutually exclusive. `Protocol` + `Port` and `ServiceTemplate` are mutually exclusive.</li>\n</ul></li></ul></li>\n</ul>"
  },
  "ModifySubnetAttribute": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "Subnet instance ID, such as `subnet-pxir56ns`."
      },
      {
        "name": "SubnetName",
        "desc": "The subnet name. The maximum length is 60 bytes."
      },
      {
        "name": "EnableBroadcast",
        "desc": "Whether the subnet has broadcast enabled."
      }
    ],
    "desc": "This API (ModifySubnetAttribute) is used to modify subnet attributes."
  },
  "DescribeNetworkInterfaces": {
    "params": [
      {
        "name": "NetworkInterfaceIds",
        "desc": "Queries the ID of the ENI instance, such as `eni-pxir56ns`. Each request can have a maximum of 100 instances. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.\n<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>\n<li>subnet-id - String - (Filter condition) Subnet instance ID, such as `subnet-f49l6u0z`.</li>\n<li>network-interface-id - String - (Filter condition) ENI instance ID, such as `eni-5k56k7k7`.</li>\n<li>attachment.instance-id - String - (Filter condition) CVM instance ID, such as `ins-3nqpdn3i`.</li>\n<li>groups.security-group-id - String - (Filter condition) Instance ID of the security group, such as `sg-f9ekbxeq`.</li>\n<li>network-interface-name - String - (Filter condition) ENI instance name.</li>\n<li>network-interface-description - String - (Filter condition) ENI instance description.</li>\n<li>address-ip - String - (Filter condition) Private IPv4 address.</li>\n<li>tag-key - String - Required: no - (Filter condition) Filters by tag key. For more information, see Example 2.</li>\n<li> `tag:tag-key` - String - Required: no - (Filter condition) Filters by tag key pair. For this parameter, `tag-key` will be replaced with a specific tag key. For more information, see Example 3.</li>\n<li>is-primary - Boolean - Required: no - (Filter condition) Filters based on whether it is a primary ENI. If the value is 'true', filter only the primary ENI. If the value is 'false', filter only the secondary ENI. If the secondary filter parameter is provided, filter the both.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      }
    ],
    "desc": "This API (DescribeNetworkInterfaces) is used to query the ENI list."
  },
  "AssociateNetworkAclSubnets": {
    "params": [
      {
        "name": "NetworkAclId",
        "desc": "Network ACL instance ID. Example: acl-12345678."
      },
      {
        "name": "SubnetIds",
        "desc": "Array of subnet instance IDs. Example: [subnet-12345678]"
      }
    ],
    "desc": "This API is used to associate a network ACL with subnets in a VPC instance."
  },
  "DisableCcnRoutes": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "RouteIds",
        "desc": "The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`."
      }
    ],
    "desc": "This API (DisableCcnRoutes) is used to disable CCN routes that are already enabled."
  },
  "InquiryPriceCreateVpnGateway": {
    "params": [
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps."
      },
      {
        "name": "InstanceChargeType",
        "desc": "The VPN gateway billing mode. PREPAID: prepaid means monthly subscription. POSTPAID_BY_HOUR: postpaid means pay-as-you-go. Default: POSTPAID_BY_HOUR. If prepaid mode is specified, the `InstanceChargePrepaid` parameter must be entered."
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "Parameter settings for prepaid billing mode, also known as monthly subscription. This parameter can specify the purchase period and other attributes such as auto-renewal. This parameter is mandatory for prepaid instances."
      }
    ],
    "desc": "This API (InquiryPriceCreateVpnGateway) is used to query the price for VPN gateway creation."
  },
  "ResetVpnConnection": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "VpnConnectionId",
        "desc": "The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`."
      }
    ],
    "desc": "The API (ResetVpnConnection) is used to reset VPN tunnels."
  },
  "CreateCustomerGateway": {
    "params": [
      {
        "name": "CustomerGatewayName",
        "desc": "Customer gateway can be named freely, but the maximum length is 60 characters."
      },
      {
        "name": "IpAddress",
        "desc": "Customer gateway public IP."
      }
    ],
    "desc": "This API (CreateCustomerGateway) is used to create customer gateways."
  },
  "ModifyDirectConnectGatewayAttribute": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "The unique ID of the direct connect gateway, such as `dcg-9o233uri`."
      },
      {
        "name": "DirectConnectGatewayName",
        "desc": "The direct connect gateway name. You can enter any name within 60 characters."
      },
      {
        "name": "CcnRouteType",
        "desc": "The CCN route-learning type. Valid values: `BGP` (Automatic learning), `STATIC` (Static, that is, user-configured). You can only modify `CcnRouteType` for a CCN direct connect gateway with BGP enabled."
      }
    ],
    "desc": "This API is used to modify the attributes of a direct connect gateway.\n"
  },
  "CreateSecurityGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "Security group can be named freely, but cannot exceed 60 characters."
      },
      {
        "name": "GroupDescription",
        "desc": "The remarks for the security group. The maximum length is 100 characters."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID. The default is 0. You can query it on the project management page of the Qcloud console."
      },
      {
        "name": "Tags",
        "desc": "Bound tags, such as [{\"Key\": \"city\", \"Value\": \"shanghai\"}]."
      }
    ],
    "desc": "This API is used to create a security group (SecurityGroup).\n* Note the <a href=\"https://cloud.tencent.com/document/product/213/12453\">maximum number of security groups</a> per project in each region under each account.\n* Both the inbound and outbound rules for a newly created security group are \"Deny All\" by default. You need to call CreateSecurityGroupPolicies to set security group rules based on your needs.\n* You can bind a tag when creating a security group. The tag list in the response indicates the tags that have been successfully added."
  },
  "ModifyNetworkInterfaceAttribute": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-pxir56ns`."
      },
      {
        "name": "NetworkInterfaceName",
        "desc": "The name of the ENI. The maximum length is 60 characters."
      },
      {
        "name": "NetworkInterfaceDescription",
        "desc": "ENI description can be named freely, but the maximum length is 60 characters."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "The specified security groups to be bound with, such as ['sg-1dd51d']."
      }
    ],
    "desc": "This API (ModifyNetworkInterfaceAttribute) is used to modify ENI attributes."
  },
  "DescribeVpnGateways": {
    "params": [
      {
        "name": "VpnGatewayIds",
        "desc": "The VPN gateway instance ID, such as `vpngw-f49l6u0z`. Each request can have a maximum of 100 instances. `VpnGatewayIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `VpnGatewayIds` and `Filters` cannot be specified at the same time.\n<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>\n<li>vpn-gateway-id - String - (Filter condition) VPN instance ID, such as `vpngw-5aluhh9t`.</li>\n<li>vpn-gateway-name - String - (Filter condition) VPN instance name.</li>\n<li>type - String - (Filter condition) VPN gateway type: 'IPSEC', 'SSL'.</li>\n<li>public-ip-address- String - (Filter condition) Public IP.</li>\n<li>renew-flag - String - (Filter condition) Gateway renewal type. Manual renewal: `NOTIFY_AND_MANUAL_RENEW`, Automatic renewal: `NOTIFY_AND_AUTO_RENEW`.</li>\n<li>zone - String - (Filter condition) The availability zone where the VPN is located, such as `ap-guangzhou-2`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The number of request objects."
      }
    ],
    "desc": "This API (DescribeVpnGateways) is used to query the VPN gateway list."
  },
  "DescribeVpcInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter condition. `RouteTableIds` and `Filters` cannot be specified at the same time.\n<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>\n<li>instance-type - String - (Filter condition) CVM instance ID.</li>\n<li>instance-name - String - (Filter condition) CVM name.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset."
      },
      {
        "name": "Limit",
        "desc": "The number of requested objects."
      }
    ],
    "desc": " This API (DescribeVpcInstances) is used to query a list of VCM instances on VPC."
  },
  "CreateDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`"
      },
      {
        "name": "Routes",
        "desc": "The list of IDC IP range that must be connected"
      }
    ],
    "desc": "This API (CreateDirectConnectGatewayCcnRoutes) is used to create the CCN route (IDC IP range) of a Direct Connect gateway."
  },
  "DescribeVpcPrivateIpAddresses": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the `VPC`, such as `vpc-f49l6u0z`."
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "The private `IP` address list. Each request supports a maximum of `10` batch querying."
      }
    ],
    "desc": "This API (DescribeVpcPrivateIpAddresses) is used to query the private IP information of a VPC.<br />\nThis API is used to query only the information of IP addresses that are already in use. When querying IPs that have not yet been used, this API will not report an error, but the IPs will not appear in the returned results."
  },
  "ModifyIpv6AddressesAttribute": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The `ID` of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "Ipv6Addresses",
        "desc": "The information of the specified private `IPv6` addresses."
      }
    ],
    "desc": "This API (ModifyIpv6AddressesAttribute) is used to modify the private IPv6 address attributes of an ENI."
  },
  "DescribeDirectConnectGateways": {
    "params": [
      {
        "name": "DirectConnectGatewayIds",
        "desc": "The unique ID of the direct connect gateway, such as `dcg-9o233uri`."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `DirectConnectGatewayIds` and `Filters` cannot be specified at the same time.\n<li>direct-connect-gateway-id - String - The unique ID of the direct connect gateway, such as `dcg-9o233uri`.</li>\n<li>direct-connect-gateway-name - String - The name of the direct connect gateway. The default is fuzzy query.</li>\n<li>direct-connect-gateway-ip - String - The IP of the direct connect gateway.</li>\n<li>gateway-type - String - The gateway type. Valid values: `NORMAL` (Standard type), `NAT` (NAT type).</li>\n<li>network-type- String - The network type. Valid values: `VPC` (VPC type), `CCN` (CCN type).</li>\n<li>ccn-id - String - The ID of the CCN where the direct connect gateway resides.</li>\n<li>vpc-id - String - The ID of the VPC where the direct connect gateway resides.</li>"
      },
      {
        "name": "Offset",
        "desc": "The offset."
      },
      {
        "name": "Limit",
        "desc": "Max number of results returned"
      }
    ],
    "desc": "This API is used to query direct connect gateways."
  },
  "RenewVpnGateway": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "Billing Methods"
      }
    ],
    "desc": "This API (RenewVpnGateway) is used to renew prepaid (monthly subscription) VPN gateways. Currently, only IPSEC gateways are supported."
  },
  "AssignIpv6Addresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The `ID` of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "Ipv6Addresses",
        "desc": "A list of `IPv6` addresses. You can specify a maximum of 10 at one time. The quota is calculated together with that of `Ipv6AddressCount`, a required input parameter alternative to this one."
      },
      {
        "name": "Ipv6AddressCount",
        "desc": "The number of automatically assigned `IPv6` addresses. The total number of private IP addresses cannot exceed the quota. The quota is calculated together with that of `Ipv6Addresses`, a required input parameter alternative to this one."
      }
    ],
    "desc": "This API (AssignIpv6Addresses) is used to apply for an IPv6 address for the ENI.<br />\nThis API is completed asynchronously. If you need to query the async execution results, use the `RequestId` returned by this API to query the `QueryTask` API.\n* An ENI can only be bound with a limited number of IPs. For more information about resource limits, see<a href=\"/document/product/576/18527\">ENI use limits</a>.\n* You can specify the `IPv6` address when applying. The address type cannot be the primary `IP`. Currently, `IPv6` can only be supported as the secondary `IP`.\n* The address must be unoccupied and is in the subnet to which the ENI belongs.\n* When applying for one to multiple secondary `IPv6` addresses on ENI, the API will return the specified number of secondary `IPv6` addresses in the subnet range where the ENI is located."
  },
  "MigratePrivateIpAddress": {
    "params": [
      {
        "name": "SourceNetworkInterfaceId",
        "desc": "ID of the ENI instance bound with the private IP, such as `eni-m6dyj72l`."
      },
      {
        "name": "DestinationNetworkInterfaceId",
        "desc": "ID of the destination ENI instance to be migrated."
      },
      {
        "name": "PrivateIpAddress",
        "desc": "The private IP to be migrated, such as 10.0.0.6."
      }
    ],
    "desc": " This API (MigratePrivateIpAddress) is used to migrate the private IPs of ENIs.\n\n* This API is used to migrate a private IP from one ENI to another. Primary IPs cannot be migrated.\n* The ENIs before and after migration must belong to the same subnet."
  },
  "DescribeServiceTemplates": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions.\n<li>service-template-name - String - (Filter condition) Protocol port template name.</li>\n<li>service-template-id - String - (Filter condition) Protocol port template instance ID, such as `ppm-e6dy460g`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeServiceTemplates) is used to query protocol port templates."
  },
  "UnassignIpv6CidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the `VPC`, such as `vpc-f49l6u0z`."
      },
      {
        "name": "Ipv6CidrBlock",
        "desc": "The `IPv6` IP range, such as `3402:4e00:20:1000::/56`"
      }
    ],
    "desc": "This API (UnassignIpv6CidrBlock) is used to release IPv6 IP ranges.\nIf the IP range still has occupied IPs that are not yet repossessed, the IP range cannot be released."
  },
  "ModifyNatGatewayDestinationIpPortTranslationNatRule": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      },
      {
        "name": "SourceNatRule",
        "desc": "The port forwarding rule of the source NAT gateway."
      },
      {
        "name": "DestinationNatRule",
        "desc": "The port forwarding rule of the destination NAT gateway."
      }
    ],
    "desc": "This API (ModifyNatGatewayDestinationIpPortTranslationNatRule) is used to modify a port forwarding rule for a NAT gateway."
  },
  "HaVipAssociateAddressIp": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "The unique `ID` of the `HAVIP`, such as `havip-9o233uri`. This must be a `HAVIP` that has not been bound to an `EIP`"
      },
      {
        "name": "AddressIp",
        "desc": "The Elastic `IP`. This must be an `EIP` that has not been bound to a `HAVIP`"
      }
    ],
    "desc": "This API (HaVipAssociateAddressIp) is used to bind an EIP to an HAVIP.<br />\nThis API is completed asynchronously. If you need to query the async job execution results, please use the `RequestId` returned by this API to query the `QueryTask` API."
  },
  "DescribeHaVips": {
    "params": [
      {
        "name": "HaVipIds",
        "desc": "The unique `ID` of the `HAVIP`, such as `havip-9o233uri`."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `HaVipIds` and `Filters` cannot be specified at the same time.\n<li>havip-id - String - The unique `ID` of the `HAVIP`, such as `havip-9o233uri`.</li>\n<li>havip-name - String - `HAVIP` name.</li>\n<li>vpc-id - String - The `ID` of the VPC where `HAVIP` is located.</li>\n<li>subnet-id - String - The `ID` of the subnet where `HAVIP` is located.</li>\n<li>address-ip - String - The `EIP` to which `HAVIP` is bound.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      }
    ],
    "desc": "This API (DescribeHaVips) is used to query the list of highly available virtual IPs (HAVIP)."
  },
  "AssociateNetworkInterfaceSecurityGroups": {
    "params": [
      {
        "name": "NetworkInterfaceIds",
        "desc": "ENI instance ID, e.g. eni-pxir56ns. You can enter up to 100 instances for each request."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups. You can enter up to 100 instances for each request."
      }
    ],
    "desc": "This API (AssociateNetworkInterfaceSecurityGroups) is used to attach a security group to an ENI."
  },
  "DeleteHaVip": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "The unique `ID` of the `HAVIP`, such as `havip-9o233uri`."
      }
    ],
    "desc": "This API (DeleteHaVip) is used to delete Highly Available Virtual IP (HAVIP)<br />\nThis API is completed asynchronously. If you need to query the async job execution results, please use the `RequestId` returned by this API to query the `QueryTask` API."
  },
  "ModifyBandwidthPackageAttribute": {
    "params": [
      {
        "name": "BandwidthPackageId",
        "desc": "The unique ID of the bandwidth package."
      },
      {
        "name": "BandwidthPackageName",
        "desc": "The name of the bandwidth package."
      },
      {
        "name": "ChargeType",
        "desc": "The billing mode of the bandwidth package."
      }
    ],
    "desc": "This API is used to modify the attributes of a bandwidth package, including the bandwidth package name, and so on."
  },
  "DescribeAddressQuota": {
    "params": [],
    "desc": "This API (DescribeAddressQuota) is used to query the quota information of your [Elastic IP](https://cloud.tencent.com/document/product/213/1941) (EIP) in the current region. For more information, see [EIP product introduction](https://cloud.tencent.com/document/product/213/5733)."
  },
  "ModifyVpnGatewayAttribute": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "VpnGatewayName",
        "desc": "The VPN gateway name. The maximum length is 60 bytes."
      },
      {
        "name": "InstanceChargeType",
        "desc": "VPN gateway billing mode. Currently, only the conversion of prepaid (monthly subscription) to postpaid (that is, pay-as-you-go) is supported. That is, the parameters only supports POSTPAID_BY_HOUR."
      }
    ],
    "desc": "This API (ModifyVpnGatewayAttribute) is used to modify the attributes of VPN gateways."
  },
  "ResetVpnGatewayInternetMaxBandwidth": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps."
      }
    ],
    "desc": "This API (ResetVpnGatewayInternetMaxBandwidth) is used to adjust the bandwidth cap of VPN gateways. Currently, only configuration upgrade is supported. VPN gateways with monthly subscription must be within the validity period."
  },
  "DeleteVpc": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      }
    ],
    "desc": "This API (DeleteVpc) is used to delete VPCs.\n* Before deleting a VPC, ensure that the VPC contains no resources, including CVMs, cloud databases, NoSQL databases, VPN gateways, direct connect gateways, load balancers, peering connections, and basic network devices that are linked to the VPC.\n* The deletion of VPCs is irreversible. Proceed with caution."
  },
  "DescribeSubnets": {
    "params": [
      {
        "name": "SubnetIds",
        "desc": "Queries the ID of the subnet instance, such as `subnet-pxir56ns`. Each request can have a maximum of 100 instances. `SubnetIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `SubnetIds` and `Filters` cannot be specified at the same time.\n<li>subnet-id - String - (Filter condition) Subnet instance name.</li>\n<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>\n<li>cidr-block - String - (Filter condition) The subnet IP range, such as 192.168.1.0.</li>\n<li>is-default - Boolean - (Filter condition) Whether it is the default subnet.</li>\n<li>is-remote-vpc-snat - Boolean - (Filter condition) Whether it is a VPC SNAT address pool subnet.</li>\n<li>subnet-name - String - (Filter condition) Subnet name.</li>\n<li>zone - String - (Filter condition) Availability zone.</li>\n<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>\n<li>tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key is replaced with the specific tag key. For usage, refer to case 2.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      }
    ],
    "desc": "This API (DescribeSubnets) is used to query the list of subnets."
  },
  "CreateCcn": {
    "params": [
      {
        "name": "CcnName",
        "desc": "The name of the CCN. The maximum length is 60 characters."
      },
      {
        "name": "CcnDescription",
        "desc": "The description of the CCN. The maximum length is 100 characters."
      },
      {
        "name": "QosLevel",
        "desc": "CCN service quality, 'PT': Platinum, 'AU': Gold, 'AG': Silver. The default is 'AU'."
      },
      {
        "name": "InstanceChargeType",
        "desc": "The billing method. POSTPAID: postpaid by traffic. Default: POSTPAID."
      },
      {
        "name": "BandwidthLimitType",
        "desc": "The bandwidth limit type. OUTER_REGION_LIMIT: regional outbound limit. INTER_REGION_LIMIT: inter-regional limit. Default: OUTER_REGION_LIMIT."
      },
      {
        "name": "Tags",
        "desc": "Bound tags, such as [{\"Key\": \"city\", \"Value\": \"shanghai\"}]."
      }
    ],
    "desc": "This API is used to create a Cloud Connect Network (CCN).<br />\n* You can bind a tag when creating a CCN instance. The tag list in the response indicates the tags that have been successfully added.\nEach account can only create a limited number of CCN instances. For more information, see product documentation. To create more instances, contact the online customer service."
  },
  "ModifyCustomerGatewayAttribute": {
    "params": [
      {
        "name": "CustomerGatewayId",
        "desc": "The ID of the customer gateway, such as `cgw-2wqq41m9`. You can query the customer gateway by using the `DescribeCustomerGateways` API."
      },
      {
        "name": "CustomerGatewayName",
        "desc": "Customer gateway can be named freely, but the maximum length is 60 characters."
      }
    ],
    "desc": "This API (ModifyCustomerGatewayAttribute) is used to modify the customer gateway information."
  },
  "ModifyVpnConnectionAttribute": {
    "params": [
      {
        "name": "VpnConnectionId",
        "desc": "The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`."
      },
      {
        "name": "VpnConnectionName",
        "desc": "VPN tunnel can be named freely, but the maximum length is 60 characters."
      },
      {
        "name": "PreShareKey",
        "desc": "The pre-shared key."
      },
      {
        "name": "SecurityPolicyDatabases",
        "desc": "The SPD policy group, for example: {\"10.0.0.5/24\":[\"172.123.10.5/16\"]}. 10.0.0.5/24 is the VPC internal IP range, and 172.123.10.5/16 is the IDC IP range. The user specifies the IP range in the VPC that can communicate with the IP range in the IDC."
      },
      {
        "name": "IKEOptionsSpecification",
        "desc": "IKE (Internet Key Exchange) configuration. IKE comes with a self-protection mechanism. The network security protocol is configured by the user."
      },
      {
        "name": "IPSECOptionsSpecification",
        "desc": "IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud."
      }
    ],
    "desc": "This API (ModifyVpnConnectionAttribute) is used to modify VPN tunnels."
  },
  "DescribeSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through `DescribeSecurityGroups`. Each request can have a maximum of 100 instances. `SecurityGroupIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions. `SecurityGroupIds` and `Filters` cannot be specified at the same time.\n<li>security-group-id - String - (Filter condition) The security group ID.</li>\n<li>project-id - Integer - (Filter condition) The project ID.</li>\n<li>security-group-name - String - (Filter condition) The security group name.</li>\n<li>tag-key - String - Required: no - (Filter condition) Filters by tag key. For more information, see Example 2.</li>\n<li> `tag:tag-key` - String - Required: no - (Filter condition) Filters by tag key pair. For this parameter, `tag-key` will be replaced with a specific tag key. For more information, see Example 3.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      }
    ],
    "desc": "This API (DescribeSecurityGroups) is used to query security groups."
  },
  "CreateVpnGateway": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "VpnGatewayName",
        "desc": "The VPN gateway name. The maximum length is 60 bytes."
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps"
      },
      {
        "name": "InstanceChargeType",
        "desc": "The VPN gateway billing mode. PREPAID: prepaid means monthly subscription. POSTPAID_BY_HOUR: postpaid means pay-as-you-go. Default: POSTPAID_BY_HOUR. If prepaid mode is specified, the `InstanceChargePrepaid` parameter must be entered."
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "Parameter settings for prepaid billing mode, also known as monthly subscription. This parameter can specify the purchase period and other attributes such as auto-renewal. This parameter is mandatory for prepaid instances."
      },
      {
        "name": "Zone",
        "desc": "The availability zone, such as `ap-guangzhou-2`."
      },
      {
        "name": "Type",
        "desc": "VPN gateway type. Value: `CCN`, indicates CCN-type VPN gateway"
      }
    ],
    "desc": "This API (CreateVpnGateway) is used to create a VPN gateway."
  },
  "ModifyPrivateIpAddressesAttribute": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "The specified private IP information."
      }
    ],
    "desc": "This API (ModifyPrivateIpAddressesAttribute) is used to modify the private IP attributes of an ENI."
  },
  "DescribeAssistantCidr": {
    "params": [
      {
        "name": "VpcIds",
        "desc": "The ID of a VPC instance set, such as `vpc-6v2ht8q5`."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.\n<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      }
    ],
    "desc": "This API (DescribeAssistantCidr) is used to query a list of secondary CIDR blocks. (To use this API that is in Beta, please submit a ticket.)"
  },
  "CreateDirectConnectGateway": {
    "params": [
      {
        "name": "DirectConnectGatewayName",
        "desc": "The name of the direct connect gateway."
      },
      {
        "name": "NetworkType",
        "desc": "The type of the associated network. Valid values:\n<li>VPC</li>\n<li>CCN</li>"
      },
      {
        "name": "NetworkInstanceId",
        "desc": "<li>When the NetworkType is VPC, this value is the VPC instance ID</li>\n<li>When the NetworkType is CCN, this value is the CCN instance ID</li>"
      },
      {
        "name": "GatewayType",
        "desc": "The type of the gateway. Valid values:\n<li>NORMAL - (Default) Standard type. Note: CCN only supports the standard type</li>\n<li>NAT - NAT type</li>NAT gateway supports network address translation. The specified type cannot be modified. A VPC can create one NAT direct connect gateway and one non-NAT direct connect gateway"
      }
    ],
    "desc": "This API is used to create a direct connect gateway."
  },
  "DetachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "Instances",
        "desc": "The list of network instances to be unbound"
      }
    ],
    "desc": "This API (DetachCcnInstances) is used to unbind a specified network instance from a CCN instance.<br />\nAfter unbinding the network instance, the corresponding routing policy will also be deleted."
  },
  "DetachClassicLinkVpc": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "InstanceIds",
        "desc": "Queries the ID of the CVM instance, such as `ins-r8hr2upy`."
      }
    ],
    "desc": "This API (DetachClassicLinkVpc) is used to delete a Classiclink."
  },
  "SetCcnRegionBandwidthLimits": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "CcnRegionBandwidthLimits",
        "desc": "The outbound bandwidth cap of each CCN region."
      }
    ],
    "desc": "This API (SetCcnRegionBandwidthLimits) is used to set the outbound bandwidth cap for CCNs in each region. This API can only set the outbound bandwidth cap for regions in the network instances that have already been associated."
  },
  "CreateHaVip": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the VPC to which the `HAVIP` belongs."
      },
      {
        "name": "SubnetId",
        "desc": "The `ID` of the subnet to which the `HAVIP` belongs."
      },
      {
        "name": "HaVipName",
        "desc": "The name of the `HAVIP`."
      },
      {
        "name": "Vip",
        "desc": "The specified virtual IP address, which must be within the IP range of the `VPC` and not in use. It will be automatically assigned if not specified."
      }
    ],
    "desc": "This API (CreateHaVip) is used to create a highly available virtual IP (HAVIP)"
  },
  "MigrateNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "SourceInstanceId",
        "desc": "The ID of the CVM bound to the ENI, such as `ins-r8hr2upy`."
      },
      {
        "name": "DestinationInstanceId",
        "desc": "ID of the destination CVM instance to be migrated."
      }
    ],
    "desc": "This API (MigrateNetworkInterface) is used to migrate ENIs."
  },
  "ReleaseAddresses": {
    "params": [
      {
        "name": "AddressIds",
        "desc": "The unique ID list of the EIP. The unique ID of an EIP is as follows: `eip-11112222`."
      }
    ],
    "desc": "This API (ReleaseAddresses) is used to release one or multiple [Elastic IPs](https://cloud.tencent.com/document/product/213/1941).\n* This operation is irreversible. Once you release an EIP, the IP address associated with the EIP no longer belongs to you.\n* Only EIPs in UNBIND status can be released."
  },
  "DisassociateNetworkAclSubnets": {
    "params": [
      {
        "name": "NetworkAclId",
        "desc": "Network ACL instance ID. Example: acl-12345678."
      },
      {
        "name": "SubnetIds",
        "desc": "Array of subnet instance IDs. Example: [subnet-12345678]."
      }
    ],
    "desc": "This API is used to disassociate a network ACL from subnets in a VPC instance."
  },
  "EnableCcnRoutes": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "RouteIds",
        "desc": "The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`."
      }
    ],
    "desc": "This API (EnableCcnRoutes) is used to enable CCN routes that are already added.<br />\nThis API is used to verify whether there will be conflict with an existing route after a CCN route is enabled. If there is a conflict, the route will not be enabled, and the process will fail. When a conflict occurs, you must disable the conflicting route before you can enable the desired route."
  },
  "ModifyRouteTableAttribute": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "The route table instance ID, such as `rtb-azd4dt1c`."
      },
      {
        "name": "RouteTableName",
        "desc": "Route table name."
      }
    ],
    "desc": "This API (ModifyRouteTableAttribute) is used to modify the attributes of a route table."
  },
  "CreateNatGateway": {
    "params": [
      {
        "name": "NatGatewayName",
        "desc": "NAT gateway name"
      },
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The maximum outbound bandwidth of the NAT gateway (unit: Mbps). Supported parameter values: `20, 50, 100, 200, 500, 1000, 2000, 5000`. Default: `100Mbps`."
      },
      {
        "name": "MaxConcurrentConnection",
        "desc": "The concurrent connection cap of the NAT gateway. Supported parameter values: `1000000, 3000000, 10000000`. The default value is `100000`."
      },
      {
        "name": "AddressCount",
        "desc": "The number of EIPs that needs to be applied for. The system will create N number of EIPs according to your requirements. Either AddressCount or PublicAddresses must be passed in."
      },
      {
        "name": "PublicIpAddresses",
        "desc": "The EIP array bound to the NAT gateway. Either AddressCount or PublicAddresses must be passed in."
      },
      {
        "name": "Zone",
        "desc": "The availability zone, such as `ap-guangzhou-1`."
      },
      {
        "name": "Tags",
        "desc": "Bound tags, such as [{\"Key\": \"city\", \"Value\": \"shanghai\"}]."
      }
    ],
    "desc": "This API (CreateNatGateway) is used to create a NAT gateway."
  },
  "ModifyNetDetect": {
    "params": [
      {
        "name": "NetDetectId",
        "desc": "The ID of a network detection instance, such as `netd-12345678`."
      },
      {
        "name": "NetDetectName",
        "desc": "The name of a network detection instance. The maximum length is 60 characters."
      },
      {
        "name": "DetectDestinationIp",
        "desc": "The array of detection destination IPv4 addresses, which contains at most two IP addresses."
      },
      {
        "name": "NextHopType",
        "desc": "The type of the next hop. Currently supported types are:\nVPN: VPN gateway;\nDIRECTCONNECT: direct connect gateway;\nPEERCONNECTION: peering connection;\nNAT: NAT gateway;\nNORMAL_CVM: normal CVM."
      },
      {
        "name": "NextHopDestination",
        "desc": "The next-hop destination gateway. The value is related to NextHopType.\nIf NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.\nIf NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.\nIf NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.\nIf NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.\nIf NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12."
      },
      {
        "name": "NetDetectDescription",
        "desc": "Network detection description."
      }
    ],
    "desc": "This API (ModifyNetDetect) is used to modify network detection parameters."
  },
  "DisableGatewayFlowMonitor": {
    "params": [
      {
        "name": "GatewayId",
        "desc": "Gateway instance ID, which currently supports these types:\nID of Direct Connect gateway instance, e.g. `dcg-ltjahce6`;\nID of NAT gateway instance, e.g. `nat-ltjahce6`;\nID of VPN gateway instance, e.g. `vpn-ltjahce6`."
      }
    ],
    "desc": "This API (DisableGatewayFlowMonitor) is used to disable gateway flow monitor."
  },
  "DeleteNatGatewayDestinationIpPortTranslationNatRule": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      },
      {
        "name": "DestinationIpPortTranslationNatRules",
        "desc": "The port forwarding rules of the NAT gateway."
      }
    ],
    "desc": "This API (DeleteNatGatewayDestinationIpPortTranslationNatRule) is used to delete a port forwarding rule for a NAT gateway."
  },
  "CreateRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "Route table instance ID."
      },
      {
        "name": "Routes",
        "desc": "Routing policy object."
      }
    ],
    "desc": "This API (CreateRoutes) is used to create a routing policy.\n* You can create routing policies in batch for a specified route table."
  },
  "CreateNetDetect": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of a `VPC` instance, such as `vpc-12345678`."
      },
      {
        "name": "SubnetId",
        "desc": "The ID of a subnet instance, such as subnet-12345678."
      },
      {
        "name": "NetDetectName",
        "desc": "The name of a network detection instance. The maximum length is 60 characters."
      },
      {
        "name": "DetectDestinationIp",
        "desc": "The array of detection destination IPv4 addresses, which contains at most two IP addresses."
      },
      {
        "name": "NextHopType",
        "desc": "The type of the next hop. Currently supported types are:\nVPN: VPN gateway;\nDIRECTCONNECT: direct connect gateway;\nPEERCONNECTION: peering connection;\nNAT: NAT gateway;\nNORMAL_CVM: normal CVM."
      },
      {
        "name": "NextHopDestination",
        "desc": "The next-hop destination gateway. The value is related to NextHopType.\nIf NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.\nIf NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.\nIf NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.\nIf NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.\nIf NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12."
      },
      {
        "name": "NetDetectDescription",
        "desc": "Network detection description."
      }
    ],
    "desc": "This API is used to create a network detection instance."
  },
  "ModifyHaVipAttribute": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "The unique `ID` of the `HAVIP`, such as `havip-9o233uri`."
      },
      {
        "name": "HaVipName",
        "desc": "`HAVIP` can be named freely, but the maximum length is 60 characters."
      }
    ],
    "desc": "This API (ModifyHaVipAttribute) is used to modify HAVIP attributes."
  },
  "ResetAttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "CcnUin",
        "desc": "The UIN (root account) to which the CCN belongs."
      },
      {
        "name": "Instances",
        "desc": "The list of network instances that re-apply for association."
      }
    ],
    "desc": "This API (ResetAttachCcnInstances) is used to re-apply for the association operation when the application for cross-account instance association expires."
  },
  "DescribeBandwidthPackages": {
    "params": [
      {
        "name": "BandwidthPackageIds",
        "desc": "The unique ID list of bandwidth packages."
      },
      {
        "name": "Filters",
        "desc": "Each request can have up to 10 `Filters`. `BandwidthPackageIds` and `Filters` cannot be specified at the same time. The specific filter conditions are as follows:\n<li> bandwidth-package_id - String - Required: No - (Filter condition) Filter by the unique ID of the bandwidth package.</li>\n<li> bandwidth-package-name - String - Required: No - (Filter condition) Filter by the bandwidth package name. Fuzzy filtering is not supported.</li>\n<li> network-type - String - Required: No - (Filter condition) Filter by the bandwidth package type. Types include 'BGP', 'SINGLEISP', and 'ANYCAST'.</li>\n<li> charge-type - String - Required: No - (Filter condition) Filter by the bandwidth package billing mode. Billing modes include 'TOP5_POSTPAID_BY_MONTH' and 'PERCENT95_POSTPAID_BY_MONTH'.</li>\n<li> resource.resource-type - String - Required: No - (Filter condition) Filter by the bandwidth package resource type. Resource types include 'Address' and 'LoadBalance'.</li>\n<li> resource.resource-id - String - Required: No - (Filter condition) Filter by the bandwidth package resource ID, such as 'eip-xxxx' and 'lb-xxxx'.</li>\n<li> resource.address-ip - String - Required: No - (Filter condition) Filter by the bandwidth package resource IP.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset of the query results"
      },
      {
        "name": "Limit",
        "desc": "Max number of the bandwidth packages to be returned."
      }
    ],
    "desc": "This API is used to query bandwidth package information, including the unique ID of the bandwidth package, the type, the billing mode, the name, and the resource information."
  },
  "CreateServiceTemplateGroup": {
    "params": [
      {
        "name": "ServiceTemplateGroupName",
        "desc": "Group name of the protocol port template."
      },
      {
        "name": "ServiceTemplateIds",
        "desc": "Instance ID of the protocol port template, such as `ppm-4dw6agho`."
      }
    ],
    "desc": "This API (CreateServiceTemplateGroup) is used to create a protocol port template group."
  },
  "ReplaceRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "The route table instance ID, such as `rtb-azd4dt1c`."
      },
      {
        "name": "Routes",
        "desc": "Routing policy object. The routing policy ID (RouteId) must be specified."
      }
    ],
    "desc": "This API (ReplaceRoutes) is used to modify a specified routing policy by its ID (RouteId). Batch modification is supported."
  },
  "ModifyCcnAttribute": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "CcnName",
        "desc": "The name of the CCN. The maximum length is 60 characters."
      },
      {
        "name": "CcnDescription",
        "desc": "The description of the CCN. The maximum length is 100 characters."
      }
    ],
    "desc": "This API (ModifyCcnAttribute) is used to modify CCN attributes."
  },
  "CreateAddressTemplateGroup": {
    "params": [
      {
        "name": "AddressTemplateGroupName",
        "desc": "The name of the IP address template group."
      },
      {
        "name": "AddressTemplateIds",
        "desc": "The instance ID of the IP address template, such as `ipm-mdunqeb6`."
      }
    ],
    "desc": "This API (CreateAddressTemplateGroup) is used to create an IP address template group."
  },
  "DescribeSecurityGroupAssociationStatistics": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "The Security instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups."
      }
    ],
    "desc": "This API (DescribeSecurityGroupAssociationStatistics) is used to query statistics on the instances associated with a security group."
  },
  "UnassignIpv6SubnetCidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the VPC where the subnet is located, such as `vpc-f49l6u0z`."
      },
      {
        "name": "Ipv6SubnetCidrBlocks",
        "desc": "The `IPv6` subnet IP range list."
      }
    ],
    "desc": "This API (UnassignIpv6SubnetCidrBlock) is used to release IPv6 subnet IP ranges.\nIf the subnet IP range still has occupied IPs that are not yet repossessed, the subnet IP range cannot be released."
  },
  "DescribeAddressTemplates": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions.\n<li>address-template-name - String - (Filter condition) IP address template name.</li>\n<li>address-template-id - String - (Filter condition) IP address template instance ID, such as `ipm-mdunqeb6`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeAddressTemplates) is used to query an IP address template."
  },
  "CreateAddressTemplate": {
    "params": [
      {
        "name": "AddressTemplateName",
        "desc": "The name of the IP address template"
      },
      {
        "name": "Addresses",
        "desc": "Address information, including IP, CIDR and IP address range."
      }
    ],
    "desc": "This API (CreateAddressTemplate) is used to create an IP address template."
  },
  "ModifyAddressAttribute": {
    "params": [
      {
        "name": "AddressId",
        "desc": "The unique ID of the EIP, such as `eip-11112222`."
      },
      {
        "name": "AddressName",
        "desc": "The EIP name after modification. The maximum length is 20 characters."
      },
      {
        "name": "EipDirectConnection",
        "desc": "Whether the set EIP is a direct connection EIP. TRUE: yes. FALSE: no. Note that this parameter is available only to users who have activated the EIP direct connection function."
      }
    ],
    "desc": "This API (ModifyAddressAttribute) is used to modify the name of an [Elastic IP](https://cloud.tencent.com/document/product/213/1941)."
  },
  "DescribeAddressTemplateGroups": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions.\n<li>address-template-group-name - String - (Filter condition) IP address template group name.</li>\n<li>address-template-group-id - String - (Filter condition) IP address template group instance ID, such as `ipmg-mdunqeb6`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeAddressTemplateGroups) is used to query an IP address template group."
  },
  "TransformAddress": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "The ID of the instance with a common public IP to be operated on, such as `ins-11112222`. You can query the instance ID by logging into the [Console](https://console.cloud.tencent.com/cvm). You can also obtain the parameter value from the `InstanceId` field in the returned result of [DescribeInstances](https://cloud.tencent.com/document/api/213/9389) API."
      }
    ],
    "desc": "This API (TransformAddress) is used to switch common public IPs into [Elastic IPs](https://cloud.tencent.com/document/product/213/1941).\n* The platform limits the number of times that a user can unbind an EIP and reassign public IPs in each region per day. For more information, see [EIP product introduction](/document/product/213/1941)). The preceding quota can be obtained through the [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) API."
  },
  "CreateSecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "Security group policy set."
      }
    ],
    "desc": "This API is used to create security group policies (SecurityGroupPolicy).\n\nFor parameters of SecurityGroupPolicySet,\n<ul>\n<li>`Version`: the version number of a security group policy, which automatically increases by one each time you update the security policy, to prevent expiration of the updated routing policies. If it is left empty, any conflicts will be ignored.</li>\n<li>When creating the `Egress` and `Ingress` polices,<ul>\n<li>`Protocol`: allows TCP, UDP, ICMP, ICMPV6, GRE, or ALL.</li>\n<li>`CidrBlock`: a CIDR block in the correct format. In a classic network, if a `CidrBlock` contains private IPs on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.</li>\n<li>`Ipv6CidrBlock`: an IPv6 CIDR block in the correct format. In a classic network, if an `Ipv6CidrBlock` contains private IPv6 addresses on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.</li>\n<li>`SecurityGroupId`: ID of the security group. It can be the ID of security group to be modified, or the ID of other security group in the same project. All private IPs of all CVMs under the security group will be covered. If this field is used, the policy will automatically change according to the CVM associated with the group ID while being used to match network messages. You don't need to change it manually.</li>\n<li>`Port`: a single port number such as 80, or a port range in the format of '8000-8010'. You may use this field only if the `Protocol` field takes the value `TCP` or `UDP`. Otherwise `Protocol` and `Port` are mutually exclusive.</li>\n<li>`Action`: only allows `ACCEPT` or `DROP`.</li>\n<li>`CidrBlock`, `Ipv6CidrBlock`, `SecurityGroupId`, and `AddressTemplate` are mutually exclusive. `Protocol` + `Port` and `ServiceTemplate` are mutually exclusive.</li>\n<li>You can only create policies in one direction in each request. To specify the `PolicyIndex` parameter, use the same index number in policies.</li>\n</ul></li></ul>"
  },
  "ModifyNetworkAclAttribute": {
    "params": [
      {
        "name": "NetworkAclId",
        "desc": "Network ACL instance ID. Example: acl-12345678."
      },
      {
        "name": "NetworkAclName",
        "desc": "Name of the network ACL. The maximum length is 60 bytes."
      }
    ],
    "desc": "This API is used to modify the attributes of a network ACL."
  },
  "ResetNatGatewayConnection": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "NAT gateway ID."
      },
      {
        "name": "MaxConcurrentConnection",
        "desc": "Concurrent connections cap of the NAT gateway, such as 1000000, 3000000, 10000000."
      }
    ],
    "desc": "This API (ResetNatGatewayConnection) is used to adjust concurrent connection cap for the NAT gateway."
  },
  "ModifyVpcAttribute": {
    "params": [
      {
        "name": "VpcId",
        "desc": "Security group can be named freely, but cannot exceed 60 characters."
      },
      {
        "name": "VpcName",
        "desc": "VPC can be named freely, but the maximum length is 60 characters."
      },
      {
        "name": "EnableMulticast",
        "desc": "Whether multicast is enabled. `true`: Enabled. `false`: Off."
      },
      {
        "name": "DnsServers",
        "desc": "DNS address. A maximum of 4 addresses is supported. The first one is primary server by default, and the rest are secondary servers."
      },
      {
        "name": "DomainName",
        "desc": "Domain name"
      }
    ],
    "desc": "This API (ModifyVpcAttribute) is used to modify VPC attributes."
  },
  "CreateSecurityGroupWithPolicies": {
    "params": [
      {
        "name": "GroupName",
        "desc": "Security group can be named freely, but cannot exceed 60 characters."
      },
      {
        "name": "GroupDescription",
        "desc": "The remarks for the security group. The maximum length is 100 characters."
      },
      {
        "name": "ProjectId",
        "desc": "The project id is 0 by default. You can query this in the project management page of the Qcloud console."
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "Security group policy set."
      }
    ],
    "desc": "This API (CreateSecurityGroupWithPolicies) is used to create security groups, and add security group policies.\n* Note the<a href=\"https://cloud.tencent.com/document/product/213/12453\">maximum number of security groups</a>per project in each region under each account.\n* Both the inbound and outbound policies for a newly created security group are Deny All by default. You need to call CreateSecurityGroupPolicies to set security group policies according to your needs.\n\nDescription:\n* `Version`: Indicates the version number of a security group policy, which will automatically increment by 1 every time you update the security policy, to prevent the expiration of the updated policies. If this field is left empty, any conflicts will be ignored.\n* `Protocol`: Values can be TCP, UDP, ICMP, ICMPV6, GRE, or ALL.\n* `CidrBlock`:  A CIDR block in the correct format. In a basic network, if a CidrBlock contains private IPs on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.\n* `Ipv6CidrBlock`: An IPv6 CIDR block in the correct format. In a basic network, if an Ipv6CidrBlock contains private IPv6 addresses on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.\n* `SecurityGroupId`: ID of the security group. It can be in the same project as the security group to be modified, including the ID of the security group itself, to represent private IP addresses of all CVMs under the security group. If this field is used, the policy will change without manual modification according to the CVM associated with the policy ID while being used to match network messages.\n* `Port`: A single port number, or a port range in the format of '8000-8010'. The Port field is accepted only if the value of the `Protocol` field is `TCP` or `UDP`. Otherwise Protocol and Port are mutually exclusive. \n* `Action`: Values can be `ACCEPT` or `DROP`.\n* CidrBlock, Ipv6CidrBlock, SecurityGroupId, and AddressTemplate are exclusive and cannot be entered at the same time. 'Protocol + Port' and ServiceTemplate are mutually exclusive and cannot be entered at the same time.\n* Only policies in one direction can be created in each request. If you need to specify the `PolicyIndex` parameter, the indexes of policies must be consistent."
  }
}