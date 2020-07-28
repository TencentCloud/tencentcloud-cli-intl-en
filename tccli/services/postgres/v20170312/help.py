# -*- coding: utf-8 -*-
DESC = "postgres-2017-03-12"
INFO = {
  "DescribeOrders": {
    "params": [
      {
        "name": "DealNames",
        "desc": "Order name set"
      }
    ],
    "desc": "This API is used to get order information."
  },
  "DestroyDBInstance": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "ID of the instance to be deleted"
      }
    ],
    "desc": "This API is used to terminate the instance corresponding to a specified `DBInstanceId`."
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
        "desc": "Number of entries to be returned per page for backup list. Default value: 20. Minimum value: 1. Maximum value: 100. (If this parameter is left empty or 0, the default value will be used)"
      },
      {
        "name": "Offset",
        "desc": "Page number for data return in paged query. Pagination starts from 0. Default value: 0."
      }
    ],
    "desc": "This API is used to query the instance backup list."
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
        "desc": "Number of entries returned per page. Value range: 1-100"
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
  "InquiryPriceCreateDBInstances": {
    "params": [
      {
        "name": "Zone",
        "desc": "AZ ID, which can be obtained through the `Zone` field in the returned value of the `DescribeZones` API."
      },
      {
        "name": "SpecCode",
        "desc": "Specification ID, which can be obtained through the `SpecCode` field in the returned value of the `DescribeProductConfig` API."
      },
      {
        "name": "Storage",
        "desc": "Storage capacity size in GB."
      },
      {
        "name": "InstanceCount",
        "desc": "Number of instances. Maximum value: 100. If you need to create more instances at a time, please contact customer service."
      },
      {
        "name": "Period",
        "desc": "Length of purchase in months. Currently, only 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36 are supported."
      },
      {
        "name": "Pid",
        "desc": "Billing ID, which can be obtained through the `Pid` field in the returned value of the `DescribeProductConfig` API."
      },
      {
        "name": "InstanceChargeType",
        "desc": "Instance billing type. Valid value: POSTPAID_BY_HOUR (pay-as-you-go)"
      }
    ],
    "desc": "This API is used to query the purchase price of one or multiple instances."
  },
  "OpenDBExtranetAccess": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-hez4fh0v"
      },
      {
        "name": "IsIpv6",
        "desc": "Whether to enable public network access over IPv6 address. Valid values: 1 (yes), 0 (no)"
      }
    ],
    "desc": "This API is used to enable public network access."
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
        "desc": "Number of entries returned per page in paged query. Value range: 1-100."
      }
    ],
    "desc": "This API is used to get the instance Xlog list."
  },
  "SetAutoRenewFlag": {
    "params": [
      {
        "name": "DBInstanceIdSet",
        "desc": "Instance ID array"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "Renewal flag. 0: normal renewal, 1: auto-renewal, 2: no renewal upon expiration"
      }
    ],
    "desc": "This API is used to set auto-renewal."
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
  "CreateDBInstances": {
    "params": [
      {
        "name": "SpecCode",
        "desc": "Purchasable specification ID, which can be obtained through the `SpecCode` field in the returned value of the `DescribeProductConfig` API."
      },
      {
        "name": "DBVersion",
        "desc": "PostgreSQL kernel version. Currently, only two versions are supported: 9.3.5 and 9.5.4."
      },
      {
        "name": "Storage",
        "desc": "Instance capacity size in GB."
      },
      {
        "name": "InstanceCount",
        "desc": "Number of instances purchased at a time. Value range: 1-100."
      },
      {
        "name": "Period",
        "desc": "Length of purchase in months. Currently, only 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36 are supported."
      },
      {
        "name": "Zone",
        "desc": "AZ ID, which can be obtained through the `Zone` field in the returned value of the `DescribeZones` API."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID."
      },
      {
        "name": "InstanceChargeType",
        "desc": "Instance billing type."
      },
      {
        "name": "AutoVoucher",
        "desc": "Whether to automatically use vouchers. 1: yes, 0: no. Default value: no."
      },
      {
        "name": "VoucherIds",
        "desc": "Voucher ID list (only one voucher can be specified currently)."
      },
      {
        "name": "VpcId",
        "desc": "VPC ID."
      },
      {
        "name": "SubnetId",
        "desc": "VPC subnet ID."
      },
      {
        "name": "AutoRenewFlag",
        "desc": "Renewal flag. 0: normal renewal (default), 1: auto-renewal."
      },
      {
        "name": "ActivityId",
        "desc": ""
      },
      {
        "name": "Name",
        "desc": "Instance name (which will be supported in the future)"
      },
      {
        "name": "NeedSupportIpv6",
        "desc": "Whether to support IPv6 address access. Valid values: 1 (yes), 0 (no)"
      }
    ],
    "desc": "This API is used to create one or more TencentDB for PostgreSQL instances."
  },
  "RenewInstance": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of `postgres-6fego161`"
      },
      {
        "name": "Period",
        "desc": "Renewal duration in months"
      },
      {
        "name": "AutoVoucher",
        "desc": "Whether to automatically use vouchers. 1: yes, 0: no. Default value: 0"
      },
      {
        "name": "VoucherIds",
        "desc": "Voucher ID list (only one voucher can be specified currently)"
      }
    ],
    "desc": "This API is used to renew an instance."
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter. Valid values: db-instance-id, db-instance-name"
      },
      {
        "name": "Limit",
        "desc": "Number of entries returned per page. Default value: 10."
      },
      {
        "name": "Offset",
        "desc": "Page number, starting from 0."
      },
      {
        "name": "OrderBy",
        "desc": ""
      },
      {
        "name": "OrderByType",
        "desc": ""
      }
    ],
    "desc": "This API is used to query the details of one or more instances."
  },
  "DescribeZones": {
    "params": [],
    "desc": "This API is used to query the supported AZs."
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
  "DescribeRegions": {
    "params": [],
    "desc": "This API is used to query the purchasable regions."
  },
  "InquiryPriceRenewDBInstance": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Period",
        "desc": "Renewal duration in months. Maximum value: 48"
      }
    ],
    "desc": "This API is used to query the renewal price of an instance."
  },
  "CloseDBExtranetAccess": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-6r233v55"
      },
      {
        "name": "IsIpv6",
        "desc": "Whether to disable public network access over IPv6 address. Valid values: 1 (yes), 0 (no)"
      }
    ],
    "desc": "This API is used to disable the public network link to an instance."
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-6fego161"
      },
      {
        "name": "Limit",
        "desc": "Number of entries returned per page. Default value: 20. Value range: 1-100."
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
  "DescribeDatabases": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to pull the list of databases."
  },
  "UpgradeDBInstance": {
    "params": [
      {
        "name": "Memory",
        "desc": "Instance memory size in GB after upgrade"
      },
      {
        "name": "Storage",
        "desc": "Instance disk size in GB after upgrade"
      },
      {
        "name": "DBInstanceId",
        "desc": "Instance ID in the format of postgres-lnp6j617"
      },
      {
        "name": "AutoVoucher",
        "desc": "Whether to automatically use vouchers. 1: yes, 0: no. Default value: no"
      },
      {
        "name": "VoucherIds",
        "desc": "Voucher ID list (only one voucher can be specified currently)"
      },
      {
        "name": "ActivityId",
        "desc": ""
      }
    ],
    "desc": "This API is used to upgrade an instance."
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
        "desc": "Number of entries returned per page. Value range: 1-100. Default value: 20."
      },
      {
        "name": "Offset",
        "desc": "Page number for data return in paged query. Pagination starts from 0"
      }
    ],
    "desc": "This API is used to get slow query logs."
  }
}