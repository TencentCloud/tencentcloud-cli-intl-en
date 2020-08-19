# -*- coding: utf-8 -*-
DESC = "monitor-2018-07-24"
INFO = {
  "DescribeProductEventList": {
    "params": [
      {
        "name": "Module",
        "desc": "API component name. It is fixed to monitor."
      },
      {
        "name": "ProductName",
        "desc": "Filter by product type. For example, 'cvm' indicates Cloud Virtual Machine."
      },
      {
        "name": "EventName",
        "desc": "Filter by product name. For example, \"guest_reboot\" indicates server restart."
      },
      {
        "name": "InstanceId",
        "desc": "Affected object, such as ins-19708ino."
      },
      {
        "name": "Dimensions",
        "desc": "Filter by dimension, such as by public IP: 10.0.0.1."
      },
      {
        "name": "RegionList",
        "desc": "Filter by region, such as by gz."
      },
      {
        "name": "Type",
        "desc": "Filter by event type. Valid values: [\"status_change\",\"abnormal\"], which indicate events whose statuses have changed and events with exceptions respectively."
      },
      {
        "name": "Status",
        "desc": "Filter by event status. Valid values: [\"recover\",\"alarm\",\"-\"], which indicate that an event has been recovered, has not been recovered, and has no status respectively."
      },
      {
        "name": "Project",
        "desc": "Filter by project ID."
      },
      {
        "name": "IsAlarmConfig",
        "desc": "Filter by alarm status configuration. The value 1 indicates that the alarm status has been configured. The value 0 indicates that the alarm status has not been configured."
      },
      {
        "name": "TimeOrder",
        "desc": "Sorting by update time. The value ASC indicates the ascending order. The value DESC indicates the descending order. The default value is DESC."
      },
      {
        "name": "StartTime",
        "desc": "Start time, which is the timestamp one day prior by default."
      },
      {
        "name": "EndTime",
        "desc": "End time, which is the current timestamp by default."
      },
      {
        "name": "Offset",
        "desc": "Page offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "The number of parameters that can be returned on each page. The default value is 20."
      }
    ],
    "desc": "This API is used to get the list of product events by page."
  },
  "DescribeAccidentEventList": {
    "params": [
      {
        "name": "Module",
        "desc": "API component name. The value for the current API is monitor."
      },
      {
        "name": "StartTime",
        "desc": "Start time, which is the timestamp one day prior by default."
      },
      {
        "name": "EndTime",
        "desc": "End time, which is the current timestamp by default."
      },
      {
        "name": "Limit",
        "desc": "Number of parameters that can be returned on each page. Value range: 1 - 100. Default value: 20."
      },
      {
        "name": "Offset",
        "desc": "Parameter offset on each page. The value starts from 0 and the default value is 0."
      },
      {
        "name": "UpdateTimeOrder",
        "desc": "Sorting rule by UpdateTime. Valid values: asc and desc."
      },
      {
        "name": "OccurTimeOrder",
        "desc": "Sorting rule by OccurTime. Valid values: asc or desc. Sorting by UpdateTimeOrder takes priority."
      },
      {
        "name": "AccidentType",
        "desc": "Filter by event type. The value 1 indicates service issues. The value 2 indicates other subscriptions."
      },
      {
        "name": "AccidentEvent",
        "desc": "Filter by event. The value 1 indicates CVM storage issues. The value 2 indicates CVM network connection issues. The value 3 indicates that the CVM has an exception. The value 202 indicates that an ISP network jitter occurs."
      },
      {
        "name": "AccidentStatus",
        "desc": "Filter by event status. The value 0 indicates that the event has been recovered. The value 1 indicates that the event has not been recovered."
      },
      {
        "name": "AccidentRegion",
        "desc": "Filter by region where the event occurs. The value gz indicates Guangzhou. The value sh indicates Shanghai."
      },
      {
        "name": "AffectResource",
        "desc": "Filter by affected resource, such as ins-19a06bka."
      }
    ],
    "desc": "This API is used to get the platform event list."
  },
  "UnBindingPolicyObject": {
    "params": [
      {
        "name": "Module",
        "desc": "The value is fixed to monitor."
      },
      {
        "name": "GroupId",
        "desc": "Policy group ID."
      },
      {
        "name": "UniqueId",
        "desc": "List of unique IDs of object instances to be deleted."
      },
      {
        "name": "InstanceGroupId",
        "desc": "Instance group ID. The UniqueId parameter is invalid if object instances are deleted by instance group."
      }
    ],
    "desc": "This API is used to delete an object that is bound to a policy."
  },
  "BindingPolicyObject": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Policy group ID."
      },
      {
        "name": "Module",
        "desc": "Required. The value is fixed to monitor."
      },
      {
        "name": "InstanceGroupId",
        "desc": "Instance group ID."
      },
      {
        "name": "Dimensions",
        "desc": "Dimensions of an object to be bound."
      }
    ],
    "desc": "This API is used to bind an alarm policy to a specific object."
  },
  "ModifyAlarmReceivers": {
    "params": [
      {
        "name": "GroupId",
        "desc": "ID of a policy group whose recipient needs to be modified."
      },
      {
        "name": "Module",
        "desc": "Required. The value is fixed to monitor."
      },
      {
        "name": "ReceiverInfos",
        "desc": "New recipient information. If this parameter is not configured, all recipients will be deleted."
      }
    ],
    "desc": "This API is used to modify alarm recipients."
  },
  "DescribeBindingPolicyObjectList": {
    "params": [
      {
        "name": "Module",
        "desc": "The value is fixed to monitor."
      },
      {
        "name": "GroupId",
        "desc": "Policy group ID."
      },
      {
        "name": "Limit",
        "desc": "Number of parameters that can be returned on each page. Value range: 1 - 100. Default value: 20."
      },
      {
        "name": "Offset",
        "desc": "Parameter offset on each page. The value starts from 0 and the default value is 0."
      },
      {
        "name": "Dimensions",
        "desc": "Dimensions of filtering objects."
      }
    ],
    "desc": "This API is used to get the bound object list."
  },
  "SendCustomAlarmMsg": {
    "params": [
      {
        "name": "Module",
        "desc": "API component name. The value for the current API is monitor."
      },
      {
        "name": "PolicyId",
        "desc": "Message policy ID, which is configured on the custom message page of Cloud Monitor."
      },
      {
        "name": "Msg",
        "desc": "Custom message content that a user wants to send."
      }
    ],
    "desc": "This API is used to send a custom alarm notification."
  },
  "DeletePolicyGroup": {
    "params": [
      {
        "name": "Module",
        "desc": "The value is fixed to monitor."
      },
      {
        "name": "GroupId",
        "desc": "Policy group ID."
      }
    ],
    "desc": "This API is used to delete an alarm policy group."
  },
  "DescribeBaseMetrics": {
    "params": [
      {
        "name": "Namespace",
        "desc": "Service namespace. Tencent Cloud services have different namespaces. For more information on service namespaces, see the monitoring metric documentation of each service. For example, see [CVM Monitoring Metrics](https://intl.cloud.tencent.com/document/product/248/6843?from_cn_redirect=1) for the namespace of CVM"
      },
      {
        "name": "MetricName",
        "desc": "Metric name. Tencent Cloud services have different metric names. For more information on metric names, see the monitoring metric documentation of each service. For example, see [CVM Monitoring Metrics](https://intl.cloud.tencent.com/document/product/248/6843?from_cn_redirect=1) for the metric names of CVM"
      }
    ],
    "desc": "This API is used to get the details of basic metrics."
  },
  "DescribePolicyGroupInfo": {
    "params": [
      {
        "name": "Module",
        "desc": "The value is fixed to monitor."
      },
      {
        "name": "GroupId",
        "desc": "Policy group ID."
      }
    ],
    "desc": "This API is used to get details of a basic policy group."
  },
  "DescribePolicyGroupList": {
    "params": [
      {
        "name": "Module",
        "desc": "The value is fixed to monitor."
      },
      {
        "name": "Limit",
        "desc": "Number of parameters that can be returned on each page. Value range: 1 - 100."
      },
      {
        "name": "Offset",
        "desc": "Parameter offset on each page. The value starts from 0."
      },
      {
        "name": "Like",
        "desc": "Search by policy name."
      },
      {
        "name": "InstanceGroupId",
        "desc": "Instance group ID."
      },
      {
        "name": "UpdateTimeOrder",
        "desc": "Sort by update time. Valid values: asc and desc."
      },
      {
        "name": "ProjectIds",
        "desc": "Project ID list."
      },
      {
        "name": "ViewNames",
        "desc": "List of alarm policy types."
      },
      {
        "name": "FilterUnuseReceiver",
        "desc": "Whether to filter policy groups without recipients. The value 1 indicates that policy groups without recipients will be filtered. The value 0 indicates that policy groups without recipients will not be filtered."
      },
      {
        "name": "Receivers",
        "desc": "Filter by recipient group."
      },
      {
        "name": "ReceiverUserList",
        "desc": "Filter by recipient."
      },
      {
        "name": "Dimensions",
        "desc": "Dimension set field (json string), for example, [[{\"name\":\"unInstanceId\",\"value\":\"ins-6e4b2aaa\"}]]."
      },
      {
        "name": "ConditionTempGroupId",
        "desc": "Template-based policy group IDs, which are separated by commas."
      },
      {
        "name": "ReceiverType",
        "desc": "Filter by recipient or recipient group. The value 'user' indicates by recipient. The value 'group' indicates by recipient group."
      },
      {
        "name": "IsOpen",
        "desc": "Filter conditions. Whether the alarm policy has been enabled or disabled"
      }
    ],
    "desc": "This API is used to get the list of basic policy alarm groups."
  },
  "DescribeBasicAlarmList": {
    "params": [
      {
        "name": "Module",
        "desc": "API component name. The value for the current API is monitor."
      },
      {
        "name": "StartTime",
        "desc": "Start time, which is the timestamp one day prior by default."
      },
      {
        "name": "EndTime",
        "desc": "End time, which is the current timestamp by default."
      },
      {
        "name": "Limit",
        "desc": "Number of parameters that can be returned on each page. Value range: 1 - 100. Default value: 20."
      },
      {
        "name": "Offset",
        "desc": "Parameter offset on each page. The value starts from 0 and the default value is 0."
      },
      {
        "name": "OccurTimeOrder",
        "desc": "Sorting by occurrence time. Valid values: asc and desc."
      },
      {
        "name": "ProjectIds",
        "desc": "Filter by project ID."
      },
      {
        "name": "ViewNames",
        "desc": "Filter by policy type."
      },
      {
        "name": "AlarmStatus",
        "desc": "Filter by alarm status."
      },
      {
        "name": "ObjLike",
        "desc": "Filter by alarm object."
      },
      {
        "name": "InstanceGroupIds",
        "desc": "Filter by instance group ID."
      },
      {
        "name": "MetricNames",
        "desc": "Filtering by metric names"
      }
    ],
    "desc": "This API is used to get the basic alarm list."
  },
  "GetMonitorData": {
    "params": [
      {
        "name": "Namespace",
        "desc": "Namespace. For detailed namespace descriptions of each Tencent Cloud service, see the corresponding [Monitoring Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1) documentation"
      },
      {
        "name": "MetricName",
        "desc": "Metric name. For detailed metric descriptions of each Tencent Cloud service, see the corresponding [Monitoring Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1) documentation"
      },
      {
        "name": "Instances",
        "desc": "Combination of instance object dimensions"
      },
      {
        "name": "Period",
        "desc": "Monitoring statistical period. The default value is 300, and the unit is s"
      },
      {
        "name": "StartTime",
        "desc": "Start time such as 2018-09-22T19:51:23+08:00"
      },
      {
        "name": "EndTime",
        "desc": "End time. Uses the current time by default and cannot be earlier than StartTime"
      }
    ],
    "desc": "This API is used to get the monitoring data of a Tencent Cloud service by passing in its namespace, object dimension description, and monitoring metrics.\nAPI call rate limit: 20 calls/second (1,200 calls/minute). A single request can obtain the data of up to 10 instances and up to 1,440 data points.\nThis API may fail due to the rate limit if you need to call a lot of metrics and objects. We recommended that you spread the call requests over time."
  },
  "ModifyPolicyGroup": {
    "params": [
      {
        "name": "Module",
        "desc": "The value is fixed to monitor."
      },
      {
        "name": "GroupId",
        "desc": "Policy group ID."
      },
      {
        "name": "ViewName",
        "desc": "Alarm type."
      },
      {
        "name": "GroupName",
        "desc": "Policy group name."
      },
      {
        "name": "IsUnionRule",
        "desc": "The 'AND' and 'OR' rules for metric alarms. The value 1 indicates 'AND', which means that an alarm will be triggered only when all rules are met. The value 0 indicates 'OR', which means that an alarm will be triggered when any rule is met."
      },
      {
        "name": "Conditions",
        "desc": "Metric alarm condition rules. No filling indicates that all existing metric alarm condition rules will be deleted."
      },
      {
        "name": "EventConditions",
        "desc": "Event alarm conditions. No filling indicates that all existing event alarm conditions will be deleted."
      },
      {
        "name": "ConditionTempGroupId",
        "desc": "Template-based policy group ID."
      }
    ],
    "desc": "This API is used to update policy group."
  },
  "CreatePolicyGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "Policy group name."
      },
      {
        "name": "Module",
        "desc": "The value is fixed to monitor."
      },
      {
        "name": "ViewName",
        "desc": "Name of the view to which the policy group belongs. If the policy group is created based on a template, this parameter is optional."
      },
      {
        "name": "ProjectId",
        "desc": "ID of the project to which the policy group belongs, which will be used for authentication."
      },
      {
        "name": "ConditionTempGroupId",
        "desc": "ID of a template-based policy group. This parameter is required only when the policy group is created based on a template."
      },
      {
        "name": "IsShielded",
        "desc": "Whether the policy group is shielded. The value 0 indicates that the policy group is not shielded. The value 1 indicates that the policy group is shielded. The default value is 0."
      },
      {
        "name": "Remark",
        "desc": "Remarks of the policy group."
      },
      {
        "name": "InsertTime",
        "desc": "Insertion time in the format of Unix timestamp. If this parameter is not configured, the backend processing time is used."
      },
      {
        "name": "Conditions",
        "desc": "Alarm threshold rules in the policy group."
      },
      {
        "name": "EventConditions",
        "desc": "Event alarm rules in the policy group."
      },
      {
        "name": "BackEndCall",
        "desc": "Whether it is a backend call. If the value is 1, rules from the policy template will be used to fill in the `Conditions` and `EventConditions` fields."
      },
      {
        "name": "IsUnionRule",
        "desc": "The 'AND' and 'OR' rules for alarm metrics. The value 0 indicates 'OR', which means that an alarm will be triggered when any rule is met. The value 1 indicates 'AND', which means that an alarm will be triggered only when all rules are met."
      }
    ],
    "desc": "This API is used to add a policy group."
  },
  "UnBindingAllPolicyObject": {
    "params": [
      {
        "name": "Module",
        "desc": "The value is fixed to monitor."
      },
      {
        "name": "GroupId",
        "desc": "Policy group ID."
      }
    ],
    "desc": "This API is used to delete all bound objects."
  },
  "PutMonitorData": {
    "params": [
      {
        "name": "Metrics",
        "desc": "A group of metrics and data."
      },
      {
        "name": "AnnounceIp",
        "desc": "IP address that is automatically specified when monitoring data is reported."
      },
      {
        "name": "AnnounceTimestamp",
        "desc": "Timestamp that is automatically specified when monitoring data is reported."
      },
      {
        "name": "AnnounceInstance",
        "desc": "IP address or product instance ID that is automatically specified when monitoring data is reported."
      }
    ],
    "desc": "The default API request rate limit is 50 requests/sec.\nThe default upper limit on metrics of a single tenant is 100.\nA maximum of 30 metric/value pairs can be reported at a time. When an error is returned for a request, no metrics/values in the request will be saved.\n\nThe reporting timestamp is the timestamp when you want to save the data. We recommend that you construct a timestamp at integer minutes.\nThe time range of a timestamp is from 300 seconds before the current time to the current time.\nThe data of the same IP metric/value pair must be reported by minute in chronological order."
  },
  "DescribePolicyConditionList": {
    "params": [
      {
        "name": "Module",
        "desc": "The value is fixed to monitor."
      }
    ],
    "desc": "This API is used to get basic alarm policy conditions."
  }
}