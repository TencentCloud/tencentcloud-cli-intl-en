# -*- coding: utf-8 -*-
DESC = "dayu-2018-07-09"
INFO = {
  "ModifyCCIpAllowDeny": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Method",
        "desc": "add: add, delete: delete"
      },
      {
        "name": "Type",
        "desc": "Blocklist/allowlist type. Valid values: [white (allowlist), black (blocklist)]"
      },
      {
        "name": "IpList",
        "desc": "Blocklisted/whitelisted IP array"
      },
      {
        "name": "Protocol",
        "desc": "CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `Domain` and `RuleId` fields are required;"
      },
      {
        "name": "Domain",
        "desc": "HTTPS layer-7 forwarding rule domain name (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only if `Protocol` is `https`;"
      },
      {
        "name": "RuleId",
        "desc": "HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API),\nIf `Method` is `delete`, this field can be left empty;"
      }
    ],
    "desc": "This API is used to add/remove a CC IP to/from the blocklist/allowlist."
  },
  "DescribeDDoSCount": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Ip",
        "desc": "Resource IP"
      },
      {
        "name": "StartTime",
        "desc": "Statistics start time"
      },
      {
        "name": "EndTime",
        "desc": "Statistics end time"
      },
      {
        "name": "MetricName",
        "desc": "Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]"
      }
    ],
    "desc": "This API is used to get the DDoS attack proportion analysis."
  },
  "DescribeRuleSets": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "IdList",
        "desc": "Resource ID list"
      }
    ],
    "desc": "This API is used to get the number of rules of a resource."
  },
  "CreateNewL7RulesUpload": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)."
      },
      {
        "name": "IdList",
        "desc": "Resource ID list."
      },
      {
        "name": "VipList",
        "desc": "Resource IP address list."
      },
      {
        "name": "Rules",
        "desc": "Rule list."
      }
    ],
    "desc": "This API is used to batch upload Layer-7 forwarding rules."
  },
  "CreateL7CCRule": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Method",
        "desc": "Operation. Valid values: [query (query), add (add), del (delete)]"
      },
      {
        "name": "RuleId",
        "desc": "Layer-7 forwarding rule ID, such as rule-0000001"
      },
      {
        "name": "RuleConfig",
        "desc": "Custom layer-7 CC protection rule. If the `Method` is `query`, this field can be left empty; if the `Method` is `add` or `del`, it is required, and the array length can only be 1;"
      }
    ],
    "desc": "This API is used to add a custom frequency control rule for layer-7 CC access (it works in the IP + Host dimension and does not support specific URIs). As it has been disused, please call the new `CreateCCFrequencyRules` API, which supports both IP + Host and URI."
  },
  "CreateCCSelfDefinePolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Policy",
        "desc": "Details of the CC protection policy"
      }
    ],
    "desc": "This API is used to create a custom CC policy."
  },
  "DescribleL7Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "RuleIdList",
        "desc": "Rule ID, which is optional. If this field is entered, the specified rule will be obtained"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. A value of 0 means no pagination"
      },
      {
        "name": "Offset",
        "desc": "Page start offset, whose value is (page number - 1) * number of entries per page"
      },
      {
        "name": "Domain",
        "desc": "Domain name search, which is optional. Enter it if you need to search for domain names"
      },
      {
        "name": "ProtocolList",
        "desc": "Forwarding protocol search, which is optional. Valid values: [http, https, http/https]"
      },
      {
        "name": "StatusList",
        "desc": "Status search, which is optional. Valid values: [0 (successfully configured rule), 1 (rule configuration taking effect), 2 (rule configuration failed), 3 (rule deletion taking effect), 5 (rule deletion failed), 6 (rule waiting for configuration), 7 (rule waiting for deletion), 8 (rule waiting for certificate configuration)]"
      }
    ],
    "desc": "This API is used to get a layer-7 forwarding rule."
  },
  "ModifyCCPolicySwitch": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "SetId",
        "desc": "Policy ID"
      },
      {
        "name": "Switch",
        "desc": "Status"
      }
    ],
    "desc": "This API is used to enable or disable a custom CC policy."
  },
  "CreateDDoSPolicyCase": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "CaseName",
        "desc": "Policy scenario name string. Length limit: 64"
      },
      {
        "name": "PlatformTypes",
        "desc": "Development platform. Valid values: [PC (PC client), MOBILE (mobile device), TV (TV), SERVER (server)]"
      },
      {
        "name": "AppType",
        "desc": "Category. Valid values: [WEB (website), GAME (game), APP (application), OTHER (other)]"
      },
      {
        "name": "AppProtocols",
        "desc": "Application protocol. Valid values: [tcp (TCP protocol), udp (UDP protocol), icmp (ICMP protocol), all (other protocols)]"
      },
      {
        "name": "TcpSportStart",
        "desc": "TCP start port. Value range: (0, 65535]"
      },
      {
        "name": "TcpSportEnd",
        "desc": "TCP end port. Value range: (0, 65535). It must be greater than or equal to the TCP start port."
      },
      {
        "name": "UdpSportStart",
        "desc": "UDP start port. Value range: (0, 65535]"
      },
      {
        "name": "UdpSportEnd",
        "desc": "UDP end port. Value range: (0, 65535). It must be greater than or equal to the UDP start port."
      },
      {
        "name": "HasAbroad",
        "desc": "Whether there are customers outside China. Valid values: [no, yes]"
      },
      {
        "name": "HasInitiateTcp",
        "desc": "Whether to actively initiate outbound TCP requests. Valid values: [no, yes]"
      },
      {
        "name": "HasInitiateUdp",
        "desc": "Whether to actively initiate outbound UDP requests. Valid values: [no, yes]"
      },
      {
        "name": "PeerTcpPort",
        "desc": "Port that actively initiates TCP requests. Value range: (0, 65535]"
      },
      {
        "name": "PeerUdpPort",
        "desc": "Port that actively initiates UDP requests. Value range: (0, 65535]"
      },
      {
        "name": "TcpFootprint",
        "desc": "Fixed feature code of TCP payload. Max string length: 512"
      },
      {
        "name": "UdpFootprint",
        "desc": "Fixed feature code of UDP payload. Max string length: 512"
      },
      {
        "name": "WebApiUrl",
        "desc": "Web application API URL"
      },
      {
        "name": "MinTcpPackageLen",
        "desc": "Minimum length of TCP packet. Value range: (0, 1500)"
      },
      {
        "name": "MaxTcpPackageLen",
        "desc": "Maximum length of TCP packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of TCP packet"
      },
      {
        "name": "MinUdpPackageLen",
        "desc": "Minimum length of UDP packet. Value range: (0, 1500)"
      },
      {
        "name": "MaxUdpPackageLen",
        "desc": "Maximum length of UDP packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of UDP packet"
      },
      {
        "name": "HasVPN",
        "desc": "Whether there are applications using VPN. Valid values: [no, yes]"
      },
      {
        "name": "TcpPortList",
        "desc": "TCP port list. You can enter a single port, or a port range. Format: 80,443,700-800,53,1000-3000."
      },
      {
        "name": "UdpPortList",
        "desc": "UDP port list. You can enter a single port, or a port range. Format: 80,443,700-800,53,1000-3000."
      }
    ],
    "desc": "This API is used to add a policy scenario."
  },
  "DescribeDDoSNetTrend": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "MetricName",
        "desc": "Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]"
      },
      {
        "name": "Period",
        "desc": "Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]"
      },
      {
        "name": "StartTime",
        "desc": "Statistics start time"
      },
      {
        "name": "EndTime",
        "desc": "Statistics end time"
      }
    ],
    "desc": "This API is used to get the DDoS attack metric data of an Anti-DDoS Ultimate resource."
  },
  "ModifyDDoSPolicyName": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "Name",
        "desc": "Policy name"
      }
    ],
    "desc": "This API is used to rename an advanced DDoS policy."
  },
  "ModifyL4Health": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Healths",
        "desc": "Health check parameter array"
      }
    ],
    "desc": "This API is used to modify the health check parameters of a layer-4 forwarding rule. It is supported for Anti-DDoS Advanced and Anti-DDoS Ultimate."
  },
  "DescribeDDoSUsedStatis": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)"
      }
    ],
    "desc": "This API is used to count the number of days of Anti-DDoS resource use and number of DDoS attacks defended against."
  },
  "DescribeDDoSDefendStatus": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `basic`: Anti-DDoS Basic, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Instance ID, which is required only if `Business` is not `basic`."
      },
      {
        "name": "Ip",
        "desc": "Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;"
      },
      {
        "name": "BizType",
        "desc": "Type of products bound to the anti-DDoS instance, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (Bare metal products), eni (elastic network interface), vpngw (VPN Gateway), natgw (NAT Gateway), waf (Web Application Firewall), fpc (Finance products), gaap (GAAP), other (hosted IP)]"
      },
      {
        "name": "DeviceType",
        "desc": "Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]"
      },
      {
        "name": "InstanceId",
        "desc": "Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;"
      },
      {
        "name": "IPRegion",
        "desc": "This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:\n\"bj\":     North China (Beijing)\n\"cd\":     Southwest China (Chengdu)\n\"cq\":     Southwest China (Chongqing)\n\"gz\":     South China (Guangzhou)\n\"gzopen\": South China (Guangzhou Open)\n\"hk\":     Hong Kong (China)\n\"kr\":     Southeast Asia (Seoul)\n\"sh\":     East China (Shanghai)\n\"shjr\":   East China (Shanghai Finance)\n\"szjr\":   South China (Shenzhen Finance)\n\"sg\":     Southeast Asia (Singapore)\n\"th\":     Southeast Asia (Thailand)\n\"de\":     Europe (Germany)\n\"usw\":    West US (Silicon Valley)\n\"ca\":     North America (Toronto)\n\"jp\":     Japan\n\"hzec\":   Hangzhou\n\"in\":     India\n\"use\":    East US (Virginia)\n\"ru\":     Russia\n\"tpe\":    Taiwan (China)\n\"nj\":     Nanjing"
      }
    ],
    "desc": "This API is used to get the DDoS protection status (temporarily disabled status). It is supported for Anti-DDoS Basic, single IP instance, multi-IP instance, Anti-DDoS Advanced, and Anti-DDoS Ultimate. It is used to query whether DDoS protection is temporarily disabled, and if yes, return parameters such as temporary disablement duration."
  },
  "DescribeCCAlarmThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "RsId",
        "desc": "Anti-DDoS instance ID"
      }
    ],
    "desc": "This API is used to get the alarm notification threshold set for CC attacks in Anti-DDoS Pro, Anti-DDoS Advanced, Anti-DDoS Ultimate, and Chess Shield."
  },
  "DescribePcap": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "StartTime",
        "desc": "Attack event start time in the format of \"2018-08-28 07:00:00\""
      },
      {
        "name": "EndTime",
        "desc": "Attack event end time in the format of \"2018-08-28 07:02:00\""
      },
      {
        "name": "Ip",
        "desc": "Resource IP, which is required only if `Business` is `net`;"
      }
    ],
    "desc": "This API is used to download the PCAP packet of an attack event."
  },
  "ModifyElasticLimit": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Limit",
        "desc": "Elastic protection threshold. Valid values: [0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 120000 150000 200000 250000 300000 400000 600000 800000 220000 310000 110000 270000 610000]"
      }
    ],
    "desc": "This API is used to modify the elastic protection threshold."
  },
  "DescribeDDoSNetIpLog": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "StartTime",
        "desc": "Attack start time"
      },
      {
        "name": "EndTime",
        "desc": "Attack end time"
      }
    ],
    "desc": "This API is used to get the DDoS IP attack logs of an Anti-DDoS Ultimate resource."
  },
  "ModifyCCAlarmThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "RsId",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "AlarmThreshold",
        "desc": "Alarm threshold, which should be greater than 0 (currently scheduled value). It is set to 1000 on the backend by default"
      },
      {
        "name": "IpList",
        "desc": "List of IPs associated with resource. If no Anti-DDoS Pro instance is bound, pass in an empty array. For Anti-DDoS Ultimate, pass in multiple IPs"
      }
    ],
    "desc": "This API is used to set the alarm notification threshold for CC attacks in Anti-DDoS Pro, Anti-DDoS Advanced, Anti-DDoS Ultimate, and Chess Shield."
  },
  "DescribeDDoSEvList": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic"
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
        "name": "Id",
        "desc": "Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)"
      },
      {
        "name": "IpList",
        "desc": "Resource IP"
      },
      {
        "name": "OverLoad",
        "desc": "Whether the elastic protection bandwidth is exceeded. Valid values: [yes, no]. If an empty string is entered, it means no filtering"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. A value of 0 means no pagination"
      },
      {
        "name": "Offset",
        "desc": "Page start offset, whose value is (page number - 1) * number of entries per page"
      }
    ],
    "desc": "This API is used to get the DDoS attack event list."
  },
  "DescribeIpBlockList": {
    "params": [],
    "desc": "This API is used to get the blocked IP list."
  },
  "DescribeL4HealthConfig": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "RuleIdList",
        "desc": "Rule ID array. To export the health check configurations of all rules, leave this field empty or enter an empty array;"
      }
    ],
    "desc": "This API is used to export the layer-4 health check configuration."
  },
  "DescribeSecIndex": {
    "params": [],
    "desc": "This API is used to get the security statistics of the current month."
  },
  "DescribeSchedulingDomainList": {
    "params": [
      {
        "name": "Limit",
        "desc": "Number of items in a page. Returned results are not paged if you enter '0'."
      },
      {
        "name": "Offset",
        "desc": "Starting offset of the page. Value: (number of pages - 1) * items per page"
      },
      {
        "name": "Domain",
        "desc": "(Optional) Filter by specific domain name"
      }
    ],
    "desc": "Get scheduling domain name list"
  },
  "DescribeCCFrequencyRules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "RuleId",
        "desc": "Layer-7 forwarding rule ID (which can be obtained from the layer-7 forwarding rule API). If a value is entered, it means to get the access frequency control rule of the forwarding rule;"
      }
    ],
    "desc": "This API is used to get an access frequency control rule for CC protection."
  },
  "DeleteDDoSPolicyCase": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "SceneId",
        "desc": "Policy scenario ID"
      }
    ],
    "desc": "This API is used to delete a policy scenario."
  },
  "DeleteL7Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "RuleIdList",
        "desc": "Rule ID list"
      }
    ],
    "desc": "This API is used to delete one or more layer-7 forwarding rules."
  },
  "CreateL4Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Rules",
        "desc": "Rule list"
      }
    ],
    "desc": "This API is used to add a layer-4 forwarding rule."
  },
  "DescribeBaradData": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "MetricName",
        "desc": "Metric name. Valid values:\nconnum: number of active TCP connections;\nnew_conn: number of new TCP connections;\ninactive_conn: number of inactive connections;\nintraffic: inbound traffic;\nouttraffic: outbound traffic;\nalltraffic: sum of inbound and outbound traffic;\ninpkg: inbound packet rate;\noutpkg: outbound packet rate;"
      },
      {
        "name": "Period",
        "desc": "Statistical time granularity in seconds (300: 5-minute, 3600: hourly, 86400: daily)"
      },
      {
        "name": "StartTime",
        "desc": "Statistics start time. The second part is kept at 0, and the minute part is a multiple of 5"
      },
      {
        "name": "EndTime",
        "desc": "Statistics end time. The second part is kept at 0, and the minute part is a multiple of 5"
      },
      {
        "name": "Statistics",
        "desc": "Statistical method. Valid values:\nmax: maximum value;\nmin: minimum value;\navg: average;"
      },
      {
        "name": "ProtocolPort",
        "desc": "Protocol port array"
      },
      {
        "name": "Ip",
        "desc": "Resource instance IP, which is required only if `Business` is `net` (Anti-DDoS Ultimate), because an Anti-DDoS Ultimate instance has multiple IPs;"
      }
    ],
    "desc": "This API is used to provide business forwarding metric data of Anti-DDoS services."
  },
  "ModifyCCFrequencyRules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "CCFrequencyRuleId",
        "desc": "CC access frequency control rule ID"
      },
      {
        "name": "Mode",
        "desc": "Matching rule. Valid values: [\"include\" (prefix match), \"equal\" (exact match)]"
      },
      {
        "name": "Period",
        "desc": "Reference period in seconds. Valid values: [10, 30, 60]"
      },
      {
        "name": "ReqNumber",
        "desc": "Number of access requests. Value range: [1-10000]"
      },
      {
        "name": "Act",
        "desc": "Action take. Valid values: [\"alg\" (CAPTCHA), \"drop\" (blocking)]"
      },
      {
        "name": "ExeDuration",
        "desc": "Execution duration in seconds. Valid range: [1-900]"
      },
      {
        "name": "Uri",
        "desc": "URI string, which must start with `/`, such as `/abc/a.php`. Length limit: 31. If URI is `/`, only prefix match can be selected as the matching mode;"
      },
      {
        "name": "UserAgent",
        "desc": "`User-Agent` string. Length limit: 80"
      },
      {
        "name": "Cookie",
        "desc": "Cookie string. Length limit: 40"
      }
    ],
    "desc": "This API is used to modify an access frequency control rule for CC protection."
  },
  "CreateDDoSPolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "DropOptions",
        "desc": "Protocol disablement, which must be entered, and the array length must be 1"
      },
      {
        "name": "Name",
        "desc": "Policy name"
      },
      {
        "name": "PortLimits",
        "desc": "Ports to be closed. If no ports are to be closed, enter an empty array"
      },
      {
        "name": "IpAllowDenys",
        "desc": "IP blocklist/allowlist. Enter an empty array if there is no IP blocklist/allowlist"
      },
      {
        "name": "PacketFilters",
        "desc": "Packet filter. Enter an empty array if there are no packets to filter"
      },
      {
        "name": "WaterPrint",
        "desc": "Watermarking policy parameters. Enter an empty array if the watermarking feature is not enabled. Only one watermarking policy can be passed in (that is, the size of the array cannot exceed 1)"
      }
    ],
    "desc": "This API is used to add an advanced DDoS policy."
  },
  "ModifyResBindDDoSPolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "Method",
        "desc": "bind: bind policy; unbind: unbind policy"
      }
    ],
    "desc": "This API is used to bind an advanced DDoS policy to an instance."
  },
  "ModifyNetReturnSwitch": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Status",
        "desc": "Switch status. 0: disabled, 1: enabled"
      },
      {
        "name": "Hour",
        "desc": "Switch duration in hours. Valid values: [0,1,2,3,4,5,6;]. If `status` is 1, this field is required and must be greater than 0"
      }
    ],
    "desc": "This API is used to switch a client to the real server and set the switch duration when the client is under attack or blocked."
  },
  "DescribeSourceIpSegment": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      }
    ],
    "desc": "This API is used to get the intermediate IP range. It is supported for Anti-DDoS Advanced and Anti-DDoS Ultimate."
  },
  "ModifyCCUrlAllow": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Method",
        "desc": "add: add, delete: delete"
      },
      {
        "name": "Type",
        "desc": "Blocklist/allowlist type. Valid value: [white (allowlist)]"
      },
      {
        "name": "UrlList",
        "desc": "URL array. URL format:\nhttp://domain name/cgi\nhttps://domain name/cgi"
      },
      {
        "name": "Protocol",
        "desc": "CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `Domain` and `RuleId` fields are required;"
      },
      {
        "name": "Domain",
        "desc": "HTTPS layer-7 forwarding rule domain name (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only if `Protocol` is `https`;"
      },
      {
        "name": "RuleId",
        "desc": "HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only when adding a rule and `Protocol` is `https`;\nIf `Method` is `delete`, this field can be left empty;"
      }
    ],
    "desc": "This API is used to add/remove a CC URL to/from the allowlist."
  },
  "DescribeBasicDeviceThreshold": {
    "params": [
      {
        "name": "BasicIp",
        "desc": "Queried IP address, such as 1.1.1.1"
      },
      {
        "name": "BasicRegion",
        "desc": "IP region. Valid values: region abbreviations such as gz, bj, sh, and hk"
      },
      {
        "name": "BasicBizType",
        "desc": "Zone type. Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel)."
      },
      {
        "name": "BasicDeviceType",
        "desc": "Device type. Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel)."
      },
      {
        "name": "BasicCheckFlag",
        "desc": "Validity check. Valid value: 1"
      },
      {
        "name": "BasicIpInstance",
        "desc": "IPInstance Nat gateway, which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)"
      },
      {
        "name": "BasicIspCode",
        "desc": "ISP line, which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)"
      }
    ],
    "desc": "This API is used to get the blackhole threshold of Anti-DDoS Basic."
  },
  "CreateUnblockIp": {
    "params": [
      {
        "name": "Ip",
        "desc": "IP"
      },
      {
        "name": "ActionType",
        "desc": "Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)"
      }
    ],
    "desc": "This API is used to unblock an IP."
  },
  "ModifyNewL4Rule": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)."
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID."
      },
      {
        "name": "Rule",
        "desc": "Forwarding rule."
      }
    ],
    "desc": "This API is used to modify layer-4 forwarding rules."
  },
  "DeleteDDoSPolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      }
    ],
    "desc": "This API is used to delete an advanced DDoS protection policy."
  },
  "DescribeDDoSNetCount": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "StartTime",
        "desc": "Statistics start time"
      },
      {
        "name": "EndTime",
        "desc": "Statistics end time"
      },
      {
        "name": "MetricName",
        "desc": "Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]"
      }
    ],
    "desc": "This API is used to get the DDoS attack proportion analysis for an Anti-DDoS Ultimate resource."
  },
  "DeleteCCSelfDefinePolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "SetId",
        "desc": "Policy ID"
      }
    ],
    "desc": "This API is used to delete a custom CC policy."
  },
  "DescribePolicyCase": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "SceneId",
        "desc": "Policy scenario ID"
      }
    ],
    "desc": "This API is used to get the policy scenario."
  },
  "DescribeActionLog": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start time"
      },
      {
        "name": "EndTime",
        "desc": "End time"
      },
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Filter",
        "desc": "Search value, which can only be resource ID or user `UIN`"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. A value of 0 means no pagination"
      },
      {
        "name": "Offset",
        "desc": "Page start offset, whose value is (page number - 1) * number of entries per page"
      }
    ],
    "desc": "This API is used to get operation logs."
  },
  "ModifyL4Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Rule",
        "desc": "Rule"
      }
    ],
    "desc": "This API is used to modify a layer-4 forwarding rule."
  },
  "DescribeDDoSIpLog": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Ip",
        "desc": "Resource IP"
      },
      {
        "name": "StartTime",
        "desc": "Attack start time"
      },
      {
        "name": "EndTime",
        "desc": "Attack end time"
      }
    ],
    "desc": "This API is used to get a DDoS IP attack log."
  },
  "DescribeDDoSAlarmThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "RsId",
        "desc": "Anti-DDoS instance ID"
      }
    ],
    "desc": "This API is used to get the alarm notification threshold set for DDoS attacks in Anti-DDoS Pro, Anti-DDoS Advanced, Anti-DDoS Ultimate, and Chess Shield."
  },
  "DescribePackIndex": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `net`: Anti-DDoS Ultimate"
      }
    ],
    "desc": "This API is used to get the product overview statistics. It is supported for Anti-DDoS Pro, Anti-DDoS Advanced, and Anti-DDoS Ultimate."
  },
  "CreateBasicDDoSAlarmThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`basic`: Anti-DDoS Basic)"
      },
      {
        "name": "Method",
        "desc": "`get`: read alarm threshold, `set`: set alarm threshold"
      },
      {
        "name": "AlarmType",
        "desc": "Alarm threshold type. 1: inbound traffic, 2: cleansed traffic. This field is required if `Method` is `set`;"
      },
      {
        "name": "AlarmThreshold",
        "desc": "Alarm threshold. It is required if `Method` is `set`. If it is set to 0, it means to clear the alarm threshold configuration;"
      }
    ],
    "desc": "This API is used to set the DDoS alarm threshold for Anti-DDoS Basic, which is only supported for Anti-DDoS Basic."
  },
  "ModifyDDoSThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Threshold",
        "desc": "DDoS cleansing threshold. Valid values: [0, 60, 80, 100, 150, 200, 250, 300, 400, 500, 700, 1000];\nIf the value is set to 0, the default value will be used;"
      }
    ],
    "desc": "This API is used to modify the DDoS cleansing threshold."
  },
  "CreateL7RuleCert": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "The resource instance ID, such as the ID of an Anti-DDoS Advanced instance or the ID of an Anti-DDoS Ultimate instance."
      },
      {
        "name": "RuleId",
        "desc": "Rule ID"
      },
      {
        "name": "CertType",
        "desc": "Certificate type, which is required if the protocol is HTTPS. Valid value: [2 (Tencent Cloud-hosted certificate)]"
      },
      {
        "name": "SSLId",
        "desc": "If the certificate is a Tencent Cloud-hosted certificate, this field must be entered with the hosted certificate ID."
      },
      {
        "name": "Cert",
        "desc": "[Disused] If the certificate is an external certificate, this field must be entered with the certificate content. "
      },
      {
        "name": "PrivateKey",
        "desc": "[Disused] If the certificate is an external certificate, this field must be entered with the certificate key. "
      }
    ],
    "desc": "This API is used to configure a certificate for a layer-7 forwarding rule."
  },
  "ModifyDDoSAIStatus": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Method",
        "desc": "get (read AI protection status), set (modify AI protection status);"
      },
      {
        "name": "DDoSAI",
        "desc": "AI protection status, which is required if `Method` is `set`. Valid values: [on, off]."
      }
    ],
    "desc": "This API is used to read or modify DDoS AI protection status."
  },
  "DescribeCCIpAllowDeny": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Type",
        "desc": "Blocklist or allowlist. Valid values: [white (allowlist), black (blocklist)]\nNote: this array can only have one value. It cannot get the blocklist and allowlist at the same time"
      },
      {
        "name": "Limit",
        "desc": "Pagination parameter"
      },
      {
        "name": "Offset",
        "desc": "Pagination parameter"
      },
      {
        "name": "Protocol",
        "desc": "HTTP or HTTPS CC protection, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)];"
      }
    ],
    "desc": "This API is used to get the CC IP blocklist/allowlist."
  },
  "CreateL4HealthConfig": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "HealthConfig",
        "desc": "Layer-4 health check configuration array"
      }
    ],
    "desc": "This API is used to upload layer-4 health check configuration."
  },
  "DescribeResourceList": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "RegionList",
        "desc": "Region code search, which is optional. If no regions are to be specified, enter an empty array. If a region is to be specified, enter a region code, such as [\"gz\", \"sh\"]"
      },
      {
        "name": "Line",
        "desc": "Line search. This field can be optionally entered only when getting the list of Anti-DDoS Advanced resources. Valid values: [1 (BGP line), 2 (Nanjing Telecom), 3 (Nanjing Unicom), 99 (third-party partner line)]. Please enter an empty array when getting other products;"
      },
      {
        "name": "IdList",
        "desc": "Resource ID search, which is optional. If this field is not an empty array, it means to get the resource list of a specified resource;"
      },
      {
        "name": "Name",
        "desc": "Resource name search, which is optional. If this field is not an empty string, it means to search for resources by name;"
      },
      {
        "name": "IpList",
        "desc": "IP search list, which is optional. If this field is not empty, it means to search for resources by IP;"
      },
      {
        "name": "Status",
        "desc": "Resource status search list, which is optional. Valid values: [0 (running), 1 (cleansing), 2 (blocking)]. No status search will be performed if an empty array is entered;"
      },
      {
        "name": "Expire",
        "desc": "Expiring resource search, which is optional. Valid values: [0 (no search), 1 (search for expiring resources)]"
      },
      {
        "name": "OderBy",
        "desc": "Sort by field, which is optional"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. A value of 0 means no pagination"
      },
      {
        "name": "Offset",
        "desc": "Page start offset, whose value is (page number - 1) * number of entries per page"
      },
      {
        "name": "CName",
        "desc": "CNAME of Anti-DDoS Ultimate resource, which is optional and only valid for the Anti-DDoS Ultimate resource list;"
      },
      {
        "name": "Domain",
        "desc": "Domain name of Anti-DDoS Ultimate resource, which is optional and only valid for the Anti-DDoS Ultimate resource list;"
      }
    ],
    "desc": "This API is used to get the resource list."
  },
  "CreateBoundIP": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "BoundDevList",
        "desc": "Array of IPs to be bound to the Anti-DDoS instance. For Anti-DDoS Pro Single IP instance, this array can contain only one IP. If there are no IPs to bind, it can be empty; however, either `BoundDevList` or `UnBoundDevList` must not be empty;"
      },
      {
        "name": "UnBoundDevList",
        "desc": "Array of IPs to be unbound from Anti-DDoS instance. For Anti-DDoS Pro Single IP instance, this array can contain only one IP; if there are no IPs to unbind, it can be empty; however, either `BoundDevList` or `UnBoundDevList` must not be empty;"
      },
      {
        "name": "CopyPolicy",
        "desc": "[Disused]"
      }
    ],
    "desc": "This API is used to bind an IP to an Anti-DDoS Pro instance, which supports both single IP instances and multi-IP instances. It should be noted that this API is async; therefore, if a binding/unbinding operation is in progress, new binding/unbinding operations cannot be initiated."
  },
  "ModifyDDoSPolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "DropOptions",
        "desc": "Protocol disablement, which must be entered, and the array length must be 1"
      },
      {
        "name": "PortLimits",
        "desc": "Port disablement. If no ports are to be disabled, enter an empty array"
      },
      {
        "name": "IpAllowDenys",
        "desc": "IP blocklist/allowlist. Enter an empty array if there is no IP blocklist/allowlist"
      },
      {
        "name": "PacketFilters",
        "desc": "Packet filter. Enter an empty array if there are no packets to filter"
      },
      {
        "name": "WaterPrint",
        "desc": "Watermarking policy parameter. Enter an empty array if the watermarking feature is not enabled. At most one watermarking policy can be passed in (that is, the size of the array cannot exceed 1)"
      }
    ],
    "desc": "This API is used to modify an advanced DDoS policy."
  },
  "ModifyDDoSPolicyCase": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "SceneId",
        "desc": "Policy scenario ID"
      },
      {
        "name": "PlatformTypes",
        "desc": "Development platform. Valid values: [PC (PC client), MOBILE (mobile device), TV (TV), SERVER (server)]"
      },
      {
        "name": "AppType",
        "desc": "Category. Valid values: [WEB (website), GAME (game), APP (application), OTHER (other)]"
      },
      {
        "name": "AppProtocols",
        "desc": "Application protocol. Valid values: [tcp (TCP protocol), udp (UDP protocol), icmp (ICMP protocol), all (other protocols)]"
      },
      {
        "name": "TcpSportStart",
        "desc": "TCP start port. Value range: (0, 65535]"
      },
      {
        "name": "TcpSportEnd",
        "desc": "TCP end port. Value range: (0, 65535). It must be greater than or equal to the TCP start port"
      },
      {
        "name": "UdpSportStart",
        "desc": "UDP start port. Value range: (0, 65535]"
      },
      {
        "name": "UdpSportEnd",
        "desc": "End UDP business port. Value range: (0, 65535). It must be greater than or equal to the start UDP business port"
      },
      {
        "name": "HasAbroad",
        "desc": "Whether there are customers outside Mainland China. Valid values: [no, yes]"
      },
      {
        "name": "HasInitiateTcp",
        "desc": "Whether to actively initiate outbound TCP requests. Valid values: [no, yes]"
      },
      {
        "name": "HasInitiateUdp",
        "desc": "Whether to actively initiate outbound UDP requests. Valid values: [no, yes]"
      },
      {
        "name": "PeerTcpPort",
        "desc": "Port that actively initiates TCP requests. Value range: (0, 65535]"
      },
      {
        "name": "PeerUdpPort",
        "desc": "Port that actively initiates UDP requests. Value range: (0, 65535]"
      },
      {
        "name": "TcpFootprint",
        "desc": "Fixed feature code of TCP payload. String length limit: 512"
      },
      {
        "name": "UdpFootprint",
        "desc": "Fixed feature code of UDP payload. String length limit: 512"
      },
      {
        "name": "WebApiUrl",
        "desc": "Web business API URL"
      },
      {
        "name": "MinTcpPackageLen",
        "desc": "Minimum length of TCP business packet. Value range: (0, 1500)"
      },
      {
        "name": "MaxTcpPackageLen",
        "desc": "Maximum length of TCP business packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of TCP business packet"
      },
      {
        "name": "MinUdpPackageLen",
        "desc": "Minimum length of UDP business packet. Value range: (0, 1500)"
      },
      {
        "name": "MaxUdpPackageLen",
        "desc": "Maximum length of UDP business packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of UDP business packet"
      },
      {
        "name": "HasVPN",
        "desc": "Whether there are VPN businesses. Valid values: [no, yes]"
      },
      {
        "name": "TcpPortList",
        "desc": "TCP business port list. Individual ports and port ranges are supported, which should be in string type, such as 80,443,700-800,53,1000-3000"
      },
      {
        "name": "UdpPortList",
        "desc": "UDP business port list. Individual ports and port ranges are supported, which should be in string type, such as 80,443,700-800,53,1000-3000"
      }
    ],
    "desc": "This API is used to modify a policy scenario."
  },
  "ModifyDDoSAlarmThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "RsId",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "AlarmType",
        "desc": "Alarm threshold type. 0: not set, 1: inbound traffic, 2: cleansed traffic"
      },
      {
        "name": "AlarmThreshold",
        "desc": "Alarm threshold, which should be greater than 0 (currently scheduled value)"
      },
      {
        "name": "IpList",
        "desc": "List of IPs associated with resource. If no Anti-DDoS Pro instance is bound, pass in an empty array. For Anti-DDoS Ultimate, pass in multiple IPs"
      }
    ],
    "desc": "This API is used to set the alarm notification threshold for DDoS attacks in Anti-DDoS Pro, Anti-DDoS Advanced, Anti-DDoS Ultimate, and Chess Shield."
  },
  "DescribeDDoSNetEvInfo": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "StartTime",
        "desc": "Attack start time"
      },
      {
        "name": "EndTime",
        "desc": "Attack end time"
      }
    ],
    "desc": "This API is used to get the DDoS attack event details of an Anti-DDoS Ultimate resource."
  },
  "DeleteCCFrequencyRules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "CCFrequencyRuleId",
        "desc": "Access frequency control rule ID for CC protection"
      }
    ],
    "desc": "This API is used to delete an access frequency control rule for CC protection."
  },
  "ModifyL4KeepTime": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "RuleId",
        "desc": "Rule ID"
      },
      {
        "name": "KeepEnable",
        "desc": "Session persistence status. Valid values: [0 (disabled), 1 (enabled)]"
      },
      {
        "name": "KeepTime",
        "desc": "Session persistence duration in seconds"
      }
    ],
    "desc": "This API is used to modify the session persistence of a layer-4 forwarding rule. It is supported for Anti-DDoS Advanced and Anti-DDoS Ultimate."
  },
  "DescribeL4RulesErrHealth": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      }
    ],
    "desc": "This API is used to get the exception result of a layer-4 forwarding rule health check."
  },
  "CreateL7RulesUpload": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Rules",
        "desc": "Rule list"
      }
    ],
    "desc": "This API is used to upload layer-7 forwarding rules in batches."
  },
  "DescribeDDoSAttackIPRegionMap": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "StartTime",
        "desc": "Statistics start time"
      },
      {
        "name": "EndTime",
        "desc": "Statistics end time. Maximum statistics time range: half a year;"
      },
      {
        "name": "IpList",
        "desc": "IP attack source of specified resource, which is optional"
      }
    ],
    "desc": "This API is used to get the geographical distribution map of DDoS attack source IPs. It supports display by global regions and Chinese provinces."
  },
  "DescribeTransmitStatis": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "MetricName",
        "desc": "Metric name. Valid values:\ntraffic: traffic bandwidth;\npkg: packet rate;"
      },
      {
        "name": "Period",
        "desc": "Statistical time granularity (300: 5-minute, 3600: hourly, 86400: daily)"
      },
      {
        "name": "StartTime",
        "desc": "Statistics start time. The second part is kept at 0, and the minute part is a multiple of 5"
      },
      {
        "name": "EndTime",
        "desc": "Statistics end time. The second part is kept at 0, and the minute part is a multiple of 5"
      },
      {
        "name": "IpList",
        "desc": "Resource IP, which is required and only supports one IP if `Business` is `bgp-multip`. If this field is left empty, all IPs of a resource instance will be counted by default. If the resource instance has multiple IPs (such as Anti-DDoS Ultimate), the statistical method is summation;"
      }
    ],
    "desc": "This API is used to get the business forwarding statistics, including forwarded traffic and packet forwarding rate."
  },
  "ModifyCCLevel": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Level",
        "desc": "CC protection level. Valid values: [default (normal), loose (loose), strict (strict)];"
      },
      {
        "name": "Protocol",
        "desc": "CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `RuleId` field is required;"
      },
      {
        "name": "RuleId",
        "desc": "Layer-7 forwarding rule ID (which can be obtained from the layer-7 forwarding rule API);"
      }
    ],
    "desc": "This API is used to modify CC protection level."
  },
  "ModifyDDoSDefendStatus": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `basic`: Anti-DDoS Basic"
      },
      {
        "name": "Status",
        "desc": "Protection status. Valid values: [0 (disabled), 1 (enabled)]"
      },
      {
        "name": "Hour",
        "desc": "Disablement duration in hours. Valid values: [0, 1, 2, 3, 4, 5, 6]. If `Status` is `0` (indicating to disable), `Hour` must be greater than 0;"
      },
      {
        "name": "Id",
        "desc": "Resource ID, which is required if `Business` is not Anti-DDoS Basic;"
      },
      {
        "name": "Ip",
        "desc": "Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;"
      },
      {
        "name": "BizType",
        "desc": "Product type of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (BM), eni (ENI), vpngw (VPN Gateway), natgw (NAT Gateway), waf (WAF), fpc (finance product), gaap (GAAP), other (hosted IP)]"
      },
      {
        "name": "DeviceType",
        "desc": "Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]"
      },
      {
        "name": "InstanceId",
        "desc": "Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;"
      },
      {
        "name": "IPRegion",
        "desc": "This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:\n\"bj\":     North China (Beijing)\n\"cd\":     Southwest China (Chengdu)\n\"cq\":     Southwest China (Chongqing)\n\"gz\":     South China (Guangzhou)\n\"gzopen\": South China (Guangzhou Open)\n\"hk\":     Hong Kong (China)\n\"kr\":     Southeast Asia (Seoul)\n\"sh\":     East China (Shanghai)\n\"shjr\":   East China (Shanghai Finance)\n\"szjr\":   South China (Shenzhen Finance)\n\"sg\":     Southeast Asia (Singapore)\n\"th\":     Southeast Asia (Thailand)\n\"de\":     Europe (Germany)\n\"usw\":    West US (Silicon Valley)\n\"ca\":     North America (Toronto)\n\"jp\":     Japan\n\"hzec\":   Hangzhou\n\"in\":     India\n\"use\":    East US (Virginia)\n\"ru\":     Russia\n\"tpe\":    Taiwan (China)\n\"nj\":     Nanjing"
      }
    ],
    "desc": "This API is used to enable or disable DDoS. It can disable DDoS protection for a period of time, which will be automatically enabled after the period of time elapses."
  },
  "DescribeUnBlockStatis": {
    "params": [],
    "desc": "This API is used to get the number of blackhole unblockings."
  },
  "DescribeDDoSTrend": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic"
      },
      {
        "name": "Ip",
        "desc": "Anti-DDoS instance IP"
      },
      {
        "name": "MetricName",
        "desc": "Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]"
      },
      {
        "name": "Period",
        "desc": "Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]"
      },
      {
        "name": "StartTime",
        "desc": "Statistics start time"
      },
      {
        "name": "EndTime",
        "desc": "Statistics end time"
      },
      {
        "name": "Id",
        "desc": "Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)"
      }
    ],
    "desc": "This API is used to get the data of DDoS attack traffic bandwidth and attack packet rate."
  },
  "CreateNetReturn": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      }
    ],
    "desc": "This API is used to switch to the real server in Anti-DDoS Ultimate."
  },
  "ModifyDDoSSwitch": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `basic`: Anti-DDoS Basic"
      },
      {
        "name": "Method",
        "desc": "`get`: read DDoS protection status, `set`: modify DDoS protection status"
      },
      {
        "name": "Ip",
        "desc": "Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;"
      },
      {
        "name": "BizType",
        "desc": "Product type of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (BM), eni (ENI), vpngw (VPN Gateway), natgw (NAT Gateway), waf (WAF), fpc (finance product), gaap (GAAP), other (hosted IP)]"
      },
      {
        "name": "DeviceType",
        "desc": "Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]"
      },
      {
        "name": "InstanceId",
        "desc": "Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;"
      },
      {
        "name": "IPRegion",
        "desc": "This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:\n\"bj\":     North China (Beijing)\n\"cd\":     Southwest China (Chengdu)\n\"cq\":     Southwest China (Chongqing)\n\"gz\":     South China (Guangzhou)\n\"gzopen\": South China (Guangzhou Open)\n\"hk\":     Hong Kong (China)\n\"kr\":     Southeast Asia (Seoul)\n\"sh\":     East China (Shanghai)\n\"shjr\":   East China (Shanghai Finance)\n\"szjr\":   South China (Shenzhen Finance)\n\"sg\":     Southeast Asia (Singapore)\n\"th\":     Southeast Asia (Thailand)\n\"de\":     Europe (Germany)\n\"usw\":    West US (Silicon Valley)\n\"ca\":     North America (Toronto)\n\"jp\":     Japan\n\"hzec\":   Hangzhou\n\"in\":     India\n\"use\":    East US (Virginia)\n\"ru\":     Russia\n\"tpe\":    Taiwan (China)\n\"nj\":     Nanjing"
      },
      {
        "name": "Status",
        "desc": "Protection status value, which is optional. Valid values: [0 (disabled), 1 (enabled)]. If `Method` is `get`, this field can be left empty;"
      }
    ],
    "desc": "This API is used to enable or disable DDoS protection, which is only supported for Anti-DDoS Basic."
  },
  "ModifyDDoSLevel": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Method",
        "desc": "get (read protection level), set (modify protection level);"
      },
      {
        "name": "DDoSLevel",
        "desc": "Protection level, which is required if `Method` is `set`. Valid values: [low,middle,high]"
      }
    ],
    "desc": "This API is used to read or modify DDoS protection level."
  },
  "DescribeDDoSAttackSource": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
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
        "name": "Limit",
        "desc": "Number of entries per page. A value of 0 means no pagination"
      },
      {
        "name": "Offset",
        "desc": "Page start offset, whose value is (page number - 1) * number of entries per page"
      },
      {
        "name": "IpList",
        "desc": "IP attack source of specified resource, which is optional"
      }
    ],
    "desc": "This API is used to get the DDoS attack source list."
  },
  "DescribeCCEvList": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic"
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
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "IpList",
        "desc": "Resource instance IP. When `business` is not `basic`, if `IpList` is not empty, `Id` must not be empty;"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. A value of 0 means no pagination"
      },
      {
        "name": "Offset",
        "desc": "Page start offset, whose value is (page number - 1) * number of entries per page"
      }
    ],
    "desc": "This API is used to get the CC attack event list."
  },
  "ModifyDDoSWaterKey": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "PolicyId",
        "desc": "Policy ID"
      },
      {
        "name": "Method",
        "desc": "Key operation. Valid values: [add (add), delete (delete), open (open), close (close), get (get key)]"
      },
      {
        "name": "KeyId",
        "desc": "Key ID, which can be left empty or 0 when adding a key but is required for other operations"
      }
    ],
    "desc": "This API is used to add, delete, enable, or disable a watermark key."
  },
  "DescribeInsurePacks": {
    "params": [
      {
        "name": "IdList",
        "desc": "Guarantee package ID, which is optional. If you need to get the guarantee package with a specified ID (such as insure-000000xe), please use this field"
      }
    ],
    "desc": "This API is used to get the guarantee package list."
  },
  "DeleteL4Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "RuleIdList",
        "desc": "Rule ID list"
      }
    ],
    "desc": "This API is used to delete one or more layer-4 forwarding rules."
  },
  "DescribeDDoSNetEvList": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`net`: Anti-DDoS Ultimate)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
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
        "name": "Limit",
        "desc": "Number of entries per page. A value of 0 means no pagination"
      },
      {
        "name": "Offset",
        "desc": "Page start offset, whose value is (page number - 1) * number of entries per page"
      }
    ],
    "desc": "This API is used to get the DDoS attack event list of an Anti-DDoS Ultimate resource."
  },
  "ModifyCCHostProtection": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "RuleId",
        "desc": "Rule ID"
      },
      {
        "name": "Method",
        "desc": "Enables/disables CC domain name protection. Valid values: [open (enable), close (disable)]"
      }
    ],
    "desc": "This API is used to enable or disable CC domain name protection."
  },
  "DescribleRegionCount": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP)"
      },
      {
        "name": "LineList",
        "desc": "Line search. Valid values: [1 (BGP line), 2 (Nanjing Telecom), 3 (Nanjing Unicom), 99 (third-party partner line)]. This field is valid only for Anti-DDoS Advanced and should be ignored for other product"
      }
    ],
    "desc": "This API is used to get the number of resource instances in a region."
  },
  "CreateL7Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Rules",
        "desc": "Rule list"
      }
    ],
    "desc": "This API is used to add a layer-7 (website) forwarding rule."
  },
  "DescribeIpUnBlockList": {
    "params": [
      {
        "name": "BeginTime",
        "desc": "Start time"
      },
      {
        "name": "EndTime",
        "desc": "End time"
      },
      {
        "name": "Ip",
        "desc": "IP (if this field is not empty, IP filtering will be performed)"
      },
      {
        "name": "Paging",
        "desc": "Pagination parameter (paginated query will be performed if this field is not empty). This field will be disused in the future. Please use the `Limit` and `Offset` fields instead;"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. A value of 0 means no pagination"
      },
      {
        "name": "Offset",
        "desc": "Page start offset, whose value is (page number - 1) * number of entries per page"
      }
    ],
    "desc": "This API is used to get the IP unblocking records."
  },
  "DescribeIPProductInfo": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP)"
      },
      {
        "name": "IpList",
        "desc": "IP list"
      }
    ],
    "desc": "This API is used to get the Tencent Cloud asset information corresponding to an IP of a single IP instance or multi-IP instance, which is supported only for IPs of single IP instances and multi-IP instances."
  },
  "DescribeCCSelfDefinePolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgp`: Anti-DDoS Pro, `bgp-multip`: Anti-DDoS Pro (multi-IP)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Limit",
        "desc": "Number of entries pulled"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      }
    ],
    "desc": "This API is used to get a custom CC policy."
  },
  "ModifyCCFrequencyRulesStatus": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "RuleId",
        "desc": "Layer-7 forwarding rule ID, which can be obtained through the `DescribleL7Rules` API"
      },
      {
        "name": "Method",
        "desc": "Enables or disable. Valid values: [\"on\", \"off\"]"
      }
    ],
    "desc": "This API is used to enable or disable an access frequency control rule for CC protection."
  },
  "ModifyCCThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate, `basic`: Anti-DDoS Basic"
      },
      {
        "name": "Threshold",
        "desc": "CC protection threshold. Valid values: (0 100 150 240 350 480 550 700 850 1000 1500 2000 3000 5000 10000 20000);\nIf `Business` is Anti-DDoS Advanced or Anti-DDoS Ultimate, its maximum CC protection threshold is subject to the base protection bandwidth in the following way:\n  Base bandwidth: maximum CC protection threshold\n  10:  20000,\n  20:  40000,\n  30:  70000,\n  40:  100000,\n  50:  150000,\n  60:  200000,\n  80:  250000,\n  100: 300000,"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Protocol",
        "desc": "CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `RuleId` field is required;"
      },
      {
        "name": "RuleId",
        "desc": "HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API);\nRequired if `Protocol` is `https`;"
      },
      {
        "name": "BasicIp",
        "desc": "Queried IP address (only provided by Anti-DDoS Basic), such as 1.1.1.1"
      },
      {
        "name": "BasicRegion",
        "desc": "IP region (only provided for Anti-DDoS Basic). Valid values: region abbreviations such as gz, bj, sh, and hk"
      },
      {
        "name": "BasicBizType",
        "desc": "Zone type (only provided for Anti-DDoS Basic). Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel)."
      },
      {
        "name": "BasicDeviceType",
        "desc": "Device type (only provided for Anti-DDoS Basic). Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel)."
      },
      {
        "name": "BasicIpInstance",
        "desc": "IPInstance Nat gateway (only provided for Anti-DDoS Basic), which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)"
      },
      {
        "name": "BasicIspCode",
        "desc": "ISP line (only provided for Anti-DDoS Basic), which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)"
      },
      {
        "name": "Domain",
        "desc": ""
      }
    ],
    "desc": "This API is used to modify the CC protection threshold."
  },
  "DescribleL4Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "RuleIdList",
        "desc": "Rule ID, which is optional. If this field is entered, the specified rule will be obtained"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. A value of 0 means no pagination"
      },
      {
        "name": "Offset",
        "desc": "Page start offset, whose value is (page number - 1) * number of entries per page"
      }
    ],
    "desc": "This API is used to get a layer-4 forwarding rule."
  },
  "ModifyNewDomainRules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)."
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID."
      },
      {
        "name": "Rule",
        "desc": "Domain name forwarding rule."
      }
    ],
    "desc": "This API is used to modify layer-7 forwarding rules."
  },
  "DescribeCCUrlAllow": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Type",
        "desc": "Blocklist or allowlist. Valid value: [white (allowlist)]. Currently, only allowlist is supported.\nNote: this array can only have one value which can only be `white`"
      },
      {
        "name": "Limit",
        "desc": "Pagination parameter"
      },
      {
        "name": "Offset",
        "desc": "Pagination parameter"
      },
      {
        "name": "Protocol",
        "desc": "HTTP or HTTPS CC protection, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)];"
      }
    ],
    "desc": "This API is used to get the CC URL allowlist."
  },
  "DescribeL7HealthConfig": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "RuleIdList",
        "desc": "Rule ID array. To export the health check configurations of all rules, leave this field empty or enter an empty array;"
      }
    ],
    "desc": "This API is used to export the layer-7 health check configuration."
  },
  "DescribeCCTrend": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic"
      },
      {
        "name": "Ip",
        "desc": "Resource IP"
      },
      {
        "name": "MetricName",
        "desc": "Metric. Valid values: [inqps (total requests peak), dropqps (attack requests peak)]"
      },
      {
        "name": "Period",
        "desc": "Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]"
      },
      {
        "name": "StartTime",
        "desc": "Statistics start time"
      },
      {
        "name": "EndTime",
        "desc": "Statistics end time"
      },
      {
        "name": "Id",
        "desc": "Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)"
      }
    ],
    "desc": "This API is used to get CC attack metric data, including total requests peak (QPS) and attack requests (QPS)."
  },
  "CreateCCFrequencyRules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "RuleId",
        "desc": "Layer-7 forwarding rule ID, which can be obtained through the `DescribleL7Rules` API"
      },
      {
        "name": "Mode",
        "desc": "Matching rule. Valid values: [\"include\" (prefix match), \"equal\" (exact match)]"
      },
      {
        "name": "Period",
        "desc": "Reference period in seconds. Valid values: [10, 30, 60]"
      },
      {
        "name": "ReqNumber",
        "desc": "Number of access requests. Value range: [1-10000]"
      },
      {
        "name": "Act",
        "desc": "Action take. Valid values: [\"alg\" (CAPTCHA), \"drop\" (blocking)]"
      },
      {
        "name": "ExeDuration",
        "desc": "Execution duration in seconds. Valid range: [1-900]"
      },
      {
        "name": "Uri",
        "desc": "URI string, which must start with `/`, such as `/abc/a.php`. Length limit: 31. If URI is `/`, only prefix match can be selected as the matching mode;"
      },
      {
        "name": "UserAgent",
        "desc": "`User-Agent` string. Length limit: 80"
      },
      {
        "name": "Cookie",
        "desc": "Cookie string. Length limit: 40"
      }
    ],
    "desc": "This API is used to add an access frequency control rule for CC protection."
  },
  "ModifyL7Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Rule",
        "desc": "Rule"
      }
    ],
    "desc": "This API is used to modify the layer-7 forwarding rules."
  },
  "DescribeBasicCCThreshold": {
    "params": [
      {
        "name": "BasicIp",
        "desc": "Queried IP address, such as 1.1.1.1"
      },
      {
        "name": "BasicRegion",
        "desc": "IP region. Valid values: region abbreviations such as gz, bj, sh, and hk"
      },
      {
        "name": "BasicBizType",
        "desc": "Zone type. Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel)."
      },
      {
        "name": "BasicDeviceType",
        "desc": "Device type. Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel)."
      },
      {
        "name": "BasicIpInstance",
        "desc": "IPInstance Nat gateway, which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)"
      },
      {
        "name": "BasicIspCode",
        "desc": "ISP line, which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)"
      }
    ],
    "desc": "This API is used to get the CC protection threshold of Anti-DDoS Basic."
  },
  "CreateL7HealthConfig": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "HealthConfig",
        "desc": "Layer-7 health check configuration array"
      }
    ],
    "desc": "This API is used to upload layer-7 health check configuration."
  },
  "DescribeResIpList": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "IdList",
        "desc": "Resource ID. If this field is left empty, it means to get all resources IP of the current user"
      }
    ],
    "desc": "This API is used to get the IP list of a resource."
  },
  "CreateInstanceName": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Name",
        "desc": "Instance name. Length limit: 32 characters"
      }
    ],
    "desc": "This API is used to rename a resource instance, which supports single IP instances, multi-IP instances, Anti-DDoS Advanced, and Anti-DDoS Ultimate."
  },
  "DescribeBGPIPL7RuleMaxCnt": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      }
    ],
    "desc": "This API is used to get the maximum number of layer-7 rules that can be added for Anti-DDoS Advanced.\n"
  },
  "ModifyResourceRenewFlag": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `shield`: Chess Shield, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `insurance`: guarantee package, `staticpack`: non-BGP package"
      },
      {
        "name": "Id",
        "desc": "Resource ID"
      },
      {
        "name": "RenewFlag",
        "desc": "Auto-renewal flag (0: manual renewal, 1: auto-renewal, 2: no renewal upon expiration)"
      }
    ],
    "desc": "This API is used to enable or disable auto-renewal for a resource."
  },
  "ModifyCCSelfDefinePolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "SetId",
        "desc": "Policy ID"
      },
      {
        "name": "Policy",
        "desc": "Details of the CC protection policy"
      }
    ],
    "desc": "This API is used to modify a custom CC policy."
  },
  "DescribeDDoSEvInfo": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Anti-DDoS instance ID"
      },
      {
        "name": "Ip",
        "desc": "Resource IP"
      },
      {
        "name": "StartTime",
        "desc": "Attack start time"
      },
      {
        "name": "EndTime",
        "desc": "Attack end time"
      }
    ],
    "desc": "This API is used to get details of a specific DDoS attack."
  },
  "DescribeDDoSPolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate"
      },
      {
        "name": "Id",
        "desc": "Resource ID, which is optional. If a value is entered, it indicates the advanced DDoS policy bound to the resource"
      }
    ],
    "desc": "This API is used to get an advanced DDoS policy."
  }
}