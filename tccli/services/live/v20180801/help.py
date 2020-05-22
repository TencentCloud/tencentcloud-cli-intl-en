# -*- coding: utf-8 -*-
DESC = "live-2018-08-01"
INFO = {
  "DescribeLiveCallbackTemplates": {
    "params": [],
    "desc": "This API is used to get the callback template list."
  },
  "DescribeBillBandwidthAndFluxList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start time point in the format of `yyyy-mm-dd HH:MM:SS`."
      },
      {
        "name": "EndTime",
        "desc": "End time point in the format of `yyyy-mm-dd HH:MM:SS`. The difference between the start time and end time cannot be greater than 31 days."
      },
      {
        "name": "PlayDomains",
        "desc": "LVB playback domain name. If this parameter is left empty, full data will be queried."
      },
      {
        "name": "MainlandOrOversea",
        "desc": "Valid values:\nMainland: query data for Mainland China,\nOversea: query data for regions outside Mainland China,\nDefault: query data for all regions.\nNote: LEB only supports querying data for all regions."
      },
      {
        "name": "Granularity",
        "desc": "Data granularity. Valid values:\n5: 5-minute granularity (the query time span should be within 1 day),\n60: 1-hour granularity (the query time span should be within one month),\n1440: 1-day granularity (the query time span should be within one month).\nDefault value: 5."
      },
      {
        "name": "ServiceName",
        "desc": "Service name. Valid values: LVB, LEB. Default value: LVB."
      }
    ],
    "desc": "This API is used to query the data of billable LVB bandwidth and traffic."
  },
  "ForbidLiveDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "LVB domain name to be disabled."
      }
    ],
    "desc": "This API is used to disable an LVB domain name."
  },
  "DeleteLiveCallbackRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default."
      }
    ],
    "desc": "This API is used to delete a callback rule."
  },
  "CreateLiveTranscodeRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Playback domain name."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. If you only bind a domain name, leave this parameter empty."
      },
      {
        "name": "StreamName",
        "desc": "Stream name. If only the domain name or path is bound, leave this parameter blank."
      },
      {
        "name": "TemplateId",
        "desc": "Designates an existing template ID."
      }
    ],
    "desc": "To create a transcoding rule, you need to first call the [CreateLiveTranscodeTemplate](/document/product/267/32646) API to create a transcoding template and bind the returned template ID to the stream.\n<br>Transcoding-related document: [LVB Remuxing and Transcoding](/document/product/267/32736)."
  },
  "DescribeLiveSnapshotTemplates": {
    "params": [],
    "desc": "This API is used to get the screencapturing template list."
  },
  "DescribeConcurrentRecordStreamNum": {
    "params": [
      {
        "name": "LiveType",
        "desc": "Live streaming type. SlowLive: LCB.\nNormalLive: LVB."
      },
      {
        "name": "StartTime",
        "desc": "Start time in the format of `yyyy-mm-dd HH:MM:SS`.\nData for the last 180 days can be queried."
      },
      {
        "name": "EndTime",
        "desc": "End time in the format of `yyyy-mm-dd HH:MM:SS`.\nThe maximum time span supported is 31 days."
      },
      {
        "name": "MainlandOrOversea",
        "desc": "Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China). If this parameter is left empty, data for all regions will be queried."
      },
      {
        "name": "PushDomains",
        "desc": "Playback domain name list. If this parameter is left empty, full data will be queried."
      }
    ],
    "desc": "This API is used to query the number of concurrent recording channels, which is applicable to LCB and LVB."
  },
  "CreateLiveRecord": {
    "params": [
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default."
      },
      {
        "name": "DomainName",
        "desc": "Push domain name. This parameter must be set for multi-domain name push."
      },
      {
        "name": "StartTime",
        "desc": "Recording start time, which is China standard time and should be URL-encoded (RFC3986). For example, the encoding of 2017-01-01 10:10:01 is 2017-01-01+10%3a10%3a01.\nIn scheduled recording mode, this field must be set; in real-time video recording mode, this field is ignored."
      },
      {
        "name": "EndTime",
        "desc": "Recording end time, which is China standard time and should be URL-encoded (RFC3986). For example, the encoding of 2017-01-01 10:30:01 is 2017-01-01+10%3a30%3a01.\nIn scheduled recording mode, this field must be set; in real-time video recording mode, this field is optional. If the recording is set to real-time video recording mode through the `Highlight` parameter, the set end time should not be more than 30 minutes after the current time. If the set end time is more than 30 minutes after the current time, earlier than the current time, or left empty, the actual end time will be 30 minutes after the current time."
      },
      {
        "name": "RecordType",
        "desc": "Recording type.\n\"video\": Audio-video recording **(default)**.\n\"audio\": audio recording.\nIn both scheduled and real-time video recording modes, this parameter is valid and is not case sensitive."
      },
      {
        "name": "FileFormat",
        "desc": "Recording file format. Valid values:\n\"flv\" **(default)**, \"hls\", \"mp4\", \"aac\", \"mp3\".\nIn both scheduled and real-time video recording modes, this parameter is valid and is not case sensitive."
      },
      {
        "name": "Highlight",
        "desc": "Mark for enabling real-time video recording mode.\n0: Real-time video recording mode is not enabled, i.e., the scheduled recording mode is used **(default)**. See [Sample 1](#.E7.A4.BA.E4.BE.8B1-.E5.88.9B.E5.BB.BA.E5.AE.9A.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1).\n1: Real-time video recording mode is enabled. See [Sample 2](#.E7.A4.BA.E4.BE.8B2-.E5.88.9B.E5.BB.BA.E5.AE.9E.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1)."
      },
      {
        "name": "MixStream",
        "desc": "Flag for enabling A+B=C mixed stream recording.\n0: A+B=C mixed stream recording is not enabled **(default)**.\n1: A+B=C mixed stream recording is enabled.\nIn both scheduled and real-time video recording modes, this parameter is valid."
      },
      {
        "name": "StreamParam",
        "desc": "Recording stream parameter. The following parameters are supported currently:\nrecord_interval: recording interval in seconds. Value range: 1800-7200.\nstorage_time: recording file storage duration in seconds.\nExample: record_interval=3600&storage_time=2592000.\nNote: the parameter needs to be URL-encoded.\nIn both scheduled and real-time video recording modes, this parameter is valid."
      }
    ],
    "desc": "- Prerequisites\n  1. Recording files are stored on the VOD platform, so if you need to use the recording feature, you must first activate the VOD service.\n  2. After the recording files are stored, applicable fees (including storage fees and downstream playback traffic fees) will be charged according to the VOD billing mode. For more information, please see the [corresponding document](https://cloud.tencent.com/document/product/266/2838).\n\n- Mode description\n  This API supports two recording modes:\n  1. Scheduled recording mode **(default mode)**.\n    The start time and end time need to be passed in, and the recording task will automatically start and end based on the time parameters.\n  2. Real-time video recording mode.\n    The start time passed in will be ignored, and recording will be started immediately after the recording task is created. The recording duration can be up to 30 minutes. If the end time passed in is more than 30 minutes after the current time, it will be counted as 30 minutes. Real-time video recording is mainly used for recording highlight scenes, and you are recommended to keep the duration within 5 minutes.\n\n- Precautions\n  1. The API call timeout period should be set to more than 3 seconds; otherwise, retries and frequent calls may result in repeated recording tasks.\n  2. Subject to the audio and video file formats (FLV/MP4/HLS), the video codec of H.264 and audio codec of AAC are supported.\n  3. In order to avoid malicious or non-subjective frequent API requests, the maximum number of tasks that can be created in scheduled recording mode is limited: up to 4,000 tasks can be created per day (excluding deleted ones), and up to 400 ones can run concurrently. If you need a higher upper limit, please submit a ticket for application."
  },
  "UpdateLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "Watermark ID.\nGet the watermark ID in the returned value of the [AddLiveWatermark](/document/product/267/30154) API call."
      },
      {
        "name": "PictureUrl",
        "desc": "Watermark image URL."
      },
      {
        "name": "XPosition",
        "desc": "Display position: X-axis offset. Default value: 0."
      },
      {
        "name": "YPosition",
        "desc": "Display position: Y-axis offset. Default value: 0."
      },
      {
        "name": "WatermarkName",
        "desc": "Watermark name."
      },
      {
        "name": "Width",
        "desc": "Watermark width or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original width is used by default."
      },
      {
        "name": "Height",
        "desc": "Watermark height or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original height is used by default."
      }
    ],
    "desc": "This API is used to update a watermark."
  },
  "StopLiveRecord": {
    "params": [
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "TaskId",
        "desc": "Task ID, which uniquely identifies the recording task globally."
      }
    ],
    "desc": "Note: Recording files are stored on the VOD platform. To use the recording feature, you need to activate a VOD account and ensure that it is available. After the recording files are stored, applicable fees (including storage fees and downstream playback traffic fees) will be charged according to the VOD billing method. For more information, please see the corresponding document."
  },
  "DeleteLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "Watermark ID.\nGet the watermark ID in the returned value of the [AddLiveWatermark](/document/product/267/30154) API call."
      }
    ],
    "desc": "This API is used to delete a watermark."
  },
  "ModifyLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID."
      },
      {
        "name": "TemplateName",
        "desc": "Template name."
      },
      {
        "name": "Description",
        "desc": "Message description"
      },
      {
        "name": "FlvParam",
        "desc": "FLV recording parameter, which is set when FLV recording is enabled."
      },
      {
        "name": "HlsParam",
        "desc": "HLS recording parameter, which is set when HLS recording is enabled."
      },
      {
        "name": "Mp4Param",
        "desc": "MP4 recording parameter, which is set when MP4 recording is enabled."
      },
      {
        "name": "AacParam",
        "desc": "AAC recording parameter, which is set when AAC recording is enabled."
      },
      {
        "name": "HlsSpecialParam",
        "desc": "Custom HLS recording parameter."
      },
      {
        "name": "Mp3Param",
        "desc": "MP3 recording parameter, which is set when MP3 recording is enabled."
      }
    ],
    "desc": "This API is used to modify the recording template configuration."
  },
  "AddDelayLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default."
      },
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "DelayTime",
        "desc": "Delay time in seconds, up to 600s."
      },
      {
        "name": "ExpireTime",
        "desc": "Expiration time of the configured delayed playback in UTC format, such as 2018-11-29T19:00:00Z.\nNotes:\n1. The configuration will expire after 7 days by default and can last up to 7 days.\n2. The Beijing time is in UTC+8. This value should be in the format as required by ISO 8601. For more information, please see [ISO Date and Time Format](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)."
      }
    ],
    "desc": "This API is used to set the delay time for the stream.\nNote: If you want to set delayed playback before pushing, you need to set 5 minutes in advance.\nCurrently, this API only supports stream granularity, and the feature supporting domain name and application granularities will be available in the future.\n"
  },
  "CreateLiveWatermarkRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default."
      },
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "TemplateId",
        "desc": "Watermark ID, which is the `WatermarkId` returned by the [AddLiveWatermark](/document/product/267/30154) API."
      }
    ],
    "desc": "To create a watermarking rule, you need to first call the [AddLiveWatermark](/document/product/267/30154) API to add a watermark and bind the returned watermark ID to the stream."
  },
  "DropLiveStream": {
    "params": [
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "DomainName",
        "desc": "Your acceleration domain name."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the AppName in push and playback addresses and is \"live\" by default."
      }
    ],
    "desc": "This API is used to disconnect the push connection, which can be resumed."
  },
  "DescribeLiveStreamEventList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start time. \nIn UTC format, such as 2018-12-29T19:00:00Z.\nThis supports querying the history of 60 days."
      },
      {
        "name": "EndTime",
        "desc": "End time.\nIn UTC format, such as 2018-12-29T20:00:00Z.\nThis cannot be after the current time and cannot be more than 30 days after the start time."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the AppName in push and playback addresses and is \"live\" by default."
      },
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "StreamName",
        "desc": "Stream name; query with wildcard (*) is not supported; fuzzy match by default.\nThe IsStrict field can be used to change to exact query."
      },
      {
        "name": "PageNum",
        "desc": "Page number to get.\nDefault value: 1.\nNote: Currently, query for up to 10,000 entries is supported."
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page.\nMaximum value: 100.\nValue range: any integer between 1 and 100.\nDefault value: 10.\nNote: Currently, query for up to 10,000 entries is supported."
      },
      {
        "name": "IsFilter",
        "desc": "Whether to filter. No filtering by default.\n0: No filtering at all.\n1: Filter out the failing streams and return only the successful ones."
      },
      {
        "name": "IsStrict",
        "desc": "Whether to query exactly. Fuzzy match by default.\n0: Fuzzy match.\n1: Exact query.\nNote: This parameter takes effect when StreamName is used."
      },
      {
        "name": "IsAsc",
        "desc": "Whether to display in ascending order by end time. Descending order by default.\n0: Descending.\n1: Ascending."
      }
    ],
    "desc": "This API is used to query streaming events.<br>\n\nNote: This API can filter by IsFilter and return the push history."
  },
  "DescribeLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\nNote: get the template ID in the returned value of the [CreateLiveTranscodeTemplate](/document/product/267/32646) API call."
      }
    ],
    "desc": "This API is used to get a single transcoding template."
  },
  "CreateCommonMixStream": {
    "params": [
      {
        "name": "MixStreamSessionId",
        "desc": "ID of stream mix session (from applying for stream mix to canceling stream mix)."
      },
      {
        "name": "InputStreamList",
        "desc": "Input stream list for stream mix."
      },
      {
        "name": "OutputParams",
        "desc": "Output stream parameter for stream mix."
      },
      {
        "name": "MixStreamTemplateId",
        "desc": "Input template ID. If this parameter is set, the output will be generated according to the default template layout, and there is no need to enter the custom position parameters.\nIf this parameter is left empty, 0 will be used by default.\nFor two input sources, 10, 20, 30, 40, and 50 are supported.\nFor three input sources, 310, 390, and 391 are supported.\nFor four input sources, 410 is supported.\nFor five input sources, 510 and 590 are supported.\nFor six input sources, 610 is supported."
      },
      {
        "name": "ControlParams",
        "desc": "Special control parameter for stream mix. If there are no special needs, leave it empty."
      }
    ],
    "desc": "This API is used to create a general stream mix. It can be used basically in the same way as the legacy `mix_streamv2.cancel_mix_stream` API.\nNote: currently, up to 16 streams can be mixed."
  },
  "DeleteLiveRecord": {
    "params": [
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "TaskId",
        "desc": "Task ID, which uniquely identifies a recording task globally.\nGet the `TaskId` from the returned value of the [CreateLiveRecord](/document/product/267/30148) API."
      }
    ],
    "desc": "Note: The `DeleteLiveRecord` API is only used to delete the record of recording tasks but not stop recording or deleting an ongoing recording task. If you need to stop a recording task, please use the [StopLiveRecord](/document/product/267/30146) API."
  },
  "DescribeLiveRecordTemplates": {
    "params": [
      {
        "name": "IsDelayLive",
        "desc": "Whether it is an LCB template. Default value: 0.\n0: LVB.\n1: LCB."
      }
    ],
    "desc": "This API is used to get the recording template list."
  },
  "CreateLiveSnapshotRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "TemplateId",
        "desc": "Template ID."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default."
      },
      {
        "name": "StreamName",
        "desc": "Stream name.\nNote: if this parameter is a non-empty string, the rule will take effect only for the particular stream."
      }
    ],
    "desc": "This API is used to create a screencapturing rule. You need to first call the [CreateLiveSnapshotTemplate](/document/product/267/32624) API to create a screencapturing template to bind the returned template ID to the stream.\n<br>Screencapturing document: [LVB Screencapturing](/document/product/267/32737).\nNote: only one screencapturing template can be associated with one domain name."
  },
  "DescribeStreamDayPlayInfoList": {
    "params": [
      {
        "name": "DayTime",
        "desc": "Date in the format of `YYYY-mm-dd`.\nData is available at 3 AM the next day. You are recommended to query the latest data after this time point."
      },
      {
        "name": "PlayDomain",
        "desc": "Playback domain name."
      },
      {
        "name": "PageNum",
        "desc": "Page number. Value range: [1,1000]. Default value: 1."
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page. Value range: [100,1000]. Default value: 1,000."
      }
    ],
    "desc": "This API is used to query the playback data of each stream at the day level, including the total traffic."
  },
  "ModifyLivePushAuthKey": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "Enable",
        "desc": "Whether to enable. 0: disabled; 1: enabled."
      },
      {
        "name": "MasterAuthKey",
        "desc": "Master authentication key."
      },
      {
        "name": "BackupAuthKey",
        "desc": "Backup authentication key."
      },
      {
        "name": "AuthDelta",
        "desc": "Validity period in seconds."
      }
    ],
    "desc": "This API is used to modify the LVB push authentication key."
  },
  "EnableLiveDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "LVB domain name to be enabled."
      }
    ],
    "desc": "This API is used to enable a disabled LVB domain name."
  },
  "DescribeLiveSnapshotRules": {
    "params": [],
    "desc": "This API is used to get the screencapturing rule list."
  },
  "ModifyLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID."
      },
      {
        "name": "Vcodec",
        "desc": "Video encoding format:\nh264/h265."
      },
      {
        "name": "Acodec",
        "desc": "Audio encoding format:\naac/mp3."
      },
      {
        "name": "AudioBitrate",
        "desc": "Audio bitrate. Default value: 0.\nValue range: 0–500."
      },
      {
        "name": "Description",
        "desc": "Template description."
      },
      {
        "name": "VideoBitrate",
        "desc": "Video bitrate. Value range: 100–8000 Kbps.\nNote: the bitrate value must be a multiple of 100."
      },
      {
        "name": "Width",
        "desc": "Width. Value range: 0-3000."
      },
      {
        "name": "NeedVideo",
        "desc": "Whether to keep the video. 0: no; 1: yes. Default value: 1."
      },
      {
        "name": "NeedAudio",
        "desc": "Whether to keep the audio. 0: no; 1: yes. Default value: 1."
      },
      {
        "name": "Height",
        "desc": "Height. Value range: 0-3000."
      },
      {
        "name": "Fps",
        "desc": "Frame rate. Value range: 0–200."
      },
      {
        "name": "Gop",
        "desc": "Keyframe interval in seconds. Value range: 0–50."
      },
      {
        "name": "Rotate",
        "desc": "Rotation angle.\n0, 90, 180, 270."
      },
      {
        "name": "Profile",
        "desc": "Encoding quality:\nbaseline/main/high."
      },
      {
        "name": "BitrateToOrig",
        "desc": "Whether to not exceed the original bitrate. 0: no; 1: yes. Default value: 0."
      },
      {
        "name": "HeightToOrig",
        "desc": "Whether to not exceed the original height. 0: no; 1: yes. Default value: 0."
      },
      {
        "name": "FpsToOrig",
        "desc": "Whether to not exceed the original frame rate. 0: no; 1: yes. Default value: 0."
      },
      {
        "name": "AdaptBitratePercent",
        "desc": "`VideoBitrate` minus top speed codec bitrate. Value range: 0.1–0.5."
      }
    ],
    "desc": "This API is used to modify the transcoding template configuration."
  },
  "DeleteLiveTranscodeRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Playback domain name."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default."
      },
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "TemplateId",
        "desc": "Template ID."
      }
    ],
    "desc": "This API is used to delete a transcoding rule.\n`DomainName+AppName+StreamName+TemplateId` uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. `TemplateId` is required. Even if other parameters are empty, you still need to pass in an empty string to make a strong match."
  },
  "DeleteLiveSnapshotRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default."
      },
      {
        "name": "StreamName",
        "desc": "Stream name."
      }
    ],
    "desc": "This API is used to delete a screencapturing rule."
  },
  "DescribeLiveWatermarks": {
    "params": [],
    "desc": "This API is used to query the watermark list."
  },
  "ResumeLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the AppName in push and playback addresses and is \"live\" by default."
      },
      {
        "name": "DomainName",
        "desc": "Your push domain name."
      },
      {
        "name": "StreamName",
        "desc": "Stream name."
      }
    ],
    "desc": "This API is used to resume the push of a specific stream."
  },
  "DescribeLiveRecordRules": {
    "params": [],
    "desc": "This API is used to get the list of recording rules."
  },
  "DeleteLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\n1. Get the template ID in the returned value of the [CreateLiveTranscodeTemplate](/document/product/267/32646) API call.\n2. You can query the list of created templates through the [DescribeLiveTranscodeTemplates](/document/product/267/32641) API."
      }
    ],
    "desc": "This API is used to delete a transcoding template."
  },
  "DeleteLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\n1. Get from the returned value of the [CreateLiveSnapshotTemplate](/document/product/267/32624) API call.\n2. You can query the list of created screencapturing templates through the [DescribeLiveSnapshotTemplates](/document/product/267/32619) API."
      }
    ],
    "desc": "This API is used to delete a screencapturing template."
  },
  "DescribeGroupProIspPlayInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start time point in the format of `yyyy-mm-dd HH:MM:SS`."
      },
      {
        "name": "EndTime",
        "desc": "End time point in the format of `yyyy-mm-dd HH:MM:SS`\nThe time span is (0,3 hours]. Data for the last month can be queried."
      },
      {
        "name": "PlayDomains",
        "desc": "Playback domain name. If this parameter is left empty, full data will be queried."
      },
      {
        "name": "ProvinceNames",
        "desc": "District list. If this parameter is left empty, data for all districts will be returned."
      },
      {
        "name": "IspNames",
        "desc": "ISP list. If this parameter is left empty, data of all ISPs will be returned."
      },
      {
        "name": "MainlandOrOversea",
        "desc": "Within or outside Mainland China. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China). If this parameter is left empty, data for all regions will be queried."
      }
    ],
    "desc": "This API is used to query the downstream playback data by district and ISP."
  },
  "DescribeStreamPushInfoList": {
    "params": [
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "StartTime",
        "desc": "Start time point in the format of `yyyy-mm-dd HH:MM:SS`."
      },
      {
        "name": "EndTime",
        "desc": "End time point in the format of `yyyy-mm-dd HH:MM:SS`. The maximum time span is 6 hours. Data for the last 6 days can be queried."
      },
      {
        "name": "PushDomain",
        "desc": "Push domain name."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default."
      }
    ],
    "desc": "This API is used to query the upstream push quality data by stream ID, including frame rate, bitrate, elapsed time, and codec of audio and video files."
  },
  "DescribeLivePlayAuthKey": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Domain name."
      }
    ],
    "desc": "This API is used to query the playback authentication key."
  },
  "DescribeLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID."
      }
    ],
    "desc": "This API is used to get a single recording template."
  },
  "DescribeLiveForbidStreamList": {
    "params": [
      {
        "name": "PageNum",
        "desc": "Page number to get. Default value: 1."
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page. Maximum value: 100. \nValue: any integer between 1 and 100.\nDefault value: 10."
      }
    ],
    "desc": "This API is used to get the forbidden stream list."
  },
  "DeleteLiveWatermarkRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default."
      },
      {
        "name": "StreamName",
        "desc": "Stream name."
      }
    ],
    "desc": "This API is used to delete a watermarking rule."
  },
  "DeleteLiveRecordRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name.\nDomain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the AppName in push and playback addresses and is \"live\" by default.\nDomain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match."
      },
      {
        "name": "StreamName",
        "desc": "Stream name.\nDomain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match."
      }
    ],
    "desc": "This API is used to delete a recording rule."
  },
  "DescribeLiveDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Domain name."
      }
    ],
    "desc": "This API is used to query the LVB domain name information."
  },
  "DescribeLiveDelayInfoList": {
    "params": [],
    "desc": "This API is used to get the list of delayed playbacks."
  },
  "CreateLiveCallbackRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default."
      },
      {
        "name": "TemplateId",
        "desc": "Template ID."
      }
    ],
    "desc": "To create a callback rule, you need to first call the [CreateLiveCallbackTemplate](/document/product/267/32637) API to create a callback template and bind the returned template ID to the domain name/path.\n<br>Callback protocol-related document: [Event Message Notification](/document/product/267/32744)."
  },
  "DeleteLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID."
      }
    ],
    "desc": "This API is used to delete a recording template."
  },
  "BindLiveDomainCert": {
    "params": [
      {
        "name": "CertId",
        "desc": "Certificate ID, which can be obtained through the `CreateLiveCert` API."
      },
      {
        "name": "DomainName",
        "desc": "Playback domain name."
      },
      {
        "name": "Status",
        "desc": "Status. 0: off, 1: on."
      }
    ],
    "desc": "This API is used to bind a domain name certificate.\nNote: you need to call the `CreateLiveCert` API first to add a certificate. After getting the certificate ID, call this API for binding."
  },
  "DescribeLiveCallbackRules": {
    "params": [],
    "desc": "This API is used to get the callback rule list."
  },
  "DescribeLiveTranscodeRules": {
    "params": [],
    "desc": "This API is used to get the list of transcoding rules."
  },
  "ModifyLiveCert": {
    "params": [
      {
        "name": "CertId",
        "desc": "Certificate ID."
      },
      {
        "name": "CertType",
        "desc": "Certificate type. 0: user-added certificate, 1: Tencent Cloud-hosted certificate."
      },
      {
        "name": "CertName",
        "desc": "Certificate name."
      },
      {
        "name": "HttpsCrt",
        "desc": "Certificate content, i.e., public key."
      },
      {
        "name": "HttpsKey",
        "desc": "Private key."
      },
      {
        "name": "Description",
        "desc": "Description."
      }
    ],
    "desc": "This API is used to modify a certificate."
  },
  "DescribeLiveStreamPublishedList": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Your push domain name."
      },
      {
        "name": "EndTime",
        "desc": "End time.\nIn UTC format, such as 2016-06-30T19:00:00Z.\nThis cannot be after the current time.\nNote: The difference between EndTime and StartTime cannot be greater than 30 days."
      },
      {
        "name": "StartTime",
        "desc": "Start time. \nIn UTC format, such as 2016-06-29T19:00:00Z.\nThis supports querying data in the past 60 days."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. Fuzzy match is not supported."
      },
      {
        "name": "PageNum",
        "desc": "Page number to get.\nDefault value: 1."
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page.\nMaximum value: 100.\nValue range: any integer between 1 and 100.\nDefault value: 10."
      },
      {
        "name": "StreamName",
        "desc": "Stream name, which supports fuzzy match."
      }
    ],
    "desc": "This API is used to return the list of pushed streams. <br>\nNote: Up to 10,000 entries can be queried per page. More data can be obtained by adjusting the query time range."
  },
  "ModifyLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID."
      },
      {
        "name": "TemplateName",
        "desc": "Template name.\nMaximum length: 255 bytes."
      },
      {
        "name": "Description",
        "desc": "Description.\nMaximum length: 1,024 bytes."
      },
      {
        "name": "SnapshotInterval",
        "desc": "Screencapturing interval in seconds. Default value: 10s.\nValue range: 5–600s."
      },
      {
        "name": "Width",
        "desc": "Screenshot width. Default value: 0 (original width)."
      },
      {
        "name": "Height",
        "desc": "Screenshot height. Default value: 0 (original height)."
      },
      {
        "name": "PornFlag",
        "desc": "Whether to enable porn detection. Default value: 0.\n0: do not enable.\n1: enable."
      },
      {
        "name": "CosAppId",
        "desc": "COS application ID."
      },
      {
        "name": "CosBucket",
        "desc": "COS bucket name."
      },
      {
        "name": "CosRegion",
        "desc": "COS region."
      },
      {
        "name": "CosPrefix",
        "desc": "COS bucket folder prefix."
      },
      {
        "name": "CosFileName",
        "desc": "COS filename."
      }
    ],
    "desc": "This API is used to modify the screencapturing template configuration."
  },
  "ModifyLiveDomainCert": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Playback domain name."
      },
      {
        "name": "CertId",
        "desc": "Certificate ID."
      },
      {
        "name": "Status",
        "desc": "Status. 0: off, 1: on."
      }
    ],
    "desc": "This API is used to modify the domain name and certificate binding information."
  },
  "ModifyLivePlayAuthKey": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Domain name."
      },
      {
        "name": "Enable",
        "desc": "Whether to enable. 0: disabled; 1: enabled."
      },
      {
        "name": "AuthKey",
        "desc": "Authentication key."
      },
      {
        "name": "AuthDelta",
        "desc": "Validity period in seconds."
      },
      {
        "name": "AuthBackKey",
        "desc": "Authentication backkey."
      }
    ],
    "desc": "This API is used to modify the playback authentication key."
  },
  "ResumeDelayLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the AppName in push and playback addresses and is \"live\" by default."
      },
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "StreamName",
        "desc": "Stream name."
      }
    ],
    "desc": "This API is used to resume a delayed playback."
  },
  "DescribeLiveDomainCert": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Playback domain name."
      }
    ],
    "desc": "This API is used to get the domain name certificate information."
  },
  "CreateLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "Template name, such as 900 900p. This can be only a combination of letters and digits."
      },
      {
        "name": "VideoBitrate",
        "desc": "Video bitrate. Value range: 100–8,000.\nNote: The bitrate must be a multiple of 100."
      },
      {
        "name": "Vcodec",
        "desc": "Video encoding format. Valid values: h264, h265. Default value: h264."
      },
      {
        "name": "Acodec",
        "desc": "Audio encoding in ACC format. Default value: original audio format.\nNote: This parameter will take effect later."
      },
      {
        "name": "AudioBitrate",
        "desc": "Audio bitrate. Value range: 0–500. Default value: 0."
      },
      {
        "name": "Description",
        "desc": "Template description."
      },
      {
        "name": "Width",
        "desc": "Width. Default value: 0."
      },
      {
        "name": "NeedVideo",
        "desc": "Whether to keep the video. 0: no; 1: yes. Default value: 1."
      },
      {
        "name": "NeedAudio",
        "desc": "Whether to keep the audio. 0: no; 1: yes. Default value: 1."
      },
      {
        "name": "Height",
        "desc": "Height. Default value: 0."
      },
      {
        "name": "Fps",
        "desc": "Frame rate. Default value: 0."
      },
      {
        "name": "Gop",
        "desc": "Keyframe interval in seconds. Original interval by default"
      },
      {
        "name": "Rotate",
        "desc": "Whether to rotate. 0: no; 1: yes. Default value: 0."
      },
      {
        "name": "Profile",
        "desc": "Encoding quality:\nbaseline/main/high. Default value: baseline."
      },
      {
        "name": "BitrateToOrig",
        "desc": "Whether to not exceed the original bitrate. 0: no; 1: yes. Default value: 0."
      },
      {
        "name": "HeightToOrig",
        "desc": "Whether to not exceed the original height. 0: no; 1: yes. Default value: 0."
      },
      {
        "name": "FpsToOrig",
        "desc": "Whether to not exceed the original frame rate. 0: no; 1: yes. Default value: 0."
      },
      {
        "name": "AiTransCode",
        "desc": "Whether it is a top speed codec template. 0: no, 1: yes. Default value: 0."
      },
      {
        "name": "AdaptBitratePercent",
        "desc": "`VideoBitrate` minus top speed codec bitrate. Value range: 0.1–0.5."
      }
    ],
    "desc": "After a transcoding template is created and a template ID is successfully returned, you need to call the [CreateLiveTranscodeRule](/document/product/267/32647) API and bind the returned template ID to the stream.\n<br>Transcoding-related document: [LVB Remuxing and Transcoding](/document/product/267/32736)."
  },
  "DeleteLiveCert": {
    "params": [
      {
        "name": "CertId",
        "desc": "Certificate ID."
      }
    ],
    "desc": "This API is used to delete a certificate corresponding to the domain name."
  },
  "DescribeLiveCerts": {
    "params": [],
    "desc": "This API is used to get the certificate information list."
  },
  "AddLiveWatermark": {
    "params": [
      {
        "name": "PictureUrl",
        "desc": "Watermark image URL."
      },
      {
        "name": "WatermarkName",
        "desc": "Watermark name."
      },
      {
        "name": "XPosition",
        "desc": "Display position: X-axis offset. Default value: 0."
      },
      {
        "name": "YPosition",
        "desc": "Display position: Y-axis offset. Default value: 0."
      },
      {
        "name": "Width",
        "desc": "Watermark width or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original width is used by default."
      },
      {
        "name": "Height",
        "desc": "Watermark height or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original height is used by default."
      }
    ],
    "desc": "After a watermark is added and a watermark ID is successfully returned, you need to call the [CreateLiveWatermarkRule](/document/product/267/32629) API and bind the watermark ID to the stream."
  },
  "DescribeLiveDomains": {
    "params": [
      {
        "name": "DomainStatus",
        "desc": "Filter by domain name status. 0: disabled, 1: enabled."
      },
      {
        "name": "DomainType",
        "desc": "Filter by domain name type. 0: push. 1: playback"
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page. Value range: 10–100. Default value: 10."
      },
      {
        "name": "PageNum",
        "desc": "Page number to get. Value range: 1–100000. Default value: 1."
      },
      {
        "name": "IsDelayLive",
        "desc": "0: LVB, 1: LCB. Default value: 0."
      },
      {
        "name": "DomainPrefix",
        "desc": "Domain name prefix."
      }
    ],
    "desc": "This API is used to query domain names by domain name status and type."
  },
  "CancelCommonMixStream": {
    "params": [
      {
        "name": "MixStreamSessionId",
        "desc": "ID of stream mix session (from applying for stream mix to canceling stream mix)."
      }
    ],
    "desc": "This API is used to cancel a stream mix. It can be used basically in the same way as `mix_streamv2.cancel_mix_stream`."
  },
  "UnBindLiveDomainCert": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Playback domain name."
      }
    ],
    "desc": "This API is used to unbind a domain name certificate."
  },
  "ForbidLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the AppName in push and playback addresses and is \"live\" by default."
      },
      {
        "name": "DomainName",
        "desc": "Your push domain name."
      },
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "ResumeTime",
        "desc": "Time to resume the stream in UTC format, such as 2018-11-29T19:00:00Z.\nNotes:\n1. The duration of forbidding is 7 days by default and can be up to 90 days.\n2. The Beijing time is in UTC+8. This value should be in the format as required by ISO 8601. For more information, please see [ISO Date and Time Format](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)."
      },
      {
        "name": "Reason",
        "desc": "Reason for forbidding.\nNote: Be sure to enter the reason for forbidding to avoid any faulty operations.\nLength limit: 2,048 bytes."
      }
    ],
    "desc": "This API is used to forbid the push of a specific stream. You can preset a time point to resume the stream."
  },
  "ModifyLivePlayDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Playback domain name."
      },
      {
        "name": "PlayType",
        "desc": "Pull domain name type. 1: Mainland China. 2: global, 3: outside Mainland China"
      }
    ],
    "desc": "This API is used to modify a playback domain name."
  },
  "DescribeLiveStreamState": {
    "params": [
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the AppName in push and playback addresses and is \"live\" by default."
      },
      {
        "name": "DomainName",
        "desc": "Your push domain name."
      },
      {
        "name": "StreamName",
        "desc": "Stream name."
      }
    ],
    "desc": "This API is used to return the stream status such as active, inactive, or forbidden."
  },
  "CreateLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "Template name.\nMaximum length: 255 bytes.\nOnly letters, digits, underscores, and hyphens can be contained."
      },
      {
        "name": "CosAppId",
        "desc": "COS application ID."
      },
      {
        "name": "CosBucket",
        "desc": "COS bucket name."
      },
      {
        "name": "CosRegion",
        "desc": "COS region."
      },
      {
        "name": "Description",
        "desc": "Description.\nMaximum length: 1,024 bytes.\nOnly letters, digits, underscores, and hyphens can be contained."
      },
      {
        "name": "SnapshotInterval",
        "desc": "Screencapturing interval in seconds. Default value: 10s.\nValue range: 5–600s."
      },
      {
        "name": "Width",
        "desc": "Screenshot width. Default value: 0 (original width)."
      },
      {
        "name": "Height",
        "desc": "Screenshot height. Default value: 0 (original height)."
      },
      {
        "name": "PornFlag",
        "desc": "Whether to enable porn detection. 0: no, 1: yes. Default value: 0"
      },
      {
        "name": "CosPrefix",
        "desc": "COS bucket folder prefix."
      },
      {
        "name": "CosFileName",
        "desc": "COS filename."
      }
    ],
    "desc": "After a screencapturing template is created and a template ID is successfully returned, you need to call the [CreateLiveSnapshotRule](/document/product/267/32625) API and bind the template ID to the stream.\n<br>Screencapturing-related document: [LVB Screencapturing](/document/product/267/32737)."
  },
  "DescribeLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\n1. Get the template ID in the returned value of the [CreateLiveCallbackTemplate](/document/product/267/32637) API call.\n2. You can query the list of created templates through the [DescribeLiveCallbackTemplates](/document/product/267/32632) API."
      }
    ],
    "desc": "This API is used to get a single callback template."
  },
  "DeleteLiveDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Domain name to be deleted."
      },
      {
        "name": "DomainType",
        "desc": "Type. 0: push, 1: playback."
      }
    ],
    "desc": "This API is used to delete an added LVB domain name."
  },
  "DescribeLiveStreamOnlineList": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name. If you use multiple paths, enter the `DomainName`."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. If you use multiple paths, enter the `AppName`."
      },
      {
        "name": "PageNum",
        "desc": "Page number to get. Default value: 1."
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page. Maximum value: 100. \nValue: any integer between 10 and 100.\nDefault value: 10."
      },
      {
        "name": "StreamName",
        "desc": "Stream name, which is used for exact query."
      }
    ],
    "desc": "This API is used to return the live stream list."
  },
  "ModifyLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID."
      },
      {
        "name": "TemplateName",
        "desc": "Template name."
      },
      {
        "name": "Description",
        "desc": "Description."
      },
      {
        "name": "StreamBeginNotifyUrl",
        "desc": "Stream starting callback URL."
      },
      {
        "name": "StreamEndNotifyUrl",
        "desc": "Interruption callback URL."
      },
      {
        "name": "RecordNotifyUrl",
        "desc": "Recording callback URL."
      },
      {
        "name": "SnapshotNotifyUrl",
        "desc": "Screencapturing callback URL."
      },
      {
        "name": "PornCensorshipNotifyUrl",
        "desc": "Porn detection callback URL."
      },
      {
        "name": "CallbackKey",
        "desc": "Callback key. The callback URL is public. For the callback signature, please see the event message notification document.\n[Event Message Notification](/document/product/267/32744)."
      }
    ],
    "desc": "This API is used to modify a callback template."
  },
  "AddLiveDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Domain name."
      },
      {
        "name": "DomainType",
        "desc": "Domain name type.\n0: push domain name.\n1: playback domain name."
      },
      {
        "name": "PlayType",
        "desc": "Pull domain name type:\n1: Mainland China.\n2: global.\n3: outside Mainland China.\nDefault value: 1."
      },
      {
        "name": "IsDelayLive",
        "desc": "Whether it is LCB:\n0: LVB,\n1: LCB.\nDefault value: 0."
      },
      {
        "name": "IsMiniProgramLive",
        "desc": "Whether it is LVB on Mini Program.\n0: LVB.\n1: LVB on Mini Program.\nDefault value: 0."
      }
    ],
    "desc": "This API is used to add a domain name. Only one domain name can be submitted at a time, and it must have an ICP filing."
  },
  "DeleteLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\n1. Get the template ID in the returned value of the [CreateLiveCallbackTemplate](/document/product/267/32637) API call.\n2. You can query the list of created templates through the [DescribeLiveCallbackTemplates](/document/product/267/32632) API."
      }
    ],
    "desc": "This API deletes a callback template."
  },
  "DescribeProIspPlaySumInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start time (Beijing time).\nIn the format of `yyyy-mm-dd HH:MM:SS`."
      },
      {
        "name": "EndTime",
        "desc": "End time (Beijing time).\nIn the format of `yyyy-mm-dd HH:MM:SS`.\nNote: `EndTime` and `StartTime` only support querying data for the last day."
      },
      {
        "name": "StatType",
        "desc": "Statistics type. Valid values: Province, Isp, CountryOrArea."
      },
      {
        "name": "PlayDomains",
        "desc": "If this parameter is left empty, full data will be queried."
      },
      {
        "name": "PageNum",
        "desc": "Page number. Value range: [1,1000]. Default value: 1."
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page. Value range: [1,1000]. Default value: 20."
      },
      {
        "name": "MainlandOrOversea",
        "desc": "Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried."
      },
      {
        "name": "OutLanguage",
        "desc": "Language used in the output field. Valid values: Chinese (default), English. Currently, country/region, district, and ISP parameters support multiple languages."
      }
    ],
    "desc": "This API is used to query the average traffic per second, total traffic, and number of total requests by country/region, district, and ISP in a certain period of time."
  },
  "CreateLiveRecordRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "TemplateId",
        "desc": "Template ID."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the AppName in push and playback addresses and is \"live\" by default."
      },
      {
        "name": "StreamName",
        "desc": "Stream name.\nNote: If the parameter is a non-empty string, the rule will be only applicable to the particular stream."
      }
    ],
    "desc": "To create a recording rule, you need to first call the [CreateLiveRecordTemplate](/document/product/267/32614) API to create a recording template and bind the returned template ID to the stream.\n<br>Recording-related document: [LVB Recording](/document/product/267/32739)."
  },
  "DescribeLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "Watermark ID."
      }
    ],
    "desc": "This API is used to get the information of a single watermark."
  },
  "DescribeLiveTranscodeTemplates": {
    "params": [],
    "desc": "This API is used to get the transcoding template list."
  },
  "CreateLiveCert": {
    "params": [
      {
        "name": "CertType",
        "desc": "Certificate type. 0: user-added certificate, 1: Tencent Cloud-hosted certificate.\nNote: if the certificate type is 0, `HttpsCrt` and `HttpsKey` are required;\nIf the certificate type is 1, the certificate corresponding to `CloudCertId` will be used first. If `CloudCertId` is empty, `HttpsCrt` and `HttpsKey` will be used."
      },
      {
        "name": "CertName",
        "desc": "Certificate name."
      },
      {
        "name": "HttpsCrt",
        "desc": "Certificate content, i.e., public key."
      },
      {
        "name": "HttpsKey",
        "desc": "Private key."
      },
      {
        "name": "Description",
        "desc": "Description."
      },
      {
        "name": "CloudCertId",
        "desc": "Tencent Cloud-hosted certificate ID."
      }
    ],
    "desc": "This API is used to add a certificate."
  },
  "DescribeLivePushAuthKey": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name."
      }
    ],
    "desc": "This API is used to query the LVB push authentication key."
  },
  "DescribeLiveWatermarkRules": {
    "params": [],
    "desc": "This API is used to get the watermarking rule list."
  },
  "CreateLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "Template name. Only letters, digits, underscores, and hyphens can be contained."
      },
      {
        "name": "Description",
        "desc": "Message description"
      },
      {
        "name": "FlvParam",
        "desc": "FLV recording parameter, which is set when FLV recording is enabled."
      },
      {
        "name": "HlsParam",
        "desc": "HLS recording parameter, which is set when HLS recording is enabled."
      },
      {
        "name": "Mp4Param",
        "desc": "Mp4 recording parameter, which is set when Mp4 recording is enabled."
      },
      {
        "name": "AacParam",
        "desc": "AAC recording parameter, which is set when AAC recording is enabled."
      },
      {
        "name": "IsDelayLive",
        "desc": "LVB type. Default value: 0.\n0: LVB.\n1: LCB."
      },
      {
        "name": "HlsSpecialParam",
        "desc": "HLS-specific recording parameter."
      },
      {
        "name": "Mp3Param",
        "desc": "Mp3 recording parameter, which is set when Mp3 recording is enabled."
      }
    ],
    "desc": "After a recording template is created and a template ID is successfully returned, you need to call the [CreateLiveRecordRule](/document/product/267/32615) API and bind the template ID to the stream.\n<br>Recording-related document: [LVB Recording](/document/product/267/32739)."
  },
  "DescribeLiveCert": {
    "params": [
      {
        "name": "CertId",
        "desc": "Certificate ID."
      }
    ],
    "desc": "This API is used to get certificate information."
  },
  "CreateLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "Template name.\nMaximum length: 255 bytes.\nOnly letters, digits, underscores, and hyphens can be contained."
      },
      {
        "name": "Description",
        "desc": "Description.\nMaximum length: 1,024 bytes.\nOnly letters, digits, underscores, and hyphens can be contained."
      },
      {
        "name": "StreamBeginNotifyUrl",
        "desc": "Stream starting callback URL,\nProtocol document: [Event Message Notification](/document/product/267/32744)."
      },
      {
        "name": "StreamEndNotifyUrl",
        "desc": "Interruption callback URL,\nProtocol document: [Event Message Notification](/document/product/267/32744)."
      },
      {
        "name": "RecordNotifyUrl",
        "desc": "Recording callback URL,\nProtocol document: [Event Message Notification](/document/product/267/32744)."
      },
      {
        "name": "SnapshotNotifyUrl",
        "desc": "Screencapturing callback URL,\nProtocol document: [Event Message Notification](/document/product/267/32744)."
      },
      {
        "name": "PornCensorshipNotifyUrl",
        "desc": "Porn detection callback URL,\nProtocol document: [Event Message Notification](/document/product/267/32741)."
      },
      {
        "name": "CallbackKey",
        "desc": "Callback key. The callback URL is public. For the callback signature, please see the event message notification document.\n[Event Message Notification](/document/product/267/32744)."
      }
    ],
    "desc": "This API is used to create a callback template. After a template ID is successfully returned, you need to call the [CreateLiveCallbackRule](/document/product/267/32638) API to bind the template ID to the domain name/path.\n<br>Callback protocol document: [Event Message Notification](/document/product/267/32744)."
  },
  "DescribeLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\nTemplate ID returned by the [CreateLiveSnapshotTemplate](/document/product/267/32624) API call."
      }
    ],
    "desc": "This API is used to get a single screencapturing template."
  }
}