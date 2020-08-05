# -*- coding: utf-8 -*-
DESC = "emr-2019-01-03"
INFO = {
  "ScaleOutInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "Time unit of scale-out. Valid values:\n<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>\n<li>m: month. When `PayMode` is 1, `TimeUnit` can only be `m`.</li>"
      },
      {
        "name": "TimeSpan",
        "desc": "Duration of scale-out, which needs to be used together with `TimeUnit`."
      },
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "PayMode",
        "desc": "Instance billing mode. Valid values:\n<li>0: pay-as-you-go.</li>"
      },
      {
        "name": "ClientToken",
        "desc": "Client token."
      },
      {
        "name": "PreExecutedFileSettings",
        "desc": "Bootstrap script settings."
      },
      {
        "name": "TaskCount",
        "desc": "Number of task nodes added."
      },
      {
        "name": "CoreCount",
        "desc": "Number of core nodes added."
      },
      {
        "name": "UnNecessaryNodeList",
        "desc": "Process not required during scale-out."
      },
      {
        "name": "RouterCount",
        "desc": "Number of router nodes added."
      },
      {
        "name": "SoftDeployInfo",
        "desc": "Deployed service.\n<li>`SoftDeployInfo` and `ServiceNodeInfo` are in the same group and mutually exclusive with `UnNecessaryNodeList`.</li>\n<li>The combination of `SoftDeployInfo` and `ServiceNodeInfo` is recommended.</li>"
      },
      {
        "name": "ServiceNodeInfo",
        "desc": "Started process."
      },
      {
        "name": "DisasterRecoverGroupIds",
        "desc": "List of spread placement group IDs. Only one can be specified currently."
      },
      {
        "name": "Tags",
        "desc": "List of tags bound to added nodes."
      },
      {
        "name": "HardwareResourceType",
        "desc": ""
      },
      {
        "name": "PodSpec",
        "desc": ""
      }
    ],
    "desc": "This API is used to scale out instance."
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "DisplayStrategy",
        "desc": "Cluster filtering policy. Valid values:\n<li>clusterList: queries the list of clusters except terminated ones.</li>\n<li>monitorManage: queries the list of clusters except those that have been terminated, are being created, or failed to be created.</li>\n<li>cloudHardwareManage/componentManage: reserved fields with the same meaning as `monitorManage`.</li>"
      },
      {
        "name": "InstanceIds",
        "desc": "Queries by one or more instance IDs in the format of `emr-xxxxxxxx`. For the format of this parameter, please see the `id.N` section in [API Overview](https://intl.cloud.tencent.com/document/api/213/15688). If no instance ID is entered, the list of all instances under this `APPID` will be returned."
      },
      {
        "name": "Offset",
        "desc": "Page number. Default value: 0, indicating the first page."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results per page. Default value: 10. Maximum value: 100"
      },
      {
        "name": "ProjectId",
        "desc": "ID of the project to which the instance belongs. This parameter can be obtained from the `projectId` field in the return value of the `DescribeProject` API. If this value is -1, the list of all instances will be returned."
      },
      {
        "name": "OrderField",
        "desc": "Sorting field. Valid values:\n<li>clusterId: sorts by cluster ID.</li>\n<li>addTime: sorts by instance creation time.</li>\n<li>status: sorts by instance status code.</li>"
      },
      {
        "name": "Asc",
        "desc": "Sorts according to `OrderField` in ascending or descending order. Valid values:\n<li>0: descending order.</li>\n<li>1: ascending order.</li>Default value: 0.\u0007"
      }
    ],
    "desc": "This API is used to query EMR instances."
  },
  "InquiryPriceUpdateInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "Time unit of scaling. Valid values:\n<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>"
      },
      {
        "name": "TimeSpan",
        "desc": "Duration of scaling, which needs to be used together with `TimeUnit`.\n<li>When `PayMode` is 0, `TimeSpan` can only be 3,600.</li>"
      },
      {
        "name": "UpdateSpec",
        "desc": "Target node specification."
      },
      {
        "name": "PayMode",
        "desc": "Instance billing mode. Valid values:\n<li>0: pay-as-you-go.</li>"
      },
      {
        "name": "Placement",
        "desc": "Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance."
      },
      {
        "name": "Currency",
        "desc": "Currency."
      }
    ],
    "desc": "This API is used to query price of scaling."
  },
  "DescribeClusterNodes": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Cluster instance ID in the format of emr-xxxxxxxx"
      },
      {
        "name": "NodeFlag",
        "desc": "Node flag. Valid values:\n<li>all: gets the information of nodes in all types except TencentDB information.</li>\n<li>master: gets master node information.</li>\n<li>core: gets core node information.</li>\n<li>task: gets task node information.</li>\n<li>common: gets common node information.</li>\n<li>router: gets router node information.</li>\n<li>db: gets TencentDB information in normal status.</li>\nNote: only the above values are supported for the time being. Entering other values will cause errors."
      },
      {
        "name": "Offset",
        "desc": "Page number. Default value: 0, indicating the first page."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results per page. Default value: 100. Maximum value: 100"
      },
      {
        "name": "HardwareResourceType",
        "desc": ""
      },
      {
        "name": "SearchFields",
        "desc": ""
      }
    ],
    "desc": "This API is used to query the information of a hardware node."
  },
  "InquiryPriceRenewInstance": {
    "params": [
      {
        "name": "TimeSpan",
        "desc": "How long the instance will be renewed for, which needs to be used together with `TimeUnit`."
      },
      {
        "name": "ResourceIds",
        "desc": "List of resource IDs of the node to be renewed. The resource ID is in the format of `emr-vm-xxxxxxxx`. A valid resource ID can be queried in the [console](https://console.cloud.tencent.com/emr/static/hardware)."
      },
      {
        "name": "Placement",
        "desc": "Location of the instance. This parameter is used to specify the AZ, project, and other attributes of the instance."
      },
      {
        "name": "PayMode",
        "desc": "Instance billing mode."
      },
      {
        "name": "TimeUnit",
        "desc": "Unit of time for instance renewal."
      },
      {
        "name": "Currency",
        "desc": "Currency."
      }
    ],
    "desc": "This API is used to query the price for renewal."
  },
  "CreateInstance": {
    "params": [
      {
        "name": "ProductId",
        "desc": "Product ID. Different product IDs represent different EMR product versions. Valid values:\n<li>1: EMR v1.3.1.</li>\n<li>2: EMR v2.0.1.</li>\n<li>4: EMR v2.1.0.</li>\n<li>7: EMR v3.0.0.</li>"
      },
      {
        "name": "VPCSettings",
        "desc": "Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc."
      },
      {
        "name": "Software",
        "desc": "List of deployed components. Different required components need to be selected for different EMR product IDs (i.e., `ProductId`; for specific meanings, please see the `ProductId` field in the input parameter):\n<li>When `ProductId` is 1, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>\n<li>When `ProductId` is 2, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>\n<li>When `ProductId` is 4, the required components include hadoop-2.8.4, knox-1.2.0, and zookeeper-3.4.9</li>\n<li>When `ProductId` is 7, the required components include hadoop-3.1.2, knox-1.2.0, and zookeeper-3.4.9</li>"
      },
      {
        "name": "ResourceSpec",
        "desc": "Node resource specification."
      },
      {
        "name": "SupportHA",
        "desc": "Whether to enable high node availability. Valid values:\n<li>0: does not enable high availability of node.</li>\n<li>1: enables high availability of node.</li>"
      },
      {
        "name": "InstanceName",
        "desc": "Instance name.\n<li>Length limit: 6-36 characters.</li>\n<li>Only letters, numbers, dashes (-), and underscores (_) are supported.</li>"
      },
      {
        "name": "PayMode",
        "desc": "Instance billing mode. Valid values:\n<li>0: pay-as-you-go.</li>"
      },
      {
        "name": "Placement",
        "desc": "Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance."
      },
      {
        "name": "TimeSpan",
        "desc": "Purchase duration of instance, which needs to be used together with `TimeUnit`.\n<li>When `TimeUnit` is `s`, this parameter can only be filled with 3600, indicating a pay-as-you-go instance.</li>\n<li>When `TimeUnit` is `m`, the number entered in this parameter indicates the purchase duration of the monthly-subscription instance; for example, 1 means one month</li>"
      },
      {
        "name": "TimeUnit",
        "desc": "Time unit of instance purchase duration. Valid values:\n<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>\n<li>m: month. When `PayMode` is 1, `TimeUnit` can only be `m`.</li>"
      },
      {
        "name": "LoginSettings",
        "desc": "Instance login settings. This parameter allows you to set the login password or key for your purchased node.\n<li>If the key is set, the password will be only used for login to the native component WebUI.</li>\n<li>If the key is not set, the password will be used for login to all purchased nodes and the native component WebUI.</li>"
      },
      {
        "name": "COSSettings",
        "desc": "Parameter required for enabling COS access."
      },
      {
        "name": "SgId",
        "desc": "Security group to which an instance belongs in the format of `sg-xxxxxxxx`. This parameter can be obtained from the `SecurityGroupId` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) API."
      },
      {
        "name": "PreExecutedFileSettings",
        "desc": "Bootstrap script settings."
      },
      {
        "name": "AutoRenew",
        "desc": "Whether auto-renewal is enabled. Valid values:\n<li>0: auto-renewal not enabled.</li>\n<li>1: auto-renewal enabled.</li>"
      },
      {
        "name": "ClientToken",
        "desc": "Client token."
      },
      {
        "name": "NeedMasterWan",
        "desc": "Whether to enable public IP access for master node. Valid values:\n<li>NEED_MASTER_WAN: enables public IP for master node.</li>\n<li>NOT_NEED_MASTER_WAN: does not enable.</li>Public IP is enabled for master node by default."
      },
      {
        "name": "RemoteLoginAtCreate",
        "desc": "Whether to enable remote public network login, i.e., port 22. When `SgId` is not empty, this parameter does not take effect."
      },
      {
        "name": "CheckSecurity",
        "desc": "Whether to enable secure cluster. 0: no; other values: yes."
      },
      {
        "name": "ExtendFsField",
        "desc": "Accesses to external file system."
      },
      {
        "name": "Tags",
        "desc": "Tag description list. This parameter is used to bind a tag to a resource instance."
      },
      {
        "name": "DisasterRecoverGroupIds",
        "desc": "List of spread placement group IDs. Only one can be specified currently."
      },
      {
        "name": "CbsEncrypt",
        "desc": "CBS disk encryption at the cluster level. 0: not encrypted, 1: encrypted"
      },
      {
        "name": "MetaType",
        "desc": "Hive-shared metadatabase type. Valid values:\n<li>EMR_DEFAULT_META: the cluster creates one by default.</li>\n<li>EMR_EXIST_META: the cluster uses the specified EMR-MetaDB instance.</li>\n<li>USER_CUSTOM_META: the cluster uses a custom MetaDB instance.</li>"
      },
      {
        "name": "UnifyMetaInstanceId",
        "desc": "EMR-MetaDB instance"
      },
      {
        "name": "MetaDBInfo",
        "desc": "Custom MetaDB instance information"
      }
    ],
    "desc": "This API is used to create EMR instance."
  },
  "InquiryPriceCreateInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "Time unit of instance purchase duration. Valid values:\n<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>"
      },
      {
        "name": "TimeSpan",
        "desc": "Purchase duration of instance, which needs to be used together with `TimeUnit`.\n<li>When `TimeUnit` is `s`, this parameter can only be filled with 3600, indicating a pay-as-you-go instance.</li>\n<li>When `TimeUnit` is `m`, the number entered in this parameter indicates the purchase duration of the monthly-subscription instance; for example, 1 means one month</li>"
      },
      {
        "name": "ResourceSpec",
        "desc": "Node specification queried for price."
      },
      {
        "name": "Currency",
        "desc": "Currency."
      },
      {
        "name": "PayMode",
        "desc": "Instance billing mode. Valid values:\n<li>0: pay-as-you-go.</li>"
      },
      {
        "name": "SupportHA",
        "desc": "Whether to enable high availability of node. Valid values:\n<li>0: does not enable high availability of node.</li>\n<li>1: enables high availability of node.</li>"
      },
      {
        "name": "Software",
        "desc": "List of deployed components. Different required components need to be selected for different EMR product IDs (i.e., `ProductId`; for specific meanings, please see the `ProductId` field in the input parameter):\n<li>When `ProductId` is 1, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>\n<li>When `ProductId` is 2, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>\n<li>When `ProductId` is 4, the required components include hadoop-2.8.4, knox-1.2.0, and zookeeper-3.4.9</li>\n<li>When `ProductId` is 7, the required components include hadoop-3.1.2, knox-1.2.0, and zookeeper-3.4.9</li>"
      },
      {
        "name": "Placement",
        "desc": "Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance."
      },
      {
        "name": "VPCSettings",
        "desc": "Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc."
      },
      {
        "name": "MetaType",
        "desc": "Hive-shared metadatabase type. Valid values:\n<li>EMR_DEFAULT_META: the cluster creates one by default.</li>\n<li>EMR_EXIST_META: the cluster uses the specified EMR-MetaDB instance.</li>\n<li>USER_CUSTOM_META: the cluster uses a custom MetaDB instance.</li>"
      },
      {
        "name": "UnifyMetaInstanceId",
        "desc": "EMR-MetaDB instance"
      },
      {
        "name": "MetaDBInfo",
        "desc": "Custom MetaDB instance information"
      },
      {
        "name": "ProductId",
        "desc": "Product ID. Different product IDs represent different EMR product versions. Valid values:\n<li>1: EMR v1.3.1.</li>\n<li>2: EMR v2.0.1.</li>\n<li>4: EMR v2.1.0.</li>\n<li>7: EMR v3.0.0.</li>"
      }
    ],
    "desc": "This API is used to query price of instance creation."
  },
  "InquiryPriceScaleOutInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "Time unit of scale-out. Valid values:\n<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>"
      },
      {
        "name": "TimeSpan",
        "desc": "Duration of scale-out, which needs to be used together with `TimeUnit`.\n<li>When `PayMode` is 0, `TimeSpan` can only be 3,600.</li>"
      },
      {
        "name": "ZoneId",
        "desc": "ID of the AZ where an instance resides."
      },
      {
        "name": "PayMode",
        "desc": "Instance billing mode. Valid values:\n<li>0: pay-as-you-go.</li>"
      },
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "CoreCount",
        "desc": "Number of core nodes added."
      },
      {
        "name": "TaskCount",
        "desc": "Number of task nodes added."
      },
      {
        "name": "Currency",
        "desc": "Currency."
      },
      {
        "name": "RouterCount",
        "desc": "Number of router nodes added."
      }
    ],
    "desc": "This API is used to query price of scale-out."
  },
  "TerminateTasks": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "ResourceIds",
        "desc": "List of resource IDs of the node to be terminated. The resource ID is in the format of `emr-vm-xxxxxxxx`. A valid resource ID can be queried in the [console](https://console.cloud.tencent.com/emr/static/hardware)."
      }
    ],
    "desc": "This API is used to terminate a task node."
  },
  "TerminateInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "ResourceIds",
        "desc": "ID of terminated node. This parameter is reserved and does not need to be configured."
      }
    ],
    "desc": "This API is used to terminate an EMR instance. It is only supported in the official paid edition of EMR."
  }
}