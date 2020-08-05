# -*- coding: utf-8 -*-
DESC = "dcdb-2018-04-11"
INFO = {
  "DescribeAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow7t8lmc."
      },
      {
        "name": "UserName",
        "desc": "Login username."
      },
      {
        "name": "Host",
        "desc": "Access host allowed for a user. An account is uniquely identified by username and host."
      },
      {
        "name": "DbName",
        "desc": "Database name. `\\*` indicates that global permissions will be queried (i.e., `\\*.\\*`), in which case the `Type` and `Object ` parameters will be ignored"
      },
      {
        "name": "Type",
        "desc": "Type. Valid values: table; view; proc; func; \\*. If `DbName` is a specific database name and `Type` is `\\*`, the permissions of the database will be queried (i.e., `db.\\*`), in which case the `Object` parameter will be ignored"
      },
      {
        "name": "Object",
        "desc": "Type name. For example, if `Type` is table, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\\*` or empty"
      },
      {
        "name": "ColName",
        "desc": "If `Type` = table and `ColName` is `\\*`, the permissions of the table will be queried; if `ColName` is a specific field name, the permissions of the corresponding field will be queried"
      }
    ],
    "desc": "This API is used to query the permissions of a TencentDB account.\nNote: accounts with the same username but different hosts are different accounts."
  },
  "DescribeDatabaseObjects": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow7t8lmc."
      },
      {
        "name": "DbName",
        "desc": "Database name, which can be obtained through the `DescribeDatabases` API."
      }
    ],
    "desc": "This API is used to query the list of database objects in a TencentDB instance, including tables, stored procedures, views, and functions."
  },
  "DescribeDCDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Query by instance ID or IDs. Instance ID is in the format of dcdbt-2t4cf98d"
      },
      {
        "name": "SearchName",
        "desc": "Search field name. Valid values: instancename (search by instance name); vip (search by private IP); all (search by instance ID, instance name, and private IP)."
      },
      {
        "name": "SearchKey",
        "desc": "Search keyword. Fuzzy search is supported. Multiple keywords should be separated by line breaks (`\\n`)."
      },
      {
        "name": "ProjectIds",
        "desc": "Query by project ID"
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
        "desc": "Sort by field. Valid values: projectId; createtime; instancename"
      },
      {
        "name": "OrderByType",
        "desc": "Sort by type. Valid values: desc; asc"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 10. Maximum value: 100."
      },
      {
        "name": "ExclusterType",
        "desc": "1: non-dedicated cluster; 2: dedicated cluster; 0: all"
      },
      {
        "name": "IsFilterExcluster",
        "desc": "Identifies whether to use the `ExclusterType` field. false: no; true: yes"
      },
      {
        "name": "ExclusterIds",
        "desc": "Dedicated cluster ID"
      }
    ],
    "desc": "This API is used to query the list of TencentDB instances. It supports filtering instances by project ID, instance ID, private network address, and instance name.\nIf no filter is specified, 10 instances will be returned by default. Up to 100 instances can be returned for a single request."
  },
  "ResetAccountPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow728lmc."
      },
      {
        "name": "UserName",
        "desc": "Login username."
      },
      {
        "name": "Host",
        "desc": "Access host allowed for a user. An account is uniquely identified by username and host."
      },
      {
        "name": "Password",
        "desc": "New password, which can contain 6-32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks."
      }
    ],
    "desc": "This API is used to reset the password of a TencentDB account.\nNote: accounts with the same username but different hosts are different accounts."
  },
  "ModifyDBParameters": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow728lmc."
      },
      {
        "name": "Params",
        "desc": "List of parameters. Every element is a combination of `Param` and `Value`."
      }
    ],
    "desc": "This API is used to modify database parameters."
  },
  "OpenDBExtranetAccess": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ID of an instance for which to enable public network access. The ID is in the format of dcdbt-ow728lmc."
      },
      {
        "name": "Ipv6Flag",
        "desc": "Whether IPv6 is used. Default value: 0"
      }
    ],
    "desc": "This API is used to enable public network access for a TencentDB instance. After that, you can access the instance with the public domain name and port obtained through the `DescribeDCDBInstances` API."
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
        "desc": "Description of a target account"
      }
    ],
    "desc": "This API is used to clone an instance account."
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow728lmc."
      }
    ],
    "desc": "This API is used to query the list of accounts of a specified TencentDB instance."
  },
  "GrantAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow728lmc."
      },
      {
        "name": "UserName",
        "desc": "Login username."
      },
      {
        "name": "Host",
        "desc": "Access host allowed for a user. An account is uniquely identified by username and host."
      },
      {
        "name": "DbName",
        "desc": "Database name. `\\*` indicates that global permissions will be queried (i.e., `\\*.\\*`), in which case the `Type` and `Object ` parameters will be ignored"
      },
      {
        "name": "Privileges",
        "desc": "Global permission. Valid values: SELECT; INSERT; UPDATE; DELETE; CREATE; DROP; REFERENCES; INDEX; ALTER; CREATE TEMPORARY TABLES; LOCK TABLES; EXECUTE; CREATE VIEW; SHOW VIEW; CREATE ROUTINE; ALTER ROUTINE; EVENT; TRIGGER; SHOW DATABASES \nDatabase permission. Valid values: SELECT; INSERT; UPDATE; DELETE; CREATE; DROP; REFERENCES; INDEX; ALTER; CREATE TEMPORARY TABLES; LOCK TABLES; EXECUTE; CREATE VIEW; SHOW VIEW; CREATE ROUTINE; ALTER ROUTINE; EVENT; TRIGGER \nTable/view permission. Valid values: SELECT; INSERT; UPDATE; DELETE; CREATE; DROP; REFERENCES; INDEX; ALTER; CREATE VIEW; SHOW VIEW; TRIGGER \nStored procedure/function permission. Valid values: ALTER ROUTINE; EXECUTE \nField permission. Valid values: INSERT; REFERENCES; SELECT; UPDATE"
      },
      {
        "name": "Type",
        "desc": "Type. Valid values: table; view; proc; func; \\*. If `DbName` is a specific database name and `Type` is `\\*`, the permissions of the database will be set (i.e., `db.\\*`), in which case the `Object` parameter will be ignored"
      },
      {
        "name": "Object",
        "desc": "Type name. For example, if `Type` is table, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\\*` or empty"
      },
      {
        "name": "ColName",
        "desc": "If `Type` = table and `ColName` is `\\*`, the permissions will be granted to the table; if `ColName` is a specific field name, the permissions will be granted to the field"
      }
    ],
    "desc": "This API is used to grant permissions to a TencentDB account.\nNote: accounts with the same username but different hosts are different accounts."
  },
  "DeleteAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow728lmc, which can be obtained through the `DescribeDCDBInstances` API."
      },
      {
        "name": "UserName",
        "desc": "Username"
      },
      {
        "name": "Host",
        "desc": "Access host allowed for a user"
      }
    ],
    "desc": "This API is used to delete a TencentDB account, which is uniquely identified by username and host."
  },
  "DescribeDBParameters": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow7t8lmc."
      }
    ],
    "desc": "This API is used to get the current parameter settings of a database."
  },
  "ModifyDBInstancesProject": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "List of IDs of instances to be modified. Instance ID is in the format of dcdbt-ow728lmc."
      },
      {
        "name": "ProjectId",
        "desc": "ID of the project to be assigned, which can be obtained through the `DescribeProjects` API."
      }
    ],
    "desc": "This API is used to modify the project to which TencentDB instances belong."
  },
  "DescribeDBLogFiles": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow7t8lmc."
      },
      {
        "name": "ShardId",
        "desc": "Shard ID in the format of shard-7noic7tv"
      },
      {
        "name": "Type",
        "desc": "Requested log type. Valid values: 1 (binlog); 2 (cold backup); 3 (errlog); 4 (slowlog)."
      }
    ],
    "desc": "This API is used to get the list of various logs of a database, including cold backups, binlogs, errlogs, and slowlogs."
  },
  "DescribeDBSyncMode": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ID of an instance for which to modify the sync mode. The ID is in the format of dcdbt-ow728lmc."
      }
    ],
    "desc": "This API is used to query the sync mode of a TencentDB instance."
  },
  "CreateAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow728lmc, which can be obtained through the `DescribeDCDBInstances` API."
      },
      {
        "name": "UserName",
        "desc": "AccountName"
      },
      {
        "name": "Host",
        "desc": "Host that can be logged in to, which is in the same format as the host of the MySQL account and supports wildcards, such as %, 10.%, and 10.20.%."
      },
      {
        "name": "Password",
        "desc": "Account password, which can contain 6-32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks."
      },
      {
        "name": "ReadOnly",
        "desc": "Whether to create a read-only account. 0: no; 1: for the account's SQL requests, the secondary will be used first, and if it is unavailable, the primary will be used; 2: the secondary will be used first, and if it is unavailable, the operation will fail; 3: only the secondary will be read from."
      },
      {
        "name": "Description",
        "desc": "Account remarks, which can contain 0-256 letters, digits, and common symbols."
      },
      {
        "name": "DelayThresh",
        "desc": "If the secondary delay exceeds the set value of this parameter, the secondary will be deemed to have failed.\nIt is recommended that this parameter be set to a value greater than 10. This parameter takes effect when `ReadOnly` is 1 or 2."
      }
    ],
    "desc": "This API is used to create a TencentDB account. Multiple accounts can be created for one instance. Accounts with the same username but different hosts are different accounts."
  },
  "ModifyDBSyncMode": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ID of an instance for which to modify the sync mode. The ID is in the format of dcdbt-ow728lmc."
      },
      {
        "name": "SyncMode",
        "desc": "Sync mode. 0: async; 1: strong sync; 2: downgradable strong sync"
      }
    ],
    "desc": "This API is used to modify the sync mode of a TencentDB instance."
  },
  "DescribeProjects": {
    "params": [],
    "desc": "This API is used to query the project list."
  },
  "CloseDBExtranetAccess": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ID of an instance for which to disable public network access. The ID is in the format of dcdbt-ow728lmc and can be obtained through the `DescribeDCDBInstances` API."
      },
      {
        "name": "Ipv6Flag",
        "desc": "Whether IPv6 is used. Default value: 0"
      }
    ],
    "desc": "This API is used to disable public network access for a TencentDB instance, which will make the public IP address inaccessible. The `DescribeDCDBInstances` API will not return the public domain name and port information of the corresponding instance."
  },
  "ModifyAccountDescription": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow728lmc."
      },
      {
        "name": "UserName",
        "desc": "Login username."
      },
      {
        "name": "Host",
        "desc": "Access host allowed for a user. An account is uniquely identified by username and host."
      },
      {
        "name": "Description",
        "desc": "New account remarks, which can contain 0-256 characters."
      }
    ],
    "desc": "This API is used to modify the remarks of a TencentDB account.\nNote: accounts with the same username but different hosts are different accounts."
  },
  "CopyAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow728lmc."
      },
      {
        "name": "SrcUserName",
        "desc": "Source username"
      },
      {
        "name": "SrcHost",
        "desc": "Access host allowed for a source user"
      },
      {
        "name": "DstUserName",
        "desc": "Target username"
      },
      {
        "name": "DstHost",
        "desc": "Access host allowed for a target user"
      },
      {
        "name": "SrcReadOnly",
        "desc": "`ReadOnly` attribute of a source account"
      },
      {
        "name": "DstReadOnly",
        "desc": "`ReadOnly` attribute of a target account"
      }
    ],
    "desc": "This API is used to copy the permissions of a TencentDB account.\nNote: Accounts with the same username but different hosts are different accounts. Permissions can only be copied between accounts with the same `Readonly` attribute."
  },
  "DescribeDCDBShards": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow728lmc."
      },
      {
        "name": "ShardInstanceIds",
        "desc": "Shard ID list."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "OrderBy",
        "desc": "Sort by field. Only `createtime` is supported currently"
      },
      {
        "name": "OrderByType",
        "desc": "Sort by type. Valid values: desc; asc"
      }
    ],
    "desc": "This API is used to query the information of shards of a TencentDB instance."
  },
  "DescribeDatabases": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow7t8lmc."
      }
    ],
    "desc": "This API is used to query the list of databases of a TencentDB instance."
  },
  "DescribeDatabaseTable": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID in the format of dcdbt-ow7t8lmc."
      },
      {
        "name": "DbName",
        "desc": "Database name, which can be obtained through the `DescribeDatabases` API."
      },
      {
        "name": "Table",
        "desc": "Table name, which can be obtained through the `DescribeDatabaseObjects` API."
      }
    ],
    "desc": "This API is used to query the table information of a TencentDB instance."
  },
  "InitDCDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "List of IDs of instances to be initialized. The ID is in the format of `dcdbt-ow728lmc` and can be obtained through the `DescribeDCDBInstances` API."
      },
      {
        "name": "Params",
        "desc": "List of parameters. Valid values: character_set_server (character set; required); lower_case_table_names (table name case sensitivity; required; 0: case-sensitive; 1: case-insensitive); innodb_page_size (InnoDB data page; default size: 16 KB); sync_mode (sync mode; 0: async; 1: strong sync; 2: downgradable strong sync; default value: strong sync)."
      }
    ],
    "desc": "This API is used to initialize instances, including setting the default character set and table name case sensitivity."
  }
}