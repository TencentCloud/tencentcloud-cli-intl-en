# -*- coding: utf-8 -*-
DESC = "ecdn-2019-10-12"
INFO = {
  "AddEcdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "Domain name."
      },
      {
        "name": "Origin",
        "desc": "Origin server configuration."
      },
      {
        "name": "Area",
        "desc": "Domain name acceleration region. Valid values: mainland (acceleration in Mainland China), overseas (acceleration outside Mainland China), global (global acceleration)."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID. Default value: 0."
      },
      {
        "name": "IpFilter",
        "desc": "IP block/allowlist configuration."
      },
      {
        "name": "IpFreqLimit",
        "desc": "IP access limit configuration."
      },
      {
        "name": "ResponseHeader",
        "desc": "Origin server response header configuration."
      },
      {
        "name": "CacheKey",
        "desc": "Node caching configuration."
      },
      {
        "name": "Cache",
        "desc": "Caching rule configuration."
      },
      {
        "name": "Https",
        "desc": "HTTPS configuration."
      },
      {
        "name": "ForceRedirect",
        "desc": "Forced access protocol redirection configuration."
      }
    ],
    "desc": "This API is used to create an acceleration domain name."
  },
  "PurgePathCache": {
    "params": [
      {
        "name": "Paths",
        "desc": "List of directories to be purged. The protocol header must be included."
      },
      {
        "name": "FlushType",
        "desc": "Purge type. flush: purges updated resources, delete: purges all resources."
      }
    ],
    "desc": "This API is used to batch purge cache directories. One purge task ID will be returned for each submission."
  },
  "StartEcdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "Domain name to be enabled."
      }
    ],
    "desc": "This API is used to enable an acceleration domain name. The domain name to be enabled must be in deactivated status."
  },
  "DescribeEcdnDomainStatistics": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Query start time, such as 2019-12-13 00:00:00.\nThe time span cannot exceed 90 days."
      },
      {
        "name": "EndTime",
        "desc": "Query end time, such as 2019-12-13 23:59:59.\nThe time span cannot exceed 90 days."
      },
      {
        "name": "Metrics",
        "desc": "Statistical metric name. flux: traffic in bytes\nbandwidth: bandwidth in bps\nrequest: number of requests\ndelay: response time in ms\nstatic_request: number of static requests\nstatic_flux: static traffic in bytes\nstatic_bandwidth: static bandwidth in bps\ndynamic_request: number of dynamic requests\ndynamic_flux: dynamic traffic in bytes\ndynamic_bandwidth: dynamic bandwidth in bps"
      },
      {
        "name": "Domains",
        "desc": "Specifies the list of domain names to be queried"
      },
      {
        "name": "Projects",
        "desc": "Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)\nIf no domain name is entered, the specified project will be queried; otherwise, the domain name will prevail"
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Default value: 1000. Maximum value: 3,000."
      }
    ],
    "desc": "This API is used to query the statistical metrics of domain name access within a specified time period."
  },
  "DeleteEcdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "Domain name to be deleted."
      }
    ],
    "desc": "This API is used to delete a specified acceleration domain name. The acceleration domain name to be deleted must be in disabled status."
  },
  "DescribePurgeTasks": {
    "params": [
      {
        "name": "PurgeType",
        "desc": "Purge type to be queried. url: query URL purge records; path: query directory purge records."
      },
      {
        "name": "StartTime",
        "desc": "Start time, such as 2018-08-08 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "End time, such as 2018-08-08 23:59:59"
      },
      {
        "name": "TaskId",
        "desc": "Task ID returned during submission. Either `TaskId` or start time must be specified for a query."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0 (starting from entry 0)."
      },
      {
        "name": "Limit",
        "desc": "Pagination limit. Default value: 20."
      },
      {
        "name": "Keyword",
        "desc": "Query keyword. Please enter a domain name or full URL beginning with `http(s)://`."
      },
      {
        "name": "Status",
        "desc": "Specified task status to be queried. fail: failed, done: succeeded, process: purging."
      }
    ],
    "desc": "This API is used to query the submission history of purge tasks and their execution progress."
  },
  "DescribeEcdnDomainLogs": {
    "params": [
      {
        "name": "Domain",
        "desc": "Domain name to be queried."
      },
      {
        "name": "StartTime",
        "desc": "Log start time, such as 2019-10-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "Log end time, such as 2019-10-02 00:00:00. Only logs for the last 30 days can be queried."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset for log link list. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of log links per page. Default value: 100. Maximum value: 1000."
      }
    ],
    "desc": "This API is used to query the access log download link of a domain name."
  },
  "DescribeDomainsConfig": {
    "params": [
      {
        "name": "Offset",
        "desc": "Pagination offset address. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of domain names per page. Default value: 100."
      },
      {
        "name": "Filters",
        "desc": "Query filter."
      },
      {
        "name": "Sort",
        "desc": "Query result sorting rule."
      }
    ],
    "desc": "This API is used to query the detailed configuration information of a CDN acceleration domain name."
  },
  "DescribePurgeQuota": {
    "params": [],
    "desc": "This API is used to query the usage quota of the purge API."
  },
  "PurgeUrlsCache": {
    "params": [
      {
        "name": "Urls",
        "desc": "List of URLs to be purged. The protocol header must be included."
      }
    ],
    "desc": "This API is used to batch purge URLs. One purge task ID will be returned for each submission."
  },
  "UpdateDomainConfig": {
    "params": [
      {
        "name": "Domain",
        "desc": "Domain name."
      },
      {
        "name": "Origin",
        "desc": "Origin server configuration."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID."
      },
      {
        "name": "IpFilter",
        "desc": "IP blocklist/allowlist configuration."
      },
      {
        "name": "IpFreqLimit",
        "desc": "IP access limit configuration."
      },
      {
        "name": "ResponseHeader",
        "desc": "Origin server response header configuration."
      },
      {
        "name": "CacheKey",
        "desc": "Node caching configuration."
      },
      {
        "name": "Cache",
        "desc": "Caching rule configuration."
      },
      {
        "name": "Https",
        "desc": "HTTPS configuration."
      },
      {
        "name": "ForceRedirect",
        "desc": "Forced access protocol redirection configuration."
      },
      {
        "name": "Area",
        "desc": "Domain name acceleration region. Valid values: mainland (acceleration in Mainland China), overseas (acceleration outside Mainland China), global (global acceleration)."
      }
    ],
    "desc": "This API is used to update the configuration information of an ECDN acceleration domain name.\nNote: if you need to update a complex configuration item, you must pass in all attributes of the entire object, and the default values will be used for the attributes that are not passed in. You are recommended to get the configuration attribute through the query API first and then directly modify and pass it to this API. Due to the special nature of the certificate for HTTPS configuration, you do not need to pass in the certificate and key fields during the update."
  },
  "DescribeDomains": {
    "params": [
      {
        "name": "Offset",
        "desc": "Pagination offset address. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of domain names per page. Default value: 100. Maximum value: 1000."
      },
      {
        "name": "Filters",
        "desc": "Query filter."
      }
    ],
    "desc": "This API is used to query the basic information of a CDN domain name, including the project ID, status, business type, creation time, update time, etc."
  },
  "DescribeEcdnStatistics": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Query start time, such as 2019-12-13 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "Query end time, such as 2019-12-13 23:59:59"
      },
      {
        "name": "Metrics",
        "desc": "Specifies the query metric, which can be:\nflux: traffic in bytes\nbandwidth: bandwidth in bps\nrequest: number of requests\ndelay: response time in ms\n2xx: returns the number of 2xx status codes or details of status codes starting with 2\n3xx: returns the number of 3xx status codes or details of status codes starting with 3\n4xx: returns the number of 4xx status codes or details of status codes starting with 4\n5xx: returns the number of 5xx status codes or details of status codes starting with 5\nstatic_request: number of static requests\nstatic_flux: static traffic in bytes\nstatic_bandwidth: static bandwidth in bps\ndynamic_request: number of dynamic requests\ndynamic_flux: dynamic traffic in bytes\ndynamic_bandwidth: dynamic bandwidth in bps"
      },
      {
        "name": "Interval",
        "desc": "Time granularity, which can be:\n1 day\t 1, 5, 15, 30, 60, 120, 240, 1440 \n2-3 days 15, 30, 60, 120, 240, 1440\n4-7 days 30, 60, 120, 240, 1440\n8-90 days\t 60, 120, 240, 1440"
      },
      {
        "name": "Domains",
        "desc": "Specifies the list of domain names to be queried\n\nUp to 30 acceleration domain names can be queried at a time."
      },
      {
        "name": "Projects",
        "desc": "Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)\nIf no domain name is entered, the specified project will be queried; otherwise, the domain name will prevail"
      }
    ],
    "desc": "This API is used to query ECDN real-time access monitoring data and supports the following metrics:\n\n+ Traffic (in bytes)\n+ Bandwidth (in bps)\n+ Number of requests\n+ Response time (in ms)\n+ Number of 2xx status codes and details of status codes starting with 2\n+ Number of 3xx status codes and details of status codes starting with 3\n+ Number of 4xx status codes and details of status codes starting with 4\n+ Number of 5xx status codes and details of status codes starting with 5"
  },
  "StopEcdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "Domain name to be disabled."
      }
    ],
    "desc": "This API is used to disable an acceleration domain name. The domain name to be disabled must be in enabled or deploying status."
  }
}