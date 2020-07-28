# -*- coding: utf-8 -*-
DESC = "cbs-2017-03-12"
INFO = {
  "DescribeInstancesDiskNum": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "ID of the CVM instance can be queried via the API [DescribeInstances](/document/product/213/15728)."
      }
    ],
    "desc": "This API (DescribeInstancesDiskNum) is used to query the number of cloud disks mounted in the instance.\n\n* Batch operations are supported. If multiple CVM instance IDs are specified, the returned results will list the number of cloud disks mounted on each CVM."
  },
  "InquiryPriceResizeDisk": {
    "params": [
      {
        "name": "DiskId",
        "desc": "ID of the cloud disk, which can be queried via the API [DescribeDisks](/document/product/362/16315)."
      },
      {
        "name": "DiskSize",
        "desc": "Cloud disk size after scale out (in GB). This cannot be smaller than the current size of the cloud disk. For the value range of the cloud disk sizes, see cloud disk [Product Types](/document/product/362/2353)."
      },
      {
        "name": "ProjectId",
        "desc": "ID of project the cloud disk belongs to. If selected, it can only be used for authentication."
      }
    ],
    "desc": "This API is used to query the price for expanding cloud disks."
  },
  "DescribeAutoSnapshotPolicies": {
    "params": [
      {
        "name": "AutoSnapshotPolicyIds",
        "desc": "List of scheduled snapshot policy IDs to be queried. The parameter does not support specifying both `SnapshotIds` and `Filters`."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions. Specification of both the `AutoSnapshotPolicyIds` and `Filters` parameters is not supported.<br><li>auto-snapshot-policy-id - Array of String - Required or not: No - (Filter condition) Filters according to the scheduled snapshot policy ID. The format of the scheduled snapshot policy ID is as follows: `asp-11112222`. <br><li>auto-snapshot-policy-state - Array of String - Required or not: No - (Filter condition) Filters according to the status of the scheduled snapshot policy. The format of the scheduled snapshot policy ID is as follows: `asp-11112222`. (NORMAL: normal | ISOLATED: isolated)<br><li>auto-snapshot-policy-name - Array of String - Required or not: No - (Filter condition) Filters according to the name of the scheduled snapshot policy."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](/document/product/362/15633)."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](/document/product/362/15633)."
      },
      {
        "name": "Order",
        "desc": "Outputs the ordering of the scheduled snapshot lists. Value range: <br><li>ASC: Ascending order <br><li>DESC: Descending order."
      },
      {
        "name": "OrderField",
        "desc": "The sorting filter applied to the scheduled snapshot list. Value range: <Sort by creation time of scheduled snapshot. By default, this is sorted by creation time."
      }
    ],
    "desc": "This API (DescribeAutoSnapshotPolicies) is used to query scheduled snapshot policies.\n\n* You can query the detailed information of scheduled snapshot policies by ID, name, or status. Insert `AND` between different values. For details on filtering information, see `Filter`.\n* If the parameter is empty, a certain number (specified by `Limit`; the default is 20) of the scheduled snapshot policy lists are returned to the current user.\n"
  },
  "AttachDisks": {
    "params": [
      {
        "name": "DiskIds",
        "desc": "ID of the elastic cloud disk to be mounted, which can be queried through the API [DescribeDisks](/document/product/362/16315). A maximum of 10 elastic cloud disks can be mounted in a single request."
      },
      {
        "name": "InstanceId",
        "desc": "ID of the CVM instance on which the cloud disk will be mounted. It can be queried via the API [DescribeInstances](/document/product/213/15728)."
      },
      {
        "name": "DeleteWithInstance",
        "desc": "Optional parameter. If this is not passed only the mount operation is executed. If `True` is passed, the cloud disk will be configured to be terminated when the server it is mounted to is terminated. This is only valid for pay-as-you-go cloud disks."
      }
    ],
    "desc": "This API (AttachDisks) is used to mount cloud disks.\n \n* Batch operations are supported. Multiple cloud disks can be mounted to a CVM. If there is a cloud disk that does not allow this operation, the operation is not performed and a specific error code is returned.\n* This API is an asynchronous API. If the request for mounting the cloud disk successfully returns results, the operation of mounting cloud disk has been initiated at the background. You can use the API [DescribeDisks](/document/product/362/16315) to query the cloud disk status. If the status changes from \"ATTACHING\" to \"ATTACHED\", the cloud disk is mounted."
  },
  "ModifyAutoSnapshotPolicyAttribute": {
    "params": [
      {
        "name": "AutoSnapshotPolicyId",
        "desc": "Scheduled snapshot policy ID."
      },
      {
        "name": "Policy",
        "desc": "The policy for executing the scheduled snapshot."
      },
      {
        "name": "AutoSnapshotPolicyName",
        "desc": "The name of the scheduled snapshot policy to be created. If it is left empty, the default is 'Not named'. The maximum length cannot exceed 60 bytes."
      },
      {
        "name": "IsActivated",
        "desc": "Whether or not the scheduled snapshot policy is activated. FALSE: Not activated. TRUE: Activated. The default value is TRUE."
      },
      {
        "name": "IsPermanent",
        "desc": "Whether the snapshot created by this scheduled snapshot policy is retained permanently. FALSE: Not retained permanently. TRUE: Retained permanently. The default value is FALSE."
      },
      {
        "name": "RetentionDays",
        "desc": "The number of days for which snapshots created by this policy are retained. This parameter cannot clash with `IsPermanent`, which is, if the scheduled snapshot policy is configured to retain permanently, `RetentionDays` must be 0."
      }
    ],
    "desc": "This API (ModifyAutoSnapshotPolicyAttribute) is used to modify the attributes of an automatic snapshot policy.\n\n* You can use this API to modify the attributes of a scheduled snapshot policy, including the execution policy, name, and activation.\n* When modifying the number of days for retention, you must ensure that there is no clash with the permanent retention attribute. Otherwise, the entire operation will fail and a specific error code will be returned."
  },
  "InquiryPriceCreateDisks": {
    "params": [
      {
        "name": "DiskType",
        "desc": "Type of cloud hard disk. Value range: <br><li>Ordinary cloud disk: CLOUD_BASIC <br><li>Premium cloud storage: CLOUD_PREMIUM <br><li>SSD cloud disk: CLOUD_SSD."
      },
      {
        "name": "DiskSize",
        "desc": "Cloud disk size (in GB). For the value range of the cloud disk sizes, see cloud disk [Product Types](/document/product/362/2353)."
      },
      {
        "name": "DiskChargeType",
        "desc": "Cloud disk billing method. <br><li>POSTPAID_BY_HOUR: Pay-as-you-go on an hourly basis"
      },
      {
        "name": "DiskChargePrepaid",
        "desc": "Relevant parameter settings for the prepaid mode (i.e., monthly subscription). The monthly subscription cloud disk purchase attributes such as usage period and whether or not auto-renewal is set up can be specified using this parameter. <br>This parameter is required when creating a prepaid cloud disk. This parameter is not required when creating an hourly postpaid cloud disk."
      },
      {
        "name": "DiskCount",
        "desc": "Quantity of cloud disks purchased. If left empty, default is 1."
      },
      {
        "name": "ProjectId",
        "desc": "ID of project the cloud disk belongs to."
      }
    ],
    "desc": "This API (InquiryPriceCreateDisks) is used to inquire the price for cloud disk creation.\n\n* It supports inquiring the price for the creation of multiple cloud disks. The total price for the creation is returned."
  },
  "DescribeDiskOperationLogs": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions. The following conditions are supported:\n<li>disk-id - Array of String - Required or not: Yes - Filter by cloud disk ID, with maximum of 10 cloud disk IDs able to be specified per request."
      },
      {
        "name": "BeginTime",
        "desc": "The start time of the operation logs to be queried, for example: '2019-11-22 00:00:00\""
      },
      {
        "name": "EndTime",
        "desc": "The end time of the operation logs to be queried, for example: '2019-11-22 23:59:59\""
      }
    ],
    "desc": "This API (DescribeDiskOperationLogs) is used to query a list of cloud disk operation logs.\n\nThis can be filtered according to the cloud disk ID. The format of cloud disk IDs is as follows: disk-a1kmcp13.\n"
  },
  "DeleteAutoSnapshotPolicies": {
    "params": [
      {
        "name": "AutoSnapshotPolicyIds",
        "desc": "List of scheduled snapshot policy IDs to be deleted."
      }
    ],
    "desc": "This API (DeleteAutoSnapshotPolicies) is used to delete scheduled snapshot policies.\n\n* Batch operations are supported. If one of the scheduled snapshot policies in a batch cannot be deleted, the operation is not performed and a specific error code is returned."
  },
  "DescribeDisks": {
    "params": [
      {
        "name": "DiskIds",
        "desc": "Query by one or more cloud disk IDs, such as `disk-11112222`. For the format of this parameter, please see the ids.N section of the API [Introduction](/document/product/362/15633). This parameter does not support specifying both `DiskIds` and `Filters`."
      },
      {
        "name": "Filters",
        "desc": "Filters. You cannot specify `DiskIds` and `Filters` at the same time. <br><li>disk-usage - Array of String - Optional - Filters by cloud disk type. (SYSTEM_DISK: system disk | DATA_DISK: data disk) <br><li>disk-charge-type - Array of String - Optional - Filters by cloud disk billing method. (POSTPAID_BY_HOUR: pay-as-you-go) <br><li>portable - Array of String- Optional - Filters by whether the cloud disk is elastic or not. (TRUE: elastic | FALSE: non-elastic) <br><li>project-id - Array of Integer - Optional - Filters by the ID of the project to which a cloud disk belongs. <br><li>disk-id - Array of String - Optional - Filters by cloud disk ID, such as `disk-11112222`. <br><li>disk-name - Array of String - Optional - Filters by cloud disk name. <br><li>disk-type - Array of String - Optional - Filters by cloud disk media type (CLOUD_BASIC: HDD cloud disk | CLOUD_PREMIUM: Premium Cloud Storage | CLOUD_SSD: SSD cloud disk.) <br><li>disk-state - Array of String - Optional - Filters by cloud disk state. (UNATTACHED: not mounted | ATTACHING: being mounted | ATTACHED: mounted | DETACHING: being unmounted | EXPANDING: being expanded | ROLLBACKING: being rolled back | TORECYCLE: to be repossessed.) <br><li>instance-id - Array of String - Optional - Filters by the ID of the CVM instance on which a cloud disk is mounted. You can use this parameter to query the cloud disks mounted on specific CVMs. <br><li>zone - Array of String - Optional - Filters by [availability zone](/document/product/213/15753#ZoneInfo) <br><li>instance-ip-address - Array of String - Optional - Filters by the private or public IP of the CVM on which a cloud disk is mounted. <br><li>instance-name - Array of String - Optional - Filters by the name of the instance on which a cloud disk is mounted. <br><li>tag-key - Array of String - Optional - Filters by tag key. <br><li>tag-value - Array of String - Optional - Filters by tag value. <br><li>tag:tag-key - Array of String - Optional - Filters by tag key-value pair. Please replace `tag-key` with a specific tag key."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](/document/product/362/15633)."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](/document/product/362/15633)."
      },
      {
        "name": "Order",
        "desc": "Outputs the ordering of the cloud disk list. Value range: <br><li>ASC: Ascending order <br><li>DESC: Descending order."
      },
      {
        "name": "OrderField",
        "desc": "The field by which the cloud disk list is sorted. Value range: <br><li>CREATE_TIME: sorted by the creation time of cloud disks <br><li>DEADLINE: sorted by the expiration time of cloud disks<br>By default, the cloud disk list is sorted by the creation time of cloud disks."
      },
      {
        "name": "ReturnBindAutoSnapshotPolicy",
        "desc": "Whether the ID of the periodic snapshot policy bound to the cloud disk needs to be returned in the cloud disk details. TRUE: return; FALSE: do not return."
      }
    ],
    "desc": "This API (DescribeDisks) is used to query the list of cloud disks.\n\n* The details of the cloud disk can be queried based on the ID, type or status of the cloud disk. The relationship between different conditions is AND. For more information about filtering, please see the `Filter`.\n* If the parameter is empty, a certain number (specified by `Limit`; the default is 20) of cloud disk lists are returned to the current user."
  },
  "CreateDisks": {
    "params": [
      {
        "name": "DiskType",
        "desc": "Type of hard disk medium. Value range: <br><li>CLOUD_BASIC: Ordinary cloud disk <br><li>CLOUD_PREMIUM: Premium cloud storage <br><li>CLOUD_SSD: SSD cloud disk."
      },
      {
        "name": "DiskChargeType",
        "desc": "Cloud disk billing method. POSTPAID_BY_HOUR: pay as you go by hour<br><li>CDCPAID: Billed together with the bound dedicated cluster<br>For information about the pricing of each method, see the cloud disk [Pricing Overview](/document/product/362/2413)."
      },
      {
        "name": "Placement",
        "desc": "The location of the instance. The availability zone and the project that the instance belongs to can be specified using this parameter. If the project is not specified, it will be created under the default project."
      },
      {
        "name": "DiskName",
        "desc": "The displayed name of the cloud disk. If it is left empty, the default is 'Not named'. The maximum length cannot exceed 60 bytes."
      },
      {
        "name": "DiskCount",
        "desc": "If the number of cloud disks to be created is left empty, the default is 1. There is a limit to the maximum number of cloud disks that can be created for a single request. For more information, please see [CBS Use Limits](https://cloud.tencent.com/doc/product/362/5145)."
      },
      {
        "name": "DiskChargePrepaid",
        "desc": "Relevant parameter settings for the prepaid mode (i.e., monthly subscription). The monthly subscription cloud disk purchase attributes such as usage period and whether or not auto-renewal is set up can be specified using this parameter. <br>This parameter is required when creating a prepaid cloud disk. This parameter is not required when creating an hourly postpaid cloud disk. "
      },
      {
        "name": "DiskSize",
        "desc": "Cloud hard disk size (in GB). <br><li> If `SnapshotId` is passed, `DiskSize` cannot be passed. In this case, the size of the cloud disk is the size of the snapshot. <br><li>To pass `SnapshotId` and `DiskSize` at the same time, the size of the disk must be larger than or equal to the size of the snapshot. <br><li>For information about the size range of cloud disks, see cloud disk [Product Types](/document/product/362/2353)."
      },
      {
        "name": "SnapshotId",
        "desc": "Snapshot ID. If this parameter is specified, the cloud disk is created based on the snapshot. The snapshot type must be a data disk snapshot. The snapshot can be queried in the DiskUsage field in the output parameter through the API [DescribeSnapshots](/document/product/362/15647)."
      },
      {
        "name": "ClientToken",
        "desc": "A string to ensure the idempotency of the request, which is generated by the client. Each request shall have a unique string with a maximum of 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be ensured."
      },
      {
        "name": "Encrypt",
        "desc": "This parameter is used to create an encrypted cloud disk. Its value is always ENCRYPT."
      },
      {
        "name": "Tags",
        "desc": "Cloud disk binding tag."
      },
      {
        "name": "Shareable",
        "desc": "The default of optional parameter is False. When True is selected, the cloud disk will be created as a shareable cloud disk."
      }
    ],
    "desc": "This API is used to create one or more cloud disks.\n\n* This API supports creating a cloud disk with a data disk snapshot so that the snapshot data can be copied to the purchased cloud disk.\n* This API is an async API. A cloud disk ID list will be returned when a request is made successfully, but it does not mean that the creation has been completed. You can call the [DescribeDisks](/document/product/362/16315) API to query cloud disks by `DiskId`. If a new cloud disk can be found and its state is 'UNATTACHED' or 'ATTACHED', it means that the cloud disk has been created successfully."
  },
  "ModifyDiskAttributes": {
    "params": [
      {
        "name": "DiskIds",
        "desc": "IDs of one or more cloud disks to be operated. If multiple cloud disk IDs are selected, it only supports modifying all cloud disks with the same attributes."
      },
      {
        "name": "ProjectId",
        "desc": "The new project ID of the cloud disk. Only the project ID of elastic cloud disk can be modified. The available projects and their IDs can be queried via the API [DescribeProject](/document/api/378/4400)."
      },
      {
        "name": "DiskName",
        "desc": "Name of new cloud disk."
      },
      {
        "name": "Portable",
        "desc": "Whether it is an elastic cloud disk. FALSE: non-elastic cloud disk; TRUE: elastic cloud disk. You can only modify non-elastic cloud disks to elastic cloud disks."
      },
      {
        "name": "DeleteWithInstance",
        "desc": "Whether the cloud disk is terminated with the CVM after it has been successfully mounted. `TRUE` indicates that it is terminated with the CVM. `FALSE` indicates that it is not terminated with the CVM. This is only supported for cloud disks and data disks that are pay-as-you-go."
      },
      {
        "name": "DiskType",
        "desc": "When changing the type of a cloud disk, this parameter can be passed to indicate the desired cloud disk type. Value range: <br><li>CLOUD_PREMIUM: Premium cloud storage.  <br><li>CLOUD_SSD: SSD cloud disk. <br>Currently, batch operations are not supported for changing type. That is, when `DiskType` is passed, only one cloud disk can be passed through `DiskIds`. <br>When the cloud disk type is changed, the changing of other attributes is not supported concurrently."
      }
    ],
    "desc": "* Only the project ID of elastic cloud disk can be modified. The project ID of the cloud disk created with the CVM is linked with the CVM. The project ID can be can be queried in the Portable field in the output parameters through the API [DescribeDisks](/document/product/362/16315).\n* \"Cloud disk name\" is only used by users for their management. Tencent Cloud does not use the name as the basis for ticket submission or cloud disk management.\n* Batch operations are supported. If multiple cloud disk IDs are specified, all the specified cloud disks must have the same attribute. If there is a cloud disk that does not allow this operation, the operation is not performed and a specific error code is returned."
  },
  "DeleteSnapshots": {
    "params": [
      {
        "name": "SnapshotIds",
        "desc": "List of IDs of snapshots to be deleted, which can be queried via [DescribeSnapshots](/document/product/362/15647)."
      }
    ],
    "desc": "This API (DeleteSnapshots) is used to delete snapshots.\n\n* The snapshot must be in NORMAL status. The snapshot status can be queried in the SnapshotState field in the output parameters through the API [DescribeSnapshots](/document/product/362/15647).\n* Batch operations are supported. If one of the snapshots in a batch cannot be deleted, the operation is not performed and a specific error code is returned."
  },
  "ModifySnapshotAttribute": {
    "params": [
      {
        "name": "SnapshotId",
        "desc": "Snapshot ID, which can be queried via [DescribeSnapshots](/document/product/362/15647)."
      },
      {
        "name": "SnapshotName",
        "desc": "Name of new snapshot. Maximum length is 60 bytes."
      },
      {
        "name": "IsPermanent",
        "desc": "The retention time of the snapshot. FALSE: non-permanent retention; TRUE: permanent retention. You can only modify non-permanent snapshots to permanent snapshots."
      }
    ],
    "desc": "This API (ModifySnapshotAttribute) is used to modify the attributes of a specified snapshot.\n\n* Currently, you can only modify snapshot name and change non-permanent snapshots into permanent snapshots.\n* \"Snapshot name\" is only used by users for their management. Tencent Cloud does not use the name as the basis for ticket submission or snapshot management."
  },
  "DescribeDiskAssociatedAutoSnapshotPolicy": {
    "params": [
      {
        "name": "DiskId",
        "desc": "The ID of the queried cloud disk."
      }
    ],
    "desc": "This API (DescribeDiskAssociatedAutoSnapshotPolicy) is used to query the scheduled snapshot policy bound to a cloud disk."
  },
  "BindAutoSnapshotPolicy": {
    "params": [
      {
        "name": "AutoSnapshotPolicyId",
        "desc": "ID of scheduled snapshot policy to be bound."
      },
      {
        "name": "DiskIds",
        "desc": "List of cloud disk IDs to be bound. Maximum of 80 cloud disks can be bound per request."
      }
    ],
    "desc": "This API (BindAutoSnapshotPolicy) is used to bind the cloud disk to the specified scheduled snapshot policy.\n\n* For the scheduled snapshot policy limit of each region, see [Scheduled Snapshots](/document/product/362/8191).\n* When a cloud disk that is bound to a scheduled snapshot policy is in the unused state (that is, an elastic cloud disk has not been mounted or the server of an inelastic disk is powered off) scheduled snapshots are not created."
  },
  "DescribeSnapshots": {
    "params": [
      {
        "name": "SnapshotIds",
        "desc": "List of snapshot IDs to be queried. The parameter does not support specifying both `SnapshotIds` and `Filters`."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions. The specification of both the `SnapshotIds` and `Filters` parameters is not supported. <br><li>snapshot-id - Array of String - Required or not: No - (Filter condition) Filter by the snapshot ID. The format of the snapshot ID is as follows: `snap-11112222`. <br><li>snapshot-name - Array of String - Required or not: No - (Filter condition) Filter by the snapshot name. <br><li>snapshot-state - Array of String - Required or not: No - (Filter condition) Filter by the snapshot status (NORMAL: normal | CREATING: creating | ROLLBACKING: rolling back). <br><li>disk-usage - Array of String - Required or not: No - (Filter condition) Filter by the type of the cloud disk for which the snapshot is created (SYSTEM_DISK: system disk | DATA_DISK: data disk). <br><li>project-id - Array of String - Required or not: No - (Filter condition) Filter by ID of the project to which the cloud disk belongs. <br><li>disk-id - Array of String - Required or not: No - (Filter condition) Filter by the ID of the cloud disk for which the snapshot is created. <br><li>zone - Array of String - Required or not: No - (Filter condition) Filter by [Availability Zone](/document/product/213/15753#ZoneInfo). <br><li>encrypt - Array of String - Required or not: No - (Filter condition) According to whether it is an encrypted disk snapshot. (TRUE: indicates an encrypted disk snapshot | FALSE: indicates that it is not an encrypted disk snapshot.)"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](/document/product/362/15633)."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](/document/product/362/15633)."
      },
      {
        "name": "Order",
        "desc": "Outputs the ordering of the cloud disk list. Value range: <br><li>ASC: Ascending order <br><li>DESC: Descending order."
      },
      {
        "name": "OrderField",
        "desc": "The field by which the snapshot list is sorted. Value range: <br><li>CREATE_TIME: sorted by the creation time of the snapshots <br>By default, the snapshot list is sorted by the creation time of snapshots."
      }
    ],
    "desc": "This API (DescribeSnapshots) is used to query the details of snapshots.\n\n* Filter the results by the snapshot ID, the ID of cloud disk, for which the snapshot is created, and the type of cloud disk, for which the snapshot is created. The relationship between different conditions is AND. For more information about filtering, please see `Filter`.\n* If the parameter is empty, a certain number (specified by `Limit`; the default is 20) of snapshot lists are returned to the current user."
  },
  "DescribeSnapshotSharePermission": {
    "params": [
      {
        "name": "SnapshotId",
        "desc": "The ID of the snapshot to be queried. You can obtain this by using [DescribeSnapshots](https://cloud.tencent.com/document/api/362/15647)."
      }
    ],
    "desc": "This API is used to query the sharing information of snapshots."
  },
  "CreateAutoSnapshotPolicy": {
    "params": [
      {
        "name": "Policy",
        "desc": "The policy for executing the scheduled snapshot."
      },
      {
        "name": "AutoSnapshotPolicyName",
        "desc": "The name of the scheduled snapshot policy to be created. If it is left empty, the default is 'Not named'. The maximum length cannot exceed 60 bytes."
      },
      {
        "name": "IsActivated",
        "desc": "Whether or not the scheduled snapshot policy is activated. FALSE: Not activated. TRUE: Activated. The default value is TRUE."
      },
      {
        "name": "IsPermanent",
        "desc": "Whether the snapshot created by this scheduled snapshot policy is retained permanently. FALSE: Not retained permanently. TRUE: Retained permanently. The default value is FALSE."
      },
      {
        "name": "RetentionDays",
        "desc": "The number of days that a snapshot created by this scheduled snapshot policy is retained. The default value is 7. If this parameter is specified, the IsPermanent input parameter can not be TRUE, otherwise a conflict will occur."
      },
      {
        "name": "DryRun",
        "desc": "Whether to create an execution policy for the scheduled snapshot. TRUE: Only the time of the initial backup needs to be obtained, and no scheduled snapshot policy is actually created. FALSE: Create. The default value is FALSE."
      }
    ],
    "desc": "This API (CreateAutoSnapshotPolicy) is used to create a scheduled snapshot policy.\n\n* For the limits on the number of scheduled snapshot policies that can be created in each region, see [Scheduled Snapshots](/document/product/362/8191).\n* The quantity and capacity of the snapshots that can be created in each region are limited. For more information, see the **Snapshots** page on the Tencent Cloud Console. If the number of snapshots exceeds the quota, the creation of the scheduled snapshots will fail."
  },
  "TerminateDisks": {
    "params": [
      {
        "name": "DiskIds",
        "desc": "List of cloud disk IDs required to be returned."
      }
    ],
    "desc": "This API is used to return cloud disks.\n\n* You can use this API to return cloud disks you no longer need.\n* This API can be used to return pay-as-you-go cloud disks billed on hourly basis. \n* Batch operations are supported. The maximum number of cloud disks in each request is 50. If there is any specified cloud disk that cannot be returned, an error code will be returned."
  },
  "DescribeDiskConfigQuota": {
    "params": [
      {
        "name": "InquiryType",
        "desc": "Inquiry type. Value range: INQUIRY_CBS_CONFIG: query the configuration list of cloud disks <br><li>INQUIRY_CVM_CONFIG: query the configuration list of cloud disks and instances."
      },
      {
        "name": "Zones",
        "desc": "Query configuration under one or more [availability zone](/document/product/213/15753#ZoneInfo)."
      },
      {
        "name": "DiskChargeType",
        "desc": "Billing mode. Value range: <br><li>POSTPAID_BY_HOUR: postpaid."
      },
      {
        "name": "DiskTypes",
        "desc": "Type of hard disk medium. Value range: <br><li>CLOUD_BASIC: Ordinary cloud disk <br><li>CLOUD_PREMIUM: Premium cloud storage <br><li>CLOUD_SSD: SSD cloud disk."
      },
      {
        "name": "DiskUsage",
        "desc": "The system disk or data disk. Value range: <br><li>SYSTEM_DISK: System disk <br><li>DATA_DISK: Data disk."
      },
      {
        "name": "InstanceFamilies",
        "desc": "Filter by the instance model series, such as S1, I1 and M1. For more information, please see [Instance Types](https://cloud.tencent.com/document/product/213/11518)"
      },
      {
        "name": "CPU",
        "desc": "Instance CPU cores."
      },
      {
        "name": "Memory",
        "desc": "Instance memory size."
      }
    ],
    "desc": "This API (DescribeDiskConfigQuota) is used to query the cloud disk quota."
  },
  "UnbindAutoSnapshotPolicy": {
    "params": [
      {
        "name": "DiskIds",
        "desc": "List of cloud disk IDs scheduled snapshot policy to be unbound from."
      },
      {
        "name": "AutoSnapshotPolicyId",
        "desc": "ID of scheduled snapshot policy to be unbound."
      }
    ],
    "desc": "This API (UnbindAutoSnapshotPolicy) is used to unbind the cloud disk from the specified scheduled snapshot policy.\n\n* Batch operations are supported. Multiple cloud disks can be unbound from a snapshot policy at one time. \n* If the passed-in cloud disks are not bound to the current scheduled snapshot policy, they will be skipped. Only cloud disks that are bound to the current scheduled snapshot policy are processed."
  },
  "ApplySnapshot": {
    "params": [
      {
        "name": "SnapshotId",
        "desc": "Snapshot ID, which can be queried via [DescribeSnapshots](/document/product/362/15647)."
      },
      {
        "name": "DiskId",
        "desc": "ID of the original cloud disk corresponding to the snapshot, which can be queried via the API [DescribeDisks](/document/product/362/16315)."
      }
    ],
    "desc": "This API (ApplySnapshot) is used to roll back a snapshot to the original cloud disk.\n\n* The snapshot can only be rolled back to the original cloud disk. For data disk snapshots, if you need to copy the snapshot data to other cloud disks, use the API [CreateDisks](/document/product/362/16312) to create an elastic cloud disk and then copy the snapshot data to the created cloud disk. \n* The snapshot for rollback must be in NORMAL status. The snapshot status can be queried in the SnapshotState field in the output parameters through the API [DescribeSnapshots](/document/product/362/15647).\n* For elastic cloud disks, the cloud disk must be in UNMOUNTED status. The cloud disk status can be queried in the Attached field returned by the API [DescribeDisks](/document/product/362/16315). For non-elastic cloud disks purchased together with instances, the instance must be in SHUTDOWN status. The instance status can be queried through the API [DescribeInstancesStatus](/document/product/213/15738)."
  },
  "DescribeSnapshotOperationLogs": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions. The following conditions are supported:\n<li>snapshot-id - Array of String - Required or not: Yes - Filter by snapshot ID, with maximum of 10 snapshot IDs able to be specified per request."
      },
      {
        "name": "BeginTime",
        "desc": "The start time of the operation logs to be queried, for example: '2019-11-22 00:00:00\""
      },
      {
        "name": "EndTime",
        "desc": "The end time of the operation logs to be queried, for example: '2019-11-22 23:59:59\""
      }
    ],
    "desc": "This API (DescribeSnapshotOperationLogs) is used to query a list of snapshot operation logs.\n\nYou can filter according to the snapshot ID. The snapshot ID format is as follows: snap-a1kmcp13.\n"
  },
  "ModifySnapshotsSharePermission": {
    "params": [
      {
        "name": "AccountIds",
        "desc": "List of account IDs with which a snapshot is shared. For the format of array-type parameters, see [API Introduction](https://cloud.tencent.com/document/api/213/568). You can find the account ID in [Account Information](https://console.cloud.tencent.com/developer)."
      },
      {
        "name": "Permission",
        "desc": "Operations. Valid values: `SHARE`, sharing an image; `CANCEL`, cancelling the sharing of an image."
      },
      {
        "name": "SnapshotIds",
        "desc": "The ID of the snapshot. You can obtain this by using [DescribeSnapshots](https://cloud.tencent.com/document/api/362/15647)."
      }
    ],
    "desc": "This API is used to modify snapshot sharing information.\n\nAfter snapshots are shared, the accounts they are shared to can use the snapshot to create cloud disks.\n* Each snapshot can be shared to at most 50 accounts.\n* You can use a shared snapshot to create cloud disks, but you cannot change its name or description.\n* Snapshots can only be shared with accounts in the same region.\n* Only data disk snapshots can be shared."
  },
  "DetachDisks": {
    "params": [
      {
        "name": "DiskIds",
        "desc": "ID of the cloud disk to be unmounted, which can be queried through the API [DescribeDisks](/document/product/362/16315). A maximum of 10 elastic cloud disks can be unmounted in a single request."
      },
      {
        "name": "InstanceId",
        "desc": "For a cloud disk that is not shared, this parameter is ignored. For a shared cloud disk, this parameter indicates which CVM instance the cloud disk is to be unmounted from."
      }
    ],
    "desc": "This API (DetachDisks) is used to unmount cloud disks.\n\n* Batch operations are supported. Multiple cloud disks mounted to the same CVM can be unmounted in batch. If there is a cloud disk that does not allow this operation, the operation is not performed and a specific error code is returned.\n* This API is an asynchronous API. When the request successfully returns results, the cloud disk is not unmounted from the CVM immediately. You can use the API [DescribeDisks](/document/product/362/16315) to query the cloud disk status. If the status changes from \"ATTACHED\" to \"UNATTACHED\", the cloud disk is unmounted."
  },
  "GetSnapOverview": {
    "params": [],
    "desc": "This API is used to get snapshot overview information."
  },
  "ResizeDisk": {
    "params": [
      {
        "name": "DiskId",
        "desc": "ID of the cloud disk, which can be queried via the API [DescribeDisks](/document/product/362/16315)."
      },
      {
        "name": "DiskSize",
        "desc": "Cloud disk size after scale out (in GB). This must be larger than the current size of the cloud disk. For the value range of the cloud disk sizes, see cloud disk [Product Types](/document/product/362/2353)."
      }
    ],
    "desc": "This API (ResizeDisk) is used to expand the capacity of the cloud disk.\n\n* Only elastic cloud disks can be expanded. The cloud disk type can be queried in the Portable field in the output parameters through the API [DescribeDisks](/document/product/362/16315). For the cloud disk created along with the CVM, the capacity can only be expanded via the API [ResizeInstanceDisks](/document/product/213/15731).\n* This API is an asynchronous API. The cloud disk is not immediately expanded to the specified size as the API successfully returns results. You can use the API [DescribeDisks](/document/product/362/16315) to query the cloud disk status. The cloud disk in the status of \"EXPANDING\" is in the process of capacity expansion. When the status changes to \"UNATTACHED\", the capacity expansion is completed. "
  },
  "CreateSnapshot": {
    "params": [
      {
        "name": "DiskId",
        "desc": "ID of the cloud disk, for which a snapshot needs to be created. It can be queried via the API [DescribeDisks](/document/product/362/16315)."
      },
      {
        "name": "SnapshotName",
        "desc": "Snapshot name. If it is left empty, the new snapshot name is \"Not named\" by default."
      }
    ],
    "desc": "This API (CreateSnapshot) is used to create a snapshot of a specified cloud disk.\n\n* Snapshots can only be created for cloud disks with the snapshot capability. To check whether a cloud disk has the snapshot capability, see the SnapshotAbility field returned by the API [DescribeDisks](/document/product/362/16315).\n* For the number of snapshots that can be created, please see [Product Usage Restriction](https://cloud.tencent.com/doc/product/362/5145)."
  }
}