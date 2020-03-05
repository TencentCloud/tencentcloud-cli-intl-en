# -*- coding: utf-8 -*-
DESC = "trtc-2019-07-22"
INFO = {
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