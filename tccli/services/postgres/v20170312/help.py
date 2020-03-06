# -*- coding: utf-8 -*-
DESC = "postgres-2017-03-12"
INFO = {
  "DescribeAccounts": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-6fego161"
      },
      {
        "name": "Limit",
        "desc": "Number of entries returned per page. Default value: 20. Value range: 1–100."
      },
      {
        "name": "Offset",
        "desc": "Page number for data return in paged query. Pagination starts from 0"
      },
      {
        "name": "OrderBy",
        "desc": "Whether to sort by creation time or username. Valid values: `createTime` (sort by creation time), `name` (sort by username)"
      },
      {
        "name": "OrderByType",
        "desc": "Whether returns are sorted in ascending or descending order. Valid values: `desc` (descending), `asc` (ascending)"
      }
    ],
    "desc": "This API is used to get the instance user list."
  },
  "OpenDBExtranetAccess": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-hez4fh0v"
      }
    ],
    "desc": "This API is used to enable public network access."
  },
  "DescribeDBBackups": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-4wdeb0zv."
      },
      {
        "name": "Type",
        "desc": "Backup mode (1: full). Currently, only full backup is supported. The value is 1."
      },
      {
        "name": "StartTime",
        "desc": "Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago"
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of 2018-06-10 17:06:38"
      },
      {
        "name": "Limit",
        "desc": "Number of entries returned per page for backup list. Default value: 20. Minimum value: 1. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Page number for data return in paged query. Pagination starts from 0. Default value: 0."
      }
    ],
    "desc": "This API is used to query the instance backup list."
  },
  "DescribeOrders": {
    "params": [
      {
        "name": "DealNames",
        "desc": "Order name set"
      }
    ],
    "desc": "This API is used to get order information."
  },
  "InitDBInstances": {
    "params": [
      {
        "name": "DBInstanceIdSet",
        "desc": "Instance ID set."
      },
      {
        "name": "AdminName",
        "desc": "Instance admin account username."
      },
      {
        "name": "AdminPassword",
        "desc": "Password corresponding to instance root account username."
      },
      {
        "name": "Charset",
        "desc": "Instance character set. Valid values: UTF8, LATIN1."
      }
    ],
    "desc": "This API is used to initialize a TencentDB for PostgreSQL instance."
  },
  "InquiryPriceUpgradeDBInstance": {
    "params": [
      {
        "name": "Storage",
        "desc": "Instance disk size in GB"
      },
      {
        "name": "Memory",
        "desc": "Instance memory size in GB"
      },
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-hez4fh0v"
      },
      {
        "name": "InstanceChargeType",
        "desc": "Instance billing type. Valid value: `POSTPAID_BY_HOUR` (pay-as-you-go hourly)"
      }
    ],
    "desc": "This API is used to query the upgrade price of an instance."
  },
  "ModifyDBInstancesProject": {
    "params": [
      {
        "name": "DBInstanceIdSet",
        "desc": "TencentDB for PostgreSQL instance ID array"
      },
      {
        "name": "ProjectId",
        "desc": "New project ID of TencentDB for PostgreSQL instance"
      }
    ],
    "desc": "This API is used to transfer an instance to another project."
  },
  "ModifyAccountRemark": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-4wdeb0zv"
      },
      {
        "name": "UserName",
        "desc": "Instance username"
      },
      {
        "name": "Remark",
        "desc": "New remarks corresponding to user `UserName`"
      }
    ],
    "desc": "This API is used to modify account remarks."
  },
  "DescribeRegions": {
    "params": [],
    "desc": "This API is used to query the purchasable regions."
  },
  "RestartDBInstance": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-6r233v55"
      }
    ],
    "desc": "This API is used to restart an instance."
  },
  "ModifyDBInstanceName": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Database instance ID in the format of postgres-6fego161"
      },
      {
        "name": "InstanceName",
        "desc": "New name of database instance"
      }
    ],
    "desc": "This API is used to rename a TencentDB for PostgreSQL instance."
  },
  "CloseDBExtranetAccess": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-6r233v55"
      }
    ],
    "desc": "This API is used to disable the public network link to an instance."
  },
  "DescribeDBXlogs": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-4wdeb0zv."
      },
      {
        "name": "StartTime",
        "desc": "Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago"
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of 2018-06-10 17:06:38"
      },
      {
        "name": "Offset",
        "desc": "Page number for data return in paged query. Pagination starts from 0"
      },
      {
        "name": "Limit",
        "desc": "Number of entries returned per page in paged query. Value range: 1–100."
      }
    ],
    "desc": "This API is used to get the instance Xlog list."
  },
  "DescribeProductConfig": {
    "params": [
      {
        "name": "Zone",
        "desc": "AZ name"
      }
    ],
    "desc": "This API is used to query the purchasable specification configuration."
  },
  "ResetAccountPassword": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-4wdeb0zv"
      },
      {
        "name": "UserName",
        "desc": "Instance account name"
      },
      {
        "name": "Password",
        "desc": "New password corresponding to `UserName` account"
      }
    ],
    "desc": "This API is used to reset the account password of an instance."
  },
  "DescribeDBErrlogs": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-5bq3wfjd"
      },
      {
        "name": "StartTime",
        "desc": "Query start time in the format of 2018-01-01 00:00:00, which cannot be more than 7 days ago"
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of 2018-01-01 00:00:00"
      },
      {
        "name": "DatabaseName",
        "desc": "Database name"
      },
      {
        "name": "SearchKeys",
        "desc": "Search keyword"
      },
      {
        "name": "Limit",
        "desc": "Number of entries returned per page. Value range: 1–100"
      },
      {
        "name": "Offset",
        "desc": "Page number for data return in paged query. Pagination starts from 0"
      }
    ],
    "desc": "This API is used to get error logs."
  },
  "DescribeDBInstanceAttribute": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to query the details of one instance."
  },
  "DescribeZones": {
    "params": [],
    "desc": "This API is used to query the supported AZs."
  },
  "DescribeDBSlowlogs": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-lnp6j617"
      },
      {
        "name": "StartTime",
        "desc": "Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago"
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of 2018-06-10 17:06:38"
      },
      {
        "name": "DatabaseName",
        "desc": "Database name"
      },
      {
        "name": "OrderBy",
        "desc": "Metric for sorting. Valid values: `sum_calls` (total number of calls), `sum_cost_time` (total time consumed)"
      },
      {
        "name": "OrderByType",
        "desc": "Sorting order. desc: descending, asc: ascending"
      },
      {
        "name": "Limit",
        "desc": "Number of entries returned per page. Value range: 1–100. Default value: 20."
      },
      {
        "name": "Offset",
        "desc": "Page number for data return in paged query. Pagination starts from 0"
      }
    ],
    "desc": "This API is used to get slow query logs."
  }
}