# -*- coding: utf-8 -*-
DESC = "sqlserver-2018-03-28"
INFO = {
  "DescribeFlowStatus": {
    "params": [
      {
        "name": "FlowId",
        "desc": "Flow ID"
      }
    ],
    "desc": "This API is used to query flow status."
  },
  "ModifyMigration": {
    "params": [
      {
        "name": "MigrateId",
        "desc": "Migration task ID"
      },
      {
        "name": "MigrateName",
        "desc": "New name of migration task. If this parameter is left empty, no modification will be made"
      },
      {
        "name": "MigrateType",
        "desc": "New migration type (1: structure migration, 2: data migration, 3: incremental sync). If this parameter is left empty, no modification will be made"
      },
      {
        "name": "SourceType",
        "desc": "Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode). If this parameter is left empty, no modification will be made"
      },
      {
        "name": "Source",
        "desc": "Migration source. If this parameter is left empty, no modification will be made"
      },
      {
        "name": "Target",
        "desc": "Migration target. If this parameter is left empty, no modification will be made"
      },
      {
        "name": "MigrateDBSet",
        "desc": "Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5). If it left empty, no modification will be made"
      }
    ],
    "desc": "This API is used to modify an existing migration task."
  },
  "DescribeOrders": {
    "params": [
      {
        "name": "DealNames",
        "desc": "Order array. The order name will be returned upon shipping, which can be used to call the `DescribeOrders` API to query shipment status"
      }
    ],
    "desc": "This API is used to query order information."
  },
  "DescribeMigrations": {
    "params": [
      {
        "name": "StatusSet",
        "desc": "Status set. As long as a migration task is in a status therein, it will be listed"
      },
      {
        "name": "MigrateName",
        "desc": "Migration task name (fuzzy match)"
      },
      {
        "name": "Limit",
        "desc": "Number of results per page. Value range: 1-100. Default value: 100"
      },
      {
        "name": "Offset",
        "desc": "Page number. Default value: 0"
      },
      {
        "name": "OrderBy",
        "desc": "The query results are sorted by keyword. Valid values: name, createTime, startTime, endTime, status"
      },
      {
        "name": "OrderByType",
        "desc": "Sorting order. Valid values: desc, asc"
      }
    ],
    "desc": "This API is used to query the list of eligible migration tasks based on the entered criteria."
  },
  "ResetAccountPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Database instance ID in the format of mssql-njj2mtpl"
      },
      {
        "name": "Accounts",
        "desc": "Updated account password information array"
      }
    ],
    "desc": "This API is used to reset the account password of an instance."
  },
  "ModifyDBName": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "OldDBName",
        "desc": "Old database name"
      },
      {
        "name": "NewDBName",
        "desc": "New name of database"
      }
    ],
    "desc": "This API is used to rename a database."
  },
  "InquiryPriceCreateDBInstances": {
    "params": [
      {
        "name": "Zone",
        "desc": "AZ ID, which can be obtained through the `Zone` field in the returned value of the `DescribeZones` API"
      },
      {
        "name": "Memory",
        "desc": "Memory size in GB"
      },
      {
        "name": "Storage",
        "desc": "Instance capacity in GB"
      },
      {
        "name": "InstanceChargeType",
        "desc": "Billing type. Valid value: POSTPAID."
      },
      {
        "name": "Period",
        "desc": "Length of purchase in months. Value range: 1-48. Default value: 1"
      },
      {
        "name": "GoodsNum",
        "desc": "Number of instances purchased at a time. Value range: 1-100. Default value: 1"
      },
      {
        "name": "DBVersion",
        "desc": "SQL Server version. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise). Default value: 2008R2."
      },
      {
        "name": "Cpu",
        "desc": "The number of CPU cores of the instance you want to purchase."
      },
      {
        "name": "InstanceType",
        "desc": "The type of purchased instance. Valid values: HA (high-availability edition, including dual-server high availability and AlwaysOn cluster), RO (read-only replica), SI (basic edition). Default value: HA."
      },
      {
        "name": "MachineType",
        "desc": "The host type of purchased instance. Valid values: PM (physical machine), CLOUD_PREMIUM (physical machine with premium cloud disk), CLOUD_SSD (physical machine with SSD). Default value: PM."
      }
    ],
    "desc": "This API is used to query the price of requested instances."
  },
  "ModifyDBInstanceProject": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "Array of instance IDs in the format of mssql-j8kv137v"
      },
      {
        "name": "ProjectId",
        "desc": "Project ID. If this parameter is 0, the default project will be used"
      }
    ],
    "desc": "This API is used to modify the project to which a database instance belongs."
  },
  "DescribeSlowlogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of mssql-k8voqdlz"
      },
      {
        "name": "StartTime",
        "desc": "Query start time"
      },
      {
        "name": "EndTime",
        "desc": "Query end time"
      },
      {
        "name": "Limit",
        "desc": "Number of results per page. Value range: 1-100. Default value: 20"
      },
      {
        "name": "Offset",
        "desc": "Page number. Default value: 0"
      }
    ],
    "desc": "This API is used to get file information of slow query logs."
  },
  "DescribeBackups": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start name (yyyy-MM-dd HH:mm:ss)"
      },
      {
        "name": "EndTime",
        "desc": "End time (yyyy-MM-dd HH:mm:ss)"
      },
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of mssql-njj2mtpl"
      },
      {
        "name": "Limit",
        "desc": "Number of results per page. Value range: 1-100. Default value: 20"
      },
      {
        "name": "Offset",
        "desc": "Page number. Default value: 0"
      }
    ],
    "desc": "This API is used to query the list of backups."
  },
  "ModifyBackupStrategy": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "BackupType",
        "desc": "Backup mode, which supports daily backup only. Valid value: daily."
      },
      {
        "name": "BackupTime",
        "desc": "Backup time. Value range: an integer from 0 to 23."
      },
      {
        "name": "BackupDay",
        "desc": "Backup interval in days when the `BackupType` is `daily`. Valid value: 1."
      }
    ],
    "desc": "This API is used to modify the backup policy."
  },
  "ModifyAccountRemark": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of mssql-j8kv137v"
      },
      {
        "name": "Accounts",
        "desc": "Information of account for which to modify remarks"
      }
    ],
    "desc": "This API is used to modify account remarks."
  },
  "ModifyAccountPrivilege": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Database instance ID in the format of mssql-njj2mtpl"
      },
      {
        "name": "Accounts",
        "desc": "Account permission change information"
      }
    ],
    "desc": "This API is used to modify instance account permissions."
  },
  "RestartDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Database instance ID in the format of mssql-njj2mtpl"
      }
    ],
    "desc": "This API is used to restart a database instance."
  },
  "ModifyDBInstanceName": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Database instance ID in the format of mssql-njj2mtpl"
      },
      {
        "name": "InstanceName",
        "desc": "New name of database instance"
      }
    ],
    "desc": "This API is used to rename an instance."
  },
  "TerminateDBInstance": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "List of instance IDs manually terminated in the format of [mssql-3l3fgqn7], which are the same as the instance IDs displayed on the TencentDB Console page"
      }
    ],
    "desc": "This API is used to manually terminate a pay-as-you-go instance."
  },
  "CreateBackup": {
    "params": [
      {
        "name": "Strategy",
        "desc": "Backup policy (0: instance backup, 1: multi-database backup)"
      },
      {
        "name": "DBNames",
        "desc": "List of names of databases to be backed up (required only for multi-database backup)"
      },
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of mssql-i1z41iwd"
      }
    ],
    "desc": "This API is used to create a backup."
  },
  "CreateDBInstances": {
    "params": [
      {
        "name": "Zone",
        "desc": "Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the `DescribeZones` API"
      },
      {
        "name": "Memory",
        "desc": "Instance memory size in GB"
      },
      {
        "name": "Storage",
        "desc": "Instance storage capacity in GB"
      },
      {
        "name": "InstanceChargeType",
        "desc": "Billing mode. Valid value: POSTPAID (pay-as-you-go)."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID"
      },
      {
        "name": "GoodsNum",
        "desc": "Number of instances purchased this time. Default value: 1. Maximum value: 10"
      },
      {
        "name": "SubnetId",
        "desc": "VPC subnet ID in the format of subnet-bdoe83fa. `SubnetId` and `VpcId` should be set or ignored simultaneously"
      },
      {
        "name": "VpcId",
        "desc": "VPC ID in the format of vpc-dsp338hz. `SubnetId` and `VpcId` should be set or ignored simultaneously"
      },
      {
        "name": "Period",
        "desc": "Length of purchase of instance. The default value is 1, indicating one month. The value cannot exceed 48"
      },
      {
        "name": "AutoVoucher",
        "desc": "Whether to automatically use voucher. 0: no, 1: yes. Default value: no"
      },
      {
        "name": "VoucherIds",
        "desc": "Array of voucher IDs (currently, only one voucher can be used per order)"
      },
      {
        "name": "DBVersion",
        "desc": "SQL Server version. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise). The version purchasable varies by region and can be queried by calling the `DescribeProductConfig` API. If this parameter is left empty, 2008R2 will be used by default."
      },
      {
        "name": "AutoRenewFlag",
        "desc": "Auto-renewal flag. 0: normal renewal, 1: auto-renewal. Default value: 1."
      },
      {
        "name": "SecurityGroupList",
        "desc": "Security group list, which contains security group IDs in the format of sg-xxx."
      },
      {
        "name": "Weekly",
        "desc": "Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: 1 (Monday), 2 (Tuesday), 3 (Wednesday), 4 (Thursday), 5 (Friday), 6 (Saturday), 7 (Sunday)."
      },
      {
        "name": "StartTime",
        "desc": "Configuration of the maintenance window, which specifies the start time of daily maintenance."
      },
      {
        "name": "Span",
        "desc": "Configuration of the maintenance window, which specifies the maintenance duration in hours."
      },
      {
        "name": "HAType",
        "desc": "The type of purchased high-availability instance. Valid values: DUAL (dual-server high availability), CLUSTER (cluster). Default value: DUAL."
      },
      {
        "name": "MultiZones",
        "desc": "Whether to deploy across availability zones. Default value: false."
      }
    ],
    "desc": "This API is used to create an instance."
  },
  "RollbackInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Type",
        "desc": "Rollback type. 0: the database rolled back overwrites the original database; 1: the database rolled back is renamed and does not overwrite the original database"
      },
      {
        "name": "DBs",
        "desc": "Database to be rolled back"
      },
      {
        "name": "Time",
        "desc": "Target time point for rollback"
      }
    ],
    "desc": "This API is used to roll back an instance."
  },
  "DescribeDBs": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "Instance ID"
      },
      {
        "name": "Limit",
        "desc": "Number of results per page. Value range: 1-100. Default value: 20"
      },
      {
        "name": "Offset",
        "desc": "Page number. Default value: 0"
      }
    ],
    "desc": "This API is used to query the list of databases"
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "Project ID"
      },
      {
        "name": "Status",
        "desc": "Instance status. Valid values:\n<li>1: applying</li>\n<li>2: running</li>\n<li>3: running restrictedly (primary/secondary switching)</li>\n<li>4: isolated</li>\n<li>5: repossessing</li>\n<li>6: repossessed</li>\n<li>7: executing task (e.g., backing up or rolling back instance)</li>\n<li>8: deactivated</li>\n<li>9: scaling out instance</li>\n<li>10: migrating instance</li>\n<li>11: read-only</li>\n<li>12: restarting</li>"
      },
      {
        "name": "Offset",
        "desc": "Page number. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Number of results per page. Value range: 1-100. Default value: 100"
      },
      {
        "name": "InstanceIdSet",
        "desc": "One or more instance IDs in the format of mssql-si2823jyl"
      },
      {
        "name": "PayMode",
        "desc": "Retrieves billing type. 0: pay-as-you-go"
      },
      {
        "name": "VpcId",
        "desc": "Unique string-type ID of instance VPC in the format of `vpc-xxx`. If an empty string (\"\") is passed in, filtering will be made by basic network."
      },
      {
        "name": "SubnetId",
        "desc": "Unique string-type ID of instance subnet in the format of `subnet-xxx`. If an empty string (\"\") is passed in, filtering will be made by basic network."
      }
    ],
    "desc": "This API is used to query the list of instances."
  },
  "DescribeZones": {
    "params": [],
    "desc": "This API is used to query currently purchasable AZs."
  },
  "ModifyDBRemark": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of mssql-rljoi3bf"
      },
      {
        "name": "DBRemarks",
        "desc": "Array of database names and remarks, where each element contains a database name and the corresponding remarks"
      }
    ],
    "desc": "This API is used to modify database remarks."
  },
  "CreateAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Database instance ID in the format of mssql-njj2mtpl"
      },
      {
        "name": "Accounts",
        "desc": "Database instance account information"
      }
    ],
    "desc": "This API is used to create an instance account."
  },
  "InquiryPriceUpgradeDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of mssql-njj2mtpl"
      },
      {
        "name": "Memory",
        "desc": "Memory size after instance upgrade in GB, which cannot be smaller than the current instance memory size"
      },
      {
        "name": "Storage",
        "desc": "Storage capacity after instance upgrade in GB, which cannot be smaller than the current instance storage capacity"
      },
      {
        "name": "Cpu",
        "desc": "The number of CUP cores after the instance is upgraded, which cannot be smaller than that of the current cores."
      }
    ],
    "desc": "This API is used to query the upgrade price of an instance."
  },
  "CreateMigration": {
    "params": [
      {
        "name": "MigrateName",
        "desc": "Migration task name"
      },
      {
        "name": "MigrateType",
        "desc": "Migration type (1: structure migration, 2: data migration, 3: incremental sync)"
      },
      {
        "name": "SourceType",
        "desc": "Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)"
      },
      {
        "name": "Source",
        "desc": "Migration source"
      },
      {
        "name": "Target",
        "desc": "Migration target"
      },
      {
        "name": "MigrateDBSet",
        "desc": "Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5)"
      }
    ],
    "desc": "This API is used to create a migration task."
  },
  "DescribeRegions": {
    "params": [],
    "desc": "This API is used to query purchasable regions."
  },
  "DeleteMigration": {
    "params": [
      {
        "name": "MigrateId",
        "desc": "Migration task ID"
      }
    ],
    "desc": "This API is used to delete a migration task."
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Limit",
        "desc": "Number of results per page. Value range: 1-100. Default value: 20"
      },
      {
        "name": "Offset",
        "desc": "Page number. Default value: 0"
      }
    ],
    "desc": "This API is used to pull the list of instance accounts."
  },
  "DescribeRollbackTime": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "DBs",
        "desc": "List of databases to be queried"
      }
    ],
    "desc": "This API is used to query the time range available for instance rollback."
  },
  "DeleteDB": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of mssql-rljoi3bf"
      },
      {
        "name": "Names",
        "desc": "Array of database names"
      }
    ],
    "desc": "This API is used to drop a database."
  },
  "CreateDB": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "DBs",
        "desc": "Database creation information"
      }
    ],
    "desc": "This API is used to create a database."
  },
  "DeleteAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Database instance ID in the format of mssql-njj2mtpl"
      },
      {
        "name": "UserNames",
        "desc": "Array of instance usernames"
      }
    ],
    "desc": "This API is used to delete an instance account."
  },
  "DescribeMigrationDetail": {
    "params": [
      {
        "name": "MigrateId",
        "desc": "Migration task ID"
      }
    ],
    "desc": "This API is used to query migration task details."
  },
  "RestoreInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of mssql-j8kv137v"
      },
      {
        "name": "BackupId",
        "desc": "Backup file ID, which can be obtained through the `Id` field in the returned value of the `DescribeBackups` API"
      }
    ],
    "desc": "This API is used to restore an instance from a backup file."
  },
  "UpgradeDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of mssql-j8kv137v"
      },
      {
        "name": "Memory",
        "desc": "Memory size after instance upgrade in GB, which cannot be smaller than the current instance memory size"
      },
      {
        "name": "Storage",
        "desc": "Storage capacity after instance upgrade in GB, which cannot be smaller than the current instance storage capacity"
      },
      {
        "name": "AutoVoucher",
        "desc": "Whether to automatically use vouchers. 0: no, 1: yes. Default value: 0"
      },
      {
        "name": "VoucherIds",
        "desc": "Voucher ID (currently, only one voucher can be used per order)"
      },
      {
        "name": "Cpu",
        "desc": "The number of CUP cores after the instance is upgraded."
      }
    ],
    "desc": "This API is used to upgrade an instance."
  },
  "RunMigration": {
    "params": [
      {
        "name": "MigrateId",
        "desc": "Migration task ID"
      }
    ],
    "desc": "This API is used to start running a migration task."
  },
  "DescribeProductConfig": {
    "params": [
      {
        "name": "Zone",
        "desc": "AZ ID in the format of ap-guangzhou-1"
      }
    ],
    "desc": "This API is used to query purchasable specification configuration."
  }
}