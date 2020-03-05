# -*- coding: utf-8 -*-
DESC = "cloudaudit-2019-03-19"
INFO = {
  "StartLogging": {
    "params": [
      {
        "name": "AuditName",
        "desc": "Tracking set name"
      }
    ],
    "desc": "This API is used to enable a tracking set."
  },
  "GetAttributeKey": {
    "params": [
      {
        "name": "WebsiteType",
        "desc": "Website type. Value range: zh, en. Default value: zh"
      }
    ],
    "desc": "This API is used to query the value range of AttributeKey."
  },
  "ListCmqEnableRegion": {
    "params": [
      {
        "name": "WebsiteType",
        "desc": "Website type. zh: Mainland China (default); en: outside Mainland China."
      }
    ],
    "desc": "This API is used to query the CloudAudit-enabled CMQ AZs."
  },
  "DeleteAudit": {
    "params": [
      {
        "name": "AuditName",
        "desc": "Tracking set name"
      }
    ],
    "desc": "This API is used to delete a tracking set."
  },
  "StopLogging": {
    "params": [
      {
        "name": "AuditName",
        "desc": "Tracking set name"
      }
    ],
    "desc": "This API is used to disable a tracking set."
  },
  "InquireAuditCredit": {
    "params": [],
    "desc": "This API is used to query the maximum number of tracking sets that can be created."
  },
  "UpdateAudit": {
    "params": [
      {
        "name": "AuditName",
        "desc": "Tracking set name"
      },
      {
        "name": "CmqQueueName",
        "desc": "Queue name, which must begin with a letter and can contain up to 64 letters, digits, and dashes (-). This field is required if the value of IsEnableCmqNotify is 1. If a queue is not newly created, CloudAudit will not verify whether it actually exists. Please enter the name with caution so as to avoid log delivery failure and consequent data loss."
      },
      {
        "name": "CmqRegion",
        "desc": "Region where the queue is located. Supported CMQ regions can be queried using the ListCmqEnableRegion API. This field is required if the value of IsEnableCmqNotify is 1."
      },
      {
        "name": "CosBucketName",
        "desc": "User-defined COS bucket name, which can only contain 1-40 lowercase letters (a-z), digits (0-9), and dashes (-) and cannot begin or end with \"-\". If a bucket is not newly created, CloudAudit will not verify whether it actually exists. Please enter the name with caution so as to avoid log delivery failure and consequent data loss."
      },
      {
        "name": "CosRegion",
        "desc": "COS region. Supported regions can be queried using the ListCosEnableRegion API."
      },
      {
        "name": "IsCreateNewBucket",
        "desc": "Whether to create a COS bucket. 1: yes; 0: no."
      },
      {
        "name": "IsCreateNewQueue",
        "desc": "Whether to create a queue. 1: yes; 0: no. This field is required if the value of IsEnableCmqNotify is 1."
      },
      {
        "name": "IsEnableCmqNotify",
        "desc": "Whether to enable CMQ message notification. 1: yes; 0: no. Only CMQ queue service is currently supported. If CMQ message notification is enabled, CloudAudit will deliver your log contents to the designated queue in the specified region in real time."
      },
      {
        "name": "LogFilePrefix",
        "desc": "Prefix of a log file, which can only contain 3-40 ASCII letters (a-z; A-Z) and digits (0-9)."
      },
      {
        "name": "ReadWriteAttribute",
        "desc": "Manages the read/write attribute of an event. Value range: 1 (read-only), 2 (write-only), 3 (read/write)."
      }
    ],
    "desc": "Parameter requirements:\n1. If the value of IsCreateNewBucket exists, cosRegion and cosBucketName are required.\n2. If the value of IsEnableCmqNotify is 1, IsCreateNewQueue, CmqRegion, and CmqQueueName are required.\n3. If the value of IsEnableCmqNotify is 0, IsCreateNewQueue, CmqRegion, and CmqQueueName cannot be passed in."
  },
  "DescribeAudit": {
    "params": [
      {
        "name": "AuditName",
        "desc": "Tracking set name"
      }
    ],
    "desc": "This API is used to query the details of a tracking set."
  },
  "CreateAudit": {
    "params": [
      {
        "name": "AuditName",
        "desc": "Tracking set name, which can contain 3-128 ASCII letters (a-z; A-Z), digits (0-9), and underscores (_)."
      },
      {
        "name": "CosBucketName",
        "desc": "User-defined COS bucket name, which can only contain 1-40 lowercase letters (a-z), digits (0-9), and dashes (-) and cannot begin or end with \"-\". If a bucket is not newly created, CloudAudit will not verify whether it actually exists. Please enter the name with caution so as to avoid log delivery failure and consequent data loss."
      },
      {
        "name": "CosRegion",
        "desc": "COS region. Supported regions can be queried using the ListCosEnableRegion API."
      },
      {
        "name": "IsCreateNewBucket",
        "desc": "Whether to create a COS bucket. 1: yes; 0: no."
      },
      {
        "name": "IsEnableCmqNotify",
        "desc": "Whether to enable CMQ message notification. 1: yes; 0: no. Only CMQ queue service is currently supported. If CMQ message notification is enabled, CloudAudit will deliver your log contents to the designated queue in the specified region in real time."
      },
      {
        "name": "ReadWriteAttribute",
        "desc": "Manages the read/write attribute of an event. Value range: 1 (read-only), 2 (write-only), 3 (read/write)."
      },
      {
        "name": "CmqQueueName",
        "desc": "Queue name, which must begin with a letter and can contain up to 64 letters, digits, and dashes (-). This field is required if the value of IsEnableCmqNotify is 1. If a queue is not newly created, CloudAudit will not verify whether it actually exists. Please enter the name with caution so as to avoid log delivery failure and consequent data loss."
      },
      {
        "name": "CmqRegion",
        "desc": "Region where the queue is located. Supported CMQ regions can be queried using the ListCmqEnableRegion API. This field is required if the value of IsEnableCmqNotify is 1."
      },
      {
        "name": "IsCreateNewQueue",
        "desc": "Whether to create a queue. 1: yes; 0: no. This field is required if the value of IsEnableCmqNotify is 1."
      },
      {
        "name": "LogFilePrefix",
        "desc": "Prefix of a log file, which can only contain 3-40 ASCII letters (a-z; A-Z) and digits (0-9). It can be left empty and is the account ID by default."
      }
    ],
    "desc": "This API is used to create a tracking set."
  },
  "ListCosEnableRegion": {
    "params": [
      {
        "name": "WebsiteType",
        "desc": "Website type. zh: Mainland China (default); en: outside Mainland China."
      }
    ],
    "desc": "This API is used to query the CloudAudit-enabled COS AZs."
  },
  "LookUpEvents": {
    "params": [
      {
        "name": "EndTime",
        "desc": "End time"
      },
      {
        "name": "StartTime",
        "desc": "Start time"
      },
      {
        "name": "LookupAttributes",
        "desc": "Search criteria"
      },
      {
        "name": "MaxResults",
        "desc": "Maximum number of logs that can be returned"
      },
      {
        "name": "NextToken",
        "desc": "Credential for viewing more logs"
      }
    ],
    "desc": "This API is used to search for operation logs to help query relevant operation information."
  },
  "ListAudits": {
    "params": [],
    "desc": "This API is used to query the summary of tracking sets."
  }
}