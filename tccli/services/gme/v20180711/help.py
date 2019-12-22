# -*- coding: utf-8 -*-
DESC = "gme-2018-07-11"
INFO = {
  "CreateApp": {
    "params": [
      {
        "name": "AppName",
        "desc": "Application name"
      },
      {
        "name": "ProjectId",
        "desc": "Tencent Cloud project ID. Default value: 0, which means that the default project is used"
      },
      {
        "name": "EngineList",
        "desc": "List of engines to be supported. Valid values: android, ios, unity, cocos, unreal, windows. All values are selected by default."
      },
      {
        "name": "RegionList",
        "desc": "List of service regions. Valid values: mainland (Mainland China), sa (South America), eu (Europe), oc (Australia), me (Middle East). All values are selected by default."
      },
      {
        "name": "RealtimeSpeechConf",
        "desc": "Configuration information of voice chat"
      },
      {
        "name": "VoiceMessageConf",
        "desc": "Configuration information of voice messaging and speech-to-text"
      },
      {
        "name": "VoiceFilterConf",
        "desc": "Configuration information of phrase analysis"
      },
      {
        "name": "Tags",
        "desc": "List of tags to be added"
      }
    ],
    "desc": "This API is used to create a GME application."
  },
  "ModifyAppStatus": {
    "params": [
      {
        "name": "BizId",
        "desc": "Application ID, which is generated and returned by the backend after application creation"
      },
      {
        "name": "Status",
        "desc": "Application status. Valid values: open, close"
      }
    ],
    "desc": "This API is used to change the status of an application's master switch."
  },
  "DescribeAppStatistics": {
    "params": [
      {
        "name": "BizId",
        "desc": "GME application ID"
      },
      {
        "name": "StartDate",
        "desc": "Data start date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13"
      },
      {
        "name": "EndDate",
        "desc": "Data end date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13"
      },
      {
        "name": "Services",
        "desc": "List of services to be queried. Valid values: RealTimeSpeech, VoiceMessage, VoiceFilter"
      }
    ],
    "desc": "This API is used to get the usage statistics of a GME application, including those of voice chat, voice messaging and speech-to-text, phrase analysis, etc. The maximum query period is the past 30 days."
  }
}