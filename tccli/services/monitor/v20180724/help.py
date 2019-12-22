# -*- coding: utf-8 -*-
DESC = "monitor-2018-07-24"
INFO = {
  "DescribeBaseMetrics": {
    "params": [
      {
        "name": "Namespace",
        "desc": "Business namespace"
      },
      {
        "name": "MetricName",
        "desc": "Metric name"
      }
    ],
    "desc": "This API is used to get the details of basic metrics."
  },
  "GetMonitorData": {
    "params": [
      {
        "name": "Namespace",
        "desc": "Namespace. Each Tencent Cloud product has a namespace"
      },
      {
        "name": "MetricName",
        "desc": "Metric name. For detailed metric descriptions of each Tencent Cloud product, see the corresponding [Monitoring API](https://cloud.tencent.com/document/product/248/30384) document"
      },
      {
        "name": "Instances",
        "desc": "Combination of instance object dimensions"
      },
      {
        "name": "Period",
        "desc": "Monitoring statistical period. The default value is 300, and the unit is s"
      },
      {
        "name": "StartTime",
        "desc": "Start time such as 2018-09-22T19:51:23+08:00"
      },
      {
        "name": "EndTime",
        "desc": "End time. Uses the current time by default and cannot be earlier than StartTime"
      }
    ],
    "desc": "This API is used to get the monitoring data of a Tencent Cloud product by passing in the product's namespace, object dimension description, and monitoring metric.\nAPI call rate limit: 20 calls/sec, 1,200 calls/min.\nIf you need to call a lot of metrics and objects, there may be cases where the call fails due to the rate limit. It is recommended to spread the call requests as much as possible over time."
  }
}