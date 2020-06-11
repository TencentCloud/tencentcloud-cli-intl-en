# -*- coding: utf-8 -*-
DESC = "trtc-2019-07-22"
INFO = {
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
    "desc": "This API is used to query the number of historical rooms and users for the last 5 days. It can query once per minute."
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
        "desc": "Page index. If it is left empty, 10 entries will be returned by default."
      },
      {
        "name": "PageSize",
        "desc": "Page size. Maximum value: 100. If it is left empty, 10 entries will be returned by default."
      }
    ],
    "desc": "This API is used to query the room list for the last 5 days according to `sdkappid`. It returns 10 calls by default and up to 100 calls at a time."
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
        "desc": "Call ID (unique call ID): sdkappid_roomgString (room ID)_createTime (room creation time in UNIX timestamp in seconds). You can get the parameter value through the `DescribeRoomInformation` API which is used to query the room list."
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
        "desc": "User `sdkappid`"
      },
      {
        "name": "UserIds",
        "desc": "User array to query, which contains up to 6 users. If it is left empty, 6 users will be returned by default."
      },
      {
        "name": "DataType",
        "desc": "Metric to query. The user list will be returned if it is left empty; all metrics will be returned if its value is `all`.\nappCpu: CPU utilization of application;\nsysCpu: CPU utilization of system;\naBit: upstream/downstream audio bitrate;\naBlock: audio lag duration;\nvBit: upstream/downstream video bitrate;\nvCapFps: video capturing frame rate;\nvEncFps: video sending frame rate;\nvDecFps: rendering frame rate;\nvBlock: video lag duration;\naLoss: upstream/downstream audio packet loss;\nvLoss: upstream/downstream video packet loss;\nvWidth: upstream/downstream resolution in width;\nvHeight: upstream/downstream resolution in height."
      }
    ],
    "desc": "This API is used to query the user list and user call quality data in a specified time period. It can query data of up to 6 users for the last 5 days, and the query time range cannot exceed 1 hour."
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