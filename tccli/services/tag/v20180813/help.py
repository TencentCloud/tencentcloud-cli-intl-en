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
  "DescribeResourceTagsByResourceIdsSeq": {
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
        "name": "ResourceIds",
        "desc": "Unique resource ID"
      },
      {
        "name": "ResourceRegion",
        "desc": "Resource region"
      },
      {
        "name": "Offset",
        "desc": "Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Default value: 15"
      }
    ],
    "desc": "This API is used to view the tags associated with a resource in sequence."
  },
  "DetachResourcesTag": {
    "params": [
      {
        "name": "ServiceType",
        "desc": "Resource service name"
      },
      {
        "name": "ResourceIds",
        "desc": "Resource ID array, which can contain up to 50 resources"
      },
      {
        "name": "TagKey",
        "desc": "Tag key to be unbound"
      },
      {
        "name": "ResourceRegion",
        "desc": "Resource region. This field is not required for resources that do not have the region attribute"
      },
      {
        "name": "ResourcePrefix",
        "desc": "Resource prefix, which is not required for COS buckets"
      }
    ],
    "desc": "This API is used to unbind a tag from multiple resources."
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
        "desc": "The resource's region."
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
  "DescribeResourceTags": {
    "params": [
      {
        "name": "CreateUin",
        "desc": "Creator `uin`"
      },
      {
        "name": "ResourceRegion",
        "desc": "Resource region."
      },
      {
        "name": "ServiceType",
        "desc": "Service type."
      },
      {
        "name": "ResourcePrefix",
        "desc": "Resource prefix"
      },
      {
        "name": "ResourceId",
        "desc": "Unique resource ID"
      },
      {
        "name": "Offset",
        "desc": "Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Default value: 15"
      },
      {
        "name": "CosResourceId",
        "desc": "Whether it is a COS resource ID"
      }
    ],
    "desc": "This API is used to query the tags associated with a resource."
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
        "desc": "[Six-segment resource description](https://cloud.tencent.com/document/product/598/10606)"
      }
    ],
    "desc": "This API is used to associate resources with tags."
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
        "desc": "[Six-segment resource description](https://cloud.tencent.com/document/product/598/10606)"
      }
    ],
    "desc": "This API is used to modify the values of tags associated with a resource (the tag key does not change)."
  },
  "DeleteResourceTag": {
    "params": [
      {
        "name": "TagKey",
        "desc": "Tag key."
      },
      {
        "name": "Resource",
        "desc": "[Six-segment resource description](https://cloud.tencent.com/document/product/598/10606)"
      }
    ],
    "desc": "This API is used to unassociate tags and resources."
  },
  "DescribeResourcesByTagsUnion": {
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
        "desc": "Service type"
      }
    ],
    "desc": "This API is used to query resource list by tags."
  },
  "DescribeTagValuesSeq": {
    "params": [
      {
        "name": "TagKeys",
        "desc": "Tag key list"
      },
      {
        "name": "CreateUin",
        "desc": "Creator `Uin`. If this parameter is blank or left empty, only `Uin` will be used as a condition for query"
      },
      {
        "name": "Offset",
        "desc": "Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Default value: 15"
      }
    ],
    "desc": "This API is used to query tag values in a created tag list."
  },
  "DescribeTags": {
    "params": [
      {
        "name": "TagKey",
        "desc": "Tag key. Either exists or does not exist alongside the tag value. If it does not exist, all of the user's tags will be queried."
      },
      {
        "name": "TagValue",
        "desc": "Tag value. Either exists or does not exist alongside the tag key. If it does not exist, all of the user's tags will be queried."
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
        "desc": "Tag key array, which either exists or does not exist with the tag value. If it does not exist, all tags of the user will be queried. If it is passed in together with `TagKey`, it will be used and the `TagKey` will be ignored."
      },
      {
        "name": "ShowProject",
        "desc": "Whether to show project tag"
      }
    ],
    "desc": "This API is used to query existing tag lists.\n"
  },
  "DescribeTagsSeq": {
    "params": [
      {
        "name": "TagKey",
        "desc": "Tag key, which either exists or does not exist with the tag value. If it does not exist, all tags of the user will be queried"
      },
      {
        "name": "TagValue",
        "desc": "Tag value, which either exists or does not exist with the tag key. If it does not exist, all tags of the user will be queried"
      },
      {
        "name": "Offset",
        "desc": "Data offset. Default value: 0. It must be an integer multiple of the `Limit` parameter"
      },
      {
        "name": "Limit",
        "desc": "Number of entries per page. Default value: 15"
      },
      {
        "name": "CreateUin",
        "desc": "Creator `Uin`. If this parameter is blank or left empty, only `Uin` will be used as a condition for query"
      },
      {
        "name": "TagKeys",
        "desc": "Tag key array, which either exists or does not exist with the tag value. If it does not exist, all tags of the user will be queried. If it is passed in together with `TagKey`, it will be used and the `TagKey` will be ignored."
      },
      {
        "name": "ShowProject",
        "desc": "Whether to show project tag"
      }
    ],
    "desc": "This API is used to query the created tag lists.\n"
  },
  "ModifyResourceTags": {
    "params": [
      {
        "name": "Resource",
        "desc": "[Six-segment resource description](https://cloud.tencent.com/document/product/598/10606)"
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
        "desc": "The resource's region."
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
  "AttachResourcesTag": {
    "params": [
      {
        "name": "ServiceType",
        "desc": "Resource service name"
      },
      {
        "name": "ResourceIds",
        "desc": "Resource ID array, which can contain up to 50 resources"
      },
      {
        "name": "TagKey",
        "desc": "Tag key"
      },
      {
        "name": "TagValue",
        "desc": "Tag value"
      },
      {
        "name": "ResourceRegion",
        "desc": "Resource region. This field is not required for resources that do not have the region attribute"
      },
      {
        "name": "ResourcePrefix",
        "desc": "Resource prefix, which is not required for COS buckets"
      }
    ],
    "desc": "This API is used to associate a tag with multiple resources."
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
  "ModifyResourcesTagValue": {
    "params": [
      {
        "name": "ServiceType",
        "desc": "Resource service name"
      },
      {
        "name": "ResourceIds",
        "desc": "Resource ID array, which can contain up to 50 resources"
      },
      {
        "name": "TagKey",
        "desc": "Tag key"
      },
      {
        "name": "TagValue",
        "desc": "Tag value"
      },
      {
        "name": "ResourceRegion",
        "desc": "Resource region. This field is not required for resources that do not have the region attribute"
      },
      {
        "name": "ResourcePrefix",
        "desc": "Resource prefix, which is not required for COS buckets"
      }
    ],
    "desc": "This API is used to modify the tag value corresponding to a tag key associated with multiple resources."
  }
}