# -*- coding: utf-8 -*-
DESC = "dbbrain-2019-10-16"
INFO = {
  "DescribeDBDiagHistory": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "StartTime",
        "desc": "Start time, such as \"2019-09-10 12:13:14\"."
      },
      {
        "name": "EndTime",
        "desc": "End time, such as \"2019-09-11 12:13:14\"."
      }
    ],
    "desc": "This API is used to get the list of instance diagnosis events."
  },
  "DescribeDBDiagEvent": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "EventId",
        "desc": "Event ID, which can be obtained through the `DescribeDBDiagHistory` API."
      }
    ],
    "desc": "This API is used to get the details of an instance exception diagnosis event."
  },
  "DescribeSlowLogTopSqls": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "StartTime",
        "desc": "Start time."
      },
      {
        "name": "EndTime",
        "desc": "End time."
      },
      {
        "name": "SortBy",
        "desc": "Sorting key. Valid values: QueryTime, ExecTimes, RowsSent, LockTime, RowsExamined."
      },
      {
        "name": "OrderBy",
        "desc": "Sorting order. Valid values: ASC (ascending), DESC (descending)."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to get and sort the top slow SQL statements in a specified time period by the aggregation mode of SQL template plus schema."
  },
  "DescribeSlowLogTimeSeriesStats": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "StartTime",
        "desc": "Start time."
      },
      {
        "name": "EndTime",
        "desc": "End time."
      }
    ],
    "desc": "This API is used to get the slow log statistics histogram."
  }
}