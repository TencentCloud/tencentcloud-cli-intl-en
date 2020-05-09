# -*- coding: utf-8 -*-
DESC = "tcaplusdb-2019-08-23"
INFO = {
  "CreateCluster": {
    "params": [
      {
        "name": "IdlType",
        "desc": "Cluster data description language type, such as `PROTO`, `TDR`, or `MIX`"
      },
      {
        "name": "ClusterName",
        "desc": "Cluster name, which can contain up to 32 letters and digits"
      },
      {
        "name": "VpcId",
        "desc": "ID of the VPC instance bound to a cluster in the format of `vpc-f49l6u0z`"
      },
      {
        "name": "SubnetId",
        "desc": "ID of the subnet instance bound to a cluster in the format of `subnet-pxir56ns`"
      },
      {
        "name": "Password",
        "desc": "Cluster access password, which must contain lowercase letters (a–z), uppercase letters (A–Z), and digits (0–9)."
      }
    ],
    "desc": "This API is used to create a TcaplusDB cluster."
  },
  "DescribeUinInWhitelist": {
    "params": [],
    "desc": "This API is used to query whether the current user is in the whitelist and control whether the user can create TDR-type apps or tables."
  },
  "DescribeTablesInRecycle": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where the table to be queried resides"
      },
      {
        "name": "TableGroupIds",
        "desc": "List of IDs of the table groups where the table to be queried resides"
      },
      {
        "name": "Filters",
        "desc": "Filter. Valid values: TableName, TableInstanceId"
      },
      {
        "name": "Offset",
        "desc": "Query result offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned query results"
      }
    ],
    "desc": "This API is used to query the details of a table in recycle bin."
  },
  "RollbackTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where the table to be rolled back resides"
      },
      {
        "name": "SelectedTables",
        "desc": "List of tables to be rolled back"
      },
      {
        "name": "RollbackTime",
        "desc": "Time to roll back to"
      },
      {
        "name": "Mode",
        "desc": "Rollback mode. `KEYS` is supported"
      }
    ],
    "desc": "This API is used to roll back table data."
  },
  "ModifyClusterName": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster to be renamed"
      },
      {
        "name": "ClusterName",
        "desc": "Cluster name to be changed to, which can contain up to 32 letters and digits"
      }
    ],
    "desc": "This API is used to rename a specified cluster."
  },
  "DeleteCluster": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of cluster to be deleted"
      }
    ],
    "desc": "This API is used to delete a TcaplusDB cluster, which will succeed only after all resources (including table groups and tables) in the cluster are released."
  },
  "ModifyClusterPassword": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster for which to modify the password"
      },
      {
        "name": "OldPassword",
        "desc": "Old cluster password"
      },
      {
        "name": "OldPasswordExpireTime",
        "desc": "Expected expiration time of old cluster password"
      },
      {
        "name": "NewPassword",
        "desc": "New cluster password, which must contain lowercase letters (a–z), uppercase letters (A–Z), and digits (0–9)."
      },
      {
        "name": "Mode",
        "desc": "Update mode. 1: updates password, 2: updates old password expiration time. Default value: 1"
      }
    ],
    "desc": "This API is used to change the password of a specified cluster. The backend will allow the TcaplusDB SDK to access databases with both old and new passwords before the old password expires. You cannot submit a new password change request before the old password expires or submit a request to modify the expiration time of the old password after the old password expires."
  },
  "DeleteIdlFiles": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where IDL resides"
      },
      {
        "name": "IdlFiles",
        "desc": "List of information of IDL files to be deleted"
      }
    ],
    "desc": "This API is used to delete a target IDL file by specifying the cluster ID and information of the file to be deleted. If the file is associated with a table, deletion will fail."
  },
  "RecoverRecycleTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where a table resides"
      },
      {
        "name": "SelectedTables",
        "desc": "Information of tables to be recovered"
      }
    ],
    "desc": "This API is used to recover a dropped table from the recycle bin. It will not work for tables to be released due to arrears."
  },
  "CreateBackup": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where the table to be backed up resides"
      },
      {
        "name": "SelectedTables",
        "desc": "Information list of tables to be backed up"
      },
      {
        "name": "Remark",
        "desc": "Remarks"
      }
    ],
    "desc": "This API is used to create a backup task."
  },
  "CreateTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where to create a table"
      },
      {
        "name": "IdlFiles",
        "desc": "Table creation IDL file list selected by user"
      },
      {
        "name": "SelectedTables",
        "desc": "Information list of tables to be created"
      }
    ],
    "desc": "This API is used to create tables in batches based on the selected IDL file list."
  },
  "ModifyTableQuotas": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where the table to be scaled resides"
      },
      {
        "name": "TableQuotas",
        "desc": "List of quotas of tables selected for modification"
      }
    ],
    "desc": "This API is used to scale a table."
  },
  "DescribeClusters": {
    "params": [
      {
        "name": "ClusterIds",
        "desc": "List of IDs of clusters to be queried"
      },
      {
        "name": "Filters",
        "desc": "Query filter"
      },
      {
        "name": "Offset",
        "desc": "Query list offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results in query list. Default value: 20"
      }
    ],
    "desc": "This API is used to query the TcaplusDB cluster list, including cluster details."
  },
  "DeleteTableGroup": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where a table group resides"
      },
      {
        "name": "TableGroupId",
        "desc": "Table group ID"
      }
    ],
    "desc": "This API is used to delete a table group."
  },
  "ModifyTableGroupName": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where a table group resides"
      },
      {
        "name": "TableGroupId",
        "desc": "ID of the table group to be renamed"
      },
      {
        "name": "TableGroupName",
        "desc": "New table group name, which can contain letters and symbols"
      }
    ],
    "desc": "This API is used to rename a TcaplusDB table group."
  },
  "CreateTableGroup": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where a table group resides"
      },
      {
        "name": "TableGroupName",
        "desc": "Table group name, which can contain up to 32 letters and digits"
      },
      {
        "name": "TableGroupId",
        "desc": "Table group ID, which can be customized but must be unique in one cluster. If it is not specified, the auto-increment mode will be used."
      }
    ],
    "desc": "This API is used to create a table group in a TcaplusDB cluster."
  },
  "DescribeRegions": {
    "params": [],
    "desc": "This API is used to query the list of regions supported by the TcaplusDB service."
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "ClusterIds",
        "desc": "List of IDs of clusters where the tasks to be queried reside"
      },
      {
        "name": "TaskIds",
        "desc": "List of IDs of tasks to be queried"
      },
      {
        "name": "Filters",
        "desc": "Filter. Valid values: Content, TaskType, Operator, Time"
      },
      {
        "name": "Offset",
        "desc": "Query list offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results in query list"
      }
    ],
    "desc": "This API is used to query the task list."
  },
  "DescribeTableGroups": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where a table group resides"
      },
      {
        "name": "TableGroupIds",
        "desc": "Table group ID list"
      },
      {
        "name": "Filters",
        "desc": "Filter. Valid values: TableGroupName, TableGroupId"
      },
      {
        "name": "Offset",
        "desc": "Query list offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results in query list"
      }
    ],
    "desc": "This API is used to query the table group list."
  },
  "CompareIdlFiles": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where the table to be modified resides"
      },
      {
        "name": "SelectedTables",
        "desc": "List of tables to be modified"
      },
      {
        "name": "ExistingIdlFiles",
        "desc": "Selected list of uploaded IDL files. Either this parameter or `NewIdlFiles` must be selected"
      },
      {
        "name": "NewIdlFiles",
        "desc": "List of IDL files to be uploaded. Either this parameter or `ExistingIdlFiles` must be selected"
      }
    ],
    "desc": "This API is used to select a target table, upload and verify the table modification file, and return the result of whether the table structure is allowed to be modified."
  },
  "DescribeIdlFileInfos": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where a file resides"
      },
      {
        "name": "TableGroupIds",
        "desc": "ID of the table group where a file resides"
      },
      {
        "name": "IdlFileIds",
        "desc": "File ID list"
      },
      {
        "name": "Offset",
        "desc": "Query list offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results in query list"
      }
    ],
    "desc": "This API is used to query table description file details."
  },
  "DeleteTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where the table to be dropped resides"
      },
      {
        "name": "SelectedTables",
        "desc": "List of information of tables to be dropped"
      }
    ],
    "desc": "This API is used to drop a specified table. Calling this API for the first time means to move the table to the recycle bin, while calling it again means to drop the table completely from the recycle bin."
  },
  "ModifyTableMemos": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster instance where a table resides"
      },
      {
        "name": "TableMemos",
        "desc": "List of details of selected tables"
      }
    ],
    "desc": "This API is used to modify table remarks."
  },
  "VerifyIdlFiles": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where to create a table"
      },
      {
        "name": "TableGroupId",
        "desc": "ID of the table group where to create a table"
      },
      {
        "name": "ExistingIdlFiles",
        "desc": "List of information of uploaded IDL files. Either this parameter or `NewIdlFiles` must be present"
      },
      {
        "name": "NewIdlFiles",
        "desc": "List of information of IDL files to be uploaded. Either this parameter or `ExistingIdlFiles` must be present"
      }
    ],
    "desc": "This API is used to upload and verify a table creation file and return the definition of tables that are verified to be valid."
  },
  "ModifyTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where the table to be modified resides"
      },
      {
        "name": "IdlFiles",
        "desc": "Selected table modification IDL files"
      },
      {
        "name": "SelectedTables",
        "desc": "List of tables to be modified"
      }
    ],
    "desc": "This API is used to modify specified tables in batches based on the selected table definition IDL file."
  },
  "DescribeTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster where the table to be queried resides"
      },
      {
        "name": "TableGroupIds",
        "desc": "List of IDs of the table groups where the table to be queried resides"
      },
      {
        "name": "SelectedTables",
        "desc": "Information list of tables to be queried"
      },
      {
        "name": "Filters",
        "desc": "Filter. Valid values: TableName, TableInstanceId"
      },
      {
        "name": "Offset",
        "desc": "Query result offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned query results"
      }
    ],
    "desc": "This API is used to query table details."
  },
  "ClearTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "ID of the cluster instance where a table resides"
      },
      {
        "name": "SelectedTables",
        "desc": "List of information of tables to be cleared"
      }
    ],
    "desc": "This API is used to clear table data based on the specified table information."
  }
}