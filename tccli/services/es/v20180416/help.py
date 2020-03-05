# -*- coding: utf-8 -*-
DESC = "es-2018-04-16"
INFO = {
  "UpgradeInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "EsVersion",
        "desc": "Target ES version"
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
        "desc": ""
      }
    ],
    "desc": "This API is used to upgrade ES cluster version"
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
        "desc": ""
      },
      {
        "name": "IpList",
        "desc": ""
      }
    ],
    "desc": "This API is used to query all eligible instances in the current region under the current account."
  },
  "CreateInstance": {
    "params": [
      {
        "name": "Zone",
        "desc": "Availability Zone"
      },
      {
        "name": "EsVersion",
        "desc": "Instance version (\"5.6.4\" or \"6.4.3\")"
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
        "desc": "Number of nodes (2-50)"
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
        "desc": "Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>"
      },
      {
        "name": "DiskType",
        "desc": "Node disk type <li>CLOUD_SSD: SSD cloud disk </li><li>CLOUD_PREMIUM: Premium cloud disk </li>Default value: CLOUD_SSD"
      },
      {
        "name": "DiskSize",
        "desc": "Node disk size in GB"
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
        "desc": "Whether to create a dedicated master node <li>true: Yes </li><li>false: No </li>Default value: false"
      },
      {
        "name": "MasterNodeNum",
        "desc": "Number of dedicated master nodes (only 3 and 5 are supported. This value must be passed in if `EnableDedicatedMaster` is true)"
      },
      {
        "name": "MasterNodeType",
        "desc": "Dedicated master node type, which must be passed in if `EnableDedicatedMaster` is true <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>"
      },
      {
        "name": "MasterNodeDiskSize",
        "desc": "Dedicated master node disk size in GB, which is optional. If passed in, it can only be 50 and cannot be customized currently"
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
        "desc": ""
      },
      {
        "name": "TagList",
        "desc": ""
      },
      {
        "name": "BasicSecurityType",
        "desc": ""
      }
    ],
    "desc": "This API is used to create an ES cluster instance with the specified specification."
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
        "desc": ""
      },
      {
        "name": "ForceRestart",
        "desc": ""
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
        "desc": "Number of nodes (2-50)"
      },
      {
        "name": "EsConfig",
        "desc": "Configuration item (JSON string). Only the following items are supported currently: <li>action.destructive_requires_name</li><li>indices.fielddata.cache.size</li><li>indices.query.bool.max_clause_count</li>"
      },
      {
        "name": "Password",
        "desc": "Password of the default user “elastic“, which must contain 8 to 16 characters, including at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]"
      },
      {
        "name": "EsAcl",
        "desc": "Access control list"
      },
      {
        "name": "DiskSize",
        "desc": "Disk size in GB"
      },
      {
        "name": "NodeType",
        "desc": "Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>"
      },
      {
        "name": "MasterNodeNum",
        "desc": "Number of dedicated master nodes (only 3 and 5 are supported)"
      },
      {
        "name": "MasterNodeType",
        "desc": "Dedicated master node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>"
      },
      {
        "name": "MasterNodeDiskSize",
        "desc": "Dedicated master node disk size in GB. This is 50 GB by default and currently cannot be customized"
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
        "desc": ""
      },
      {
        "name": "PublicAccess",
        "desc": ""
      },
      {
        "name": "EsPublicAcl",
        "desc": ""
      },
      {
        "name": "KibanaPublicAccess",
        "desc": ""
      },
      {
        "name": "KibanaPrivateAccess",
        "desc": ""
      }
    ],
    "desc": "This API is used for operations such as scaling a cluster, renaming an instance, modifying configuration, resetting password, and setting Kibana blacklist/whitelist. InstanceId is required, while ForceRestart is optional. Other parameters or parameter combinations and their meanings are as follows:\n- InstanceName: Renames an instance (only for instance identification)\n- NodeNum: Horizontally scales a cluster by adding or removing node\n- NodeType, DiskSize: Vertically scales a data node in a cluster\n- MasterNodeNum: Horizontally scales a cluster by adding or removing dedicated master nodes\n- MasterNodeType, MasterNodeDiskSize: Vertically scales a dedicated master node in a cluster\n- EsConfig: Modifies cluster configuration\n- Password: Changes the password of the default user “elastic”\n- EsAcl: Modifies the ACL\n- CosBackUp: Sets auto-backup to COS for a cluster\nOnly one of the parameters or parameter combinations above can be passed in at a time, and passing fewer or more will cause the request to fail."
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
  }
}