# -*- coding: utf-8 -*-
DESC = "mdl-2020-03-26"
INFO = {
  "CreateMediaLiveInputSecurityGroup": {
    "params": [
      {
        "name": "Name",
        "desc": "Input security group name, which can contain letters, digits, and underscores and must be unique at the region level."
      },
      {
        "name": "Whitelist",
        "desc": "List of allowlist entries. Quantity limit: [1,10]."
      }
    ],
    "desc": "This API is used to create an input security group. Up to 5 ones can be created."
  },
  "DescribeMediaLiveChannelLogs": {
    "params": [
      {
        "name": "ChannelId",
        "desc": "Channel ID."
      },
      {
        "name": "StartTime",
        "desc": "Log start time, which is one hour ago by default. Maximum value: the last 7 days.\nUTC time, such as `2020-01-01T12:00:00Z`."
      },
      {
        "name": "EndTime",
        "desc": "Log end time, which is one hour after `StartTime` by default.\nUTC time, such as `2020-01-01T12:00:00Z`."
      }
    ],
    "desc": "This API is used to query MediaLive channel logs, such as push event logs."
  },
  "DescribeMediaLiveChannelOutputStatistics": {
    "params": [
      {
        "name": "ChannelId",
        "desc": "Channel ID."
      },
      {
        "name": "StartTime",
        "desc": "Statistics start time, which is one hour ago by default. Maximum value: the last 7 days.\nUTC time, such as `2020-01-01T12:00:00Z`."
      },
      {
        "name": "EndTime",
        "desc": "Statistics end time, which is one hour after `StartTime` by default.\nUTC time, such as `2020-01-01T12:00:00Z`."
      },
      {
        "name": "Period",
        "desc": "Data interval. Valid values: 5s, 1min, 5min, 15min. Default value: 1min."
      }
    ],
    "desc": "This API is used to query the output statistics of a channel."
  },
  "DeleteMediaLiveInput": {
    "params": [
      {
        "name": "Id",
        "desc": "Media input ID."
      }
    ],
    "desc": "This API is used to delete a media input."
  },
  "ModifyMediaLiveInput": {
    "params": [
      {
        "name": "Id",
        "desc": "Media input ID."
      },
      {
        "name": "Name",
        "desc": "Media input name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "List of IDs of bound security groups."
      },
      {
        "name": "InputSettings",
        "desc": "Input settings information.\nOne or two sets of settings need to be configured for RTMP_PUSH/RTMP_PULL/HLS_PULL/MP4_PULL.\nThis parameter can be left empty for RTP_PUSH and UDP_PUSH.\nNote: if it is left empty or the array is empty, the original `InputSettings` value will be used."
      }
    ],
    "desc": "This API is used to update a media input."
  },
  "DescribeMediaLiveInputSecurityGroups": {
    "params": [],
    "desc": "This API is used to query the information of input security groups in batches."
  },
  "DescribeMediaLiveInputs": {
    "params": [],
    "desc": "This API is used to query the information of media inputs in batches."
  },
  "DeleteMediaLiveInputSecurityGroup": {
    "params": [
      {
        "name": "Id",
        "desc": "Input security group ID."
      }
    ],
    "desc": "This API is used to delete an input security group."
  },
  "CreateMediaLiveChannel": {
    "params": [
      {
        "name": "Name",
        "desc": "Channel name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level."
      },
      {
        "name": "AttachedInputs",
        "desc": "Associated media input. Quantity limit: [1,1]."
      },
      {
        "name": "OutputGroups",
        "desc": "Configuration information of channel output groups. Quantity limit: [1,10]."
      },
      {
        "name": "AudioTemplates",
        "desc": "Audio transcoding template array. Quantity limit: [1,20]."
      },
      {
        "name": "VideoTemplates",
        "desc": "Video transcoding template array. Quantity limit: [1,10]."
      }
    ],
    "desc": "This API is used to create a media channel."
  },
  "DescribeMediaLiveChannelAlerts": {
    "params": [
      {
        "name": "ChannelId",
        "desc": "Channel ID."
      }
    ],
    "desc": "This API is used to query the channel alarm information."
  },
  "DescribeMediaLiveChannel": {
    "params": [
      {
        "name": "Id",
        "desc": "Channel ID."
      }
    ],
    "desc": "This API is used to query the information of a MediaLive channel."
  },
  "ModifyMediaLiveInputSecurityGroup": {
    "params": [
      {
        "name": "Id",
        "desc": "Input security group ID."
      },
      {
        "name": "Name",
        "desc": "Input security group name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level."
      },
      {
        "name": "Whitelist",
        "desc": "List of allowlist entries. Up to 10 entries are allowed."
      }
    ],
    "desc": "This API is used to update an input security group."
  },
  "CreateMediaLiveInput": {
    "params": [
      {
        "name": "Name",
        "desc": "Media input name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level."
      },
      {
        "name": "Type",
        "desc": "Media input type.\nValid values: RTMP_PUSH/RTP_PUSH/UDP_PUSH/RTMP_PULL/HLS_PULL/MP4_PULL."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "ID of the input security group to be bound.\nOnly one security group can be associated."
      },
      {
        "name": "InputSettings",
        "desc": "Input settings information, one or two sets of which need to be configured for RTMP_PUSH/RTMP_PULL/HLS_PULL/MP4_PULL."
      }
    ],
    "desc": "This API is used to create a media input."
  },
  "StartMediaLiveChannel": {
    "params": [
      {
        "name": "Id",
        "desc": "Channel ID."
      }
    ],
    "desc": "This API is used to start a MediaLive channel."
  },
  "ModifyMediaLiveChannel": {
    "params": [
      {
        "name": "Id",
        "desc": "Channel ID."
      },
      {
        "name": "Name",
        "desc": "Channel name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level."
      },
      {
        "name": "AttachedInputs",
        "desc": "Associated media input. Quantity limit: [1,1]."
      },
      {
        "name": "OutputGroups",
        "desc": "Configuration information of channel output groups. Quantity limit: [1,10]."
      },
      {
        "name": "AudioTemplates",
        "desc": "Audio transcoding template array. Quantity limit: [1,20]."
      },
      {
        "name": "VideoTemplates",
        "desc": "Video transcoding template array. Quantity limit: [1,10]."
      }
    ],
    "desc": "This API is used to modify the information of a MediaLive channel."
  },
  "DeleteMediaLiveChannel": {
    "params": [
      {
        "name": "Id",
        "desc": "Channel ID."
      }
    ],
    "desc": "This API is used to delete a MediaLive channel."
  },
  "DescribeMediaLiveChannelInputStatistics": {
    "params": [
      {
        "name": "ChannelId",
        "desc": "Channel ID."
      },
      {
        "name": "StartTime",
        "desc": "Statistics start time, which is one hour ago by default. Maximum value: the last 7 days.\nUTC time, such as `2020-01-01T12:00:00Z`."
      },
      {
        "name": "EndTime",
        "desc": "Statistics end time, which is one hour after `StartTime` by default.\nUTC time, such as `2020-01-01T12:00:00Z`."
      },
      {
        "name": "Period",
        "desc": "Data interval. Valid values: 5s, 1min, 5min, 15min. Default value: 1min."
      }
    ],
    "desc": "This API is used to query the input statistics."
  },
  "DescribeMediaLiveChannels": {
    "params": [],
    "desc": "This API is used to query the information of MediaLive channels in batches."
  },
  "DescribeMediaLiveInputSecurityGroup": {
    "params": [
      {
        "name": "Id",
        "desc": "Input security group ID."
      }
    ],
    "desc": "This API is used to query an input security group."
  },
  "DescribeMediaLiveInput": {
    "params": [
      {
        "name": "Id",
        "desc": "Media input ID."
      }
    ],
    "desc": "This API is used to query a media input."
  },
  "StopMediaLiveChannel": {
    "params": [
      {
        "name": "Id",
        "desc": "Channel ID."
      }
    ],
    "desc": "This API is used to stop a MediaLive channel."
  }
}