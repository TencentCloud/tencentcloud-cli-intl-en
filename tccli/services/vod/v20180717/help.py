# -*- coding: utf-8 -*-
DESC = "vod-2018-07-17"
INFO = {
  "CreateSnapshotByTimeOffsetTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Name of a time point screencapturing template. Length limit: 64 characters."
      },
      {
        "name": "Width",
        "desc": "Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "Height",
        "desc": "Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "Resolution adaption. Valid values:\n<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>\n<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>\nDefault value: open."
      },
      {
        "name": "Format",
        "desc": "Image format. Valid values: jpg, png. Default value: jpg."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      },
      {
        "name": "FillType",
        "desc": "Fill type. \"Fill\" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:\n<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot \"shorter\" or \"longer\";</li>\n<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>\n<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>\n<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>\nDefault value: black."
      }
    ],
    "desc": "This API is used to create a custom time point screencapturing template. Up to 16 templates can be created."
  },
  "EditMedia": {
    "params": [
      {
        "name": "InputType",
        "desc": "Input video type. Valid values: File, Stream."
      },
      {
        "name": "FileInfos",
        "desc": "Information of input video file, which is required if `InputType` is `File`."
      },
      {
        "name": "StreamInfos",
        "desc": "Input stream information, which is required if `InputType` is `Stream`."
      },
      {
        "name": "Definition",
        "desc": "Editing template ID. Valid values: 10, 20. If this parameter is left empty, template 10 will be used.\n<li>10: the input with the highest resolution will be used as the benchmark;</li>\n<li>20: the input with the highest bitrate will be used as the benchmark;</li>"
      },
      {
        "name": "ProcedureName",
        "desc": "[Task flow template](/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF) name, which should be entered if you want to perform a task flow on the generated new video."
      },
      {
        "name": "OutputConfig",
        "desc": "Configuration of file generated after editing."
      },
      {
        "name": "SessionContext",
        "desc": "Identifies the source context which is used to pass through the user request information. The `EditMediaComplete` callback and task flow status change callback will return the value of this field. It can contain up to 1,000 characters."
      },
      {
        "name": "TasksPriority",
        "desc": "Task priority. The higher the value, the higher the priority. Value range: -10-10. If this parameter is left empty, 0 will be used."
      },
      {
        "name": "SessionId",
        "desc": "ID used for task deduplication. If there was a request with the same ID in the last day, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or a blank string is entered, no deduplication will be performed."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to edit a video (by clipping, splicing, etc.) to generate a new VOD video. Editing features include:\n\n1. Clipping a file in VOD to generate a new video;\n2. Splicing multiple files in VOD to generate a new video;\n3. Clipping multiple files in VOD and then splicing the clips to generate a new video;\n4. Directly generating a new video from a stream in VOD;\n5. Clipping a stream in VOD to generate a new video;\n6. Splicing multiple streams in VOD to generate a new video;\n7. Clipping multiple streams in VOD and then splicing the clips to generate a new video.\n\nYou can also specify whether to perform a task flow for the generated new video."
  },
  "ApplyUpload": {
    "params": [
      {
        "name": "MediaType",
        "desc": "Media type. For the detailed valid values, please see [Upload Overview](/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)."
      },
      {
        "name": "MediaName",
        "desc": "Media name."
      },
      {
        "name": "CoverType",
        "desc": "Cover type. For the detailed valid values, please see [Upload Overview](/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)."
      },
      {
        "name": "Procedure",
        "desc": "Subsequent task operation on a media file, i.e., after a media file is uploaded, task flow operations will be initiated automatically. This parameter value is a task flow template name. VOD supports [creating task flow templates](/document/product/266/33819) and naming the templates."
      },
      {
        "name": "ExpireTime",
        "desc": "Expiration time of a media file in ISO 8601 format. For more information, please see [Notes on ISO Date Format](/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)."
      },
      {
        "name": "StorageRegion",
        "desc": "Specifies upload region. This is only applicable to users that have special requirements for the upload region."
      },
      {
        "name": "ClassId",
        "desc": "Category ID, which is used to categorize the media for management. A category can be created and its ID can be obtained by using the [category creating](/document/product/266/7812) API.\n<li>Default value: 0, which means \"Other\".</li>"
      },
      {
        "name": "SourceContext",
        "desc": "Source context, which is used to pass through the user request information. The [upload callback](/document/product/266/7830) API will return the value of this field. It can contain up to 250 characters."
      },
      {
        "name": "SessionContext",
        "desc": "Session context, which is used to pass through the user request information. If the `Procedure` parameter is specified, the [task flow status change callback](/document/product/266/9636) API will return the value of this field. It can contain up to 1,000 characters."
      },
      {
        "name": "ExtInfo",
        "desc": ""
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "* This API is used to apply for uploading a media file (and cover file) to VOD and obtain the metadata of file storage (including upload path and upload signature) for subsequent use by the uploading API.\n* For the detailed upload process, please see [Overview of Upload from Client](/document/product/266/9759)."
  },
  "DeleteAnimatedGraphicsTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of an animated image generating template."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete a custom animated image generating template."
  },
  "DescribeAIAnalysisTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of video content analysis templates. Array length limit: 100."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to get the list of video content analysis templates based on unique template ID. The returned result includes all eligible custom and [preset video content analysis templates](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.88.86.E6.9E.90.E6.A8.A1.E6.9D.BF)."
  },
  "PullEvents": {
    "params": [
      {
        "name": "ExtInfo",
        "desc": "Reserved field for special purposes."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "* This API is used to get event notifications from the business server through [reliable callback](https://cloud.tencent.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83);\n* The API is in long polling mode, i.e., if there is an unconsumed event on the server, it will be immediately returned to the requester; otherwise, the backend will suspend the request until a new event is generated;\n* The request can be suspended for 5 seconds at most. It is recommended that the requester set the timeout period to 10 seconds.\n* If the API returns an event, the caller must call the [ConfirmEvents](https://cloud.tencent.com/document/product/266/33434) API within <font color=\"red\">30 seconds</font> to confirm that the event notification has been processed; otherwise, the event notification will be pulled again after <font color=\"red\">30 seconds</font>."
  },
  "ProcessMediaByProcedure": {
    "params": [
      {
        "name": "FileId",
        "desc": "Media file ID."
      },
      {
        "name": "ProcedureName",
        "desc": "[Task flow template](/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF) name."
      },
      {
        "name": "TasksPriority",
        "desc": "Task flow priority. The higher the value, the higher the priority. Value range: -10-10. If this parameter is left empty, 0 will be used."
      },
      {
        "name": "TasksNotifyMode",
        "desc": "Notification mode for task flow status change. Valid values: Finish, Change, None. If this parameter is left empty, `Finish` will be used."
      },
      {
        "name": "SessionContext",
        "desc": "The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters."
      },
      {
        "name": "SessionId",
        "desc": "ID used for deduplication. If there was a request with the same ID on the last day, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or a blank string is entered, no deduplication will be performed."
      },
      {
        "name": "ExtInfo",
        "desc": "Reserved field for special purposes."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to initiate a processing task for a VOD video with a task flow template.\nThere are two ways to create a task flow template:\n1. Create and modify a task flow template in the console;\n2. Create a task flow template through the task flow template API."
  },
  "DeleteTranscodeTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of transcoding template."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete a custom transcoding template."
  },
  "DescribeTaskDetail": {
    "params": [
      {
        "name": "TaskId",
        "desc": "Video processing task ID."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the details of execution status and result of a task submitted in the last 3 days by task ID."
  },
  "DescribeReviewDetails": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start date in [ISO date format](https://cloud.tencent.com/document/product/266/11732#I)."
      },
      {
        "name": "EndTime",
        "desc": "End date in [ISO date format](https://cloud.tencent.com/document/product/266/11732#I). The end date must be after the start date."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the length of audited video content in seconds per day within the specified time range.\n\n1. Statistics on the length of audited video content for the last 365 days can be queried.\n2. The query time range cannot be more than 90 days."
  },
  "DescribeWordSamples": {
    "params": [
      {
        "name": "Usages",
        "desc": "<b>Keyword use case filter. Valid values:</b>\n1. Recognition.Ocr: OCR-based content recognition;\n2. Recognition.Asr: ASR-based content recognition;\n3. Review.Ocr: OCR-based content audit;\n4. Review.Asr: ASR-based content audit;\n<b>These values can be merged as follows:</b>\n5. Recognition: ASR-based and OCR-based content recognition, which is equivalent to 1+2 above;\n6. Review: ASR-based and OCR-based content audit, which is equivalent to 3+4 above;\nMultiple elements can be selected, and the relationship between them is \"OR\", i.e., any keyword use case that contains any element in this field set will be deemed eligible."
      },
      {
        "name": "Keywords",
        "desc": "Keyword filter. Array length limit: 100 words."
      },
      {
        "name": "Tags",
        "desc": "Tag filter. Array length limit: 20 words."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of entries to be returned. Default value: 100. Maximum value: 100."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to perform paginated queries of keyword sample information by use case, keyword, and tag."
  },
  "DescribeStorageData": {
    "params": [
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the storage capacity usage and number of files."
  },
  "ModifyAIAnalysisTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of video content analysis template."
      },
      {
        "name": "Name",
        "desc": "Video content analysis template name. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Video content analysis template description. Length limit: 256 characters."
      },
      {
        "name": "ClassificationConfigure",
        "desc": "Control parameter of intelligent categorization task."
      },
      {
        "name": "TagConfigure",
        "desc": "Control parameter of intelligent tagging task."
      },
      {
        "name": "CoverConfigure",
        "desc": "Control parameter of intelligent cover generating task."
      },
      {
        "name": "FrameTagConfigure",
        "desc": "Control parameter of intelligent frame-specific tagging task."
      },
      {
        "name": "HighlightConfigure",
        "desc": "Control parameter of an intelligent highlight generating task."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify a custom video content analysis template.\n\nNote: templates with an ID below 10000 are preset and cannot be modified."
  },
  "DeleteProcedureTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Task flow name."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete a custom task flow template.  "
  },
  "DeleteAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of adaptive bitrate streaming template."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete an adaptive bitrate streaming template."
  },
  "CreateAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Format",
        "desc": "Adaptive bitstream format. Valid values:\n<li>HLS.</li>"
      },
      {
        "name": "StreamInfos",
        "desc": "Parameter information of output substream for adaptive bitrate streaming. Up to 10 substreams can be output.\nNote: the frame rate of all substreams must be the same; otherwise, the frame rate of the first substream will be used as the output frame rate."
      },
      {
        "name": "Name",
        "desc": "Template name. Length limit: 64 characters."
      },
      {
        "name": "DrmType",
        "desc": "DRM scheme type. Valid values:\n<li>SimpleAES.</li>\nIf this field is an empty string, DRM will not be performed on the video."
      },
      {
        "name": "DisableHigherVideoBitrate",
        "desc": "Whether to prohibit transcoding video from low bitrate to high bitrate. Valid values:\n<li>0: no,</li>\n<li>1: yes.</li>\nDefault value: no."
      },
      {
        "name": "DisableHigherVideoResolution",
        "desc": "Whether to prohibit transcoding from low resolution to high resolution. Valid values:\n<li>0: no,</li>\n<li>1: yes.</li>\nDefault value: no."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create an adaptive bitrate streaming template. Up to 100 templates can be created."
  },
  "DescribeSampleSnapshotTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of sampled screencapturing templates. Array length limit: 100."
      },
      {
        "name": "Offset",
        "desc": "Paged offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: preset template;</li>\n<li>Custom: custom template.</li>"
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the list of sampled screencapturing templates and supports paged queries by filters."
  },
  "CreateAnimatedGraphicsTemplate": {
    "params": [
      {
        "name": "Fps",
        "desc": "Video frame rate in Hz. Value range: [1, 30]."
      },
      {
        "name": "Width",
        "desc": "Maximum value of the width (or long side) of an animated image in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "Height",
        "desc": "Maximum value of the height (or short side) of an animated image in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "Resolution adaption. Valid values:\n<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>\n<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>\nDefault value: open."
      },
      {
        "name": "Format",
        "desc": "Animated image format. Valid values: gif; webp. Default value: gif."
      },
      {
        "name": "Quality",
        "desc": "Image quality. Value range: [1, 100]. Default value: 75."
      },
      {
        "name": "Name",
        "desc": "Name of an animated image generating template. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create a custom animated image generating template. Up to 16 templates can be created."
  },
  "ModifyClass": {
    "params": [
      {
        "name": "ClassId",
        "desc": "Category ID"
      },
      {
        "name": "ClassName",
        "desc": "Category name, which can contain 1–64 characters."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify the category of a media file."
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "Status",
        "desc": "Filter: Task status. Valid values: WAITING (waiting), PROCESSING (processing), FINISH (completed)."
      },
      {
        "name": "FileId",
        "desc": "Filter: file ID."
      },
      {
        "name": "Limit",
        "desc": "Number of entries to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "ScrollToken",
        "desc": "Scrolling identifier which is used for pulling in batches. If a single request cannot pull all the data entries, the API will return `ScrollToken`, and if the next request carries it, the next pull will start from the next entry."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "* This API is used to query the task list;\n* If there are many data entries in the list, one single call of the API may not be able to pull the entire list. The `ScrollToken` parameter can be used to pull the list in batches;\n* Only tasks in the last three days (72 hours) can be queried."
  },
  "ResetProcedureTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Task flow name"
      },
      {
        "name": "Comment",
        "desc": ""
      },
      {
        "name": "MediaProcessTask",
        "desc": "Parameter of video processing task."
      },
      {
        "name": "AiContentReviewTask",
        "desc": "Parameter of AI-based content audit task."
      },
      {
        "name": "AiAnalysisTask",
        "desc": "Parameter of AI-based content analysis task."
      },
      {
        "name": "AiRecognitionTask",
        "desc": "Type parameter of AI-based content recognition task."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to reset a custom task flow template.  "
  },
  "DescribeCDNUsageData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start date in [ISO date format](https://cloud.tencent.com/document/product/266/11732#I)."
      },
      {
        "name": "EndTime",
        "desc": "End date in [ISO date format](https://cloud.tencent.com/document/product/266/11732#I). The end date must be after the start date."
      },
      {
        "name": "DataType",
        "desc": "CDN statistics type. Valid values:\n<li>Flux: traffic in bytes.</li>\n<li>Bandwidth: bandwidth in bps.</li>"
      },
      {
        "name": "DataInterval",
        "desc": "Time granularity of usage data in minutes. Valid values:\n<li>5: 5-minute granularity, which returns the details at the 5-minute granularity within the specified time range.</li>\n<li>60: 1-hour granularity, which returns the details at the 1-hour granularity within the specified time range.</li>\n<li>1440: 1-day granularity, which returns the details at the 1-day granularity within the specified time range.</li>\nDefault value: 1440. Data at the 1-day granularity will be returned.\nWhen the value of this field is 1, the total usage of all subapplications (including primary application) are queried by an admin."
      },
      {
        "name": "DomainNames",
        "desc": "List of domain names. The usage data of up to 20 domain names can be queried at a time. You can specify multiple domain names and query their combined usage data. The usage data of all domain names will be returned by default."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\nWhen the value of this field is 1, the total usage of all subapplications (including primary application) are queried by an admin. In this case, only 1-day granularity is supported."
      }
    ],
    "desc": "This API is used to query the CDN statistics of VOD such as traffic and bandwidth.\n   1. Only CDN usage data for the last 365 days can be queried.\n   2. The query time range cannot be more than 90 days.\n   3. The time granularity of usage data can be specified, including 5-minute, 1-hour, and 1-day.\n   4. Traffic refers to the total traffic within the query time granularity, while bandwidth the peak bandwidth."
  },
  "CreateTranscodeTemplate": {
    "params": [
      {
        "name": "Container",
        "desc": "Container. Valid values: mp4; flv; hls; mp3; flac; ogg; m4a. Among them, mp3, flac, ogg, and m4a are for audio files."
      },
      {
        "name": "Name",
        "desc": "Transcoding template name. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "RemoveVideo",
        "desc": "Whether to remove video data. Valid values:\n<li>0: retain</li>\n<li>1: remove</li>\nDefault value: 0."
      },
      {
        "name": "RemoveAudio",
        "desc": "Whether to remove audio data. Valid values:\n<li>0: retain</li>\n<li>1: remove</li>\nDefault value: 0."
      },
      {
        "name": "VideoTemplate",
        "desc": "Video stream configuration parameter. This field is required when `RemoveVideo` is 0."
      },
      {
        "name": "AudioTemplate",
        "desc": "Audio stream configuration parameter. This field is required when `RemoveAudio` is 0."
      },
      {
        "name": "TEHDConfig",
        "desc": "TESHD transcoding parameter."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create a custom transcoding template. Up to 100 templates can be created."
  },
  "ModifyImageSpriteTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of an image sprite generating template."
      },
      {
        "name": "Name",
        "desc": "Name of an image sprite generating template. Length limit: 64 characters."
      },
      {
        "name": "Width",
        "desc": "Subimage width of an image sprite in px. Value range: [128, 4,096]."
      },
      {
        "name": "Height",
        "desc": "Subimage height of an image sprite in px. Value range: [128, 4,096]."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "Resolution adaption. Valid values:\n<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>\n<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>\nDefault value: open."
      },
      {
        "name": "SampleType",
        "desc": "Sampling type. Valid values:\n<li>Percent: by percent.</li>\n<li>Time: by time interval.</li>"
      },
      {
        "name": "SampleInterval",
        "desc": "Sampling interval.\n<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>\n<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>"
      },
      {
        "name": "RowCount",
        "desc": "Subimage row count of an image sprite."
      },
      {
        "name": "ColumnCount",
        "desc": "Subimage column count of an image sprite."
      },
      {
        "name": "FillType",
        "desc": "Fill type. \"Fill\" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:\n<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot \"shorter\" or \"longer\";</li>\n<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>\nDefault value: black."
      },
      {
        "name": "Comment",
        "desc": ""
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify a custom image sprite generating template."
  },
  "DeleteClass": {
    "params": [
      {
        "name": "ClassId",
        "desc": "Category ID"
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "* A category can be deleted only if it has no subcategories and associated media files;\n* Otherwise, [delete the media files](/document/product/266/31764) and subcategories first before deleting the category."
  },
  "ExecuteFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "Name of called backend API."
      },
      {
        "name": "FunctionArg",
        "desc": "API parameter. For specific parameter format, negotiate with the backend before calling."
      },
      {
        "name": "SessionContext",
        "desc": "The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters."
      },
      {
        "name": "SessionId",
        "desc": "The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or a blank string is entered, no deduplication will be performed."
      },
      {
        "name": "ExtInfo",
        "desc": "Reserved field for special purposes."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is only used in special scenarios of custom development. Unless requested by VOD customer service, please do not call it."
  },
  "DescribeMediaProcessUsageData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start date in [ISO date format](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)."
      },
      {
        "name": "EndTime",
        "desc": "End date in [ISO date format](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). The end date must be on or after the start date."
      },
      {
        "name": "Type",
        "desc": "Type of video processing task to be queried. Valid value: Transcode. Default value: Transcode.\n<li>Transcode: transcoding</li>"
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the information of video processing usage within the specified time range.\n   1. Statistics on video processing for the last 365 days can be queried.\n   2. The query time range cannot be more than 90 days."
  },
  "ModifyAnimatedGraphicsTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of an animated image generating template."
      },
      {
        "name": "Name",
        "desc": "Name of an animated image generating template. Length limit: 64 characters."
      },
      {
        "name": "Width",
        "desc": "Maximum value of the width (or long side) of an animated image in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "Height",
        "desc": "Maximum value of the height (or short side) of an animated image in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "Resolution adaption. Valid values:\n<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>\n<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>\nDefault value: open."
      },
      {
        "name": "Format",
        "desc": "Animated image format. Valid values: gif, webp."
      },
      {
        "name": "Fps",
        "desc": "Video frame rate in Hz. Value range: [1, 30]."
      },
      {
        "name": "Quality",
        "desc": "Image quality. Value range: [1, 100]. Default value: 75."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify a custom animated image generating template."
  },
  "ComposeMedia": {
    "params": [
      {
        "name": "Tracks",
        "desc": "List of input media tracks, i.e., information of multiple tracks composed of video, audio, image, and other materials. Multiple input tracks are aligned with the output media file on the time axis. The materials of each track at the same time point on the time axis will be superimposed. Specifically, videos or images will be superimposed for video image by track order, where a material with a higher track order will be more on top, while audio materials will be mixed."
      },
      {
        "name": "Output",
        "desc": "Information of output media file."
      },
      {
        "name": "Canvas",
        "desc": "Canvas used for composing video file."
      },
      {
        "name": "SessionContext",
        "desc": ""
      },
      {
        "name": "SessionId",
        "desc": ""
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to compose a media file, including:\n\n1. Clipping a media file to generate a new media file;\n2. Clipping and splicing multiple media files to generate a new media file;\n3. Clipping and splicing the media streams of multiple media files to generate a new media file;"
  },
  "CreateContentReviewTemplate": {
    "params": [
      {
        "name": "ReviewWallSwitch",
        "desc": "Switch controlling whether to add audit result to review list (for human review).\n<li>ON: yes;</li>\n<li>OFF: no.</li>"
      },
      {
        "name": "Name",
        "desc": "Content audit template name. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Description of content audit template. Length limit: 256 characters."
      },
      {
        "name": "PornConfigure",
        "desc": "Control parameter of porn detection."
      },
      {
        "name": "TerrorismConfigure",
        "desc": "Control parameter of terrorism information detection."
      },
      {
        "name": "PoliticalConfigure",
        "desc": "Control parameter of politically sensitive information detection."
      },
      {
        "name": "ProhibitedConfigure",
        "desc": "Control parameter of prohibited information detection. Prohibited information includes:\n<li>Abusive;</li>\n<li>Drug-related.</li>"
      },
      {
        "name": "UserDefineConfigure",
        "desc": "Control parameter of custom content audit."
      },
      {
        "name": "ScreenshotInterval",
        "desc": "Frame capturing interval in seconds. If this parameter is left empty, 1 second will be used by default. Minimum value: 0.5 seconds."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create a custom video content audit template. Up to 50 templates can be created."
  },
  "CreateSampleSnapshotTemplate": {
    "params": [
      {
        "name": "SampleType",
        "desc": "Sampled screencapturing type. Valid values:\n<li>Percent: by percent.</li>\n<li>Time: by time interval.</li>"
      },
      {
        "name": "SampleInterval",
        "desc": "Sampling interval.\n<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>\n<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>"
      },
      {
        "name": "Name",
        "desc": "Name of a sampled screencapturing template. Length limit: 64 characters."
      },
      {
        "name": "Width",
        "desc": "Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "Height",
        "desc": "Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "Resolution adaption. Valid values:\n<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>\n<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>\nDefault value: open."
      },
      {
        "name": "Format",
        "desc": "Image format. Valid values: jpg, png. Default value: jpg."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      },
      {
        "name": "FillType",
        "desc": "Fill type. \"Fill\" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:\n<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot \"shorter\" or \"longer\";</li>\n<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>\n<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>\n<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>\nDefault value: black."
      }
    ],
    "desc": "This API is used to create a custom sampled screencapturing template. Up to 16 templates can be created."
  },
  "DeleteAIAnalysisTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of video content analysis template."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete a custom video content analysis template.\n\nNote: templates with an ID below 10000 are preset and cannot be deleted."
  },
  "DescribeMediaInfos": {
    "params": [
      {
        "name": "FileIds",
        "desc": "List of media file IDs. N starts from 0 and can be up to 19."
      },
      {
        "name": "Filters",
        "desc": "Specifies information entry that needs to be returned by all media files. Multiple entries can be specified simultaneously. N starts from 0. If this field is left empty, all information entries will be returned by default. Valid values:\n<li>basicInfo (basic video information).</li>\n<li>metaData (video metadata).</li>\n<li>transcodeInfo (result information of video transcoding).</li>\n<li>animatedGraphicsInfo (result information of animated image generating task).</li>\n<li>imageSpriteInfo (image sprite information).</li>\n<li>snapshotByTimeOffsetInfo (time point screenshot information).</li>\n<li>sampleSnapshotInfo (sampled screenshot information).</li>\n<li>keyFrameDescInfo (timestamp information).</li>\n<li>adaptiveDynamicStreamingInfo (information of adaptive bitrate streaming).</li>\n<li>miniProgramReviewInfo (WeChat Mini Program audit information).</li>"
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "1. This API can get multiple types of information of multiple media files, including:\n    1. Basic information (basicInfo): media name, category, playback address, cover image, etc.\n    2. Metadata (metaData): size, duration, video stream information, audio stream information, etc.\n    3. Information of the transcoding result (transcodeInfo): addresses, video stream parameters, and audio stream parameters of the media files with various specifications generated by transcoding a media file.\n    4. Information of the animated image generating result (animatedGraphicsInfo): information of an animated image (such as .gif) generated from a video.\n    5. Information of a sampled screenshot (sampleSnapshotInfo): information of a sampled screenshot of a video.\n    6. Information of an image sprite (imageSpriteInfo): information of an image sprite generated from a video.\n    7. Information of a time point screenshot (snapshotByTimeOffsetInfo): information of a time point screenshot of a video.\n    8. Information of a timestamp (keyFrameDescInfo): information of a timestamp set for a video.\n    9. Information of transcoding to adaptive bitrate streaming (adaptiveDynamicStreamingInfo): specification, encryption type, container format, etc.\n2. The return packet can be configured to only contain certain information."
  },
  "LiveRealTimeClip": {
    "params": [
      {
        "name": "StreamId",
        "desc": "[LVB code](https://cloud.tencent.com/document/product/267/5959) of a stream."
      },
      {
        "name": "StartTime",
        "desc": "Start time of stream clipping in [ISO date format](https://cloud.tencent.com/document/product/266/11732#I)."
      },
      {
        "name": "EndTime",
        "desc": "End time of stream clipping in [ISO date format](https://cloud.tencent.com/document/product/266/11732#I)."
      },
      {
        "name": "IsPersistence",
        "desc": "Whether to clip persistently. 0: no, 1: yes. Default: no."
      },
      {
        "name": "ExpireTime",
        "desc": "Storage expiration time of video generated by persistent clipping in [ISO date format](https://cloud.tencent.com/document/product/266/11732#I). `9999-12-31T23:59:59Z` means `never expire`. After the expiration, the media file and its related resources (such as transcoding results and image sprites) will be permanently deleted. This parameter will be valid only when `IsPersistence` is 1. By default, the video will never expire."
      },
      {
        "name": "Procedure",
        "desc": "VOD task flow processing for video generated by persistent clipping. For more information, please see [Specifying Task Flow After Upload](https://cloud.tencent.com/document/product/266/9759). This parameter will be valid only when `IsPersistence` is 1."
      },
      {
        "name": "MetaDataRequired",
        "desc": "Whether the metadata of clipped video needs to be returned. 0: no, 1: yes. Default value: no."
      },
      {
        "name": "Host",
        "desc": "Domain name used for live clipping. Time shifting must be enabled in LVB."
      },
      {
        "name": "ExtInfo",
        "desc": "Reserved field. Do not enter a value for it."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "Live clipping means that during a live broadcast (before it ends), you can select a segment of previous live broadcast content to generate a new video (in HLS format) in real time and share it immediately or store it persistently.\n\nVOD supports two live clipping modes:\n- Persistent clipping: in this mode, the clipped video is saved as an independent video file with a `FileId`, which is suitable for **persistently storing** highlights;\n- Temporary clipping: in this mode, the clipped video is part of the LVB recording file with no `FileId`, which is suitable for **temporarily sharing** highlights;\n\nNote:\n- The live clipping feature can be used only when [time shifting](https://cloud.tencent.com/document/product/267/32742) has been enabled for the target live stream.\n- Live clipping is performed based on the m3u8 file generated by LVB recording, so its minimum clipping granularity is one ts segment rather than at or below the second level.\n\n\n### Persistent clipping\nIn persistent clipping mode, the clipped video is saved as an independent video file with a `FileId`, and its lifecycle is not subject to the source LVB recording video (even if the source video is deleted, the clipped video will not be affected in any way). It can be further processed (transcoded, published on WeChat, etc.).\n\nAn example is as follows: for a complete football match, the source LVB recording video may be up to 2 hours in length. You want to store this video for only 2 months for the purpose of cost savings. However, you want to specify a longer retention period for the \"highlights\" video created by live clipping and perform additional VOD operations on it such as transcoding and release on WeChat. In this case, you need to choose the persistent clipping mode of live clipping.\n\nThe advantage of persistent clipping is that the clipped video has a lifecycle independent of the source recording video and can be managed independently and stored persistently.\n\n### Temporary clipping\nIn temporary clipping mode, the clipped video (m3u8 file) shares the same ts segments with the LVB recording video instead of being an independent video. It only has a playback URL but has no `FileId`, and its validity period is the same as that of the LVB recording video; therefore, if the LVB recording video is deleted, it cannot be played back.\n\nFor temporary clipping, as the clipping result is not an independent video, it will not be included in VOD's media asset management (for example, it will not be counted in the total videos in the console), and no video processing operations can be separately performed on it, such as transcoding and release on WeChat.\n\nThe advantage of temporary clipping is that the clipping operation is very \"lightweight\" and does not incur additional storage fees. However, the clipped video has the same lifecycle as the source recording video and cannot be further transcoded or processed."
  },
  "PullUpload": {
    "params": [
      {
        "name": "MediaUrl",
        "desc": "URL of the media to be pulled. Supported media format: HLS; unsupported media format: DASH.\nFor more information about supported extensions, please see [Media Types](https://cloud.tencent.com/document/product/266/9760#.E5.AA.92.E4.BD.93.E7.B1.BB.E5.9E.8B)."
      },
      {
        "name": "MediaName",
        "desc": "Media name."
      },
      {
        "name": "CoverUrl",
        "desc": "URL of video cover to be pulled. Only gif, jpeg, and png formats are supported."
      },
      {
        "name": "Procedure",
        "desc": "Subsequent task for media. For more information, please see [Specifying Task Flow After Upload](https://cloud.tencent.com/document/product/266/9759)."
      },
      {
        "name": "ExpireTime",
        "desc": "Expiration time of media file in ISO 8601 format. For more information, please see [Notes on ISO Date Format](https://cloud.tencent.com/document/product/266/11732#I)."
      },
      {
        "name": "StorageRegion",
        "desc": "Specifies upload region. This is only applicable to users that have special requirements for the upload region (currently, only Beijing, Shanghai, and Chongqing regions are supported)."
      },
      {
        "name": "ClassId",
        "desc": "Category ID, which is used to categorize the media for management. A category can be created and its ID can be obtained by using the [CreateClass](https://cloud.tencent.com/document/product/266/7812) API."
      },
      {
        "name": "SessionContext",
        "desc": "The source context which is used to pass through the user request information. After `Procedure` is specified, the task flow status change callback will return the value of this field. It can contain up to 1,000 characters."
      },
      {
        "name": "SessionId",
        "desc": "The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or a blank string is entered, no deduplication will be performed."
      },
      {
        "name": "ExtInfo",
        "desc": "Reserved field for special purposes."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      },
      {
        "name": "SourceContext",
        "desc": "Source context, which is used to pass through the user request information. The [upload callback](/document/product/266/7830) API will return the value of this field. It can contain up to 250 characters."
      }
    ],
    "desc": "This API is used to pull a video on the internet to the VOD platform."
  },
  "ModifySampleSnapshotTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a sampled screencapturing template."
      },
      {
        "name": "Name",
        "desc": "Name of a sampled screencapturing template. Length limit: 64 characters."
      },
      {
        "name": "Width",
        "desc": "Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "Height",
        "desc": "Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "Resolution adaption. Valid values:\n<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>\n<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>\nDefault value: open."
      },
      {
        "name": "SampleType",
        "desc": "Sampled screencapturing type. Valid values:\n<li>Percent: by percent.</li>\n<li>Time: by time interval.</li>"
      },
      {
        "name": "SampleInterval",
        "desc": "Sampling interval.\n<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>\n<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>"
      },
      {
        "name": "Format",
        "desc": "Image format. Valid values: jpg, png."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      },
      {
        "name": "FillType",
        "desc": "Fill type. \"Fill\" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:\n<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot \"shorter\" or \"longer\";</li>\n<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>\n<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>\n<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>\nDefault value: black."
      }
    ],
    "desc": "This API is used to modify a custom sampled screencapturing template."
  },
  "DeleteSuperPlayerConfig": {
    "params": [
      {
        "name": "Name",
        "desc": "Player configuration name."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete a superplayer configuration.  \n*Note: preset player configurations cannot be deleted.*"
  },
  "DescribeProcedureTemplates": {
    "params": [
      {
        "name": "Names",
        "desc": "Name filter of task flow template. Array length limit: 100."
      },
      {
        "name": "Type",
        "desc": "Filter of task flow template types. Valid values:\n<li>Preset: preset task flow template;</li>\n<li>Custom: custom task flow template.</li>"
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to get the list of task flow template details by task flow template name."
  },
  "DescribeTranscodeTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of transcoding templates. Array length limit: 100."
      },
      {
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: preset template;</li>\n<li>Custom: custom template.</li>"
      },
      {
        "name": "ContainerType",
        "desc": "Container filter. Valid values:\n<li>Video: video container that can contain both video stream and audio stream;</li>\n<li>PureAudio: audio container that can contain only audio stream.</li>"
      },
      {
        "name": "TEHDType",
        "desc": "TESHD filter, which is used to filter common transcoding or ultra-fast HD transcoding templates. Valid values:\n<li>Common: Common transcoding template;</li>\n<li>TEHD: TESHD template.</li>"
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to get the list of transcoding templates based on unique template ID. The return result includes all eligible custom and [preset transcoding templates](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)."
  },
  "ParseStreamingManifest": {
    "params": [
      {
        "name": "MediaManifestContent",
        "desc": "Index file content to be parsed."
      },
      {
        "name": "ManifestType",
        "desc": "Video index file format, which is `m3u8` by default.\n<li>m3u8</li>\n<li>mpd</li>"
      }
    ],
    "desc": "This API is used to parse the index file content and return the list of segment files to be uploaded when an HLS video is uploaded. A segment file path must be a relative path of the current directory or subdirectory instead of a URL or absolute path."
  },
  "CreateProcedureTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Task flow name (up to 20 characters)."
      },
      {
        "name": "Comment",
        "desc": ""
      },
      {
        "name": "MediaProcessTask",
        "desc": "Parameter of video processing task."
      },
      {
        "name": "AiContentReviewTask",
        "desc": "Parameter of AI-based content audit task."
      },
      {
        "name": "AiAnalysisTask",
        "desc": "Parameter of AI-based content analysis task."
      },
      {
        "name": "AiRecognitionTask",
        "desc": "Type parameter of AI-based content recognition task."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create a custom task flow template. Up to 50 templates can be created."
  },
  "PushUrlCache": {
    "params": [
      {
        "name": "Urls",
        "desc": "List of prefetched URLs. Up to 20 ones can be specified at a time."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "1. This API is used to prefetch a list of specified URLs.\n2. The URL domain names must have already been registered with VOD.\n3. Up to 20 URLs can be specified in one request."
  },
  "DeleteMedia": {
    "params": [
      {
        "name": "FileId",
        "desc": "Unique media file ID."
      },
      {
        "name": "DeleteParts",
        "desc": "Content to be deleted. The default value is \"[]\", which indicates to delete the media file and all its corresponding files generated by video processing."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "* This API is used to delete a media file and its corresponding files generated by video processing (such as transcoded videos, image sprites, screenshots, and videos published on WeChat);\n* The transcoded video files or video files published on WeChat can be deleted separately for a specified video ID."
  },
  "CreateSuperPlayerConfig": {
    "params": [
      {
        "name": "Name",
        "desc": "Player configuration name, which can contain up to 64 letters, digits, underscores, and hyphens (such as test_ABC-123) and must be unique under a user."
      },
      {
        "name": "DrmSwitch",
        "desc": "Switch of DRM-protected adaptive bitstream playback:\n<li>ON: enabled, indicating to play back only output adaptive bitstreams protected by DRM;</li>\n<li>OFF: disabled, indicating to play back unencrypted output adaptive bitstreams.</li>\nDefault value: OFF."
      },
      {
        "name": "AdaptiveDynamicStreamingDefinition",
        "desc": "ID of the unencrypted adaptive bitrate streaming template that allows output, which is required if `DrmSwitch` is `OFF`."
      },
      {
        "name": "DrmStreamingsInfo",
        "desc": "Content of the DRM-protected adaptive bitrate streaming template that allows output, which is required if `DrmSwitch` is `ON`."
      },
      {
        "name": "ImageSpriteDefinition",
        "desc": "ID of the image sprite generating template that allows output."
      },
      {
        "name": "ResolutionNames",
        "desc": "Display name of player for substreams with different resolutions. If this parameter is left empty or an empty array, the default configuration will be used:\n<li>MinEdgeLength: 240, Name: LD;</li>\n<li>MinEdgeLength: 480, Name: SD;</li>\n<li>MinEdgeLength: 720, Name: HD;</li>\n<li>MinEdgeLength: 1080, Name: FHD;</li>\n<li>MinEdgeLength: 1440, Name: 2K;</li>\n<li>MinEdgeLength: 2160, Name: 4K;</li>\n<li>MinEdgeLength: 4320, Name: 8K.</li>"
      },
      {
        "name": "Domain",
        "desc": ""
      },
      {
        "name": "Scheme",
        "desc": ""
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create a superplayer configuration. Up to 100 configurations can be created."
  },
  "ModifyPersonSample": {
    "params": [
      {
        "name": "PersonId",
        "desc": "Figure ID."
      },
      {
        "name": "Name",
        "desc": "Name. Length limit: 128 characters."
      },
      {
        "name": "Description",
        "desc": "Description. Length limit: 1,024 characters."
      },
      {
        "name": "Usages",
        "desc": "Figure use case. Valid values:\n1. Recognition: it is used for content recognition and equivalent to `Recognition.Face`.\n2. Review: it is used for content audit and equivalent to `Review.Face`.\n3. All: it is used for content recognition and content audit and equivalent to 1+2 above."
      },
      {
        "name": "FaceOperationInfo",
        "desc": "Face operation information."
      },
      {
        "name": "TagOperationInfo",
        "desc": "Tag operation information."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify figure sample information based on figure ID, such as modifying the name and description and adding/deleting/resetting a face or tag. There should be at least one image left after the face deletion operation; otherwise, please use the reset operation."
  },
  "DeleteContentReviewTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of content audit template."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete a custom video content audit template."
  },
  "CreateAIAnalysisTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Video content analysis template name. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Video content analysis template description. Length limit: 256 characters."
      },
      {
        "name": "ClassificationConfigure",
        "desc": "Control parameter of intelligent categorization task."
      },
      {
        "name": "TagConfigure",
        "desc": "Control parameter of intelligent tagging task."
      },
      {
        "name": "CoverConfigure",
        "desc": "Control parameter of intelligent cover generating task."
      },
      {
        "name": "FrameTagConfigure",
        "desc": "Control parameter of intelligent frame-specific tagging task."
      },
      {
        "name": "HighlightConfigure",
        "desc": "Control parameter of an intelligent highlight generating task."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create a custom video content analysis template. Up to 50 templates can be created."
  },
  "DescribeSnapshotByTimeOffsetTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of time point screencapturing templates. Array length limit: 100."
      },
      {
        "name": "Offset",
        "desc": "Paged offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: preset template;</li>\n<li>Custom: custom template.</li>"
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the list of time point screencapturing templates and supports paged queries by filters."
  },
  "ProcessMediaByUrl": {
    "params": [
      {
        "name": "InputInfo",
        "desc": "Information of input video, including video's URL, name, and custom ID."
      },
      {
        "name": "OutputInfo",
        "desc": "Information of COS path to output file."
      },
      {
        "name": "AiContentReviewTask",
        "desc": "Type parameter of video content audit task."
      },
      {
        "name": "AiAnalysisTask",
        "desc": "Video content analysis task parameter."
      },
      {
        "name": "AiRecognitionTask",
        "desc": "Type parameter of video content recognition task."
      },
      {
        "name": "TasksPriority",
        "desc": "Task flow priority. The higher the value, the higher the priority. Value range: -10-10. If this parameter is left empty, 0 will be used."
      },
      {
        "name": "TasksNotifyMode",
        "desc": "Notification mode for task flow status change. Valid values: Finish, Change, None. If this parameter is left empty, `Finish` will be used."
      },
      {
        "name": "SessionContext",
        "desc": "The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters."
      },
      {
        "name": "SessionId",
        "desc": "The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or a blank string is entered, no deduplication will be performed."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to initiate a processing task for an audio/video media file from a URL, including:\n\n1. Intelligent content audit (detection of porn, terrorism, and politically sensitive information);\n2. Intelligent content analysis (tag, category, cover, and frame-specific tag);\n3. Intelligent content recognition (opening and closing credits, face, full text, text keyword, full speech, speech keyword, and object).\n\nIf the event notification is used, its type is [Task Flow Status Change](https://cloud.tencent.com/document/product/266/9636)."
  },
  "ModifyTranscodeTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of transcoding template."
      },
      {
        "name": "Container",
        "desc": "Container. Valid values: mp4; flv; hls; mp3; flac; ogg; m4a. Among them, mp3, flac, ogg, and m4a are for audio files."
      },
      {
        "name": "Name",
        "desc": "Transcoding template name. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 bytes."
      },
      {
        "name": "RemoveVideo",
        "desc": "Whether to remove video data. Valid values:\n<li>0: retain</li>\n<li>1: remove</li>"
      },
      {
        "name": "RemoveAudio",
        "desc": "Whether to remove audio data. Valid values:\n<li>0: retain</li>\n<li>1: remove</li>"
      },
      {
        "name": "VideoTemplate",
        "desc": "Video stream configuration parameter."
      },
      {
        "name": "AudioTemplate",
        "desc": "Audio stream configuration parameter."
      },
      {
        "name": "TEHDConfig",
        "desc": "TESHD transcoding parameter."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify a custom transcoding template."
  },
  "DescribeContentReviewTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of content audit templates. Array length limit: 100."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to get the list of video content audit templates based on unique template ID. The return result includes all eligible custom and [preset video content audit templates](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.AE.A1.E6.A0.B8.E6.A8.A1.E6.9D.BF)."
  },
  "ModifyWatermarkTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of watermarking template."
      },
      {
        "name": "Name",
        "desc": "Watermarking template name. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "CoordinateOrigin",
        "desc": "Origin position. Valid values:\n<li>TopLeft: the origin of coordinates is in the top-left corner of the video, and the origin of the watermark is in the top-left corner of the image or text;</li>\n<li>TopRight: the origin of coordinates is in the top-right corner of the video, and the origin of the watermark is in the top-right corner of the image or text;</li>\n<li>BottomLeft: the origin of coordinates is in the bottom-left corner of the video, and the origin of the watermark is in the bottom-left corner of the image or text;</li>\n<li>BottomRight: the origin of coordinates is in the bottom-right corner of the video, and the origin of the watermark is in the bottom-right corner of the image or text.</li>"
      },
      {
        "name": "XPos",
        "desc": "The horizontal position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:\n<li>If the string ends in %, the `XPos` of the watermark will be the specified percentage of the video width; for example, `10%` means that `XPos` is 10% of the video width;</li>\n<li>If the string ends in px, the `XPos` of the watermark will be the specified px; for example, `100px` means that `XPos` is 100 px.</li>"
      },
      {
        "name": "YPos",
        "desc": "The vertical position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:\n<li>If the string ends in %, the `YPos` of the watermark will be the specified percentage of the video height; for example, `10%` means that `YPos` is 10% of the video height;</li>\n<li>If the string ends in px, the `YPos` of the watermark will be the specified px; for example, `100px` means that `YPos` is 100 px.</li>"
      },
      {
        "name": "ImageTemplate",
        "desc": "Image watermarking template. This field is valid only for image watermarking templates."
      },
      {
        "name": "TextTemplate",
        "desc": "Text watermarking template. This field is valid only for text watermarking templates."
      },
      {
        "name": "SvgTemplate",
        "desc": "SVG watermarking template. This field is only valid for SVG watermarking templates."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify a custom watermarking template. The watermark type cannot be modified."
  },
  "DescribeStorageDetails": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start time in ISO 8601 format. For more information, please see [Notes on ISO Date Format](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)."
      },
      {
        "name": "EndTime",
        "desc": "End time in ISO 8601 format, which must be after the start time. For more information, please see [Notes on ISO Date Format](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)."
      },
      {
        "name": "Interval",
        "desc": "Query time interval. Valid values:\n<li>Minute: once per minute.</li>\n<li>Hour: once per hour.</li>\n<li>Day: once per day.</li>\nThe default value is determined by the time span. `Minute` will be used if the time span is less than 1 hour, `Hour` if less than or equal to 7 days, and `Day` if more than 7 days."
      },
      {
        "name": "StorageType",
        "desc": "Storage class to be queried. Valid values:\n<li>TotalStorage: total storage capacity.</li>\n<li>StandardStorage: Standard storage.</li>\n<li>InfrequentStorage: Standard_IA storage.</li>\nDefault value: TotalStorage."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\nWhen the value of this field is 1, the total usage of all subapplications (including primary application) are queried by an admin."
      }
    ],
    "desc": "This API is used to query the used VOD storage capacity in bytes within the specified time range.\n   1. Only storage capacity usage data for the last 365 days can be queried.\n   2. The query time range cannot be more than 90 days;\n   3. The query time range at the minute granularity cannot be more than 5 days;\n   4. The query time range at the hour granularity cannot be more than 10 days."
  },
  "DeleteWordSamples": {
    "params": [
      {
        "name": "Keywords",
        "desc": "Keyword. Array length limit: 100 words."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete keyword samples in batches."
  },
  "ModifySubAppIdInfo": {
    "params": [
      {
        "name": "SubAppId",
        "desc": "Subapplication ID."
      },
      {
        "name": "Name",
        "desc": "Subapplication name. Length limit: 40 characters."
      },
      {
        "name": "Description",
        "desc": "Subapplication overview. Length limit: 300 characters."
      }
    ],
    "desc": "This API is used to modify subapplication information, but it is not allowed to modify primary application information."
  },
  "CreateWatermarkTemplate": {
    "params": [
      {
        "name": "Type",
        "desc": "Watermarking type. Valid values:\n<li>image: image watermark;</li>\n<li>text: text watermark;</li>\n<li>svg: SVG watermark.</li>"
      },
      {
        "name": "Name",
        "desc": "Watermarking template name. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "CoordinateOrigin",
        "desc": "Origin position. Valid values:\n<li>TopLeft: the origin of coordinates is in the top-left corner of the video, and the origin of the watermark is in the top-left corner of the image or text;</li>\n<li>TopRight: the origin of coordinates is in the top-right corner of the video, and the origin of the watermark is in the top-right corner of the image or text;</li>\n<li>BottomLeft: the origin of coordinates is in the bottom-left corner of the video, and the origin of the watermark is in the bottom-left corner of the image or text;</li>\n<li>BottomRight: the origin of coordinates is in the bottom-right corner of the video, and the origin of the watermark is in the bottom-right corner of the image or text.</li>\nDefault value: TopLeft."
      },
      {
        "name": "XPos",
        "desc": "The horizontal position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:\n<li>If the string ends in %, the `XPos` of the watermark will be the specified percentage of the video width; for example, `10%` means that `XPos` is 10% of the video width;</li>\n<li>If the string ends in px, the `XPos` of the watermark will be the specified px; for example, `100px` means that `XPos` is 100 px.</li>\nDefault value: 0 px."
      },
      {
        "name": "YPos",
        "desc": "The vertical position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:\n<li>If the string ends in %, the `YPos` of the watermark will be the specified percentage of the video height; for example, `10%` means that `YPos` is 10% of the video height;</li>\n<li>If the string ends in px, the `YPos` of the watermark will be the specified px; for example, `100px` means that `YPos` is 100 px.</li>\nDefault value: 0 px."
      },
      {
        "name": "ImageTemplate",
        "desc": "Image watermarking template. This field is required when `Type` is `image` and is invalid when `Type` is `text`."
      },
      {
        "name": "TextTemplate",
        "desc": "Text watermarking template. This field is required when `Type` is `text` and is invalid when `Type` is `image`."
      },
      {
        "name": "SvgTemplate",
        "desc": "SVG watermarking template. This field is required when `Type` is `svg` and is invalid when `Type` is `image` or `text`."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create a custom watermarking template. Up to 1,000 templates can be created."
  },
  "DescribePersonSamples": {
    "params": [
      {
        "name": "Type",
        "desc": "Pulled figure type. Valid values:\n<li>UserDefine: custom figure library;</li>\n<li>Default: default figure library.</li>\n\nDefault value: UserDefine (the custom figure library will be pulled.)\nNote: the default figure library can be pulled only through \"figure name\" or \"figure ID + figure name\", and only one face image will be returned."
      },
      {
        "name": "PersonIds",
        "desc": "Figure ID. Array length limit: 100."
      },
      {
        "name": "Names",
        "desc": "Figure name. Array length limit: 20."
      },
      {
        "name": "Tags",
        "desc": "Figure tag. Array length limit: 20."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of entries to be returned. Default value: 100. Maximum value: 100."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the information of figure samples and supports paginated queries by figure ID, name, and tag."
  },
  "DeleteAIRecognitionTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of video content recognition template."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete a custom video content recognition template."
  },
  "CreateSubAppId": {
    "params": [
      {
        "name": "Name",
        "desc": "Subapplication name. Length limit: 40 characters."
      },
      {
        "name": "Description",
        "desc": "Subapplication overview. Length limit: 300 characters."
      }
    ],
    "desc": "This API is used to create a VOD subapplication."
  },
  "DescribeAnimatedGraphicsTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of animated image generating templates. Array length limit: 100."
      },
      {
        "name": "Offset",
        "desc": "Paged offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: preset template;</li>\n<li>Custom: custom template.</li>"
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the list of animated image generating templates and supports paged queries by filters."
  },
  "ForbidMediaDistribution": {
    "params": [
      {
        "name": "FileIds",
        "desc": "List of media files. Up to 20 ones can be submitted at a time."
      },
      {
        "name": "Operation",
        "desc": "forbid: forbids, recover: unblocks."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "* After a media file is forbidden, except previewing it in the VOD Console, accessing the URLs of its various resources (such as source file, output files, and screenshots) in other scenarios will return error 403.\n  It takes about 5-10 minutes for a forbidding/unblocking operation to take effect across the entire network."
  },
  "ModifySnapshotByTimeOffsetTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a specified time point screencapturing template."
      },
      {
        "name": "Name",
        "desc": "Name of a time point screencapturing template. Length limit: 64 characters."
      },
      {
        "name": "Width",
        "desc": "Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "Height",
        "desc": "Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "Resolution adaption. Valid values:\n<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>\n<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>\nDefault value: open."
      },
      {
        "name": "Format",
        "desc": "Image format. Valid values: jpg, png."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      },
      {
        "name": "FillType",
        "desc": "Fill type. \"Fill\" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:\n<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot \"shorter\" or \"longer\";</li>\n<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>\n<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>\n<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>\nDefault value: black."
      }
    ],
    "desc": "This API is used to modify a custom time point screencapturing template."
  },
  "ModifySuperPlayerConfig": {
    "params": [
      {
        "name": "Name",
        "desc": "Player configuration name."
      },
      {
        "name": "DrmSwitch",
        "desc": "Switch of DRM-protected adaptive bitstream playback:\n<li>ON: enabled, indicating to play back only output adaptive bitstreams protected by DRM;</li>\n<li>OFF: disabled, indicating to play back unencrypted output adaptive bitstreams.</li>"
      },
      {
        "name": "AdaptiveDynamicStreamingDefinition",
        "desc": "ID of the unencrypted adaptive bitrate streaming template that allows output."
      },
      {
        "name": "DrmStreamingsInfo",
        "desc": "Content of the DRM-protected adaptive bitrate streaming template that allows output."
      },
      {
        "name": "ImageSpriteDefinition",
        "desc": "ID of the image sprite generating template that allows output."
      },
      {
        "name": "ResolutionNames",
        "desc": "Display name of player for substreams with different resolutions."
      },
      {
        "name": "Domain",
        "desc": ""
      },
      {
        "name": "Scheme",
        "desc": ""
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify a superplayer configuration."
  },
  "CreateClass": {
    "params": [
      {
        "name": "ParentId",
        "desc": "Parent category ID. For a first-level category, enter `-1`."
      },
      {
        "name": "ClassName",
        "desc": "Category name. Length limit: 1-64 characters."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "* This API is used to categorize media assets for management;\n* It does not affect the categories of existing media assets. If you want to modify the category of a media asset, call the [ModifyMediaInfo](/document/product/266/31762) API.\n* There can be up to 4 levels of categories.\n* One category can have up to 500 subcategories under it."
  },
  "CreateWordSamples": {
    "params": [
      {
        "name": "Usages",
        "desc": "<b>Keyword use case. Valid values:</b>\n1. Recognition.Ocr: OCR-based content recognition;\n2. Recognition.Asr: ASR-based content recognition;\n3. Review.Ocr: OCR-based content audit;\n4. Review.Asr: ASR-based content audit;\n<b>These values can be merged as follows:</b>\n5. Recognition: ASR-based and OCR-based content recognition, which is equivalent to 1+2 above;\n6. Review: ASR-based and OCR-based content audit, which is equivalent to 3+4 above;\n7. All: ASR-based and OCR-based content recognition and audit, which is equivalent to 1+2+3+4 above;"
      },
      {
        "name": "Words",
        "desc": "Keyword. Array length limit: 100."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create keyword samples in batches for video processing operations such as content recognition and audit by using the OCR and ASR technologies."
  },
  "DescribeAdaptiveDynamicStreamingTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of transcoding to adaptive bitrate streaming templates. Array length limit: 100."
      },
      {
        "name": "Offset",
        "desc": "Paged offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: preset template;</li>\n<li>Custom: custom template.</li>"
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the list of transcoding to adaptive bitrate streaming templates and supports paged queries by filters."
  },
  "ModifyWordSample": {
    "params": [
      {
        "name": "Keyword",
        "desc": "Keyword. Length limit: 128 characters."
      },
      {
        "name": "Usages",
        "desc": "<b>Keyword use case. Valid values:</b>\n1. Recognition.Ocr: OCR-based content recognition;\n2. Recognition.Asr: ASR-based content recognition;\n3. Review.Ocr: OCR-based content audit;\n4. Review.Asr: ASR-based content audit;\n<b>These values can be merged as follows:</b>\n5. Recognition: ASR-based and OCR-based content recognition, which is equivalent to 1+2 above;\n6. Review: ASR-based and OCR-based content audit, which is equivalent to 3+4 above;\n7. All: ASR-based and OCR-based content recognition and audit, which is equivalent to 1+2+3+4 above;"
      },
      {
        "name": "TagOperationInfo",
        "desc": "Tag operation information."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify the use case and tag of a keyword. The keyword itself cannot be modified, but you can delete it and create another one if needed."
  },
  "DescribeImageSpriteTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of image sprite generating templates. Array length limit: 100."
      },
      {
        "name": "Offset",
        "desc": "Paged offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: preset template;</li>\n<li>Custom: custom template.</li>"
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the list of image sprite generating templates and supports paged queries by filters."
  },
  "DescribeAllClass": {
    "params": [
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "* This API is used to get the information of all categories."
  },
  "DescribeWatermarkTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of watermarking templates. Array length limit: 100."
      },
      {
        "name": "Type",
        "desc": "Watermark type filter. Valid values:\n<li>image: image watermark;</li>\n<li>text: text watermark.</li>"
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries\n<li>Default value: 10;</li>\n<li>Maximum value: 100.</li>"
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query custom watermarking templates and supports paged queries by filters."
  },
  "CreateImageSpriteTemplate": {
    "params": [
      {
        "name": "SampleType",
        "desc": "Sampling type. Valid values:\n<li>Percent: by percent.</li>\n<li>Time: by time interval.</li>"
      },
      {
        "name": "SampleInterval",
        "desc": "Sampling interval.\n<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>\n<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>"
      },
      {
        "name": "RowCount",
        "desc": "Subimage row count of an image sprite."
      },
      {
        "name": "ColumnCount",
        "desc": "Subimage column count of an image sprite."
      },
      {
        "name": "Name",
        "desc": "Name of an image sprite generating template. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": ""
      },
      {
        "name": "FillType",
        "desc": "Fill type. \"Fill\" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:\n<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot \"shorter\" or \"longer\";</li>\n<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>\nDefault value: black."
      },
      {
        "name": "Width",
        "desc": "Maximum value of the width (or long side) of a subimage in an image sprite in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "Height",
        "desc": "Maximum value of the height (or short side) of a subimage in an image sprite in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "Resolution adaption. Valid values:\n<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>\n<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>\nDefault value: open."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create a custom image sprite generating template. Up to 16 templates can be created."
  },
  "DescribeAIRecognitionTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of video content recognition templates. Array length limit: 100."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to get the list of video content recognition templates based on unique template ID. The return result includes all eligible custom and [preset video content recognition templates](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E8.AF.86.E5.88.AB.E6.A8.A1.E6.9D.BF)."
  },
  "DescribeSuperPlayerConfigs": {
    "params": [
      {
        "name": "Names",
        "desc": "Player configuration name filter. Array length limit: 100."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of entries to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Type",
        "desc": "Player configuration type filter. Valid values:\n<li>Preset: preset configuration;</li>\n<li>Custom: custom configuration.</li>"
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the list of superplayer configurations and supports paginated queries by filters."
  },
  "DescribeSubAppIds": {
    "params": [],
    "desc": "This API is used to get the list of subapplications to which the current account has permissions, including primary applications. If the subapplication feature has not been enabled, this API will return. \n `FailedOperation`."
  },
  "CommitUpload": {
    "params": [
      {
        "name": "VodSessionKey",
        "desc": "VOD session, which takes the returned value (VodSessionKey) of the `ApplyUpload` API."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to confirm the result of uploading a media file (and cover file) to VOD, store the media information, and return the playback address and ID of the file."
  },
  "ConfirmEvents": {
    "params": [
      {
        "name": "EventHandles",
        "desc": "Event handler, i.e., the `EventSet. EventHandle` field in the output parameters of the [event notification pulling](/document/product/266/33433) API.\nArray length limit: 16."
      },
      {
        "name": "ExtInfo",
        "desc": "Reserved field for special purposes."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "* After the `PullEvents` API is called to get an event, this API must be called to confirm that the message has been received;\n* After the event handler is obtained, the validity period of waiting for confirmation is 30 seconds. If the wait exceeds 30 seconds, a parameter error will be reported (4000);\n* For more information, please see the [reliable callback](https://cloud.tencent.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83) of event notification."
  },
  "ModifyAIRecognitionTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of video content recognition template."
      },
      {
        "name": "Name",
        "desc": "Video content recognition template name. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Description of video content recognition template. Length limit: 256 characters."
      },
      {
        "name": "HeadTailConfigure",
        "desc": "Control parameter of video opening and ending credits recognition."
      },
      {
        "name": "SegmentConfigure",
        "desc": "Control parameter of video splitting recognition."
      },
      {
        "name": "FaceConfigure",
        "desc": "Control parameter of face recognition."
      },
      {
        "name": "OcrFullTextConfigure",
        "desc": "Control parameter of full text recognition."
      },
      {
        "name": "OcrWordsConfigure",
        "desc": "Control parameter of text keyword recognition."
      },
      {
        "name": "AsrFullTextConfigure",
        "desc": "Control parameter of full speech recognition."
      },
      {
        "name": "AsrWordsConfigure",
        "desc": "Control parameter of speech keyword recognition."
      },
      {
        "name": "ObjectConfigure",
        "desc": "Control parameter of object recognition."
      },
      {
        "name": "ScreenshotInterval",
        "desc": "Frame capturing interval in seconds. Minimum value: 0.5 seconds."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify a custom video content recognition template."
  },
  "ModifyAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of adaptive bitrate streaming template."
      },
      {
        "name": "Name",
        "desc": "Template name. Length limit: 64 characters."
      },
      {
        "name": "Format",
        "desc": "Adaptive bitstream format. Valid values:\n<li>HLS.</li>"
      },
      {
        "name": "DisableHigherVideoBitrate",
        "desc": "Whether to prohibit transcoding video from low bitrate to high bitrate. Valid values:\n<li>0: no,</li>\n<li>1: yes.</li>"
      },
      {
        "name": "DisableHigherVideoResolution",
        "desc": "Whether to prohibit transcoding from low resolution to high resolution. Valid values:\n<li>0: no,</li>\n<li>1: yes.</li>"
      },
      {
        "name": "StreamInfos",
        "desc": "Parameter information of input stream for adaptive bitrate streaming. Up to 10 streams can be input.\nNote: the frame rate of all streams must be the same; otherwise, the frame rate of the first stream will be used as the output frame rate."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify an adaptive bitrate streaming template."
  },
  "SearchMedia": {
    "params": [
      {
        "name": "Text",
        "desc": "Search text, which fuzzily matches the media file name or description. The more matching items and the higher the match rate, the higher-ranked the result. It can contain up to 64 characters."
      },
      {
        "name": "Tags",
        "desc": "Tag set, which matches any element in the set.\n<li>Tag length limit: 8 characters.</li>\n<li>Array length limit: 10.</li>"
      },
      {
        "name": "ClassIds",
        "desc": "Category ID set, which matches the categories of the specified IDs and all subcategories. Array length limit: 10."
      },
      {
        "name": "StartTime",
        "desc": "Start time in the creation time range.\n<li>After or at the start time.</li>\n<li>In ISO 8601 format. For more information, please see [Notes on ISO Date Format](https://cloud.tencent.com/document/product/266/11732#I).</li>"
      },
      {
        "name": "EndTime",
        "desc": "End time in the creation time range.\n<li>Before the end time.</li>\n<li>In ISO 8601 format. For more information, please see [Notes on ISO Date Format](https://cloud.tencent.com/document/product/266/11732#I).</li>"
      },
      {
        "name": "SourceType",
        "desc": "Media file source. For valid values, please see [SourceType](https://cloud.tencent.com/document/product/266/31773#MediaSourceData)."
      },
      {
        "name": "StreamId",
        "desc": "[LVB code](https://cloud.tencent.com/document/product/267/5959) of a stream."
      },
      {
        "name": "Vid",
        "desc": "Unique ID of LVB recording file."
      },
      {
        "name": "Sort",
        "desc": "Sorting order.\n<li>Valid value of `Sort.Field`: CreateTime</li>\n<li>If `Text` is specified for the search, the results will be sorted by the match rate, and this field will not take effect</li>"
      },
      {
        "name": "Offset",
        "desc": "<div id=\"p_offset\">Start offset of a paged return. Default value: 0. Entries from No. \"Offset\" to No. \"Offset + Limit - 1\" will be returned.\n<li>Value range: \"Offset + Limit\" cannot be more than 5,000. (For more information, please see <a href=\"#maxResultsDesc\">Limit on the Number of Results Returned by API</a>)</li></div>"
      },
      {
        "name": "Limit",
        "desc": "<div id=\"p_limit\">Number of entries returned by a paged query. Default value: 10. Entries from No. \"Offset\" to No. \"Offset + Limit - 1\" will be returned.\n<li>Value range: \"Offset + Limit\" cannot be more than 5,000. (For more information, please see <a href=\"#maxResultsDesc\">Limit on the Number of Results Returned by API</a>)</li></div>"
      },
      {
        "name": "Categories",
        "desc": "File type:\n<li>Video: video file</li>\n<li>Audio: audio file</li>\n<li>Image: image file</li>"
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to search for media information and supports filtering and sorting the returned results in many ways. It can:\n- Fuzzily search by media file name or description.\n- Retrieve media files by category and tag.\n    - Specify the `ClassIds` category set (please see the input parameters) and return the media files in any category in the set. For example, assuming that there are categories of Movies, TV Series, and Variety Shows, and there are subcategories of History, Action, and Romance in the category of Movies, if Movies and TV Series are specified in `ClassIds`, then all the subcategories under Movies and TV Series will be returned; however, if History and Action are specified in `ClassIds`, only the media files in those two subcategories will be returned.\n    - Specify the `Tags` tag set (please see the input parameters) and return the media files with any tag in the set. For example, assuming that there are tags of ACG, Drama, and YTPMV, if ACG and YTPMV are specified in Tags, then any media files with either tag will be retrieved.\n- Filter media files from a specified source (`Source`) (please see the input parameters).\n- Filter LVB recording media files by LVB push code and `Vid` (please see the input parameters).\n- Filter media files by the creation time range.\n- Mix and match any filters above to retrieve the media files that meet all the specified criteria. For example, you can filter the media files with the tag of \"Drama\" in the category of \"Movies\" created between December 1, 2018 and December 8, 2018.\n- Sort the results and return them in multiple pages by specifying `Offset` and `Limit` (please see the input parameters).\n\n<div id=\"maxResultsDesc\">Upper limit of returned results:</div>\n- The <b><a href=\"#p_offset\">Offset</a> and <a href=\"#p_limit\">Limit</a> parameters determine the number of search results on one single page. Note: if both of them use the default value, this API will return up to 10 results.</b>\n- <b>Up to 5,000 search results can be returned, and excessive ones will not be displayed. If there are too many search results, you are recommended to use more specified filters to narrow down the search results.</b>"
  },
  "DeleteWatermarkTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of watermarking template."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete a custom watermarking template."
  },
  "DeletePersonSample": {
    "params": [
      {
        "name": "PersonId",
        "desc": "Figure ID."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete a figure sample based on figure ID."
  },
  "DeleteSnapshotByTimeOffsetTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a specified time point screencapturing template."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete a custom time point screencapturing template."
  },
  "DeleteSampleSnapshotTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a sampled screencapturing template."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete a custom sampled screencapturing template."
  },
  "WeChatMiniProgramPublish": {
    "params": [
      {
        "name": "FileId",
        "desc": "Media file ID."
      },
      {
        "name": "SourceDefinition",
        "desc": "ID of the transcoding template corresponding to the published video. 0 represents the source video."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to publish a VOD video on WeChat Mini Program for playback in the WeChat Mini Program player."
  },
  "SimpleHlsClip": {
    "params": [
      {
        "name": "Url",
        "desc": "URL of the HLS video in VOD that needs to be clipped."
      },
      {
        "name": "StartTimeOffset",
        "desc": "Start offset time of clipping in seconds. Default value: 0, which means to clip from the beginning of the video. A negative number indicates how many seconds from the end of the video clipping will start at. For example, -10 means that clipping will start at the 10th second from the end."
      },
      {
        "name": "EndTimeOffset",
        "desc": "End offset time of clipping in seconds. Default value: 0, which means to clip till the end of the video. A negative number indicates how many seconds from the end of the video clipping will end. For example, -10 means that clipping will end at the 10th second from the end."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to clip an HLS video by time period.\n\nNote: the clipped video shares the same ts segments with the source video, and only a new m3u8 file will be generated. Deleting the source video will also delete the clipped video."
  },
  "CreatePersonSample": {
    "params": [
      {
        "name": "Name",
        "desc": "Figure name. Length limit: 20 characters."
      },
      {
        "name": "Usages",
        "desc": "Figure use case. Valid values:\n1. Recognition: it is used for content recognition and equivalent to `Recognition.Face`.\n2. Review: it is used for content audit and equivalent to `Review.Face`.\n3. All: it is used for content recognition and content audit and equivalent to 1+2 above."
      },
      {
        "name": "Description",
        "desc": "Figure description. Length limit: 1,024 characters."
      },
      {
        "name": "FaceContents",
        "desc": "String generated by [Base64-encoding](https://tools.ietf.org/html/rfc4648) face image. Only JPEG and PNG images are supported. Array length limit: 5 images.\nNote: the image must be a relatively clear full-face photo of a figure in at least 200 * 200 px."
      },
      {
        "name": "Tags",
        "desc": "Figure tag\n<li>Array length limit: 20 tags;</li>\n<li>Tag length limit: 128 characters.</li>"
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create a figure sample for video processing operations such as content recognition and audit using the face recognition technology."
  },
  "ModifySubAppIdStatus": {
    "params": [
      {
        "name": "SubAppId",
        "desc": "Subapplication ID."
      },
      {
        "name": "Status",
        "desc": "Subapplication status. Valid values:\n<li>On: enabled</li>\n<li>Off: disabled</li>"
      }
    ],
    "desc": "This API is used to enable/disable a subapplication. After a subapplication is disabled, its corresponding domain name will be blocked and its access to the console will be restricted."
  },
  "ModifyContentReviewTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of content audit template."
      },
      {
        "name": "Name",
        "desc": "Content audit template name. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Description of content audit template. Length limit: 256 characters."
      },
      {
        "name": "PornConfigure",
        "desc": "Control parameter of porn detection."
      },
      {
        "name": "TerrorismConfigure",
        "desc": "Control parameter of terrorism information detection."
      },
      {
        "name": "PoliticalConfigure",
        "desc": "Control parameter of politically sensitive information detection."
      },
      {
        "name": "ProhibitedConfigure",
        "desc": "Control parameter of prohibited information detection. Prohibited information includes:\n<li>Abusive;</li>\n<li>Drug-related.</li>"
      },
      {
        "name": "UserDefineConfigure",
        "desc": "Control parameter of custom content audit."
      },
      {
        "name": "ScreenshotInterval",
        "desc": "Frame capturing interval in seconds. Minimum value: 0.5 seconds."
      },
      {
        "name": "ReviewWallSwitch",
        "desc": "Switch controlling whether to add audit result to review list (for human review).\n<li>ON: yes;</li>\n<li>OFF: no.</li>"
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify a custom video content audit template."
  },
  "ProcessMedia": {
    "params": [
      {
        "name": "FileId",
        "desc": "Media file ID, i.e., the globally unique ID of a file in VOD assigned by the VOD backend after successful upload. This field can be obtained through the [video upload completion event notification](/document/product/266/7830) or [VOD Console](https://console.cloud.tencent.com/vod/media)."
      },
      {
        "name": "MediaProcessTask",
        "desc": "Parameter of video processing task."
      },
      {
        "name": "AiContentReviewTask",
        "desc": "Type parameter of video content audit task."
      },
      {
        "name": "AiAnalysisTask",
        "desc": "Video content analysis task parameter."
      },
      {
        "name": "AiRecognitionTask",
        "desc": "Type parameter of video content recognition task."
      },
      {
        "name": "TasksPriority",
        "desc": "Task flow priority. The higher the value, the higher the priority. Value range: -10-10. If this parameter is left empty, 0 will be used."
      },
      {
        "name": "TasksNotifyMode",
        "desc": "Notification mode for task flow status change. Valid values: Finish, Change, None. If this parameter is left empty, `Finish` will be used."
      },
      {
        "name": "SessionContext",
        "desc": "The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters."
      },
      {
        "name": "SessionId",
        "desc": "The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or a blank string is entered, no deduplication will be performed."
      },
      {
        "name": "ExtInfo",
        "desc": "Reserved field for special purposes."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to initiate a processing task for an audio/video media file in VOD, including:\n1. Video transcoding (with watermark);\n2. Animated image generating;\n3. Time point screencapturing;\n4. Sampled screencapturing;\n5. Image sprite generating;\n6. Cover generating by screencapturing;\n7. Adaptive bitrate streaming (with encryption);\n8. Intelligent content audit (detection of porn, terrorism, and politically sensitive information);\n9. Intelligent content analysis (tag, category, cover, and frame-specific tag);\n10. Intelligent content recognition (opening and closing credits, face, full text, text keyword, full speech, speech keyword, and object)."
  },
  "CreateAIRecognitionTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Video content recognition template name. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Description of video content recognition template. Length limit: 256 characters."
      },
      {
        "name": "HeadTailConfigure",
        "desc": "Control parameter of video opening and ending credits recognition."
      },
      {
        "name": "SegmentConfigure",
        "desc": "Control parameter of video splitting recognition."
      },
      {
        "name": "FaceConfigure",
        "desc": "Control parameter of face recognition."
      },
      {
        "name": "OcrFullTextConfigure",
        "desc": "Control parameter of full text recognition."
      },
      {
        "name": "OcrWordsConfigure",
        "desc": "Control parameter of text keyword recognition."
      },
      {
        "name": "AsrFullTextConfigure",
        "desc": "Control parameter of full speech recognition."
      },
      {
        "name": "AsrWordsConfigure",
        "desc": "Control parameter of speech keyword recognition."
      },
      {
        "name": "ObjectConfigure",
        "desc": "Control parameter of object recognition."
      },
      {
        "name": "ScreenshotInterval",
        "desc": "Frame capturing interval in seconds. If this parameter is left empty, 1 second will be used by default. Minimum value: 0.5 seconds."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to create a custom video content recognition template. Up to 50 templates can be created."
  },
  "ModifyMediaInfo": {
    "params": [
      {
        "name": "FileId",
        "desc": "Unique media file ID."
      },
      {
        "name": "Name",
        "desc": "Media filename, which can contain up to 64 characters."
      },
      {
        "name": "Description",
        "desc": "Media file description, which can contain up to 128 characters."
      },
      {
        "name": "ClassId",
        "desc": "Media file category ID."
      },
      {
        "name": "ExpireTime",
        "desc": "Media file expiration time in [ISO date format](https://cloud.tencent.com/document/product/266/11732#I). The value `9999-12-31T23:59:59Z` indicates that the media file never expires. After the expiration, the media file and its related resources (such as transcoding results and image sprites) will be permanently deleted."
      },
      {
        "name": "CoverData",
        "desc": "String generated by [Base64-encoding](https://tools.ietf.org/html/rfc4648) the video cover image file (such as .jpeg or .png file). Only .gif, .jpeg, and .png image formats are supported."
      },
      {
        "name": "AddKeyFrameDescs",
        "desc": "Set of video timestamps to be added. If a timestamp already exists at an offset time point, it will be overwritten. Up to 100 timestamps can be added to one media file. In the same request, the time offset parameters of `AddKeyFrameDescs` must be different from those of `DeleteKeyFrameDescs`."
      },
      {
        "name": "DeleteKeyFrameDescs",
        "desc": "Time offset of the set of video timestamps to be deleted in seconds. In the same request, the time offset parameters of `AddKeyFrameDescs` must be different from those of `DeleteKeyFrameDescs`."
      },
      {
        "name": "ClearKeyFrameDescs",
        "desc": "The value `1` indicates to delete all timestamps in the video. Other values are meaningless.\nIn the same request, `ClearKeyFrameDescs` and `AddKeyFrameDescs` cannot be present at the same time."
      },
      {
        "name": "AddTags",
        "desc": "Set of tags to be added. Up to 16 tags can be added to one media file, and one tag can contain up to 16 characters. In the same request, the parameters of `AddTags` must be different from those of `DeleteTags`."
      },
      {
        "name": "DeleteTags",
        "desc": "Set of tags to be deleted. In the same request, the parameters of `AddTags` must be different from those of `DeleteTags`."
      },
      {
        "name": "ClearTags",
        "desc": "The value `1` indicates to delete all tags of the media file. Other values are meaningless.\nIn the same request, `ClearTags` and `AddTags` cannot be present at the same time."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to modify the attributes of a media file, including category, name, description, tag, expiration time, timestamp information, and video cover."
  },
  "DeleteImageSpriteTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of an image sprite generating template."
      },
      {
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to delete an image sprite generating template."
  }
}