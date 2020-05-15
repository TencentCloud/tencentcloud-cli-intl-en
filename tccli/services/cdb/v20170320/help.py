# -*- coding: utf-8 -*-
DESC = "cdb-2017-03-20"
INFO = {
  "DescribeDBInstanceGTID": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      }
    ],
    "desc": "This API (DescribeDBInstanceGTID) is used to query whether GTID is activated for a TencentDB instance. Instances on or below version 5.5 are not supported."
  },
  "DescribeTimeWindow": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (DescribeTimeWindow) is used to query the maintenance time window of a TencentDB instance."
  },
  "DescribeDataBackupOverview": {
    "params": [
      {
        "name": "Product",
        "desc": "TencentDB product type to be queried. Currently, only `mysql` is supported."
      }
    ],
    "desc": "This API is used to query the data backup overview of a user in the current region."
  },
  "BalanceRoGroupLoad": {
    "params": [
      {
        "name": "RoGroupId",
        "desc": "RO group ID in the format of `cdbrg-c1nl9rpv`."
      }
    ],
    "desc": "This API is used to rebalance the loads of instances in an RO group. Please note that the database connections to those instances will be interrupted transiently; therefore, you should ensure that your application can reconnect to the databases. This operation should be performed with caution."
  },
  "IsolateDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      }
    ],
    "desc": "This API is used to isolate a TencentDB instance, which will no longer be accessible via IP and port. The isolated instance can be started up in the recycle bin. If it is isolated due to arrears, please top up your account as soon as possible."
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Offset",
        "desc": "Record offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned for a single request. Value range: 1-100. Default value: 20."
      },
      {
        "name": "AccountRegexp",
        "desc": "Regular expression for matching account names, which complies with the rules at MySQL official website."
      }
    ],
    "desc": "This API (DescribeAccounts) is used to query information of all TencentDB accounts."
  },
  "ModifyInstanceTag": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "ReplaceTags",
        "desc": "Tag to be added or modified."
      },
      {
        "name": "DeleteTags",
        "desc": "Tag to be deleted."
      }
    ],
    "desc": "This API (ModifyInstanceTag) is used to add, modify, or delete an instance tag."
  },
  "DescribeBackupOverview": {
    "params": [
      {
        "name": "Product",
        "desc": "TencentDB product type to be queried. Currently, only `mysql` is supported."
      }
    ],
    "desc": "This API is used to query the backup overview of a user. It will return the user's current total number of backups, total capacity used by backups, capacity in the free tier, and paid capacity (all capacity values are in bytes)."
  },
  "ModifyDBInstanceName": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      },
      {
        "name": "InstanceName",
        "desc": "Instance name."
      }
    ],
    "desc": "This API (ModifyDBInstanceName) is used to rename a TencentDB instance."
  },
  "OfflineIsolatedInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (OfflineIsolatedInstances) is used to deactivate isolated TencentDB instances immediately. The instances must be in isolated status, i.e., their `Status` value is 5 in the return of the [instance list querying API](https://cloud.tencent.com/document/api/236/15872).\n\nThis is an asynchronous API. There may be a delay in repossessing some resources. You can query the details by using the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) and specifying the InstanceId and the `Status` value as [5, 6, 7]. If the returned instance is empty, then all its resources have been released.\n\nNote that once an instance is deactivated, its resources and data will not be recoverable. Please do so with caution."
  },
  "OpenDBInstanceGTID": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (OpenDBInstanceGTID) is used to enable GTID for a TencentDB instance. Only instances on or above version 5.6 are supported."
  },
  "DescribeRollbackTaskDetail": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID, which is the same as the instance ID displayed in the TencentDB Console. You can use the [DescribeDBInstances API](https://cloud.tencent.com/document/api/236/15872) to query the ID."
      },
      {
        "name": "AsyncRequestId",
        "desc": "Async task ID."
      },
      {
        "name": "Limit",
        "desc": "Pagination parameter, i.e., the number of entries to be returned for a single request. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      }
    ],
    "desc": "This API is used to query the details of a TencentDB instance rollback task."
  },
  "ModifyDBInstanceSecurityGroups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "List of IDs of security groups to be modified, which is an array of one or more security group IDs."
      }
    ],
    "desc": "This API (ModifyDBInstanceSecurityGroups) is used to modify the security groups bound to a TencentDB instance."
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      },
      {
        "name": "AsyncRequestId",
        "desc": "ID of an async task request, i.e., `AsyncRequestId` returned by relevant TencentDB operations."
      },
      {
        "name": "TaskTypes",
        "desc": "Task type. If no value is passed in, all task types will be queried. Valid values:\n1 - rolling back a database;\n2 - performing an SQL operation;\n3 - importing data;\n5 - setting a parameter;\n6 - initializing a TencentDB instance;\n7 - restarting a TencentDB instance;\n8 - enabling GTID of a TencentDB instance;\n9 - upgrading a read-only instance;\n10 - rolling back databases in batches;\n11 - upgrading a master instance;\n12 - deleting a TencentDB table;\n13 - promoting a disaster recovery instance."
      },
      {
        "name": "TaskStatus",
        "desc": "Task status. If no value is passed in, all task statuses will be queried. Valid values:\n-1 - undefined;\n0 - initializing;\n1 - running;\n2 - succeeded;\n3 - failed;\n4 - terminated;\n5 - deleted;\n6 - paused."
      },
      {
        "name": "StartTimeBegin",
        "desc": "Start time of the first task in the format of yyyy-MM-dd HH:mm:ss, such as 2017-12-31 10:40:01. It is used for queries by time range."
      },
      {
        "name": "StartTimeEnd",
        "desc": "End time of the last task in the format of yyyy-MM-dd HH:mm:ss, such as 2017-12-31 10:40:01. It is used for queries by time range."
      },
      {
        "name": "Offset",
        "desc": "Record offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned for a single request. Default value: 20. Maximum value: 100."
      }
    ],
    "desc": "This API (DescribeTasks) is used to query the list of tasks for a TencentDB instance."
  },
  "DescribeBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (DescribeBackupConfig) is used to query the configuration information of a TencentDB instance backup."
  },
  "CloseWanService": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      }
    ],
    "desc": "This API (CloseWanService) is used to disable public network access for TencentDB instance, which will make public IP addresses inaccessible."
  },
  "DescribeDefaultParams": {
    "params": [
      {
        "name": "EngineVersion",
        "desc": "MySQL version. Currently, the supported versions are [\"5.1\", \"5.5\", \"5.6\", \"5.7\"]."
      }
    ],
    "desc": "This API (DescribeDefaultParams) is used to query the list of default configurable parameters."
  },
  "DescribeTagsOfInstanceIds": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "List of instances."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset."
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page."
      }
    ],
    "desc": "This API (DescribeTagsOfInstanceIds) is used to query the tag information of a TencentDB instance."
  },
  "DescribeDatabases": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Offset",
        "desc": "Offset. Minimum value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned for a single request. Value range: 1-100. Maximum value: 20."
      },
      {
        "name": "DatabaseRegexp",
        "desc": "Regular expression for matching database names."
      }
    ],
    "desc": "This API (DescribeDatabases) is used to query the information of databases of a TencentDB instance."
  },
  "DescribeErrorLogData": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "StartTime",
        "desc": "Start timestamp."
      },
      {
        "name": "EndTime",
        "desc": "End timestamp."
      },
      {
        "name": "KeyWords",
        "desc": "List of keywords to match. Up to 15 keywords are supported."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned per page. Maximum value: 400."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to query the details of instance error logs by search criteria. You can only query error logs within a month."
  },
  "DisassociateSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "Security group ID."
      },
      {
        "name": "InstanceIds",
        "desc": "List of instance IDs, which is an array of one or more instance IDs."
      }
    ],
    "desc": "This API (DisassociateSecurityGroups) is used to unbind security groups from instances in batches."
  },
  "DescribeTables": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Database",
        "desc": "Database name."
      },
      {
        "name": "Offset",
        "desc": "Record offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned for a single request. Default value: 20. Maximum value: 2,000."
      },
      {
        "name": "TableRegexp",
        "desc": "Regular expression for matching table names, which complies with the rules at MySQL's official website"
      }
    ],
    "desc": "This API (DescribeTables) is used to query the database tables of a TencentDB instance."
  },
  "DescribeAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "User",
        "desc": "Database user account."
      },
      {
        "name": "Host",
        "desc": "Database account domain name."
      }
    ],
    "desc": "This API (DescribeAccountPrivileges) is used to query the information of TencentDB account permissions."
  },
  "ReleaseIsolatedDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Array of instance IDs in the format of `cdb-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [DescribeDBInstances](https://cloud.tencent.com/document/api/236/15872) API to query the ID, whose value is the `InstanceId` value in the output parameters."
      }
    ],
    "desc": "This API is used to deisolate an isolated TencentDB instance."
  },
  "ModifyTimeWindow": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "TimeRanges",
        "desc": "Time period available for maintenance after modification in the format of 10:00-12:00. Each period lasts from half an hour to three hours, with the start time and end time aligned by half-hour. Up to two time periods can be set. Start and end time range: [00:00, 24:00]."
      },
      {
        "name": "Weekdays",
        "desc": "Specifies for which day to modify the time period. Value range: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. If it is not specified or is left blank, the time period will be modified for every day by default."
      }
    ],
    "desc": "This API (ModifyTimeWindow) is used to update the maintenance time window of a TencentDB instance."
  },
  "DeleteDeployGroups": {
    "params": [
      {
        "name": "DeployGroupIds",
        "desc": "List of IDs of placement groups to be deleted."
      }
    ],
    "desc": "This API is used to delete placement groups by placement group ID (a placement group cannot be deleted if it contains resources)."
  },
  "SwitchForUpgrade": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (SwitchForUpgrade) is used to switch to a new instance. You can initiate this process when the master instance being upgraded is pending switch."
  },
  "DeleteParamTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Parameter template ID."
      }
    ],
    "desc": "This API (DeleteParamTemplate) is used to delete a parameter template."
  },
  "DescribeBackups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Offset",
        "desc": "Offset. Minimum value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Value range: 1-100. Default value: 20."
      }
    ],
    "desc": "This API (DescribeBackups) is used to query the backups of a TencentDB instance."
  },
  "DeleteTimeWindow": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (DeleteTimeWindow) is used to delete a maintenance time window for a TencentDB instance. After it is deleted, the default maintenance time window will be 03:00-04:00, i.e., switch to a new instance will be performed during 03:00-04:00 by default."
  },
  "CreateDBInstanceHour": {
    "params": [
      {
        "name": "GoodsNum",
        "desc": "Number of instances. Value range: 1–100. Default value: 1."
      },
      {
        "name": "Memory",
        "desc": "Instance memory size in MB. Please use the [DescribeDBZoneConfig](https://cloud.tencent.com/document/api/236/17229) API to query the supported memory specifications."
      },
      {
        "name": "Volume",
        "desc": "Instance disk size in GB. Please use the [DescribeDBZoneConfig](https://cloud.tencent.com/document/api/236/17229) API to query the supported disk specifications."
      },
      {
        "name": "EngineVersion",
        "desc": "MySQL version. Valid values: 5.5, 5.6, 5.7. Please use the [DescribeDBZoneConfig](https://cloud.tencent.com/document/api/236/17229) API to query the supported instance versions."
      },
      {
        "name": "UniqVpcId",
        "desc": "VPC ID. If this parameter is not passed in, the basic network will be selected by default. Please use the [DescribeVpcs](/document/api/215/15778) API to query the VPCs."
      },
      {
        "name": "UniqSubnetId",
        "desc": "VPC subnet ID. If `UniqVpcId` is set, then `UniqSubnetId` will be required. Please use the [DescribeSubnets](/document/api/215/15784) API to query the subnet lists."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID. If this is left empty, the default project will be used. Please use the [DescribeProject](https://cloud.tencent.com/document/product/378/4400) API to get the project ID."
      },
      {
        "name": "Zone",
        "desc": "AZ information. By default, the system will automatically select an AZ. Please use the [DescribeDBZoneConfig](https://cloud.tencent.com/document/api/236/17229) API to query the supported AZs."
      },
      {
        "name": "MasterInstanceId",
        "desc": "Instance ID, which is required and the same as the master instance ID when purchasing read-only or disaster recovery instances. Please use the [DescribeDBInstances](https://cloud.tencent.com/document/api/236/15872) API to query the instance IDs."
      },
      {
        "name": "InstanceRole",
        "desc": "Instance type. Valid values: master (master instance), dr (disaster recovery instance), ro (read-only instance). Default value: master."
      },
      {
        "name": "MasterRegion",
        "desc": "AZ information of the master instance, which is required for purchasing disaster recovery instances."
      },
      {
        "name": "Port",
        "desc": "Custom port. Value range: [1024-65535]."
      },
      {
        "name": "Password",
        "desc": "Sets the root account password. Rule: the password can contain 8–64 characters and must contain at least two of the following types of characters: letters, digits, and special symbols (_+-&=!@#$%^*()). This parameter can be specified when purchasing master instances and is meaningless for read-only or disaster recovery instances."
      },
      {
        "name": "ParamList",
        "desc": "List of parameters in the format of `ParamList.0.Name=auto_increment&ParamList.0.Value=1`. You can use the [DescribeDefaultParams](https://cloud.tencent.com/document/api/236/32662) API to query the configurable parameters."
      },
      {
        "name": "ProtectMode",
        "desc": "Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync). Default value: 0. This parameter can be specified when purchasing master instances and is meaningless for read-only or disaster recovery instances."
      },
      {
        "name": "DeployMode",
        "desc": "Multi-AZ. Valid value: 0 (single-AZ), 1 (multi-AZ). Default value: 0. This parameter can be specified when purchasing master instances and is meaningless for read-only or disaster recovery instances."
      },
      {
        "name": "SlaveZone",
        "desc": "AZ information of slave database 1, which is the `Zone` value by default. This parameter can be specified when purchasing master instances and is meaningless for read-only or disaster recovery instances."
      },
      {
        "name": "BackupZone",
        "desc": "AZ information of slave database 2, which is empty by default. This parameter can be specified when purchasing strong sync master instances and is meaningless for other types of instances."
      },
      {
        "name": "SecurityGroup",
        "desc": "Security group parameter. You can use the [DescribeProjectSecurityGroups](https://cloud.tencent.com/document/api/236/15850) API to query the security group details of a project."
      },
      {
        "name": "RoGroup",
        "desc": "Read-only instance information. This parameter must be passed in when purchasing read-only instances."
      },
      {
        "name": "AutoRenewFlag",
        "desc": "This field is meaningless when purchasing pay-as-you-go instances."
      },
      {
        "name": "InstanceName",
        "desc": "Instance name."
      },
      {
        "name": "ResourceTags",
        "desc": "Instance tag information."
      },
      {
        "name": "DeployGroupId",
        "desc": "Placement group ID."
      },
      {
        "name": "ClientToken",
        "desc": "A string that is used to guarantee the idempotency of the request, which is generated by the user and must be unique in each request on the same day. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed."
      },
      {
        "name": "DeviceType",
        "desc": "Instance type. Valid values: HA (High-Availability Edition), BASIC (Basic Edition). If this parameter is not specified, High-Availability Edition will be used by default."
      }
    ],
    "desc": "This API is used to create a pay-as-you-go TencentDB instance (which can be a master, disaster recovery, or read-only instance) by passing in information such as instance specifications, MySQL version number, and quantity.\n\nThis is an async API. You can also use the [DescribeDBInstances](https://cloud.tencent.com/document/api/236/15872) API to query the instance details. If the `Status` value of an instance is 1 and `TaskStatus` is 0, the instance has been successfully delivered.\n\n1. Please use the [DescribeDBZoneConfig](https://cloud.tencent.com/document/api/236/17229) API to query the supported instance specifications first and then use the [DescribeDBPrice](https://cloud.tencent.com/document/api/236/18566) API to query the prices of the supported instances;\n2. You can create up to 100 instances at a time, with an instance validity period of up to 36 months;\n3. MySQL v5.5, v5.6, and v5.7 are supported;\n4. Master instances, read-only instances, and disaster recovery instances can be created;\n5. If `Port`, `ParamList`, or `Password` is set in the input parameters, the instance will be initialized."
  },
  "AddTimeWindow": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Monday",
        "desc": "Time period available for maintenance on Monday in the format of 10:00-12:00. Each period lasts from half an hour to three hours, with the start time and end time aligned by half-hour. Up to two time periods can be set. The same rule applies below."
      },
      {
        "name": "Tuesday",
        "desc": "Maintenance time window on Tuesday"
      },
      {
        "name": "Wednesday",
        "desc": "Maintenance time window on Wednesday"
      },
      {
        "name": "Thursday",
        "desc": "Maintenance time window on Thursday"
      },
      {
        "name": "Friday",
        "desc": "Maintenance time window on Friday"
      },
      {
        "name": "Saturday",
        "desc": "Maintenance time window on Saturday"
      },
      {
        "name": "Sunday",
        "desc": "Maintenance time window on Sunday"
      }
    ],
    "desc": "This API (AddTimeWindow) is used to add a maintenance time window for a TencentDB instance, so as to specify when the instance can automatically perform access switch operations."
  },
  "CreateBackup": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "BackupMethod",
        "desc": "Backup method of target instance. Value range: logical (logical cold backup), physical (physical cold backup)."
      },
      {
        "name": "BackupDBTableList",
        "desc": "Information of the table to be backed up. If this parameter is not set, the entire instance will be backed up by default. It can be set only in logical backup (i.e., BackupMethod = logical). The specified table must exist; otherwise, backup may fail.\nFor example, if you want to backup tb1 and tb2 in db1 and the entire db2, you should set the parameter as [{\"Db\": \"db1\", \"Table\": \"tb1\"}, {\"Db\": \"db1\", \"Table\": \"tb2\"}, {\"Db\": \"db2\"} ]."
      }
    ],
    "desc": "This API (CreateBackup) is used to create a TencentDB instance backup."
  },
  "ModifyDBInstanceVipVport": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      },
      {
        "name": "DstIp",
        "desc": "Destination IP. Either this parameter or `DstPort` must be passed in."
      },
      {
        "name": "DstPort",
        "desc": "Destination port number. Value range: [1024-65535]. Either this parameter or `DstIp` must be passed in."
      },
      {
        "name": "UniqVpcId",
        "desc": "Unified VPC ID"
      },
      {
        "name": "UniqSubnetId",
        "desc": "Unified subnet ID."
      },
      {
        "name": "ReleaseDuration",
        "desc": "Repossession duration in hours for old IP in the original network when changing from the basic network to VPC or changing the VPC subnet. Value range: 0–168 hours. Default value: 24 hours."
      }
    ],
    "desc": "This API (ModifyDBInstanceVipVport) is used to modify the IP and port number of a TencentDB instance, switch from the basic network to VPC, or change VPC subnets."
  },
  "DescribeDBInstanceConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (DescribeDBInstanceConfig) is used to query the configuration information of a TencentDB instance, such as its synchronization mode and deployment mode."
  },
  "DescribeBackupTables": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "StartTime",
        "desc": "Start time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-07-12 10:29:20."
      },
      {
        "name": "DatabaseName",
        "desc": "Specified database name."
      },
      {
        "name": "SearchTable",
        "desc": "Prefix of the table to be queried."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset."
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Value range: 1-2,000."
      }
    ],
    "desc": "This API is used to query the backup tables of the specified database. It has been disused.\nAfter the legacy version becomes capable of full backup, if you want to download logical backup files by table, you need to use this API.\nThe new API (CreateBackup) can specify the table to be backed up when a logical backup file is created, which can be downloaded directly."
  },
  "DescribeProjectSecurityGroups": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "Project ID."
      }
    ],
    "desc": "This API (DescribeProjectSecurityGroups) is used to query the security group details of a project."
  },
  "DescribeSlowLogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Offset",
        "desc": "Offset. Minimum value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Value range: 1-100. Default value: 20."
      }
    ],
    "desc": "This API (DescribeSlowLogs) is used to query the slow logs of a TencentDB instance."
  },
  "ModifyParamTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID."
      },
      {
        "name": "Name",
        "desc": "Template name."
      },
      {
        "name": "Description",
        "desc": "Template description."
      },
      {
        "name": "ParamList",
        "desc": "List of parameters."
      }
    ],
    "desc": "This API (ModifyParamTemplate) is used to modify a parameter template."
  },
  "DescribeInstanceParams": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      }
    ],
    "desc": "This API (DescribeInstanceParams) is used to query the list of parameters for an instance."
  },
  "DescribeDeployGroupList": {
    "params": [
      {
        "name": "DeployGroupId",
        "desc": "ID of a placement group."
      },
      {
        "name": "DeployGroupName",
        "desc": "Name of a placement group."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to query the list of placement groups of a user. You can specify the placement group ID or name."
  },
  "StopDBImportJob": {
    "params": [
      {
        "name": "AsyncRequestId",
        "desc": "Async task request ID."
      }
    ],
    "desc": "This API (StopDBImportJob) is used to stop a data import task."
  },
  "CreateAccounts": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Accounts",
        "desc": "TencentDB account."
      },
      {
        "name": "Password",
        "desc": "Password of the new account"
      },
      {
        "name": "Description",
        "desc": "Remarks"
      }
    ],
    "desc": "This API (CreateAccounts) is used to create TencentDB accounts. The new account names, domain names, and passwords need to be specified, and account remarks can also be added."
  },
  "UpgradeDBInstanceEngineVersion": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      },
      {
        "name": "EngineVersion",
        "desc": "Version of master instance database engine. Value range: 5.6, 5.7"
      },
      {
        "name": "WaitSwitch",
        "desc": "Mode of switch to a new instance. Value range: 0 (switch immediately), 1 (switch within a time window). Default value: 0. If the value is 1, the switch process will be performed within a time window. Or, you can call the [switching to new instance API](https://cloud.tencent.com/document/product/236/15864) to trigger the process."
      }
    ],
    "desc": "This API (UpgradeDBInstanceEngineVersion) is used to upgrade the version of a TencentDB instance, which can be a master instance, disaster recovery instance, or read-only instance."
  },
  "DescribeInstanceParamRecords": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset."
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page."
      }
    ],
    "desc": "This API (DescribeInstanceParamRecords) is used to query the parameter modification records of an instance."
  },
  "DescribeBackupSummaries": {
    "params": [
      {
        "name": "Product",
        "desc": "TencentDB product type to be queried. Currently, only `mysql` is supported."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset."
      },
      {
        "name": "Limit",
        "desc": "Paginated query limit. Default value: 20."
      },
      {
        "name": "OrderBy",
        "desc": "Sorting criterion. Valid values: BackupVolume (backup capacity), DataBackupVolume (data backup capacity), BinlogBackupVolume (log backup capacity), AutoBackupVolume (automatic backup capacity), ManualBackupVolume (manual backup capacity)."
      },
      {
        "name": "OrderDirection",
        "desc": "Sorting order. Valid values: ASC (ascending), DESC (descending)."
      }
    ],
    "desc": "This API is used to query the statistics of backups. It will return the capacity used by backups at the instance level and the number and used capacity of data backups and log backups of each instance (all capacity values are in bytes)."
  },
  "DescribeParamTemplateInfo": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Parameter template ID."
      }
    ],
    "desc": "This API (DescribeParamTemplateInfo) is used to query parameter template details."
  },
  "DescribeBinlogBackupOverview": {
    "params": [
      {
        "name": "Product",
        "desc": "TencentDB product type to be queried. Currently, only `mysql` is supported."
      }
    ],
    "desc": "This API is used to query the log backup overview of a user in the current region."
  },
  "DeleteAccounts": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Accounts",
        "desc": "TencentDB account."
      }
    ],
    "desc": "This API (DeleteAccounts) is used to delete TencentDB accounts."
  },
  "DescribeDBInstanceInfo": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      }
    ],
    "desc": "This API is used to query the basic information of an instance (instance ID, instance name, and whether encryption is enabled)."
  },
  "DescribeRollbackRangeTime": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID list. An instance ID is in the format of cdb-c1nl9rpv, which is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (DescribeRollbackRangeTime) is used to query the time range available for instance rollback."
  },
  "DescribeParamTemplates": {
    "params": [],
    "desc": "This API (DescribeParamTemplates) is used to query the list of parameter templates"
  },
  "DeleteBackup": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "BackupId",
        "desc": "Backup task ID, which is the task ID returned by the [TencentDB instance backup creating API](https://cloud.tencent.com/document/api/236/15844)."
      }
    ],
    "desc": "This API is used to delete a database backup. It can only delete manually initiated backups."
  },
  "ModifyInstanceParam": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "List of short instance IDs."
      },
      {
        "name": "ParamList",
        "desc": "List of parameters to be modified. Every element is a combination of `Name` (parameter name) and `CurrentValue` (new value)."
      }
    ],
    "desc": "This API (ModifyInstanceParam) is used to modify instance parameters."
  },
  "DescribeAsyncRequestInfo": {
    "params": [
      {
        "name": "AsyncRequestId",
        "desc": "Async task request ID."
      }
    ],
    "desc": "This API (DescribeAsyncRequestInfo) is used to query the async task execution result of a TencentDB instance."
  },
  "DescribeDBZoneConfig": {
    "params": [],
    "desc": "This API (DescribeDBZoneConfig) is used to query the specifications of TencentDB instances purchasable in a region."
  },
  "DescribeDBInstanceRebootTime": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (DescribeDBInstanceRebootTime) is used to query the estimated time needed for a TencentDB instance to restart."
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "Project ID. You can use the [project list querying API](https://cloud.tencent.com/document/product/378/4400) to query the project ID."
      },
      {
        "name": "InstanceTypes",
        "desc": "Instance type. Value range: 1 (master), 2 (disaster recovery), 3 (read-only)."
      },
      {
        "name": "Vips",
        "desc": "Private IP address of the instance."
      },
      {
        "name": "Status",
        "desc": "Instance status. Value range: <br>0 - creating <br>1 - running <br>4 - isolating <br>5 - isolated (the instance can be restored and started in the recycle bin)"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned for a single request. Default value: 20. Maximum value: 2,000."
      },
      {
        "name": "SecurityGroupId",
        "desc": "Security group ID. When it is used as a filter, the `WithSecurityGroup` parameter should be set to 1."
      },
      {
        "name": "PayTypes",
        "desc": "Billing method. Value range: 0 (monthly subscribed), 1 (hourly)."
      },
      {
        "name": "InstanceNames",
        "desc": "Instance name."
      },
      {
        "name": "TaskStatus",
        "desc": "Instance task status. Value range: <br>0 - no task <br>1 - upgrading <br>2 - importing data <br>3 - activating slave <br>4 - public network access enabled <br>5 - batch operation in progress <br>6 - rolling back <br>7 - public network access not enabled <br>8 - modifying password <br>9 - renaming instance <br>10 - restarting <br>12 - migrating self-built instance <br>13 - dropping table <br>14 - creating and syncing disaster recovery instance <br>15 - pending upgrade and switch <br>16 - upgrade and switch in progress <br>17 - upgrade and switch completed"
      },
      {
        "name": "EngineVersions",
        "desc": "Version of the instance database engine. Value range: 5.1, 5.5, 5.6, 5.7."
      },
      {
        "name": "VpcIds",
        "desc": "VPC ID."
      },
      {
        "name": "ZoneIds",
        "desc": "AZ ID."
      },
      {
        "name": "SubnetIds",
        "desc": "Subnet ID."
      },
      {
        "name": "CdbErrors",
        "desc": "Lock flag."
      },
      {
        "name": "OrderBy",
        "desc": "Sort by field of the returned result set. Currently, supported values include \"InstanceId\", \"InstanceName\", \"CreateTime\", and \"DeadlineTime\"."
      },
      {
        "name": "OrderDirection",
        "desc": "Sorting method of the returned result set. Currently, \"ASC\" or \"DESC\" is supported."
      },
      {
        "name": "WithSecurityGroup",
        "desc": "Whether security group ID is used as a filter"
      },
      {
        "name": "WithExCluster",
        "desc": "Whether dedicated cluster details are included. Value range: 0 (not included), 1 (included)"
      },
      {
        "name": "ExClusterId",
        "desc": "Exclusive cluster ID."
      },
      {
        "name": "InstanceIds",
        "desc": "Instance ID."
      },
      {
        "name": "InitFlag",
        "desc": "Initialization flag. Value range: 0 (not initialized), 1 (initialized)."
      },
      {
        "name": "WithDr",
        "desc": "Whether instances corresponding to the disaster recovery relationship are included. Valid values: 0 (not included), 1 (included). Default value: 1. If a master instance is pulled, the data of the disaster recovery relationship will be in the `DrInfo` field. If a disaster recovery instance is pulled, the data of the disaster recovery relationship will be in the `MasterInfo` field. The disaster recovery relationship contains only partial basic data. To get the detailed data, you need to call an API to pull it."
      },
      {
        "name": "WithRo",
        "desc": "Whether read-only instances are included. Valid values: 0 (not included), 1 (included). Default value: 1."
      },
      {
        "name": "WithMaster",
        "desc": "Whether master instances are included. Valid values: 0 (not included), 1 (included). Default value: 1."
      },
      {
        "name": "DeployGroupIds",
        "desc": "Placement group ID list."
      }
    ],
    "desc": "This API (DescribeDBInstances) is used to query the list of TencentDB instances (which can be master, disaster recovery, or read-only instances). It supports filtering instances by project ID, instance ID, access address, and instance status."
  },
  "ModifyRoGroupInfo": {
    "params": [
      {
        "name": "RoGroupId",
        "desc": "RO group ID."
      },
      {
        "name": "RoGroupInfo",
        "desc": "RO group details."
      },
      {
        "name": "RoWeightValues",
        "desc": "Weights of instances in RO group. If the weighting mode of an RO group is changed to custom mode, this parameter must be set, and a weight value needs to be set for each RO instance."
      },
      {
        "name": "IsBalanceRoLoad",
        "desc": "Whether to rebalance the loads of RO instances in the RO group. Supported values include `1` (yes) and `0` (no). The default value is `0`. Please note that if this value is set to `1`, connections to the RO instances in the RO group will be interrupted transiently; therefore, you should ensure that your application can reconnect to the databases."
      }
    ],
    "desc": "This API is used to update the information of a TencentDB RO group, such as configuring an instance removal policy in case of excessive delay and setting read weights of RO instances."
  },
  "DescribeDBInstanceCharset": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      }
    ],
    "desc": "This API (DescribeDBInstanceCharset) is used to query the character set and its name of a TencentDB instance."
  },
  "AssociateSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "Security group ID."
      },
      {
        "name": "InstanceIds",
        "desc": "List of instance IDs, which is an array of one or more instance IDs."
      }
    ],
    "desc": "This API (AssociateSecurityGroups) is used to bind security groups to instances in batches."
  },
  "InitDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      },
      {
        "name": "NewPassword",
        "desc": "New password of the instance. Rule: It can only contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and special characters (!@#$%^*())."
      },
      {
        "name": "Parameters",
        "desc": "List of instance parameters. Currently, \"character_set_server\" and \"lower_case_table_names\" are supported, whose value ranges are [\"utf8\",\"latin1\",\"gbk\",\"utf8mb4\"] and [\"0\",\"1\"], respectively."
      },
      {
        "name": "Vport",
        "desc": "Instance port. Value range: [1024, 65535]."
      }
    ],
    "desc": "This API (InitDBInstances) is used to initialize instances, including their password, default character set, and instance port number."
  },
  "ModifyAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Accounts",
        "desc": "Database account, including username and domain name."
      },
      {
        "name": "GlobalPrivileges",
        "desc": "Global permission. Valid values: \"SELECT\", \"INSERT\", \"UPDATE\", \"DELETE\", \"CREATE\", \"PROCESS\", \"DROP\", \"REFERENCES\", \"INDEX\", \"ALTER\", \"SHOW DATABASES\", \"CREATE TEMPORARY TABLES\", \"LOCK TABLES\", \"EXECUTE\", \"CREATE VIEW\", \"SHOW VIEW\", \"CREATE ROUTINE\", \"ALTER ROUTINE\", \"EVENT\", \"TRIGGER\".\nNote: if this parameter is not passed in, it means to clear the permission."
      },
      {
        "name": "DatabasePrivileges",
        "desc": "Database permission. Valid values: \"SELECT\", \"INSERT\", \"UPDATE\", \"DELETE\", \"CREATE\", \t\"DROP\", \"REFERENCES\", \"INDEX\", \"ALTER\", \"CREATE TEMPORARY TABLES\", \"LOCK TABLES\", \"EXECUTE\", \"CREATE VIEW\", \"SHOW VIEW\", \"CREATE ROUTINE\", \"ALTER ROUTINE\", \"EVENT\", \"TRIGGER\".\nNote: if this parameter is not passed in, it means to clear the permission."
      },
      {
        "name": "TablePrivileges",
        "desc": "Table permission in the database. Valid values: \"SELECT\", \"INSERT\", \"UPDATE\", \"DELETE\", \"CREATE\", \t\"DROP\", \"REFERENCES\", \"INDEX\", \"ALTER\", \"CREATE VIEW\", \"SHOW VIEW\", \"TRIGGER\".\nNote: if this parameter is not passed in, it means to clear the permission."
      },
      {
        "name": "ColumnPrivileges",
        "desc": "Column permission in table. Valid values: \"SELECT\", \"INSERT\", \"UPDATE\", \"REFERENCES\".\nNote: if this parameter is not passed in, it means to clear the permission."
      }
    ],
    "desc": "This API is used to modify the permissions of a TencentDB instance account.\n\nNote that when modifying account permissions, you need to pass in the full permission information of the account. You can [query the account permission information\n](https://cloud.tencent.com/document/api/236/17500) first before modifying permissions."
  },
  "DescribeDBImportRecords": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "StartTime",
        "desc": "Start time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-01-01 00:00:01."
      },
      {
        "name": "EndTime",
        "desc": "End time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-01-01 23:59:59."
      },
      {
        "name": "Offset",
        "desc": "Pagination parameter indicating the offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Pagination parameter indicating the number of results to be returned for a single request. Value range: 1-100. Default value: 20."
      }
    ],
    "desc": "This API (DescribeDBImportRecords) is used to query the records of import tasks in a TencentDB instance."
  },
  "DescribeDBSwitchRecords": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset."
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Value range: 1-2,000. Default value: 50."
      }
    ],
    "desc": "This API (DescribeDBSwitchRecords) is used to query the instance switch records."
  },
  "CreateDBImportJob": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "FileName",
        "desc": "Filename. The file should have already been uploaded to Tencent Cloud."
      },
      {
        "name": "User",
        "desc": "TencentDB username"
      },
      {
        "name": "Password",
        "desc": "Password of a TencentDB instance user account"
      },
      {
        "name": "DbName",
        "desc": "Name of the target database. If this parameter is not passed in, no database is specified."
      }
    ],
    "desc": "This API (CreateDBImportJob) is used to create a data import task for a TencentDB instance.\n\nNote that the files for a data import task must be uploaded to Tencent Cloud in advance. You need to do so in the console."
  },
  "RestartDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Array of instance IDs in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (RestartDBInstances) is used to restart TencentDB instances.\n\nNote:\n1. This API only supports restarting master instances.\n2. The instance status must be normal, and no other async tasks are in progress."
  },
  "ModifyAccountPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "NewPassword",
        "desc": "New password of the database account. It can only contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and special characters (_+-&=!@#$%^*())."
      },
      {
        "name": "Accounts",
        "desc": "TencentDB account"
      }
    ],
    "desc": "This API (ModifyAccountPassword) is used to modify the password of a TencentDB instance account."
  },
  "DescribeUploadedFiles": {
    "params": [
      {
        "name": "Path",
        "desc": "File path. `OwnerUin` information of the root account should be entered in this field."
      },
      {
        "name": "Offset",
        "desc": "Record offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned for a single request. Default value: 20."
      }
    ],
    "desc": "This API is used to query the list of user-imported SQL files."
  },
  "ModifyAccountDescription": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Accounts",
        "desc": "TencentDB account"
      },
      {
        "name": "Description",
        "desc": "Database account remarks"
      }
    ],
    "desc": "This API (ModifyAccountDescription) is used to modify the remarks of a TencentDB instance account."
  },
  "DescribeSlowLogData": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "StartTime",
        "desc": "Start timestamp."
      },
      {
        "name": "EndTime",
        "desc": "End timestamp."
      },
      {
        "name": "UserHosts",
        "desc": "Client `Host` list."
      },
      {
        "name": "UserNames",
        "desc": "Client username list."
      },
      {
        "name": "DataBases",
        "desc": "Accessed database list."
      },
      {
        "name": "SortBy",
        "desc": "Sort by field. Valid values: Timestamp, QueryTime, LockTime, RowsExamined, RowsSent."
      },
      {
        "name": "OrderBy",
        "desc": "Sorting order. Valid values: ASC (ascending), DESC (descending)."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned at a time. Maximum value: 400."
      }
    ],
    "desc": "This API is used to search for slow logs of an instance by criteria. You can only view slow logs within a month."
  },
  "ModifyBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "ExpireDays",
        "desc": "Backup file retention period in days. Value range: 7-732."
      },
      {
        "name": "StartTime",
        "desc": "(This parameter will be disused. The `BackupTimeWindow` parameter is recommended.) Backup time range in the format of 02:00–06:00, with the start time and end time on the hour. Valid values: 00:00–12:00, 02:00–06:00, 06:00–10:00, 10:00–14:00, 14:00–18:00, 18:00–22:00, 22:00–02:00."
      },
      {
        "name": "BackupMethod",
        "desc": "Automatic backup mode. Only `physical` (physical cold backup) is supported"
      },
      {
        "name": "BinlogExpireDays",
        "desc": "Binlog retention period in days. Value range: 7-732. It cannot be greater than the retention period of backup files."
      },
      {
        "name": "BackupTimeWindow",
        "desc": "Backup time window; for example, to set up backup between 10:00 and 14:00 on every Tuesday and Sunday, you should set this parameter as follows: {\"Monday\": \"\", \"Tuesday\": \"10:00-14:00\", \"Wednesday\": \"\", \"Thursday\": \"\", \"Friday\": \"\", \"Saturday\": \"\", \"Sunday\": \"10:00-14:00\"} (Note: You can set up backup on different days, but the backup time windows need to be the same. If this field is set, the `StartTime` field will be ignored)"
      }
    ],
    "desc": "This API (ModifyBackupConfig) is used to modify the database backup configuration."
  },
  "ModifyDBInstanceProject": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Array of instance IDs in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      },
      {
        "name": "NewProjectId",
        "desc": "Project ID."
      }
    ],
    "desc": "This API (ModifyDBInstanceProject) is used to modify the project to which a TencentDB instance belongs."
  },
  "DescribeBackupDatabases": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "StartTime",
        "desc": "Start time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-07-12 10:29:20."
      },
      {
        "name": "SearchDatabase",
        "desc": "Prefix of the database to be queried."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset."
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Value range: 1-2,000."
      }
    ],
    "desc": "This API is used to query the databases contained in a backup file. It has been disused.\nAfter the legacy version becomes capable of full backup, if you want to download logical backup files by table, you need to use this API.\nThe new API (CreateBackup) can specify the table to be backed up when a logical backup file is created, which can be downloaded directly."
  },
  "ModifyAutoRenewFlag": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "AutoRenew",
        "desc": "Auto-renewal flag. Value range: 0 (auto-renewal not enabled), 1 (auto-renewal enabled)."
      }
    ],
    "desc": "This API is used to modify the auto-renewal flag of a TencentDB instance."
  },
  "StartBatchRollback": {
    "params": [
      {
        "name": "Instances",
        "desc": "Details of the instance for rollback"
      }
    ],
    "desc": "This API (StartBatchRollback) is used to roll back the tables of a TencentDB instance in batches."
  },
  "DescribeDeviceMonitorInfo": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Count",
        "desc": "This parameter is used to return the monitoring data of Count 5-minute time periods on the day. Value range: 1-288. If this parameter is not passed in, all monitoring data in a 5-minute granularity on the day will be returned by default."
      }
    ],
    "desc": "This API (DescribeDeviceMonitorInfo) is used to query the monitoring information of a TencentDB physical machine on the day. Currently, it only supports instances with 488 GB memory and 6 TB disk."
  },
  "OpenWanService": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://cloud.tencent.com/document/api/236/15872) to query the ID, whose value is the `InstanceId` value in output parameters."
      }
    ],
    "desc": "This API (OpenWanService) is used to enable public network access for an instance.\n\nNote that before enabling public network access, you need to first [initialize the instance](https://cloud.tencent.com/document/api/236/15873)."
  },
  "DescribeSupportedPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (DescribeSupportedPrivileges) is used to query the information of TencentDB account permissions, including global permissions, database permissions, table permissions, and column permissions."
  },
  "DescribeBinlogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      },
      {
        "name": "Offset",
        "desc": "Offset. Minimum value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Value range: 1-100. Default value: 20."
      }
    ],
    "desc": "This API is used to query the list of binlog files of a TencentDB instance."
  },
  "DescribeDBSecurityGroups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API (DescribeDBSecurityGroups) is used to query the security group details of an instance."
  },
  "DescribeRoGroups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `cdb-c1nl9rpv` or `cdb-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page."
      }
    ],
    "desc": "This API is used to query the information of all RO groups of a TencentDB instance."
  },
  "ModifyNameOrDescByDpId": {
    "params": [
      {
        "name": "DeployGroupId",
        "desc": "ID of a placement group."
      },
      {
        "name": "DeployGroupName",
        "desc": "Name of a placement group, which can contain up to 60 characters. The placement group name and description cannot both be empty."
      },
      {
        "name": "Description",
        "desc": "Description of a placement group, which can contain up to 200 characters. The placement group name and description cannot both be empty."
      }
    ],
    "desc": "This API is used to modify the name or description of a placement group."
  },
  "UpgradeDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of `cdb-c1nl9rpv` or `cdbro-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [DescribeDBInstances](https://cloud.tencent.com/document/api/236/15872) API to query the ID, whose value is the `InstanceId` value in output parameters."
      },
      {
        "name": "Memory",
        "desc": "Memory size in MB after upgrade. To ensure that the `Memory` value to be passed in is valid, please use the [DescribeDBZoneConfig](https://cloud.tencent.com/document/product/236/17229) API to query the specifications of the memory that can be upgraded to."
      },
      {
        "name": "Volume",
        "desc": "Disk size in GB after upgrade. To ensure that the `Volume` value to be passed in is valid, please use the [DescribeDBZoneConfig](https://cloud.tencent.com/document/product/236/17229) API to query the specifications of the disk that can be upgraded to."
      },
      {
        "name": "ProtectMode",
        "desc": "Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync). This parameter can be specified when upgrading master instances and is meaningless for read-only or disaster recovery instances."
      },
      {
        "name": "DeployMode",
        "desc": "Deployment mode. Valid values: 0 (single-AZ), 1 (multi-AZ). Default value: 0. This parameter can be specified when upgrading master instances and is meaningless for read-only or disaster recovery instances."
      },
      {
        "name": "SlaveZone",
        "desc": "AZ information of slave database 1, which is the `Zone` value of the instance by default. This parameter can be specified when upgrading master instances in multi-AZ mode and is meaningless for read-only or disaster recovery instances. You can use the [DescribeDBZoneConfig](https://cloud.tencent.com/document/product/236/17229) API to query the supported AZs."
      },
      {
        "name": "EngineVersion",
        "desc": "Version of master instance database engine. Valid values: 5.5, 5.6, 5.7."
      },
      {
        "name": "WaitSwitch",
        "desc": "Mode of switch to new instance. Valid values: 0 (switch immediately), 1 (switch within a time window). Default value: 0. If the value is 1, the switch process will be performed within a time window. Or, you can call the [SwitchForUpgrade](https://cloud.tencent.com/document/product/236/15864) API to trigger the process."
      },
      {
        "name": "BackupZone",
        "desc": "AZ information of slave database 2, which is empty by default. This parameter can be specified when upgrading master instances and is meaningless for read-only or disaster recovery instances."
      },
      {
        "name": "InstanceRole",
        "desc": "Instance type. Valid values: master (master instance), dr (disaster recovery instance), ro (read-only instance). Default value: master."
      }
    ],
    "desc": "This API is used to upgrade or downgrade a TencentDB instance, which can be a master instance, disaster recovery instance, or read-only instance."
  },
  "CreateDeployGroup": {
    "params": [
      {
        "name": "DeployGroupName",
        "desc": "Name of a placement group, which can contain up to 60 characters."
      },
      {
        "name": "Description",
        "desc": "Description of a placement group, which can contain up to 200 characters."
      },
      {
        "name": "Affinity",
        "desc": "Affinity policy of placement group. Currently, the value of this parameter can only be 1. Policy 1 indicates the upper limit of instances on one physical machine."
      },
      {
        "name": "LimitNum",
        "desc": "Upper limit of instances on one physical machine as defined in affinity policy 1 of placement group."
      },
      {
        "name": "DevClass",
        "desc": "Model attribute of placement group. Valid values: SH12+SH02, TS85."
      }
    ],
    "desc": "This API is used to create a placement group for placing instances."
  },
  "CreateParamTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Parameter template name."
      },
      {
        "name": "Description",
        "desc": "Parameter template description."
      },
      {
        "name": "EngineVersion",
        "desc": "MySQL version number."
      },
      {
        "name": "TemplateId",
        "desc": "Source parameter template ID."
      },
      {
        "name": "ParamList",
        "desc": "List of parameters."
      }
    ],
    "desc": "This API (CreateParamTemplate) is used to create a parameter template."
  }
}