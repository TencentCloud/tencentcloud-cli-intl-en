# -*- coding: utf-8 -*-
DESC = "scf-2018-04-16"
INFO = {
  "CreateFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Name of the new function. The name can contain 2 to 60 characters, including English letters, digits, hyphens (-), and underscores (_). The name must start with a letter and cannot end with a hyphen or underscore."
      },
      {
        "name": "Code",
        "desc": "Function code. Note: You cannot specify `Cos` and `ZipFile` at the same time."
      },
      {
        "name": "Handler",
        "desc": "Name of the handler, which is in the “file name.handler name” form. Use periods (.) to separate a file name and function name. The file name and function name must start and end with a letter and can contain 2 to 60 characters, including letters, digits, hyphens (-), and underscores (_)."
      },
      {
        "name": "Description",
        "desc": "Function description. It can contain up to 1,000 characters including letters, digits, spaces, commas (,), periods (.), and Chinese characters."
      },
      {
        "name": "MemorySize",
        "desc": "Memory size of a running function. The value ranges from 128 MB (default) to 1,536 MB with a granularity of 128 MB."
      },
      {
        "name": "Timeout",
        "desc": "The longest function running time. The unit is second (s). The value ranges from 1 to 300 seconds. The default value is 3 seconds."
      },
      {
        "name": "Environment",
        "desc": "Function environment variable"
      },
      {
        "name": "Runtime",
        "desc": "Function running environment. Currently, only Python 2.7 (default), Python 3.6, Nodejs 6.10, PHP 5, PHP 7, Golang 1, and Java 8 are supported."
      },
      {
        "name": "VpcConfig",
        "desc": "Function VPC configuration"
      },
      {
        "name": "Namespace",
        "desc": "Function namespace"
      },
      {
        "name": "Role",
        "desc": "Role bound to the function"
      },
      {
        "name": "ClsLogsetId",
        "desc": "CLS Logset ID to which the function logs are shipped"
      },
      {
        "name": "ClsTopicId",
        "desc": "CLS Topic ID to which the function logs are shipped"
      },
      {
        "name": "Type",
        "desc": "Function type. The default value is `Event`. Enter `Event` if you need to create a trigger function. Enter `HTTP` if you need to create an HTTP function service."
      },
      {
        "name": "CodeSource",
        "desc": "Code source, including ZipFile, Cos, Demo, TempCos, and Git. This field is required if the source is Git."
      },
      {
        "name": "Layers",
        "desc": "List of layer versions to be associate with the function. Layers will be overwritten sequentially in the order in the list."
      },
      {
        "name": "DeadLetterConfig",
        "desc": "Dead letter queue parameter"
      }
    ],
    "desc": "This API is used to create a function based on the input parameters."
  },
  "ListVersionByFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Function ID"
      },
      {
        "name": "Namespace",
        "desc": "Namespace"
      }
    ],
    "desc": "This API is used to query the function version based on the input parameters."
  },
  "UpdateNamespace": {
    "params": [
      {
        "name": "Namespace",
        "desc": "Namespace name"
      },
      {
        "name": "Description",
        "desc": "Namespace description"
      }
    ],
    "desc": "This API is used to update a namespace."
  },
  "Invoke": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Function name"
      },
      {
        "name": "InvocationType",
        "desc": "The value is `RequestResponse` (synchronous) or `Event` (asynchronous). The default value is synchronous."
      },
      {
        "name": "Qualifier",
        "desc": "Version number of the triggered function"
      },
      {
        "name": "ClientContext",
        "desc": "Function running parameter, which is in the JSON format. Maximum parameter size is 1 MB."
      },
      {
        "name": "LogType",
        "desc": "If this field is specified for a synchronous invocation, the return value will contain a 4-KB log. The value is `None` (default) or `Tail`. If the value is `Tail`, `logMsg` in the return parameter will contain the corresponding function execution log."
      },
      {
        "name": "Namespace",
        "desc": "Namespace"
      }
    ],
    "desc": "This API is used to run a function."
  },
  "DeleteFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Name of the function to be deleted"
      },
      {
        "name": "Namespace",
        "desc": "Function namespace"
      }
    ],
    "desc": "This API is used to delete a function based on the input parameters."
  },
  "PublishVersion": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Name of the released function"
      },
      {
        "name": "Description",
        "desc": "Function description"
      },
      {
        "name": "Namespace",
        "desc": "Function namespace"
      }
    ],
    "desc": "This API is used for users to release a new version of the function."
  },
  "ListNamespaces": {
    "params": [
      {
        "name": "Limit",
        "desc": "Return data length. The default value is `20`."
      },
      {
        "name": "Offset",
        "desc": "Data offset. The default value is `0`."
      },
      {
        "name": "Orderby",
        "desc": "It specifies the sorting order of the results according to a specified field, such as `Name` and `Updatetime`."
      },
      {
        "name": "Order",
        "desc": "It specifies whether to return the results in ascending or descending order. The value is `ASC` or `DESC`."
      }
    ],
    "desc": "This API is used to display a namespace list."
  },
  "GetFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Name of the function to obtain details"
      },
      {
        "name": "Qualifier",
        "desc": "Function version number"
      },
      {
        "name": "Namespace",
        "desc": "Function namespace"
      },
      {
        "name": "ShowCode",
        "desc": "It indicates whether to display the code. `TRUE` means displaying the code, and `FALSE` means hiding the code. The code will not be displayed for entry files exceeding 1 MB."
      }
    ],
    "desc": "This API is used to obtain function details, such as name, code, handler, associated trigger, and timeout."
  },
  "GetFunctionAddress": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Function name"
      },
      {
        "name": "Qualifier",
        "desc": "Function version"
      },
      {
        "name": "Namespace",
        "desc": "Function namespace"
      }
    ],
    "desc": "This API is used to obtain the download address of the function code package."
  },
  "DeleteNamespace": {
    "params": [
      {
        "name": "Namespace",
        "desc": "Namespace name"
      }
    ],
    "desc": "This API is used to create a namespace based on the input parameters."
  },
  "CreateTrigger": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Name of the function bound to the new trigger"
      },
      {
        "name": "TriggerName",
        "desc": "Name of a new trigger. For a timer trigger, the name can contain up to 100 letters, digits, dashes, and underscores; for a COS trigger, it should be an access domain name of the corresponding COS bucket applicable to the XML API (e.g., 5401-5ff414-12345.cos.ap-shanghai.myqcloud.com); for other triggers, please see the descriptions of parameters bound to the specific trigger."
      },
      {
        "name": "Type",
        "desc": "Trigger type. Currently, COS, CMQ, timer, and ckafka triggers are supported."
      },
      {
        "name": "TriggerDesc",
        "desc": "Parameter corresponding to the trigger. For a timer trigger, it should be a Linux cron expression; for a COS trigger, it should be a JSON string ({\"event\":\"cos:ObjectCreated:*\",\"filter\":{\"Prefix\":\"\",\"Suffix\":\"\"}}), where `event` is the triggered COS event, `Prefix` in the `filter` is the corresponding file prefix filter, and `Suffix` is the corresponding suffix filter, and the `filter` can be left blank if not needed; for other triggers, please see the description of the specific trigger."
      },
      {
        "name": "Namespace",
        "desc": "Function namespace"
      },
      {
        "name": "Qualifier",
        "desc": "Function version"
      },
      {
        "name": "Enable",
        "desc": "Initial enabling status of the trigger. `OPEN` indicates enabled, and `CLOSE` indicates disabled."
      }
    ],
    "desc": "This API is used to create a trigger based on the input parameters."
  },
  "CreateNamespace": {
    "params": [
      {
        "name": "Namespace",
        "desc": "Namespace name"
      },
      {
        "name": "Description",
        "desc": "Namespace description"
      }
    ],
    "desc": "This API is used to create a namespace based on the input parameters."
  },
  "CopyFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Name of the function to be replicated"
      },
      {
        "name": "NewFunctionName",
        "desc": "Name of the new function"
      },
      {
        "name": "Namespace",
        "desc": "Namespace of the function to be replicated. The default value is `default`."
      },
      {
        "name": "TargetNamespace",
        "desc": "Namespace of the replicated function. The default value is default."
      },
      {
        "name": "Description",
        "desc": "Description of the new function"
      },
      {
        "name": "TargetRegion",
        "desc": "Region of the target of the function replication. If the value is not set, the current region is used by default."
      },
      {
        "name": "Override",
        "desc": "It specifies whether to replace the function with the same name in the target namespace. The default option is `FALSE`.\n(Note: The `TRUE` option results in deletion of the function in the target namespace. Please operate with caution.)\nTRUE: Replaces the function.\nFALSE: Does not replace the function."
      },
      {
        "name": "CopyConfiguration",
        "desc": "It specifies whether to replicate the function attributes, including environment variables, memory, timeout, function description, labels, and VPC. The default value is `TRUE`.\nTRUE: Replicates the function configuration.\nFALSE: Does not replicate the function configuration."
      }
    ],
    "desc": "This API is used to replicate a function. You can store the replicated function in a specified Region and Namespace.\nNote: This API **does not** replicate the following objects or attributes of the function:\n1. Function trigger\n2. Versions other than $LATEST\n3. CLS target of the logs configured in the function\n\nYou can manually configure the function after replication as required."
  },
  "UpdateFunctionConfiguration": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Name of the function to be modified"
      },
      {
        "name": "Description",
        "desc": "Function description. It can contain up to 1,000 characters, including letters, digits, spaces, commas (,), periods (.), and Chinese characters."
      },
      {
        "name": "MemorySize",
        "desc": "Memory size when the function is running. The value ranges from 128 MB (default) to 1,536 MB."
      },
      {
        "name": "Timeout",
        "desc": "The longest function running time. The unit is second (s). The value ranges from 1 to 300 seconds. The default value is 3 seconds."
      },
      {
        "name": "Runtime",
        "desc": "Function running environment. Currently, only Python 2.7, Python 3.6, Nodejs 6.10, PHP 5, PHP 7, Golang 1, and Java 8 are supported."
      },
      {
        "name": "Environment",
        "desc": "Function environment variable"
      },
      {
        "name": "Namespace",
        "desc": "Function namespace"
      },
      {
        "name": "VpcConfig",
        "desc": "Function VPC configuration"
      },
      {
        "name": "Role",
        "desc": "Role bound to the function"
      },
      {
        "name": "ClsLogsetId",
        "desc": "CLS logset ID to which logs are shipped"
      },
      {
        "name": "ClsTopicId",
        "desc": "CLS Topic ID to which logs are shipped"
      },
      {
        "name": "Publish",
        "desc": "It specifies whether to synchronously release a new version during the update. The default value is `FALSE`, indicating not to release a new version."
      },
      {
        "name": "L5Enable",
        "desc": "Whether to enable L5 access. TRUE: enable; FALSE: not enable"
      },
      {
        "name": "Layers",
        "desc": "List of layer versions with which a function will be associated. Layers will be overwritten sequentially in the order in the list."
      },
      {
        "name": "DeadLetterConfig",
        "desc": "Information of a dead letter queue associated with a function"
      },
      {
        "name": "OnsEnable",
        "desc": ""
      }
    ],
    "desc": "This API is used to update the function configuration based on the input parameters."
  },
  "ListFunctions": {
    "params": [
      {
        "name": "Order",
        "desc": "It specifies whether to return the results in ascending or descending order. The value is `ASC` or `DESC`."
      },
      {
        "name": "Orderby",
        "desc": "It specifies the sorting order of the results according to a specified field, such as `AddTime`, `ModTime`, and `FunctionName`."
      },
      {
        "name": "Offset",
        "desc": "Data offset. The default value is `0`."
      },
      {
        "name": "Limit",
        "desc": "Return data length. The default value is `20`."
      },
      {
        "name": "SearchKey",
        "desc": "It specifies whether to support fuzzy matching for the function name."
      },
      {
        "name": "Namespace",
        "desc": "Namespace"
      },
      {
        "name": "Description",
        "desc": "Function description. Fuzzy search is supported."
      },
      {
        "name": "Filters",
        "desc": "Filters\n- tag:tag-key - String - Required: No - Filtering criteria based on tag-key - value pairs. Replace `tag-key` with a specific tag-key.\n\nThe maximum number of `Filters` for each request is 10, and that of `Filter.Values` is 5."
      }
    ],
    "desc": "This API is used to return relevant function information based on the input query parameters."
  },
  "DeleteTrigger": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Function name"
      },
      {
        "name": "TriggerName",
        "desc": "Name of the trigger to be deleted"
      },
      {
        "name": "Type",
        "desc": "Type of the trigger to be deleted. Currently, COS, CMQ, timer, and ckafka triggers are supported."
      },
      {
        "name": "Namespace",
        "desc": "Function namespace"
      },
      {
        "name": "TriggerDesc",
        "desc": "This field is required if a COS trigger is to be deleted. It stores the data {\"event\":\"cos:ObjectCreated:*\"} in the JSON format. The data content of this field is in the same format as that of SetTrigger. This field is optional if a scheduled trigger or CMQ trigger is to be deleted."
      },
      {
        "name": "Qualifier",
        "desc": "Function version information"
      }
    ],
    "desc": "This API is used to delete an existing trigger based on the input parameters."
  },
  "GetFunctionLogs": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Function name"
      },
      {
        "name": "Offset",
        "desc": "Data offset. The addition of `Offset` and `Limit` cannot exceed 10,000."
      },
      {
        "name": "Limit",
        "desc": "Length of the return data. The addition of `Offset` and `Limit` cannot exceed 10,000."
      },
      {
        "name": "Order",
        "desc": "It specifies whether to sort the logs in an ascending or descending order. The value is `desc` or `asc`."
      },
      {
        "name": "OrderBy",
        "desc": "It specifies the sorting order of the logs based on a specified field, such as `function_name`, `duration`, `mem_usage`, and `start_time`."
      },
      {
        "name": "Filter",
        "desc": "Log filter used to identify whether to return logs of successful or failed requests. `filter.RetCode=not0` indicates that only the logs of failed requests will be returned. `filter.RetCode=is0` indicates that only the logs of successful requests will be returned. If this parameter is left blank, all logs will be returned. "
      },
      {
        "name": "Namespace",
        "desc": "Function namespace"
      },
      {
        "name": "Qualifier",
        "desc": "Function version"
      },
      {
        "name": "FunctionRequestId",
        "desc": "RequestId corresponding to the executed function"
      },
      {
        "name": "StartTime",
        "desc": "Query date, for example, 2017-05-16 20:00:00. The date must be within one day of the end time."
      },
      {
        "name": "EndTime",
        "desc": "Query date, for example, 2017-05-16 20:59:59. The date must be within one day of the start time."
      },
      {
        "name": "SearchContext",
        "desc": "Service log related parameter. `Offset` on the first page is a null string. Enter other pages based on SearchContext in the response field."
      }
    ],
    "desc": "This API is used to return function running logs according to the specified log query criteria."
  },
  "UpdateFunctionCode": {
    "params": [
      {
        "name": "Handler",
        "desc": "Function handler name, which is in the `file name.function name` form. Use a period (.) to separate a file name and function name. The file name and function name must start and end with letters and contain 2-60 characters, including letters, digits, underscores (_), and hyphens (-)."
      },
      {
        "name": "FunctionName",
        "desc": "Name of the function to be modified"
      },
      {
        "name": "CosBucketName",
        "desc": "COS bucket name"
      },
      {
        "name": "CosObjectName",
        "desc": "COS object path"
      },
      {
        "name": "ZipFile",
        "desc": "It contains a function code file and its dependencies in the ZIP format. When you use this API, the ZIP file needs to be encoded with Base64. Up to 20 MB is supported."
      },
      {
        "name": "Namespace",
        "desc": "Function namespace"
      },
      {
        "name": "CosBucketRegion",
        "desc": "COS region. Note: Beijing includes ap-beijing and ap-beijing-1."
      },
      {
        "name": "EnvId",
        "desc": "Function environment"
      },
      {
        "name": "Publish",
        "desc": "It specifies whether to synchronously release a new version during the update. The default value is `FALSE`, indicating not to release a new version."
      },
      {
        "name": "Code",
        "desc": "Function code"
      },
      {
        "name": "CodeSource",
        "desc": "Source mode of code. Valid values: `ZipFile`, `Cos`, `Inline`, `TempCos` and `Git`. This field must be specified if the source is Git"
      }
    ],
    "desc": "This API is used to update the function code based on the input parameters."
  }
}