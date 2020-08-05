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
        "desc": "Tencent Cloud project ID. Default value: 0, which means the default project"
      },
      {
        "name": "EngineList",
        "desc": "List of engines to be supported. All values are selected by default."
      },
      {
        "name": "RegionList",
        "desc": "Service region list. All values are selected by default."
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
        "desc": "Application ID, which is generated and returned by the backend after application creation."
      },
      {
        "name": "Status",
        "desc": "Application status. Valid values: open, close"
      }
    ],
    "desc": "This API is used to change the status of an application's primary switch."
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
  },
  "DescribeScanResultList": {
    "params": [
      {
        "name": "BizId",
        "desc": "Application ID, which is the `AppID` obtained when you create an application in the [console](https://console.cloud.tencent.com/gamegme)"
      },
      {
        "name": "TaskIdList",
        "desc": "List of IDs of the tasks to be queried. Up to 100 entries can be added in the ID list."
      },
      {
        "name": "Limit",
        "desc": "Number of task results to be returned. Default value: 10. Maximum value: 500. This parameter will be ignored for large file tasks where all results will be returned"
      }
    ],
    "desc": "This API is used to query the speech detection result. Up to 100 tasks can be added in the task query list.\n<p style=\"color:red\">If the `Callback` field is not set when a speech detection task is submitted, this API will be needed to get the detection result.</p>"
  },
  "ScanVoice": {
    "params": [
      {
        "name": "BizId",
        "desc": "Application ID, which is the `AppID` obtained when you create an application in [Console > Service Management](https://console.cloud.tencent.com/gamegme)"
      },
      {
        "name": "Scenes",
        "desc": "Speech detection scenario. The value of this parameter is currently required to be `default`. Preset scenarios: abusive, pornographic, politically sensitive, advertising, terrorism, and prohibited scenarios. For specific values, please see the <a href=\"#Label_Value\">Label description</a> above."
      },
      {
        "name": "Live",
        "desc": "Whether it is a live stream. false: audio file detection, true: audio stream detection."
      },
      {
        "name": "Tasks",
        "desc": "Speech detection task list. Up to 100 tasks can be added in the list. The structure contains:\n<li>DataId: unique data ID</li>\n<li>Url: URL-encoded data file URL, which is a pull address if the detected speech is a stream</li>"
      },
      {
        "name": "Callback",
        "desc": "Async callback address for detection result. For more information, please see the <a href=\"#Callback_Declare\">callback description</a> above. (Note: if this field is empty, the detection result can only be obtained by calling the `DescribeScanResultList` API.)"
      }
    ],
    "desc": "This API is used to submit a speech detection task. Up to 100 tasks can be added in the detection task list. Before using this API, please enable the speech analysis service in [Console > Service Configuration](https://console.cloud.tencent.com/gamegme/conf).\n</br></br>\n\n<h4><b>Feature trial description:</b></h4>\n<li>You can try out the speech analysis service free of charge in <a href=\"https://console.cloud.tencent.com/gamegme/tryout\">Console > Product Trial</a>.</li>\n</br>\n\n<h4><b>API feature description:</b></h4>\n<li>This API can check audio streams or files for non-compliant content.</li>\n<li>The detection result can be obtained by setting the callback address (`Callback`) or calling the `DescribeScanResultList` API for polling.</li>\n<li>The scenario can be specified, such as abusive, pornographic, or politically sensitive information.</li>\n<li>Detection tasks can be submitted in batches. Up to 100 tasks can be added in the detection task list.</li>\n</br>\n<h4><b>Audio file limit description:</b></h4>\n<li>Audio file size limit: 100 MB</li>\n<li>Audio file duration limit: 30 minutes</li>\n<li>Supported audio file formats: .wav, .m4a, .amr, .mp3, .aac, .wma, .ogg</li>\n</br>\n<h4><b>Audio stream limit description:</b></h4>\n<li>Supported audio stream formats: .m3u8, .flv</li>\n<li>Supported audio stream transfer protocols: RTMP, HTTP, HTTPS</li>\n<li>Audio stream duration limit: 4 hours</li>\n<li>Audio/video stream separation and audio stream analysis are supported</li>\n</br>\n<h4 id=\"Label_Value\"><b>`Scenes` and `Label` parameter description:</b></h4>\n<p>When submitting a speech detection task, you need to specify the `Scenes` parameter. <font color=\"red\">You are currently required to set the `Scenes` parameter to `[\"default\"]`</font>. The detection result will contain the scenario specified at the time of request and detection result in the corresponding type.</p>\n<table>\n<thread>\n<tr>\n<th>Scenario</th>\n<th>Description</th>\n<th>Label</th>\n</tr>\n</thread>\n<tbody>\n<tr>\n<td>Speech detection</td>\n<td>Speech detection type</td>\n<td>\n<p>normal: normal</p>\n<p>porn: pornographic</p>\n<p>politics: politically sensitive</p>\n<p>abuse: abusive</p>\n<p>ad: advertising</p>\n<p>terrorism: terrorism</p>\n<p>contraband: prohibited</p>\n<p>customized: custom keyword library. This feature is only available to allowlisted users. To try it out, please <a href=\"https://cloud.tencent.com/apply/p/8809fjcik56\">contact us</a>.</p>\n</td>\n</tr>\n</tbody>\n</table>\n</br>\n<h4 id=\"Callback_Declare\"><b>Callback description:</b></h4>\n<li>If the callback address parameter `Callback` (i.e., the URL of an HTTP(S) API) is specified in the request parameters, then the POST method should be supported and transferred data should be encoded with UTF-8.</li>\n<li>After the callback data is pushed, if the HTTP status code received is 200, the push is successful.</li>\n<li>HTTP header parameter description:</li>\n<table>\n<thread>\n<tr>\n<th>Name</th>\n<th>Type</th>\n<th>Required</th>\n<th>Description</th>\n</tr>\n</thread>\n<tbody>\n<tr>\n<td>Signatue</td>\n<td>string</td>\n<td>Yes</td>\n<td>Signature. For more information, please see <a href=\"#Callback_Signatue\">Signature generation description</a>.</td>\n</tr>\n</tbody>\n</table>\n<ul  id=\"Callback_Signatue\">\n\t<li>Signature generation description:</li>\n\t<ul>\n\t\t<li>The HMAC-SH1 algorithm should be used, and the result should be encoded with Base64;</li>\n\t\t<li>The original signature string is the entire JSON content of POST and body (the length is subject to `Content-Length`);</li>\n\t\t<li>The signature key is the `SecretKey` of the application, which can be viewed in the console.</li>\n\t</ul>\n</ul>\n\n<li>Below is a sample callback <font color=\"red\">(for more information on the fields, please see the structure:\n<a href=\"https://cloud.tencent.com/document/api/607/35375#DescribeScanResult\" target=\"_blank\">DescribeScanResult</a>)</font>:</li>\n<pre><code>{\n\t\"Code\": 0,\n\t\"DataId\": \"1400000000_test_data_id\",\n\t\"ScanFinishTime\": 1566720906,\n\t\"HitFlag\": true,\n\t\"Live\": false,\n\t\"Msg\": \"\",\n\t\"ScanPiece\": [{\n\t\t\"DumpUrl\": \"\",\n\t\t\"HitFlag\": true,\n\t\t\"MainType\": \"abuse\",\n\t\t\"RoomId\": \"123\",\n\t\t\"OpenId\": \"xxx\",\n\t\t\"Info\":\"\",\n\t\t\"Offset\": 0,\n\t\t\"Duration\": 3400,\n\t\t\"PieceStartTime\":1574684231,\n\t\t\"ScanDetail\": [{\n\t\t\t\"EndTime\": 1110,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 1110\n\t\t}, {\n\t\t\t\"EndTime\": 1380,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 930\n\t\t}, {\n\t\t\t\"EndTime\": 1560,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 930\n\t\t}, {\n\t\t\t\"EndTime\": 2820,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 2490\n\t\t}]\n\t}],\n\t\"ScanStartTime\": 1566720905,\n\t\"Scenes\": [\n\t\t\"default\"\n\t],\n\t\"Status\": \"Success\",\n\t\"TaskId\": \"xxx\",\n\t\"Url\": \"https://xxx/xxx.m4a\"\n}\n</code></pre>"
  }
}