# -*- coding: utf-8 -*-
DESC = "dts-2018-03-30"
INFO = {
  "CreateSyncCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Disaster recovery sync task ID"
      }
    ],
    "desc": "Before the StartSyncJob API is called to start disaster recovery sync, this API should be called first to create a check. Data sync can start only if the check succeeds. You can view the check result through the DescribeSyncCheckJob API.\nSync can begin only if the check succeeds."
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
  "DescribeSyncCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "ID of the disaster recovery sync task to be queried"
      }
    ],
    "desc": "This API is used to get the check result after a disaster recovery sync check task is created through the CreateSyncCheckJob API. Check status and progress can be queried.\nIf the check succeeds, you can call the StartSyncJob API to start the sync task.\nIf the check fails, the reason will be returned. You can modify the configuration through the ModifySyncJob API and initiate check again.\nIt takes about 30 seconds to complete the check task. If the returned status is not \"finished\", the check has not been completed, and this API needs to be polled.\nIf Status=finished and CheckFlag=1, the check succeeds.\nIf Status=finished and CheckFlag !=1, the check fails."
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
  "DeleteMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Data migration task ID"
      }
    ],
    "desc": "This API (DeleteMigrationJob) is used to delete a data migration task. If the task status queried through the DescribeMigrateJobs API is checking (status=3), running (status=7), ready (status=8), canceling (status=11), or completing (status=12), the task cannot be deleted."
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
  "StopMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Data migration task ID"
      }
    ],
    "desc": "This API (StopMigrateJob) is used to cancel a data migration task.\nDuring migration, this API can be used to cancel migration if the task status queried through the DescribeMigrateJobs API is running (status=7) or ready (status=8), and the migration task will fail."
  },
  "CompleteMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Data migration task ID"
      }
    ],
    "desc": "This API (CompleteMigrateJob) is used to complete a data migration task.\nFor tasks in incremental migration mode, you need to call this API before migration gets ready, so as to stop migrating incremental data.\nIf the task status queried through the (DescribeMigrateJobs) API is ready (status=8), you can call this API to complete the migration task.\n"
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
  "StartSyncJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Disaster recovery sync task ID"
      }
    ],
    "desc": "This API is used to start a disaster recovery sync task after it is successfully checked through the CreateSyncCheckJob and DescribeSyncCheckJob APIs."
  },
  "CreateMigrateCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Data migration task ID"
      }
    ],
    "desc": "This API is used to create a migration check task.\nBefore migration, you should call this API to create a check. Migration will start only if the check succeeds. You can view the check result through the DescribeMigrateCheckJob API.\nAfter successful check, if the migration task needs to be modified, a new check task should be created and migration will begin only after the new check succeeds."
  }
}