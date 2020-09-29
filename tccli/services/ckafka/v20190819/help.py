# -*- coding: utf-8 -*-
DESC = "ckafka-2019-08-19"
INFO = {
  "DescribeRoute": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Unique instance ID"
      }
    ],
    "desc": "This API is used to view route information."
  },
  "DescribeGroupInfo": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "(Filter) filter by instance ID."
      },
      {
        "name": "GroupList",
        "desc": "Kafka consumer group (`Consumer-group`), which is an array in the format of `GroupList.0=xxx&GroupList.1=yyy`."
      }
    ],
    "desc": "This API is used to get consumer group information."
  },
  "CreateAcl": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID information"
      },
      {
        "name": "ResourceType",
        "desc": "ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available, and other fields will be used for future ACLs compatible with open-source Kafka"
      },
      {
        "name": "ResourceName",
        "desc": "Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name"
      },
      {
        "name": "Operation",
        "desc": "ACL operation mode. 0: UNKNOWN, 1: ANY, 2: ALL, 3: READ, 4: WRITE, 5: CREATE, 6: DELETE, 7: ALTER, 8: DESCRIBE, 9: CLUSTER_ACTION, 10: DESCRIBE_CONFIGS, 11: ALTER_CONFIGS"
      },
      {
        "name": "PermissionType",
        "desc": "Permission type. 0: UNKNOWN, 1: ANY, 2: DENY, 3: ALLOW. Currently, CKafka supports `ALLOW` (equivalent to allowlist), and other fields will be used for future ACLs compatible with open-source Kafka"
      },
      {
        "name": "Host",
        "desc": "The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this"
      },
      {
        "name": "Principal",
        "desc": "User list. The default value is `*`, which means that any user can access. The current user can only be one included in the user list"
      }
    ],
    "desc": "This API is used to add an ACL policy."
  },
  "ModifyTopicAttributes": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID."
      },
      {
        "name": "TopicName",
        "desc": "Topic name."
      },
      {
        "name": "Note",
        "desc": "Topic remarks string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "EnableWhiteList",
        "desc": "IP allowlist switch. 1: enabled, 0: disabled."
      },
      {
        "name": "MinInsyncReplicas",
        "desc": "Default value: 1."
      },
      {
        "name": "UncleanLeaderElectionEnable",
        "desc": "0: false, 1: true. Default value: 0."
      },
      {
        "name": "RetentionMs",
        "desc": "Message retention period in ms. The current minimum value is 60,000 ms."
      },
      {
        "name": "SegmentMs",
        "desc": "Segment rolling duration in ms. The current minimum value is 86,400,000 ms."
      },
      {
        "name": "MaxMessageBytes",
        "desc": "Maximum topic message length in bytes. The maximum value is 8,388,608 bytes (i.e., 8 MB)."
      },
      {
        "name": "CleanUpPolicy",
        "desc": "Message deletion policy. Valid values: delete, compact"
      }
    ],
    "desc": "This API is used to modify topic attributes."
  },
  "CreateTopicIpWhiteList": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "TopicName",
        "desc": "Topic name"
      },
      {
        "name": "IpWhiteList",
        "desc": "IP allowlist list"
      }
    ],
    "desc": "This API is used to create a topic IP allowlist."
  },
  "DescribeGroup": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "SearchWord",
        "desc": "Search keyword"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Maximum number of results to be returned"
      }
    ],
    "desc": "This API is used to enumerate consumer groups (simplified)."
  },
  "ModifyGroupOffsets": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Kafka instance ID"
      },
      {
        "name": "Group",
        "desc": "Kafka consumer group"
      },
      {
        "name": "Strategy",
        "desc": "Offset resetting policy. Meanings of the input parameters: 0: equivalent to the `shift-by` parameter, which indicates to shift the offset forward or backward by the value of the `shift`. 1: equivalent to `by-duration`, `to-datetime`, `to-earliest`, or `to-latest`, which indicates to move the offset to the specified timestamp. 2: equivalent to `to-offset`, which indicates to move the offset to the specified offset position"
      },
      {
        "name": "Topics",
        "desc": "Indicates the topics to be reset. If this parameter is left empty, all topics will be reset"
      },
      {
        "name": "Shift",
        "desc": "When `strategy` is 0, this field is required. If it is above zero, the offset will be shifted backward by the value of the `shift`. If it is below zero, the offset will be shifted forward by the value of the `shift`. After a correct reset, the new offset should be (old_offset + shift). Note that if the new offset is smaller than the `earliest` parameter of the partition, it will be set to `earliest`, and if it is greater than the `latest` parameter of the partition, it will be set to `latest`"
      },
      {
        "name": "ShiftTimestamp",
        "desc": "Unit: ms. When `strategy` is 1, this field is required, where -2 indicates to reset the offset to the initial position, -1 indicates to reset to the latest position (equivalent to emptying), and other values represent the specified time, i.e., the offset of the topic at the specified time will be obtained and then reset. Note that if there is no message at the specified time, the last offset will be obtained"
      },
      {
        "name": "Offset",
        "desc": "Position of the offset that needs to be reset. When `strategy` is 2, this field is required"
      }
    ],
    "desc": "This API is used to set the consumer group (Groups) offset."
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "(Filter) filter by instance ID"
      },
      {
        "name": "SearchWord",
        "desc": "(Filter) filter by instance name. Fuzzy search is supported"
      },
      {
        "name": "Status",
        "desc": "(Filter) instance status. 0: creating, 1: running, 2: deleting. If this parameter is left empty, all instances will be returned by default"
      },
      {
        "name": "Offset",
        "desc": "Offset. If this parameter is left empty, 0 will be used by default"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 100."
      },
      {
        "name": "TagKey",
        "desc": "Tag key match."
      }
    ],
    "desc": "This API is used to get the list of CKafka instances under a user account."
  },
  "ModifyInstanceAttributes": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "MsgRetentionTime",
        "desc": "Maximum retention period in minutes for instance log, which can be up to 30 days. 0 indicates not to enable the log retention period policy"
      },
      {
        "name": "InstanceName",
        "desc": "Instance name string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)"
      },
      {
        "name": "Config",
        "desc": "Instance configuration"
      }
    ],
    "desc": "This API is used to set instance attributes."
  },
  "DescribeUser": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "SearchWord",
        "desc": "Filter by name"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned in this request"
      }
    ],
    "desc": "This API is used to query user information."
  },
  "DescribeACL": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "ResourceType",
        "desc": "ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available, and other fields will be used for future ACLs compatible with open-source Kafka"
      },
      {
        "name": "ResourceName",
        "desc": "Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name"
      },
      {
        "name": "Offset",
        "desc": "Offset position"
      },
      {
        "name": "Limit",
        "desc": "Quantity limit"
      },
      {
        "name": "SearchWord",
        "desc": "Keyword match"
      }
    ],
    "desc": "This API is used to enumerate ACLs."
  },
  "DescribeTopicDetail": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "SearchWord",
        "desc": "(Filter) filter by `topicName`. Fuzzy search is supported"
      },
      {
        "name": "Offset",
        "desc": "Offset. If this parameter is left empty, 0 will be used by default"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20. This value must be greater than 0"
      }
    ],
    "desc": "This API is used to get topic list details (only for call in the console)."
  },
  "DeleteTopicIpWhiteList": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "TopicName",
        "desc": "Topic name"
      },
      {
        "name": "IpWhiteList",
        "desc": "IP allowlist list"
      }
    ],
    "desc": "This API is used to delete a topic IP allowlist."
  },
  "ModifyPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Name",
        "desc": "Username"
      },
      {
        "name": "Password",
        "desc": "Current user password"
      },
      {
        "name": "PasswordNew",
        "desc": "New user password"
      }
    ],
    "desc": "This API is used to change the password."
  },
  "DescribeConsumerGroup": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "CKafka instance ID."
      },
      {
        "name": "GroupName",
        "desc": "Name of the group to be queried, which is optional."
      },
      {
        "name": "TopicName",
        "desc": "Name of the corresponding topic in the group to be queried, which is optional. If this parameter is specified but `group` is not specified, this parameter will be ignored."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned in this request"
      },
      {
        "name": "Offset",
        "desc": "Offset position"
      }
    ],
    "desc": "This API is used to query consumer group information."
  },
  "CreateTopic": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "TopicName",
        "desc": "Topic name string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)"
      },
      {
        "name": "PartitionNum",
        "desc": "Number of partitions, which should be greater than 0"
      },
      {
        "name": "ReplicaNum",
        "desc": "Number of replicas, which cannot be higher than the number of brokers. Maximum value: 3"
      },
      {
        "name": "EnableWhiteList",
        "desc": "IP allowlist switch. 1: enabled, 0: disabled. Default value: 0"
      },
      {
        "name": "IpWhiteList",
        "desc": "IP allowlist list for quota limit, which is required if `enableWhileList` is 1"
      },
      {
        "name": "CleanUpPolicy",
        "desc": "Log cleanup policy, which is `delete` by default. `delete`: logs will be deleted by save time; `compact`: logs will be compressed by key; `compact, delete`: logs will be compressed by key and deleted by save time."
      },
      {
        "name": "Note",
        "desc": "Topic remarks string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)"
      },
      {
        "name": "MinInsyncReplicas",
        "desc": "Default value: 1"
      },
      {
        "name": "UncleanLeaderElectionEnable",
        "desc": "Whether to allow an unsynced replica to be elected as leader. false: no, true: yes. Default value: false"
      },
      {
        "name": "RetentionMs",
        "desc": "Message retention period in ms, which is optional. The current minimum value is 60,000 ms"
      },
      {
        "name": "SegmentMs",
        "desc": "Segment rolling duration in ms. The current minimum value is 3,600,000 ms"
      }
    ],
    "desc": "This API is used to create a CKafka topic."
  },
  "CreatePartition": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "TopicName",
        "desc": "Topic name"
      },
      {
        "name": "PartitionNum",
        "desc": "Number of topic partitions"
      }
    ],
    "desc": "This API is used to add a partition in a topic."
  },
  "DeleteAcl": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID information"
      },
      {
        "name": "ResourceType",
        "desc": "ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available, and other fields will be used for future ACLs compatible with open-source Kafka"
      },
      {
        "name": "ResourceName",
        "desc": "Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name"
      },
      {
        "name": "Operation",
        "desc": "ACL operation mode. 0: UNKNOWN, 1: ANY, 2: ALL, 3: READ, 4: WRITE, 5: CREATE, 6: DELETE, 7: ALTER, 8: DESCRIBE, 9: CLUSTER_ACTION, 10: DESCRIBE_CONFIGS, 11: ALTER_CONFIGS, 12: IDEMPOTEN_WRITE. Currently, CKafka only supports `READ` and `WRITE`, and other values will be used for future ACLs compatible with open-source Kafka"
      },
      {
        "name": "PermissionType",
        "desc": "Permission type. 0: UNKNOWN, 1: ANY, 2: DENY, 3: ALLOW. Currently, CKafka supports `ALLOW` (equivalent to allowlist), and other fields will be used for future ACLs compatible with open-source Kafka"
      },
      {
        "name": "Host",
        "desc": "The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this"
      },
      {
        "name": "Principal",
        "desc": "User list. The default value is `*`, which means that any user can access. The current user can only be one included in the user list"
      }
    ],
    "desc": "This API is used to delete an ACL."
  },
  "DescribeAppInfo": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset position"
      },
      {
        "name": "Limit",
        "desc": "Maximum number of users to be queried in this request. Maximum value: 50. Default value: 50"
      }
    ],
    "desc": "This API is used to query the user list."
  },
  "DescribeGroupOffsets": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "(Filter) filter by instance ID"
      },
      {
        "name": "Group",
        "desc": "Kafka consumer group"
      },
      {
        "name": "Topics",
        "desc": "Array of the names of topics subscribed to by a group. If there is no such array, this parameter means the information of all topics in the specified group"
      },
      {
        "name": "SearchWord",
        "desc": "Fuzzy match by `topicName`"
      },
      {
        "name": "Offset",
        "desc": "Offset position of this query. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Maximum number of results to be returned in this request. Default value: 50. Maximum value: 50"
      }
    ],
    "desc": "This API is used to get the consumer group offset."
  },
  "DescribeInstanceAttributes": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to get instance attributes."
  },
  "DescribeInstancesDetail": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "(Filter) filter by instance ID"
      },
      {
        "name": "SearchWord",
        "desc": "(Filter) filter by instance name. Fuzzy search is supported"
      },
      {
        "name": "Status",
        "desc": "(Filter) instance status. 0: creating, 1: running, 2: deleting. If this parameter is left empty, all instances will be returned by default"
      },
      {
        "name": "Offset",
        "desc": "Offset. If this parameter is left empty, 0 will be used by default"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20"
      },
      {
        "name": "TagKey",
        "desc": "Tag key match."
      },
      {
        "name": "Filters",
        "desc": "Filter"
      }
    ],
    "desc": "This API is used to get instance list details under a user account."
  },
  "DeleteUser": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Name",
        "desc": "Username"
      }
    ],
    "desc": "This API is used to delete a user."
  },
  "DescribeTopicAttributes": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "TopicName",
        "desc": "Topic name"
      }
    ],
    "desc": "This API is used to get topic attributes.\n"
  },
  "DescribeTopic": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "SearchWord",
        "desc": "Filter by `topicName`. Fuzzy search is supported"
      },
      {
        "name": "Offset",
        "desc": "Offset. If this parameter is left empty, 0 will be used by default"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20"
      }
    ],
    "desc": "API domain name: https://ckafka.tencentcloudapi.com\nThis API is used to get the list of topics in a CKafka instance of a user."
  },
  "CreateUser": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      },
      {
        "name": "Name",
        "desc": "Username"
      },
      {
        "name": "Password",
        "desc": "User password"
      }
    ],
    "desc": "This API is used to add a user."
  },
  "DeleteTopic": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "CKafka instance ID"
      },
      {
        "name": "TopicName",
        "desc": "CKafka topic name"
      }
    ],
    "desc": "This API is used to delete a CKafka topic."
  }
}