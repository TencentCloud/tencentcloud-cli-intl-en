# -*- coding: utf-8 -*-
DESC = "vod-2018-07-17"
INFO = {
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
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to compose a media file, including:\n\n1. Clipping a media file to generate a new media file;\n2. Clipping and splicing multiple media files to generate a new media file;\n3. Clipping and splicing the media streams of multiple media files to generate a new media file;"
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
        "desc": "Task priority. The higher the value, the higher the priority. Value range: -10–10. If this parameter is left empty, 0 will be used."
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
  "DescribeSubAppIds": {
    "params": [],
    "desc": "This API is used to get the list of subapplications to which the current account has permissions, including primary applications. If the subapplication feature has not been enabled, this API will return. \n `FailedOperation`."
  },
  "PullUpload": {
    "params": [
      {
        "name": "MediaUrl",
        "desc": "URL of the media to be pulled. Media files in HLS and Dash formats cannot be pulled currently.\nFor the supported extensions, please see [Media Types](https://cloud.tencent.com/document/product/266/9760#.E5.AA.92.E4.BD.93.E7.B1.BB.E5.9E.8B)."
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
      }
    ],
    "desc": "This API is used to pull a video on the internet to the VOD platform."
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
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "* This API is used to apply for uploading a media file (and cover file) to VOD and obtain the metadata of file storage (including upload path and upload signature) for subsequent use by the uploading API.\n* For the detailed upload process, please see [Overview of Upload from Client](/document/product/266/9759)."
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
  "DescribeAudioTrackTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of templates. Array length limit: 100."
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
    "desc": "This API is used to query the list of transcoding to adaptive bitrate streaming audio track templates and supports paged queries by filters."
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
        "desc": "Task flow priority. The higher the value, the higher the priority. Value range: -10–10. If this parameter is left empty, 0 will be used."
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
    "desc": "This API is used to initiate a processing task for an audio/video media file from a URL, including:\n\n1. Intelligent content audit (detection of porn, terrorism, and politically sensitive information);\n2. Intelligent content analysis (tag, category, cover, and frame-specific tag);\n3. Intelligent content recognition (opening and closing credits, face, full text, text keyword, full speech, speech keyword, and object)."
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
  "DescribeStorageData": {
    "params": [
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "This API is used to query the storage capacity usage and number of files."
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
    "desc": "* After a media file is forbidden, except previewing it in the VOD Console, accessing the URLs of its various resources (such as source file, output files, and screenshots) in other scenarios will return error 403.\n  It takes about 5–10 minutes for a forbidding/unblocking operation to take effect across the entire network."
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
  "CreateProcedureTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Task flow name (up to 20 characters)."
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
  "DescribeVideoTrackTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of templates. Array length limit: 100."
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
    "desc": "This API is used to query the list of transcoding to adaptive bitrate streaming video track templates and supports paged queries by filters."
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
  "ResetProcedureTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Task flow name"
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
  "CreateClass": {
    "params": [
      {
        "name": "ParentId",
        "desc": "Parent category ID. For a first-level category, enter `-1`."
      },
      {
        "name": "ClassName",
        "desc": "Category name. Length limit: 1–64 characters."
      },
      {
        "name": "SubAppId",
        "desc": "[Subapplication](/document/product/266/14574) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      }
    ],
    "desc": "* This API is used to categorize media assets for management;\n* It does not affect the categories of existing media assets. If you want to modify the category of a media asset, call the [ModifyMediaInfo](/document/product/266/31762) API.\n* There can be up to 4 levels of categories.\n* One category can have up to 500 subcategories under it."
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
        "desc": "Task flow priority. The higher the value, the higher the priority. Value range: -10–10. If this parameter is left empty, 0 will be used."
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
        "name": "SubAppId",
        "desc": "ID of a [subapplication](/document/product/266/14574) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty."
      },
      {
        "name": "FillType",
        "desc": "Fill type. \"Fill\" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:\n<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot \"shorter\" or \"longer\";</li>\n<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>\nDefault value: black."
      }
    ],
    "desc": "This API is used to modify a custom image sprite generating template."
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
      },
      {
        "name": "FillType",
        "desc": "Fill type. \"Fill\" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:\n<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot \"shorter\" or \"longer\";</li>\n<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>\nDefault value: black."
      }
    ],
    "desc": "This API is used to create a custom image sprite generating template. Up to 16 templates can be created."
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
        "desc": "Task flow priority. The higher the value, the higher the priority. Value range: -10–10. If this parameter is left empty, 0 will be used."
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
  }
}