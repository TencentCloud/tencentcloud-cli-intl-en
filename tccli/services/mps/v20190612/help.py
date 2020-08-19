# -*- coding: utf-8 -*-
DESC = "mps-2019-06-12"
INFO = {
  "CreateSnapshotByTimeOffsetTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Name of a time point screencapturing template. Length limit: 64 characters."
      },
      {
        "name": "Width",
        "desc": "Image width in px. Value range: [128, 4,096]."
      },
      {
        "name": "Height",
        "desc": "Image height in px. Value range: [128, 4,096]."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": ""
      },
      {
        "name": "Format",
        "desc": "Image format. Valid values: jpg; png. Default value: jpg."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "FillType",
        "desc": ""
      }
    ],
    "desc": "This API is used to create a custom time point screencapturing template. Up to 16 templates can be created."
  },
  "DeleteSampleSnapshotTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a sampled screencapturing template."
      }
    ],
    "desc": "This API is used to delete a custom sampled screencapturing template."
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
        "desc": "Maximum value of the height (or short side) of a video stream in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": ""
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
      }
    ],
    "desc": "This API is used to create a custom animated image generating template. Up to 16 templates can be created."
  },
  "DescribeAdaptiveDynamicStreamingTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of adaptive bitrate streaming templates. Array length limit: 100."
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
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: preset template;</li>\n<li>Custom: custom template.</li>"
      }
    ],
    "desc": "This API is used to query the list of adaptive bitrate streaming templates and supports paginated queries by filters."
  },
  "CreateContentReviewTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Name of a content audit template. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Description of a content audit template. Length limit: 256 characters."
      },
      {
        "name": "PornConfigure",
        "desc": "Porn information detection control parameter."
      },
      {
        "name": "TerrorismConfigure",
        "desc": "Terrorism information detection control parameter."
      },
      {
        "name": "PoliticalConfigure",
        "desc": "Politically sensitive information detection control parameter."
      },
      {
        "name": "ProhibitedConfigure",
        "desc": ""
      },
      {
        "name": "UserDefineConfigure",
        "desc": "Custom content audit control parameter."
      }
    ],
    "desc": "This API is used to create a custom content audit template. Up to 50 templates can be created."
  },
  "CreateSampleSnapshotTemplate": {
    "params": [
      {
        "name": "SampleType",
        "desc": "Sampled screencapturing type. Valid values:\n<li>Percent: By percent.</li>\n<li>Time: By time interval.</li>"
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
        "desc": "Image width in px. Value range: [128, 4,096]."
      },
      {
        "name": "Height",
        "desc": "Image height in px. Value range: [128, 4,096]."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": ""
      },
      {
        "name": "Format",
        "desc": "Image format. Valid values: jpg; png. Default value: jpg."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "FillType",
        "desc": ""
      }
    ],
    "desc": "This API is used to create a custom sampled screencapturing template. Up to 16 templates can be created."
  },
  "EditMedia": {
    "params": [
      {
        "name": "FileInfos",
        "desc": "Information of input video file."
      },
      {
        "name": "OutputStorage",
        "desc": "Target storage of video processing output file."
      },
      {
        "name": "OutputObjectPath",
        "desc": "Target path of video processing output file."
      },
      {
        "name": "TaskNotifyConfig",
        "desc": "Event notification information of task. If this parameter is left empty, no event notifications will be obtained."
      },
      {
        "name": "TasksPriority",
        "desc": "Task priority. The higher the value, the higher the priority. Value range: -10–10. If this parameter is left empty, 0 will be used."
      },
      {
        "name": "SessionId",
        "desc": "The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or a blank string is entered, no deduplication will be performed."
      },
      {
        "name": "SessionContext",
        "desc": "The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters."
      }
    ],
    "desc": "This API is used to edit a video (by clipping, splicing, etc.) to generate a new VOD video. Editing features include:\n\n1. Clipping a file to generate a new video;\n2. Splicing multiple files to generate a new video;\n3. Clipping multiple files and then splicing the clips to generate a new video."
  },
  "DeleteAIAnalysisTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of video content analysis template."
      }
    ],
    "desc": "This API is used to delete a custom content analysis template.\n\nNote: templates with an ID below 10000 are preset and cannot be deleted."
  },
  "DeletePersonSample": {
    "params": [
      {
        "name": "PersonId",
        "desc": "Figure ID."
      }
    ],
    "desc": "This API is used to delete a figure sample based on figure ID."
  },
  "DescribeSnapshotByTimeOffsetTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of time point screencapturing templates. Array length limit: 100."
      },
      {
        "name": "Offset",
        "desc": "Paging offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: Preset template;</li>\n<li>Custom: Custom template.</li>"
      }
    ],
    "desc": "This API is used to query the list of time point screencapturing templates and supports paged queries by filters."
  },
  "DeleteTranscodeTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a transcoding template."
      }
    ],
    "desc": "This API is used to delete a custom transcoding template."
  },
  "ModifyTranscodeTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a transcoding template."
      },
      {
        "name": "Container",
        "desc": "Container format. Valid values: mp4; flv; hls; mp3; flac; ogg; m4a. Among them, mp3, flac, ogg, and m4a are for audio files."
      },
      {
        "name": "Name",
        "desc": "Name of a transcoding template. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "RemoveVideo",
        "desc": "Whether to remove video data. Valid values:\n<li>0: Retain</li>\n<li>1: Remove</li>"
      },
      {
        "name": "RemoveAudio",
        "desc": "Whether to remove audio data. Valid values:\n<li>0: Retain</li>\n<li>1: Remove</li>"
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
        "desc": "TESHD transcoding parameter. To enable it, please contact your Tencent Cloud sales rep."
      }
    ],
    "desc": "This API is used to modify a custom transcoding template."
  },
  "DeleteAnimatedGraphicsTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of an animated image generating template."
      }
    ],
    "desc": "This API is used to delete a custom animated image generating template."
  },
  "DescribeAIAnalysisTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of video content analysis templates. Array length limit: 10."
      },
      {
        "name": "Offset",
        "desc": "Pagination offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      }
    ],
    "desc": "This API is used to get the list of content analysis templates based on unique template ID. The returned result includes all eligible custom and preset video content analysis templates."
  },
  "DescribeTaskDetail": {
    "params": [
      {
        "name": "TaskId",
        "desc": "Video processing task ID."
      }
    ],
    "desc": "This API is used to query the details of execution status and result of a task submitted in the last 3 days by task ID."
  },
  "ModifyAIRecognitionTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a video content recognition template."
      },
      {
        "name": "Name",
        "desc": "Name of a video content recognition template. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Description of a video content recognition template. Length limit: 256 characters."
      },
      {
        "name": "FaceConfigure",
        "desc": "Face recognition control parameter."
      },
      {
        "name": "OcrFullTextConfigure",
        "desc": "Full text recognition control parameter."
      },
      {
        "name": "OcrWordsConfigure",
        "desc": "Text keyword recognition control parameter."
      },
      {
        "name": "AsrFullTextConfigure",
        "desc": "Full speech recognition control parameter."
      },
      {
        "name": "AsrWordsConfigure",
        "desc": "Speech keyword recognition control parameter."
      }
    ],
    "desc": "This API is used to modify a custom content recognition template."
  },
  "ModifyAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of an adaptive bitrate streaming template."
      },
      {
        "name": "Name",
        "desc": "Template name. Length limit: 64 characters."
      },
      {
        "name": "Format",
        "desc": "Adaptive bitrate streaming format. Valid values:\n<li>HLS,</li>\n<li>MPEG-DASH.</li>"
      },
      {
        "name": "DisableHigherVideoBitrate",
        "desc": "Whether to prohibit transcoding from low bitrate to high bitrate. Valid values:\n<li>0: no,</li>\n<li>1: yes.</li>"
      },
      {
        "name": "DisableHigherVideoResolution",
        "desc": "Whether to prohibit transcoding from low resolution to high resolution. Valid values:\n<li>0: no,</li>\n<li>1: yes.</li>"
      },
      {
        "name": "StreamInfos",
        "desc": "Parameter information of input streams for transcoding to adaptive bitrate streaming. Up to 10 streams can be input.\nNote: the frame rate of each stream must be consistent; otherwise, the frame rate of the first stream is used as the output frame rate."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      }
    ],
    "desc": "This API is used to modify an adaptive bitrate streaming template."
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
        "desc": "Image width in px. Value range: [128, 4,096]."
      },
      {
        "name": "Height",
        "desc": "Image height in px. Value range: [128, 4,096]."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": ""
      },
      {
        "name": "SampleType",
        "desc": "Sampled screencapturing type. Valid values:\n<li>Percent: By percent.</li>\n<li>Time: By time interval.</li>"
      },
      {
        "name": "SampleInterval",
        "desc": "Sampling interval.\n<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>\n<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>"
      },
      {
        "name": "Format",
        "desc": "Image format. Valid values: jpg; png."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "FillType",
        "desc": ""
      }
    ],
    "desc": "This API is used to modify a custom sampled screencapturing template."
  },
  "DeleteWatermarkTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a watermarking template."
      }
    ],
    "desc": "This API is used to delete a custom watermarking template."
  },
  "DescribeWorkflows": {
    "params": [
      {
        "name": "WorkflowIds",
        "desc": "Workflow ID filter. Array length limit: 100."
      },
      {
        "name": "Status",
        "desc": "Workflow status. Valid values:\n<li>Enabled: Enabled,</li>\n<li>Disabled: Disabled.</li>\nIf this parameter is left empty, the workflow status will not be distinguished."
      },
      {
        "name": "Offset",
        "desc": "Paging offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      }
    ],
    "desc": "This API is used to get the list of workflow details by workflow ID."
  },
  "ResetWorkflow": {
    "params": [
      {
        "name": "WorkflowId",
        "desc": "Workflow ID."
      },
      {
        "name": "WorkflowName",
        "desc": "Workflow name of up to 128 characters, which must be unique for the same user."
      },
      {
        "name": "Trigger",
        "desc": "Triggering rule bound to a workflow. If an uploaded video hits the rule for the object, the workflow will be triggered."
      },
      {
        "name": "OutputStorage",
        "desc": "Output configuration of a video processing output file. If this parameter is left empty, the storage location in `Trigger` will be inherited."
      },
      {
        "name": "OutputDir",
        "desc": "Target directory of a video processing output file, such as `/movie/201907/`. If this parameter is left empty, the file will be outputted to the same directory where the source file is located, i.e.; `{inputDir}`."
      },
      {
        "name": "MediaProcessTask",
        "desc": "Parameter of a video processing task."
      },
      {
        "name": "AiContentReviewTask",
        "desc": "Type parameter of a video content audit task."
      },
      {
        "name": "AiAnalysisTask",
        "desc": ""
      },
      {
        "name": "AiRecognitionTask",
        "desc": "Type parameter of a video content recognition task."
      },
      {
        "name": "TaskPriority",
        "desc": "Workflow priority. The higher the value, the higher the priority. Value range: [-10, 10]. If this parameter is left empty, 0 will be used."
      },
      {
        "name": "TaskNotifyConfig",
        "desc": "Event notification information of a task. If this parameter is left empty, no event notifications will be obtained."
      }
    ],
    "desc": "This API is used to reset an existing workflow that is disabled."
  },
  "ParseLiveStreamProcessNotification": {
    "params": [
      {
        "name": "Content",
        "desc": "Live stream event notification obtained from CMQ."
      }
    ],
    "desc": "This API is used to parse the content of an MPS live stream processing event notification from the `msgBody` field in the message received from CMQ.\nInstead of initiating a video processing task, this API is used to help generate SDKs for various programming languages. You can parse the event notification based on the analytic function of the SDKs."
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
        "desc": "Maximum value of the height (or short side) of a video stream in px. Value range: 0 and [128, 4,096].\n<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>\n<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>\n<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>\n<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\nDefault value: 0."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": ""
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
      }
    ],
    "desc": "This API is used to modify a custom animated image generating template."
  },
  "DescribeWordSamples": {
    "params": [
      {
        "name": "Usages",
        "desc": "<b>Keyword use case filter. Valid values:</b>\n1. Recognition.Ocr: OCR-based content recognition;\n2. Recognition.Asr: ASR-based content recognition;\n3. Review.Ocr: OCR-based content audit;\n4. Review.Asr: ASR-based content audit;\n<b>These values can be merged as follows:</b>\n5. Recognition: ASR-based and OCR-based content recognition, which is equivalent to 1+2 above;\n6. Review: ASR-based and OCR-based content audit, which is equivalent to 3+4 above;\nMultiple elements can be selected, and the relationship between them is \"or\", i.e., any keyword use case that contains any element in this field set will be deemed eligible."
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
        "desc": "Paging offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 100. Maximum value: 100."
      }
    ],
    "desc": "This API is used to perform paged queries of keyword sample information by use case, keyword, and tag."
  },
  "ModifyWatermarkTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a watermarking template."
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
        "desc": "Origin position. Valid values:\n<li>TopLeft: The origin of coordinates is in the top-left corner of the video, and the origin of the watermark is in the top-left corner of the image or text;</li>\n<li>TopRight: The origin of coordinates is in the top-right corner of the video, and the origin of the watermark is in the top-right corner of the image or text;</li>\n<li>BottomLeft: The origin of coordinates is in the bottom-left corner of the video, and the origin of the watermark is in the bottom-left corner of the image or text;</li>\n<li>BottomRight: The origin of coordinates is in the bottom-right corner of the video, and the origin of the watermark is in the bottom-right corner of the image or text.</li>"
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
        "desc": "SVG watermarking template. This field is required when `Type` is `svg` and is invalid when `Type` is `image` or `text`."
      }
    ],
    "desc": "This API is used to modify a custom watermarking template. The watermark type cannot be modified."
  },
  "DeleteWordSamples": {
    "params": [
      {
        "name": "Keywords",
        "desc": "Keyword. Array length limit: 100 words."
      }
    ],
    "desc": "This API is used to delete keyword samples in batches."
  },
  "DeleteWorkflow": {
    "params": [
      {
        "name": "WorkflowId",
        "desc": "Workflow ID."
      }
    ],
    "desc": "This API is used to delete a workflow. An enabled workflow must be disabled before it can be deleted."
  },
  "DeleteAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of an adaptive bitrate streaming template."
      }
    ],
    "desc": "This API is used to delete an adaptive bitrate streaming template."
  },
  "CreateAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Format",
        "desc": "Adaptive bitrate streaming format. Valid values:\n<li>HLS,</li>\n<li>MPEG-DASH.</li>"
      },
      {
        "name": "StreamInfos",
        "desc": "Parameter information of output substreams for transcoding to adaptive bitrate streaming. Up to 10 substreams can be output.\nNote: the frame rate of each substream must be consistent; otherwise, the frame rate of the first substream is used as the output frame rate."
      },
      {
        "name": "Name",
        "desc": "Template name. Length limit: 64 characters."
      },
      {
        "name": "DisableHigherVideoBitrate",
        "desc": "Whether to prohibit transcoding from low bitrate to high bitrate. Valid values:\n<li>0: no,</li>\n<li>1: yes.</li>\nDefault value: 0."
      },
      {
        "name": "DisableHigherVideoResolution",
        "desc": "Whether to prohibit transcoding from low resolution to high resolution. Valid values:\n<li>0: no,</li>\n<li>1: yes.</li>\nDefault value: 0."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      }
    ],
    "desc": "This API is used to create an adaptive bitrate streaming template. Up up to 100 such templates can be created."
  },
  "DisableWorkflow": {
    "params": [
      {
        "name": "WorkflowId",
        "desc": "Workflow ID."
      }
    ],
    "desc": "This API is used to disable a workflow."
  },
  "DescribeSampleSnapshotTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of sampled screencapturing templates. Array length limit: 100."
      },
      {
        "name": "Offset",
        "desc": "Paging offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: Preset template;</li>\n<li>Custom: Custom template.</li>"
      }
    ],
    "desc": "This API is used to query the list of sampled screencapturing templates and supports paged queries by filters."
  },
  "CreateWatermarkTemplate": {
    "params": [
      {
        "name": "Type",
        "desc": "Watermarking type. Valid values:\n<li>image: Image watermark;</li>\n<li>text: Text watermark;</li>\n<li>svg: SVG watermark.</li>"
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
        "desc": "Origin position. Valid values:\n<li>TopLeft: The origin of coordinates is in the top-left corner of the video, and the origin of the watermark is in the top-left corner of the image or text;</li>\n<li>TopRight: The origin of coordinates is in the top-right corner of the video, and the origin of the watermark is in the top-right corner of the image or text;</li>\n<li>BottomLeft: The origin of coordinates is in the bottom-left corner of the video, and the origin of the watermark is in the bottom-left corner of the image or text;</li>\n<li>BottomRight: The origin of coordinates is in the bottom-right corner of the video, and the origin of the watermark is in the bottom-right corner of the image or text.</li>\nDefault value: TopLeft."
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
        "desc": "Image watermarking template. This field is required and valid only when `Type` is `image`."
      },
      {
        "name": "TextTemplate",
        "desc": "Text watermarking template. This field is required and valid only when `Type` is `text`."
      },
      {
        "name": "SvgTemplate",
        "desc": "SVG watermarking template. This field is required and valid only when `Type` is `svg`."
      }
    ],
    "desc": "This API is used to create a custom watermarking template. Up to 1,000 templates can be created."
  },
  "DescribePersonSamples": {
    "params": [
      {
        "name": "Type",
        "desc": "Pulled figure type. Valid values:\n<li>UserDefine: Custom figure library;</li>\n<li>Default: Default figure library.</li>\n\nDefault value: UserDefine (the custom figure library will be pulled.)\nNote: The default figure library can be pulled only through \"figure name\" or \"figure ID + figure name\", and only one face image will be returned."
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
        "desc": "Paging offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 100. Maximum value: 100."
      }
    ],
    "desc": "This API is used to query the information of figure samples and supports paged queries by figure ID, name, and tag."
  },
  "ParseNotification": {
    "params": [
      {
        "name": "Content",
        "desc": "Event notification obtained from CMQ."
      }
    ],
    "desc": "This API is used to parse the content of an MPS event notification from the `msgBody` field in the message received from CMQ.\nInstead of initiating a video processing task, this API is used to help generate SDKs for various programming languages. You can parse the event notification based on the analytic function of the SDKs."
  },
  "DeleteAIRecognitionTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a video content recognition template."
      }
    ],
    "desc": "This API is used to delete a custom content recognition template."
  },
  "DeleteSnapshotByTimeOffsetTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a time point screencapturing template."
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
        "desc": "Paging offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: Preset template;</li>\n<li>Custom: Custom template.</li>"
      }
    ],
    "desc": "This API is used to query the list of animated image generating templates and supports paged queries by filters."
  },
  "EnableWorkflow": {
    "params": [
      {
        "name": "WorkflowId",
        "desc": "Workflow ID."
      }
    ],
    "desc": "This API is used to enable a workflow."
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
      }
    ],
    "desc": "This API is used to create a custom content analysis template. Up to 50 templates can be created."
  },
  "ManageTask": {
    "params": [
      {
        "name": "OperationType",
        "desc": "Operation type. Valid values:\n<li>Abort: terminates task.</li>"
      },
      {
        "name": "TaskId",
        "desc": "Video processing task ID."
      }
    ],
    "desc": "This API is used to manage an initiated task.\n> Note: currently, you can only terminate an ongoing live stream processing task."
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
      }
    ],
    "desc": "This API is used to modify a custom content analysis template.\n\nNote: templates with an ID below 10000 are preset and cannot be modified."
  },
  "DescribeMediaMetaData": {
    "params": [
      {
        "name": "InputInfo",
        "desc": "Input information of file for metadata getting."
      }
    ],
    "desc": "This API is used to get the metadata of media, such as video image width/height, codec, length, and frame rate."
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "Status",
        "desc": "Filter: Task status. Valid values: WAITING (waiting), PROCESSING (processing), FINISH (completed)."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "ScrollToken",
        "desc": "Scrolling identifier which is used for pulling in batches. If a single request cannot pull all the data entries, the API will return `ScrollToken`, and if the next request carries it, the next pull will start from the next entry."
      }
    ],
    "desc": "* This API is used to query the task list;\n* If there are many data entries in the list, one single call of the API may not be able to pull the entire list. The `ScrollToken` parameter can be used to pull the list in batches;\n* Only tasks in the last three days (72 hours) can be queried."
  },
  "CreateTranscodeTemplate": {
    "params": [
      {
        "name": "Container",
        "desc": "Container format. Valid values: mp4; flv; hls; mp3; flac; ogg; m4a. Among them, mp3, flac, ogg, and m4a are for audio files."
      },
      {
        "name": "Name",
        "desc": "Name of a transcoding template. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Template description. Length limit: 256 characters."
      },
      {
        "name": "RemoveVideo",
        "desc": "Whether to remove video data. Valid values:\n<li>0: Retain</li>\n<li>1: Remove</li>\nDefault value: 0."
      },
      {
        "name": "RemoveAudio",
        "desc": "Whether to remove audio data. Valid values:\n<li>0: Retain</li>\n<li>1: Remove</li>\nDefault value: 0."
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
        "desc": "TESHD transcoding parameter. To enable it, please contact your Tencent Cloud sales rep."
      }
    ],
    "desc": "This API is used to create a custom transcoding template. Up to 1,000 templates can be created."
  },
  "ModifySnapshotByTimeOffsetTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a time point screencapturing template."
      },
      {
        "name": "Name",
        "desc": "Name of a time point screencapturing template. Length limit: 64 characters."
      },
      {
        "name": "Width",
        "desc": "Image width in px. Value range: [128, 4,096]."
      },
      {
        "name": "Height",
        "desc": "Image height in px. Value range: [128, 4,096]."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": ""
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
        "name": "FillType",
        "desc": ""
      }
    ],
    "desc": "This API is used to modify a custom time point screencapturing template."
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
        "desc": "Figure sample use case. Valid values:\n1. Recognition: It is used for content recognition, equivalent to `Recognition.Face`.\n2. Review: It is used for content audit, equivalent to `Review.Face`.\n3. All: It is used for content recognition and content audit, equivalent to 1+2 above."
      },
      {
        "name": "FaceOperationInfo",
        "desc": "Face operation information."
      },
      {
        "name": "TagOperationInfo",
        "desc": "Tag operation information."
      }
    ],
    "desc": "This API is used to modify figure sample information based on figure ID, such as modifying the name and description and adding/deleting/resetting a face or tag. There should be at least one image left after the face deletion operation; otherwise, please use the reset operation."
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
      }
    ],
    "desc": "This API is used to create keyword samples in batches for video processing operations such as content recognition and audit using the OCR and ASR technologies."
  },
  "CreateWorkflow": {
    "params": [
      {
        "name": "WorkflowName",
        "desc": "Workflow name of up to 128 characters, which must be unique for the same user."
      },
      {
        "name": "Trigger",
        "desc": "Triggering rule bound to a workflow. If an uploaded video hits the rule for the object, the workflow will be triggered."
      },
      {
        "name": "OutputStorage",
        "desc": "Storage location of a video processing output file. If this parameter is left empty, the storage location in `Trigger` will be inherited."
      },
      {
        "name": "OutputDir",
        "desc": "Target directory of a video processing output file, such as `/movie/201907/`. If this parameter is left empty, the file will be outputted to the same directory where the source file is located."
      },
      {
        "name": "MediaProcessTask",
        "desc": "Parameter of a video processing task."
      },
      {
        "name": "AiContentReviewTask",
        "desc": "Type parameter of a video content audit task."
      },
      {
        "name": "AiAnalysisTask",
        "desc": ""
      },
      {
        "name": "AiRecognitionTask",
        "desc": "Type parameter of a video content recognition task."
      },
      {
        "name": "TaskNotifyConfig",
        "desc": "Event notification configuration for a task. If this parameter is left empty, no event notifications will be obtained."
      },
      {
        "name": "TaskPriority",
        "desc": "Workflow priority. The higher the value, the higher the priority. Value range: [-10, 10]. If this parameter is left empty, 0 will be used."
      }
    ],
    "desc": "This API is used to set a processing rule for media files uploaded to the specified directory of a COS bucket, including:\n1. Video transcoding (with watermark);\n2. Animated image generating;\n3. Time point screencapturing;\n4. Sampled screencapturing;\n5. Image sprite generating;\n6. Video conversion to adaptive bitrate streaming;\n7. Intelligent content audit (detection of porn, terrorism, and politically sensitive information);\n8. Intelligent content recognition (face recognition, full text recognition, text keyword recognition, full speech recognition, and speech keyword recognition).\n\nNote: Once successfully created, a workflow is disabled by default and needs to be enabled manually."
  },
  "ProcessLiveStream": {
    "params": [
      {
        "name": "Url",
        "desc": "Live stream URL, which must be a live stream file address. RTMP, HLS, and FLV are supported."
      },
      {
        "name": "TaskNotifyConfig",
        "desc": "Event notification information of a task, which is used to specify the live stream processing result."
      },
      {
        "name": "OutputStorage",
        "desc": "Target bucket of a live stream processing output file. This parameter is required if a file will be output."
      },
      {
        "name": "OutputDir",
        "desc": "Target directory of a live stream processing output file, such as `/movie/201909/`. If this parameter is left empty, the `/` directory will be used."
      },
      {
        "name": "AiContentReviewTask",
        "desc": "Type parameter of a video content audit task."
      },
      {
        "name": "AiRecognitionTask",
        "desc": ""
      },
      {
        "name": "SessionId",
        "desc": "The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or an empty string is entered, no deduplication will be performed."
      },
      {
        "name": "SessionContext",
        "desc": "The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters."
      }
    ],
    "desc": "This API is used to initiate a processing task for a live streaming media file, including:\n\n* Intelligent content audit (detection of porn, terrorism, and politically sensitive information in image and porn information in speech);\n\nThe live stream processing event notification is written into the specified CMQ queue in real time. You need to obtain the event notification result from CMQ. If a file is output during video processing, it will be written into the specified target bucket."
  },
  "ModifyContentReviewTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a content audit template."
      },
      {
        "name": "Name",
        "desc": "Name of a content audit template. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Description of a content audit template. Length limit: 256 characters."
      },
      {
        "name": "PornConfigure",
        "desc": "Porn information detection control parameter."
      },
      {
        "name": "TerrorismConfigure",
        "desc": "Terrorism information detection control parameter."
      },
      {
        "name": "PoliticalConfigure",
        "desc": "Politically sensitive information detection control parameter."
      },
      {
        "name": "ProhibitedConfigure",
        "desc": ""
      },
      {
        "name": "UserDefineConfigure",
        "desc": "Custom content audit control parameter."
      }
    ],
    "desc": "This API is used to modify a custom content audit template."
  },
  "ProcessMedia": {
    "params": [
      {
        "name": "InputInfo",
        "desc": "Input information of a file for video processing."
      },
      {
        "name": "OutputStorage",
        "desc": "Target bucket of a video processing output file. If this parameter is left empty, the storage location in `InputInfo` will be inherited."
      },
      {
        "name": "OutputDir",
        "desc": "Target directory of a video processing output file, such as `/movie/201907/`. If this parameter is left empty, the file will be outputted to the same directory as that in `InputInfo`."
      },
      {
        "name": "MediaProcessTask",
        "desc": "Parameter of a video processing task."
      },
      {
        "name": "AiContentReviewTask",
        "desc": "Type parameter of a video content audit task."
      },
      {
        "name": "AiAnalysisTask",
        "desc": ""
      },
      {
        "name": "AiRecognitionTask",
        "desc": "Type parameter of a video content recognition task."
      },
      {
        "name": "TaskNotifyConfig",
        "desc": "Event notification information of a task. If this parameter is left empty, no event notifications will be obtained."
      },
      {
        "name": "TasksPriority",
        "desc": "Task flow priority. The higher the value, the higher the priority. Value range: [-10, 10]. If this parameter is left empty, 0 will be used."
      },
      {
        "name": "SessionId",
        "desc": "The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or an empty string is entered, no deduplication will be performed."
      },
      {
        "name": "SessionContext",
        "desc": "The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters."
      }
    ],
    "desc": "This API is used to initiate a processing task for media files in COS, including:\n1. Video transcoding (with watermark);\n2. Animated image generating;\n3. Time point screencapturing;\n4. Sampled screencapturing;\n5. Image sprite generating;\n6. Video conversion to adaptive bitrate streaming;\n7. Intelligent content audit (detection of porn, terrorism, and politically sensitive information);\n8. Intelligent content recognition (face recognition, full text recognition, text keyword recognition, full speech recognition, and speech keyword recognition)."
  },
  "CreateAIRecognitionTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "Name of a video content recognition template. Length limit: 64 characters."
      },
      {
        "name": "Comment",
        "desc": "Description of a video content recognition template. Length limit: 256 characters."
      },
      {
        "name": "FaceConfigure",
        "desc": "Face recognition control parameter."
      },
      {
        "name": "OcrFullTextConfigure",
        "desc": "Full text recognition control parameter."
      },
      {
        "name": "OcrWordsConfigure",
        "desc": "Text keyword recognition control parameter."
      },
      {
        "name": "AsrFullTextConfigure",
        "desc": "Full speech recognition control parameter."
      },
      {
        "name": "AsrWordsConfigure",
        "desc": "Speech keyword recognition control parameter."
      }
    ],
    "desc": "This API is used to create a custom content recognition template. Up to 50 templates can be created."
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
        "desc": ""
      },
      {
        "name": "SampleType",
        "desc": "Sampling type. Valid values:\n<li>Percent: By percent.</li>\n<li>Time: By time interval.</li>"
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
        "desc": ""
      },
      {
        "name": "Comment",
        "desc": ""
      }
    ],
    "desc": "This API is used to modify a custom image sprite generating template."
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
        "desc": "Paging offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: Preset template;</li>\n<li>Custom: Custom template.</li>"
      }
    ],
    "desc": "This API is used to query the list of image sprite generating templates and supports paged queries by filters."
  },
  "DeleteContentReviewTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of a content audit template."
      }
    ],
    "desc": "This API is used to delete a custom content audit template."
  },
  "CreatePersonSample": {
    "params": [
      {
        "name": "Name",
        "desc": "Name of a figure. Length limit: 20 characters."
      },
      {
        "name": "Usages",
        "desc": "Figure sample use case. Valid values:\n1. Recognition: It is used for content recognition, equivalent to `Recognition.Face`.\n2. Review: It is used for content audit, equivalent to `Review.Face`.\n3. All: It is used for content recognition and content audit, equivalent to 1+2 above."
      },
      {
        "name": "Description",
        "desc": "Figure description. Length limit: 1,024 characters."
      },
      {
        "name": "FaceContents",
        "desc": "String generated by [Base64-encoding](https://tools.ietf.org/html/rfc4648) a face image. Only JPEG and PNG images are supported. Array length limit: 5 images.\nNote: The image must be a relatively clear full-face photo of a figure in at least 200 * 200 px."
      },
      {
        "name": "Tags",
        "desc": "Figure tag\n<li>Array length limit: 20 tags;</li>\n<li>Tag length limit: 128 characters.</li>"
      }
    ],
    "desc": "This API is used to create a figure sample for video processing operations such as content recognition and audit using the face recognition technology."
  },
  "DescribeAIRecognitionTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of video content recognition templates. Array length limit: 10."
      },
      {
        "name": "Offset",
        "desc": "Paging offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 50."
      }
    ],
    "desc": "This API is used to get the list of content recognition templates based on unique template ID. The return result includes all eligible custom and preset content recognition templates."
  },
  "DescribeWatermarkTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of watermarking templates. Array length limit: 100."
      },
      {
        "name": "Type",
        "desc": "Watermark type filter. Valid values:\n<li>image: Image watermark;</li>\n<li>text: Text watermark.</li>"
      },
      {
        "name": "Offset",
        "desc": "Paging offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries\n<li>Default value: 10;</li>\n<li>Maximum value: 100.</li>"
      }
    ],
    "desc": "This API is used to query custom watermarking templates and supports paged queries by filters."
  },
  "CreateImageSpriteTemplate": {
    "params": [
      {
        "name": "SampleType",
        "desc": "Sampling type. Valid values:\n<li>Percent: By percent.</li>\n<li>Time: By time interval.</li>"
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
        "desc": "Subimage width of an image sprite in px. Value range: [128, 4,096]."
      },
      {
        "name": "Height",
        "desc": "Subimage height of an image sprite in px. Value range: [128, 4,096]."
      },
      {
        "name": "ResolutionAdaptive",
        "desc": ""
      },
      {
        "name": "FillType",
        "desc": ""
      },
      {
        "name": "Comment",
        "desc": ""
      }
    ],
    "desc": "This API is used to create a custom image sprite generating template. Up to 16 templates can be created."
  },
  "DeleteImageSpriteTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "Unique ID of an image sprite generating template."
      }
    ],
    "desc": "This API is used to delete an image sprite generating template."
  },
  "DescribeTranscodeTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of transcoding templates. Array length limit: 100."
      },
      {
        "name": "Type",
        "desc": "Template type filter. Valid values:\n<li>Preset: Preset template;</li>\n<li>Custom: Custom template.</li>"
      },
      {
        "name": "ContainerType",
        "desc": "Container format filter. Valid values:\n<li>Video: Video container format that can contain both video stream and audio stream;</li>\n<li>PureAudio: Audio container format that can contain only audio stream.</li>"
      },
      {
        "name": "TEHDType",
        "desc": "TESHD filter, which is used to filter common transcoding or ultra-fast HD transcoding templates. Valid values:\n<li>Common: Common transcoding template;</li>\n<li>TEHD: TESHD template.</li>"
      },
      {
        "name": "Offset",
        "desc": "Paging offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 100."
      }
    ],
    "desc": "This API is used to get the list of transcoding templates based on unique template ID. The return result includes all eligible custom and [preset transcoding templates](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)."
  },
  "DescribeContentReviewTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "Unique ID filter of content audit templates. Array length limit: 50."
      },
      {
        "name": "Offset",
        "desc": "Paging offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned entries. Default value: 10. Maximum value: 50."
      }
    ],
    "desc": "This API is used to get the list of content audit templates based on unique template ID. The return result includes all eligible custom and preset content audit templates."
  }
}