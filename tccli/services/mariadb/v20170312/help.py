# -*- coding: utf-8 -*-
DESC = "mariadb-2017-03-12"
INFO = {
  "DescribeAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      },
      {
        "name": "UserName",
        "desc": "Login username."
      },
      {
        "name": "Host",
        "desc": "Access host allowed for user. An account is uniquely identified by username and host."
      },
      {
        "name": "DbName",
        "desc": "Database name. `\\*` indicates that global permissions will be queried (i.e., `\\*.\\*`), in which case the `Type` and `Object ` parameters will be ignored"
      },
      {
        "name": "Type",
        "desc": "Type. Valid values: table, view, proc, func, \\*. If `DbName` is a specific database name and `Type` is `\\*`, the permissions of the database will be queried (i.e., `db.\\*`), in which case the `Object` parameter will be ignored"
      },
      {
        "name": "Object",
        "desc": "Type name. For example, if `Type` is `table`, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\\*` or empty"
      },
      {
        "name": "ColName",
        "desc": "If `Type` is `table` and `ColName` is `\\*`, the permissions of the table will be queried; if `ColName` is a specific field name, the permissions of the corresponding field will be queried"
      }
    ],
    "desc": "This API is used to query the permissions of a TencentDB account.\nNote: accounts with the same username but different hosts are different accounts."
  },
  "ModifyAccountDescription": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      },
      {
        "name": "UserName",
        "desc": "Login username."
      },
      {
        "name": "Host",
        "desc": "Access host allowed for user. An account is uniquely identified by username and host."
      },
      {
        "name": "Description",
        "desc": "New account remarks, which can contain 0–256 characters."
      }
    ],
    "desc": "This API is used to modify the remarks of a TencentDB account.\nNote: accounts with the same username but different hosts are different accounts."
  },
  "DescribeBackupTime": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      }
    ],
    "desc": "This API is used to get the backup time of a TencentDB instance. The backend system will perform instance backup regularly according to this configuration."
  },
  "DescribeDBResourceUsageDetails": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `tdsql-ow728lmc`."
      },
      {
        "name": "StartTime",
        "desc": "Start date in the format of `yyyy-mm-dd`"
      },
      {
        "name": "EndTime",
        "desc": "End date in the format of `yyyy-mm-dd`"
      },
      {
        "name": "MetricName",
        "desc": "Name of pulled metric. Valid values: data_disk_available, binlog_disk_available, mem_available, cpu_usage_rate"
      }
    ],
    "desc": "This API is used to view the current performance data of a database instance."
  },
  "ResetAccountPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      },
      {
        "name": "UserName",
        "desc": "Login username."
      },
      {
        "name": "Host",
        "desc": "Access host allowed for user. An account is uniquely identified by username and host."
      },
      {
        "name": "Password",
        "desc": "New password, which can contain 6–32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks."
      }
    ],
    "desc": "This API is used to reset the password of a TencentDB account.\nNote: accounts with the same username but different hosts are different accounts."
  },
  "ModifyDBParameters": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `tdsql-ow728lmc`."
      },
      {
        "name": "Params",
        "desc": "Parameter list. Each element is a combination of `Param` and `Value`."
      }
    ],
    "desc": "This API is used to modify database parameters."
  },
  "DescribeDBPerformanceDetails": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `tdsql-ow728lmc`."
      },
      {
        "name": "StartTime",
        "desc": "Start date in the format of `yyyy-mm-dd`"
      },
      {
        "name": "EndTime",
        "desc": "End date in the format of `yyyy-mm-dd`"
      },
      {
        "name": "MetricName",
        "desc": "Name of pulled metric. Valid values: long_query, select_total, update_total, insert_total, delete_total, mem_hit_rate, disk_iops, conn_active, is_master_switched, slave_delay"
      }
    ],
    "desc": "This API is used to view the instance performance data details."
  },
  "OpenDBExtranetAccess": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ID of instance for which to enable public network access. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      }
    ],
    "desc": "This API is used to enable public network access for a TencentDB instance. After that, you can access the instance with the public domain name and port obtained through the `DescribeDCDBInstances` API."
  },
  "DescribeDBLogFiles": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `tdsql-ow728lmc`."
      },
      {
        "name": "Type",
        "desc": "Requested log type. Valid values: 1 (binlog), 2 (cold backup), 3 (errlog), 4 (slowlog)."
      }
    ],
    "desc": "This API is used to get the list of various logs of a database, including cold backups, binlogs, errlogs, and slowlogs."
  },
  "GrantAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      },
      {
        "name": "UserName",
        "desc": "Login username."
      },
      {
        "name": "Host",
        "desc": "Access host allowed for user. An account is uniquely identified by username and host."
      },
      {
        "name": "DbName",
        "desc": "Database name. `\\*` indicates that global permissions will be set (i.e., `\\*.\\*`), in which case the `Type` and `Object ` parameters will be ignored. If `DbName` is not `\\*`, the input parameter `Type` is required."
      },
      {
        "name": "Privileges",
        "desc": "Global permission. Valid values: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER, SHOW DATABASES \nDatabase permission. Valid values: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER \nTable/view permission. Valid values: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE VIEW, SHOW VIEW, TRIGGER \nStored procedure/function permission. Valid values: ALTER ROUTINE, EXECUTE \nField permission. Valid values: INSERT, REFERENCES, SELECT, UPDATE"
      },
      {
        "name": "Type",
        "desc": "Type. Valid values: table, view, proc, func, \\*. If `DbName` is a specific database name and `Type` is `\\*`, the permissions of the database will be set (i.e., `db.\\*`), in which case the `Object` parameter will be ignored"
      },
      {
        "name": "Object",
        "desc": "Type name. For example, if `Type` is `table`, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\\*` or empty"
      },
      {
        "name": "ColName",
        "desc": "If `Type` is `table` and `ColName` is `\\*`, the permissions will be granted to the table; if `ColName` is a specific field name, the permissions will be granted to the field"
      }
    ],
    "desc": "This API is used to grant permissions to a TencentDB account.\nNote: accounts with the same username but different hosts are different accounts."
  },
  "DeleteAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      },
      {
        "name": "UserName",
        "desc": "Username"
      },
      {
        "name": "Host",
        "desc": "Access host allowed for user"
      }
    ],
    "desc": "This API is used to delete a TencentDB account, which is uniquely identified by username and host."
  },
  "DescribeDBParameters": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `tdsql-ow728lmc`."
      }
    ],
    "desc": "This API is used to get the current parameter settings of a database."
  },
  "ModifyDBInstancesProject": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "List of IDs of instances to be modified. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      },
      {
        "name": "ProjectId",
        "desc": "ID of the project to be assigned, which can be obtained through the `DescribeProjects` API."
      }
    ],
    "desc": "This API is used to modify the project to which TencentDB instances belong."
  },
  "ModifyLogFileRetentionPeriod": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `tdsql-ow728lmc`."
      },
      {
        "name": "Days",
        "desc": "Retention days up to 30"
      }
    ],
    "desc": "This API is used to modify the number of days for retention of database backup logs."
  },
  "ModifyDBInstanceName": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ID of instance to be modified, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      },
      {
        "name": "InstanceName",
        "desc": "New name of instance, which can contain letters, digits, underscores, and hyphens."
      }
    ],
    "desc": "This API is used to rename a TencentDB instance."
  },
  "DescribeFlow": {
    "params": [
      {
        "name": "FlowId",
        "desc": "Flow ID returned by async request API."
      }
    ],
    "desc": "This API is used to query flow status."
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Queries by instance ID or IDs. Instance ID is in the format of `tdsql-ow728lmc`. Up to 100 instances can be queried in one request."
      },
      {
        "name": "SearchName",
        "desc": "Search field name. Valid values: instancename (search by instance name), vip (search by private IP), all (search by instance ID, instance name, and private IP)."
      },
      {
        "name": "SearchKey",
        "desc": "Search keyword. Fuzzy search is supported. Multiple keywords should be separated by line breaks (`\\n`)."
      },
      {
        "name": "ProjectIds",
        "desc": "Queries by project ID"
      },
      {
        "name": "IsFilterVpc",
        "desc": "Whether to search by VPC"
      },
      {
        "name": "VpcId",
        "desc": "VPC ID, which is valid when `IsFilterVpc` is 1"
      },
      {
        "name": "SubnetId",
        "desc": "VPC subnet ID, which is valid when `IsFilterVpc` is 1"
      },
      {
        "name": "OrderBy",
        "desc": "Sort by field. Valid values: projectId, createtime, instancename"
      },
      {
        "name": "OrderByType",
        "desc": "Sorting order. Valid values: desc, asc"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 20. Maximum value: 100."
      },
      {
        "name": "OriginSerialIds",
        "desc": "Queries by `OriginSerialId`"
      },
      {
        "name": "IsFilterExcluster",
        "desc": "Identifies whether to use the `ExclusterType` field. false: no, true: yes"
      },
      {
        "name": "ExclusterType",
        "desc": "Instance cluster type. 1: non-dedicated cluster, 2: dedicated cluster, 0: all"
      },
      {
        "name": "ExclusterIds",
        "desc": "Filters instances by dedicated cluster ID in the format of `dbdc-4ih6uct9`"
      }
    ],
    "desc": "This API is used to query the TencentDB instance list. It supports filtering instances by project ID, instance ID, private address, and instance name.\nIf no filter is specified, 20 instances will be returned by default. Up to 100 instances can be returned for a single request."
  },
  "CreateAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      },
      {
        "name": "UserName",
        "desc": "Login username, which can contain 1–32 letters, digits, underscores, and hyphens."
      },
      {
        "name": "Host",
        "desc": "Host that can be logged in to, which is in the same format as the host of the MySQL account and supports wildcards, such as %, 10.%, and 10.20.%."
      },
      {
        "name": "Password",
        "desc": "Account password, which can contain 6–32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks."
      },
      {
        "name": "ReadOnly",
        "desc": "Whether to create a read-only account. 0: no; 1: for the account's SQL requests, the slave will be used first, and if it is unavailable, the master will be used; 2: the slave will be used first, and if it is unavailable, the operation will fail."
      },
      {
        "name": "Description",
        "desc": "Account remarks, which can contain 0–256 letters, digits, and common symbols."
      },
      {
        "name": "DelayThresh",
        "desc": "Determines whether the slave is unavailable based on the passed-in time"
      }
    ],
    "desc": "This API is used to create a TencentDB account. Multiple accounts can be created for one instance. Accounts with the same username but different hosts are different accounts."
  },
  "InitDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "List of IDs of instances to be initialized. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      },
      {
        "name": "Params",
        "desc": "Parameter list. Valid values: character_set_server (character set; required); lower_case_table_names (table name case sensitivity; required; 0: case-sensitive, 1: case-insensitive); innodb_page_size (InnoDB data page; default size: 16 KB); sync_mode (sync mode; 0: async; 1: strong sync; 2: downgradable strong sync; default value: strong sync)."
      }
    ],
    "desc": "This API is used to initialize TencentDB instances, including setting the default character set and table name case sensitivity."
  },
  "ModifyBackupTime": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      },
      {
        "name": "StartBackupTime",
        "desc": "Start time of daily backup window in the format of `mm:ss`, such as 22:00"
      },
      {
        "name": "EndBackupTime",
        "desc": "End time of daily backup window in the format of `mm:ss`, such as 23:59"
      }
    ],
    "desc": "This API is used to set the backup time of a TencentDB instance. The backend system will perform instance backup regularly according to this configuration."
  },
  "DescribeDBSlowLogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `tdsql-ow728lmc`."
      },
      {
        "name": "Offset",
        "desc": "Data entry number starting from which to return results"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned"
      },
      {
        "name": "StartTime",
        "desc": "Query start time in the format of `2016-07-23 14:55:20`"
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of `2016-08-22 14:55:20`"
      },
      {
        "name": "Db",
        "desc": "Specific name of database to be queried"
      },
      {
        "name": "OrderBy",
        "desc": "Sort by metric. Valid values: query_time_sum, query_count"
      },
      {
        "name": "OrderByType",
        "desc": "Sorting order. Valid values: desc, asc"
      },
      {
        "name": "Slave",
        "desc": "Whether to query slow queries of the slave. 0: master, 1: slave"
      }
    ],
    "desc": "This API is used to query the slow query log list."
  },
  "CloseDBExtranetAccess": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ID of instance for which to disable public network access. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      }
    ],
    "desc": "This API is used to disable public network access for a TencentDB instance, which will make the public IP address inaccessible. The `DescribeDCDBInstances` API will not return the public domain name and port information of the corresponding instance."
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      }
    ],
    "desc": "This API is used to query the list of accounts of a specified TencentDB instance."
  },
  "CopyAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API."
      },
      {
        "name": "SrcUserName",
        "desc": "Source username"
      },
      {
        "name": "SrcHost",
        "desc": "Access host allowed for source user"
      },
      {
        "name": "DstUserName",
        "desc": "Target username"
      },
      {
        "name": "DstHost",
        "desc": "Access host allowed for target user"
      },
      {
        "name": "SrcReadOnly",
        "desc": "`ReadOnly` attribute of source account"
      },
      {
        "name": "DstReadOnly",
        "desc": "`ReadOnly` attribute of target account"
      }
    ],
    "desc": "This API is used to copy the permissions of a TencentDB account.\nNote: accounts with the same username but different hosts are different accounts. Permissions can only be copied between accounts with the same `Readonly` attribute."
  },
  "DescribeDatabases": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `dcdbt-ow7t8lmc`."
      }
    ],
    "desc": "This API is used to query the list of databases of a TencentDB instance."
  },
  "CloneAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "SrcUser",
        "desc": "Source user account name"
      },
      {
        "name": "SrcHost",
        "desc": "Source user host"
      },
      {
        "name": "DstUser",
        "desc": "Target user account name"
      },
      {
        "name": "DstHost",
        "desc": "Target user host"
      },
      {
        "name": "DstDesc",
        "desc": "Description of target account"
      }
    ],
    "desc": "This API is used to clone an instance account."
  },
  "DescribeDBPerformance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `tdsql-ow728lmc`."
      },
      {
        "name": "StartTime",
        "desc": "Start date in the format of `yyyy-mm-dd`"
      },
      {
        "name": "EndTime",
        "desc": "End date in the format of `yyyy-mm-dd`"
      },
      {
        "name": "MetricName",
        "desc": "Name of pulled metric. Valid values: long_query, select_total, update_total, insert_total, delete_total, mem_hit_rate, disk_iops, conn_active, is_master_switched, slave_delay"
      }
    ],
    "desc": "This API is used to view the current performance data of a database instance."
  },
  "DescribeLogFileRetentionPeriod": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `tdsql-ow728lmc`."
      }
    ],
    "desc": "This API is used to view the configured number of days for retention of database backup logs."
  },
  "DescribeDBResourceUsage": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `tdsql-ow728lmc`."
      },
      {
        "name": "StartTime",
        "desc": "Start date in the format of `yyyy-mm-dd`"
      },
      {
        "name": "EndTime",
        "desc": "End date in the format of `yyyy-mm-dd`"
      },
      {
        "name": "MetricName",
        "desc": "Name of pulled metric. Valid values: data_disk_available, binlog_disk_available, mem_available, cpu_usage_rate"
      }
    ],
    "desc": "This API is used to view the resource usage of a database instance."
  }
}