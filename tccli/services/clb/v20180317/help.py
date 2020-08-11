# -*- coding: utf-8 -*-
DESC = "clb-2018-03-17"
INFO = {
  "RegisterTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "Targets",
        "desc": "List of real servers to be bound. Array length limit: 20"
      },
      {
        "name": "LocationId",
        "desc": "Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url"
      },
      {
        "name": "Domain",
        "desc": "Target forwarding rule domain name. This parameter does not take effect if LocationId is specified"
      },
      {
        "name": "Url",
        "desc": "Target forwarding rule URL. This parameter does not take effect if LocationId is specified"
      }
    ],
    "desc": "This API (RegisterTargets) is used to bind one or more real servers to a CLB listener or layer-7 forwarding rule. Before using this API, you need to create relevant layer-4 listeners or layer-7 forwarding rules. For the former (TCP/UDP), only the listener ID needs to be specified, while for the latter (HTTP/HTTPS), the forwarding rule also needs to be specified through LocationId or Domain+Url.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "SetLoadBalancerSecurityGroups": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "SecurityGroups",
        "desc": "Array of security group IDs. One CLB instance can be bound to up to 50 security groups. If you want to unbind all security groups, you do not need to pass in this parameter, or you can pass in an empty array."
      }
    ],
    "desc": "This API (SetLoadBalancerSecurityGroups) is used to bind/unbind security groups for a public network CLB instance. You can use the DescribeLoadBalancers API to query the security groups bound to a CLB instance. This API uses `set` semantics.\nDuring a binding operation, the input parameters need to be all security groups to be bound to the CLB instance (including those already bound ones and new ones).\nDuring an unbinding operation, the input parameters need to be all the security groups still bound to the CLB instance after the unbinding operation. To unbind all security groups, you can leave this parameter empty or pass in an empty array. Note: Private network CLB do not support binding security groups."
  },
  "DescribeClassicalLBListeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerIds",
        "desc": "List of CLB listener IDs"
      },
      {
        "name": "Protocol",
        "desc": "CLB listening protocol. Value range: TCP, UDP, HTTP, HTTPS"
      },
      {
        "name": "ListenerPort",
        "desc": "CLB listening port. Value range: [1-65535]"
      },
      {
        "name": "Status",
        "desc": "Listener status. Value range: 0 (creating), 1 (running)"
      }
    ],
    "desc": "This API (DescribeClassicalLBListeners) is used to get the listener information of a classic CLB."
  },
  "DescribeBlockIPTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "Async task ID returned by the `ModifyBlockIPList` API"
      }
    ],
    "desc": "This API is used to query the execution status of an async IP blocking (blocklisting) task by the async task ID returned by the `ModifyBlockIPList` API. (This API is in beta test. To use it, please submit a ticket.)"
  },
  "CreateListener": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "Ports",
        "desc": "Specifies for which ports to create listeners. Each port corresponds to a new listener"
      },
      {
        "name": "Protocol",
        "desc": "Listener protocol: TCP, UDP, HTTP, HTTPS, or TCP_SSL (which is currently in beta test. If you want to use it, please submit a ticket for application)"
      },
      {
        "name": "ListenerNames",
        "desc": "List of names of the listeners to be created. The array of names and array of ports are in one-to-one correspondence. If you do not want to name them now, you do not need to provide this parameter."
      },
      {
        "name": "HealthCheck",
        "desc": "Health check parameter, which is applicable only to TCP/UDP/TCP_SSL listeners"
      },
      {
        "name": "Certificate",
        "desc": "Certificate information. This parameter is applicable only to TCP_SSL listeners and HTTPS listeners with the SNI feature not enabled."
      },
      {
        "name": "SessionExpireTime",
        "desc": "Session persistence time in seconds. Value range: 30-3,600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners."
      },
      {
        "name": "Scheduler",
        "desc": "Forwarding method of a listener. Value range: WRR, LEAST_CONN.\nThey represent weighted round robin and least connections, respectively. Default value: WRR. This parameter is applicable only to TCP/UDP/TCP_SSL listeners."
      },
      {
        "name": "SniSwitch",
        "desc": "Whether to enable the SNI feature. This parameter is applicable only to HTTPS listeners"
      },
      {
        "name": "TargetType",
        "desc": "Target real server type. `NODE`: binding a general node; `TARGETGROUP`: binding a target group."
      }
    ],
    "desc": "This API is used to create a listener for a CLB instance.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful."
  },
  "DeleteLoadBalancerSnatIps": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "Unique CLB instance ID, such as lb-12345678"
      },
      {
        "name": "Ips",
        "desc": "Array of the SNAT IP addresses to be deleted"
      }
    ],
    "desc": "This API is used to delete a SNAT IP for a SnatPro CLB instance."
  },
  "DeleteListener": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "ID of the listener to be deleted"
      }
    ],
    "desc": "This API is used to delete a listener from a CLB instance (layer-4 or layer-7).\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "SetSecurityGroupForLoadbalancers": {
    "params": [
      {
        "name": "SecurityGroup",
        "desc": "Security group ID, such as sg-12345678"
      },
      {
        "name": "OperationType",
        "desc": "ADD: bind a security group;\nDEL: unbind a security group"
      },
      {
        "name": "LoadBalancerIds",
        "desc": "Array of CLB instance IDs"
      }
    ],
    "desc": "This API is used to bind or unbind a security group for multiple public network CLB instances. Note: Private network CLB do not support binding security groups."
  },
  "BatchDeregisterTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "Targets",
        "desc": "Unbound targets"
      }
    ],
    "desc": "This API is used to unbind layer-4/layer-7 real servers in batches."
  },
  "RegisterTargetGroupInstances": {
    "params": [
      {
        "name": "TargetGroupId",
        "desc": "Target group ID"
      },
      {
        "name": "TargetGroupInstances",
        "desc": "Server instance array"
      }
    ],
    "desc": "This API is used to register servers to a target group.\nThis is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful."
  },
  "CreateRule": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "Rules",
        "desc": "Information of the new forwarding rule"
      }
    ],
    "desc": "This API (CreateRule) is used to create a forwarding rule under an existing layer-7 CLB listener, where real servers must be bound to the rule instead of the listener.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "AutoRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "`HTTPS:443` listener ID"
      },
      {
        "name": "Domains",
        "desc": "The domain name to be redirected under the listener `HTTPS:443`. If it is left empty, all domain names under the listener `HTTPS:443` will be configured with redirects."
      }
    ],
    "desc": "An HTTPS:443 listener needs to be created first, along with a forwarding rule. When this API is called, an HTTP:80 listener will be created automatically if it did not exist and a forwarding rule corresponding to `Domains` (specified in the input parameter) under the HTTPS:443 listener will also be created. After successful creation, access requests to an HTTP:80 address will be redirected to an HTTPS:443 address automatically."
  },
  "ModifyDomain": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "Domain",
        "desc": "Legacy domain name under a listener."
      },
      {
        "name": "NewDomain",
        "desc": "New domain name. \tLength limit: 1-120. There are three usage formats: non-regular expression, wildcard, and regular expression. A non-regular expression can only contain letters, digits, \"-\", and \".\". In a wildcard, \"*\" can only be at the beginning or the end. A regular expressions must begin with a \"~\"."
      }
    ],
    "desc": "This API (ModifyDomain) is used to modify a domain name under a layer-7 CLB listener.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "DeleteLoadBalancerListeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerIds",
        "desc": "Array of IDs of the listeners to be deleted. If this parameter is left empty, all listeners of the CLB instance will be deleted."
      }
    ],
    "desc": "This API is used to delete multiple listeners of a CLB instance.\nThis is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful."
  },
  "DeleteTargetGroups": {
    "params": [
      {
        "name": "TargetGroupIds",
        "desc": "Target group ID array"
      }
    ],
    "desc": "This API is used to delete a target group."
  },
  "DeregisterTargetsFromClassicalLB": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "InstanceIds",
        "desc": "List of real server instance IDs"
      }
    ],
    "desc": "This API (DeregisterTargetsFromClassicalLB) is used to unbind real servers from a classic load balancer.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful."
  },
  "CreateLoadBalancer": {
    "params": [
      {
        "name": "LoadBalancerType",
        "desc": "CLB instance network type:\nOPEN: public network; INTERNAL: private network."
      },
      {
        "name": "Forward",
        "desc": "CLB instance type. 1: generic CLB instance. Currently, only 1 can be passed in"
      },
      {
        "name": "LoadBalancerName",
        "desc": "CLB instance name, which takes effect only when an instance is created. Rule: 1-50 letters, digits, dashes (-), or underscores (_).\nNote: If this name is the same as the name of an existing CLB instance in the system, the system will automatically generate a name for this newly created instance."
      },
      {
        "name": "VpcId",
        "desc": "Network ID of the backend target server of CLB, which can be obtained through the DescribeVpcEx API. If this parameter is not passed in, it will default to a basic network (\"0\")."
      },
      {
        "name": "SubnetId",
        "desc": "A subnet ID must be specified when you purchase a private network CLB instance in a VPC, and the VIP of this instance will be generated in this subnet."
      },
      {
        "name": "ProjectId",
        "desc": "ID of the project to which a CLB instance belongs, which can be obtained through the DescribeProject API. If this parameter is not passed in, the default project will be used."
      },
      {
        "name": "AddressIPVersion",
        "desc": "IP version. Valid values: IPv4, IPv6, IPv6FullChain. Default value: IPv4. This parameter is applicable only to public network CLB instances."
      },
      {
        "name": "Number",
        "desc": "Number of CLBs to be created. Default value: 1."
      },
      {
        "name": "MasterZoneId",
        "desc": "Sets the primary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1, which is applicable only to public network CLB.\nNote: A primary AZ carries traffic, while a secondary AZ does not carry traffic by default and will be used only if the primary AZ becomes unavailable. The platform will automatically select the optimal secondary AZ. The list of primary AZs in a specific region can be queried through the DescribeMasterZones API."
      },
      {
        "name": "ZoneId",
        "desc": "Specifies an AZ ID for creating a CLB instance, such as ap-guangzhou-1, which is applicable only to public network CLB."
      },
      {
        "name": "InternetAccessible",
        "desc": "CLB network billing mode. This parameter is applicable only to public network CLB instances."
      },
      {
        "name": "VipIsp",
        "desc": "This parameter is applicable only to public network CLB instances. Valid values: CMCC (China Mobile), CTCC (China Telecom), CUCC (China Unicom). If this parameter is not specified, BGP will be used by default. ISPs supported in a region can be queried with the `DescribeSingleIsp` API. If an ISP is specified, only bill-by-bandwidth-package (BANDWIDTH_PACKAGE) can be used as the network billing mode."
      },
      {
        "name": "Tags",
        "desc": "Tags a CLB instance when purchasing it"
      }
    ],
    "desc": "This API (CreateLoadBalancer) is used to create a CLB instance. To use the CLB service, you first need to purchase one or more instances. After this API is called successfully, a unique instance ID will be returned. There are two types of instances: public network and private network. For more information, see the product types in the product documentation.\nNote: (1) To apply for a CLB instance in the specified AZ and cross-AZ disaster recovery, please [submit a ticket](https://console.cloud.tencent.com/workorder/category); (2) Currently, IPv6 is supported only in Beijing, Shanghai, and Guangzhou regions.\nThis is an async API. After it is returned successfully, you can call the DescribeLoadBalancers API to query the status of the instance (such as creating and normal) to check whether it is successfully created."
  },
  "DescribeLoadBalancerListByCertId": {
    "params": [
      {
        "name": "CertIds",
        "desc": "Server or client certificate ID"
      }
    ],
    "desc": "This API is used to query the list of CLB instances associated with a certificate in a region by certificate ID."
  },
  "ModifyListener": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "ListenerName",
        "desc": "New listener name"
      },
      {
        "name": "SessionExpireTime",
        "desc": "Session persistence time in seconds. Value range: 30-3,600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners."
      },
      {
        "name": "HealthCheck",
        "desc": "Health check parameter, which is applicable only to TCP/UDP/TCP_SSL listeners."
      },
      {
        "name": "Certificate",
        "desc": "Certificate information. This parameter is applicable only to HTTPS/TCP_SSL listeners."
      },
      {
        "name": "Scheduler",
        "desc": "Forwarding method of a listener. Value range: WRR, LEAST_CONN.\nThey represent weighted round robin and least connections, respectively. Default value: WRR."
      },
      {
        "name": "SniSwitch",
        "desc": "Whether to enable the SNI feature. This parameter is applicable only to HTTPS listeners. Note: The SNI feature can be enabled but cannot be disabled once enabled."
      }
    ],
    "desc": "This API (ModifyListener) is used to modify the attributes of a CLB listener, such as listener name, health check parameter, certificate information, and forwarding policy.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "DeleteLoadBalancer": {
    "params": [
      {
        "name": "LoadBalancerIds",
        "desc": "Array of IDs of the CLB instances to be deleted. Array length limit: 20"
      }
    ],
    "desc": "This API (DeleteLoadBalancer) is used to delete one or more specified CLB instances.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful."
  },
  "ModifyDomainAttributes": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "Domain",
        "desc": "Domain name, which must be under a created forwarding rule."
      },
      {
        "name": "NewDomain",
        "desc": "New domain name"
      },
      {
        "name": "Certificate",
        "desc": "Domain name certificate information. Note: This is only applicable to SNI-enabled listeners."
      },
      {
        "name": "Http2",
        "desc": "Whether to enable HTTP/2. Note: HTTP/2 can be enabled only for HTTPS domain names."
      },
      {
        "name": "DefaultServer",
        "desc": "Whether to set this domain name as the default domain name. Note: Only one default domain name can be set under one listener."
      },
      {
        "name": "NewDefaultServerDomain",
        "desc": "A listener must be configured with a default domain name. If you need to disable the default domain name, you must specify another one as the new default domain name."
      }
    ],
    "desc": "This API is used to modify the domain name-level attributes of a layer-7 listener's forwarding rule, such as modifying the domain name, changing the DefaultServer, enabling/disabling HTTP/2, and modifying certificates.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful."
  },
  "DisassociateTargetGroups": {
    "params": [
      {
        "name": "Associations",
        "desc": "Array of rules to be unbound"
      }
    ],
    "desc": "This API is used to unbind target groups from a rule.\nThis is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful."
  },
  "CreateLoadBalancerSnatIps": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "Unique CLB instance ID, such as lb-12345678"
      },
      {
        "name": "SnatIps",
        "desc": "Information of the SNAT IP to be added. You can apply for a specified IP or apply for an automatically assigned IP by specifying a subnet."
      }
    ],
    "desc": "This API is used to add a SNAT IP for a SnatPro CLB instance. If SnatPro is not enabled for CLB, it will be automatically enabled after the SNAT IP is added."
  },
  "AssociateTargetGroups": {
    "params": [
      {
        "name": "Associations",
        "desc": "Association array"
      }
    ],
    "desc": "This API is used to bind target groups to CLB listeners (layer-4 protocol) or forwarding rules (layer-7 protocol).\nThis is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful."
  },
  "DeregisterTargetGroupInstances": {
    "params": [
      {
        "name": "TargetGroupId",
        "desc": "Target group ID"
      },
      {
        "name": "TargetGroupInstances",
        "desc": "Information of server to be unbound"
      }
    ],
    "desc": "This API is used to unbind a server from a target group.\nThis is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful."
  },
  "DescribeLoadBalancers": {
    "params": [
      {
        "name": "LoadBalancerIds",
        "desc": "CLB instance ID."
      },
      {
        "name": "LoadBalancerType",
        "desc": "CLB instance network type:\nOPEN: public network; INTERNAL: private network."
      },
      {
        "name": "Forward",
        "desc": "CLB instance type. 1: generic CLB instance; 0: classic CLB instance"
      },
      {
        "name": "LoadBalancerName",
        "desc": "CLB instance name."
      },
      {
        "name": "Domain",
        "desc": "Domain name assigned to a CLB instance by Tencent Cloud. This parameter is meaningful only for the public network classic CLB."
      },
      {
        "name": "LoadBalancerVips",
        "desc": "VIP address of a CLB instance (there can be multiple addresses)"
      },
      {
        "name": "BackendPublicIps",
        "desc": "Public IP of the real server bound to a CLB."
      },
      {
        "name": "BackendPrivateIps",
        "desc": "Private IP of the real server bound to a CLB."
      },
      {
        "name": "Offset",
        "desc": "Data offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned CLB instances. Default value: 20. Maximum value: 100."
      },
      {
        "name": "OrderBy",
        "desc": "Sort by parameter. Value range: LoadBalancerName, CreateTime, Domain, LoadBalancerType."
      },
      {
        "name": "OrderType",
        "desc": "1: reverse; 0: sequential. Default value: reverse by creation time |"
      },
      {
        "name": "SearchKey",
        "desc": "Search field which fuzzy matches name, domain name, or VIP."
      },
      {
        "name": "ProjectId",
        "desc": "ID of the project to which a CLB instance belongs, which can be obtained through the DescribeProject API."
      },
      {
        "name": "WithRs",
        "desc": "Whether a CLB instance is bound to a real server. 0: no; 1: yes; -1: query all."
      },
      {
        "name": "VpcId",
        "desc": "VPC where a CLB instance resides, such as vpc-bhqkbhdx.\nBasic network does not support queries by VpcId."
      },
      {
        "name": "SecurityGroup",
        "desc": "Security group ID, such as sg-m1cc9123"
      },
      {
        "name": "MasterZone",
        "desc": "Master AZ, such as \"100001\" (Guangzhou Zone 1)"
      },
      {
        "name": "Filters",
        "desc": "Each request can have up to 10 `Filters` and 100 `Filter.Values`. Detailed filter conditions:\n<li> internet-charge-type - Type: String - Required: No - Filter by CLB network billing mode, including `TRAFFIC_POSTPAID_BY_HOUR`</li>"
      }
    ],
    "desc": "This API is used to query the list of CLB instances in a region.\n"
  },
  "DescribeBlockIPList": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID."
      },
      {
        "name": "Offset",
        "desc": "Data offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Maximum number of IPs to be returned. Default value: 100,000."
      }
    ],
    "desc": "This API is used to query the list of blocked IPs (blocklist) of a CLB instance. (This API is in beta test. To use it, please submit a ticket.)"
  },
  "DescribeListeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerIds",
        "desc": "Array of IDs of the CLB listeners to be queried"
      },
      {
        "name": "Protocol",
        "desc": "Type of the listener protocol to be queried. Value range: TCP, UDP, HTTP, HTTPS, TCP_SSL"
      },
      {
        "name": "Port",
        "desc": "Port of the listener to be queried"
      }
    ],
    "desc": "This API is used to get the list of listeners by CLB instance ID, listener protocol, or port. If no filter is specified, all listeners under the CLB instance will be returned."
  },
  "DescribeClassicalLBTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      }
    ],
    "desc": "This API (DescribeClassicalLBTargets) is used to get the real servers bound to a classic CLB."
  },
  "CreateTopic": {
    "params": [
      {
        "name": "TopicName",
        "desc": "Log topic name"
      },
      {
        "name": "PartitionCount",
        "desc": "The number of topic partitions, which changes as partitions are split or merged. Each log topic can have up to 50 partitions. If this parameter is not passed in, 1 partition will be created by default and up to 10 partitions are allowed to be created."
      }
    ],
    "desc": "This API is used to create a topic with the full-text index and key-value index enabled by default. The creation will fail if there is no CLB exclusive logset."
  },
  "BatchRegisterTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "Targets",
        "desc": "Binding target"
      }
    ],
    "desc": "This API is used to bind CVM instances or ENIs in batches. It supports cross-region binding and layer-4 and layer-7 (TCP, UDP, HTTP, HTTPS) protocols."
  },
  "DescribeClsLogSet": {
    "params": [],
    "desc": "This API is used to obtain the CLB exclusive logset of a user."
  },
  "DeleteRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "SourceListenerId",
        "desc": "Source listener ID"
      },
      {
        "name": "TargetListenerId",
        "desc": "Target listener ID"
      },
      {
        "name": "RewriteInfos",
        "desc": "Redirection relationship between forwarding rules"
      }
    ],
    "desc": "This API (DeleteRewrite) is used to delete the redirection relationship between the specified forwarding rules."
  },
  "ModifyTargetWeight": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "LocationId",
        "desc": "Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url"
      },
      {
        "name": "Domain",
        "desc": "Target rule domain name. This parameter does not take effect if LocationId is specified"
      },
      {
        "name": "Url",
        "desc": "Target rule URL. This parameter does not take effect if LocationId is specified"
      },
      {
        "name": "Targets",
        "desc": "List of real servers for which to modify the weight"
      },
      {
        "name": "Weight",
        "desc": "New forwarding weight of a real server. Value range: 0-100. Default value: 10. If the Targets.Weight parameter is set, this parameter will not take effect."
      }
    ],
    "desc": "This API (ModifyTargetWeight) is used to modify the forwarding weight of a real server bound to a CLB instance.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "DescribeTaskStatus": {
    "params": [
      {
        "name": "TaskId",
        "desc": "Request ID, i.e., the RequestId parameter returned by the API"
      }
    ],
    "desc": "This API is used to query the execution status of an async task. After non-query APIs (used to create/delete CLB instances, listeners, or rules or to bind/unbind real servers) are called successfully, this API needs to be used to query whether the task is successful."
  },
  "DescribeTargetGroups": {
    "params": [
      {
        "name": "TargetGroupIds",
        "desc": "Target group ID, which is exclusive of `Filters`."
      },
      {
        "name": "Limit",
        "desc": "Limit of the number of displayed results. Default value: 20"
      },
      {
        "name": "Offset",
        "desc": "Starting display offset"
      },
      {
        "name": "Filters",
        "desc": "Filter array, which is exclusive of `TargetGroupIds`. Valid values: TargetGroupVpcId, TargetGroupName"
      }
    ],
    "desc": "This API is used to query the target group information."
  },
  "ModifyRule": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "LocationId",
        "desc": "ID of the forwarding rule to be modified."
      },
      {
        "name": "Url",
        "desc": "New forwarding path of the forwarding rule. This parameter is not required if the URL does not need to be modified"
      },
      {
        "name": "HealthCheck",
        "desc": "Health check information"
      },
      {
        "name": "Scheduler",
        "desc": "Request forwarding method of the rule. Value range: WRR, LEAST_CONN, IP_HASH\nThey represent weighted round robin, least connections, and IP hash, respectively. Default value: WRR."
      },
      {
        "name": "SessionExpireTime",
        "desc": "Session persistence time"
      },
      {
        "name": "ForwardType",
        "desc": "Forwarding protocol between CLB instance and real server. Default value: HTTP. Valid values: HTTP, HTTPS, TRPC."
      },
      {
        "name": "TrpcCallee",
        "desc": "TRPC callee server route, which is required when `ForwardType` is `TRPC`."
      },
      {
        "name": "TrpcFunc",
        "desc": "TRPC calling service API, which is required when `ForwardType` is `TRPC`."
      }
    ],
    "desc": "This API (ModifyRule) is used to modify the attributes of a forwarding rule under a layer-7 CLB listener, such as forwarding path, health check attribute, and forwarding policy.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "DeleteRule": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "LocationIds",
        "desc": "Array of IDs of the forwarding rules to be deleted"
      },
      {
        "name": "Domain",
        "desc": "Domain name of the forwarding rule to be deleted. This parameter does not take effect if LocationIds is specified"
      },
      {
        "name": "Url",
        "desc": "Forwarding path of the forwarding rule to be deleted. This parameter does not take effect if LocationIds is specified"
      },
      {
        "name": "NewDefaultServerDomain",
        "desc": "A listener must be configured with a default domain name. If you need to delete the default domain name, you can specify another one as the new default domain name."
      }
    ],
    "desc": "This API (DeleteRule) is used to delete a forwarding rule under a layer-7 CLB instance listener\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "SetLoadBalancerClsLog": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "LogSetId",
        "desc": "CLS logset ID"
      },
      {
        "name": "LogTopicId",
        "desc": "CLS log topic ID"
      }
    ],
    "desc": "This API is used to add, delete, and update the CLS topic of a CLB instance."
  },
  "DescribeTargetGroupList": {
    "params": [
      {
        "name": "TargetGroupIds",
        "desc": "Target group ID array"
      },
      {
        "name": "Filters",
        "desc": "Filter array, which is exclusive of `TargetGroupIds`. Valid values: TargetGroupVpcId, TargetGroupName. Target group ID will be used first."
      },
      {
        "name": "Offset",
        "desc": "Starting display offset"
      },
      {
        "name": "Limit",
        "desc": "Limit of the number of displayed results. Default value: 20"
      }
    ],
    "desc": "This API is used to get the target group list."
  },
  "ModifyBlockIPList": {
    "params": [
      {
        "name": "LoadBalancerIds",
        "desc": "CLB instance ID"
      },
      {
        "name": "Type",
        "desc": "Operation type. Valid values:\n<li> add_customized_field (sets header initially to enable the blocklist feature)</li>\n<li> set_customized_field (modifies header)</li>\n<li> del_customized_field (deletes header)</li>\n<li> add_blocked (adds IPs to blocklist)</li>\n<li> del_blocked (deletes IPs from blocklist)</li>\n<li> flush_blocked (clears blocklist)</li>"
      },
      {
        "name": "ClientIPField",
        "desc": "Header field that stores real client IPs"
      },
      {
        "name": "BlockIPList",
        "desc": "List of blocked IPs. The array can contain up to 200,000 entries in one operation."
      },
      {
        "name": "ExpireTime",
        "desc": "Expiration time in seconds. Default value: 3600"
      },
      {
        "name": "AddStrategy",
        "desc": "IP adding policy. Valid value: fifo (if a blocklist is full, new IPs added to the blocklist will adopt the first-in first-out policy)"
      }
    ],
    "desc": "This API is used to modify the client IP blocklist of a CLB instance. One forwarding rule supports blocking up to 2,000,000 IPs. One blocklist can contain up to 2,000,000 entries.\n(This API is in beta test. To use it, please submit a ticket.)"
  },
  "CreateTargetGroup": {
    "params": [
      {
        "name": "TargetGroupName",
        "desc": "Target group name (up to 50 characters)"
      },
      {
        "name": "VpcId",
        "desc": "`vpcid` attribute of a target group. If this parameter is left empty, the default VPC will be used."
      },
      {
        "name": "Port",
        "desc": "Default port of a target group, which can be used for subsequently added servers."
      },
      {
        "name": "TargetGroupInstances",
        "desc": "Real server bound to a target group"
      }
    ],
    "desc": "This API is used to create a target group. This feature is in beta test, if you want to try it out, please [submit a ticket](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1)."
  },
  "DescribeTargetGroupInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter. Currently, only filtering by `TargetGroupId`, `BindIP`, or `InstanceId` is supported."
      },
      {
        "name": "Limit",
        "desc": "Number of displayed results. Default value: 20"
      },
      {
        "name": "Offset",
        "desc": "Display offset. Default value: 0"
      }
    ],
    "desc": "This API is used to get the information of servers bound to a target group."
  },
  "DescribeTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerIds",
        "desc": "List of listener IDs"
      },
      {
        "name": "Protocol",
        "desc": "Listener protocol type"
      },
      {
        "name": "Port",
        "desc": "Listener port"
      }
    ],
    "desc": "This API (DescribeTargets) is used to query the list of real servers bound to some listeners of a CLB instance."
  },
  "DescribeRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "SourceListenerIds",
        "desc": "Array of CLB listener IDs"
      },
      {
        "name": "SourceLocationIds",
        "desc": "Array of CLB forwarding rules"
      }
    ],
    "desc": "This API (DescribeRewrite) is used to query the redirection relationship between the forwarding rules of a CLB instance by instance ID. If no listener ID or forwarding rule ID is specified, all redirection relationships in the instance will be returned."
  },
  "RegisterTargetsWithClassicalLB": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "Targets",
        "desc": "Real server information"
      }
    ],
    "desc": "This API (RegisterTargetsWithClassicalLB) is used to bind real servers to a classic CLB.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful."
  },
  "ModifyTargetPort": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "Targets",
        "desc": "List of real servers for which to modify the ports"
      },
      {
        "name": "NewPort",
        "desc": "New port of the real server bound to a listener or forwarding rule"
      },
      {
        "name": "LocationId",
        "desc": "Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url"
      },
      {
        "name": "Domain",
        "desc": "Target rule domain name. This parameter does not take effect if LocationId is specified"
      },
      {
        "name": "Url",
        "desc": "Target rule URL. This parameter does not take effect if LocationId is specified"
      }
    ],
    "desc": "This API (ModifyTargetPort) is used to modify the port of a real server bound to a listener.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "ModifyTargetGroupAttribute": {
    "params": [
      {
        "name": "TargetGroupId",
        "desc": "Target group ID"
      },
      {
        "name": "TargetGroupName",
        "desc": "New name of target group"
      },
      {
        "name": "Port",
        "desc": "New default port of target group"
      }
    ],
    "desc": "This API is used to rename a target group or modify its default port attribute."
  },
  "DescribeClassicalLBHealthStatus": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      }
    ],
    "desc": "This API (DescribeClassicalLBHealthStatus) is used to get the real server health status of a classic CLB"
  },
  "DeregisterTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID in the format of lb-12345678"
      },
      {
        "name": "ListenerId",
        "desc": "Listener ID in the format of lbl-12345678"
      },
      {
        "name": "Targets",
        "desc": "List of real servers to be unbound. Array length limit: 20"
      },
      {
        "name": "LocationId",
        "desc": "Forwarding rule ID in the format of loc-12345678. When unbinding a server from a layer-7 forwarding rule, you must provide either this parameter or Domain+Url"
      },
      {
        "name": "Domain",
        "desc": "Target rule domain name. This parameter does not take effect if LocationId is specified"
      },
      {
        "name": "Url",
        "desc": "Target rule URL. This parameter does not take effect if LocationId is specified"
      }
    ],
    "desc": "This API (DeregisterTargets) is used to unbind one or more real servers from a CLB listener or forwarding rule. For layer-4 listeners, only the listener ID needs to be specified. For layer-7 listeners, the forwarding rule also needs to be specified through LocationId or Domain+Url.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "ModifyLoadBalancerAttributes": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "Unique CLB ID"
      },
      {
        "name": "LoadBalancerName",
        "desc": "CLB instance name"
      },
      {
        "name": "TargetRegionInfo",
        "desc": "Region information of the real server bound to a CLB."
      },
      {
        "name": "InternetChargeInfo",
        "desc": "Network billing parameter"
      },
      {
        "name": "LoadBalancerPassToTarget",
        "desc": "Whether the target opens traffic from CLB to the internet. If yes (true), only security groups on CLB will be verified; if no (false), security groups on both CLB and backend instance need to be verified."
      },
      {
        "name": "SnatPro",
        "desc": "Whether to enable SnatPro"
      }
    ],
    "desc": "This API is used to modify the attributes of a CLB instance such as name and cross-region attributes."
  },
  "CreateClsLogSet": {
    "params": [
      {
        "name": "Period",
        "desc": "Logset retention period in days; max value: 90"
      },
      {
        "name": "LogsetName",
        "desc": "Logset name, which must be unique among all CLS logsets; default value: clb_logset"
      }
    ],
    "desc": "This API is used to create a CLB exclusive logset for storing CLB logs."
  },
  "DescribeClassicalLBByInstanceId": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "List of real server IDs."
      }
    ],
    "desc": "This API (DescribeClassicalLBByInstanceId) is used to get the list of classic CLB IDs through the real server instance ID."
  },
  "ReplaceCertForLoadBalancers": {
    "params": [
      {
        "name": "OldCertificateId",
        "desc": "ID of the certificate to be replaced, which can be a server certificate or a client certificate."
      },
      {
        "name": "Certificate",
        "desc": "Information such as the content of the new certificate"
      }
    ],
    "desc": "This API (ReplaceCertForLoadBalancers) is used to replace the certificate associated with a CLB instance. A new certificates can be associated with a CLB only after the original certificate is disassociated from it.\nThis API supports replacing server certificates and client certificates.\nThe new certificate to be used can be specified by passing in the certificate ID. If no certificate ID is specified, relevant information such as certificate content must be passed in to create a new certificate and bind it to the CLB.\nNote: This API can only be called in the Guangzhou region; for other regions, an error will occur due to domain name resolution problems."
  },
  "ModifyTargetGroupInstancesPort": {
    "params": [
      {
        "name": "TargetGroupId",
        "desc": "Target group ID"
      },
      {
        "name": "TargetGroupInstances",
        "desc": "Array of servers for which to modify port"
      }
    ],
    "desc": "This API is used to modify server ports of a target group in batches.\nThis is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful."
  },
  "BatchModifyTargetWeight": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ModifyList",
        "desc": "List of weights to be modified in batches"
      }
    ],
    "desc": "This API is used to modify the forwarding weights of real servers bound to a CLB listener in batches. It supports layer-4 and layer-7 CLB listeners but not Classic CLB.\nThis is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful."
  },
  "DescribeTargetHealth": {
    "params": [
      {
        "name": "LoadBalancerIds",
        "desc": "List of IDs of CLB instances to be queried"
      }
    ],
    "desc": "This API (DescribeTargetHealth) is used to query the health check result of a real server of a CLB instance."
  },
  "ModifyTargetGroupInstancesWeight": {
    "params": [
      {
        "name": "TargetGroupId",
        "desc": "Target group ID"
      },
      {
        "name": "TargetGroupInstances",
        "desc": "Array of servers for which to modify weight"
      }
    ],
    "desc": "This API is used to modify server weights of a target group in batches.\nThis is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful."
  },
  "ManualRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "SourceListenerId",
        "desc": "Source listener ID"
      },
      {
        "name": "TargetListenerId",
        "desc": "Target listener ID"
      },
      {
        "name": "RewriteInfos",
        "desc": "Redirection relationship between forwarding rules"
      }
    ],
    "desc": "After the original access address and the address to be redirected are configured manually, the system will automatically redirect requests made to the original access address to the target address of the corresponding path. Multiple paths can be configured as a redirection policy under one domain name to achieve automatic redirection between HTTP and HTTPS. A redirection policy should meet the following rules: if A has already been redirected to B, then it cannot be redirected to C (unless the original redirection relationship is deleted and a new one is created), and B cannot be redirected to any other addresses."
  }
}