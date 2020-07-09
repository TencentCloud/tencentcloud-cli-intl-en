# -*- coding: utf-8 -*-
DESC = "mdp-2020-05-27"
INFO = {
  "ModifyMediaPackageChannelEndpoint": {
    "params": [
      {
        "name": "Id",
        "desc": "Channel ID."
      },
      {
        "name": "Url",
        "desc": "Channel endpoint URL."
      },
      {
        "name": "Name",
        "desc": "The channel name after modification."
      },
      {
        "name": "AuthInfo",
        "desc": "The channel authentication after modification."
      }
    ],
    "desc": "This API is used to modify an endpoint of a media package channel."
  },
  "DeleteMediaPackageChannels": {
    "params": [
      {
        "name": "Ids",
        "desc": "The ID list of channels to be deleted."
      }
    ],
    "desc": "This API is used to delete media package channels in batches."
  },
  "ModifyMediaPackageChannel": {
    "params": [
      {
        "name": "Id",
        "desc": "Channel ID."
      },
      {
        "name": "Name",
        "desc": "The channel name after modification."
      },
      {
        "name": "Protocol",
        "desc": "The channel protocol after modification. Valid values: HLS, DASH."
      }
    ],
    "desc": "This API is used to modify the information of a media package channel."
  },
  "ModifyMediaPackageChannelInputAuthInfo": {
    "params": [
      {
        "name": "Id",
        "desc": "Channel ID."
      },
      {
        "name": "Url",
        "desc": "Channel input URL."
      },
      {
        "name": "ActionType",
        "desc": "Authentication configuration type. Valid values: CLOSE, UPDATE.\nCLOSE: disable authentication.\nUPDATE: update authentication."
      }
    ],
    "desc": "This API is used to modify the input authentication information of a media package channel."
  },
  "DeleteMediaPackageChannelEndpoints": {
    "params": [
      {
        "name": "Id",
        "desc": "Channel ID."
      },
      {
        "name": "Urls",
        "desc": "The list of endpoint URLs."
      }
    ],
    "desc": "This API is used to delete endpoints from a media package channel in batches."
  },
  "DescribeMediaPackageChannels": {
    "params": [
      {
        "name": "PageNum",
        "desc": "Page number. Value range: [1, 1000]."
      },
      {
        "name": "PageSize",
        "desc": "The size of each page. Value range: [1, 1000]."
      }
    ],
    "desc": "This API is used to query the information list of media package channels."
  },
  "CreateMediaPackageChannel": {
    "params": [
      {
        "name": "Name",
        "desc": "Channel name."
      },
      {
        "name": "Protocol",
        "desc": "Channel protocol. Valid values: HLS, DASH."
      }
    ],
    "desc": "This API is used to create a media package channel."
  },
  "CreateMediaPackageChannelEndpoint": {
    "params": [
      {
        "name": "Id",
        "desc": "Channel ID."
      },
      {
        "name": "Name",
        "desc": "Channel name."
      },
      {
        "name": "AuthInfo",
        "desc": "Authentication information."
      }
    ],
    "desc": "This API is used to create an endpoint of a media package channel."
  },
  "DescribeMediaPackageChannel": {
    "params": [
      {
        "name": "Id",
        "desc": "Channel ID."
      }
    ],
    "desc": "This API is used to query the information of a media package channel."
  }
}