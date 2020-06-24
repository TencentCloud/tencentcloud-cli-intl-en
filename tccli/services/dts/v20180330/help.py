# -*- coding: utf-8 -*-
DESC = "dts-2018-03-30"
INFO = {
  "DeleteSyncJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "ID of the disaster recovery sync task to be deleted"
      }
    ],
    "desc": "This API is used to delete a disaster recovery sync task. Sync tasks that are running cannot be deleted."
  },
  "DescribeSyncJobs": {
    "params": [
      {
        "name": "JobId",
        "desc": "Disaster recovery sync task ID"
      },
      {
        "name": "JobName",
        "desc": "Disaster recovery sync task name"
      },
      {
        "name": "Order",
        "desc": "Sort by field. Value range: JobId, Status, JobName, CreateTime"
      },
      {
        "name": "OrderSeq",
        "desc": "Sorting order. Value range: ASC (ascending), DESC (descending)"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Number of the returned instances. Value range: [1, 100]. Default value: 20"
      }
    ],
    "desc": "This API is used to query disaster recovery sync tasks initiated on the DTS platform."
  },
  "ActivateSubscribe": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "Subscription instance ID."
      },
      {
        "name": "InstanceId",
        "desc": "Database Instance ID"
      },
      {
        "name": "SubscribeObjectType",
        "desc": "Data subscription type. 0: full instance subscription, 1: data subscription, 2: structure subscription, 3: data subscription and structure subscription"
      },
      {
        "name": "Objects",
        "desc": "Subscription object"
      },
      {
        "name": "UniqSubnetId",
        "desc": "Subnet of data subscription service, which is the subnet of the database instance by default."
      },
      {
        "name": "Vport",
        "desc": "Subscription service port. Default value: 7507"
      }
    ],
    "desc": "This API is used to configure a data subscription, which can be called only for subscription instances in unconfigured status."
  },
  "ModifySyncJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "ID of the disaster recovery sync task to be modified"
      },
      {
        "name": "JobName",
        "desc": "Name of the disaster recovery sync task"
      },
      {
        "name": "SyncOption",
        "desc": "Configuration options of a disaster recovery sync task"
      },
      {
        "name": "DatabaseInfo",
        "desc": "When syncing the specified table, you need to set the information of the source table to be synced, which should be described in JSON string format. Below are examples.\nFor databases with a database-table structure:\n[{\"Database\":\"db1\",\"Table\":[\"table1\",\"table2\"]},{\"Database\":\"db2\"}]"
      }
    ],
    "desc": "This API is used to modify a disaster recovery sync task. \nIf the status of a sync task is creating, created, check succeeded, or check failed, this API can be called to modify the task. \nThe information of the source and target instances cannot be modified, but the task name and the tables to be synced can."
  },
  "CreateSyncJob": {
    "params": [
      {
        "name": "JobName",
        "desc": "Disaster recovery sync task name"
      },
      {
        "name": "SyncOption",
        "desc": "Configuration options of a disaster recovery sync task"
      },
      {
        "name": "SrcDatabaseType",
        "desc": "Source instance database type, which currently only supports mysql"
      },
      {
        "name": "SrcAccessType",
        "desc": "Source instance access type, which currently only supports cdb (TencentDB instances)"
      },
      {
        "name": "SrcInfo",
        "desc": "Source instance information"
      },
      {
        "name": "DstDatabaseType",
        "desc": "Target instance access type, which currently only supports mysql"
      },
      {
        "name": "DstAccessType",
        "desc": "Target instance access type, which currently only supports cdb (TencentDB instances)"
      },
      {
        "name": "DstInfo",
        "desc": "Target instance information"
      },
      {
        "name": "DatabaseInfo",
        "desc": "Information of the source table to be synced, which is described in JSON string format.\nFor databases with a database-table structure:\n[{Database:db1,Table:[table1,table2]},{Database:db2}]"
      }
    ],
    "desc": "This API (CreateSyncJob) is used to create a disaster recovery sync task.\nAfter successful creation, check can be initiated through the CreateSyncCheckJob API. The sync task can be started through the StartSyncJob API only if the check succeeds."
  },
  "ModifySubscribeObjects": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "Data subscription instance ID"
      },
      {
        "name": "SubscribeObjectType",
        "desc": "Data subscription type. Valid values: 0 (full instance subscription), 1 (data subscription), 2 (structure subscription), 3 (data subscription + structure subscription)"
      },
      {
        "name": "Objects",
        "desc": "Information of subscribed table"
      }
    ],
    "desc": "This API is used to modify the subscription rule of a data subscription channel."
  },
  "StartSyncJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Disaster recovery sync task ID"
      }
    ],
    "desc": "This API is used to start a disaster recovery sync task after it is successfully checked through the CreateSyncCheckJob and DescribeSyncCheckJob APIs."
  },
  "DeleteMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Data migration task ID"
      }
    ],
    "desc": "This API (DeleteMigrationJob) is used to delete a data migration task. If the task status queried through the DescribeMigrateJobs API is checking (status=3), running (status=7), ready (status=8), canceling (status=11), or completing (status=12), the task cannot be deleted."
  },
  "DescribeAsyncRequestInfo": {
    "params": [
      {
        "name": "AsyncRequestId",
        "desc": "Task ID"
      }
    ],
    "desc": "This API is used to query the execution result of a task."
  },
  "SwitchDrToMaster": {
    "params": [
      {
        "name": "DstInfo",
        "desc": "Disaster recovery instance information"
      },
      {
        "name": "DatabaseType",
        "desc": "Database type (such as MySQL)"
      }
    ],
    "desc": "This API is used to promote a disaster recovery instance to a master instance, which will stop sync from the original master instance and end the master/slave relationship."
  },
  "StopMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Data migration task ID"
      }
    ],
    "desc": "This API (StopMigrateJob) is used to cancel a data migration task.\nDuring migration, this API can be used to cancel migration if the task status queried through the DescribeMigrateJobs API is running (status=7) or ready (status=8), and the migration task will fail."
  },
  "DescribeRegionConf": {
    "params": [],
    "desc": "This API is used to query the purchasable subscription instance regions."
  },
  "DescribeMigrateJobs": {
    "params": [
      {
        "name": "JobId",
        "desc": "Data migration task ID"
      },
      {
        "name": "JobName",
        "desc": "Data migration task name"
      },
      {
        "name": "Order",
        "desc": "Sort by field. Value range: JobId, Status, JobName, MigrateType, RunMode, CreateTime"
      },
      {
        "name": "OrderSeq",
        "desc": "Sorting order. Value range: ASC (ascending), DESC (descending)"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Number of the returned instances. Value range: [1, 100]. Default value: 20"
      }
    ],
    "desc": "This API is used to query data migration tasks.\nFor a finance zone linkage, please use the domain name https://dts.ap-shenzhen-fsi.tencentcloudapi.com."
  },
  "DescribeSubscribes": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "Data subscription instance ID"
      },
      {
        "name": "SubscribeName",
        "desc": "Data subscription instance name"
      },
      {
        "name": "InstanceId",
        "desc": "ID of bound database instance"
      },
      {
        "name": "ChannelId",
        "desc": "Data subscription instance channel ID"
      },
      {
        "name": "PayType",
        "desc": "Billing mode filter. Default value: 1 (pay-as-you-go)"
      },
      {
        "name": "Product",
        "desc": "Subscribed database product, such as MySQL"
      },
      {
        "name": "Status",
        "desc": "Data subscription instance status. Valid values: creating, normal, isolating, isolated, offlining"
      },
      {
        "name": "SubsStatus",
        "desc": "Data subscription instance configuration status. Valid values: unconfigure, configuring, configured"
      },
      {
        "name": "Offset",
        "desc": "Starting offset of returned results"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned at a time"
      },
      {
        "name": "OrderDirection",
        "desc": "Sorting order. Valid values: DESC, ASC. Default value: DESC, indicating descending by creation time"
      }
    ],
    "desc": "This API is used to get the information list of data subscription instances. Pagination is enabled by default with 20 results returned each time."
  },
  "DescribeSyncCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "ID of the disaster recovery sync task to be queried"
      }
    ],
    "desc": "This API is used to get the check result after a disaster recovery sync check task is created through the CreateSyncCheckJob API. Check status and progress can be queried.\nIf the check succeeds, you can call the StartSyncJob API to start the sync task.\nIf the check fails, the reason will be returned. You can modify the configuration through the ModifySyncJob API and initiate check again.\nIt takes about 30 seconds to complete the check task. If the returned status is not \"finished\", the check has not been completed, and this API needs to be polled.\nIf Status=finished and CheckFlag=1, the check succeeds.\nIf Status=finished and CheckFlag !=1, the check fails."
  },
  "CreateMigrateJob": {
    "params": [
      {
        "name": "JobName",
        "desc": "Data migration task name"
      },
      {
        "name": "MigrateOption",
        "desc": "Migration task configuration options"
      },
      {
        "name": "SrcDatabaseType",
        "desc": "Source instance database type, which currently supports MySQL, Redis, MongoDB, PostgreSQL, MariaDB, and Percona. For more information on the supported types in a specific region, see the migration task creation page in the console."
      },
      {
        "name": "SrcAccessType",
        "desc": "Source instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance), ccn (CCN instance)"
      },
      {
        "name": "SrcInfo",
        "desc": "Source instance information, which is correlated with the migration task type"
      },
      {
        "name": "DstDatabaseType",
        "desc": "Target instance access type, which currently supports MySQL, Redis, MongoDB, PostgreSQL, MariaDB, and Percona. For more information on the supported types in a specific region, see the migration task creation page in the console."
      },
      {
        "name": "DstAccessType",
        "desc": "Target instance access type, which currently only supports cdb (TencentDB instance)"
      },
      {
        "name": "DstInfo",
        "desc": "Destination instance information"
      },
      {
        "name": "DatabaseInfo",
        "desc": "Information of the source table to be migrated, which is described in JSON string format. It is required if MigrateOption.MigrateObject is 2 (migrating the specified table).\nFor databases with a database-table structure:\n[{Database:db1,Table:[table1,table2]},{Database:db2}]\nFor databases with a database-schema-table structure:\n[{Database:db1,Schema:s1\nTable:[table1,table2]},{Database:db1,Schema:s2\nTable:[table1,table2]},{Database:db2,Schema:s1\nTable:[table1,table2]},{Database:db3},{Database:db4\nSchema:s1}]"
      }
    ],
    "desc": "This API (CreateMigrateJob) is used to create a data migration task.\n\nFor a finance zone linkage, please use the domain name dts.ap-shenzhen-fsi.tencentcloudapi.com."
  },
  "ModifySubscribeVipVport": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "Data subscription instance ID"
      },
      {
        "name": "DstUniqSubnetId",
        "desc": "Specified destination subnet. If this parameter is passed in, `DstIp` must be in the destination subnet"
      },
      {
        "name": "DstIp",
        "desc": "Target IP. Either this field or `DstPort` must be passed in"
      },
      {
        "name": "DstPort",
        "desc": "Target port. Value range: [1025-65535]"
      }
    ],
    "desc": "This API is used to modify the IP and port number of a data subscription instance."
  },
  "CreateMigrateCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Data migration task ID"
      }
    ],
    "desc": "This API is used to create a migration check task.\nBefore migration, you should call this API to create a check. Migration will start only if the check succeeds. You can view the check result through the DescribeMigrateCheckJob API.\nAfter successful check, if the migration task needs to be modified, a new check task should be created and migration will begin only after the new check succeeds."
  },
  "ModifySubscribeConsumeTime": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "Data subscription instance ID"
      },
      {
        "name": "ConsumeStartTime",
        "desc": "Consumption starting time point in the format of `Y-m-d h:m:s`, i.e., the starting time point for data subscription. Value range: within the last 24 hours"
      }
    ],
    "desc": "This API is used to modify the consumption time point of a data subscription channel."
  },
  "ModifySubscribeName": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "Data subscription instance ID"
      },
      {
        "name": "SubscribeName",
        "desc": "Data subscription instance name. Length limit: [1,60]"
      }
    ],
    "desc": "This API is used to rename a data subscription instance."
  },
  "CreateSyncCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Disaster recovery sync task ID"
      }
    ],
    "desc": "Before the StartSyncJob API is called to start disaster recovery sync, this API should be called first to create a check. Data sync can start only if the check succeeds. You can view the check result through the DescribeSyncCheckJob API.\nSync can begin only if the check succeeds."
  },
  "CreateSubscribe": {
    "params": [
      {
        "name": "Product",
        "desc": "Subscribed database type. Currently, MySQL is supported"
      },
      {
        "name": "PayType",
        "desc": "Instance billing mode, which is always 1 (hourly billing),"
      },
      {
        "name": "Duration",
        "desc": "Purchase duration in months, which is required if `PayType` is 0. Maximum value: 120 (this field is not required of global site users and is better to be hidden)"
      },
      {
        "name": "Count",
        "desc": "Quantity. Default value: 1. Maximum value: 10"
      },
      {
        "name": "AutoRenew",
        "desc": "Whether to auto-renew. Default value: 0. This flag does not take effect for hourly billed instances (this field should be hidden from global site users)"
      }
    ],
    "desc": "This API is used to create a data subscription instance."
  },
  "ResetSubscribe": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "Data subscription instance ID"
      }
    ],
    "desc": "This API is used to reset a data subscription instance. Once reset, an activated instance can be bound to other database instances through the `ActivateSubscribe` API."
  },
  "StartMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Data migration task ID"
      }
    ],
    "desc": "This API (StartMigrationJob) is used to start a migration task. After the API is called, non-scheduled migration tasks will start the migration immediately, while scheduled tasks will start the countdown.\nBefore calling this API, be sure to use the CreateMigrateCheckJob API to check the data migration task, which can be started only if its status queried through the DescribeMigrateJobs API is check succeeded (status=4)."
  },
  "ModifyMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "ID of the data migration task to be modified"
      },
      {
        "name": "JobName",
        "desc": "Data migration task name"
      },
      {
        "name": "MigrateOption",
        "desc": "Migration task configuration options"
      },
      {
        "name": "SrcAccessType",
        "desc": "Source instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance)"
      },
      {
        "name": "SrcInfo",
        "desc": "Source instance information, which is correlated with the migration task type"
      },
      {
        "name": "DstAccessType",
        "desc": "Target instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance). Currently, only `cdb` is supported"
      },
      {
        "name": "DstInfo",
        "desc": "Target instance information. The region where the target instance is located cannot be modified."
      },
      {
        "name": "DatabaseInfo",
        "desc": "When migrating the specified table, you need to set the information of the source database table to be migrated, which should be described in JSON string format. Below are examples.\n\nFor databases with a database-table structure:\n[{\"Database\":\"db1\",\"Table\":[\"table1\",\"table2\"]},{\"Database\":\"db2\"}]\nFor databases with a database-schema-table structure:\n[{\"Database\":\"db1\",\"Schema\":\"s1\",\"Table\":[\"table1\",\"table2\"]},{\"Database\":\"db1\",\"Schema\":\"s2\",\"Table\":[\"table1\",\"table2\"]},{\"Database\":\"db2\",\"Schema\":\"s1\",\"Table\":[\"table1\",\"table2\"]},{\"Database\":\"db3\"},{\"Database\":\"db4\",\"Schema\":\"s1\"}]\n\nThis field does not need to be set when the entire instance is to be migrated"
      }
    ],
    "desc": "This API (ModifyMigrateJob) is used to modify a data migration task.\nIf the status of a migration task is creating (status=1), check succeeded (status=4), check failed (status=5), or migration failed (status=10), this API can be called to modify the task, but the type of the source and target instances and the region of the target instance cannot be modified.\n\nFor a finance zone linkage, please use the domain name dts.ap-shenzhen-fsi.tencentcloudapi.com."
  },
  "OfflineIsolatedSubscribe": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "Data subscription instance ID"
      }
    ],
    "desc": "This API is used to deactivate an isolated data subscription instance."
  },
  "IsolateSubscribe": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "Subscription instance ID"
      }
    ],
    "desc": "This API is used to isolate an hourly billed subscription instance. After this API is called, the instance will become unavailable and billing will stop for it."
  },
  "DescribeSubscribeConf": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "Subscription instance ID"
      }
    ],
    "desc": "This API is used to query the subscription instance configuration."
  },
  "DescribeMigrateCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Data migration task ID"
      }
    ],
    "desc": "This API is used to get the check result and query check status and progress after a check is created. \nIf the check succeeds, you can call the StartMigrateJob API to start migration.\nIf the check fails, the reason can be queried. Please modify the migration configuration or adjust relevant parameters of the source/target instances through the ModifyMigrateJob API based on the error message."
  },
  "CompleteMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Data migration task ID"
      }
    ],
    "desc": "This API (CompleteMigrateJob) is used to complete a data migration task.\nFor tasks in incremental migration mode, you need to call this API before migration gets ready, so as to stop migrating incremental data.\nIf the task status queried through the (DescribeMigrateJobs) API is ready (status=8), you can call this API to complete the migration task.\n"
  }
}