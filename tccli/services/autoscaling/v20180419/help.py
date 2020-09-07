# -*- coding: utf-8 -*-
DESC = "autoscaling-2018-04-19"
INFO = {
  "ExecuteScalingPolicy": {
    "params": [
      {
        "name": "AutoScalingPolicyId",
        "desc": "Alarm-based scaling policy ID"
      },
      {
        "name": "HonorCooldown",
        "desc": "Whether to check if the auto scaling group is in the cooldown period. Default value: false"
      },
      {
        "name": "TriggerSource",
        "desc": "Source that triggers the scaling policy. Valid values: API and CLOUD_MONITOR. Default value: API. The value `CLOUD_MONITOR` is specific to the Cloud Monitor service."
      }
    ],
    "desc": "This API (ExecuteScalingPolicy) is used to execute a scaling policy.\n\n* The scaling policy can be executed based on the scaling policy ID.\n* When the auto scaling group to which the scaling policy belongs is performing a scaling activity, the scaling policy will be rejected."
  },
  "CreateAutoScalingGroup": {
    "params": [
      {
        "name": "AutoScalingGroupName",
        "desc": "Auto scaling group name, which can only contain letters, numbers, underscores, hyphens (\"-\"), and decimal points with a maximum length of 55 bytes and must be unique under your account."
      },
      {
        "name": "LaunchConfigurationId",
        "desc": "Launch configuration ID"
      },
      {
        "name": "MaxSize",
        "desc": "Maximum number of instances. Value range: 0-2,000."
      },
      {
        "name": "MinSize",
        "desc": "Minimum number of instances. Value range: 0-2,000."
      },
      {
        "name": "VpcId",
        "desc": "VPC ID; if on a basic network, enter an empty string"
      },
      {
        "name": "DefaultCooldown",
        "desc": "Default cooldown period in seconds. Default value: 300"
      },
      {
        "name": "DesiredCapacity",
        "desc": "Desired number of instances. The number should be no larger than the maximum and no smaller than minimum number of instances"
      },
      {
        "name": "LoadBalancerIds",
        "desc": "List of classic CLB IDs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID"
      },
      {
        "name": "ForwardLoadBalancers",
        "desc": "List of CLBs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time."
      },
      {
        "name": "SubnetIds",
        "desc": "List of subnet IDs. A subnet must be specified in the VPC scenario. If multiple subnets are entered, their priority will be determined by the order in which they are entered, and they will be tried one by one until instances can be successfully created."
      },
      {
        "name": "TerminationPolicies",
        "desc": "Termination policy. Currently, the maximum length is 1. Value range: OLDEST_INSTANCE, NEWEST_INSTANCE. Default value: OLDEST_INSTANCE.\n<br><li> OLDEST_INSTANCE: The oldest instance in the auto scaling group will be terminated first.\n<br><li> NEWEST_INSTANCE: The newest instance in the auto scaling group will be terminated first."
      },
      {
        "name": "Zones",
        "desc": "List of availability zones. An availability zone must be specified in the basic network scenario. If multiple availability zones are entered, their priority will be determined by the order in which they are entered, and they will be tried one by one until instances can be successfully created."
      },
      {
        "name": "RetryPolicy",
        "desc": "Retry policy. Value range: IMMEDIATE_RETRY, INCREMENTAL_INTERVALS, and NO_RETRY. Default value: IMMEDIATE_RETRY.\n<br><li> IMMEDIATE_RETRY: Retrying immediately in a short period of time and stopping after a number of consecutive failures (5).\n<br><li> INCREMENTAL_INTERVALS: Retrying at incremental intervals, i.e., as the number of consecutive failures increases, the retry interval gradually increases, ranging from one second to one day.\n<br><li> NO_RETRY: No retry until a user call or alarm message is received again."
      },
      {
        "name": "ZonesCheckPolicy",
        "desc": "Availability zone verification policy. Value range: ALL, ANY. Default value: ANY.\n<br><li> ALL: The verification will succeed only if all availability zones (Zone) or subnets (SubnetId) are available; otherwise, an error will be reported.\n<br><li> ANY: The verification will success if any availability zone (Zone) or subnet (SubnetId) is available; otherwise, an error will be reported.\n\nCommon reasons why an availability zone or subnet is unavailable include stock-out of CVM instances or CBS cloud disks in the availability zone, insufficient quota in the availability zone, or insufficient IPs in the subnet.\nIf an availability zone or subnet in Zones/SubnetIds does not exist, a verification error will be reported regardless of the value of ZonesCheckPolicy."
      },
      {
        "name": "Tags",
        "desc": "List of tag descriptions. In this parameter, you can specify the tags to be bound with a scaling group as well as corresponding resource instances. Each scaling group can have up to 30 tags."
      },
      {
        "name": "ServiceSettings",
        "desc": "Service settings such as unhealthy instance replacement."
      },
      {
        "name": "Ipv6AddressCount",
        "desc": "The number of IPv6 addresses that an instance has. Valid values: 0 and 1. Default value: 0."
      },
      {
        "name": "MultiZoneSubnetPolicy",
        "desc": "Multi-availability zone/subnet policy. Valid values: PRIORITY and EQUALITY. Default value: PRIORITY.\n<br><li> PRIORITY: creates instances based on the priority determined by the order in the availability zone/subnet list. If an instance can be successfully created in the availability zone/subnet of the highest priority, all instances will be created in the availability zone/subnet.\n<br><li> EQUALITY: scales out the availability zone/subnet with the least instances each time. This gives each availability zone/subnet an opportunity for scale-out and disperses the instances created during multiple scale-out operations across different availability zones/subnets.\n\nNotes about this policy:\n<br><li> When the scaling group is based on basic network, this policy applies to multiple availability zones. When the scaling group is based on VPC, this policy applies to multiple subnets, and you do not need to consider availability zones. For example, if you have four subnets (A, B, C, and D) and A, B, and C are in availability zone 1 and D is in availability zone 2, you only need to decide the order of the four subnets, without worrying about the issue of availability zones.\n<br><li> This policy is applicable to multiple availability zones/subnets, but is not applicable to multiple models with launch configurations. When there are multiple models, the PRIORITY policy is applied.\n<br><li> During instance creation, apply the multi-model policy and then apply the multi-availability zones/subnet policy. For example, if you have models A and B and subnets 1, 2, and 3 (based on the PRIORITY policy), creation will be attempted in the following order: A1, A2, A3, B1, B2, and B3. If A1 is sold out, A2 (not B1) is tried next.\n<br><li> No matter what policy is used, a single scaling event always uses a specific configuration at priority (model * availability zone/subnet)."
      }
    ],
    "desc": "This API (CreateAutoScalingGroup) is used to create an auto scaling group."
  },
  "ModifyScalingPolicy": {
    "params": [
      {
        "name": "AutoScalingPolicyId",
        "desc": "Alarm policy ID."
      },
      {
        "name": "ScalingPolicyName",
        "desc": "Alarm policy name."
      },
      {
        "name": "AdjustmentType",
        "desc": "The method to adjust the desired number of instances after the alarm is triggered. Value range: <br><li>CHANGE_IN_CAPACITY: Increase or decrease the desired number of instances </li><li>EXACT_CAPACITY: Adjust to the specified desired number of instances </li> <li>PERCENT_CHANGE_IN_CAPACITY: Adjust the desired number of instances by percentage </li>"
      },
      {
        "name": "AdjustmentValue",
        "desc": "The adjusted value of desired number of instances after the alarm is triggered. Value range: <br><li>When AdjustmentType is CHANGE_IN_CAPACITY, if AdjustmentValue is a positive value, some new instances will be added after the alarm is triggered, and if it is a negative value, some existing instances will be removed after the alarm is triggered </li> <li> When AdjustmentType is EXACT_CAPACITY, the value of AdjustmentValue is the desired number of instances after the alarm is triggered, which should be equal to or greater than 0 </li> <li> When AdjustmentType is PERCENT_CHANGE_IN_CAPACITY, if AdjusmentValue (in %) is a positive value, new instances will be added by percentage after the alarm is triggered; if it is a negative value, existing instances will be removed by percentage after the alarm is triggered."
      },
      {
        "name": "Cooldown",
        "desc": "Cooldown period in seconds."
      },
      {
        "name": "MetricAlarm",
        "desc": "Alarm monitoring metric."
      },
      {
        "name": "NotificationUserGroupIds",
        "desc": "Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) API.\nIf you want to clear the user group, you need to pass in the specific string \"NULL\" to the list."
      }
    ],
    "desc": "This API (ModifyScalingPolicy) is used to modify an alarm trigger policy."
  },
  "ModifyScheduledAction": {
    "params": [
      {
        "name": "ScheduledActionId",
        "desc": "ID of the scheduled task to be edited"
      },
      {
        "name": "ScheduledActionName",
        "desc": "Scheduled task name, which can only contain letters, numbers, underscores, hyphens (\"-\"), and decimal points with a maximum length of 60 bytes and must be unique in an auto scaling group."
      },
      {
        "name": "MaxSize",
        "desc": "The maximum number of instances set for the auto scaling group when the scheduled task is triggered."
      },
      {
        "name": "MinSize",
        "desc": "The minimum number of instances set for the auto scaling group when the scheduled task is triggered."
      },
      {
        "name": "DesiredCapacity",
        "desc": "The desired number of instances set for the auto scaling group when the scheduled task is triggered."
      },
      {
        "name": "StartTime",
        "desc": "Initial triggered time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard."
      },
      {
        "name": "EndTime",
        "desc": "End time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard. <br>This parameter and `Recurrence` need to be specified at the same time. After the end time, the scheduled task will no longer take effect."
      },
      {
        "name": "Recurrence",
        "desc": "Repeating mode of the scheduled task, which is in standard cron format. <br>This parameter and `EndTime` need to be specified at the same time."
      }
    ],
    "desc": "This API (ModifyScheduledAction) is used to modify a scheduled task."
  },
  "DescribeNotificationConfigurations": {
    "params": [
      {
        "name": "AutoScalingNotificationIds",
        "desc": "Queries by one or more notification IDs in the format of asn-2sestqbr. The maximum number of instances per request is 100. This parameter does not support specifying both `AutoScalingNotificationIds` and `Filters` at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li> auto-scaling-notification-id - String - Required: No - (Filter) Filter by notification ID.</li>\n<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>\nThe maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `AutoScalingNotificationIds` and `Filters` at the same time."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      }
    ],
    "desc": "This API (DescribeNotificationConfigurations) is used to query the information of one or more notifications.\n\nYou can query the details of notifications based on information such as notification ID and auto scaling group ID. For more information on filters, see `Filter`.\nIf the parameter is empty, a certain number (specified by `Limit` and 20 by default) of notifications of the current user will be returned."
  },
  "DeleteAutoScalingGroup": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID"
      }
    ],
    "desc": "This API (DeleteAutoScalingGroup) is used to delete the specified auto scaling group that has no instances and remains inactive."
  },
  "StartAutoScalingInstances": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "The scaling group ID."
      },
      {
        "name": "InstanceIds",
        "desc": "The list of the CVM instances you want to start up."
      }
    ],
    "desc": "This API is used to start up CVM instances in a scaling group.\n* After startup, the instance will be in the `IN_SERVICE` status, which will increase the desired capacity. Please note that the desired capacity cannot exceed the maximum value.\n* This API supports batch operation. Up to 100 instances can be started up in each request."
  },
  "CreatePaiInstance": {
    "params": [
      {
        "name": "DomainName",
        "desc": "PAI instance domain name."
      },
      {
        "name": "InternetAccessible",
        "desc": "Information of the public network bandwidth configuration."
      },
      {
        "name": "InitScript",
        "desc": "Base64-encoded string of the launch script."
      },
      {
        "name": "Zones",
        "desc": "List of availability zones."
      },
      {
        "name": "VpcId",
        "desc": "VPC ID."
      },
      {
        "name": "SubnetIds",
        "desc": "List of subnets."
      },
      {
        "name": "InstanceName",
        "desc": "Instance display name."
      },
      {
        "name": "InstanceTypes",
        "desc": "List of instance models."
      },
      {
        "name": "LoginSettings",
        "desc": "Instance login settings."
      },
      {
        "name": "InstanceChargeType",
        "desc": "Instance billing type."
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "Relevant parameter settings for the prepaid mode (i.e., monthly subscription). This parameter can specify the purchased usage period, whether to set automatic renewal, and other attributes of the instance purchased on a prepaid basis. If the billing method of the specified instance is prepaid, this parameter is required."
      }
    ],
    "desc": "This API (CreatePaiInstance) is used to create a PAI instance."
  },
  "UpgradeLaunchConfiguration": {
    "params": [
      {
        "name": "LaunchConfigurationId",
        "desc": "Launch configuration ID."
      },
      {
        "name": "ImageId",
        "desc": "Valid [image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-8toqc6s3`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>This value can be obtained from the `ImageId` field in the return value of the [DescribeImages API](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1).</li>"
      },
      {
        "name": "InstanceTypes",
        "desc": "List of instance models. Different instance models specify different resource specifications. Up to 5 instance models can be supported."
      },
      {
        "name": "LaunchConfigurationName",
        "desc": "Display name of the launch configuration, which can contain Chinese characters, letters, numbers, underscores, separators (\"-\"), and decimal points with a maximum length of 60 bytes."
      },
      {
        "name": "DataDisks",
        "desc": "Information of the instance's data disk configuration. If this parameter is not specified, no data disk is purchased by default. Up to 11 data disks can be supported."
      },
      {
        "name": "EnhancedService",
        "desc": "Enhanced service. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, Cloud Monitoring and Cloud Security will be enabled by default."
      },
      {
        "name": "InstanceChargeType",
        "desc": "Instance billing type. CVM instances are POSTPAID_BY_HOUR by default.\n<br><li>POSTPAID_BY_HOUR: Pay-as-you-go on an hourly basis\n<br><li>SPOTPAID: Bidding"
      },
      {
        "name": "InstanceMarketOptions",
        "desc": "Market-related options of the instance, such as the parameters related to stop instances. If the billing method of instance is specified as bidding, this parameter must be passed in."
      },
      {
        "name": "InstanceTypesCheckPolicy",
        "desc": "Instance type verification policy. Value range: ALL, ANY. Default value: ANY.\n<br><li> ALL: The verification will success only if all instance types (InstanceType) are available; otherwise, an error will be reported.\n<br><li> ANY: The verification will success if any instance type (InstanceType) is available; otherwise, an error will be reported.\n\nCommon reasons why an instance type is unavailable include stock-out of the instance type and the corresponding cloud disk.\nIf a model in InstanceTypes does not exist or has been deactivated, a verification error will be reported regardless of the value of InstanceTypesCheckPolicy."
      },
      {
        "name": "InternetAccessible",
        "desc": "Configuration information of public network bandwidth. If this parameter is not specified, the default public network bandwidth is 0 Mbps."
      },
      {
        "name": "LoginSettings",
        "desc": "Login settings of the instance. This parameter is used to set the login password and key for the instance, or to keep the original login settings for the image. By default, a random password is generated and sent to the user via the internal message."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID of the instance. This parameter can be obtained from the `projectId` field in the returned values of [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1). If this is left empty, default project is used."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "The security group of instance. This parameter can be obtained by calling the `SecurityGroupId` field in the returned value of [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1). If this parameter is not specified, no security group will be bound by default."
      },
      {
        "name": "SystemDisk",
        "desc": "System disk configuration of the instance. If this parameter is not specified, the default value will be assigned to it."
      },
      {
        "name": "UserData",
        "desc": "Base64-encoded custom data of up to 16 KB."
      },
      {
        "name": "InstanceTags",
        "desc": "List of tags. This parameter is used to bind up to 10 tags to newly added instances."
      },
      {
        "name": "CamRoleName",
        "desc": "CAM role name, which can be obtained from the roleName field in the return value of the DescribeRoleList API."
      },
      {
        "name": "HostNameSettings",
        "desc": "CVM HostName settings."
      },
      {
        "name": "InstanceNameSettings",
        "desc": "Settings of CVM instance names."
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "Advance payment mode, also known as monthly subscription. This parameter can specify the purchase period and other attributes such as auto-renewal. This parameter is mandatory for prepaid instances."
      }
    ],
    "desc": "This API (UpgradeLaunchConfiguration) is used to upgrade a launch configuration.\n\n* This API is used to upgrade a launch configuration in a \"completely overriding\" manner, i.e., it uniformly sets a new configuration according to the API parameters regardless of the original parameters. If optional fields are left empty, their default values will be used.\n* After the launch configuration is upgraded, the existing instances that have been created by it will not be changed, but new instances will be created according to the new configuration."
  },
  "DescribeLaunchConfigurations": {
    "params": [
      {
        "name": "LaunchConfigurationIds",
        "desc": "Queries by one or more launch configuration IDs in the format of `asc-ouy1ax38`. The maximum quantity per request is 100. This parameter does not support specifying both `LaunchConfigurationIds` and `Filters` at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filters.\n<li> launch-configuration-id - String - Required: No - (Filter) Filter by launch configuration ID.</li>\n<li> launch-configuration-name - String - Required: No - (Filter) Filter by launch configuration name.</li>\n<li> launch-configuration-name - String - Required: No - (Filter) Fuzzy search by launch configuration name.</li>\nThe maximum number of `Filters` in each request is 10. The upper limit for `Filter.Values` is 5. This parameter cannot specify `LaunchConfigurationIds` and `Filters` at the same time."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      }
    ],
    "desc": "This API (DescribeLaunchConfigurations) is used to query the information of launch configurations.\n\n* You can query the launch configuration details based on information such as launch configuration ID and name. For more information on filters, see `Filter`.\n* If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of launch configurations of the current user will be returned."
  },
  "AttachInstances": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID"
      },
      {
        "name": "InstanceIds",
        "desc": "List of CVM instance IDs"
      }
    ],
    "desc": "This API (AttachInstances) is used to add CVM instances to an auto scaling group.\n"
  },
  "DescribeScalingPolicies": {
    "params": [
      {
        "name": "AutoScalingPolicyIds",
        "desc": "Queries by one or more alarm policy IDs in the format of asp-i9vkg894. The maximum number of instances per request is 100. This parameter does not support specifying both `AutoScalingPolicyIds` and `Filters` at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li> auto-scaling-policy-id - String - Required: No - (Filter) Filter by alarm policy ID.</li>\n<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>\n<li> scaling-policy-name - String - Required: No - (Filter) Filter by alarm policy name.</li>\nThe maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `AutoScalingPolicyIds` and `Filters` at the same time."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      }
    ],
    "desc": "This API (DescribeScalingPolicies) is used to query alarm trigger policies."
  },
  "DeleteScheduledAction": {
    "params": [
      {
        "name": "ScheduledActionId",
        "desc": "ID of the scheduled task to be deleted."
      }
    ],
    "desc": "This API (DeleteScheduledAction) is used to delete the specified scheduled task."
  },
  "StopAutoScalingInstances": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "The scaling group ID."
      },
      {
        "name": "InstanceIds",
        "desc": "The list of the CVM instances you want to shut down."
      },
      {
        "name": "StoppedMode",
        "desc": "Whether the shutdown instances will be charged. Valid values:  \nKEEP_CHARGING: keep charging after shutdown.  \nSTOP_CHARGING: stop charging after shutdown.\nDefault value: KEEP_CHARGING."
      }
    ],
    "desc": "This API is used to shut down CVM instances in a scaling group.\n* Use the `SOFT_FIRST` shutdown, which means the CVM will be forcibly shut down if the soft shutdown fails.\n* Shutting down instances in the `IN_SERVICE` status will reduce the desired capacity, but the desired capacity cannot be less than the minimum value.\n* To use the `STOP_CHARGING` shutdown, the instances you want to shut down must satisfy the conditions of [no charges when shut down](https://intl.cloud.tencent.com/document/product/213/19918?from_cn_redirect=1).\n* This API supports batch operation. Up to 100 instances can be shut down in each request."
  },
  "CreateScheduledAction": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID"
      },
      {
        "name": "ScheduledActionName",
        "desc": "Scheduled task name, which can only contain letters, numbers, underscores, hyphens (\"-\"), and decimal points with a maximum length of 60 bytes and must be unique in an auto scaling group."
      },
      {
        "name": "MaxSize",
        "desc": "The maximum number of instances set for the auto scaling group when the scheduled task is triggered."
      },
      {
        "name": "MinSize",
        "desc": "The minimum number of instances set for the auto scaling group when the scheduled task is triggered."
      },
      {
        "name": "DesiredCapacity",
        "desc": "The desired number of instances set for the auto scaling group when the scheduled task is triggered."
      },
      {
        "name": "StartTime",
        "desc": "Initial triggered time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard."
      },
      {
        "name": "EndTime",
        "desc": "End time of the scheduled task. The value is in `Beijing time` (UTC+8) in the format of `YYYY-MM-DDThh:mm:ss+08:00` according to the `ISO8601` standard. <br><br>This parameter and `Recurrence` need to be specified at the same time. After the end time, the scheduled task will no longer take effect."
      },
      {
        "name": "Recurrence",
        "desc": "Repeating mode of the scheduled task, which is in standard cron format. <br><br>This parameter and `EndTime` need to be specified at the same time."
      }
    ],
    "desc": "This API (CreateScheduledAction) is used to create a scheduled task."
  },
  "RemoveInstances": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID"
      },
      {
        "name": "InstanceIds",
        "desc": "List of CVM instance IDs"
      }
    ],
    "desc": "This API (RemoveInstances) is used to remove CVM instances from an auto scaling group. Instances created automatically by AS will be terminated, while those added to the auto scaling group after creation will be removed and retained."
  },
  "DeleteScalingPolicy": {
    "params": [
      {
        "name": "AutoScalingPolicyId",
        "desc": "ID of the alarm policy to be deleted."
      }
    ],
    "desc": "This API (DeleteScalingPolicy) is used to delete an alarm trigger policy."
  },
  "CompleteLifecycleAction": {
    "params": [
      {
        "name": "LifecycleHookId",
        "desc": "Lifecycle hook ID"
      },
      {
        "name": "LifecycleActionResult",
        "desc": "Result of the lifecycle action. Value range: \"CONTINUE\", \"ABANDON\""
      },
      {
        "name": "InstanceId",
        "desc": "Instance ID. Either \"InstanceId\" or \"LifecycleActionToken\" must be specified"
      },
      {
        "name": "LifecycleActionToken",
        "desc": "Either \"InstanceId\" or \"LifecycleActionToken\" must be specified"
      }
    ],
    "desc": "This API (CompleteLifecycleAction) is used to complete a lifecycle action.\n\n* The result (\"CONTINUE\" or \"ABANDON\") of a specific lifecycle hook can be specified by calling this API. If this API is not called at all, the lifecycle hook will be processed based on the \"DefaultResult\" after timeout.\n"
  },
  "ModifyLoadBalancers": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID"
      },
      {
        "name": "LoadBalancerIds",
        "desc": "List of classic CLB IDs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time."
      },
      {
        "name": "ForwardLoadBalancers",
        "desc": "List of CLBs. Currently, the maximum length is 20. You cannot specify LoadBalancerIds and ForwardLoadBalancers at the same time."
      },
      {
        "name": "LoadBalancersCheckPolicy",
        "desc": "CLB verification policy. Valid values: \"ALL\" and \"DIFF\". Default value: \"ALL\"\n<br><li> ALL. Verification is successful only when all CLBs are valid. Otherwise, verification fails.\n<br><li> DIFF. Only the changes in the CLB parameters are verified. If valid, the verification is successful. Otherwise, verification fails."
      }
    ],
    "desc": "This API (ModifyLoadBalancers) is used to modify the load balancers of an auto scaling group.\n\n* This API can specify a new load balancer configuration for the auto scaling group. The new configuration overwrites the original load balancer configuration.\n* If you want to clear the load balancer for the auto scaling group, specify only the auto scaling group ID but not the specific load balancer when calling this API.\n* This API modifies the load balancer of the auto scaling group and generate a scaling activity to asynchronously modify the load balancers of existing instances."
  },
  "ModifyDesiredCapacity": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID"
      },
      {
        "name": "DesiredCapacity",
        "desc": "Desired capacity"
      }
    ],
    "desc": "This API (ModifyDesiredCapacity) is used to modify the desired number of instances in the specified auto scaling group."
  },
  "SetInstancesProtection": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID."
      },
      {
        "name": "InstanceIds",
        "desc": "Instance ID."
      },
      {
        "name": "ProtectedFromScaleIn",
        "desc": "Whether the instance needs to be protected from scale-in."
      }
    ],
    "desc": "This API (SetInstancesProtection) is used to enable scale-in protection for an instance.\nWhen an instance has scale-in protection enabled, it will not be removed when scaling is triggered by replacement of unhealthy instances, alarm trigger policy, threshold change, etc."
  },
  "CreateLaunchConfiguration": {
    "params": [
      {
        "name": "LaunchConfigurationName",
        "desc": "Display name of the launch configuration, which can contain Chinese characters, letters, numbers, underscores, separators (\"-\"), and decimal points with a maximum length of 60 bytes."
      },
      {
        "name": "ImageId",
        "desc": "Valid [image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-8toqc6s3`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>This value can be obtained from the `ImageId` field in the return value of the [DescribeImages API](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1).</li>"
      },
      {
        "name": "ProjectId",
        "desc": "ID of the project to which the instance belongs. This parameter can be obtained from the `projectId` field in the returned values of [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1). If this is left empty, default project is used."
      },
      {
        "name": "InstanceType",
        "desc": "Instance model. Different instance models specify different resource specifications. The specific value can be obtained by calling the [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) API to get the latest specification table or referring to the descriptions in [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1).\n`InstanceType` and `InstanceTypes` are mutually exclusive, and one and only one of them must be entered."
      },
      {
        "name": "SystemDisk",
        "desc": "System disk configuration of the instance. If this parameter is not specified, the default value will be assigned to it."
      },
      {
        "name": "DataDisks",
        "desc": "Information of the instance's data disk configuration. If this parameter is not specified, no data disk is purchased by default. Up to 11 data disks can be supported."
      },
      {
        "name": "InternetAccessible",
        "desc": "Configuration information of public network bandwidth. If this parameter is not specified, the default public network bandwidth is 0 Mbps."
      },
      {
        "name": "LoginSettings",
        "desc": "Login settings of the instance. This parameter is used to set the login password and key for the instance, or to keep the original login settings for the image. By default, a random password is generated and sent to the user via the internal message."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "The security group to which the instance belongs. This parameter can be obtained by calling the `SecurityGroupId` field in the returned value of [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1). If this parameter is not specified, no security group will be bound by default."
      },
      {
        "name": "EnhancedService",
        "desc": "Enhanced service. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, Cloud Monitoring and Cloud Security will be enabled by default."
      },
      {
        "name": "UserData",
        "desc": "Base64-encoded custom data of up to 16 KB."
      },
      {
        "name": "InstanceChargeType",
        "desc": "Instance billing type. CVM instances are POSTPAID_BY_HOUR by default.\n<br><li>POSTPAID_BY_HOUR: Pay-as-you-go on an hourly basis\n<br><li>SPOTPAID: Bidding"
      },
      {
        "name": "InstanceMarketOptions",
        "desc": "Market-related options of the instance, such as the parameters related to stop instances. If the billing method of instance is specified as bidding, this parameter must be passed in."
      },
      {
        "name": "InstanceTypes",
        "desc": "List of instance models. Different instance models specify different resource specifications. Up to 10 instance models can be supported.\n`InstanceType` and `InstanceTypes` are mutually exclusive, and one and only one of them must be entered."
      },
      {
        "name": "InstanceTypesCheckPolicy",
        "desc": "Instance type verification policy. Value range: ALL, ANY. Default value: ANY.\n<br><li> ALL: The verification will success only if all instance types (InstanceType) are available; otherwise, an error will be reported.\n<br><li> ANY: The verification will success if any instance type (InstanceType) is available; otherwise, an error will be reported.\n\nCommon reasons why an instance type is unavailable include stock-out of the instance type or the corresponding cloud disk.\nIf a model in InstanceTypes does not exist or has been discontinued, a verification error will be reported regardless of the value of InstanceTypesCheckPolicy."
      },
      {
        "name": "InstanceTags",
        "desc": "List of tags. This parameter is used to bind up to 10 tags to newly added instances."
      },
      {
        "name": "CamRoleName",
        "desc": "CAM role name, which can be obtained from the roleName field in the return value of the DescribeRoleList API."
      },
      {
        "name": "HostNameSettings",
        "desc": "CVM HostName settings."
      },
      {
        "name": "InstanceNameSettings",
        "desc": "Settings of CVM instance names."
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "Sets prepaid billing mode, also known as monthly subscription. This parameter can specify the purchase period and other attributes such as auto-renewal. This parameter is mandatory for prepaid instances."
      }
    ],
    "desc": "This API (CreateLaunchConfiguration) is used to create a launch configuration.\n\n* A few fields of a launch configuration can be modified through `ModifyLaunchConfigurationAttributes`. To use a new launch configuration, it is recommended to create it from scratch.\n\n* You can create up to 20 launch configurations for each project. For more information, see [Usage Limits](https://intl.cloud.tencent.com/document/product/377/3120?from_cn_redirect=1).\n"
  },
  "ModifyNotificationConfiguration": {
    "params": [
      {
        "name": "AutoScalingNotificationId",
        "desc": "ID of the notification to be modified."
      },
      {
        "name": "NotificationTypes",
        "desc": "Notification type, i.e., the set of types of notifications to be subscribed to. Value range:\n<li>SCALE_OUT_SUCCESSFUL: scale-out succeeded</li>\n<li>SCALE_OUT_FAILED: scale-out failed</li>\n<li>SCALE_IN_SUCCESSFUL: scale-in succeeded</li>\n<li>SCALE_IN_FAILED: scale-in failed</li>\n<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL: unhealthy instance replacement succeeded</li>\n<li>REPLACE_UNHEALTHY_INSTANCE_FAILED: unhealthy instance replacement failed</li>"
      },
      {
        "name": "NotificationUserGroupIds",
        "desc": "Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) API."
      }
    ],
    "desc": "This API (ModifyNotificationConfiguration) is used to modify a notification."
  },
  "ModifyAutoScalingGroup": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID"
      },
      {
        "name": "AutoScalingGroupName",
        "desc": "Auto scaling group name, which can only contain letters, numbers, underscores, hyphens (\"-\"), and decimal points with a maximum length of 55 bytes and must be unique under your account."
      },
      {
        "name": "DefaultCooldown",
        "desc": "Default cooldown period in seconds. Default value: 300"
      },
      {
        "name": "DesiredCapacity",
        "desc": "Desired number of instances. The number should be no larger than the maximum and no smaller than minimum number of instances"
      },
      {
        "name": "LaunchConfigurationId",
        "desc": "Launch configuration ID"
      },
      {
        "name": "MaxSize",
        "desc": "Maximum number of instances. Value range: 0-2,000."
      },
      {
        "name": "MinSize",
        "desc": "Minimum number of instances. Value range: 0-2,000."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID"
      },
      {
        "name": "SubnetIds",
        "desc": "List of subnet IDs"
      },
      {
        "name": "TerminationPolicies",
        "desc": "Termination policy. Currently, the maximum length is 1. Value range: OLDEST_INSTANCE, NEWEST_INSTANCE.\n<br><li> OLDEST_INSTANCE: The oldest instance in the auto scaling group will be terminated first.\n<br><li> NEWEST_INSTANCE: The newest instance in the auto scaling group will be terminated first."
      },
      {
        "name": "VpcId",
        "desc": "VPC ID. This field is left empty for basic networks. You need to specify SubnetIds when modifying the network of the auto scaling group to a VPC with a specified VPC ID. Specify Zones when modifying the network to a basic network."
      },
      {
        "name": "Zones",
        "desc": "List of availability zones"
      },
      {
        "name": "RetryPolicy",
        "desc": "Retry policy. Value range: IMMEDIATE_RETRY, INCREMENTAL_INTERVALS, and NO_RETRY. Default value: IMMEDIATE_RETRY.\n<br><li> IMMEDIATE_RETRY: Retrying immediately in a short period of time and stopping after a number of consecutive failures (5).\n<br><li> INCREMENTAL_INTERVALS: Retrying at incremental intervals, i.e., as the number of consecutive failures increases, the retry interval gradually increases, ranging from one second to one day.\n<br><li> NO_RETRY: No retry until a user call or alarm message is received again."
      },
      {
        "name": "ZonesCheckPolicy",
        "desc": "Availability zone verification policy. Value range: ALL, ANY. Default value: ANY. This will work when the resource-related fields (launch configuration, availability zone, or subnet) of the auto scaling group are actually modified.\n<br><li> ALL: The verification will succeed only if all availability zones (Zone) or subnets (SubnetId) are available; otherwise, an error will be reported.\n<br><li> ANY: The verification will success if any availability zone (Zone) or subnet (SubnetId) is available; otherwise, an error will be reported.\n\nCommon reasons why an availability zone or subnet is unavailable include stock-out of CVM instances or CBS cloud disks in the availability zone, insufficient quota in the availability zone, or insufficient IPs in the subnet.\nIf an availability zone or subnet in Zones/SubnetIds does not exist, a verification error will be reported regardless of the value of ZonesCheckPolicy."
      },
      {
        "name": "ServiceSettings",
        "desc": "Service settings such as unhealthy instance replacement."
      },
      {
        "name": "Ipv6AddressCount",
        "desc": "The number of IPv6 addresses that an instance has. Valid values: 0 and 1."
      },
      {
        "name": "MultiZoneSubnetPolicy",
        "desc": "Multi-availability zone/subnet policy. Valid values: PRIORITY and EQUALITY.\n<br><li> PRIORITY: creates instances based on the priority determined by the order in the availability zone/subnet list. If an instance can be successfully created in the availability zone/subnet of the highest priority, all instances will be created in the availability zone/subnet.\n<br><li> EQUALITY: scales out the availability zone/subnet with the least instances each time. This gives each availability zone/subnet an opportunity for scale-out and disperses the instances created during multiple scale-out operations across different availability zones/subnets.\n\nNotes about this policy:\n<br><li> When the scaling group is a basic network, this policy applies to multiple availability zones. When the scaling group is a VPC, this policy applies to multiple subnets, and you do not need to consider availability zones. For example, if you have four subnets (A, B, C, and D) and A, B, and C are in availability zone 1 and D is in availability zone 2, you do not need to consider the availability zones when determining the order of the subnets.\n<br><li> This policy is applicable to multiple availability zones/subnets, but is not applicable to multiple models with launch configurations. When there are multiple models, the PRIORITY policy is applied.\n<br><li> During instance creation, apply the multi-model policy and then apply the multi-availability zones/subnet policy. For example, if you have models A and B and subnets 1, 2, and 3 (based on the PRIORITY policy), creation will be attempted in the following order: A1, A2, A3, B1, B2, and B3. If A1 is sold out, A2 (not B1) is tried next.\n<br><li> No matter what policy is used, a single scaling event always uses a specific configuration at priority (model * availability zone/subnet)."
      }
    ],
    "desc": "This API (ModifyAutoScalingGroup) is used to modify an auto scaling group."
  },
  "CreateNotificationConfiguration": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID."
      },
      {
        "name": "NotificationTypes",
        "desc": "Notification type, i.e., the set of types of notifications to be subscribed to. Value range:\n<li>SCALE_OUT_SUCCESSFUL: scale-out succeeded</li>\n<li>SCALE_OUT_FAILED: scale-out failed</li>\n<li>SCALE_IN_SUCCESSFUL: scale-in succeeded</li>\n<li>SCALE_IN_FAILED: scale-in failed</li>\n<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL: unhealthy instance replacement succeeded</li>\n<li>REPLACE_UNHEALTHY_INSTANCE_FAILED: unhealthy instance replacement failed</li>"
      },
      {
        "name": "NotificationUserGroupIds",
        "desc": "Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) API."
      }
    ],
    "desc": "This API (CreateNotificationConfiguration) is used to create a notification."
  },
  "DescribeAutoScalingInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "ID of the CVM instance to be queried. This parameter does not support specifying both InstanceIds and Filters at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li> instance-id - String - Required: No - (Filter) Filter by instance ID.</li>\n<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>\nThe maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `InstanceIds` and `Filters` at the same time."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      }
    ],
    "desc": "This API (DescribeAutoScalingInstances) is used to query the information of instances associated with AS.\n\n* You can query the details of instances based on information such as instance ID and auto scaling group ID. For more information on filters, see `Filter`.\n* If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of instances of the current user will be returned."
  },
  "CreateAutoScalingGroupFromInstance": {
    "params": [
      {
        "name": "AutoScalingGroupName",
        "desc": "The scaling group name. It must be unique under your account. The name can only contain letters, numbers, underscore, hyphen “-” and periods. It cannot exceed 55 bytes."
      },
      {
        "name": "InstanceId",
        "desc": "The instance ID."
      },
      {
        "name": "MinSize",
        "desc": "The maximum number of instances. Value range: 0 - 2000."
      },
      {
        "name": "MaxSize",
        "desc": "The minimum number of instances. Value range: 0 - 2000."
      },
      {
        "name": "DesiredCapacity",
        "desc": "The desired capacity. Its value must be greater than the minimum and smaller than the maximum."
      },
      {
        "name": "InheritInstanceTag",
        "desc": "Whether to inherit the instance tag. Default value: False"
      }
    ],
    "desc": "This API is used to create launch configurations and scaling groups based on an instance.\n\nNote: for a scaling group that is created based on a monthly-subscribed instance, the instances added for scale-out are pay-as-you-go instance."
  },
  "CreateLifecycleHook": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID"
      },
      {
        "name": "LifecycleHookName",
        "desc": "Lifecycle hook name, which can contain Chinese characters, letters, numbers, underscores (_), hyphens (-), and periods (.) with a maximum length of 128 bytes."
      },
      {
        "name": "LifecycleTransition",
        "desc": "Scenario for the lifecycle hook. Valid values: \"INSTANCE_LAUNCHING\" and \"INSTANCE_TERMINATING\""
      },
      {
        "name": "DefaultResult",
        "desc": "Defined actions when lifecycle hook times out. Valid values: \"CONTINUE\" and \"ABANDON\". Default value: \"CONTINUE\""
      },
      {
        "name": "HeartbeatTimeout",
        "desc": "The maximum length of time (in seconds) that can elapse before the lifecycle hook times out. Value range: 30-3,600. Default value: 300"
      },
      {
        "name": "NotificationMetadata",
        "desc": "Additional information sent by Auto Scaling to the notification target. Default value is ''. Maximum length is 1024 characters."
      },
      {
        "name": "NotificationTarget",
        "desc": "Notification target"
      },
      {
        "name": "LifecycleTransitionType",
        "desc": "The scenario where the lifecycle hook is applied. `EXTENSION`: the lifecycle hook will be triggered when AttachInstances, DetachInstances or RemoveInstaces is called. `NORMAL`: the lifecycle hook is not triggered by the above APIs. "
      }
    ],
    "desc": "This API (CreateLifeCycleHook) is used to create a lifecycle hook.\n\n* You can configure message notifications in the following format for lifecycle hooks, which will be sent to your CMQ queue by AS:\n\n```\n{\n\t\"Service\": \"Tencent Cloud Auto Scaling\",\n\t\"Time\": \"2019-03-14T10:15:11Z\",\n\t\"AppId\": \"1251783334\",\n\t\"ActivityId\": \"asa-fznnvrja\",\n\t\"AutoScalingGroupId\": \"asg-rrrrtttt\",\n\t\"LifecycleHookId\": \"ash-xxxxyyyy\",\n\t\"LifecycleHookName\": \"my-hook\",\n\t\"LifecycleActionToken\": \"3080e1c9-0efe-4dd7-ad3b-90cd6618298f\",\n\t\"InstanceId\": \"ins-aaaabbbb\",\n\t\"LifecycleTransition\": \"INSTANCE_LAUNCHING\",\n\t\"NotificationMetadata\": \"\"\n}\n```"
  },
  "UpgradeLifecycleHook": {
    "params": [
      {
        "name": "LifecycleHookId",
        "desc": "Lifecycle hook ID"
      },
      {
        "name": "LifecycleHookName",
        "desc": "Lifecycle hook name"
      },
      {
        "name": "LifecycleTransition",
        "desc": "Scenario for the lifecycle hook. Value range: \"INSTANCE_LAUNCHING\", \"INSTANCE_TERMINATING\""
      },
      {
        "name": "DefaultResult",
        "desc": "Defines the action to be taken by the auto scaling group upon lifecycle hook timeout. Value range: \"CONTINUE\", \"ABANDON\". Default value: \"CONTINUE\""
      },
      {
        "name": "HeartbeatTimeout",
        "desc": "The maximum length of time (in seconds) that can elapse before the lifecycle hook times out. Value range: 30-3,600. Default value: 300"
      },
      {
        "name": "NotificationMetadata",
        "desc": "Additional information sent by AS to the notification target. The default value is ''"
      },
      {
        "name": "NotificationTarget",
        "desc": "Notification target"
      },
      {
        "name": "LifecycleTransitionType",
        "desc": "The scenario where the lifecycle hook is applied. `EXTENSION`: the lifecycle hook will be triggered when AttachInstances, DetachInstances or RemoveInstaces is called. `NORMAL`: the lifecycle hook is not triggered by the above APIs. "
      }
    ],
    "desc": "This API (UpgradeLifecycleHook) is used to upgrade a lifecycle hook.\n\n* This API is used to upgrade a lifecycle hook in a \"completely overriding\" manner, i.e., it uniformly sets a new configuration according to the API parameters regardless of the original parameters. If optional fields are left empty, their default values will be used.\n"
  },
  "DisableAutoScalingGroup": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID"
      }
    ],
    "desc": "This API (DisableAutoScalingGroup) is used to disable the specified auto scaling group."
  },
  "PreviewPaiDomainName": {
    "params": [
      {
        "name": "DomainNameType",
        "desc": "Domain name type"
      }
    ],
    "desc": "This API (PreviewPaiDomainName) is used to preview a PAI domain name.\n"
  },
  "DescribePaiInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "Queries by PAI instance ID."
      },
      {
        "name": "Filters",
        "desc": "Filter."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API (DescribePaiInstances) is used to query the information of PAI instances.\n\n* You can query the detailed information of PAI instances based on information such as instance ID and instance domain name. For more information on filters, see `Filter`.\n* If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of PAI instances of the current user will be returned."
  },
  "CreateScalingPolicy": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID."
      },
      {
        "name": "ScalingPolicyName",
        "desc": "Alarm trigger policy name."
      },
      {
        "name": "AdjustmentType",
        "desc": "The method to adjust the desired number of instances after the alarm is triggered. Value range: <br><li>CHANGE_IN_CAPACITY: Increase or decrease the desired number of instances </li><li>EXACT_CAPACITY: Adjust to the specified desired number of instances </li> <li>PERCENT_CHANGE_IN_CAPACITY: Adjust the desired number of instances by percentage </li>"
      },
      {
        "name": "AdjustmentValue",
        "desc": "The adjusted value of desired number of instances after the alarm is triggered. Value range: <br><li>When AdjustmentType is CHANGE_IN_CAPACITY, if AdjustmentValue is a positive value, some new instances will be added after the alarm is triggered, and if it is a negative value, some existing instances will be removed after the alarm is triggered </li> <li> When AdjustmentType is EXACT_CAPACITY, the value of AdjustmentValue is the desired number of instances after the alarm is triggered, which should be equal to or greater than 0 </li> <li> When AdjustmentType is PERCENT_CHANGE_IN_CAPACITY, if AdjusmentValue (in %) is a positive value, new instances will be added by percentage after the alarm is triggered; if it is a negative value, existing instances will be removed by percentage after the alarm is triggered."
      },
      {
        "name": "MetricAlarm",
        "desc": "Alarm monitoring metric."
      },
      {
        "name": "Cooldown",
        "desc": "Cooldown period in seconds. Default value: 300 seconds."
      },
      {
        "name": "NotificationUserGroupIds",
        "desc": "Notification group ID, which is the set of user group IDs. You can query the user group IDs through the [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) API."
      }
    ],
    "desc": "This API (CreateScalingPolicy) is used to create an alarm trigger policy."
  },
  "DeleteLaunchConfiguration": {
    "params": [
      {
        "name": "LaunchConfigurationId",
        "desc": "ID of the launch configuration to be deleted."
      }
    ],
    "desc": "This API (DeleteLaunchConfiguration) is used to delete a launch configuration.\n\n* If the launch configuration is active in an auto scaling group, it cannot be deleted.\n"
  },
  "DeleteLifecycleHook": {
    "params": [
      {
        "name": "LifecycleHookId",
        "desc": "Lifecycle hook ID"
      }
    ],
    "desc": "This API (DeleteLifeCycleHook) is used to delete a lifecycle hook."
  },
  "DescribeAutoScalingGroupLastActivities": {
    "params": [
      {
        "name": "AutoScalingGroupIds",
        "desc": "ID list of an auto scaling group."
      }
    ],
    "desc": "This API is used to query the latest activity history of an auto scaling group."
  },
  "DescribeLifecycleHooks": {
    "params": [
      {
        "name": "LifecycleHookIds",
        "desc": "Queries by one or more lifecycle hook IDs in the format of `ash-8azjzxcl`. The maximum quantity per request is 100. This parameter does not support specifying both `LifecycleHookIds` and `Filters` at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li> lifecycle-hook-id - String - Required: No - (Filter) Filter by lifecycle hook ID.</li>\n<li> lifecycle-hook-name - String - Required: No - (Filter) Filter by lifecycle hook name.</li>\n<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>\nFilter.\n<li> lifecycle-hook-id - String - Required: No - (Filter) Filter by lifecycle hook ID.</li>\n<li> lifecycle-hook-name - String - Required: No - (Filter) Filter by lifecycle hook name.</li>\n<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>\nThe maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `LifecycleHookIds` and `Filters` at the same time."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      }
    ],
    "desc": "This API (DescribeLifecycleHooks) is used to query the information of lifecycle hooks.\n\n* You can query the details of lifecycle hooks based on information such as auto scaling group ID, lifecycle hook ID, or lifecycle hook name. For more information on filters, see `Filter`.\n* If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of lifecycle hooks of the current user will be returned."
  },
  "EnableAutoScalingGroup": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID"
      }
    ],
    "desc": "This API (EnableAutoScalingGroup) is used to enable the specified auto scaling group."
  },
  "DescribeAccountLimits": {
    "params": [],
    "desc": "This API (DescribeAccountLimits) is used to query the limits of user's AS resources."
  },
  "DescribeAutoScalingGroups": {
    "params": [
      {
        "name": "AutoScalingGroupIds",
        "desc": "Queries by one or more auto scaling group IDs in the format of `asg-nkdwoui0`. The maximum quantity per request is 100. This parameter does not support specifying both `AutoScalingGroupIds` and `Filters` at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filters.\n<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>\n<li> auto-scaling-group-name - String - Required: No - (Filter) Filter by auto scaling group name.</li>\n<li> vague-auto-scaling-group-name - String - Required: No - (Filter) Fuzzy search by auto scaling group name.</li>\n<li> launch-configuration-id - String - Required: No - (Filter) Filter by launch configuration ID.</li>\n<li> tag-key - String - Required: No - (Filter) Filter by tag key.</li>\n<li> tag-value - String - Required: No - (Filter) Filter by tag value.</li>\n<li> tag:tag-key - String - Required: No - (Filter) Filter by tag key-value pair. The tag-key should be replaced with a specified tag key. For more information, see example 2.</li>\nThe maximum number of `Filters` in each request is 10. The upper limit for `Filter.Values` is 5. This parameter cannot specify `AutoScalingGroupIds` and `Filters` at the same time."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      }
    ],
    "desc": "This API (DescribeAutoScalingGroups) is used to query the information of auto scaling groups.\n\n* You can query the details of auto scaling groups based on information such as auto scaling group ID, auto scaling group name, or launch configuration ID. For more information on filters, see `Filter`.\n* If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of auto scaling groups of the current user will be returned."
  },
  "DetachInstances": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "Auto scaling group ID"
      },
      {
        "name": "InstanceIds",
        "desc": "List of CVM instance IDs"
      }
    ],
    "desc": "This API (DetachInstances) is used to remove CVM instances from an auto scaling group. Instances removed via this API will not be terminated."
  },
  "DescribeAutoScalingActivities": {
    "params": [
      {
        "name": "ActivityIds",
        "desc": "Queries by one or more scaling activity IDs in the format of `asa-5l2ejpfo`. The maximum quantity per request is 100. This parameter does not support specifying both `ActivityIds` and `Filters` at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>\n<li> activity-status-code - String - Required: No - (Filter) Filter by scaling activity status . (INIT: initializing | RUNNING: running | SUCCESSFUL: succeeded | PARTIALLY_SUCCESSFUL: partially succeeded | FAILED: failed | CANCELLED: canceled)</li>\n<li> activity-type - String - Required: No - (Filter) Filter by scaling activity type. (SCALE_OUT: scale-out | SCALE_IN: scale-in | ATTACH_INSTANCES: adding an instance | REMOVE_INSTANCES: terminating an instance | DETACH_INSTANCES: removing an instance | TERMINATE_INSTANCES_UNEXPECTEDLY: terminating an instance in the CVM console | REPLACE_UNHEALTHY_INSTANCE: replacing an unhealthy instance | UPDATE_LOAD_BALANCERS: updating a load balancer)</li>\n<li> activity-id - String - Required: No - (Filter) Filter by scaling activity ID.</li>\nThe maximum number of `Filters` per request is 10. The upper limit for `Filter.Values` is 5. This parameter does not support specifying both `ActivityIds` and `Filters` at the same time."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      },
      {
        "name": "StartTime",
        "desc": "The earliest start time of the scaling activity, which will be ignored if ActivityIds is specified. The value is in `UTC time` in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard."
      },
      {
        "name": "EndTime",
        "desc": "The latest end time of the scaling activity, which will be ignored if ActivityIds is specified. The value is in `UTC time` in the format of `YYYY-MM-DDThh:mm:ssZ` according to the `ISO8601` standard."
      }
    ],
    "desc": "This API (DescribeAutoScalingActivities) is used to query the activity history of an auto scaling group."
  },
  "DeleteNotificationConfiguration": {
    "params": [
      {
        "name": "AutoScalingNotificationId",
        "desc": "ID of the notification to be deleted."
      }
    ],
    "desc": "This API (DeleteNotificationConfiguration) is used to delete the specified notification."
  },
  "DescribeScheduledActions": {
    "params": [
      {
        "name": "ScheduledActionIds",
        "desc": "Queries by one or more scheduled task IDs in the format of asst-am691zxo. The maximum number of instances per request is 100. This parameter does not support specifying both ScheduledActionIds` and `Filters` at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li> scheduled-action-id - String - Required: No - (Filter) Filter by scheduled task ID.</li>\n<li> scheduled-action-name - String - Required: No - (Filter) Filter by scheduled task name.</li>\n<li> auto-scaling-group-id - String - Required: No - (Filter) Filter by auto scaling group ID.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0. For more information on `Offset`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section in the API [overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1)."
      }
    ],
    "desc": "This API (DescribeScheduledActions) is used to query the details of one or more scheduled tasks.\n\n* You can query the details of scheduled tasks based on information such as scheduled task ID, scheduled task name, or auto scaling group ID. For more information on filters, see `Filter`.\n* If the parameter is empty, a certain number (specified by `Limit` and 20 by default) of scheduled tasks of the current user will be returned."
  },
  "ModifyLaunchConfigurationAttributes": {
    "params": [
      {
        "name": "LaunchConfigurationId",
        "desc": "Launch configuration ID"
      },
      {
        "name": "ImageId",
        "desc": "Valid [image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-8toqc6s3`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>This value can be obtained from the `ImageId` field in the return value of the [DescribeImages API](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1).</li>"
      },
      {
        "name": "InstanceTypes",
        "desc": "List of instance types. Different instance models specify different resource specifications. Up to 5 instance models can be supported.\nThe launch configuration uses InstanceType to indicate one single instance type and InstanceTypes to indicate multiple instance types. After InstanceTypes is successfully specified for the launch configuration, the original InstanceType will be automatically invalidated."
      },
      {
        "name": "InstanceTypesCheckPolicy",
        "desc": "Instance type verification policy which works when InstanceTypes is actually modified. Value range: ALL, ANY. Default value: ANY.\n<br><li> ALL: The verification will success only if all instance types (InstanceType) are available; otherwise, an error will be reported.\n<br><li> ANY: The verification will success if any instance type (InstanceType) is available; otherwise, an error will be reported.\n\nCommon reasons why an instance type is unavailable include stock-out of the instance type or the corresponding cloud disk.\nIf a model in InstanceTypes does not exist or has been discontinued, a verification error will be reported regardless of the value of InstanceTypesCheckPolicy."
      },
      {
        "name": "LaunchConfigurationName",
        "desc": "Display name of the launch configuration, which can contain Chinese characters, letters, numbers, underscores, separators (\"-\"), and decimal points with a maximum length of 60 bytes."
      },
      {
        "name": "UserData",
        "desc": "Base64-encoded custom data of up to 16 KB. If you want to clear UserData, specify it as an empty string"
      }
    ],
    "desc": "This API (ModifyLaunchConfigurationAttributes) is used to modify some attributes of a launch configuration.\n\n* The changes of launch configuration do not affect the existing instances. New instances will be created based on the modified configuration.\n* This API supports modifying certain simple types of attributes."
  }
}