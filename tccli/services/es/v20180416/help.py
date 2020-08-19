# -*- coding: utf-8 -*-
DESC = "es-2018-04-16"
INFO = {
  "DescribeInstanceOperations": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Cluster instance ID"
      },
      {
        "name": "StartTime",
        "desc": "Start time, such as \"2019-03-07 16:30:39\""
      },
      {
        "name": "EndTime",
        "desc": "End time, such as \"2019-03-30 20:18:03\""
      },
      {
        "name": "Offset",
        "desc": "Pagination start value"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page"
      }
    ],
    "desc": "This API is used to query the operation history of an instance by specified criteria."
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "Zone",
        "desc": "AZ of the cluster instance. If this is not passed in, all AZs are used by default"
      },
      {
        "name": "InstanceIds",
        "desc": "List of cluster instance IDs"
      },
      {
        "name": "InstanceNames",
        "desc": "List of cluster instance names"
      },
      {
        "name": "Offset",
        "desc": "Pagination start value. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Default value: 20"
      },
      {
        "name": "OrderByKey",
        "desc": "Sort by field <li>1: instance ID </li><li>2: instance name </li><li>3: AZ </li><li>4: creation time </li>If `orderKey` is not passed in, sort by creation time in descending order"
      },
      {
        "name": "OrderByType",
        "desc": "Sorting order <li>0: ascending </li><li>1: descending </li>If orderByKey is passed in but orderByType is not, ascending order is used by default"
      },
      {
        "name": "TagList",
        "desc": "Node tag information list"
      },
      {
        "name": "IpList",
        "desc": "VPC VIP list"
      }
    ],
    "desc": "This API is used to query all eligible instances in the current region under the current account."
  },
  "UpdatePlugins": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "InstallPluginList",
        "desc": "List of names of the plugins to be installed"
      },
      {
        "name": "RemovePluginList",
        "desc": "List of names of the plugins to be uninstalled"
      },
      {
        "name": "ForceRestart",
        "desc": "Whether to force restart"
      }
    ],
    "desc": "This API is used to change the list of plugins."
  },
  "CreateInstance": {
    "params": [
      {
        "name": "Zone",
        "desc": "Availability Zone"
      },
      {
        "name": "EsVersion",
        "desc": "Instance version (\"5.6.4\", \"6.4.3\", \"6.8.2\", or \"7.5.1\")"
      },
      {
        "name": "VpcId",
        "desc": "VPC ID"
      },
      {
        "name": "SubnetId",
        "desc": "Subnet ID"
      },
      {
        "name": "Password",
        "desc": "Access password, which must contain 8 to 16 characters, and include at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]"
      },
      {
        "name": "InstanceName",
        "desc": "Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)"
      },
      {
        "name": "NodeNum",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nNumber of nodes (2-50)"
      },
      {
        "name": "ChargeType",
        "desc": "Billing mode <li>POSTPAID_BY_HOUR: Pay-as-you-go hourly </li>Default value: POSTPAID_BY_HOUR"
      },
      {
        "name": "ChargePeriod",
        "desc": "This parameter is not used on the global website"
      },
      {
        "name": "RenewFlag",
        "desc": "This parameter is not used on the global website"
      },
      {
        "name": "NodeType",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nNode specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>"
      },
      {
        "name": "DiskType",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nNode storage type <li>CLOUD_SSD: SSD cloud storage </li><li>CLOUD_PREMIUM: premium cloud storage </li>Default value: CLOUD_SSD"
      },
      {
        "name": "DiskSize",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nNode disk size in GB"
      },
      {
        "name": "TimeUnit",
        "desc": "This parameter is not used on the global website"
      },
      {
        "name": "AutoVoucher",
        "desc": "Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0"
      },
      {
        "name": "VoucherIds",
        "desc": "List of voucher IDs (only one voucher can be specified at a time currently)"
      },
      {
        "name": "EnableDedicatedMaster",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nWhether to create a dedicated primary node <li>true: yes </li><li>false: no </li>Default value: false"
      },
      {
        "name": "MasterNodeNum",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nNumber of dedicated primary nodes (only 3 and 5 are supported. This value must be passed in if `EnableDedicatedMaster` is `true`)"
      },
      {
        "name": "MasterNodeType",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nDedicated primary node type, which must be passed in if `EnableDedicatedMaster` is `true` <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>"
      },
      {
        "name": "MasterNodeDiskSize",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nDedicated primary node disk size in GB, which is optional. If passed in, it can only be 50 and cannot be customized currently"
      },
      {
        "name": "ClusterNameInConf",
        "desc": "ClusterName in the cluster configuration file, which is the instance ID by default and currently cannot be customized"
      },
      {
        "name": "DeployMode",
        "desc": "Cluster deployment mode <li>0: single-AZ deployment </li><li>1: multi-AZ deployment </li>Default value: 0"
      },
      {
        "name": "MultiZoneInfo",
        "desc": "Details of AZs in multi-AZ deployment mode (which is required when DeployMode is 1)"
      },
      {
        "name": "LicenseType",
        "desc": "License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum"
      },
      {
        "name": "NodeInfoList",
        "desc": "Node information list, which is used to describe the specification information of various types of nodes in the cluster, such as node type, node quantity, node specification, disk type, and disk size"
      },
      {
        "name": "TagList",
        "desc": "Node tag information list"
      },
      {
        "name": "BasicSecurityType",
        "desc": "Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>"
      }
    ],
    "desc": "This API is used to create an ES cluster instance with the specified specification."
  },
  "UpgradeInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "EsVersion",
        "desc": "Target ES version. Valid values: 6.4.3, 6.8.2, 7.5.1"
      },
      {
        "name": "CheckOnly",
        "desc": "Whether to check for upgrade only. Default value: false"
      },
      {
        "name": "LicenseType",
        "desc": "Target X-Pack edition: <li>OSS: Open-source Edition </li><li>basic: Basic Edition </li>Currently only used for v5.6.4 to v6.x upgrade. Default value: basic"
      },
      {
        "name": "BasicSecurityType",
        "desc": "Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>"
      }
    ],
    "desc": "This API is used to upgrade ES cluster version"
  },
  "UpgradeLicense": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "LicenseType",
        "desc": "License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum"
      },
      {
        "name": "AutoVoucher",
        "desc": "Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0"
      },
      {
        "name": "VoucherIds",
        "desc": "List of voucher IDs (only one voucher can be specified at a time currently)"
      },
      {
        "name": "BasicSecurityType",
        "desc": "Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>"
      },
      {
        "name": "ForceRestart",
        "desc": "Whether to force restart <li>true: yes </li><li>false: no </li>Default value: false"
      }
    ],
    "desc": "This API is used to upgrade ES X-Pack."
  },
  "UpdateInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "InstanceName",
        "desc": "Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)"
      },
      {
        "name": "NodeNum",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nNumber of nodes (2-50)"
      },
      {
        "name": "EsConfig",
        "desc": "Configuration item (JSON string). Only the following items are supported currently: <li>action.destructive_requires_name</li><li>indices.fielddata.cache.size</li><li>indices.query.bool.max_clause_count</li>"
      },
      {
        "name": "Password",
        "desc": "Password of the default user 'elastic', which must contain 8 to 16 characters, including at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]"
      },
      {
        "name": "EsAcl",
        "desc": "Access control list"
      },
      {
        "name": "DiskSize",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nDisk size in GB"
      },
      {
        "name": "NodeType",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nNode specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>"
      },
      {
        "name": "MasterNodeNum",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nNumber of dedicated primary nodes (only 3 and 5 are supported)"
      },
      {
        "name": "MasterNodeType",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nDedicated primary node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>"
      },
      {
        "name": "MasterNodeDiskSize",
        "desc": "This parameter has been disused. Please use `NodeInfoList`\nDedicated primary node disk size in GB. This is 50 GB by default and currently cannot be customized"
      },
      {
        "name": "ForceRestart",
        "desc": "Whether to force restart during configuration update <li>true: Yes </li><li>false: No </li>This needs to be set only for EsConfig. Default value: false"
      },
      {
        "name": "CosBackup",
        "desc": "Auto-backup to COS"
      },
      {
        "name": "NodeInfoList",
        "desc": "Node information list. You can pass in only the nodes to be updated and their corresponding specification information. Supported operations include: <li>modifying the number of nodes in the same type </li><li>modifying the specification and disk size of nodes in the same type </li><li>adding a node type (you must also specify the node type, quantity, specification, disk, etc.) </li>The above operations can only be performed one at a time, and the disk type cannot be modified"
      },
      {
        "name": "PublicAccess",
        "desc": "Public network access status"
      },
      {
        "name": "EsPublicAcl",
        "desc": "Public network ACL"
      },
      {
        "name": "KibanaPublicAccess",
        "desc": "Public network access status of Kibana"
      },
      {
        "name": "KibanaPrivateAccess",
        "desc": "Private network access status of Kibana"
      },
      {
        "name": "BasicSecurityType",
        "desc": "Enables or disables user authentication for ES Basic Edition v6.8 and above"
      },
      {
        "name": "KibanaPrivatePort",
        "desc": "Kibana private port"
      },
      {
        "name": "ScaleType",
        "desc": "0: scaling in blue/green deployment mode without cluster restart (default); 1: scaling by unmounting disk with rolling cluster restart"
      }
    ],
    "desc": "This API is used for operations such as modifying node specification, renaming an instance, modifying configuration, resetting password, and setting Kibana blocklist/allowlist. `InstanceId` is required, while `ForceRestart` is optional. Other parameters or parameter combinations and their meanings are as follows:\n- InstanceName: renames an instance (only for instance identification)\n- NodeInfoList: modifies node configuration (horizontally scaling nodes, vertically scaling nodes, adding primary nodes, adding cold nodes, etc.)\n- EsConfig: modifies cluster configuration\n- Password: changes the password of the default user \"elastic\"\n- EsAcl: modifies the ACL\n- CosBackUp: sets auto-backup to COS for a cluster\nOnly one of the parameters or parameter combinations above can be passed in at a time, while passing fewer or more ones will cause the request to fail."
  },
  "DeleteInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to terminate a cluster instance. "
  },
  "RestartInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "ForceRestart",
        "desc": "Whether to force restart <li>true: Yes </li><li>false: No </li>Default value: false"
      }
    ],
    "desc": "This API is used to restart an ES cluster instance (for operations such as system update). "
  },
  "DescribeInstanceLogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Cluster instance ID"
      },
      {
        "name": "LogType",
        "desc": "Log type. Default value: 1\n<li>1: primary log</li>\n<li>2: search slow log</li>\n<li>3: index slow log</li>\n<li>4: GC log</li>"
      },
      {
        "name": "SearchKey",
        "desc": "Search keyword, which supports LUCENE syntax, such as `level:WARN`, `ip:1.1.1.1`, and `message:test-index`"
      },
      {
        "name": "StartTime",
        "desc": "Log start time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53"
      },
      {
        "name": "EndTime",
        "desc": "Log end time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53"
      },
      {
        "name": "Offset",
        "desc": "Pagination start value. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Default value: 100. Maximum value: 100"
      },
      {
        "name": "OrderByType",
        "desc": "Time sorting order. Default value: 0\n<li>0: descending</li>\n<li>1: ascending</li>"
      }
    ],
    "desc": "This API is used to query the eligible ES cluster logs in the current region."
  }
}