# -*- coding: utf-8 -*-
DESC = "cdn-2018-06-06"
INFO = {
  "DescribeIpStatus": {
    "params": [
      {
        "name": "Domain",
        "desc": "Acceleration domain name"
      },
      {
        "name": "Layer",
        "desc": "Node type.\nedge: edge server\nlast: intermediate server\nIf this parameter is left empty, edge server information will be returned by default"
      }
    ],
    "desc": "This API is used to query the status of the edge servers and intermediate nodes on the domain name acceleration platform. Note: edge servers are not generally available. This API can only be used by allowlisted accounts."
  },
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
        "desc": "Offset for paginated queries. Default value: 0"
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
        "desc": "Offset for paginated queries. Default value: 0"
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
        "desc": "IP blocklist/allowlist configuration"
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
      },
      {
        "name": "Tag",
        "desc": "Tag configuration"
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
        "desc": "Specifies an ISP when you query the CDN data within Mainland China. If this is left blank, all ISPs will be queried.\nTo view ISP codes, see [ISP Code Mappings](https://intl.cloud.tencent.com/document/product/228/6316?from_cn_redirect=1#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)\nIf you have specified an ISP, you cannot specify a province or an IP protocol for the same query."
      },
      {
        "name": "District",
        "desc": "Specifies a province when you query the CDN data within Mainland China. If this is left blank, all provinces will be queried.\nSpecifies a country/region when you query the CDN data outside Mainland China. If this is left blank, all countries/regions will be queried.\nTo view codes of provinces or countries/regions, see [Province Code Mappings](https://intl.cloud.tencent.com/document/product/228/6316?from_cn_redirect=1#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)\nIf you have specified a province for your query on CDN data within mainland China, you cannot specify an ISP or an IP protocol for the same query."
      },
      {
        "name": "Protocol",
        "desc": "Specifies the protocol to be queried; if you leave it blank, all protocols will be queried.\nall: All protocols\nhttp: specifies the HTTP metric to be queried\nhttps: specifies the HTTPS metric to be queried"
      },
      {
        "name": "DataSource",
        "desc": "Specifies the data source to be queried, which can be seen as the allowlist function."
      },
      {
        "name": "IpProtocol",
        "desc": "Specified IP protocol to be queried. If this parameter is left empty, all protocols will be queried\nall: all protocols\nipv4: specifies to query IPv4 metrics\nipv6: specifies to query IPv6 metrics\nIf the IP protocol to be queried is specified, the district and ISP cannot be specified at the same time\nNote: non-IPv6 allowlisted users cannot specify `ipv4` and `ipv6` for query"
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
        "desc": "Offset for paginated queries. Default value: 0"
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
  "SearchClsLog": {
    "params": [
      {
        "name": "LogsetId",
        "desc": "ID of logset to be queried"
      },
      {
        "name": "TopicIds",
        "desc": "List of IDs of log topics to be queried, separated by commas"
      },
      {
        "name": "StartTime",
        "desc": "Start time of log to be queried in the format of `YYYY-mm-dd HH:MM:SS`"
      },
      {
        "name": "EndTime",
        "desc": "End time of log to be queried in the format of `YYYY-mm-dd HH:MM:SS`"
      },
      {
        "name": "Limit",
        "desc": "Number of logs to be returned at a time. Maximum value: 100"
      },
      {
        "name": "Channel",
        "desc": "Connection channel. Default value: cdn"
      },
      {
        "name": "Query",
        "desc": "Content to be queried. For more information, please visit https://intl.cloud.tencent.com/document/product/614/16982?from_cn_redirect=1"
      },
      {
        "name": "Context",
        "desc": "This field is used when loading more results. Pass through the last `context` value returned to get more log content. Up to 10,000 logs can be obtained through the cursor. Please narrow down the time range as much as possible."
      },
      {
        "name": "Sort",
        "desc": "Sorting by log time. Valid values: asc (ascending), desc (descending). Default value: desc"
      }
    ],
    "desc": "This API is used to search for CLS logs. Search filters can be set to today, 24 hours (one of the last 7 days), and the last 7 days."
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
  "DescribePurgeQuota": {
    "params": [],
    "desc": "This API is used to query the purge usage quota and daily available usage for an account."
  },
  "DescribePushQuota": {
    "params": [],
    "desc": "This API is used to query the prefetch quota and daily available usage."
  },
  "ListTopData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Query start time in the format of `yyyy-MM-dd HH:mm:ss`\nOnly supports data query at daily granularity. The date in the input parameter is used as the start date.\nData generated after or at 00:00:00 on the start date will be returned\nOnly data for the last 90 days can be queried"
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of `yyyy-MM-dd HH:mm:ss`\nOnly supports data query at daily granularity. The date in the input parameter is used as the end date.\nData generated before or at 23:59:59 on the end date will be returned\n`EndTime` must be later than or equal to `StartTime`"
      },
      {
        "name": "Metric",
        "desc": "Object representing the sort criteria. The following objects are supported:\nurl: sorts by access URL (including the query string). Supported filters are `flux` and `request`\npath: sorts by access URL (excluding the query string). Supported filters are `flux` and `request` (allowlist-based feature)\ndistrict: sorts by district. Supported filters are `flux` and `request`\nisp: sorts by ISP. Supported filters are `flux` and `request`\nhost: sorts by domain name access data. Supported filters are `flux`, `request`, `bandwidth`, `fluxHitRate`, 2XX, 3XX, 4XX, 5XX, and `statusCode`\noriginHost: sorts by domain name origin-pull data. Supported filters are `flux`, `request`, `bandwidth`, `origin_2XX`, `origin_3XX`, `origin_4XX`, `origin_5XX`, and `OriginStatusCode`"
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
        "desc": "Default is `false` for multi-domain name queries, which returns sorted results of all domain names. \nIf `Metric` is `url`, `path`, `district`, or `isp` and `Filter` is `flux` or `request`, it can be set to `true` to return the sorted results of each domain."
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
        "desc": "The region type can be specified only when you query CDN data outside Mainland China and `Metric` is `district` or `host`; if you leave it empty, data of the service region will be queried (only applicable when `Area` is `overseas` and `Metric` is `district` or `host`)\nserver: specifies to query data of service region (where a CDN node is located)\nclient: specifies to query data of the client region (where a user request device is located). If `Metric` is `host`, `Filter` can only be `flux`, `request`, or `bandwidth`"
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
        "desc": "Project ID, which can be viewed [here](https://console.cloud.tencent.com/project)\nIf the domain name is not specified, the specified project will be queried. Up to 30 acceleration domain names can be queried at a time\nIf the domain name information is specified, the domain name will prevail"
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
    "desc": "This API is used to query the CDN IP ownership.\n(Note: the request rate limit of this API is subject to the limit in CDN, which is 200 calls/10 minutes)."
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
        "desc": "Offset for paginated queries. Default value: 0"
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
      },
      {
        "name": "Area",
        "desc": "Purging region\nThe acceleration region of the acceleration domain name will be purged if this parameter is not passed in\nIf `mainland` is passed in, only the content cached on nodes in the Chinese mainland will be purged\nIf `overseas` is passed in, only the content cached on nodes outside the Chinese mainland will be purged\nThe specified purging region should match the domain name acceleration region"
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
        "desc": "Project ID"
      },
      {
        "name": "Origin",
        "desc": "Origin server configuration"
      },
      {
        "name": "IpFilter",
        "desc": "IP blocklist/allowlist configuration"
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
        "desc": "Origin access authentication for S3 bucket"
      },
      {
        "name": "UserAgentFilter",
        "desc": "UA blocklist/allowlist Configuration"
      },
      {
        "name": "AccessControl",
        "desc": "Access control"
      },
      {
        "name": "UrlRedirect",
        "desc": "URL redirect configuration"
      },
      {
        "name": "AccessPort",
        "desc": "Access port configuration"
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
        "desc": "Offset for paginated queries. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Limit on paged queries. Default value: 100. Maximum value: 1,000"
      },
      {
        "name": "Area",
        "desc": "Specifies a region for the query.\n`mainland`: specifies to return the download link of logs on acceleration within Mainland China;\n`overseas`: specifies to return the download link of logs on acceleration outside Mainland China;\n`global`: specifies to return a download link of logs on acceleration within Mainland China and a link of logs on acceleration outside Mainland China.\nDefault value: `mainland`."
      },
      {
        "name": "LogType",
        "desc": "The type of log to be downloaded.\naccess: access logs"
      }
    ],
    "desc": "This API is used to query the download link of an access log. You can use this API for access logs in the last 30 days either within or outside Mainland China."
  },
  "ManageClsTopicDomains": {
    "params": [
      {
        "name": "LogsetId",
        "desc": "Logset ID"
      },
      {
        "name": "TopicId",
        "desc": "Log topic ID"
      },
      {
        "name": "Channel",
        "desc": "Connection channel. Default value: cdn"
      },
      {
        "name": "DomainAreaConfigs",
        "desc": "Domain name region configuration. Note: if this field is empty, it means to unbind all domain names from the corresponding topic"
      }
    ],
    "desc": "This API is used to manage the list of domain names bound to a log topic."
  },
  "DescribeCertDomains": {
    "params": [
      {
        "name": "Cert",
        "desc": "Base64-encoded string of certificate in PEM format"
      }
    ],
    "desc": "This API is used to verify an SSL certificate and extract the domain names. It will then return the list of domain names connected to CDN and the list of domain names with the certificate configured."
  },
  "CreateClsLogTopic": {
    "params": [
      {
        "name": "TopicName",
        "desc": "Log topic name"
      },
      {
        "name": "LogsetId",
        "desc": "Logset ID"
      },
      {
        "name": "Channel",
        "desc": "Connection channel. Default value: cdn"
      },
      {
        "name": "DomainAreaConfigs",
        "desc": "Domain name region information"
      }
    ],
    "desc": "This API is used to create a log topic. Note: up to 10 log topics can be created under one logset."
  },
  "DisableClsLogTopic": {
    "params": [
      {
        "name": "LogsetId",
        "desc": "Logset ID"
      },
      {
        "name": "TopicId",
        "desc": "Log topic ID"
      },
      {
        "name": "Channel",
        "desc": "Connection channel. Default value: cdn"
      }
    ],
    "desc": "This API is used to stop publishing to a log topic. Note: after a log topic is disabled, all logs of the domain names bound to it will no longer be published to the topic, and the logs that have already been published will be retained. This action will take effect within 5-15 minutes.\n"
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
      },
      {
        "name": "Layer",
        "desc": "If this parameter is `middle` or left empty, prefetch will be performed onto the intermediate node"
      }
    ],
    "desc": "This API is used to cache specified URL resources to CDN nodes. You can specify acceleration regions for the prefetch.\nBy default, a maximum of 1,000 URLs can be prefetched per day either within or outside Mainland China, and up to 20 tasks can be submitted at a time.\nThis API is in beta test and not fully available yet. Please stay tuned."
  },
  "ListClsTopicDomains": {
    "params": [
      {
        "name": "LogsetId",
        "desc": "Logset ID"
      },
      {
        "name": "TopicId",
        "desc": "Log topic ID"
      },
      {
        "name": "Channel",
        "desc": "Connection channel. Default value: cdn"
      }
    ],
    "desc": "This API is used to get the list of domain names bound to a log topic."
  },
  "ListClsLogTopics": {
    "params": [
      {
        "name": "Channel",
        "desc": "Connection channel. Default value: cdn"
      }
    ],
    "desc": "This API is used to display the list of log topics. Note: a logset can contain up to 10 log topics."
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
        "desc": "Offset for paginated queries. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Limit on paged queries. Default value: 20"
      }
    ],
    "desc": "This API is used to query the resource blocking history and the current URL status. (This API is in beta test and not generally available yet.)"
  },
  "DeleteClsLogTopic": {
    "params": [
      {
        "name": "TopicId",
        "desc": "Log topic ID"
      },
      {
        "name": "LogsetId",
        "desc": "Logset ID"
      },
      {
        "name": "Channel",
        "desc": "Connection channel. Default value: cdn"
      }
    ],
    "desc": "This API is used to delete a log topic. Note: when a log topic is deleted, all logs of the domain names bound to it will no longer be published to the topic, and the logs previously published to the topic will be deleted. This action will take effect within 5-15 minutes."
  },
  "DescribeBillingData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Query start time, e.g., 2018-09-04 10:40:00. The returned result will be later than or equal to the specified time\nThe time will be rounded forward based on the granularity parameter `Interval`. For example, if the query start time is 2018-09-04 10:40:00 and the query time granularity is 1-hour, the time for the first returned entry will be 2018-09-04 10:00:00\nThe range between the start time and end time should be less than or equal to 90 days"
      },
      {
        "name": "EndTime",
        "desc": "Query end time, e.g. 2018-09-04 10:40:00. The returned result will be earlier than or equal to the specified time\nThe time will be rounded forward based on the granularity parameter `Interval`. For example, if the query end time is 2018-09-04 10:40:00 and the query time granularity is 1-hour, the time for the last returned entry will be 2018-09-04 10:00:00\nThe range between the start time and end time should be less than or equal to 90 days"
      },
      {
        "name": "Interval",
        "desc": "Time granularity, which can be:\nmin: 1-minute. The query range should be less than or equal to 24 hours\n5min: 5-minute. The query range should be less than or equal to 31 days\nhour: 1-hour. The query range should be less than or equal to 31 days\nday: 1-day. The query period should be greater than 31 days\n\nCurrently, data query at 1-minute granularity is not supported if the `Area` field is `overseas`"
      },
      {
        "name": "Domain",
        "desc": "Domain name whose billing data is to be queried"
      },
      {
        "name": "Project",
        "desc": "Project ID, which can be viewed [here](https://console.cloud.tencent.com/project)\nIf the `Domain` parameter is populated with specific domain name information, then the billing data of this domain name instead of the specified project will be returned"
      },
      {
        "name": "Area",
        "desc": "Acceleration region whose billing data is to be queried:\nmainland: in the mainland of China\noverseas: outside the mainland of China\nIf this parameter is left empty, `mainland` will be used by default"
      },
      {
        "name": "District",
        "desc": "Country/region to be queried if `Area` is `overseas`\nFor district or country/region codes, please see [District Code Mappings](https://intl.cloud.tencent.com/document/product/228/6316?from_cn_redirect=1#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)\nIf this parameter is left empty, all countries/regions will be queried"
      },
      {
        "name": "Metric",
        "desc": "Billing statistics type\nflux: bill-by-traffic\nbandwidth: bill-by-bandwidth\nDefault value: `bandwidth`"
      }
    ],
    "desc": "This API is used to query billing data details."
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
        "desc": "Offset for paginated queries. Default value: 0"
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
  "EnableClsLogTopic": {
    "params": [
      {
        "name": "LogsetId",
        "desc": "Logset ID"
      },
      {
        "name": "TopicId",
        "desc": "Log topic ID"
      },
      {
        "name": "Channel",
        "desc": "Connection channel. Default value: cdn"
      }
    ],
    "desc": "This API is used to start publishing to a log topic. Note: after a log topic is enabled, all logs of the domain names bound to the topic will be published to it. This action will take effect within 5-15 minutes."
  },
  "DescribeReportData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Query start time in the format of `yyyy-MM-dd`"
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of `yyyy-MM-dd`"
      },
      {
        "name": "ReportType",
        "desc": "Report type\ndaily: daily report\nweekly: weekly report (Monday to Sunday)\nmonthly: monthly report (calendar month)"
      },
      {
        "name": "Area",
        "desc": "Domain name acceleration region\nmainland: in Mainland China\noverseas: outside Mainland China"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of data entries. Default value: 1000."
      },
      {
        "name": "Project",
        "desc": "Filters by project ID"
      }
    ],
    "desc": "This API is used to query the daily/weekly/monthly report data at domain name/project levels."
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