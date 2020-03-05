# -*- coding: utf-8 -*-
DESC = "mongodb-2019-07-25"
INFO = {
  "AssignProject": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "List of instance IDs in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page"
      },
      {
        "name": "ProjectId",
        "desc": "Project ID"
      }
    ],
    "desc": "This API is used to specify the project to which a TencentDB instance belongs.\n"
  },
  "ModifyDBInstanceSpec": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page"
      },
      {
        "name": "Memory",
        "desc": "Memory size after instance configuration change in GB. Memory and disk must be upgraded or degraded simultaneously"
      },
      {
        "name": "Volume",
        "desc": "Disk size after instance configuration change in GB. Memory and disk must be upgraded or degraded simultaneously. For degradation, the new disk capacity must be greater than 1.2 times the used disk capacity"
      },
      {
        "name": "OplogSize",
        "desc": "Oplog size after instance configuration change in GB, which ranges from 10% to 90% of the disk capacity and is 10% of the disk capacity by default"
      }
    ],
    "desc": "This API is used to adjust the specification configuration of a TencentDB for MongoDB. The purchasable specifications supported by the API can be obtained through the DescribeSpecInfo API."
  },
  "OfflineIsolatedDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page"
      }
    ],
    "desc": "This API is used to deactivate isolated TencentDB instances immediately. The instances must be in isolated status."
  },
  "DescribeClientConnections": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page"
      }
    ],
    "desc": "This API is used to query the client connection information of an instance, including the IP and number of connections. Currently, only instances of MongoDB 3.2 are supported."
  },
  "CreateDBInstanceHour": {
    "params": [
      {
        "name": "Memory",
        "desc": "Instance memory size in GB"
      },
      {
        "name": "Volume",
        "desc": "Instance disk size in GB"
      },
      {
        "name": "ReplicateSetNum",
        "desc": "Number of replica sets. When a replica set instance is created, this parameter must be set to 1. When a sharding instance is created, please see the parameters returned by the DescribeSpecInfo API"
      },
      {
        "name": "NodeNum",
        "desc": "Number of nodes in each replica set. Currently, the number of nodes in a replica set is fixed at 3, while the number of shards is customizable. For more information, please see the parameter returned by the DescribeSpecInfo API"
      },
      {
        "name": "MongoVersion",
        "desc": "Version number. For the specific purchasable versions supported, please see the return result of the DescribeSpecInfo API. The correspondences between parameters and versions are as follows: MONGO_3_WT: MongoDB 3.2 WiredTiger Edition; MONGO_3_ROCKS: MongoDB 3.2 RocksDB Edition; MONGO_36_WT: MongoDB 3.6 WiredTiger Edition"
      },
      {
        "name": "MachineCode",
        "desc": "Server type. HIO: high IO; HIO10G: 10-Gigabit high IO"
      },
      {
        "name": "GoodsNum",
        "desc": "Number of instances. Minimum value: 1. Maximum value: 10"
      },
      {
        "name": "Zone",
        "desc": "AZ information in the format of ap-guangzhou-2"
      },
      {
        "name": "ClusterType",
        "desc": "Instance type. REPLSET: replica set; SHARD: sharding cluster"
      },
      {
        "name": "VpcId",
        "desc": "VPC ID. If this parameter is not set, the basic network will be selected by default"
      },
      {
        "name": "SubnetId",
        "desc": "VPC subnet ID. If VpcId is set, then SubnetId will be required"
      },
      {
        "name": "Password",
        "desc": "Instance password. If this parameter is not set, you need to set an instance password through the password setting API after creating an instance. The password can only contain 8–16 characters and must contain at least two of the following types of characters: letters, digits, and special characters `!@#%^*()` |"
      },
      {
        "name": "ProjectId",
        "desc": "Project ID. If this parameter is not set, the default project will be used"
      },
      {
        "name": "Tags",
        "desc": "Instance tag information"
      }
    ],
    "desc": "This API is used to create a pay-as-you-go TencentDB for MongoDB instance."
  },
  "RenameInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page"
      },
      {
        "name": "NewName",
        "desc": "Instance name"
      }
    ],
    "desc": "This API is used to rename a TencentDB instance."
  },
  "DescribeSpecInfo": {
    "params": [
      {
        "name": "Zone",
        "desc": "AZ to be queried"
      }
    ],
    "desc": "This API is used to query the purchasable instance specifications."
  },
  "DescribeDBBackups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page"
      }
    ],
    "desc": "This API is used to query the list of instance backups. Currently, only backups in the last 7 days can be queried."
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "List of instance IDs in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page"
      },
      {
        "name": "InstanceType",
        "desc": "Instance type. Valid values: 0 (all instances), 1 (promoted), 2 (temp), 3 (read-only), -1 (promoted + read-only + disaster recovery)"
      },
      {
        "name": "ClusterType",
        "desc": "Cluster type. Valid values: 0 (replica set instance), 1 (sharding instance), -1 (all instances)"
      },
      {
        "name": "Status",
        "desc": "Instance status. Valid values: 0 (to be initialized), 1 (in process), 2 (valid), -2 (expired)"
      },
      {
        "name": "VpcId",
        "desc": "VPC ID. This parameter can be left empty for the basic network"
      },
      {
        "name": "SubnetId",
        "desc": "Subnet ID of VPC. This parameter can be left empty for the basic network. If it is passed in as an input parameter, the corresponding VpcId must be set"
      },
      {
        "name": "PayMode",
        "desc": "Billing type. Valid value: 0 (pay-as-you-go)"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned for a single request. Valid values: 1–100. Default value: 20"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0"
      },
      {
        "name": "OrderBy",
        "desc": "Sort by field of the returned result set. Currently, supported values include \"ProjectId\", \"InstanceName\", and \"CreateTime\". The return results are sorted in ascending order by default."
      },
      {
        "name": "OrderByType",
        "desc": "Sorting method of the return result set. Currently, \"ASC\" or \"DESC\" is supported"
      },
      {
        "name": "ProjectIds",
        "desc": "Project ID"
      },
      {
        "name": "SearchKey",
        "desc": "Search keyword, which can be instance ID, instance name, or complete IP"
      }
    ],
    "desc": "This API is used to query the list of TencentDB instances (which can be master, disaster recovery, or read-only instances). It supports filtering instances by project ID, instance ID, and instance status."
  },
  "IsolateDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page"
      }
    ],
    "desc": "This API is used to isolate a pay-as-you-go TencentDB for MongoDB instance. An isolated instance is retained in the recycle bin and data can no longer be written to it. After it is isolated for a certain period of time, it will be completely deleted. For the retention period in the recycle bin, please see the terms of service for pay-as-you-go billing. Isolated pay-as-you-go instances cannot be recovered, so please proceed with caution."
  },
  "DescribeBackupAccess": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page"
      },
      {
        "name": "BackupName",
        "desc": "Name of the backup file for which to get the download permission"
      }
    ],
    "desc": "This API is used to get the permission to download a backup file. The specific backup file information can be obtained through the DescribeDBBackups API."
  }
}