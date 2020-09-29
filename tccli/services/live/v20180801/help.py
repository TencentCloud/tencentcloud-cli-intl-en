# -*- coding: utf-8 -*-
DESC = "live-2018-08-01"
INFO = {
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
  "DescribeLiveWatermarks": {
    "params": [],
    "desc": "This API is used to query the watermark list."
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
    "desc": "- Prerequisites\n  1. Recording files are stored on the VOD platform, so if you need to use the recording feature, you must first activate the VOD service.\n  2. After the recording files are stored, applicable fees (including storage fees and downstream playback traffic fees) will be charged according to the VOD billing mode. For more information, please see the [corresponding document](https://intl.cloud.tencent.com/document/product/266/2838?from_cn_redirect=1).\n\n- Mode description\n  This API supports two recording modes:\n  1. Scheduled recording mode **(default mode)**.\n    The start time and end time need to be passed in, according to which the recording task will start and end automatically. Before the set end time expires (provided that `StopLiveRecord` is not called to terminate the task prematurely), the recording task is valid and will be started even after the push is interrupted and restarted multiple times.\n  2. Real-time video recording mode.\n    The start time passed in will be ignored, and recording will be started immediately after the recording task is created. The recording duration can be up to 30 minutes. If the end time passed in is more than 30 minutes after the current time, it will be counted as 30 minutes. Real-time video recording is mainly used for recording highlight scenes, and you are recommended to keep the duration within 5 minutes.\n\n- Precautions\n  1. The API call timeout period should be set to more than 3 seconds; otherwise, retries and calls by different start/end time values may result in repeated recording tasks and thus incur additional recording fees.\n  2. Subject to the audio and video file formats (FLV/MP4/HLS), the video codec of H.264 and audio codec of AAC are supported.\n  3. In order to avoid malicious or unintended frequent API requests, the maximum number of tasks that can be created in scheduled recording mode is limited: up to 4,000 tasks can be created per day (excluding deleted ones), and up to 400 ones can run concurrently. If you need a higher upper limit, please submit a ticket for application.\n  4. This calling method does not support recording streams outside Mainland China for the time being."
  },
  "UpdateLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "Watermark ID.\nGet the watermark ID in the returned value of the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API call."
      },
      {
        "name": "PictureUrl",
        "desc": "Watermark image URL."
      },
      {
        "name": "XPosition",
        "desc": "Display position: X-axis offset in %. Default value: 0."
      },
      {
        "name": "YPosition",
        "desc": "Display position: Y-axis offset in %. Default value: 0."
      },
      {
        "name": "WatermarkName",
        "desc": "Watermark name.\nUp to 16 bytes."
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
        "desc": "Screencapturing interval in seconds. Default value: 10s.\nValue range: 5-300s."
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
        "desc": "COS bucket name.\nNote: the value of `CosBucket` cannot contain `-[appid]`."
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
  "ModifyLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID obtained through the `DescribeRecordTemplates` API."
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
        "desc": "Watermark ID, which is the `WatermarkId` returned by the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API."
      }
    ],
    "desc": "To create a watermarking rule, you need to first call the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API to add a watermark and bind the returned watermark ID to the stream."
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
        "desc": "Number of entries per page.\nMaximum value: 100.\nValue range: any integer between 1 and 100.\nDefault value: 10.\nNote: currently, query for up to 10,000 entries is supported."
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
    "desc": "This API is used to create a general stream mix. It can be used basically in the same way as the legacy `mix_streamv2.start_mix_stream_advanced` API.\nNote: currently, up to 16 streams can be mixed.\nBest practice: https://intl.cloud.tencent.com/document/product/267/45566?from_cn_redirect=1"
  },
  "DescribeHttpStatusInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start time (Beijing time).\nFormat: yyyy-mm-dd HH:MM:SS."
      },
      {
        "name": "EndTime",
        "desc": "End time (Beijing time).\nFormat: yyyy-mm-dd HH:MM:SS.\nNote: data in the last 3 months can be queried and the query period is up to 1 day."
      },
      {
        "name": "PlayDomains",
        "desc": "Playback domain name list."
      }
    ],
    "desc": "This API is used to query the number of each playback HTTP status code at a 5-minute granularity in a certain period of time.\nNote: data can be queried one hour after it is generated. For example, data between 10:00 and 10:59 cannot be queried until 12:00."
  },
  "DescribeProvinceIspPlayInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start point in time (Beijing time).\nExample: 2019-02-21 10:00:00."
      },
      {
        "name": "EndTime",
        "desc": "End point in time (Beijing time).\nExample: 2019-02-21 12:00:00.\nNote: `EndTime` and `StartTime` only support querying data for the last day."
      },
      {
        "name": "Granularity",
        "desc": "Supported granularities:\n1: 1-minute granularity (the query interval should be within 1 day)"
      },
      {
        "name": "StatType",
        "desc": "Statistical metric type:\n\"Bandwidth\": bandwidth\n\"FluxPerSecond\": average traffic\n\"Flux\": traffic\n\"Request\": number of requests\n\"Online\": number of concurrent connections"
      },
      {
        "name": "PlayDomains",
        "desc": "Playback domain name list."
      },
      {
        "name": "ProvinceNames",
        "desc": "List of the districts to be queried, such as Beijing."
      },
      {
        "name": "IspNames",
        "desc": "List of the ISPs to be queried, such as China Mobile. If this parameter is left empty, the data of all ISPs will be queried."
      },
      {
        "name": "MainlandOrOversea",
        "desc": "Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried."
      }
    ],
    "desc": "This API is used to query the downstream playback data of a specified ISP in a specified district, including bandwidth, traffic, number of requests, and number of concurrent connections."
  },
  "ModifyLivePushAuthKey": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "Enable",
        "desc": "Whether to enable. 0: disabled; 1: enabled.\nIf this parameter is left empty, the current value will not be modified."
      },
      {
        "name": "MasterAuthKey",
        "desc": "Master authentication key.\nIf this parameter is left empty, the current value will not be modified."
      },
      {
        "name": "BackupAuthKey",
        "desc": "Backup authentication key.\nIf this parameter is left empty, the current value will not be modified."
      },
      {
        "name": "AuthDelta",
        "desc": "Validity period in seconds."
      }
    ],
    "desc": "This API is used to modify the LVB push authentication key."
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
  "DescribeLiveSnapshotRules": {
    "params": [],
    "desc": "This API is used to get the screencapturing rule list."
  },
  "DeleteLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\n1. Get the template ID in the returned value of the [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/32646?from_cn_redirect=1) API call.\n2. You can query the list of created templates through the [DescribeLiveTranscodeTemplates](https://intl.cloud.tencent.com/document/product/267/32641?from_cn_redirect=1) API."
      }
    ],
    "desc": "This API is used to delete a transcoding template."
  },
  "DescribeTopClientIpSumInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start point in time in the format of `yyyy-mm-dd HH:MM:SS`."
      },
      {
        "name": "EndTime",
        "desc": "End point in time in the format of `yyyy-mm-dd HH:MM:SS`\nThe time span is [0,4 hours]. Data for the last day can be queried."
      },
      {
        "name": "PlayDomains",
        "desc": "Playback domain name. If this parameter is left empty, full data will be queried by default."
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
        "name": "OrderParam",
        "desc": "Sorting metric. Valid values: TotalRequest (default value), FailedRequest, TotalFlux."
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
    "desc": "This API is used to query the information of the top n client IPs in a certain period of time (top 1,000 is supported currently)."
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
  "DescribeVisitTopSumInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start point in time in the format of `yyyy-mm-dd HH:MM:SS`."
      },
      {
        "name": "EndTime",
        "desc": "End point in time in the format of `yyyy-mm-dd HH:MM:SS`\nThe time span is (0,4 hours]. Data for the last day can be queried."
      },
      {
        "name": "TopIndex",
        "desc": "Bandwidth metric. Valid values: \"Domain\", \"StreamId\"."
      },
      {
        "name": "PlayDomains",
        "desc": "Playback domain name. If this parameter is left empty, full data will be queried by default."
      },
      {
        "name": "PageNum",
        "desc": "Page number,\nValue range: [1,1000],\nDefault value: 1."
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page. Value range: [1,1000].\nDefault value: 20."
      },
      {
        "name": "OrderParam",
        "desc": "Sorting metric. Valid values: \"AvgFluxPerSecond\", \"TotalRequest\" (default), \"TotalFlux\"."
      }
    ],
    "desc": "This API is used to query the information of the top n domain names or stream IDs in a certain period of time (top 1,000 is supported currently)."
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
  "AddLiveWatermark": {
    "params": [
      {
        "name": "PictureUrl",
        "desc": "Watermark image URL."
      },
      {
        "name": "WatermarkName",
        "desc": "Watermark name.\nUp to 16 bytes."
      },
      {
        "name": "XPosition",
        "desc": "Display position: X-axis offset in %. Default value: 0."
      },
      {
        "name": "YPosition",
        "desc": "Display position: Y-axis offset in %. Default value: 0."
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
    "desc": "After a watermark is added and a watermark ID is successfully returned, you need to call the [CreateLiveWatermarkRule](https://intl.cloud.tencent.com/document/product/267/32629?from_cn_redirect=1) API and bind the watermark ID to the stream."
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
        "desc": "COS bucket name.\nNote: the value of `CosBucket` cannot contain `-[appid]`."
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
        "desc": "Screencapturing interval in seconds. Default value: 10s.\nValue range: 5-300s."
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
        "desc": "COS Bucket folder prefix.\nIf no value is entered, the default value\n`/{Year}-{Month}-{Day}`\nwill be used."
      },
      {
        "name": "CosFileName",
        "desc": "COS filename.\nIf no value is entered, the default value \n`{StreamID}-screenshot-{Hour}-{Minute}-{Second}-{Width}x{Height}{Ext}`\nwill be used."
      }
    ],
    "desc": "After a screencapturing template is created and a template ID is successfully returned, you need to call the [CreateLiveSnapshotRule](https://intl.cloud.tencent.com/document/product/267/32625?from_cn_redirect=1) API and bind the template ID to the stream.\n<br>Screencapturing-related document: [LVB Screencapturing](https://intl.cloud.tencent.com/document/product/267/32737?from_cn_redirect=1)."
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
    "desc": "This API is used to return a list of live streams. It queries the information of live streams after they are pushed successfully.\nNote: this API can query up to 20,000 streams. If you want to query more than 20,000 streams, please contact after-sales service."
  },
  "DeleteLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\n1. Get the template ID in the returned value of the [CreateLiveCallbackTemplate](https://intl.cloud.tencent.com/document/product/267/32637?from_cn_redirect=1) API call.\n2. You can query the list of created templates through the [DescribeLiveCallbackTemplates](https://intl.cloud.tencent.com/document/product/267/32632?from_cn_redirect=1) API."
      }
    ],
    "desc": "This API deletes a callback template."
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
  "DescribeLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID obtained through the `DescribeRecordTemplates` API."
      }
    ],
    "desc": "This API is used to get a single recording template."
  },
  "DeleteLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "Watermark ID.\nWatermark ID obtained in the returned value of the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API call.\nWatermark ID returned by the `DescribeLiveWatermarks` API."
      }
    ],
    "desc": "This API is used to delete a watermark."
  },
  "DescribePlayErrorCodeSumInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start point in time (Beijing time).\nIn the format of `yyyy-mm-dd HH:MM:SS`."
      },
      {
        "name": "EndTime",
        "desc": "End point in time (Beijing time).\nIn the format of `yyyy-mm-dd HH:MM:SS`.\nNote: `EndTime` and `StartTime` only support querying data for the last day."
      },
      {
        "name": "PlayDomains",
        "desc": "Playback domain name list. If this parameter is left empty, full data will be queried."
      },
      {
        "name": "PageNum",
        "desc": "Number of pages. Value range: [1,1000]. Default value: 1."
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
        "name": "GroupType",
        "desc": "Grouping parameter. Valid values: CountryProIsp (default value), Country (country/region). Grouping is made by country/region + district + ISP by default. Currently, districts and ISPs outside Mainland China cannot be recognized."
      },
      {
        "name": "OutLanguage",
        "desc": "Language used in the output field. Valid values: Chinese (default), English. Currently, country/region, district, and ISP parameters support multiple languages."
      }
    ],
    "desc": "This API is used to query the information of downstream playback error codes."
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
        "desc": "Expiration time of the configured delayed playback in UTC format, such as 2018-11-29T19:00:00Z.\nNotes:\n1. The configuration will expire after 7 days by default and can last up to 7 days.\n2. The Beijing time is in UTC+8. This value should be in the format as required by ISO 8601. For more information, please see [ISO Date and Time Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)."
      }
    ],
    "desc": "This API is used to set the delay time for a stream.\nNote: if you want to set delayed playback before pushing, you need to do so 5 minutes in advance.\nCurrently, this API only supports stream granularity, and the feature supporting domain name and application granularities will be available in the future.\nUse case: for important live streams, you can set delayed playback in advance to avoid contingency issues.\n"
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
  "ModifyLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID."
      },
      {
        "name": "Vcodec",
        "desc": "Video codec: `h264/h265/origin`. Default value: `h264`.\n\norigin: original codec as the output codec"
      },
      {
        "name": "Acodec",
        "desc": "Audio codec: acc by default.\nNote: this parameter is unsupported now."
      },
      {
        "name": "AudioBitrate",
        "desc": "Audio bitrate. Default value: 0.\nValue range: 0-500."
      },
      {
        "name": "Description",
        "desc": "Template description."
      },
      {
        "name": "VideoBitrate",
        "desc": "Video bitrate in Kbps. Value range: 100-8,000.\nNote: the transcoding template requires that the bitrate should be unique, yet the final saved bitrate may be different from the input bitrate."
      },
      {
        "name": "Width",
        "desc": "Width in pixels. Value range: 0-3,000.\nIt must be a multiple of 2. The original width is 0"
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
        "desc": "Height in pixels. Value range: 0-3,000.\nIt must be a multiple of 2. The original height is 0"
      },
      {
        "name": "Fps",
        "desc": "Frame rate in fps. Default value: 0.\nValue range: 0-60"
      },
      {
        "name": "Gop",
        "desc": "Keyframe interval in seconds.\nValue range: 2-6"
      },
      {
        "name": "Rotate",
        "desc": "Rotation angle. Default value: 0.\nValid values: 0, 90, 180, 270"
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
        "desc": "Bitrate compression ratio of top speed codec video.\nTarget bitrate of top speed code = VideoBitrate * (1-AdaptBitratePercent)\n\nValue range: 0.0-0.5."
      },
      {
        "name": "ShortEdgeAsHeight",
        "desc": "This parameter is used to define whether the short side is the video height. 0: no, 1: yes. The default value is 0."
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
  "DescribeLiveCert": {
    "params": [
      {
        "name": "CertId",
        "desc": "Certificate ID obtained through the `DescribeLiveCerts` API."
      }
    ],
    "desc": "This API is used to get certificate information."
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
        "desc": "Number of entries per page. Value range: 10-100. Default value: 10."
      },
      {
        "name": "PageNum",
        "desc": "Page number to get. Value range: 1-100000. Default value: 1."
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
  "DeleteLiveCert": {
    "params": [
      {
        "name": "CertId",
        "desc": "Certificate ID obtained through the `DescribeLiveCerts` API."
      }
    ],
    "desc": "This API is used to delete a certificate corresponding to the domain name."
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
        "desc": "Stream starting callback URL,\nProtocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1)."
      },
      {
        "name": "StreamEndNotifyUrl",
        "desc": "Interruption callback URL,\nProtocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1)."
      },
      {
        "name": "RecordNotifyUrl",
        "desc": "Recording callback URL,\nProtocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1)."
      },
      {
        "name": "SnapshotNotifyUrl",
        "desc": "Screencapturing callback URL,\nProtocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1)."
      },
      {
        "name": "PornCensorshipNotifyUrl",
        "desc": "Porn detection callback URL,\nProtocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32741?from_cn_redirect=1)."
      },
      {
        "name": "CallbackKey",
        "desc": "Callback key. The callback URL is public. For the callback signature, please see the event message notification document.\n[Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1)."
      },
      {
        "name": "StreamMixNotifyUrl",
        "desc": "Stream mixing callback URL,\nProtocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1)."
      }
    ],
    "desc": "After a callback template is created and a template ID is successfully returned, you need to call the [CreateLiveCallbackRule](https://intl.cloud.tencent.com/document/product/267/32638?from_cn_redirect=1) API and bind the template ID to the domain name/path.\n<br>Callback protocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).\nNote: at least enter one callback URL."
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
  "DescribeLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\n1. Get the template ID in the returned value of the [CreateLiveCallbackTemplate](https://intl.cloud.tencent.com/document/product/267/32637?from_cn_redirect=1) API call.\n2. You can query the list of created templates through the [DescribeLiveCallbackTemplates](https://intl.cloud.tencent.com/document/product/267/32632?from_cn_redirect=1) API."
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
  "ModifyLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID returned by the `DescribeLiveCallbackTemplates` API."
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
        "desc": "Callback key. The callback URL is public. For the callback signature, please see the event message notification document.\n[Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1)."
      }
    ],
    "desc": "This API is used to modify a callback template."
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
  "DescribeStreamPlayInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start time (Beijing time) in the format of `yyyy-mm-dd HH:MM:SS`,\nThe start time cannot be more than 30 days after the current time."
      },
      {
        "name": "EndTime",
        "desc": "End time (Beijing time) in the format of `yyyy-mm-dd HH:MM:SS`.\nThe end time and start time must be on the same day."
      },
      {
        "name": "PlayDomain",
        "desc": "Playback domain name,\nIf this parameter is left empty, data of live streams of all playback domain names will be queried."
      },
      {
        "name": "StreamName",
        "desc": "Stream name (exact match).\nIf this parameter is left empty, full playback data will be queried."
      },
      {
        "name": "AppName",
        "desc": "Push address. Its value is the same as the `AppName` in playback address. It supports exact match, and takes effect only when `StreamName` is passed at the same time.\nIf it is left empty, the full playback data will be queried.\nNote: to query by `AppName`, you need to submit a ticket first. After your application succeeds, it will take about 5 business days (subject to the time in the reply) for the configuration to take effect."
      }
    ],
    "desc": "This API is used to query the playback data. It supports querying the playback details by stream name and aggregated data by playback domain name. Data in the last 4 minutes or so cannot be queried due to delay.\nNote: to query by `AppName`, you need to submit a ticket first. After your application succeeds, it will take about 5 business days (subject to the time in the reply) for the configuration to take effect."
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
  "DescribeLiveTranscodeRules": {
    "params": [
      {
        "name": "TemplateIds",
        "desc": ""
      },
      {
        "name": "DomainNames",
        "desc": ""
      }
    ],
    "desc": "This API is used to get the list of transcoding rules."
  },
  "DescribeLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\nTemplate ID returned by the [CreateLiveSnapshotTemplate](https://intl.cloud.tencent.com/document/product/267/32624?from_cn_redirect=1) API call."
      }
    ],
    "desc": "This API is used to get a single screencapturing template."
  },
  "DescribeLiveCallbackTemplates": {
    "params": [],
    "desc": "This API is used to get the callback template list."
  },
  "StopRecordTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "Recording task ID."
      }
    ],
    "desc": "This API is used to end a recording prematurely and terminate the running recording task. After the task is successfully terminated, it will no longer start."
  },
  "DescribeLiveSnapshotTemplates": {
    "params": [],
    "desc": "This API is used to get the screencapturing template list."
  },
  "StopLiveRecord": {
    "params": [
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "TaskId",
        "desc": "Task ID returned by the `CreateLiveRecord` API."
      }
    ],
    "desc": "Note: Recording files are stored on the VOD platform. To use the recording feature, you need to activate a VOD account and ensure that it is available. After the recording files are stored, applicable fees (including storage fees and downstream playback traffic fees) will be charged according to the VOD billing method. For more information, please see the corresponding document."
  },
  "ModifyLivePlayAuthKey": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Playback domain name."
      },
      {
        "name": "Enable",
        "desc": "Whether to enable. 0: disabled; 1: enabled.\nIf this parameter is left empty, the current value will not be modified."
      },
      {
        "name": "AuthKey",
        "desc": "Authentication key.\nIf this parameter is left empty, the current value will not be modified."
      },
      {
        "name": "AuthDelta",
        "desc": "Validity period in seconds.\nIf this parameter is left empty, the current value will not be modified."
      },
      {
        "name": "AuthBackKey",
        "desc": "Backup authentication key.\nIf this parameter is left empty, the current value will not be modified."
      }
    ],
    "desc": "This API is used to modify the playback authentication key."
  },
  "DescribeLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\nNote: get the template ID in the returned value of the [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/32646?from_cn_redirect=1) API call."
      }
    ],
    "desc": "This API is used to get a single transcoding template."
  },
  "DescribeScreenShotSheetNumList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start time in UTC time in the format of `yyyy-mm-ddTHH:MM:SSZ`."
      },
      {
        "name": "EndTime",
        "desc": "End time in UTC time in the format of `yyyy-mm-ddTHH:MM:SSZ`. Data for the last year can be queried."
      },
      {
        "name": "Zone",
        "desc": "Region information. Valid values: Mainland, Oversea. The former is to query data within Mainland China, while the latter outside Mainland China. If this parameter is left empty, data of all regions will be queried."
      },
      {
        "name": "PushDomains",
        "desc": "Push domain name (data at the domain name level after November 1, 2019 can be queried)."
      },
      {
        "name": "Granularity",
        "desc": "Data dimension. The data has a delay of one and a half hours. Valid values: 1. Minute (5-minute granularity, which supports a maximum query time range of 31 days); 2. Day (1-day granularity, which is the default value and supports a maximum query time range of 186 days)."
      }
    ],
    "desc": "The API is used to query the number of screenshots as an LVB value-added service."
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
  "DeleteRecordTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "Task ID returned by `CreateRecordTask`. The recording task specified by `TaskId` will be deleted."
      }
    ],
    "desc": "This API is used to delete a recording task configuration. The deletion does not affect running tasks and takes effect only for new pushes."
  },
  "DescribeLiveTranscodeDetailInfo": {
    "params": [
      {
        "name": "PushDomain",
        "desc": "Push domain name."
      },
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "DayTime",
        "desc": "Start time (Beijing time).\nIn the format of `yyyymmdd`.\nNote: details for a specified day in the last month can be queried."
      },
      {
        "name": "PageNum",
        "desc": "Number of pages. Default value: 1.\nUp to 100 pages."
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page. Default value: 20,\nValue range: [10,1000]."
      },
      {
        "name": "StartDayTime",
        "desc": "Start day time (Beijing time),\nIn the format of `yyyymmdd`.\nNote: details for the last month can be queried."
      },
      {
        "name": "EndDayTime",
        "desc": "End day time (Beijing time),\nIn the format of `yyyymmdd`.\nNote: detailed data for the last month can be queried. Either `DayTime` or `(StartDayTime,EndDayTime)` must be passed in. If both are passed in, `DayTime` shall prevail."
      }
    ],
    "desc": "This API is used to query the details of transcoding on a specified day or in a specified period of time."
  },
  "DescribeLiveRecordRules": {
    "params": [],
    "desc": "This API is used to get the list of recording rules."
  },
  "DescribeLiveDelayInfoList": {
    "params": [],
    "desc": "This API is used to get the list of delayed playbacks."
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
  "DescribeLiveDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "Domain name."
      }
    ],
    "desc": "This API is used to query the LVB domain name information."
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
    "desc": "To create a callback rule, you need to first call the [CreateLiveCallbackTemplate](https://intl.cloud.tencent.com/document/product/267/32637?from_cn_redirect=1) API to create a callback template and bind the returned template ID to the domain name/path.\n<br>Callback protocol-related document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1)."
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
        "desc": "HTTPS status. 0: disabled, 1: enabled."
      }
    ],
    "desc": "This API is used to bind a domain name certificate.\nNote: you need to call the `CreateLiveCert` API first to add a certificate. After getting the certificate ID, call this API for binding."
  },
  "DescribeLiveCallbackRules": {
    "params": [],
    "desc": "This API is used to get the callback rule list."
  },
  "DescribePlayErrorCodeDetailInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start time (Beijing time),\nIn the format of `yyyy-mm-dd HH:MM:SS`."
      },
      {
        "name": "EndTime",
        "desc": "End time (Beijing time),\nIn the format of `yyyy-mm-dd HH:MM:SS`.\nNote: `EndTime` and `StartTime` only support querying data for the last day."
      },
      {
        "name": "Granularity",
        "desc": "Query granularity:\n1: 1-minute granularity."
      },
      {
        "name": "StatType",
        "desc": "Yes. Valid values: \"4xx\", \"5xx\". Mixed codes in the format of `4xx,5xx` are also supported."
      },
      {
        "name": "PlayDomains",
        "desc": "Playback domain name list."
      },
      {
        "name": "MainlandOrOversea",
        "desc": "Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried."
      }
    ],
    "desc": "This API is used to query the information of downstream playback error codes, i.e., the occurrences of each HTTP error code (4xx and 5xx) at a 1-minute granularity in a certain period of time.\n\n"
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
        "desc": "Time to resume the stream in UTC format, such as 2018-11-29T19:00:00Z.\nNotes:\n1. The duration of forbidding is 7 days by default and can be up to 90 days.\n2. The Beijing time is in UTC+8. This value should be in the format as required by ISO 8601. For more information, please see [ISO Date and Time Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)."
      },
      {
        "name": "Reason",
        "desc": "Reason for forbidding.\nNote: Be sure to enter the reason for forbidding to avoid any faulty operations.\nLength limit: 2,048 bytes."
      }
    ],
    "desc": "This API is used to forbid the push of a specific stream. You can preset a time point to resume the stream."
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
  "DescribeDeliverBandwidthList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Start time in the format of \"%Y-%m-%d %H:%M:%S\"."
      },
      {
        "name": "EndTime",
        "desc": "End time in the format of \"%Y-%m-%d %H:%M:%S\". Data in the last 3 months can be queried, and the query period is up to 1 month."
      }
    ],
    "desc": "This API is used to query the billable bandwidth of live stream relaying in the last 3 months. The query period is up to 31 days."
  },
  "DescribeLiveDomainPlayInfoList": {
    "params": [
      {
        "name": "PlayDomains",
        "desc": "Playback domain name list."
      }
    ],
    "desc": "This API is used to query the real-time downstream playback data at the domain name level. As it takes certain time to process data, the API queries quasi-real-time data generated 4 minutes ago by default."
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
    "desc": "To create a recording rule, you need to first call the [CreateLiveRecordTemplate](https://intl.cloud.tencent.com/document/product/267/32614?from_cn_redirect=1) API to create a recording template and bind the returned template ID to the stream.\n<br>Recording-related document: [LVB Recording](https://intl.cloud.tencent.com/document/product/267/32739?from_cn_redirect=1)."
  },
  "DescribeLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "Watermark ID returned by the `DescribeLiveWatermarks` API."
      }
    ],
    "desc": "This API is used to get the information of a single watermark."
  },
  "DescribeLiveTranscodeTemplates": {
    "params": [],
    "desc": "This API is used to get the transcoding template list."
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
    "desc": "After a recording template is created and a template ID is successfully returned, you need to call the [CreateLiveRecordRule](https://intl.cloud.tencent.com/document/product/267/32615?from_cn_redirect=1) API and bind the template ID to the stream.\n<br>Recording-related document: [LVB Recording](https://intl.cloud.tencent.com/document/product/267/32739?from_cn_redirect=1)."
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
    "desc": "To create a transcoding rule, you need to first call the [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/32646?from_cn_redirect=1) API to create a transcoding template and bind the returned template ID to the stream.\n<br>Transcoding-related document: [LVB Remuxing and Transcoding](https://intl.cloud.tencent.com/document/product/267/32736?from_cn_redirect=1)."
  },
  "DescribeLiveWatermarkRules": {
    "params": [],
    "desc": "This API is used to get the watermarking rule list."
  },
  "DeleteLiveRecord": {
    "params": [
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "TaskId",
        "desc": "Task ID returned by the `CreateLiveRecord` API."
      }
    ],
    "desc": "Note: The `DeleteLiveRecord` API is only used to delete the record of recording tasks but not stop recording or deleting an ongoing recording task. If you need to stop a recording task, please use the [StopLiveRecord](https://intl.cloud.tencent.com/document/product/267/30146?from_cn_redirect=1) API."
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
    "desc": "This API is used to create a screencapturing rule. You need to first call the [CreateLiveSnapshotTemplate](https://intl.cloud.tencent.com/document/product/267/32624?from_cn_redirect=1) API to create a screencapturing template to bind the returned template ID to the stream.\n<br>Screencapturing document: [LVB Screencapturing](https://intl.cloud.tencent.com/document/product/267/32737?from_cn_redirect=1).\nNote: only one screencapturing template can be associated with one domain name."
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
        "desc": "Statistics type. Valid values: Province (district), Isp (ISP), CountryOrArea (country or region)."
      },
      {
        "name": "PlayDomains",
        "desc": "Playback domain name list. If it is left empty, it refers to all playback domain names."
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
  "DescribeAllStreamPlayInfoList": {
    "params": [
      {
        "name": "QueryTime",
        "desc": "Query time accurate down to the minute in the format of `yyyy-mm-dd HH:MM:SS`. Data for the last month can be queried. The data has a delay of about 5 minutes; therefore, if you want to query real-time data, we recommend you pass in a point in time 5 minutes ago."
      }
    ],
    "desc": "This API is used to query the downstream information of all streams at a specified point in time (at a 1-minute granularity)."
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
  "DeleteLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID obtained through the `DescribeRecordTemplates` API."
      }
    ],
    "desc": "This API is used to delete a recording template."
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
  "CreateRecordTask": {
    "params": [
      {
        "name": "StreamName",
        "desc": "Stream name."
      },
      {
        "name": "DomainName",
        "desc": "Push domain name."
      },
      {
        "name": "AppName",
        "desc": "Push path."
      },
      {
        "name": "EndTime",
        "desc": "The recording end time in UNIX timestamp format. The “EndTime” should be later than “StartTime”. Normally the duration between “EndTime” and “StartTime” is up to 24 hours."
      },
      {
        "name": "StartTime",
        "desc": "The recording start time in UNIX timestamp format. If the “StartTime” is not entered, recording will start immediately after the API is successfully called. Normally the “StartTime” should be within 6 days from current time."
      },
      {
        "name": "StreamType",
        "desc": "Push type. Default value: 0. Valid values:\n0: LVB push.\n1: mixed stream, i.e., A + B = C mixed stream."
      },
      {
        "name": "TemplateId",
        "desc": "Recording template ID, which is the returned value of `CreateLiveRecordTemplate`. If this parameter is left empty or incorrect, the stream will be recorded in HLS format and retained permanently by default."
      },
      {
        "name": "Extension",
        "desc": "Extension field which is not defined now. It is empty by default."
      }
    ],
    "desc": "This API is used to create a recording task that starts and ends at specified times and records by using the configuration corresponding to a specified recording template ID.\n- Prerequisites\n1. Recording files are stored on the VOD platform, so if you need to use the recording feature, you must first activate the VOD service.\n2. After the recording files are stored, applicable fees (including storage fees and downstream playback traffic fees) will be charged according to the VOD billing mode. For more information, please see the corresponding document.\n- Precautions\n1. An interruption will end the current recording and generate a recording file. The task will still be valid before the end time expires, and as long as the stream is pushed normally during the period, it will record normally, regardless of whether the push is interrupted or restarted multiple times.\n2. Creating recording tasks with overlapping time periods must be avoided. If there are multiple tasks with overlapping time periods for the same stream, the system will start three recording tasks at most to avoid repeated recording.\n3. The record of a created recording task will be retained for 3 months on the platform.\n4. The current recording task management APIs (CreateRecordTask/StopRecordTask/DeleteRecordTask) are not compatible with the legacy APIs (CreateLiveRecord/StopLiveRecord/DeleteLiveRecord), and they cannot be mixed."
  },
  "CreateLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "Template name, such as “900p”. This can be only a combination of letters and digits.\nLength limit:\n  Standard transcoding: 1-10 characters\n  Top speed codec transcoding: 3-10 characters"
      },
      {
        "name": "VideoBitrate",
        "desc": "Video bitrate in Kbps. Value range: 100-8,000.\nNote: the transcoding template requires that bitrate should be unique, yet the final saved bitrate may be different from the input bitrate."
      },
      {
        "name": "Acodec",
        "desc": "Audio codec: acc by default.\nNote: this parameter is unsupported now."
      },
      {
        "name": "AudioBitrate",
        "desc": "Audio bitrate. Default value: 0.\nValue range: 0-500."
      },
      {
        "name": "Vcodec",
        "desc": "Video codec: `h264/h265/origin`. Default value: `h264`.\n\norigin: original codec as the output codec"
      },
      {
        "name": "Description",
        "desc": "Template description."
      },
      {
        "name": "Width",
        "desc": "Width. Default value: 0.\nValue range: 0-3,000\nIt must be a multiple of 2. The original width is 0"
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
        "desc": "Height. Default value: 0.\nValue range: 0-3,000\nIt must be a multiple of 2. The original height is 0"
      },
      {
        "name": "Fps",
        "desc": "Frame rate. Default value: 0.\nValue range: 0-60"
      },
      {
        "name": "Gop",
        "desc": "Keyframe interval in seconds. Default value: original interval\nValue range: 2-6"
      },
      {
        "name": "Rotate",
        "desc": "Rotation angle. Default value: 0.\nValid values: 0, 90, 180, 270"
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
        "desc": "Bitrate compression ratio of top speed codec video.\nTarget bitrate of top speed code = VideoBitrate * (1-AdaptBitratePercent)\n\nValue range: 0.0-0.5."
      },
      {
        "name": "ShortEdgeAsHeight",
        "desc": "This parameter is used to define whether the short side is the video height. 0: no, 1: yes. The default value is 0."
      }
    ],
    "desc": "After a transcoding template is created and a template ID is successfully returned, you need to call the [CreateLiveTranscodeRule](https://intl.cloud.tencent.com/document/product/267/32647?from_cn_redirect=1) API and bind the returned template ID to the stream.\n<br>Transcoding-related document: [LVB Remuxing and Transcoding](https://intl.cloud.tencent.com/document/product/267/32736?from_cn_redirect=1)."
  },
  "DescribeLiveCerts": {
    "params": [],
    "desc": "This API is used to get the certificate information list."
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
  "CancelCommonMixStream": {
    "params": [
      {
        "name": "MixStreamSessionId",
        "desc": "ID of stream mix session (from applying for stream mix to canceling stream mix).\nThis value is the same as the `MixStreamSessionId` in `CreateCommonMixStream`."
      }
    ],
    "desc": "This API is used to cancel a stream mix. It can be used basically in the same way as `mix_streamv2.cancel_mix_stream`."
  },
  "DescribeLiveStreamPushInfoList": {
    "params": [
      {
        "name": "PushDomain",
        "desc": "Push domain name."
      },
      {
        "name": "AppName",
        "desc": "Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default."
      },
      {
        "name": "PageNum",
        "desc": "Number of pages,\nValue range: [1,10000],\nDefault value: 1."
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page,\nValue range: [1,1000],\nDefault value: 200."
      }
    ],
    "desc": "This API is used to query the push information of all real-time streams, including client IP, server IP, frame rate, bitrate, domain name, and push start time."
  },
  "DeleteLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "Template ID.\n1. Get from the returned value of the [CreateLiveSnapshotTemplate](https://intl.cloud.tencent.com/document/product/267/32624?from_cn_redirect=1) API call.\n2. You can query the list of created screencapturing templates through the [DescribeLiveSnapshotTemplates](https://intl.cloud.tencent.com/document/product/267/32619?from_cn_redirect=1) API."
      }
    ],
    "desc": "This API is used to delete a screencapturing template."
  }
}