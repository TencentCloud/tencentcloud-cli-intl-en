# -*- coding: utf-8 -*-
DESC = "tiw-2019-09-19"
INFO = {
  "SetOnlineRecordCallback": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the customer"
      },
      {
        "name": "Callback",
        "desc": "Callback address of the real-time recording task result. If an empty string is passed in, the existing callback address will be deleted. The callback address only supports the HTTP or HTTPS protocol, so the callback address must start with `http://` or `https://`. For the callback format, please [see here](https://intl.cloud.tencent.com/document/product/1137/40258?from_cn_redirect=1)."
      }
    ],
    "desc": "This API is used to set the real-time recording callback address. For the callback format, please [see here](https://intl.cloud.tencent.com/document/product/1137/40258?from_cn_redirect=1)."
  },
  "SetTranscodeCallbackKey": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the application"
      },
      {
        "name": "CallbackKey",
        "desc": "Authentication key for the document transcoding callback. It is a string that can have up to 64 characters. If an empty string is passed in, the existing callback authentication key will be deleted. For more information about callback authentication, please [see here](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1)."
      }
    ],
    "desc": "This API is used to set the callback authentication key for document transcoding. For more information, see [Event Notification](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1)."
  },
  "DescribeTranscode": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the customer"
      },
      {
        "name": "TaskId",
        "desc": "Unique ID of the document transcoding task"
      }
    ],
    "desc": "This API is used to query the progress and result of a document transcoding task."
  },
  "CreateTranscode": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the customer"
      },
      {
        "name": "Url",
        "desc": "Address of the file for transcoding"
      },
      {
        "name": "IsStaticPPT",
        "desc": "Whether the PowerPoint file is static. The default value is False.\nIf IsStaticPPT is False, documents with the .ppt or .pptx extension will be dynamically transcoded to HTML5 pages, and documents with other extensions will be statically transcoded to images. If IsStaticPPT is True, documents with any extensions will be statically transcoded to images."
      },
      {
        "name": "MinResolution",
        "desc": "Minimum resolution of the transcoded document. If no value or null is specified for it or the resolution format is invalid, the original document resolution is used.\n\n "
      },
      {
        "name": "ThumbnailResolution",
        "desc": "Resolution of the thumbnail generated for the dynamically transcoded PowerPoint file. If no value or null is specified for it or the resolution format is invalid, no thumbnail will be generated. The resolution format is the same as that of MinResolution.\n\nFor static transcoding, this parameter does not work."
      },
      {
        "name": "CompressFileType",
        "desc": "Compression format of the transcoded file. If no value or null is specified for it or the specified format is invalid, no compression file will be generated. Currently, the following compression formats are supported:\n\n`zip`: generates a .zip compression package.\n`tar.gz: generates a .tar.gz compression package."
      }
    ],
    "desc": "This API is used to create a document transcoding task."
  },
  "StartOnlineRecord": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the customer"
      },
      {
        "name": "RoomId",
        "desc": "ID of the room for recording. Value range: (1, 4294967295)"
      },
      {
        "name": "RecordUserId",
        "desc": "User ID used by the real-time recording service for entering a room. Its format is `tic_record_user_${RoomId}_${Random}`, where `${RoomId}` indicates the ID of the room for recording and `${Random}` is a random string.\nThe ID must be an unused ID in the SDK. The real-time recording service uses the user ID to enter the room for audio, video, and whiteboard recording. If this ID is already used in the SDK, the SDK and recording service will conflict, affecting the recording operation."
      },
      {
        "name": "RecordUserSig",
        "desc": "Signature corresponding to RecordUserId"
      },
      {
        "name": "GroupId",
        "desc": "(Disused) IM group ID of the whiteboard. By default, it is the same as the room ID."
      },
      {
        "name": "Concat",
        "desc": "Real-time recording video splicing parameter"
      },
      {
        "name": "Whiteboard",
        "desc": "Real-time recording whiteboard parameter, such as the whiteboard width and height"
      },
      {
        "name": "MixStream",
        "desc": "Real-time recording stream mixing parameter\nNotes:\n1. The stream mixing feature needs to be enabled separately. If you need the feature, contact TIW customer service.\n2. To use the stream mixing feature, the Extras parameter is required and must contain \"MIX_STREAM\"."
      },
      {
        "name": "Extras",
        "desc": "List of advanced features used\nList of possible values:\nMIX_STREAM - Stream mixing feature"
      },
      {
        "name": "AudioFileNeeded",
        "desc": "Whether to return the audio-only recording file of different streams in the result callback. The file format is mp3."
      },
      {
        "name": "RecordControl",
        "desc": "A group of real-time recording parameters. It specifies the streams to be recorded, whether to disable the audio recording, and whether to record only low-resolution videos, etc."
      }
    ],
    "desc": "This API is used to start a real-time recording task."
  },
  "StopOnlineRecord": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the customer"
      },
      {
        "name": "TaskId",
        "desc": "ID of the recording task to stop"
      }
    ],
    "desc": "This API is used to stop real-time recording."
  },
  "PauseOnlineRecord": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the customer"
      },
      {
        "name": "TaskId",
        "desc": "ID of the real-time recording task"
      }
    ],
    "desc": "This API is used to pause real-time recording."
  },
  "SetTranscodeCallback": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the customer"
      },
      {
        "name": "Callback",
        "desc": "Callback address for the document transcoding progress. If an empty string is passed in, the existing callback address will be deleted. The callback address only supports the HTTP or HTTPS protocol, so the callback address must start with `http://` or `https://`.\nFor more information about the callback format, please [see here](https://intl.cloud.tencent.com/document/product/1137/40260?from_cn_redirect=1)."
      }
    ],
    "desc": "This API is used to set the callback address for document transcoding. For the callback format, please [see here](https://intl.cloud.tencent.com/document/product/1137/40260?from_cn_redirect=1)."
  },
  "SetOnlineRecordCallbackKey": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the application"
      },
      {
        "name": "CallbackKey",
        "desc": "Authentication key for the real-time recording callback. It is a string that can have up to 64 characters. If an empty string is passed in, the existing callback authentication key will be deleted. For more information, please [see here](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1)."
      }
    ],
    "desc": "This API is used to set the callback authentication key for real-time recording. For more information, see [Event Notification](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1)."
  },
  "ResumeOnlineRecord": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the customer"
      },
      {
        "name": "TaskId",
        "desc": "ID of the resumed real-time recording task"
      }
    ],
    "desc": "This API is used to resume real-time recording."
  },
  "DescribeOnlineRecordCallback": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the application"
      }
    ],
    "desc": "This API is used to query the real-time recording callback address."
  },
  "DescribeTranscodeCallback": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the application"
      }
    ],
    "desc": "This API is used to query the document transcoding callback address."
  },
  "DescribeOnlineRecord": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "SdkAppId of the customer"
      },
      {
        "name": "TaskId",
        "desc": "ID of the real-time recording task"
      }
    ],
    "desc": "This API is used to query the status and result of a real-time recording task."
  }
}