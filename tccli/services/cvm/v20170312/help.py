# -*- coding: utf-8 -*-
DESC = "cvm-2017-03-12"
INFO = {
  "CreateImage": {
    "params": [
      {
        "name": "ImageName",
        "desc": "Image name"
      },
      {
        "name": "InstanceId",
        "desc": "The ID of the instance used to create an image"
      },
      {
        "name": "ImageDescription",
        "desc": "Image description"
      },
      {
        "name": "ForcePoweroff",
        "desc": "Whether to force shut down an instance to create an image when a soft shutdown fails"
      },
      {
        "name": "Sysprep",
        "desc": "Whether to enable Sysprep when creating a Windows image"
      },
      {
        "name": "DataDiskIds",
        "desc": "The ID of the data disk used to create an image"
      },
      {
        "name": "SnapshotIds",
        "desc": "The ID of the snapshot used to create an image. A system disk snapshot must be included."
      },
      {
        "name": "DryRun",
        "desc": "Verifies the validity of the request without affecting the resources involved."
      }
    ],
    "desc": "This API is used to create a new image with the system disk of an instance. The image can be used to create new instances."
  },
  "DescribeInstancesStatus": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s) in the format of `ins-xxxxxxxx`. For more information on the format of this parameter, see the `id.N` section of [API Introduction](https://cloud.tencent.com/document/api/213/15688). The maximum number of instances in each request is 100."
      },
      {
        "name": "Offset",
        "desc": "Offset; default value: 0. For more information on `Offset`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377)."
      },
      {
        "name": "Limit",
        "desc": "Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377)."
      }
    ],
    "desc": "This API is used to query the status of instances.\n\n* You can query the status of an instance with its `ID`.\n* If no parameter is defined, the status of a certain number of instances under the current account will be returned. The number is specified by `Limit` and is 20 by default."
  },
  "ModifyImageSharePermission": {
    "params": [
      {
        "name": "ImageId",
        "desc": "Image ID such as `img-gvbnzy6f`. You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://cloud.tencent.com/document/api/213/15715) and look for `ImageId` in the response. <br><li>Look for the information in the [Image Console](https://console.cloud.tencent.com/cvm/image). <br>You can only specify an image in the `NORMAL` state. For more information on image states, see [here](/document/api/213/9452#image_state)."
      },
      {
        "name": "AccountIds",
        "desc": "List of account IDs with which an image is shared. For the format of array-type parameters, see [API Introduction](/document/api/213/568). The account ID is different from the QQ number. You can find the account ID in [Account Information](https://console.cloud.tencent.com/developer). "
      },
      {
        "name": "Permission",
        "desc": "Operations. Valid values: `SHARE`, sharing an image; `CANCEL`, cancelling an image sharing. "
      }
    ],
    "desc": "This API is used to modify image sharing information.\n\n* The accounts with which an image is shared can use the shared image to create instances.\n* Each custom image can be shared with up to 50 accounts.\n* You can use a shared image to create instances, but you cannot change its name and description.\n* If an image is shared with another account, the shared image will be in the same region as the original image.\n"
  },
  "DescribeImageSharePermission": {
    "params": [
      {
        "name": "ImageId",
        "desc": "The ID of the image to be shared"
      }
    ],
    "desc": "This API is used to query image sharing information."
  },
  "ImportImage": {
    "params": [
      {
        "name": "Architecture",
        "desc": "OS architecture of the image to be imported, `x86_64` or `i386`."
      },
      {
        "name": "OsType",
        "desc": "OS type of the image to be imported. You can call `DescribeImportImageOs` to obtain the list of supported operating systems."
      },
      {
        "name": "OsVersion",
        "desc": "OS version of the image to be imported. You can call `DescribeImportImageOs` to obtain the list of supported operating systems."
      },
      {
        "name": "ImageUrl",
        "desc": "Address on COS where the image to be imported is stored."
      },
      {
        "name": "ImageName",
        "desc": "Image name"
      },
      {
        "name": "ImageDescription",
        "desc": "Image description"
      },
      {
        "name": "DryRun",
        "desc": "Dry run to check the parameters without performing the operation"
      },
      {
        "name": "Force",
        "desc": "Whether to force import the image. For more information, see [Forcibly Import Image](https://intl.cloud.tencent.com/document/product/213/12849)."
      }
    ],
    "desc": "This API is used to import images. Imported images can be used to create instances. "
  },
  "InquiryPriceRunInstances": {
    "params": [
      {
        "name": "Placement",
        "desc": "Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone and project."
      },
      {
        "name": "ImageId",
        "desc": "[Image](/document/product/213/4940) ID in the format of `img-xxx`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For IDs of `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the information; for IDs of `marketplace images`, go to [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>Call [DescribeImages](https://cloud.tencent.com/document/api/213/15715) and look for `ImageId` in the response.</li>"
      },
      {
        "name": "InstanceChargeType",
        "desc": "The instance [billing method](https://cloud.tencent.com/document/product/213/2180).<br><li>POSTPAID_BY_HOUR: hourly, pay-as-you-go<br>Default value: POSTPAID_BY_HOUR."
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "Configuration of prepaid instances. You can use the parameter to specify the attributes of prepaid instances, such as the subscription period and the auto-renewal plan. This parameter is required for prepaid instances."
      },
      {
        "name": "InstanceType",
        "desc": "The instance model. Different resource specifications are specified for different models. For specific values, call [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749) to retrieve the latest specification list or refer to [Instance Types](https://cloud.tencent.com/document/product/213/11518). If the parameter is not specified, `S1.SMALL1` will be used by default."
      },
      {
        "name": "SystemDisk",
        "desc": "System disk configuration of the instance. If this parameter is not specified, the default value will be used."
      },
      {
        "name": "DataDisks",
        "desc": "The configuration information of the instance data disk. If this parameter is not specified, no data disk will be purchased by default. When purchasing, you can specify 21 data disks, which can contain at most 1 LOCAL_BASIC data disk or LOCAL_SSD data disk, and at most 20 CLOUD_BASIC data disks, CLOUD_PREMIUM data disks, or CLOUD_SSD data disks."
      },
      {
        "name": "VirtualPrivateCloud",
        "desc": "VPC configurations. You can use this parameter to specify the VPC ID, subnet ID, etc. If this parameter is not specified, the basic network will be used by default. If a VPC IP is specified in this parameter, the `InstanceCount` parameter can only be 1. "
      },
      {
        "name": "InternetAccessible",
        "desc": "Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default."
      },
      {
        "name": "InstanceCount",
        "desc": "Number of instances to be purchased. Value range: [1, 100]; default value: 1. The specified number of instances to be purchased cannot exceed the remaining quota allowed for the user. For more information on quota, see [CVM instance purchase limit](https://intl.cloud.tencent.com/document/product/213/2664)."
      },
      {
        "name": "InstanceName",
        "desc": "Instance name to be displayed. <br><li>If this parameter is not specified, \"Unnamed\" will be displayed by default. </li><li>If you purchase multiple instances at the same time and specify a pattern string `{R:x}`, numbers `[x, x+n-1]` will be generated, where `n` represents the number of instances purchased. For example, you specify a pattern string, `server_{R:3}`. If you only purchase 1 instance, the instance will be named `server_3`; if you purchase 2, they will be named `server_3` and `server_4`. You can specify multiple pattern strings in the format of `{R:x}`. </li><li>If you purchase multiple instances at the same time and do not specify a pattern string, the instance names will be suffixed by `1, 2...n`, where `n` represents the number of instances purchased. For example, if you purchase 2 instances and the instance name body is `server_`, the instance names will be `server_1` and `server_2`."
      },
      {
        "name": "LoginSettings",
        "desc": "Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response. If this parameter is not specified, the instance will not be associated with any security group by default."
      },
      {
        "name": "EnhancedService",
        "desc": "Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Monitor and Cloud Security. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default."
      },
      {
        "name": "ClientToken",
        "desc": "A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed. <br>For more information, see “How to ensure idempotency”."
      },
      {
        "name": "HostName",
        "desc": "Host name of the CVM. <br><li>Periods (.) or hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name.<br><li>For Windows instances, the host name must be 2-15 characters long and can contain uppercase and lowercase letters, numbers, and hyphens (-). It cannot contain periods (.) or contain only numbers. <br><li>For other instances, such as Linux instances, the host name must be 2-30 characters long. It supports multiple periods (.) and allows uppercase and lowercase letters, numbers, and hyphens (-) between any two periods (.)."
      },
      {
        "name": "TagSpecification",
        "desc": "The tag description list. This parameter is used to bind a tag to a resource instance. A tag can only be bound to CVM instances."
      },
      {
        "name": "InstanceMarketOptions",
        "desc": "The market options of the instance."
      }
    ],
    "desc": "This API is used to query the price of creating instances. You can only use this API for instances whose configuration is within the purchase limit. For more information, see [RunInstances](https://cloud.tencent.com/document/api/213/15730)."
  },
  "DescribeImages": {
    "params": [
      {
        "name": "ImageIds",
        "desc": "List of image IDs, such as `img-gvbnzy6f`. For the format of array-type parameters, see [API Introduction](https://cloud.tencent.com/document/api/213/15688). You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://cloud.tencent.com/document/api/213/15715) and look for `ImageId` in the response. <br><li>View the image IDs in the [Image Console](https://console.cloud.tencent.com/cvm/image)."
      },
      {
        "name": "Filters",
        "desc": "Filters. Each request can have up to 10 `Filters` and 5 `Filters.Values`. You cannot specify `ImageIds` and `Filters` at the same time. Specific filters:\n<li>`image-id` - String - Optional - Filter results by image ID</li>\n<li>`image-type` - String - Optional - Filter results by image type. Valid values:\n    PRIVATE_IMAGE: private image created by the current account \n    PUBLIC_IMAGE: public image created by Tencent Cloud\n   SHARED_IMAGE: image shared with the current account by another account.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset; default value: 0. For more information on `Offset`, see [API Introduction](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)."
      },
      {
        "name": "Limit",
        "desc": "Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see [API Introduction](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)."
      },
      {
        "name": "InstanceType",
        "desc": "Instance type, e.g. `S1.SMALL1`"
      }
    ],
    "desc": "This API is used to view the list of images.\n\n* You specify the image ID or set filters to query the details of certain images.\n* You can specify `Offset` and `Limit` to select a certain part of the results. By default, the information on the first 20 matching results is returned."
  },
  "ModifyKeyPairAttribute": {
    "params": [
      {
        "name": "KeyId",
        "desc": "Key pair ID in the format of `skey-xxxxxxxx`. <br><br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) and look for `KeyId` in the response."
      },
      {
        "name": "KeyName",
        "desc": "New key pair name, which can contain numbers, letters, and underscores, with a maximum length of 25 characters."
      },
      {
        "name": "Description",
        "desc": "New key pair description. You can specify any name you like, but its length cannot exceed 60 characters."
      }
    ],
    "desc": "This API is used to modify the attributes of key pairs.\n\n* This API modifies the name and description of the key pair identified by the key pair ID.\n* The name of the key pair must be unique.\n* Key pair ID is the unique identifier of a key pair and cannot be modified."
  },
  "ModifyInstancesAttribute": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The maximum number of instances in each request is 100."
      },
      {
        "name": "InstanceName",
        "desc": "Instance name. You can specify any name you like, but its length cannot exceed 60 characters."
      },
      {
        "name": "SecurityGroups",
        "desc": "ID list of security groups of the instance. The instance will be associated with the specified security groups and will be disassociated from the original security groups."
      }
    ],
    "desc": "This API is used to modify the attributes of an instance. Currently you can only use the API to modify the name and the associated security groups of the instance.\n\n* Instance names are used only for users' convenience. Tencent Cloud does not use the name for ticket submission or instance management.\n* Batch operations are supported. The maximum number of instances in each request is 100.\n* When you change the security groups associated with an instance, the original security groups will be disassociated."
  },
  "DescribeRegions": {
    "params": [],
    "desc": "This API is used to query regions."
  },
  "InquiryPriceResetInstancesInternetMaxBandwidth": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The maximum number of instances in each request is 100. When changing the bandwidth of instances with `BANDWIDTH_PREPAID` or `BANDWIDTH_POSTPAID_BY_HOUR` as the network billing method, you can only specify one instance at a time."
      },
      {
        "name": "InternetAccessible",
        "desc": "Configuration of public network egress bandwidth. The maximum bandwidth varies among different models. For more information, see the documentation on bandwidth limits. Currently only the `InternetMaxBandwidthOut` parameter is supported."
      },
      {
        "name": "StartTime",
        "desc": "Date from which the new bandwidth takes effect. Format: `YYYY-MM-DD`, such as `2016-10-30`. The starting date cannot be earlier than the current date. If the starting date is the current date, the new bandwidth takes effect immediately. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned."
      },
      {
        "name": "EndTime",
        "desc": "Date until which the new bandwidth is effective. Format: `YYYY-MM-DD`, such as `2016-10-30`. The validity period of the new bandwidth covers the end date. The end date cannot be later than the expiration date of a prepaid instance. You can query the expiration time of an instance by calling [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728) and looking for `ExpiredTime` in the response. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned."
      }
    ],
    "desc": "This API is used to query the price for upgrading the public bandwidth cap of an instance.\n\n* The allowed bandwidth cap varies for different models. For details, see [Purchasing Network Bandwidth](https://cloud.tencent.com/document/product/213/509).\n* For bandwidth billed by the `TRAFFIC_POSTPAID_BY_HOUR` method, changing the bandwidth cap through this API takes effect in real time. You can increase or reduce bandwidth within applicable limits."
  },
  "DisassociateInstancesKeyPairs": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). The maximum number of instances in each request is 100. <br><br>You can obtain the available instance IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the instance IDs. <br><li>Call [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response."
      },
      {
        "name": "KeyIds",
        "desc": "List of key pair IDs. The maximum number of key pairs in each request is 100. The key pair ID is in the format of `skey-11112222`. <br><br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) and look for `KeyId` in the response."
      },
      {
        "name": "ForceStop",
        "desc": "Whether to force shut down a running instances. It is recommended to manually shut down a running instance before disassociating a key pair from it. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE."
      }
    ],
    "desc": "This API is used to unbind one or more key pairs from one or more instances.\n\n* It only supports [`STOPPED`](https://cloud.tencent.com/document/product/213/15753#InstanceStatus) Linux instances.\n* After a key pair is disassociated from an instance, you can log in to the instance with password.\n* If you did not set a password for the instance, you will not be able to log in via SSH after the unbinding. In this case, you can call [ResetInstancesPassword](https://cloud.tencent.com/document/api/213/15736) to set a login password.\n* Batch operations are supported. The maximum number of instances in each request is 100. If instances not available for the operation are selected, you will get an error code."
  },
  "CreateKeyPair": {
    "params": [
      {
        "name": "KeyName",
        "desc": "Name of the key pair, which can contain numbers, letters, and underscores, with a maximum length of 25 characters."
      },
      {
        "name": "ProjectId",
        "desc": "The ID of the project to which the new key pair belongs.\nYou can query the project IDs in two ways:\n<li>Query the project IDs in the project list.\n<li>Call `DescribeProject` and look for `projectId` in the response."
      }
    ],
    "desc": "This API is used to create an `OpenSSH RSA` key pair, which you can use to log in to a `Linux` instance.\n\n* You only need to specify a name, and the system will automatically create a key pair and return its `ID` and the public and private keys.\n* The name of the key pair must be unique.\n* You can save the private key to a file and use it as an authentication method for `SSH`.\n* Tencent Cloud does not save users' private keys. Be sure to save it yourself."
  },
  "DescribeInstanceFamilyConfigs": {
    "params": [],
    "desc": "This API is used to query the list of model families that are available for the current user and in the current region."
  },
  "DeleteKeyPairs": {
    "params": [
      {
        "name": "KeyIds",
        "desc": "Key ID(s). The maximum number of key pairs in each request is 100. <br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) and look for `KeyId` in the response."
      }
    ],
    "desc": "This API is used to delete the key pairs hosted in Tencent Cloud.\n\n* You can delete multiple key pairs at the same time.\n* A key pair used by an instance or image cannot be deleted. Therefore, you need to verify whether all the key pairs have been deleted successfully."
  },
  "CreateDisasterRecoverGroup": {
    "params": [
      {
        "name": "Name",
        "desc": "Name of the spread placement group. The name must be 1-60 characters long and can contain both Chinese characters and English letters."
      },
      {
        "name": "Type",
        "desc": "Type of the spread placement group. Valid values: <br><li>HOST: physical machine <br><li>SW: switch <br><li>RACK: rack"
      },
      {
        "name": "ClientToken",
        "desc": "A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed. <br>For more information, see “How to ensure idempotency”."
      }
    ],
    "desc": "This API is used to create a [spread placement group](https://cloud.tencent.com/document/product/213/15486). After you create one, you can specify it for an instance when you [create the instance](https://cloud.tencent.com/document/api/213/15730), "
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s) in the format of `ins-xxxxxxxx`. For more information on the format of this parameter, see the `id.N` section of [API Introduction](https://cloud.tencent.com/document/api/213/15688). The maximum number of instances in each request is 100. You cannot specify `InstanceIds` and `Filters` at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filters.\n<li> `zone` - String - Optional - Filter results by availability zone.</li>\n<li> `project-id` - Integer - Optional - Filter results by project ID. You can call [DescribeProject](https://cloud.tencent.com/document/api/378/4400) or log in to the [console](https://console.cloud.tencent.com/cvm/index) to view the list of existing projects. You can also create a new project by calling [AddProject](https://cloud.tencent.com/document/api/378/4398).</li>\n<li> `host-id` - String - Optional - Filter results by [CDH](https://cloud.tencent.com/document/product/416) ID. [CDH](https://cloud.tencent.com/document/product/416) ID format: `host-xxxxxxxx`.</li>\n</li>`vpc-id` - String - Optional - Filter results by VPC ID. VPC ID format: `vpc-xxxxxxxx`.</li>\n<li> `subnet-id` - String - Optional - Filter results by subnet ID. Subnet ID format: `subnet-xxxxxxxx`.</li>\n</li>`instance-id` - String - Optional - Filter results by instance ID. Instance ID format: `ins-xxxxxxxx`.</li>\n</li>`security-group-id` - String - Optional - Filter results by security group ID. Security group ID format: `sg-8jlk3f3r`.</li>\n</li>`instance-name` - String - Optional - Filter results by instance name.</li>\n</li>`instance-charge-type` - String - Optional - Filter results by instance billing method. `POSTPAID_BY_HOUR`: pay-as-you-go | `CDHPAID`: you are only billed for [CDH](https://cloud.tencent.com/document/product/416) instances, not the CVMs running on the [CDH](https://cloud.tencent.com/document/product/416) instances.</li>\n</li>`private-ip-address` - String - Optional - Filter results by the private IP address of the instance’s primary ENI.</li>\n</li>`public-ip-address` - String - Optional - Filter results by the public IP address of the instance’s primary ENI, including the IP addresses automatically assigned during the instance creation and the EIPs manually associated after the instance creation.</li>\n<li> `tag-key` - String - Optional - Filter results by tag key.</li>\n</li>`tag-value` - String - Optional - Filter results by tag value.</li>\n<li> `tag:tag-key` - String - Optional - Filter results by tag key-value pair. Replace `tag-key` with specific tag keys, as shown in example 2.</li>\nEach request can have up to 10 `Filters` and 5 `Filters.Values`. You cannot specify `InstanceIds` and `Filters` at the same time."
      },
      {
        "name": "Offset",
        "desc": "Offset; default value: 0. For more information on `Offset`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377)."
      },
      {
        "name": "Limit",
        "desc": "Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). "
      }
    ],
    "desc": "This API is used to query the details of instances.\n\n* You can filter the query results with the instance `ID`, name, or billing method. See `Filter` for more information.\n* If no parameter is defined, a certain number of instances under the current account will be returned. The number is specified by `Limit` and is 20 by default."
  },
  "ImportKeyPair": {
    "params": [
      {
        "name": "KeyName",
        "desc": "Key pair name, which can contain numbers, letters, and underscores, with a maximum length of 25 characters."
      },
      {
        "name": "ProjectId",
        "desc": "The ID of the [project](https://cloud.tencent.com/document/product/378/10861) to which the created key pair belongs.<br><br>You can retrieve the project ID in two ways:<br><li>Query the project ID in [Project Management](https://console.cloud.tencent.com/project).<br><li>Call [DescribeProject](https://cloud.tencent.com/document/api/378/4400) and search for `projectId` in the response.\n\nIf you want to use the default project, specify 0 for the parameter."
      },
      {
        "name": "PublicKey",
        "desc": "Content of the public key in the key pair in the `OpenSSH RSA` format."
      }
    ],
    "desc": "This API is used to import key pairs.\n\n* You can use this API to import key pairs to a user account, but the key pairs will not be automatically associated with any instance. You may use [AssociasteInstancesKeyPair](https://cloud.tencent.com/document/api/213/9404) to associate key pairs with instances.\n* You need to specify the names of the key pairs and the content of the public keys.\n* If you only have private keys, you can convert them to public keys with the `SSL` tool before importing them."
  },
  "AssociateInstancesKeyPairs": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). The maximum number of instances in each request is 100. <br>You can obtain the available instance IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the instance IDs. <br><li>Call [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response."
      },
      {
        "name": "KeyIds",
        "desc": "Key ID(s). The maximum number of key pairs in each request is 100. The key pair ID is in the format of `skey-3glfot13`. <br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) and look for `KeyId` in the response."
      },
      {
        "name": "ForceStop",
        "desc": "Whether to force shut down a running instances. It is recommended to manually shut down a running instance before associating a key pair with it. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE."
      }
    ],
    "desc": "This API is used to associate key pairs with instances.\n\n* If the public key of a key pair is written to the `SSH` configuration of the instance, users will be able to log in to the instance with the private key of the key pair.\n* If the instance is already associated with a key, the old key will become invalid.\nIf you currently use a password to log in, you will no longer be able to do so after you associate the instance with a key.\n* Batch operations are supported. The maximum number of instances in each request is 100. If any instance in the request cannot be associated with a key, you will get an error code."
  },
  "RunInstances": {
    "params": [
      {
        "name": "Placement",
        "desc": "Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone, project, and CDH. You can specify a CDH for a CVM by creating the CVM on the CDH."
      },
      {
        "name": "ImageId",
        "desc": "The [image](/document/product/213/4940) ID in the format of `img-xxx`. There are four types of images:<br/><li>Public images</li><li>Custom images</li><li>Shared images</li><li>Marketplace images</li><br/>You can retrieve available image IDs in the following ways:<br/><li>For the IDs of `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the information. For the IDs of `marketplace images`, go to [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>Call [DescribeImages](https://cloud.tencent.com/document/api/213/15715), pass in `InstanceType` to retrieve the list of images supported by the current model, and then find the `ImageId` in the response.</li>"
      },
      {
        "name": "InstanceChargeType",
        "desc": "The instance [billing method](https://cloud.tencent.com/document/product/213/2180). Valid values: <br><li>`POSTPAID_BY_HOUR`: hourly, pay-as-you-go<br><li>`CDHPAID`: you are only billed for CDH instances, not the CVMs running on the CDH instances.<br>Default value: POSTPAID_BY_HOUR."
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "Configuration of prepaid instances. You can use the parameter to specify the attributes of prepaid instances, such as the subscription period and the auto-renewal plan. This parameter is required for prepaid instances."
      },
      {
        "name": "InstanceType",
        "desc": "The instance model. Different resource specifications are specified for different instance models.\n<br><li>To view specific values for `POSTPAID_BY_HOUR` instances, you can call [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749) or refer to [Instance Types](https://cloud.tencent.com/document/product/213/11518). If this parameter is not specified, `S1.SMALL1` will be used by default.<br><li>For `CDHPAID` instances, the value of this parameter is in the format of `CDH_XCXG` based on the number of CPU cores and memory capacity. For example, if you want to create a CDH instance with a single-core CPU and 1 GB memory, specify this parameter as `CDH_1C1G`."
      },
      {
        "name": "SystemDisk",
        "desc": "System disk configuration of the instance. If this parameter is not specified, the default value will be used."
      },
      {
        "name": "DataDisks",
        "desc": "The configuration information of instance data disks. If this parameter is not specified, no data disk will be purchased by default. When purchasing, you can specify 21 data disks, which can contain at most 1 LOCAL_BASIC data disk or LOCAL_SSD data disk, and at most 20 CLOUD_BASIC data disks, CLOUD_PREMIUM data disks, or CLOUD_SSD data disks."
      },
      {
        "name": "VirtualPrivateCloud",
        "desc": "VPC configurations. You can use this parameter to specify the VPC ID, subnet ID, etc. If this parameter is not specified, the basic network will be used by default. If a VPC IP is specified in this parameter, it will represent the primary ENI IP of each instance. The value of `InstanceCount` must be the same as the number of VPC IPs."
      },
      {
        "name": "InternetAccessible",
        "desc": "Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default."
      },
      {
        "name": "InstanceCount",
        "desc": "The number of instances to be purchased. Value range: [1, 100]; default value: 1. The specified number of instances to be purchased cannot exceed the remaining quota allowed for the user. For more information on the quota, see [CVM instance purchase limit](https://intl.cloud.tencent.com/document/product/213/2664)."
      },
      {
        "name": "InstanceName",
        "desc": "Instance name to be displayed. <br><li>If this parameter is not specified, \"Unnamed\" will be displayed by default. </li><li>If you purchase multiple instances at the same time and specify a pattern string `{R:x}`, numbers `[x, x+n-1]` will be generated, where `n` represents the number of instances purchased. For example, you specify a pattern string, `server_{R:3}`. If you only purchase 1 instance, the instance will be named `server_3`; if you purchase 2, they will be named `server_3` and `server_4`. You can specify multiple pattern strings in the format of `{R:x}`. </li><li>If you purchase multiple instances at the same time and do not specify a pattern string, the instance names will be suffixed by `1, 2...n`, where `n` represents the number of instances purchased. For example, if you purchase 2 instances and the instance name body is `server_`, the instance names will be `server_1` and `server_2`."
      },
      {
        "name": "LoginSettings",
        "desc": "Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response. If this parameter is not specified, the instance will be associated with default security groups."
      },
      {
        "name": "EnhancedService",
        "desc": "Specifies whether to enable services Anti-DDoS and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Anti-DDoS are enabled for public images by default. But for custom images and images from market place, Anti-DDoS and Cloud Monitor are not enabled by default. The original services in the image will be retained."
      },
      {
        "name": "ClientToken",
        "desc": "A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed. <br>For more information, see “How to ensure idempotency”."
      },
      {
        "name": "HostName",
        "desc": "Host name of the CVM. <br><li>Periods (.) or hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name.<br><li>For Windows instances, the host name must be 2-15 characters long and can contain uppercase and lowercase letters, numbers, and hyphens (-). It cannot contain periods (.) or contain only numbers. <br><li>For other instances, such as Linux instances, the host name must be 2-60 characters long. It supports multiple periods (.) and allows uppercase and lowercase letters, numbers, and hyphens (-) between any two periods (.)."
      },
      {
        "name": "ActionTimer",
        "desc": "Scheduled tasks. You can use this parameter to specify scheduled tasks for the instance. Only scheduled termination is supported."
      },
      {
        "name": "DisasterRecoverGroupIds",
        "desc": "Placement group ID. You can only specify one."
      },
      {
        "name": "TagSpecification",
        "desc": "The tag description list. This parameter is used to bind a tag to a resource instance. A tag can only be bound to CVM instances."
      },
      {
        "name": "InstanceMarketOptions",
        "desc": "The market options of the instance."
      },
      {
        "name": "UserData",
        "desc": "User data provided to the instance, which needs to be encoded in base64 format with the maximum size of 16KB. For more information on how to get the value of this parameter, see the commands you need to execute on startup for [Windows](https://intl.cloud.tencent.com/document/product/213/17526) or [Linux](https://intl.cloud.tencent.com/document/product/213/17525)."
      },
      {
        "name": "DryRun",
        "desc": "Whether the request is a dry run only.\ntrue: dry run only. The request will not create instance(s). A dry run can check whether all the required parameters are specified, whether the request format is right, whether the request exceeds service limits, and whether the specified CVMs are available.\nIf the dry run fails, the corresponding error code will be returned.\nIf the dry run succeeds, the RequestId will be returned.\nfalse (default value): send a normal request and create instance(s) if all the requirements are met."
      }
    ],
    "desc": "This API is used to create one or more instances with a specified configuration.\n\n* After an instance is created successfully, it will start up automatically, and the [instance state](/document/api/213/9452#instance_state) will become \"Running\".\n* If you create a pay-as-you-go instance billed on an hourly basis, an amount equivalent to the hourly rate will be frozen before the creation. Make sure your account balance is sufficient before calling this API.\n* The number of instances you can purchase through this API is subject to the [CVM instance purchase limit](https://cloud.tencent.com/document/product/213/2664). Both the instances created through this API and the console will be counted toward the quota.\n* This API is an async API. An instance `ID` list will be returned after you successfully make a creation request. However, it does not mean the creation has been completed. The state of the instance will be `Creating` during the creation. You can use [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) to query the status of the instance. If the status changes from `Creating` to `Running`, it means that the instance has been created successfully."
  },
  "DeleteImages": {
    "params": [
      {
        "name": "ImageIds",
        "desc": "List of the IDs of the instances to be deleted."
      }
    ],
    "desc": "This API is used to delete images.\n\n* If the [ImageState](https://cloud.tencent.com/document/api/213/9452#image_state) of an image is `Creating` or `In Use`, it cannot be deleted. Use [DescribeImages](https://cloud.tencent.com/document/api/213/9418) to query the image state.\n* You can only create up to 10 custom images in each region. If you have used up the quota, you can delete images to create new ones.\n* A shared image cannot be deleted."
  },
  "InquiryPriceResizeInstanceDisks": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response."
      },
      {
        "name": "DataDisks",
        "desc": "The configuration of data disks to be expanded. Currently, you can only use the API to expand non-elastic data disks whose [disk type](https://cloud.tencent.com/document/product/213/15753#DataDisk) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is non-elastic. Data disk capacity unit: GB; minimum increment: 10 GB. For more information about selecting a data disk type, see the product overview on cloud disks. Available data disk types are subject to the instance type (`InstanceType`). In addition, the maximum capacity allowed for expansion varies by data disk type."
      },
      {
        "name": "ForceStop",
        "desc": "Whether to force shut down a running instances. It is recommended to manually shut down a running instance before resetting the user password. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE. <br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be shut down normally."
      }
    ],
    "desc": "This API is used to query the price for expanding data disks of an instance.\n\n* Currently, you can only use this API to query the price of non-elastic data disks whose [disk type](/document/api/213/9452#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is non-elastic.\n* Currently, you cannot use this API to query the price for [CDH](https://cloud.tencent.com/document/product/416) instances. *Also, you can only query the price of expanding one data disk at a time."
  },
  "ModifyInstancesVpcAttribute": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response."
      },
      {
        "name": "VirtualPrivateCloud",
        "desc": "VPC configurations. You can use this parameter to specify the VPC ID, subnet ID, VPC IP, etc. If the specified VPC ID and subnet ID (the subnet must be in the same availability zone as the instance) are different from the VPC where the specified instance resides, the instance will be migrated to a subnet of the specified VPC. You can use `PrivateIpAddresses` to specify the VPC subnet IP. If you want to specify the subnet IP, you will need to specify a subnet IP for each of the specified instances, and each `InstanceIds` will match a `PrivateIpAddresses`. If `PrivateIpAddresses` is not specified, the VPC subnet IP will be assigned randomly."
      },
      {
        "name": "ForceStop",
        "desc": "Whether to force shut down a running instances. Default value: TRUE."
      },
      {
        "name": "ReserveHostName",
        "desc": "Whether to keep the host name. Default value: FALSE."
      }
    ],
    "desc": "This API is used to modify the VPC attributes of an instance, such as the VPC IP address.\n* By default, the instances will shut down when you perform this operation and restart upon completion.\n* If the specified VPC ID and subnet ID (the subnet must be in the same availability zone as the instance) are different from the VPC where the specified instance resides, the instance will be migrated to a subnet of the specified VPC. Before performing this operation, make sure that the specified instance is not bound with an [ENI](https://cloud.tencent.com/document/product/576) or [CLB](https://cloud.tencent.com/document/product/214)."
  },
  "InquiryPriceResetInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response."
      },
      {
        "name": "ImageId",
        "desc": "[Image](/document/product/213/4940) ID in the format of `img-xxx`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For IDs of `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the information; for IDs of `marketplace images`, go to [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>Call [DescribeImages](https://cloud.tencent.com/document/api/213/15715) and look for `ImageId` in the response.</li>"
      },
      {
        "name": "SystemDisk",
        "desc": "Configuration of the system disk of the instance. For instances with a cloud disk as the system disk, you can expand the system disk by using this parameter to specify the new capacity after reinstallation. If the parameter is not specified, the system disk capacity remains unchanged by default. You can only expand the capacity of the system disk; reducing its capacity is not supported. When reinstalling the system, you can only modify the capacity of the system disk, not the type."
      },
      {
        "name": "LoginSettings",
        "desc": "Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center."
      },
      {
        "name": "EnhancedService",
        "desc": "Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Monitor and Cloud Security. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default."
      }
    ],
    "desc": "This API is used to query the price for reinstalling an instance.\n\n* If you have specified the `ImageId` parameter, the price query is performed with the specified image. Otherwise, the image used by the current instance is used.\n* You can only query the price for reinstallation caused by switching between Linux and Windows OS. And the [system disk type](https://cloud.tencent.com/document/api/213/15753#SystemDisk) of the instance must be `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`.\n* Currently, this API only supports instances in Mainland China regions."
  },
  "DescribeDisasterRecoverGroupQuota": {
    "params": [],
    "desc": "This API is used to query the quota of [spread placement groups](https://cloud.tencent.com/document/product/213/15486)."
  },
  "ResetInstancesPassword": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The maximum number of instances in each request is 100."
      },
      {
        "name": "Password",
        "desc": "Login password of the instance(s). The password requirements vary among different operating systems:\nFor a Linux instance, the password must be 8 to 30 characters in length; password with more than 12 characters is recommended. It cannot begin with \"/\", and must contain at least one character from three of the following categories: <br><li>Lowercase letters: [a-z]<br><li>Uppercase letters: [A-Z]<br><li>Numbers: 0-9<br><li>Special characters: ()\\`~!@#$%^&\\*-+=\\_|{}[]:;'<>,.?/:\nFor a Windows CVM, the password must be 12 to 30 characters in length. It cannot begin with \"/\" or contain your username. It must contain at least one character from three of the following categories: <br><li>Lowercase letters: [a-z]<br><li>Uppercase letters: [A-Z]<br><li>Numbers: 0-9<br><li>Special characters: ()\\`~!@#$%^&\\*-+=\\_|{}[]:;' <>,.?/:<br><li>If the specified instances include both `Linux` and `Windows` instances, you will need to follow the password requirements for `Windows` instances."
      },
      {
        "name": "UserName",
        "desc": "Operating system username of the instance for which you want to reset the password. The length of the username cannot exceed 64 characters."
      },
      {
        "name": "ForceStop",
        "desc": "Whether to force shut down a running instances. It is recommended to manually shut down a running instance before resetting the user password. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE. <br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be shut down normally."
      }
    ],
    "desc": "This API is used to reset the password of the instance OS to a user-specified password.\n\n* You can only use this API to modify the password of the administrator account. The name of the administrator account varies depending on the operating system. On Windows, it is `Administrator`; `Ubuntu`, `ubuntu`; `Linux`, `root`.)\n* To reset the password of a running instance, you need to explicitly specify the force shutdown parameter `ForceStop`. Otherwise, you can only reset passwords of instances that have been shut down.\n* Batch operations are supported. You can reset the passwords of multiple instances to the same one. The maximum number of instances in each request is 100."
  },
  "ResetInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response."
      },
      {
        "name": "ImageId",
        "desc": "[Image](/document/product/213/4940) ID in the format of `img-xxx`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For IDs of `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the information; for IDs of `marketplace images`, go to [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>Call [DescribeImages](https://cloud.tencent.com/document/api/213/15715) and look for `ImageId` in the response.</li>\n<br>The current image will be used by default."
      },
      {
        "name": "SystemDisk",
        "desc": "Configuration of the system disk of the instance. For instances with a cloud disk as the system disk, you can expand the system disk by using this parameter to specify the new capacity after reinstallation. If the parameter is not specified, the system disk capacity remains unchanged by default. You can only expand the capacity of the system disk; reducing its capacity is not supported. When reinstalling the system, you can only modify the capacity of the system disk, not the type."
      },
      {
        "name": "LoginSettings",
        "desc": "Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center."
      },
      {
        "name": "EnhancedService",
        "desc": "Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Monitor and Cloud Security. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default."
      },
      {
        "name": "HostName",
        "desc": "You can use this parameter to specify a new HostName for the instance when reinstalling the system."
      }
    ],
    "desc": "This API is used to reinstall the operating system of the specified instance.\n\n* If you specify an `ImageId`, the specified image is used. Otherwise, the image used by the current instance is used.\n* The system disk will be formatted and reset. Therefore, make sure that no important files are stored on the system disk.\n* If the operating system switches between `Linux` and `Windows`, the system disk `ID` of the instance will change, and the snapshots that are associated with the system disk can no longer be used to roll back and restore data.\n* If no password is specified, you will get a random password via internal message.\n* You can only use this API to switch the operating system between `Linux` and `Windows` for instances whose [system disk type](https://cloud.tencent.com/document/api/213/9452#SystemDisk) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`.\n* Currently, this API only supports instances in Mainland China regions."
  },
  "ResizeInstanceDisks": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response."
      },
      {
        "name": "DataDisks",
        "desc": "Configuration of data disks to be expanded. Currently you can only use the API to expand non-elastic data disks whose [disk type](/document/api/213/9452#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is not elastic. Data disk capacity unit: GB; minimum increment: 10 GB. For more information on selecting the data disk type, see the product overview on cloud disks. Available data disk types are subject to the instance type (`InstanceType`). In addition, the maximum capacity allowed for expansion varies by data disk type."
      },
      {
        "name": "ForceStop",
        "desc": "Whether to force shut down a running instances. It is recommended to manually shut down a running instance before resetting the user password. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE. <br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be shut down normally."
      }
    ],
    "desc": "This API (ResizeInstanceDisks) is used to expand the data disks of an instance.\n\n* Currently, you can only use the API to expand non-elastic data disks whose [disk type](/document/api/213/9452#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is non-elastic.\n* Currently, this API does not support [CDH](https://cloud.tencent.com/document/product/416) instances.\n* Currently, only one data disk can be expanded at a time."
  },
  "DescribeZones": {
    "params": [],
    "desc": "This API is used to query availability zones."
  },
  "DescribeImageQuota": {
    "params": [],
    "desc": "This API is used to query the image quota of an user account."
  },
  "AssociateSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "ID of the security group to be associated, such as `sg-efil73jd`. Only one security group can be associated."
      },
      {
        "name": "InstanceIds",
        "desc": "ID(s) of the instance(s) to be associated, such as `ins-lesecurk`. You can specify multiple instances."
      }
    ],
    "desc": "This API is used to associate security groups with specified instances."
  },
  "ResetInstancesType": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The maximum number of instances in each request is 1."
      },
      {
        "name": "InstanceType",
        "desc": "Instance model. Different resource specifications are specified for different models. For specific values, call [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749) to get the latest specification list or refer to [Instance Types](https://cloud.tencent.com/document/product/213/11518)."
      },
      {
        "name": "ForceStop",
        "desc": "Whether to force shut down a running instances. It is recommended to manually shut down a running instance before resetting the user password. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE. <br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be shut down normally."
      }
    ],
    "desc": "This API is used to change the model of an instance.\n* You can only use this API to change the models of instances whose [system disk type](/document/api/213/9452#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`.\n* Currently, you cannot use this API to change the models of [CDH](https://cloud.tencent.com/document/product/416) instances."
  },
  "ModifyImageAttribute": {
    "params": [
      {
        "name": "ImageId",
        "desc": "Image ID such as `img-gvbnzy6f`. You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://cloud.tencent.com/document/api/213/15715) and look for `ImageId` in the response. <br><li>Look for the information in the [Image Console](https://console.cloud.tencent.com/cvm/image)."
      },
      {
        "name": "ImageName",
        "desc": "New image name, which must meet the following requirements: <br> <li>No more than 20 characters. <br> <li>Must be unique."
      },
      {
        "name": "ImageDescription",
        "desc": "New image description, which must meet the following requirement: <br> <li> No more than 60 characters."
      }
    ],
    "desc": "This API is used to modify image attributes.\n\n* Attributes of shared images cannot be modified."
  },
  "DescribeInstancesOperationLimit": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The instance ID format is `ins-xxxxxxxx`. For more information on the format of this parameter, see the `id.N` section of [API Introduction](https://cloud.tencent.com/document/api/213/15688)). The maximum number of instance IDs in each request is 100."
      },
      {
        "name": "Operation",
        "desc": "Operation on the instance(s).\n<li> INSTANCE_DEGRADE: downgrade the instance configurations</li>"
      }
    ],
    "desc": "This API is used to query limitations on operations on an instance.\n\n* Currently you can use this API to query the maximum number of times you can modify the configuration of an instance."
  },
  "InquiryPriceResetInstancesType": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The maximum number of instances in each request is 1."
      },
      {
        "name": "InstanceType",
        "desc": "Instance model. Different resource specifications are specified for different models. For specific values, see the instance resource specification table. You can also obtain the latest specification list by calling the API for querying the list of instance resource specifications."
      }
    ],
    "desc": "This API is used to query the price for adjusting the instance model.\n\n* Currently, you can only use this API to query the prices of instances whose [system disk type](https://cloud.tencent.com/document/api/213/9452#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`.\n* Currently, you cannot use this API to query the prices of [CDH](https://cloud.tencent.com/document/product/416) instances."
  },
  "StopInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The maximum number of instances in each request is 100."
      },
      {
        "name": "ForceStop",
        "desc": "Whether to force shut down an instance after a normal shutdown fails. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails <br><li>FALSE: do not force shut down an instance after a normal shutdown fails <br><br>Default value: FALSE."
      },
      {
        "name": "StopType",
        "desc": "Instance shutdown mode. Valid values: <br><li>SOFT_FIRST: perform a soft shutdown first, and force shut down the instance if the soft shutdown fails <br><li>HARD: force shut down the instance directly <br><li>SOFT: soft shutdown only <br>Default value: SOFT."
      },
      {
        "name": "StoppedMode",
        "desc": "Billing method of a pay-as-you-go instance after shutdown.\nValid values: <br><li>KEEP_CHARGING: billing continues after shutdown <br><li>STOP_CHARGING: billing stops after shutdown <br>Default value: KEEP_CHARGING.\nThis parameter is only valid for some pay-as-you-go instances using cloud disks. For more information, see [No charges when shut down for pay-as-you-go instances](https://intl.cloud.tencent.com/document/product/213/19918)."
      }
    ],
    "desc": "This API is used to shut down instances.\n\n* You can only perform this operation on instances whose status is `RUNNING`.\n* The instance status will become `STOPPING` when the API is called successfully and `STOPPED` when the instance is successfully shut down.\n* Forced shutdown is supported. A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be sht down normally.\n* Batch operations are supported. The maximum number of instances in each request is 100."
  },
  "ModifyHostsAttribute": {
    "params": [
      {
        "name": "HostIds",
        "desc": "CDH instance ID(s)."
      },
      {
        "name": "HostName",
        "desc": "CDH instance name to be displayed. You can specify any name you like, but its length cannot exceed 60 characters."
      },
      {
        "name": "RenewFlag",
        "desc": "Auto renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify upon expiration nor renew automatically <br><br>If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis if the account balance is sufficient."
      }
    ],
    "desc": "This API is used to modify the attributes of a CDH instance, such as instance name and renewal flag. One of the two parameters, HostName and RenewFlag, must be set, but you cannot set both of them at the same time."
  },
  "DescribeImportImageOs": {
    "params": [],
    "desc": "This API is used to query the list of supported operating systems of imported images."
  },
  "DescribeInstanceVncUrl": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response."
      }
    ],
    "desc": "This API is used to query the VNC URL of an instance.\n\n* It does not support `STOPPED` CVMs.\n* A VNC URL is only valid for 15 sec. If you do not access the URL within 15 seconds, it will become invalid and you will have to query another one.\n* Once you access a VNC URL, it will become invalid and you will have to query another one.\n* If the connection breaks up, you can make up to 30 requests per minute to reestablish the connection.\n* After you get the value of `InstanceVncUrl`, you need to append `InstanceVncUrl=xxxx` to the end of the link <https://img.qcloud.com/qcloud/app/active_vnc/index.html?>.\n  - Parameter `InstanceVncUrl`: the value of `InstanceVncUrl` returned after a successful API call.\n\n    The final URLs are in the following format:\n\n```\nhttps://img.qcloud.com/qcloud/app/active_vnc/index.html?InstanceVncUrl=wss%3A%2F%2Fbjvnc.qcloud.com%3A26789%2Fvnc%3Fs%3DaHpjWnRVMFNhYmxKdDM5MjRHNlVTSVQwajNUSW0wb2tBbmFtREFCTmFrcy8vUUNPMG0wSHZNOUUxRm5PMmUzWmFDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9\n```\n"
  },
  "SyncImages": {
    "params": [
      {
        "name": "ImageIds",
        "desc": "List of image IDs. You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://cloud.tencent.com/document/api/213/15715) and look for `ImageId` in the response. <br><li>Look for the information in the [Image Console](https://console.cloud.tencent.com/cvm/image). <br>The specified images must meet the following requirements: <br><li>The images must be in the `NORMAL` state. <br><li>The image size must be smaller than 50 GB. <br>For more information on image states, see [here](/document/api/213/9452#image_state)."
      },
      {
        "name": "DestinationRegions",
        "desc": "List of destination regions for synchronization. A destination region must meet the following requirements: <br><li>It cannot be the source region. <br><li>It must be valid. <br><li>Currently some regions do not support image synchronization. <br>For specific regions, see [Region](https://cloud.tencent.com/document/product/213/6091)."
      }
    ],
    "desc": "This API is used to sync a custom image to other regions.\n\n* Each API call syncs a single image.\n* This API supports syncing an image to multiple regions.\n* Each account can have up to 10 custom images in each region. "
  },
  "DeleteDisasterRecoverGroups": {
    "params": [
      {
        "name": "DisasterRecoverGroupIds",
        "desc": "List of spread placement group IDs, which can be obtained by calling the [DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/api/213/17810) API."
      }
    ],
    "desc": "This API is used to delete a [spread placement group](https://cloud.tencent.com/document/product/213/15486). Only empty placement groups can be deleted. To delete a non-empty group, you need to terminate all the CVM instances in it first. Otherwise, the deletion will fail."
  },
  "TerminateInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The maximum number of instances in each request is 100."
      }
    ],
    "desc": "This API is used to return instances.\n\n* Use this API to return instances that are no longer required.\n* Pay-as-you-go instances can be returned directly through this API.\n* When this API is called for the first time, the instance will be moved to the recycle bin. When this API is called for the second time, the instance will be terminated and cannot be recovered.\n* Batch operations are supported. The allowed maximum number of instances in each request is 100."
  },
  "DescribeZoneInstanceConfigInfos": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filters.\n\n<li> `zone` - String - Optional - Filter results by availability zone.</li>\n\n<li>`instance-family` - String - Optional - Filter results by instance model family, such as `S1`, `I1`, and `M1`.</li>\n\n<li>`instance-type` - String - Optional - Filter results by model. Different instance models have different configurations. You can call `DescribeInstanceTypeConfigs` to query the latest configuration list or refer to the documentation on instance types. If this parameter is not specified, `S1.SMALL1` will be used by default.</li>\n\n<li>`instance-charge-type` - String - Optional - Filter results by instance billing method. `POSTPAID_BY_HOUR`: pay-as-you-go | `CDHPAID`: you are only billed for CDH instances, not the CVMs running on the CDH instances.</li>"
      }
    ],
    "desc": "This API is used to query the configurations of models in an availability zone."
  },
  "ResetInstancesInternetMaxBandwidth": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The maximum number of instances in each request is 100. When changing the bandwidth of instances with `BANDWIDTH_PREPAID` or `BANDWIDTH_POSTPAID_BY_HOUR` as the network billing method, you can only specify one instance at a time."
      },
      {
        "name": "InternetAccessible",
        "desc": "Configuration of public network egress bandwidth. The maximum bandwidth varies among different models. For more information, see the documentation on bandwidth limits. Currently only the `InternetMaxBandwidthOut` parameter is supported."
      },
      {
        "name": "StartTime",
        "desc": "Date from which the new bandwidth takes effect. Format: `YYYY-MM-DD`, such as `2016-10-30`. The starting date cannot be earlier than the current date. If the starting date is the current date, the new bandwidth takes effect immediately. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned."
      },
      {
        "name": "EndTime",
        "desc": "Date until which the new bandwidth is effective. Format: `YYYY-MM-DD`, such as `2016-10-30`. The validity period of the new bandwidth covers the end date. The end date cannot be later than the expiration date of a prepaid instance. You can query the expiration time of an instance by calling [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728) and looking for `ExpiredTime` in the response. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned."
      }
    ],
    "desc": "This API is used to change the public bandwidth cap of an instance.\n\n* The allowed bandwidth cap varies for different models. For details, see [Purchasing Network Bandwidth](https://cloud.tencent.com/document/product/213/509).\n* For bandwidth billed by the `TRAFFIC_POSTPAID_BY_HOUR` method, changing the bandwidth cap through this API takes effect in real time. Users can increase or reduce bandwidth within applicable limits."
  },
  "StartInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The maximum number of instances in each request is 100."
      }
    ],
    "desc": "This API is used to start instances.\n\n* You can only perform this operation on instances whose status is `STOPPED`.\n* The instance status will become `STARTING` when the API is called successfully and `RUNNING` when the instance is successfully started.\n* Batch operations are supported. The maximum number of instances in each request is 100."
  },
  "DescribeDisasterRecoverGroups": {
    "params": [
      {
        "name": "DisasterRecoverGroupIds",
        "desc": "List of spread placement group IDs."
      },
      {
        "name": "Name",
        "desc": "Name of a spread placement group. Fuzzy match is supported."
      },
      {
        "name": "Offset",
        "desc": "Offset; default value: 0. For more information on `Offset`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377)."
      },
      {
        "name": "Limit",
        "desc": "Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). "
      }
    ],
    "desc": "This API is used to query the information on [spread placement groups](https://cloud.tencent.com/document/product/213/15486)."
  },
  "DescribeKeyPairs": {
    "params": [
      {
        "name": "KeyIds",
        "desc": "Key pair ID(s) in the format of `skey-11112222`. This API supports using multiple IDs as filters at the same time. For more information on the format of this parameter, see the `id.N` section in [API Introduction](https://cloud.tencent.com/document/api/213/15688). You cannot specify `KeyIds` and `Filters` at the same time. You can log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the key pair IDs."
      },
      {
        "name": "Filters",
        "desc": "Filters.\n<li> `project-id` - Integer - Optional - Filter results by project ID. To view the list of project IDs, you can go to [Project Management](https://console.cloud.tencent.com/project), or call [DescribeProject](https://cloud.tencent.com/document/api/378/4400) and look for `projectId` in the response. </li>\n<li> `key-name` - String - Optional - Filter results by key pair name. </li> You cannot specify `KeyIds` and `Filters` at the same time."
      },
      {
        "name": "Offset",
        "desc": "Offset; default value: 0. For more information on `Offset`, see the corresponding sections in API [Introduction](https://intl.cloud.tencent.com/document/product/377). Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). "
      },
      {
        "name": "Limit",
        "desc": "Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). "
      }
    ],
    "desc": "This API is used to query key pairs.\n\n* A key pair is a pair of keys generated by an algorithm in which the public key is available to the public and the private key is available only to the user. You can use this API to query the public key but not the private key."
  },
  "DescribeHosts": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filters.\n<li> `zone` - String - Optional - Filter results by availability zone.</li>\n<li> `project-id` - Integer - Optional - Filter results by project ID. You can call `DescribeProject` or log in to the console to view the list of existing projects. You can also create a new project by calling `AddProject`.</li>\n<li> `host-id` - String - Optional - Filter results by CDH ID. CDH IDs are in the format of `host-11112222`.</li>\n<li> `host-name` - String - Optional - Filter results by CDH instance name.</li>\n<li> `host-state` - String - Optional - Filter results by CDH instance state. (PENDING: creating | LAUNCH_FAILURE: creation failed | RUNNING: running | EXPIRED: expired)</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset; default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of results returned; default value: 20; maximum: 100."
      }
    ],
    "desc": "This API is used to query the details of CDH instances."
  },
  "ModifyDisasterRecoverGroupAttribute": {
    "params": [
      {
        "name": "DisasterRecoverGroupId",
        "desc": "Spread placement group ID, which can be obtained by calling the [DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/api/213/17810) API."
      },
      {
        "name": "Name",
        "desc": "Name of a spread placement group. The name must be 1-60 characters long and can contain both Chinese characters and English letters."
      }
    ],
    "desc": "This API is used to modify the attributes of [spread placement groups](https://cloud.tencent.com/document/product/213/15486)."
  },
  "DescribeInternetChargeTypeConfigs": {
    "params": [],
    "desc": "This API is used to query the network billing methods."
  },
  "RebootInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The maximum number of instances in each request is 100."
      },
      {
        "name": "ForceReboot",
        "desc": "Whether to force restart an instance after a normal restart fails. Valid values: <br><li>TRUE: force restart an instance after a normal restart fails <br><li>FALSE: do not force restart an instance after a normal restart fails <br><br>Default value: FALSE."
      },
      {
        "name": "StopType",
        "desc": "Shutdown type. Valid values: <br><li>SOFT: soft shutdown<br><li>HARD: hard shutdown<br><li>SOFT_FIRST: perform a soft shutdown first, and perform a hard shutdown if the soft shutdown fails<br><br>Default value: SOFT."
      }
    ],
    "desc": "This API is used to restart instances.\n\n* You can only perform this operation on instances whose status is `RUNNING`.\n* If the API is called successfully, the instance status will become `REBOOTING`. After the instance is restarted, its status will become `RUNNING` again.\n* Forced restart is supported. A forced restart is similar to switching off the power of a physical computer and starting it again. It may cause data loss or file system corruption. Be sure to only force start a CVM when it cannot be restarted normally.\n* Batch operations are supported. The maximum number of instances in each request is 100."
  },
  "DescribeInstanceTypeConfigs": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filters.\n<li> `zone` - String - Optional - Filter results by [availability zone](https://cloud.tencent.com/document/product/213/15753#ZoneInfo).</li>\n<li> `instance-family` - String - Optional - Filter results by instance model family, such as `S1`, `I1`, and `M1`.</li>\nEach request can have up to 10 `Filters` and 1 `Filters.Values`."
      }
    ],
    "desc": "This API is used to query the model configuration of an instance.\n\n* You can filter the query results with `zone` or `instance-family`. For more information on filtering conditions, see `Filter`.\n* If no parameter is defined, the model configuration of all the instances in the specified region will be returned."
  },
  "ModifyInstancesProject": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) and look for `InstanceId` in the response. The maximum number of instances in each request is 100."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID. You can create a project by calling [AddProject](https://cloud.tencent.com/doc/api/403/4398). When calling [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) to query instances, the project IDs can be used to filter the results."
      }
    ],
    "desc": "This API is used to change the project to which an instance belongs.\n\n* Project is a virtual concept. Users can create multiple projects under one account, manage different resources in each project, and assign different instances to different projects. You may use [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) to query instances and use the project ID to filter results.\n* You cannot modify the project of an instance which is bound to a load balancer. You need to unbind the load balancer from the instance with [`DeregisterInstancesFromLoadBalancer`](https://cloud.tencent.com/document/api/214/1258) before using this API.\n* If you modify the project of an instance, security groups associated with the instance will be automatically disassociated. You can use [`ModifySecurityGroupsOfInstance`](https://cloud.tencent.com/document/api/213/1367) to associate the instance with certian security groups again.\n* Batch operations are supported. The maximum number of instances in each request is 100."
  },
  "DisassociateSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "ID of the security group to be disassociated, such as `sg-efil73jd`. Only one security group can be disassociated."
      },
      {
        "name": "InstanceIds",
        "desc": "ID(s) of the instance(s) to be disassociated, such as `ins-lesecurk`. You can specify multiple instances."
      }
    ],
    "desc": "This API is used to disassociate security groups from instances."
  },
  "AllocateHosts": {
    "params": [
      {
        "name": "Placement",
        "desc": "Instance location. This parameter is used to specify the attributes of an instance, such as its availability zone and project."
      },
      {
        "name": "ClientToken",
        "desc": "A string used to ensure the idempotency of the request."
      },
      {
        "name": "HostChargePrepaid",
        "desc": "Configuration of prepaid instances. You can use the parameter to specify the attributes of prepaid instances, such as the subscription period and the auto-renewal plan. This parameter is required for prepaid instances."
      },
      {
        "name": "HostChargeType",
        "desc": "The billing method of an instance. Currently only `PREPAID` is supported."
      },
      {
        "name": "HostType",
        "desc": "CDH instance model. Default value: `HS1`."
      },
      {
        "name": "HostCount",
        "desc": "The quantity of CDH instances you want to purchase."
      },
      {
        "name": "TagSpecification",
        "desc": "Tag description. You can specify the parameter to associate a tag with an instance."
      }
    ],
    "desc": "This API is used to create CDH instances with specified configuration.\n* When HostChargeType is PREPAID, the HostChargePrepaid parameter must be specified."
  }
}