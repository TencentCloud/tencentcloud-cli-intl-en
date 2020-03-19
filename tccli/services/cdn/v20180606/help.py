# -*- coding: utf-8 -*-
DESC = "cdn-2018-06-06"
INFO = {
  "DescribeMapInfo": {
    "params": [
      {
        "name": "Name",
        "desc": "Query type:\n`isp`: queries ISP codes\n`district`: queries codes of provinces (Mainland China) or countries/regions (outside Mainland China)"
      }
    ],
    "desc": "This API (DescribeMapInfo) is used to query the IDs of districts or ISPs."
  },
  "DeleteCdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "Domain name\nThe domain name status should be `Disabled`"
      }
    ],
    "desc": "This API is used to delete a specified acceleration domain name."
  },
  "DescribePurgeTasks": {
    "params": [
      {
        "name": "PurgeType",
        "desc": "Specifies a purge type:\n`url`: URL purge record\n`path`: Directory purge record"
      },
      {
        "name": "StartTime",
        "desc": "Specifies the starting time of the period you want to query, such as `2018-08-08 00:00:00`"
      },
      {
        "name": "EndTime",
        "desc": "Specifies the end time of the period you want to query, such as 2018-08-08 23:59:59"
      },
      {
        "name": "TaskId",
        "desc": "Specifies a task ID when you want to query by task ID.\nYou must specify either a task ID or a starting time for your query."
      },
      {
        "name": "Offset",
        "desc": "Offset for paged queries. Default value: 0 (the first page)"
      },
      {
        "name": "Limit",
        "desc": "Limit on paged queries. Default value: 20"
      },
      {
        "name": "Keyword",
        "desc": "You can filter the results by domain name or a complete URL beginning with `http(s)://`"
      },
      {
        "name": "Status",
        "desc": "Specifies a task state for your query:\n`fail`: purge failed\n`done`: purge succeeded\n`process`: purge in progress"
      },
      {
        "name": "Area",
        "desc": "Specifies a purge region for your query:\n`mainland`: within Mainland China\n`overseas`: outside Mainland China\n`global`: global"
      }
    ],
    "desc": "This API is used to query the record and progress of URL or directory purge tasks submitted via the `PurgePathCache` or `PurgeUrlsCache` APIs."
  },
  "DescribePayType": {
    "params": [
      {
        "name": "Area",
        "desc": "Specifies a service region.\n`mainland`: queries billing methods within Mainland China;\n`overseas`: queries billing methods outside Mainland China.\nDefault value: `mainland`."
      }
    ],
    "desc": "This API (DescribePayType) is used to query billing information of the current account, such as billing mode and billing cycle."
  },
  "DescribeDomainsConfig": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset for paginated queries. Default value: 0 (the first page)."
      },
      {
        "name": "Limit",
        "desc": "Limit on paginated queries. Default value: 100. Maximum value: 1000."
      },
      {
        "name": "Filters",
        "desc": "Query condition filter, complex type."
      },
      {
        "name": "Sort",
        "desc": "Sorting rules"
      }
    ],
    "desc": "This API is used to query the complete configuration information of CDN acceleration domain names (inside and outside mainland China)."
  },
  "AddCdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "Domain name"
      },
      {
        "name": "ServiceType",
        "desc": "Acceleration domain name service type\nweb: static acceleration\ndownload: download acceleration\nmedia: streaming media VOD acceleration"
      },
      {
        "name": "Origin",
        "desc": "Origin server configuration"
      },
      {
        "name": "ProjectId",
        "desc": "Project ID. Default value: 0, indicating `Default Project`"
      },
      {
        "name": "IpFilter",
        "desc": "IP blacklist/whitelist configuration"
      },
      {
        "name": "IpFreqLimit",
        "desc": "IP access limit configuration"
      },
      {
        "name": "StatusCodeCache",
        "desc": "Status code cache configuration"
      },
      {
        "name": "Compression",
        "desc": "Smart compression configuration"
      },
      {
        "name": "BandwidthAlert",
        "desc": "Bandwidth cap configuration"
      },
      {
        "name": "RangeOriginPull",
        "desc": "Range GETs configuration"
      },
      {
        "name": "FollowRedirect",
        "desc": "301/302 origin-pull follow-redirect configuration"
      },
      {
        "name": "ErrorPage",
        "desc": "Error code redirect configuration (This feature is in beta and not generally available yet.)"
      },
      {
        "name": "RequestHeader",
        "desc": "Request header configuration"
      },
      {
        "name": "ResponseHeader",
        "desc": "Response header configuration"
      },
      {
        "name": "DownstreamCapping",
        "desc": "Download speed configuration"
      },
      {
        "name": "CacheKey",
        "desc": "Node cache key configuration"
      },
      {
        "name": "ResponseHeaderCache",
        "desc": "Header cache configuration"
      },
      {
        "name": "VideoSeek",
        "desc": "Video dragging configuration"
      },
      {
        "name": "Cache",
        "desc": "Cache expiration time configuration"
      },
      {
        "name": "OriginPullOptimization",
        "desc": "Cross-border linkage optimization configuration"
      },
      {
        "name": "Https",
        "desc": "HTTPS acceleration configuration"
      },
      {
        "name": "Authentication",
        "desc": "Timestamp hotlink protection configuration"
      },
      {
        "name": "Seo",
        "desc": "SEO configuration"
      },
      {
        "name": "ForceRedirect",
        "desc": "Access protocol forced redirect configuration"
      },
      {
        "name": "Referer",
        "desc": "Referer hotlink protection configuration"
      },
      {
        "name": "MaxAge",
        "desc": "Browser cache configuration (This feature is in beta and not generally available yet.)"
      },
      {
        "name": "Ipv6",
        "desc": "IPv6 configuration (This feature is in beta and not generally available yet.)"
      },
      {
        "name": "SpecificConfig",
        "desc": "Specific region configuration\nApplicable to cases where the acceleration domain name configuration differs for regions in and outside mainland China."
      },
      {
        "name": "Area",
        "desc": "Domain name acceleration region\nmainland: acceleration inside mainland China\noverseas: acceleration outside mainland China\nglobal: global acceleration\nOverseas acceleration service must be enabled to use overseas acceleration and global acceleration."
      },
      {
        "name": "OriginPullTimeout",
        "desc": "Origin-pull timeout configuration"
      }
    ],
    "desc": "This API is used to add a CDN acceleration domain name."
  },
  "DescribeIpVisit": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Query start time, such as 2018-09-04 10:40:10; the returned result is later than or equal to the specified time.\nAccording to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:10 and the query time granularity is 5 minutes, the time for the first returned entry will be 2018-09-04 10:40:00."
      },
      {
        "name": "EndTime",
        "desc": "Query end time, such as 2018-09-04 10:40:10; the returned result is earlier than or equal to the specified time.\nAccording to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:10 and the query time granularity is 5 minutes, the time for the last returned entry will be 2018-09-04 10:40:00."
      },
      {
        "name": "Domains",
        "desc": "Specifies the list of domain names to be queried; up to 30 domain names can be queried at a time."
      },
      {
        "name": "Project",
        "desc": "Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)\nPlease note that if domain names are specified, this parameter will be ignored."
      },
      {
        "name": "Interval",
        "desc": "Time granularity, which can be:\n5min: 5 minutes. If the query period is within 24 hours, `5min` will be used by default.\nday: 1 day. If the query period is longer than 24 hours, `day` will be used by default."
      }
    ],
    "desc": "This API (DescribeIpVisit) is used to query the number of users who remain active for 5 minutes and the detailed number of daily active users.\n\n+ Number of users who remain active for 5 minutes: Collects deduplicated statistics based on client IP addresses in the log with the 5-minute granularity.\n+ Number of daily active users: Collects deduplicated statistics based on client IP addresses in the log with the 1-day granularity."
  },
  "DescribeCdnData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Queries start time, such as 2018-09-04 10:40:00; the returned result is later than or equal to the specified time.\nAccording to the specified time granularity, forward rounding is applied; for example, if the query end time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the first returned entry will be 2018-09-04 10:00:00.\nThe gap between the start time and end time should be less than or equal to 90 days."
      },
      {
        "name": "EndTime",
        "desc": "Queries end time, such as 2018-09-04 10:40:00; the returned result is earlier than or equal to the specified time.\nAccording to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the last returned entry will be 2018-09-04 10:00:00.\nThe gap between the start time and end time should be less than or equal to 90 days."
      },
      {
        "name": "Metric",
        "desc": "Specifies the query metric, which can be:\nflux: traffic (in bytes)\nbandwidth: bandwidth (in bps)\nrequest: number of requests\nfluxHitRate: traffic hit rate (in %)\nstatusCode: status code. The aggregate data for 2xx, 3xx, 4xx, and 5xx status codes will be returned (in entries)\n2xx: Returns the aggregate list of 2xx status codes and the data for status codes starting with 2 (in entries)\n3xx: Returns the aggregate list of 3xx status codes and the data for status codes starting with 3 (in entries)\n4xx: Returns the aggregate list of 4xx status codes and the data for status codes starting with 4 (in entries)\n5xx: Returns the aggregate list of 5xx status codes and the data for status codes starting with 5 (in entries)\nIt is supported to specify a status code for query. The return will be empty if the status code has never been generated."
      },
      {
        "name": "Domains",
        "desc": "Specifies the list of domain names to be queried\nUp to 30 domain names can be queried at a time"
      },
      {
        "name": "Project",
        "desc": "Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)\nPlease note that if domain names are specified, this parameter will be ignored."
      },
      {
        "name": "Interval",
        "desc": "Time granularity; valid values:\n`min`: data with 1-minute granularity is returned when the queried period is no longer than 24 hours. This value is not supported if the service region you want to query is outside Mainland China;\n`5min`: data with 5-minute granularity is returned when the queried period is no longer than 31 days;\n`hour`: data with 1-hour granularity is returned when the queried period is no longer than 31 days;\n`day`: data with 1-day granularity is returned when the queried period is longer than 31 days."
      },
      {
        "name": "Detail",
        "desc": "The aggregate data for multiple domain names is returned by default (false) during a multi-domain-name query.\nYou can set it to true to return the details for each Domain (the statusCode metric is currently not supported)"
      },
      {
        "name": "Isp",
        "desc": "Specifies an ISP when you query the CDN data within Mainland China. If this is left blank, all ISPs will be queried.\nTo view ISP codes, see [ISP Code Mappings](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)\nIf you have specified an ISP, you cannot specify a province or an IP protocol for the same query."
      },
      {
        "name": "District",
        "desc": "Specifies a province when you query the CDN data within Mainland China. If this is left blank, all provinces will be queried.\nSpecifies a country/region when you query the CDN data outside Mainland China. If this is left blank, all countries/regions will be queried.\nTo view codes of provinces or countries/regions, see [Province Code Mappings](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)\nIf you have specified a province for your query on CDN data within mainland China, you cannot specify an ISP or an IP protocol for the same query."
      },
      {
        "name": "Protocol",
        "desc": "Specifies the protocol to be queried; if you leave it blank, all protocols will be queried.\nall: All protocols\nhttp: specifies the HTTP metric to be queried\nhttps: specifies the HTTPS metric to be queried"
      },
      {
        "name": "DataSource",
        "desc": "Specifies the data source to be queried, which can be seen as the whitelist function."
      },
      {
        "name": "IpProtocol",
        "desc": "Specifies an IP protocol; if it is left blank, all IP protocols will be queried.\n`all`: All protocols\n`ipv4`: IPv4\n`ipv6`: IPv6\nIf the IP protocol to be queried is specified, the district and ISP cannot be specified at the same time"
      },
      {
        "name": "Area",
        "desc": "Specifies a service region. If this value is left blank, CDN data within Mainland China will be queried.\n`mainland`: specifies to query CDN data within Mainland China;\n`overseas`: specifies to query CDN data outside Mainland China."
      },
      {
        "name": "AreaType",
        "desc": "Specifies a region type for your query on CDN data outside Mainland China. If this parameter is left blank, data on the service region will be queried. This parameter is valid only when `Area` is `overseas`.\n`server`: specifies to query data on the service region where Tencent Cloud CDN nodes are located;\n`client`: specifies to query data on the client region where the request devices are located."
      }
    ],
    "desc": "This API (DescribeCdnData) is used to query CDN real-time access monitoring data and supports the following metrics:\n\n+ Traffic (in bytes)\n+ Bandwidth (in bps)\n+ Number of requests\n+ Traffic hit rate (in % with two decimal digits)\n+ Aggregate list of 2xx status codes and the details of status codes starting with 2 (in entries)\n+ Aggregate list of 3xx status codes and the details of status codes starting with 3 (in entries)\n+ Aggregate list of 4xx status codes and the details of status codes starting with 4 (in entries)\n+ Aggregate list of 5xx status codes and the details of status codes starting with 5 (in entries)"
  },
  "DisableCaches": {
    "params": [
      {
        "name": "Urls",
        "desc": "List of URLs to be blocked\nUp to 100 entries can be submitted at a time and 3,000 entries per day."
      }
    ],
    "desc": "This API (DisableCaches) is used to block access to a specific URL on CDN. After a URL is blocked, error 403 will be returned for all access requests to it. (This API is during beta test and not fully available now.)"
  },
  "DescribeDomains": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset for paginated queries. Default value: 0 (the first page)."
      },
      {
        "name": "Limit",
        "desc": "Limit on paginated queries. Default value: 100. Maximum value: 1000."
      },
      {
        "name": "Filters",
        "desc": "Query condition filter, complex type."
      }
    ],
    "desc": "This API is used to query the basic configuration information of CDN acceleration domain names (inside and outside mainland China), including the project ID, service status, service type, creation time, and update time, etc."
  },
  "StartCdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "Domain name\nThe domain name status should be `Disabled`"
      }
    ],
    "desc": "This API is used to enable the acceleration service for a disabled domain name."
  },
  "StopCdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "Domain name\nThe domain name status should be **Enabled**"
      }
    ],
    "desc": "This API is used to suspend the acceleration service for a domain name.\nNote: after the acceleration service has been suspended, requests to the cache node will return a 404 error. In order to avoid impact to your business, please move the domain name to another service before suspending the acceleration service."
  },
  "ListTopData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Query start date. Example: 2018-09-09.\nOnly supports data query at daily granularity. The date in the input parameter is used as the start date.\nData generated at or after 00:00:00 on the start date will be returned.\nOnly data from the last 90 days will be queried."
      },
      {
        "name": "EndTime",
        "desc": "Query end date. Example: 2018-09-10\nOnly supports data query at daily granularity. The date in the input parameter is used as the end date.\nData generated before or at 23:59:59 on the end date will be returned.\nEndTime must be greater than or equal to StartTime"
      },
      {
        "name": "Metric",
        "desc": "Objects to be sorted. Valid values:\n`url`: sorts access URLs with query string parameters included. Supported filters are `flux` and `request`.\n`path`: sorts access URLs with query string parameters excluded. Supported filters are `flux` and `request`. You need to be whitelisted before using this feature.\n`district`: sorts provinces or countries/regions. Supported filters are `flux` and `request`.\n`isp`: sorts ISPs. Supported filters are `flux` and `request`.\n`host`: sorts domain name access data. Supported filters are `flux`, `request`, `bandwidth`, `fluxHitRate`, `2XX`, `3XX`, `4XX`, `5XX` and `statusCode`.\n`originHost`: sorts by domain name origin-pull data. Supported filters are `flux`, `request`, `bandwidth`, `origin_2XX`, `origin_3XX`, `oringin_4XX`, `origin_5XX` and `OriginStatusCode`"
      },
      {
        "name": "Filter",
        "desc": "Metric name used for sorting:\nflux: If Metric is `host`, it indicates the access traffic; if Metric is `originHost`, it indicates the origin-pull traffic.\nbandwidth: If Metric is `host`, it indicates the access bandwidth; if Metric is `originHost`, it indicates the origin-pull bandwidth.\nrequest: If Metric is `host`, it indicates the number of access requests; if Metric is `originHost`, it indicates the number of origin-pull requests.\nfluxHitRate: Average traffic hit rate\n2XX: access 2XX status code\n3XX: access 3XX status code\n4XX: access 4XX status code\n5XX: access 5XX status code\norigin_2XX: origin-pull 2XX status code\norigin_3XX: origin-pull 3XX status code\norigin_4XX: origin-pull 4XX status code\norigin_5XX: origin-pull 5XX status code\nstatusCode: statistics of a specific access status code which is specified in the `Code` parameter.\nOriginStatusCode: statistics of a specific origin-pull status code which is specified in the `Code` parameter."
      },
      {
        "name": "Domains",
        "desc": "Specifies the list of domain names to be queried; up to 30 domain names can be queried at a time."
      },
      {
        "name": "Project",
        "desc": "Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)\nPlease note that if domain names are specified, this parameter will be ignored."
      },
      {
        "name": "Detail",
        "desc": "Default value: `false`, indicating that results for all domain names are returned together when you query multiple domain names.\nIf `Metric` is `Url`, `Path`, `District`, or `Isp` and `Filter` is `flux` or `request`, you can set this parameter to `true`, indicating that results for each domain name are returned."
      },
      {
        "name": "Code",
        "desc": "When Filter is `statusCode` or `OriginStatusCode`, enter a code to query and sort results."
      },
      {
        "name": "Area",
        "desc": "Specifies a service region for the query. If it is left blank, CDN data within Mainland China will be queried.\n`mainland`: specifies to query CDN data within Mainland China;\n`overseas`: specifies to query CDN data outside Mainland China. Supported metrics are `url`, `district`, `host`, and `originHost`. If `Metric` is `originHost`, supported filters are `flux`, `request`, and `bandwidth`."
      },
      {
        "name": "AreaType",
        "desc": "Specifies a region type for the query. If it is left blank, data on the service region will be queried. This parameter is only valid when `Area` is `overseas` and `Metric` is `District` or `Host`.\n`server`: specifies to query data on the service region where Tencent Cloud CDN nodes are located;\n`client`: specifies to query data on the client region where the request devices are located; if `Metric` is `Host`, supported filters are `flux`, `request`, and `bandwidth`."
      }
    ],
    "desc": "This API is used to list data sorted the following ways by using different combinations of the Metric and Filter input parameters:\n\n+ It sorts access URLs by total traffic and total requests, and returns the top 1,000 URLs in descending order.\n+ It sorts client districts by total traffic and total requests, and returns the list of districts in descending order.\n+ It sorts client ISPs by total traffic and total requests, and returns the list of ISPs in descending order.\n+ It sorts domain names by total traffic, peak bandwidth, total requests, average hit rate, and 2XX/3XX/4XX/5XX status codes, and returns the list of domain names in descending order.\n+ It sorts domain names by total origin-pull traffic, peak origin-pull bandwidth, total origin-pull requests, average origin-pull failure rate, and 2XX/3XX/4XX/5XX origin-pull status codes, and returns the list of domain names in descending order.\n\nNote: only data from the last 90 days will be queried."
  },
  "DescribeOriginData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Query start time, such as 2018-09-04 10:40:00; the returned result is later than or equal to the specified time.\nAccording to the specified time granularity, forward rounding is applied; for example, if the query end time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the first returned entry will be 2018-09-04 10:00:00.\nThe gap between the start time and end time should be less than or equal to 90 days."
      },
      {
        "name": "EndTime",
        "desc": "Query end time, such as 2018-09-04 10:40:00; the returned result is earlier than or equal to the specified time.\nAccording to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the last returned entry will be 2018-09-04 10:00:00.\nThe gap between the start time and end time should be less than or equal to 90 days."
      },
      {
        "name": "Metric",
        "desc": "Specifies the query metric, which can be:\nflux: origin-pull traffic (in bytes)\nbandwidth: origin-pull bandwidth (in bps)\nrequest: number of origin-pull requests\nfailRequest: number of failed origin-pull requests\nfailRate: origin-pull failure rate (in %)\nstatusCode: origin-pull status code. The aggregate data for 2xx, 3xx, 4xx, and 5xx origin-pull status codes will be returned (in entries)\n2xx: Returns the aggregate list of 2xx origin-pull status codes and the data for origin-pull status codes starting with 2 (in entries)\n3xx: Returns the aggregate list of 3xx origin-pull status codes and the data for origin-pull status codes starting with 3 (in entries)\n4xx: Returns the aggregate list of 4xx origin-pull status codes and the data for origin-pull status codes starting with 4 (in entries)\n5xx: Returns the aggregate list of 5xx origin-pull status codes and the data for origin-pull status codes starting with 5 (in entries)\nIt is supported to specify a status code for query. The return will be empty if the status code has never been generated."
      },
      {
        "name": "Domains",
        "desc": "Specifies the list of domain names to be queried; up to 30 domain names can be queried at a time."
      },
      {
        "name": "Project",
        "desc": "Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)\nPlease note that if domain names are specified, this parameter will be ignored."
      },
      {
        "name": "Interval",
        "desc": "Time granularity; valid values:\n`min`: data with 1-minute granularity is returned when the queried period is no longer than 24 hours. This value is not supported if the service region you want to query is outside Mainland China;\n`5min`: data with 5-minute granularity is returned when the queried period is no longer than 31 days;\n`hour`: data with 1-hour granularity is returned when the queried period is no longer than 31 days;\n`day`: data with 1-day granularity is returned when the queried period is longer than 31 days."
      },
      {
        "name": "Detail",
        "desc": "The aggregate data for multiple domain names is returned by default (false) when multiple `Domains` are passed in.\nYou can set it to true to return the details for each Domain (the statusCode metric is currently not supported)"
      },
      {
        "name": "Area",
        "desc": "Specifies a service region. If this value is left blank, CDN data within Mainland China will be queried.\n`mainland`: specifies to query CDN data within Mainland China;\n`overseas`: specifies to query CDN data outside Mainland China."
      }
    ],
    "desc": "This API (DescribeOriginData) is used to query CDN real-time origin-pull monitoring data and supports the following metrics:\n\n+ Origin-pull traffic (in bytes)\n+ Origin-pull bandwidth (in bps)\n+ Number of origin-pull requests\n+ Number of failed origin-pull requests\n+ Origin-pull failure rate (in % with two decimal digits)\n+ Aggregate list of 2xx origin-pull status codes and the details of origin-pull status codes starting with 2 (in entries)\n+ Aggregate list of 3xx origin-pull status codes and the details of origin-pull status codes starting with 3 (in entries)\n+ Aggregate list of 4xx origin-pull status codes and the details of origin-pull status codes starting with 4 (in entries)\n+ Aggregate list of 5xx origin-pull status codes and the details of origin-pull status codes starting with 5 (in entries)"
  },
  "DescribeCdnIp": {
    "params": [
      {
        "name": "Ips",
        "desc": "List of IPs to be queried"
      }
    ],
    "desc": "This API is used to query CDN IP ownership."
  },
  "PurgePathCache": {
    "params": [
      {
        "name": "Paths",
        "desc": "List of directories. The protocol header such as \"http://\" or \"https://\" needs to be included."
      },
      {
        "name": "FlushType",
        "desc": "Purge type:\n`flush`: purges updated resources\n`delete`: purges all resources"
      }
    ],
    "desc": "This API is used to submit multiple directory purge tasks, which are carried out according to the acceleration region of the domain names.\nBy default, a maximum of 100 directories can be purged per day for acceleration regions either within or outside Mainland China, and up to 20 tasks can be submitted at a time."
  },
  "DescribeUrlViolations": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset for paginated queries. Default value: 0 (the first page)."
      },
      {
        "name": "Limit",
        "desc": "Limit on paginated queries. Default value: 100."
      },
      {
        "name": "Domains",
        "desc": "Specified domain name query"
      }
    ],
    "desc": "This API is used to query the list of domain name URLs containing regulation-violating content scanned and detected by the CDN system, and the current status of the URLs.\nIt corresponds to the **Pornography Detection** page on the CDN Console."
  },
  "PurgeUrlsCache": {
    "params": [
      {
        "name": "Urls",
        "desc": "List of URLs. The protocol header such as \"http://\" or \"https://\" needs to be included."
      }
    ],
    "desc": "This API is used to submit multiple URL purge tasks, which are carried out according to the current acceleration region of the domain names in the URLs.\nBy default, a maximum of 10,000 URLs can be purged per day for acceleration regions either within or outside Mainland China, and up to 1,000 tasks can be submitted at a time."
  },
  "UpdateDomainConfig": {
    "params": [
      {
        "name": "Domain",
        "desc": "Domain name"
      },
      {
        "name": "ProjectId",
        "desc": "Project ID\b"
      },
      {
        "name": "Origin",
        "desc": "Origin server configuration"
      },
      {
        "name": "IpFilter",
        "desc": "IP blacklist/whitelist configuration"
      },
      {
        "name": "IpFreqLimit",
        "desc": "IP access limit configuration"
      },
      {
        "name": "StatusCodeCache",
        "desc": "Status code cache configuration"
      },
      {
        "name": "Compression",
        "desc": "Smart compression configuration"
      },
      {
        "name": "BandwidthAlert",
        "desc": "Bandwidth cap configuration"
      },
      {
        "name": "RangeOriginPull",
        "desc": "Range GETs configuration"
      },
      {
        "name": "FollowRedirect",
        "desc": "301/302 origin-pull follow-redirect configuration"
      },
      {
        "name": "ErrorPage",
        "desc": "Error code redirect configuration (This feature is in beta and not generally available yet.)"
      },
      {
        "name": "RequestHeader",
        "desc": "Request header configuration"
      },
      {
        "name": "ResponseHeader",
        "desc": "Response header configuration"
      },
      {
        "name": "DownstreamCapping",
        "desc": "Download speed configuration"
      },
      {
        "name": "CacheKey",
        "desc": "Node cache key configuration"
      },
      {
        "name": "ResponseHeaderCache",
        "desc": "Header cache configuration"
      },
      {
        "name": "VideoSeek",
        "desc": "Video dragging configuration"
      },
      {
        "name": "Cache",
        "desc": "Cache expiration time configuration"
      },
      {
        "name": "OriginPullOptimization",
        "desc": "Cross-border linkage optimization configuration"
      },
      {
        "name": "Https",
        "desc": "HTTPS acceleration configuration"
      },
      {
        "name": "Authentication",
        "desc": "Timestamp hotlink protection configuration"
      },
      {
        "name": "Seo",
        "desc": "SEO configuration"
      },
      {
        "name": "ForceRedirect",
        "desc": "Access protocol forced redirect configuration"
      },
      {
        "name": "Referer",
        "desc": "Referer hotlink protection configuration"
      },
      {
        "name": "MaxAge",
        "desc": "Browser cache configuration (This feature is in beta and not generally available yet.)"
      },
      {
        "name": "ServiceType",
        "desc": "Domain name service type\nweb: static acceleration\ndownload: download acceleration\nmedia: streaming media VOD acceleration"
      },
      {
        "name": "SpecificConfig",
        "desc": "Specific region configuration\nApplicable to cases where the acceleration domain name configuration differs for regions in and outside mainland China."
      },
      {
        "name": "Area",
        "desc": "Domain name acceleration region\nmainland: acceleration inside mainland China\noverseas: acceleration outside mainland China\nglobal: global acceleration"
      },
      {
        "name": "OriginPullTimeout",
        "desc": "Origin-pull timeout configuration"
      },
      {
        "name": "AwsPrivateAccess",
        "desc": ""
      }
    ],
    "desc": "This API is used to modify the configuration of CDN acceleration domain names.\nNote: if you need to update complex configuration items, you must pass all the attributes of the entire object. The default value will be used for attributes that are not passed. We recommend calling the querying API to obtain the configuration attributes first. You can then modify and pass the attributes to the API. The certificate and key fields do not need to be passed for HTTPS configuration."
  },
  "DescribeCdnDomainLogs": {
    "params": [
      {
        "name": "Domain",
        "desc": "Specifies a domain name for the query"
      },
      {
        "name": "StartTime",
        "desc": "Starting time, such as `2019-09-04 00:00:00`"
      },
      {
        "name": "EndTime",
        "desc": "End time, such as `2019-09-04 12:00:00`"
      },
      {
        "name": "Offset",
        "desc": "Offset for paged queries. Default value: 0 (the first page)"
      },
      {
        "name": "Limit",
        "desc": "Limit on paged queries. Default value: 100. Maximum value: 1,000"
      },
      {
        "name": "Area",
        "desc": "Specifies a region for the query.\n`mainland`: specifies to return the download link of logs on acceleration within Mainland China;\n`overseas`: specifies to return the download link of logs on acceleration outside Mainland China;\n`global`: specifies to return a download link of logs on acceleration within Mainland China and a link of logs on acceleration outside Mainland China.\nDefault value: `mainland`."
      }
    ],
    "desc": "This API is used to query the download link of an access log. You can use this API for access logs in the last 30 days either within or outside Mainland China."
  },
  "DescribePushTasks": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Starting time, such as `2018-08-08 00:00:00`"
      },
      {
        "name": "EndTime",
        "desc": "End time, such as `2018-08-08 23:59:59`"
      },
      {
        "name": "TaskId",
        "desc": "Specifies a task ID for your query.\nYou must specify either a task ID or a starting time."
      },
      {
        "name": "Keyword",
        "desc": "Specifies a keyword for your query. Please enter a domain name or a complete URL beginning with `http(s)://`"
      },
      {
        "name": "Offset",
        "desc": "Offset for paged queries. Default value: 0 (the first page)"
      },
      {
        "name": "Limit",
        "desc": "Limit on paged queries. Default value: 20"
      },
      {
        "name": "Area",
        "desc": "Specifies a region for your query:\n`mainland`: within Mainland China\n`overseas`: outside Mainland China\n`global`: global"
      },
      {
        "name": "Status",
        "desc": "Specifies a task state for your query:\n`fail`: prefetch failed\n`done`: prefetch succeeded\n`process`: prefetch in progress"
      }
    ],
    "desc": "This API is used to query the submission record and progress of prefetch tasks.\nThis API is in beta test and not fully available yet. Please stay tuned."
  },
  "PushUrlsCache": {
    "params": [
      {
        "name": "Urls",
        "desc": "List of URLs. The protocol header such as \"http://\" or \"https://\" needs to be included."
      },
      {
        "name": "UserAgent",
        "desc": "Specifies the User-Agent header of an HTTP prefetch request when it is forwarded to the origin server\nDefault value: `TencentCdn`"
      },
      {
        "name": "Area",
        "desc": "Destination region for the prefetch\n`mainland`: prefetches resources to nodes within Mainland China\n`overseas`: prefetches resources to nodes outside Mainland China\n`global`: prefetches resources to global nodes\nDefault value: `mainland`. You can prefetch a URL to nodes in a region provided that CDN service has been enabled for the domain name in the URL in the region."
      }
    ],
    "desc": "This API is used to cache specified URL resources to CDN nodes. You can specify acceleration regions for the prefetch.\nBy default, a maximum of 1,000 URLs can be prefetched per day either within or outside Mainland China, and up to 20 tasks can be submitted at a time.\nThis API is in beta test and not fully available yet. Please stay tuned."
  },
  "GetDisableRecords": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Starting time, such as `2018-12-12 10:24:00`"
      },
      {
        "name": "EndTime",
        "desc": "End time, such as 2018-12-14 10:24:00"
      },
      {
        "name": "Url",
        "desc": "Specifies the URL to be queried"
      },
      {
        "name": "Status",
        "desc": "Current URL status\ndisable: The URL remains disabled, and accessing it will return an error 403\nenable: The URL is enabled (unblocked) and can be normally accessed"
      },
      {
        "name": "Offset",
        "desc": "Offset for paged queries. Default value: 0 (the first page)"
      },
      {
        "name": "Limit",
        "desc": "Limit on paged queries. Default value: 20"
      }
    ],
    "desc": "This API is used to query the resource blocking history and the current URL status. (This API is in beta test and not generally available yet.)"
  },
  "UpdatePayType": {
    "params": [
      {
        "name": "Area",
        "desc": "Billing region, which can be mainland or overseas."
      },
      {
        "name": "PayType",
        "desc": "Billing mode, which can be flux or bandwidth."
      }
    ],
    "desc": "This API is used to modify the billing mode of an account. At present, the billing mode of accounts on a monthly billing cycle and sub-accounts cannot be modified."
  },
  "EnableCaches": {
    "params": [
      {
        "name": "Urls",
        "desc": "List of unblocked URLs"
      }
    ],
    "desc": "This API (EnableCaches) is used to unblock manually blocked URLs. After a URL is successfully unblocked, it takes about 5 to 10 minutes to take effect across the entire network. (This API is during beta test and not fully available now.)"
  }
}