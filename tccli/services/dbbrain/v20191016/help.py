# -*- coding: utf-8 -*-
DESC = "dbbrain-2019-10-16"
INFO = {
  "DescribeTopSpaceTableTimeSeries": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "Limit",
        "desc": "Number of returned top tables. Default value: 20. Maximum value: 20."
      },
      {
        "name": "SortBy",
        "desc": "Field used to sort top tables. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize. Default value: PhysicalFileSize."
      },
      {
        "name": "StartDate",
        "desc": "Start date. It can be as early as 6 days before the current date, and defaults to 6 days before the end date."
      },
      {
        "name": "EndDate",
        "desc": "End date. It can be as early as 6 days before the current date, and defaults to the current date."
      }
    ],
    "desc": "This API is used to query the daily space data of top tables consuming the most instance space. The data is daily collected by DBbrain during a specified time period. The return results are sorted by size by default."
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
  "DescribeDBSpaceStatus": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "RangeDays",
        "desc": "Query period in days. The end date is the current date and the query period is 7 days by default."
      }
    ],
    "desc": "This API is used to query the overview of instance space usage during a specified time period, including disk usage growth (MB), available disk space (MB), total disk space (MB), and estimated number of available days."
  },
  "DescribeTopSpaceTables": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "Limit",
        "desc": "Number of returned top tables. Default value: 20. Maximum value: 20."
      },
      {
        "name": "SortBy",
        "desc": "Field used to sort top tables. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize. Default value: PhysicalFileSize."
      }
    ],
    "desc": "This API is used to query real-time space statistics of top tables of an instance. The return results are sorted by size by default."
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
  }
}