# -*- coding: utf-8 -*-
DESC = "trtc-2019-07-22"
INFO = {
  "CreateTroubleInfo": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "Application ID"
      },
      {
        "name": "RoomId",
        "desc": "Room ID"
      },
      {
        "name": "TeacherUserId",
        "desc": "Teacher user ID"
      },
      {
        "name": "StudentUserId",
        "desc": "Student user ID"
      },
      {
        "name": "TroubleUserId",
        "desc": "ID of the user (teacher or student) with exception."
      },
      {
        "name": "TroubleType",
        "desc": "Exception type.\n1: exceptional video\n2: exceptional audio\n3: exceptional video and audio\n5: exceptional room entry\n4: course switch\n6: help seeking\n7: problem feedback\n8: complaint"
      },
      {
        "name": "TroubleTime",
        "desc": "UNIX timestamp when the exception occurred in seconds."
      },
      {
        "name": "TroubleMsg",
        "desc": "Exception details"
      }
    ],
    "desc": "This API is used to create exception information."
  },
  "DescribeHistoryScale": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "User `sdkappid`"
      },
      {
        "name": "StartTime",
        "desc": "Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 5 days."
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of local UNIX timestamp, such as 1588031999s."
      }
    ],
    "desc": "This API is used to query the daily numbers of rooms and users under a specified `SDKAppID`. It can query data once per minute for the last 14 days. If a day has not ended, the numbers of rooms and users on the day cannot be queried."
  },
  "DescribeRealtimeQuality": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 24 hours."
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of local UNIX timestamp, such as 1588031999s."
      },
      {
        "name": "SdkAppId",
        "desc": "User `sdkappid`"
      },
      {
        "name": "DataType",
        "desc": "Type of data to query\nenterTotalSuccPercent: room entry success rate;\nfistFreamInSecRate: instant playback rate of the first frame;\nblockPercent: video lag rate;\naudioBlockPercent: audio lag rate."
      }
    ],
    "desc": "This API is used to query real-time quality data for the last 24 hours according to `sdkappid`, including the room entry success rate, instant playback rate of the first frame, audio lag rate, and video lag rate. The query time range cannot exceed 1 hour."
  },
  "StartMCUMixTranscode": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "`SDKAppId` of TRTC."
      },
      {
        "name": "RoomId",
        "desc": "Room ID."
      },
      {
        "name": "OutputParams",
        "desc": "On-Cloud MixTranscoding output control parameters."
      },
      {
        "name": "EncodeParams",
        "desc": "On-Cloud MixTranscoding output encoding parameters."
      },
      {
        "name": "LayoutParams",
        "desc": "On-Cloud MixTranscoding output layout parameters."
      }
    ],
    "desc": "This API is used to enable On-Cloud MixTranscoding and specify the layout position of each channel of video image in the mixed video image.\n\nThere may be multiple channels of audio/video streams in a TRTC room. You can call this API to request the Tencent Cloud server to combine multiple channels of video images into one channel, specify the position of each channel, and mix the multiple channels of audio so as to output one channel of audio/video stream for easier recording and live streaming.\n\nYou can use this API to perform the following operations:\n- Set the image and audio quality parameters of the final live stream, including video resolution, video bitrate, video frame rate, and audio quality.\n- Set the image layout, i.e., positions of all channels of images. You only need to set the layout once when enabling On-Cloud MixTranscoding, and the layout engine will automatically arrange the video images in the configured layout in subsequent operations.\n- Set the recording file name for future playback.\n- Set the CDN live stream ID for live streaming over CDN.\n\nCurrently, the following layout templates are supported:\n- Floating template: the entire screen will be covered by the video image of the first user who enters the room, and the video images of other users will be displayed as small images in horizontal rows from the bottom-left corner in room entry sequence. The screen can contain up to 4 rows with 4 small images each row, which float over the big image. Up to 1 big image and 15 small images are supported. If a user sends audio only, the user will still use an image spot.\n- Grid template: the screen is divided into user video images with the same dimensions. The more the users, the smaller the image dimensions. Up to 16 images are supported. If a user sends audio only, the user will still use an image spot.\n- Screen sharing template: it is suitable for video conferencing and online education. The shared screen (or camera of the anchor) is always displayed in the big image on the left of the screen, and the video images of other users are vertically displayed on the right in up to 2 columns with up to 8 small images in each column. Up to 1 big image and 15 small images are supported. If width and height of the upstream image’s resolution don’t match those of the output image, the big image on the left will be scaled to display it as a whole, while the small images on the right will be cropped.\n- Picture-in-picture template: it is suitable for mixing a pair of big/small images or a big image with the audio of other users. The small image floats over the big image, and the users in the big/small images and the display position of the small image can be specified."
  },
  "DescribeRealtimeScale": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 24 hours."
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of local UNIX timestamp, such as 1588031999s."
      },
      {
        "name": "SdkAppId",
        "desc": "User `sdkappid`"
      },
      {
        "name": "DataType",
        "desc": "Type of data to query\n`UserNum: number of users in call;\nRoomNum: number of rooms."
      }
    ],
    "desc": "This API is used to query the real-time scale for the last 24 hours according to `sdkappid`. The query time range cannot exceed 1 hour."
  },
  "DescribeRealtimeNetwork": {
    "params": [
      {
        "name": "StartTime",
        "desc": "Query start time in the format of UNIX timestamp, such as 1588031999s, which is a point in time in the last 24 hours."
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of local UNIX timestamp, such as 1588031999s."
      },
      {
        "name": "SdkAppId",
        "desc": "User `sdkappid`"
      },
      {
        "name": "DataType",
        "desc": "Type of data to query\nsendLossRateRaw: upstream packet loss rate;\nrecvLossRateRaw: downstream packet loss rate."
      }
    ],
    "desc": "This API is used to query real-time network status for the last 24 hours according to `sdkappid`, including upstream and downstream packet losses. The query time range cannot exceed 1 hour."
  },
  "DescribeRoomInformation": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "User `sdkappid`"
      },
      {
        "name": "StartTime",
        "desc": "Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 5 days."
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of local UNIX timestamp, such as 1588031999s."
      },
      {
        "name": "RoomId",
        "desc": "Room ID of uint type"
      },
      {
        "name": "PageNumber",
        "desc": "Page index starting from 0 (if either `PageNumber` or `PageSize` is left empty, 10 data entries will be returned by default)"
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page (if either `PageNumber` or `PageSize` is left empty, 10 data entries will be returned by default. Maximum value: 100)"
      }
    ],
    "desc": "This API is used to query the room list under a specified `SDKAppID`. It returns 10 calls by default and up to 100 calls at a time. It can query data for the last 14 days."
  },
  "RemoveUser": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "`SDKAppId` of TRTC."
      },
      {
        "name": "RoomId",
        "desc": "Room number."
      },
      {
        "name": "UserIds",
        "desc": "List of up to 10 users to be removed."
      }
    ],
    "desc": "This API is used to remove a user from a room. It is applicable to scenarios where the anchor, room owner, or admin wants to kick out a user. It supports all platforms. For Android, iOS, Windows, and macOS, the TRTC SDK needs to be upgraded to v6.6 or above."
  },
  "DescribeCallDetail": {
    "params": [
      {
        "name": "CommId",
        "desc": "Unique ID of a call: sdkappid_roomgString_createTime. The `roomgString` refers to the room ID, and `createTime` refers to the creation time of a room in the format of UNIX timestamp in seconds, such as 1400353843_218695_1590065777. Its value can be obtained from the `DescribeRoomInformation` API (related document: https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1)."
      },
      {
        "name": "StartTime",
        "desc": "Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 5 days."
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of local UNIX timestamp, such as 1588031999s."
      },
      {
        "name": "SdkAppId",
        "desc": "User `sdkappid`, such as 1400188366."
      },
      {
        "name": "UserIds",
        "desc": "User array to query, which contains up to 6 users. If it is left empty, 6 users will be returned by default."
      },
      {
        "name": "DataType",
        "desc": "Metric to query. The user list will be returned if it is left empty; all metrics will be returned if its value is `all`.\nappCpu: CPU utilization of the application;\nsysCpu: CPU utilization of the system;\naBit: upstream/downstream audio bitrate;\naBlock: audio lag duration;\nbigvBit: upstream/downstream video bitrate;\nbigvCapFps: frame rate for capturing videos;\nbigvEncFps: frame rate for sending videos;\nbigvDecFps: rendering frame rate;\nbigvBlock: video lag duration;\naLoss: upstream/downstream audio packet loss;\nbigvLoss: upstream/downstream video packet loss;\nbigvWidth: upstream/downstream resolution in width;\nbigvHeight: upstream/downstream resolution in height."
      },
      {
        "name": "PageNumber",
        "desc": "Page index starting from 0. If either `PageNumber` or `PageSize` is left empty, 6 data entries will be returned by default."
      },
      {
        "name": "PageSize",
        "desc": "Number of entries per page. If either `PageNumber` or `PageSize` is left empty, 6 data entries will be returned by default. When `DataType` and all `UserId`s are not null, `PageSize` is up to 6. When `DataType` and all `UserId`s are null, `PageSize` is up to 100."
      }
    ],
    "desc": "This API is used to query user list and call quality data within a specified time. It queries data in last 14 days. When `DataType` is not null, real-time data of up to 1 hour and up to 6 users can be queried. The query period can start and end on different days. When `DataType` and all `UserId`s are null, data of 6 users will be queried by default. Data of up to 100 users can be displayed on one page (`PageSize` is up to 100)."
  },
  "DescribeDetailEvent": {
    "params": [
      {
        "name": "CommId",
        "desc": "Unique ID of a call: sdkappid_roomgString_createTime. The `roomgString` refers to the room ID, and `createTime` refers to the creation time of a room in the format of UNIX timestamp in seconds. Its value can be obtained from the `DescribeRoomInformation` API (related document: https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1)."
      },
      {
        "name": "StartTime",
        "desc": "Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 5 days."
      },
      {
        "name": "EndTime",
        "desc": "Query end time in the format of local UNIX timestamp, such as 1588031999s."
      },
      {
        "name": "UserId",
        "desc": "User ID"
      },
      {
        "name": "RoomId",
        "desc": "Room ID"
      }
    ],
    "desc": "This API is used to query a user’s activity details such as room entry/exit and video enablement/disablement during a call. It can query data for the last 14 days."
  },
  "DescribeAbnormalEvent": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "User `SDKAppID`, which can be used to query 20 exceptional experience events (in one or more rooms)"
      },
      {
        "name": "StartTime",
        "desc": "Query start time"
      },
      {
        "name": "EndTime",
        "desc": "Query end time"
      },
      {
        "name": "RoomId",
        "desc": "Room ID, which can be used to query up to 20 exceptional experience events in a specific room"
      }
    ],
    "desc": "This API is used to query exception occurrences under a specified `SDKAppID` and return the exception ID and possible causes. It queries data in last 5 days, and the query period is up to 1 hour which can start and end on different days. For more information about exceptions, please see the exception ID mapping table: https://intl.cloud.tencent.com/document/product/647/37906"
  },
  "StopMCUMixTranscode": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "`SDKAppId` of TRTC."
      },
      {
        "name": "RoomId",
        "desc": "Room ID."
      }
    ],
    "desc": "This API is used to end On-Cloud MixTranscoding."
  },
  "DismissRoom": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "`SDKAppId` of TRTC."
      },
      {
        "name": "RoomId",
        "desc": "Room number."
      }
    ],
    "desc": "This API is used to remove all users from a room and dismiss the room. It supports all platforms. For Android, iOS, Windows, and macOS, the TRTC SDK needs to be upgraded to v6.6 or above."
  }
}