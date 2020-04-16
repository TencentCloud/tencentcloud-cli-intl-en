# -*- coding: utf-8 -*-
DESC = "tag-2018-08-13"
INFO = {
  "DescribeResourceTagsByTagKeys": {
    "params": [
      {
        "name": "ServiceType",
        "desc": "Service type"
      },
      {
        "name": "ResourcePrefix",
        "desc": "Resource prefix"
      },
      {
        "name": "ResourceRegion",
        "desc": "Resource region"
      },
      {
        "name": "ResourceIds",
        "desc": "Unique resource ID"
      },
      {
        "name": "TagKeys",
        "desc": "Resource tag key"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Default value: 400"
      },
      {
        "name": "Offset",
        "desc": "Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter"
      }
    ],
    "desc": "This API is used to get resource tags based on tag keys."
  },
  "UpdateResourceTagValue": {
    "params": [
      {
        "name": "TagKey",
        "desc": "Tag key associated with the resource."
      },
      {
        "name": "TagValue",
        "desc": "Modified tag value."
      },
      {
        "name": "Resource",
        "desc": "Resource description in six-piece format."
      }
    ],
    "desc": "This API is used to modify the values of tags associated with a resource (the tag key does not change)."
  },
  "DescribeTagValues": {
    "params": [
      {
        "name": "TagKeys",
        "desc": "Tag key list."
      },
      {
        "name": "CreateUin",
        "desc": "Creator `Uin`. If not specified, `Uin` is only used as the query condition."
      },
      {
        "name": "Offset",
        "desc": "Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter."
      },
      {
        "name": "Limit",
        "desc": "Page size. The default value is 0."
      }
    ],
    "desc": "This API is used to query tag values in an existing tag list."
  },
  "DescribeResourceTagsByResourceIds": {
    "params": [
      {
        "name": "ServiceType",
        "desc": "Service type."
      },
      {
        "name": "ResourcePrefix",
        "desc": "Resource prefix."
      },
      {
        "name": "ResourceIds",
        "desc": "Unique resource ID."
      },
      {
        "name": "ResourceRegion",
        "desc": "The resource’s region."
      },
      {
        "name": "Offset",
        "desc": "Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter."
      },
      {
        "name": "Limit",
        "desc": "Page size. The default value is 0."
      }
    ],
    "desc": "This API is used to query tag key and value pairs for existing resources."
  },
  "AddResourceTag": {
    "params": [
      {
        "name": "TagKey",
        "desc": "Tag key."
      },
      {
        "name": "TagValue",
        "desc": "Tag value."
      },
      {
        "name": "Resource",
        "desc": "Resource description in six-piece format."
      }
    ],
    "desc": "This API is used to associate resources with tags."
  },
  "DeleteResourceTag": {
    "params": [
      {
        "name": "TagKey",
        "desc": "Tag key."
      },
      {
        "name": "Resource",
        "desc": "Resource description in six-piece format."
      }
    ],
    "desc": "This API is used to unassociate tags and resources."
  },
  "CreateTag": {
    "params": [
      {
        "name": "TagKey",
        "desc": "Tag key."
      },
      {
        "name": "TagValue",
        "desc": "Tag value."
      }
    ],
    "desc": "This API is used to create a tag key and tag value pair."
  },
  "DescribeTags": {
    "params": [
      {
        "name": "TagKey",
        "desc": "Tag key. Either exists or does not exist alongside the tag value. If it does not exist, all of the user’s tags will be queried."
      },
      {
        "name": "TagValue",
        "desc": "Tag value. Either exists or does not exist alongside the tag key. If it does not exist, all of the user’s tags will be queried."
      },
      {
        "name": "Offset",
        "desc": "Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter."
      },
      {
        "name": "Limit",
        "desc": "Page size. The default value is 0."
      },
      {
        "name": "CreateUin",
        "desc": "Creator `Uin`. If not specified, `Uin` is only used as the query condition."
      },
      {
        "name": "TagKeys",
        "desc": "Tag key array, which either exists or does not exist with the tag value. If it does not exist, all tags of the user will be queried. If it is passed in together with `TagKey`, it will be used and the `TagKey` will be ignored"
      },
      {
        "name": "ShowProject",
        "desc": "Whether to show project tag"
      }
    ],
    "desc": "This API is used to query existing tag lists.\n"
  },
  "ModifyResourceTags": {
    "params": [
      {
        "name": "Resource",
        "desc": "Resource description in six-piece format."
      },
      {
        "name": "ReplaceTags",
        "desc": "The tags to be added or modified. If the resource described by `Resource` is not associated with the input tag keys, an association will be added. If the tag keys are already associated, the values corresponding to the associated tag keys will be modified to the input values. This API must contain either `ReplaceTags` or `DeleteTag`. And these two parameters cannot include the same tag keys."
      },
      {
        "name": "DeleteTags",
        "desc": "The tags to be unassociated. This API must contain either `ReplaceTags` or `DeleteTag`. And these two parameters cannot include the same tag keys."
      }
    ],
    "desc": "This API is used to modify all tags associated with a resource."
  },
  "DescribeResourcesByTags": {
    "params": [
      {
        "name": "TagFilters",
        "desc": "Tag filtering arrays."
      },
      {
        "name": "CreateUin",
        "desc": "Tag creator uin."
      },
      {
        "name": "Offset",
        "desc": "Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter."
      },
      {
        "name": "Limit",
        "desc": "Page size. The default value is 15."
      },
      {
        "name": "ResourcePrefix",
        "desc": "Resource prefix."
      },
      {
        "name": "ResourceId",
        "desc": "Unique resource ID."
      },
      {
        "name": "ResourceRegion",
        "desc": "The resource’s region."
      },
      {
        "name": "ServiceType",
        "desc": "Service type."
      }
    ],
    "desc": "This API is used to query resources by tags."
  },
  "DescribeTagKeys": {
    "params": [
      {
        "name": "CreateUin",
        "desc": "Creator `Uin`. If not specified, `Uin` is only used as the query condition."
      },
      {
        "name": "Offset",
        "desc": "Data offset. The default value is 0. Must be an integral multiple of the `Limit` parameter."
      },
      {
        "name": "Limit",
        "desc": "Page size. The default value is 0."
      },
      {
        "name": "ShowProject",
        "desc": "Whether to show project"
      }
    ],
    "desc": "This API is used to query tag keys in an existing tag list.\n"
  },
  "DeleteTag": {
    "params": [
      {
        "name": "TagKey",
        "desc": "The tag key to be deleted."
      },
      {
        "name": "TagValue",
        "desc": "The tag value to be deleted."
      }
    ],
    "desc": "This API is used to delete a tag key and tag value pair."
  }
}