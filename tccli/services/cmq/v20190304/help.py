# -*- coding: utf-8 -*-
DESC = "cmq-2019-03-04"
INFO = {
  "CreateTopic": {
    "params": [
      {
        "name": "TopicName",
        "desc": "Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "MaxMsgSize",
        "desc": "Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536."
      },
      {
        "name": "FilterType",
        "desc": "Message match policy for a specified topic."
      },
      {
        "name": "MsgRetentionSeconds",
        "desc": "Message retention period. Value range: 60–86400 seconds (i.e., 1 minute–1 day). Default value: 86400."
      },
      {
        "name": "Trace",
        "desc": "Whether to enable message trace. true: yes, false: no. If this field is left empty, the feature will not be enabled."
      }
    ],
    "desc": "This API is used to create a topic."
  },
  "CreateSubscribe": {
    "params": [
      {
        "name": "TopicName",
        "desc": "Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "SubscriptionName",
        "desc": "Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "Protocol",
        "desc": "Subscription protocol. Currently, two protocols are supported: http and queue. To use the `http` protocol, you need to build your own web server to receive messages. With the `queue` protocol, messages are automatically pushed to a CMQ queue and you can pull them concurrently."
      },
      {
        "name": "Endpoint",
        "desc": "`Endpoint` for notification receipt, which is distinguished by `Protocol`. For `http`, `Endpoint` must begin with `http://` and `host` can be a domain name or IP. For `Queue`, enter `QueueName`. Please note that currently the push service cannot push messages to a VPC; therefore, if a VPC domain name or address is entered for `Endpoint`, pushed messages will not be received. Currently, messages can be pushed only to the public network and basic network."
      },
      {
        "name": "NotifyStrategy",
        "desc": "CMQ push server retry policy in case an error occurs while pushing a message to `Endpoint`. Valid values: 1. BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message; 2. EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY."
      },
      {
        "name": "FilterTag",
        "desc": "Message body tag (used for message filtering). The number of tags cannot exceed 5, and each tag can contain up to 16 characters. It is used in conjunction with the `MsgTag` parameter of `(Batch)PublishMessage`. Rules: 1. If `FilterTag` is not set, no matter whether `MsgTag` is set, the subscription will receive all messages published to the topic; 2. If the `FilterTag` array has a value, only when at least one of the values in the array also exists in the `MsgTag` array (i.e., `FilterTag` and `MsgTag` have an intersection) can the subscription receive messages published to the topic; 3. If the `FilterTag` array has a value, but `MsgTag` is not set, then no message published to the topic will be received, which can be considered as a special case of rule 2 as `FilterTag` and `MsgTag` do not intersect in this case. The overall design idea of rules is based on the intention of the subscriber."
      },
      {
        "name": "BindingKey",
        "desc": "The number of `BindingKey` cannot exceed 5, and the length of each `BindingKey` cannot exceed 64 bytes. This field indicates the filtering policy for subscribing to and receiving messages. Each `BindingKey` can contain up to 15 `.`, i.e., up to 16 phrases."
      },
      {
        "name": "NotifyContentFormat",
        "desc": "Push content format. Valid values: 1. JSON, 2. SIMPLIFIED, i.e., the raw format. If `Protocol` is `queue`, this value must be `SIMPLIFIED`. If `Protocol` is `http`, both options are acceptable, and the default value is `JSON`."
      }
    ],
    "desc": "This API is used to create a subscription."
  },
  "ModifyTopicAttribute": {
    "params": [
      {
        "name": "TopicName",
        "desc": "Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "MaxMsgSize",
        "desc": "Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536."
      },
      {
        "name": "MsgRetentionSeconds",
        "desc": "Message retention period. Value range: 60–86400 seconds (i.e., 1 minute–1 day). Default value: 86400."
      },
      {
        "name": "Trace",
        "desc": "Whether to enable message trace. true: yes, false: no. If this field is left empty, the feature will not be enabled."
      }
    ],
    "desc": "This API is used to modify topic attributes."
  },
  "ClearSubscriptionFilterTags": {
    "params": [
      {
        "name": "TopicName",
        "desc": "Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "SubscriptionName",
        "desc": "Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      }
    ],
    "desc": "This API is used to clear the message tags of a subscriber."
  },
  "DeleteSubscribe": {
    "params": [
      {
        "name": "TopicName",
        "desc": "Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "SubscriptionName",
        "desc": "Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      }
    ],
    "desc": "This API is used to delete a subscription."
  },
  "CreateQueue": {
    "params": [
      {
        "name": "QueueName",
        "desc": "Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "MaxMsgHeapNum",
        "desc": "Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released."
      },
      {
        "name": "PollingWaitSeconds",
        "desc": "Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0."
      },
      {
        "name": "VisibilityTimeout",
        "desc": "Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30."
      },
      {
        "name": "MaxMsgSize",
        "desc": "Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536."
      },
      {
        "name": "MsgRetentionSeconds",
        "desc": "Message retention period. Value range: 60–1296000 seconds (i.e., 1 minute–15 days). Default value: 345600 (i.e., 4 days)."
      },
      {
        "name": "RewindSeconds",
        "desc": "Whether to enable the message rewinding feature for a queue. Value range: 0–msgRetentionSeconds, where 0 means not to enable this feature, while `msgRetentionSeconds` indicates that the maximum rewindable period is the message retention period of the queue."
      },
      {
        "name": "Transaction",
        "desc": "1: transaction queue, 0: general queue"
      },
      {
        "name": "FirstQueryInterval",
        "desc": "First lookback interval"
      },
      {
        "name": "MaxQueryCount",
        "desc": "Maximum number of lookbacks"
      },
      {
        "name": "DeadLetterQueueName",
        "desc": "Dead letter queue name"
      },
      {
        "name": "Policy",
        "desc": "Dead letter policy. 0: message has been consumed multiple times but not deleted, 1: `Time-To-Live` has elapsed"
      },
      {
        "name": "MaxReceiveCount",
        "desc": "Maximum receipt times. Value range: 1–1000"
      },
      {
        "name": "MaxTimeToLive",
        "desc": "Maximum period in seconds before an unconsumed message expires, which is required if `policy` is 1. Value range: 300–43200. This value should be smaller than `msgRetentionSeconds` (maximum message retention period)"
      },
      {
        "name": "Trace",
        "desc": "Whether to enable message trace. true: yes, false: no. If this field is not set, the feature will not be enabled"
      }
    ],
    "desc": "This API is used to create a queue.\n"
  },
  "RewindQueue": {
    "params": [
      {
        "name": "QueueName",
        "desc": "Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "StartConsumeTime",
        "desc": "After this time is set, the `(Batch)receiveMessage` API will consume the messages received after this timestamp in the order in which they are produced."
      }
    ],
    "desc": "This API is used to rewind a queue."
  },
  "ModifySubscriptionAttribute": {
    "params": [
      {
        "name": "TopicName",
        "desc": "Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "SubscriptionName",
        "desc": "Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "NotifyStrategy",
        "desc": "CMQ push server retry policy in case an error occurs while pushing a message to `Endpoint`. Valid values:\n1. BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message.\n2. EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY."
      },
      {
        "name": "NotifyContentFormat",
        "desc": "Push content format. Valid values: 1. JSON, 2. SIMPLIFIED, i.e., the raw format. If `Protocol` is `queue`, this value must be `SIMPLIFIED`. If `Protocol` is `HTTP`, both options are acceptable, and the default value is `JSON`."
      },
      {
        "name": "FilterTags",
        "desc": "Message body tag (used for message filtering). The number of tags cannot exceed 5, and each tag can contain up to 16 characters. It is used in conjunction with the `MsgTag` parameter of `(Batch)PublishMessage`. Rules: 1. If `FilterTag` is not set, no matter whether `MsgTag` is set, the subscription will receive all messages published to the topic; 2. If the `FilterTag` array has a value, only when at least one of the values in the array also exists in the `MsgTag` array (i.e., `FilterTag` and `MsgTag` have an intersection) can the subscription receive messages published to the topic; 3. If the `FilterTag` array has a value, but `MsgTag` is not set, then no message published to the topic will be received, which can be considered as a special case of rule 2 as `FilterTag` and `MsgTag` do not intersect in this case. The overall design idea of rules is based on the intention of the subscriber."
      },
      {
        "name": "BindingKey",
        "desc": "The number of `BindingKey` cannot exceed 5, and the length of each `BindingKey` cannot exceed 64 bytes. This field indicates the filtering policy for subscribing to and receiving messages. Each `BindingKey` can contain up to 15 `.`, i.e., up to 16 phrases."
      }
    ],
    "desc": "This API is used to modify subscription attributes."
  },
  "DescribeQueueDetail": {
    "params": [
      {
        "name": "Offset",
        "desc": "Starting position of queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default"
      },
      {
        "name": "Limit",
        "desc": "Number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50."
      },
      {
        "name": "Filters",
        "desc": "Filter parameter. Currently, filtering by `QueueName` is supported, and only one keyword is allowed"
      },
      {
        "name": "TagKey",
        "desc": "Tag search"
      },
      {
        "name": "QueueName",
        "desc": "Exact match by `QueueName`"
      }
    ],
    "desc": "This API is used to enumerate queues."
  },
  "DeleteQueue": {
    "params": [
      {
        "name": "QueueName",
        "desc": "Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      }
    ],
    "desc": "This API is used to delete a queue."
  },
  "UnbindDeadLetter": {
    "params": [
      {
        "name": "QueueName",
        "desc": "Source queue name of dead letter policy. Calling this API will clear the dead letter queue policy of this queue."
      }
    ],
    "desc": "This API is used to unbind a dead letter queue."
  },
  "DeleteTopic": {
    "params": [
      {
        "name": "TopicName",
        "desc": "Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      }
    ],
    "desc": "This API is used to delete a topic."
  },
  "DescribeTopicDetail": {
    "params": [
      {
        "name": "Offset",
        "desc": "Starting position of queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default."
      },
      {
        "name": "Limit",
        "desc": "Number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50."
      },
      {
        "name": "Filters",
        "desc": "Currently, only filtering by `TopicName` is supported, and only one filter value can be entered"
      },
      {
        "name": "TagKey",
        "desc": "Tag match"
      },
      {
        "name": "TopicName",
        "desc": "Exact match by `TopicName`"
      }
    ],
    "desc": "This API is used to query topic details."
  },
  "DescribeSubscriptionDetail": {
    "params": [
      {
        "name": "TopicName",
        "desc": "Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "Offset",
        "desc": "Starting position of topic list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default"
      },
      {
        "name": "Limit",
        "desc": "Number of topics to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50."
      },
      {
        "name": "Filters",
        "desc": "Filter parameter. Currently, only filtering by `SubscriptionName` is supported, and only one keyword is allowed."
      }
    ],
    "desc": "This API is used to query subscription details."
  },
  "DescribeDeadLetterSourceQueues": {
    "params": [
      {
        "name": "DeadLetterQueueName",
        "desc": "Dead letter queue name"
      },
      {
        "name": "Limit",
        "desc": "Starting position of topic list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default."
      },
      {
        "name": "Offset",
        "desc": "Number of topics to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50."
      },
      {
        "name": "Filters",
        "desc": "Filters source queue name of dead letter queue. Currently, only filtering by `SourceQueueName` is supported"
      }
    ],
    "desc": "This API is used to enumerate the source queues of a dead letter queue."
  },
  "ClearQueue": {
    "params": [
      {
        "name": "QueueName",
        "desc": "Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      }
    ],
    "desc": "This API is used to clear all messages in a queue."
  },
  "ModifyQueueAttribute": {
    "params": [
      {
        "name": "QueueName",
        "desc": "Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)."
      },
      {
        "name": "MaxMsgHeapNum",
        "desc": "Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released."
      },
      {
        "name": "PollingWaitSeconds",
        "desc": "Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0."
      },
      {
        "name": "VisibilityTimeout",
        "desc": "Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30."
      },
      {
        "name": "MaxMsgSize",
        "desc": "Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536."
      },
      {
        "name": "MsgRetentionSeconds",
        "desc": "Message retention period. Value range: 60–1296000 seconds (i.e., 1 minute–15 days). Default value: 345600 (i.e., 4 days)."
      },
      {
        "name": "RewindSeconds",
        "desc": "Maximum message rewindable period. Value range: 0–msgRetentionSeconds (maximum message retention period of a queue). 0 means not to enable message rewinding."
      },
      {
        "name": "FirstQueryInterval",
        "desc": "First query time"
      },
      {
        "name": "MaxQueryCount",
        "desc": "Maximum number of queries"
      },
      {
        "name": "DeadLetterQueueName",
        "desc": "Dead letter queue name"
      },
      {
        "name": "MaxTimeToLive",
        "desc": "Maximum period in seconds before an unconsumed message expires, which is required if `MaxTimeToLivepolicy` is 1. Value range: 300–43200. This value should be smaller than `MsgRetentionSeconds` (maximum message retention period)"
      },
      {
        "name": "MaxReceiveCount",
        "desc": "Maximum number of receipts"
      },
      {
        "name": "Policy",
        "desc": "Dead letter queue policy"
      },
      {
        "name": "Trace",
        "desc": "Whether to enable message trace. true: yes, false: no. If this field is left empty, the feature will not be enabled."
      }
    ],
    "desc": "This API is used to modify queue attributes."
  }
}