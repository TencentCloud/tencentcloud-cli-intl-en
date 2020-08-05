# -*- coding: utf-8 -*-
DESC = "redis-2018-04-12"
INFO = {
  "ClearInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Password",
        "desc": "Redis instance password (this parameter is not required for password-free instances but for password-enabled instances)"
      }
    ],
    "desc": "This API is used to clear the data of a Redis instance."
  },
  "DescribeInstanceMonitorBigKeySizeDist": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Date",
        "desc": "Time, such as \"20190219\""
      }
    ],
    "desc": "This API is used to query the big key size distribution of an instance."
  },
  "CreateInstanceAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "AccountName",
        "desc": "Sub-account name"
      },
      {
        "name": "AccountPassword",
        "desc": "Sub-account password"
      },
      {
        "name": "ReadonlyPolicy",
        "desc": "Routing policy. Enter `master` for primary node or `replication` for secondary node"
      },
      {
        "name": "Privilege",
        "desc": "Read/write policy. Valid values: r (read-only), rw (read/write)."
      },
      {
        "name": "Remark",
        "desc": "Sub-account description information"
      }
    ],
    "desc": "This API is used to create an instance sub-account."
  },
  "ModifyInstanceAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "AccountName",
        "desc": "Sub-account name. If the root account is to be modified, enter `root`"
      },
      {
        "name": "AccountPassword",
        "desc": "Sub-account password"
      },
      {
        "name": "Remark",
        "desc": "Sub-account description information"
      },
      {
        "name": "ReadonlyPolicy",
        "desc": "Sub-account routing policy. Enter `master` to route to the primary node or `slave` to route to the secondary node"
      },
      {
        "name": "Privilege",
        "desc": "Sub-account read/write policy. Enter `r` for read-only, `w` for write-only, or `rw` for read/write"
      },
      {
        "name": "NoAuth",
        "desc": "true: make the root account password-free. This is applicable to root accounts only; sub-accounts cannot be made password-free"
      }
    ],
    "desc": "This API is used to modify an instance sub-account."
  },
  "DescribeTaskList": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "InstanceName",
        "desc": "Instance name"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page"
      },
      {
        "name": "Offset",
        "desc": "Offset, which is an integral multiple of `Limit` (rounded down automatically)"
      },
      {
        "name": "ProjectIds",
        "desc": "Project ID"
      },
      {
        "name": "TaskTypes",
        "desc": "Task type"
      },
      {
        "name": "BeginTime",
        "desc": "Start time"
      },
      {
        "name": "EndTime",
        "desc": "End time"
      },
      {
        "name": "TaskStatus",
        "desc": "Task status"
      }
    ],
    "desc": "This API is used to query the list of tasks."
  },
  "CleanUpInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to deactivate an instance in the recycle bin immediately."
  },
  "StartupInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to deisolate an instance."
  },
  "DescribeInstanceAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page"
      },
      {
        "name": "Offset",
        "desc": "Page offset"
      }
    ],
    "desc": "This API is used to view instance sub-account information."
  },
  "DescribeInstanceDTSInfo": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to query the DTS task details of an instance."
  },
  "DescribeInstanceMonitorTopNCmdTook": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "SpanType",
        "desc": "Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours"
      }
    ],
    "desc": "This API is used to query the instance CPU time."
  },
  "ModifyNetworkConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Operation",
        "desc": "Operation type. changeVip: modify the VIP of an instance; changeVpc: modify the subnet of an instance; changeBaseToVpc: change from basic network to VPC"
      },
      {
        "name": "Vip",
        "desc": "VIP address, which is required for the `changeVip` operation. If this parameter is left blank, a random one will be assigned by default"
      },
      {
        "name": "VpcId",
        "desc": "VPC ID, which is required for `changeVpc` and `changeBaseToVpc` operations"
      },
      {
        "name": "SubnetId",
        "desc": "Subnet ID, which is required for `changeVpc` and `changeBaseToVpc` operations"
      }
    ],
    "desc": "This API is used to modify the network configuration of an instance."
  },
  "ResetPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Redis instance ID"
      },
      {
        "name": "Password",
        "desc": "Password reset (this parameter can be left blank when switching to password-free instance mode and is required in other cases)"
      },
      {
        "name": "NoAuth",
        "desc": "Whether to switch to password-free instance mode. false: switch to password-enabled instance mode; true: switch to password-free instance mode. Default value: false"
      }
    ],
    "desc": "This API is used to reset a password."
  },
  "DestroyPrepaidInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to return a monthly subscribed instance."
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "Limit",
        "desc": "Instance list size. Default value: 20"
      },
      {
        "name": "Offset",
        "desc": "Offset, which is an integral multiple of `Limit`"
      },
      {
        "name": "InstanceId",
        "desc": "Instance ID, such as crs-6ubhgouj"
      },
      {
        "name": "OrderBy",
        "desc": "Enumerated values: projectId, createtime, instancename, type, curDeadline"
      },
      {
        "name": "OrderType",
        "desc": "1: reverse; 0: sequential; reverse by default"
      },
      {
        "name": "VpcIds",
        "desc": "Array of VPC IDs such as 47525. The array subscript starts from 0. If this parameter is not passed in, the basic network will be selected by default"
      },
      {
        "name": "SubnetIds",
        "desc": "Array of subnet IDs such as 56854. The array subscript starts from 0"
      },
      {
        "name": "ProjectIds",
        "desc": "Array of project IDs. The array subscript starts from 0"
      },
      {
        "name": "SearchKey",
        "desc": "ID of the instance to be searched for."
      },
      {
        "name": "InstanceName",
        "desc": "Instance name"
      },
      {
        "name": "UniqVpcIds",
        "desc": "Array of VPC IDs such as vpc-sad23jfdfk. The array subscript starts from 0. If this parameter is not passed in, the basic network will be selected by default"
      },
      {
        "name": "UniqSubnetIds",
        "desc": "Array of subnet IDs such as subnet-fdj24n34j2. The array subscript starts from 0"
      },
      {
        "name": "RegionIds",
        "desc": "Region ID, which has already been disused. The corresponding region can be queried through the common parameter `Region`"
      },
      {
        "name": "Status",
        "desc": "Instance status. 0: to be initialized; 1: in process; 2: running; -2: isolated; -3: to be deleted"
      },
      {
        "name": "TypeVersion",
        "desc": "Type edition. 1: standalone edition; 2: primary-secondary edition; 3: cluster edition"
      },
      {
        "name": "EngineName",
        "desc": "Engine information: Redis-2.8, Redis-4.0, CKV"
      },
      {
        "name": "AutoRenew",
        "desc": "Renewal mode. 0: default status (manual renewal); 1: auto-renewal enabled; 2: auto-renewal disabled"
      },
      {
        "name": "BillingMode",
        "desc": "Billing method. postpaid: pay-as-you-go; prepaid: monthly subscription"
      },
      {
        "name": "Type",
        "desc": "Instance type. 1: legacy Redis Cluster Edition, 2: Redis 2.8 Master-Slave Edition, 3: CKV Master-Slave Edition, 4: CKV Cluster Edition, 5: Redis 2.8 Standalone Edition, 6: Redis 4.0 Master-Slave Edition, 7: Redis 4.0 Cluster Edition, 8: Redis 5.0 Master-Slave Edition, 9: Redis 5.0 Cluster Edition,"
      },
      {
        "name": "SearchKeys",
        "desc": "Search keywords, which can be instance ID, instance name, or complete IP"
      },
      {
        "name": "TypeList",
        "desc": "Internal parameter, which can be ignored"
      }
    ],
    "desc": "This API is used to query the list of Redis instances."
  },
  "DescribeInstanceParamRecords": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page"
      },
      {
        "name": "Offset",
        "desc": "Offset, which is an integral multiple of `Limit`"
      }
    ],
    "desc": "This API is used to query the list of parameter modifications."
  },
  "DescribeInstanceMonitorTopNCmd": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "SpanType",
        "desc": "Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours"
      }
    ],
    "desc": "This API is used to query an instance access command."
  },
  "DisableReplicaReadonly": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Serial ID of an instance"
      }
    ],
    "desc": "This API is used to disable read/write separation."
  },
  "DescribeAutoBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to get the backup configuration."
  },
  "ModifyAutoBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "WeekDays",
        "desc": "Date. Value range: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
      },
      {
        "name": "TimePeriod",
        "desc": "Time period. Value range: 00:00-01:00, 01:00-02:00...... 23:00-00:00"
      },
      {
        "name": "AutoBackupType",
        "desc": "Auto backup type: 1 \"scheduled rollback\""
      }
    ],
    "desc": "This API is used to set an auto-backup schedule."
  },
  "DescribeInstanceMonitorSIP": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to query the access source information of an instance."
  },
  "DescribeInstanceParams": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to query the list of instance parameters."
  },
  "DescribeProjectSecurityGroup": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "0: default project; -1: all projects; >0: specified project"
      },
      {
        "name": "SecurityGroupId",
        "desc": "Security group ID"
      }
    ],
    "desc": "This API is used to query the security group information of a project."
  },
  "DescribeInstanceShards": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "FilterSlave",
        "desc": "Whether to filter out the secondary node information"
      }
    ],
    "desc": "This API is used to get the information of cluster edition instance shards."
  },
  "DescribeTaskInfo": {
    "params": [
      {
        "name": "TaskId",
        "desc": "Task ID"
      }
    ],
    "desc": "This API is used to query a task result."
  },
  "DescribeInstanceDealDetail": {
    "params": [
      {
        "name": "DealIds",
        "desc": "Array of order IDs"
      }
    ],
    "desc": "This API is used to query the order information."
  },
  "EnableReplicaReadonly": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Serial ID of an instance"
      },
      {
        "name": "ReadonlyPolicy",
        "desc": "Account routing policy. If `master` or `replication` is entered, it means to route to the primary or secondary node; if this is left blank, it means to write into the primary node and read from the secondary node by default"
      }
    ],
    "desc": "This API is used to enable read/write separation."
  },
  "DescribeProjectSecurityGroups": {
    "params": [
      {
        "name": "Product",
        "desc": "Database engine name: mariadb, cdb, cynosdb, dcdb, redis, mongodb."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID."
      },
      {
        "name": "Offset",
        "desc": "Offset."
      },
      {
        "name": "Limit",
        "desc": "The number of security groups to be pulled."
      },
      {
        "name": "SearchKey",
        "desc": "Search criteria. You can enter a security group ID or name."
      }
    ],
    "desc": "This API is used to query the security group details of a project."
  },
  "AssociateSecurityGroups": {
    "params": [
      {
        "name": "Product",
        "desc": "Database engine name: mariadb, cdb, cynosdb, dcdb, redis, mongodb, etc."
      },
      {
        "name": "SecurityGroupId",
        "desc": "ID of the security group to be associated in the format of sg-efil73jd."
      },
      {
        "name": "InstanceIds",
        "desc": "ID(s) of the instance(s) to be associated in the format of ins-lesecurk. You can specify multiple instances."
      }
    ],
    "desc": "This API is used to associate security groups with specified instances."
  },
  "ModifyDBInstanceSecurityGroups": {
    "params": [
      {
        "name": "Product",
        "desc": "Database engine name: mariadb, cdb, cynosdb, dcdb, redis, mongodb, etc."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "The ID list of the security groups to be modified, which is an array of one or more security group IDs."
      },
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB Console."
      }
    ],
    "desc": "This API is used to modify the security groups associated with an instance."
  },
  "DeleteInstanceAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "AccountName",
        "desc": "Sub-account name"
      }
    ],
    "desc": "This API is used to delete an instance sub-account."
  },
  "DescribeInstanceMonitorBigKey": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "ReqType",
        "desc": "Request type. 1: string type; 2: all types"
      },
      {
        "name": "Date",
        "desc": "Time, such as \"20190219\""
      }
    ],
    "desc": "This API is used to query the big key of an instance."
  },
  "DescribeInstanceSecurityGroup": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance list"
      }
    ],
    "desc": "This API is used to query the security group information of an instance."
  },
  "DescribeInstanceMonitorBigKeyTypeDist": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Date",
        "desc": "Time, such as \"20190219\""
      }
    ],
    "desc": "This API is used to query the big key type distribution of an instance"
  },
  "DescribeProductInfo": {
    "params": [],
    "desc": "This API is used to query the purchasable capacity specifications of Redis instances in the specified AZ and instance type. If you are not in the allowlist for the AZ or instance type, you cannot view the details of the capacity specifications. To apply for the eligibility, please submit a ticket."
  },
  "UpgradeInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "MemSize",
        "desc": "Shard size in MB"
      },
      {
        "name": "RedisShardNum",
        "desc": "Number of shards. This parameter can be left blank for Redis 2.8 primary-secondary edition, CKV primary-secondary edition, and Redis 2.8 standalone edition"
      },
      {
        "name": "RedisReplicasNum",
        "desc": "Number of replicas. This parameter can be left blank for Redis 2.8 primary-secondary edition, CKV primary-secondary edition, and Redis 2.8 standalone edition"
      }
    ],
    "desc": "This API is used to upgrade an instance."
  },
  "DescribeInstanceMonitorHotKey": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "SpanType",
        "desc": "Time span. 1: real time; 2: past 30 minutes; 3: past 6 hours; 4: past 24 hours"
      }
    ],
    "desc": "This API is used to query the hot key of an instance."
  },
  "ManualBackupInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ID of the instance to be operated on, which can be obtained through the `InstanceId` field in the return value of the DescribeInstance API."
      },
      {
        "name": "Remark",
        "desc": "Backup remarks"
      }
    ],
    "desc": "This API is used to manually back up a Redis instance."
  },
  "ModfiyInstancePassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "OldPassword",
        "desc": "Old password of an instance"
      },
      {
        "name": "Password",
        "desc": "New password of an instance"
      }
    ],
    "desc": "This API is used to change the Redis password."
  },
  "DescribeDBSecurityGroups": {
    "params": [
      {
        "name": "Product",
        "desc": "Database engine name: mariadb, cdb, cynosdb, dcdb, redis, mongodb, etc."
      },
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB Console."
      }
    ],
    "desc": "This API is used to query the security group details of an instance."
  },
  "DescribeSlowLog": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "BeginTime",
        "desc": "Start time"
      },
      {
        "name": "EndTime",
        "desc": "End time"
      },
      {
        "name": "MinQueryTime",
        "desc": "Slow log threshold in microseconds"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page"
      },
      {
        "name": "Offset",
        "desc": "Offset, which is an integral multiple of `Limit`"
      }
    ],
    "desc": "This API is used to query the slow log."
  },
  "RestoreInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ID of the instance to be operated on, which can be obtained through the `redisId` field in the return value of the DescribeRedis API."
      },
      {
        "name": "BackupId",
        "desc": "Backup ID, which can be obtained through the `backupId` field in the return value of the GetRedisBackupList API"
      },
      {
        "name": "Password",
        "desc": "Instance password, which needs to be validated during instance restoration (this parameter is not required for password-free instances)"
      }
    ],
    "desc": "This API is used to restore a Redis instance."
  },
  "ModifyInstanceParams": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "InstanceParams",
        "desc": "List of instance parameters modified"
      }
    ],
    "desc": "This API is used to modify instance parameters."
  },
  "CreateInstances": {
    "params": [
      {
        "name": "ZoneId",
        "desc": "AZ ID of instance"
      },
      {
        "name": "TypeId",
        "desc": "Instance type. Valid values: 2 (Redis 2.8 memory edition in standard architecture), 3 (Redis 3.2 memory edition in standard architecture), 4 (CKV 3.2 memory edition in standard architecture), 6 (Redis 4.0 memory edition in standard architecture), 7 (Redis 4.0 memory edition in cluster architecture), 8 (Redis 5.0 memory edition in standard architecture), 9 (Redis 5.0 memory edition in cluster architecture)."
      },
      {
        "name": "MemSize",
        "desc": "Instance capacity in MB. The actual value is subject to the specifications returned by the purchasable specification querying API |"
      },
      {
        "name": "GoodsNum",
        "desc": "Number of instances. The actual quantity purchasable at a time is subject to the specifications returned by the purchasable specification querying API"
      },
      {
        "name": "Period",
        "desc": "Length of purchase in months, which is required when creating a monthly subscribed instances. Value range: [1,2,3,4,5,6,7,8,9,10,11,12,24,36]. For pay-as-you-go instances, enter 1"
      },
      {
        "name": "BillingMode",
        "desc": "Billing method. 0: pay as you go"
      },
      {
        "name": "Password",
        "desc": "Instance password. It can contain 8-30 characters and must contain at least two of the following types of characters: lowercase letters, uppercase letters, digits, and special symbols (()`~!@#$%^&*-+=_|{}[]:;<>,.?/). It cannot stat with the symbol (/)."
      },
      {
        "name": "VpcId",
        "desc": "VPC ID such as vpc-sad23jfdfk. If this parameter is not passed in, the basic network will be selected by default. Please use the VPC list querying API to query."
      },
      {
        "name": "SubnetId",
        "desc": "In a basic network, subnetId is invalid. In a VPC subnet, the value is the subnet ID, such as subnet-fdj24n34j2"
      },
      {
        "name": "ProjectId",
        "desc": "Project ID. The value is subject to the projectId returned by user account > user account-related querying APIs > project list"
      },
      {
        "name": "AutoRenew",
        "desc": "Auto-renewal flag. 0: default status (manual renewal); 1: auto-renewal enabled; 2: auto-renewal disabled"
      },
      {
        "name": "SecurityGroupIdList",
        "desc": "Array of security group IDs"
      },
      {
        "name": "VPort",
        "desc": "User-defined port. If this parameter is left empty, 6379 will be used by default. Value range: [1024,65535]"
      },
      {
        "name": "RedisShardNum",
        "desc": "Number of shards in an instance. This parameter is required for cluster edition instances. Valid values: 3, 5, 8, 12, 16, 24, 32, 64, 96, 128."
      },
      {
        "name": "RedisReplicasNum",
        "desc": "Number of replicas in an instance. Redis 2.8 standard edition and CKV standard edition support 1 replica. Standard/cluster edition 4.0 and 5.0 support 1-5 replicas."
      },
      {
        "name": "ReplicasReadonly",
        "desc": "Whether to support read-only replicas. Neither Redis 2.8 standard edition nor CKV standard edition supports read-only replicas. Read/write separation will be automatically enabled for an instance after it enables read-only replicas. Write requests will be directed to the primary node and read requests will be distributed on secondary nodes. To enable read-only replicas, we recommend you create 2 or more replicas."
      },
      {
        "name": "InstanceName",
        "desc": "Instance name. It contains only letters, digits, underscores, and dashes with a length of up to 60 characters."
      },
      {
        "name": "NoAuth",
        "desc": "Whether to support the password-free feature. Valid values: true (password-free instance), false (password-enabled instance). Default value: false. Only instances in a VPC support the password-free access."
      }
    ],
    "desc": "This API is used to create a Redis instance."
  },
  "DescribeBackupUrl": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "BackupId",
        "desc": "Backup ID, which can be queried through the `DescribeInstanceBackups` API"
      }
    ],
    "desc": "This API is used to query the download address of a backup RDB (it is during beta test and can be used only after you apply for the eligibility)."
  },
  "DestroyPostpaidInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to terminate a pay-as-you-go instance."
  },
  "DescribeInstanceBackups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ID of the instance to be operated on, which can be obtained through the `InstanceId` field in the return value of the DescribeInstance API."
      },
      {
        "name": "Limit",
        "desc": "Instance list size. Default value: 20"
      },
      {
        "name": "Offset",
        "desc": "Offset, which is an integral multiple of `Limit`"
      },
      {
        "name": "BeginTime",
        "desc": "Start time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-02-08 16:46:34. This parameter is used to query the list of instance backups started during the [beginTime, endTime] range."
      },
      {
        "name": "EndTime",
        "desc": "End time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-02-08 19:09:26. This parameter is used to query the list of instance backups started during the [beginTime, endTime] range."
      },
      {
        "name": "Status",
        "desc": "1: backup in process; 2: backing up normally; 3: converting from backup to RDB file; 4: RDB conversion completed; -1: backup expired; -2: backup deleted."
      }
    ],
    "desc": "This API is used to query the list of Redis instance backups."
  },
  "DisassociateSecurityGroups": {
    "params": [
      {
        "name": "Product",
        "desc": "Database engine name: mariadb, cdb, cynosdb, dcdb, redis, mongodb, etc."
      },
      {
        "name": "SecurityGroupId",
        "desc": "Security group ID."
      },
      {
        "name": "InstanceIds",
        "desc": "Instance ID list, which is an array of one or more instance IDs."
      }
    ],
    "desc": "This API is used to unassociate security groups from instances in batches."
  },
  "RenewInstance": {
    "params": [
      {
        "name": "Period",
        "desc": "Length of purchase in months"
      },
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to renew an instance."
  },
  "ModifyInstance": {
    "params": [
      {
        "name": "Operation",
        "desc": "Instance modification type. rename: rename an instance; modifyProject: modify the project of an instance; modifyAutoRenew: modify the auto-renewal flag of an instance"
      },
      {
        "name": "InstanceIds",
        "desc": "Instance ID"
      },
      {
        "name": "InstanceNames",
        "desc": "New name of instance"
      },
      {
        "name": "ProjectId",
        "desc": "Project ID"
      },
      {
        "name": "AutoRenews",
        "desc": "Auto-renewal flag. 0: default status (manual renewal), 1: auto-renewal enabled, 2: auto-renewal disabled"
      },
      {
        "name": "InstanceId",
        "desc": "Disused"
      },
      {
        "name": "InstanceName",
        "desc": "Disused"
      },
      {
        "name": "AutoRenew",
        "desc": "Disused"
      }
    ],
    "desc": "This API is used to modify instance information."
  },
  "DescribeInstanceMonitorTookDist": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Date",
        "desc": "Time, such as \"20190219\""
      },
      {
        "name": "SpanType",
        "desc": "Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours"
      }
    ],
    "desc": "This API is used to query the distribution of instance access duration."
  },
  "SwitchInstanceVip": {
    "params": [
      {
        "name": "SrcInstanceId",
        "desc": "Source instance ID."
      },
      {
        "name": "DstInstanceId",
        "desc": "Target instance ID."
      },
      {
        "name": "TimeDelay",
        "desc": "The time that lapses in seconds since DTS is disconnected between the source instance and the target instance. If the DTS disconnection time period is greater than `TimeDelay`, the VIP will not be switched. We recommend setting an acceptable value based on the actual business conditions."
      },
      {
        "name": "ForceSwitch",
        "desc": "Whether to force the switch when DTS is disconnected. Valid values: 1 (yes), 0 (no)."
      },
      {
        "name": "SwitchTime",
        "desc": "Valid values: now (switch now), syncComplete (switch after sync is completed)."
      }
    ],
    "desc": "This API is used to swap the VIPs of instances for instance disaster recovery switch in scenarios where cross-AZ disaster recovery is supported through DTS. After the VIPs of the source and target instances are swapped, the target instance can be written into and the DTS sync task between them will be disconnected."
  }
}