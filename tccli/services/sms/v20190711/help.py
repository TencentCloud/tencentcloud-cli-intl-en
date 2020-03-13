# -*- coding: utf-8 -*-
DESC = "sms-2019-07-11"
INFO = {
  "DeleteSmsTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "ID of template to be deleted."
      }
    ],
    "desc": "This API is used to delete an SMS template."
  },
  "AddSmsSign": {
    "params": [
      {
        "name": "SignName",
        "desc": "Signature name."
      },
      {
        "name": "SignType",
        "desc": "Signature type. Each of these types is followed by their `DocumentType` (identity document type) option:\n0: company (0, 1, 2, 3).\n1: app (0, 1, 2, 3, 4).\n2: website (0, 1, 2, 3, 5).\n3: WeChat Official Account or WeChat Mini Program (0, 1, 2, 3, 6).\n4: trademark (7).\n5: governmental/public institution or others (2, 3).\nNote: the identity document type must be selected according to the correspondence; otherwise, the review will fail."
      },
      {
        "name": "DocumentType",
        "desc": "Identity document type:\n0: 3-in-1 license.\n1: business license.\n2: organization code certificate.\n3: certificate of unified social credit code.\n4: screenshot of application backend management (for personal app).\n5: screenshot of website ICP filing backend (for personal website).\n6: screenshot of WeChat Mini Program settings page (for personal WeChat Mini Program).\n7: trademark registration certificate."
      },
      {
        "name": "International",
        "desc": "Whether it is Global SMS:\n0: Mainland China SMS.\n1: Global SMS."
      },
      {
        "name": "UsedMethod",
        "desc": "Signature use:\n0: for self-use.\n1: for others."
      },
      {
        "name": "ProofImage",
        "desc": "You should Base64-encode the image of the identity document corresponding to the signature first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter."
      },
      {
        "name": "CommissionImage",
        "desc": "Authorization letter, which should be submitted if `UsedMethod` is for others.\nYou should Base64-encode the image first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.\nNote: this field will take effect only when `UsedMethod` is 1 (for others)."
      },
      {
        "name": "Remark",
        "desc": "Signature application remarks."
      }
    ],
    "desc": "This API is used to add an SMS signature."
  },
  "PullSmsSendStatus": {
    "params": [
      {
        "name": "Limit",
        "desc": "Maximum number of pulled entries. Maximum value: 100."
      },
      {
        "name": "SmsSdkAppid",
        "desc": "SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666."
      }
    ],
    "desc": "This API is used to pull SMS delivery status."
  },
  "SendSms": {
    "params": [
      {
        "name": "PhoneNumberSet",
        "desc": "Target mobile numbers in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number). Up to 200 mobile numbers are supported."
      },
      {
        "name": "TemplateID",
        "desc": "Template ID. You must enter the ID of an approved template, which can be viewed in the [SMS Console](https://console.cloud.tencent.com/sms/smslist)."
      },
      {
        "name": "SmsSdkAppid",
        "desc": "SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666."
      },
      {
        "name": "Sign",
        "desc": "The content of SMS signature should be encoded in UTF-8. You must enter an approved signature, which can be viewed in the [SMS Console](https://console.cloud.tencent.com/sms/smslist). Note: this parameter is required for Mainland China SMS."
      },
      {
        "name": "TemplateParamSet",
        "desc": "Template parameter. If there is no template parameter, leave this parameter blank."
      },
      {
        "name": "ExtendCode",
        "desc": "SMS code number extension, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://cloud.tencent.com/document/product/382/3773)."
      },
      {
        "name": "SessionContext",
        "desc": "User session content, which can carry context information such as user-side ID and will be returned as-is by the server."
      },
      {
        "name": "SenderId",
        "desc": "`senderid` for Global SMS, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://cloud.tencent.com/document/product/382/3773) for assistance. This parameter should be empty for Mainland China SMS."
      }
    ],
    "desc": "This API is used to send SMS verification codes, notification, or marketing messages to users.\n\n"
  },
  "ModifySmsSign": {
    "params": [
      {
        "name": "SignId",
        "desc": "ID of signature to be modified."
      },
      {
        "name": "SignName",
        "desc": "Signature name."
      },
      {
        "name": "SignType",
        "desc": "Signature type. Each of these types is followed by their `DocumentType` (identity document type) option:\n0: company (0, 1, 2, 3).\n1: app (0, 1, 2, 3, 4).\n2: website (0, 1, 2, 3, 5).\n3: WeChat Official Account or WeChat Mini Program (0, 1, 2, 3, 6).\n4: trademark (7).\n5: governmental/public institution or others (2, 3).\nNote: the identity document type must be selected according to the correspondence; otherwise, the review will fail."
      },
      {
        "name": "DocumentType",
        "desc": "Identity document type:\n0: 3-in-1 license.\n1: business license.\n2: organization code certificate.\n3: certificate of unified social credit code.\n4: screenshot of application backend management (for personal app).\n5: screenshot of website ICP filing backend (for personal website).\n6: screenshot of WeChat Mini Program settings page (for personal WeChat Mini Program).\n7: trademark registration certificate."
      },
      {
        "name": "International",
        "desc": "Whether it is Global SMS:\n0: Mainland China SMS.\n1: Global SMS."
      },
      {
        "name": "UsedMethod",
        "desc": "Signature use:\n0: for self-use.\n1: for others."
      },
      {
        "name": "ProofImage",
        "desc": "You should Base64-encode the image of the identity document corresponding to the signature first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter."
      },
      {
        "name": "CommissionImage",
        "desc": "Authorization letter, which should be submitted if `UsedMethod` is for others.\nYou should Base64-encode the image first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.\nNote: this field will take effect only when `UsedMethod` is 1 (for others)."
      },
      {
        "name": "Remark",
        "desc": "Signature application remarks."
      }
    ],
    "desc": "This API is used to modify an SMS signature."
  },
  "SmsPackagesStatistics": {
    "params": [
      {
        "name": "SmsSdkAppid",
        "desc": "SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666."
      },
      {
        "name": "Limit",
        "desc": "Upper limit (number of packages to be pulled)."
      },
      {
        "name": "Offset",
        "desc": "Offset.\nNote: this parameter is currently fixed at 0."
      }
    ],
    "desc": "This API is used to collect statistics on user's packages."
  },
  "SendStatusStatistics": {
    "params": [
      {
        "name": "StartDateTime",
        "desc": "Start time of pull in the format of `yyyymmddhh` accurate to the hour."
      },
      {
        "name": "EndDataTime",
        "desc": "End time of pull in the format of `yyyymmddhh` accurate to the hour\nNote: `EndDataTime` must be later than `StartDateTime`."
      },
      {
        "name": "SmsSdkAppid",
        "desc": "SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666."
      },
      {
        "name": "Limit",
        "desc": "Upper limit.\nNote: this parameter is currently fixed at 0."
      },
      {
        "name": "Offset",
        "desc": "Offset.\nNote: this parameter is currently fixed at 0."
      }
    ],
    "desc": "This API is used to collect statistics on SMS sent by users."
  },
  "CallbackStatusStatistics": {
    "params": [
      {
        "name": "StartDateTime",
        "desc": "Start time of pull in the format of `yyyymmddhh` accurate to the hour."
      },
      {
        "name": "EndDataTime",
        "desc": "End time of pull in the format of `yyyymmddhh` accurate to the hour.\nNote: `EndDataTime` must be later than `StartDateTime`."
      },
      {
        "name": "SmsSdkAppid",
        "desc": "SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666."
      },
      {
        "name": "Limit",
        "desc": "Upper limit.\nNote: this parameter is currently fixed at 0."
      },
      {
        "name": "Offset",
        "desc": "Offset.\nNote: this parameter is currently fixed at 0."
      }
    ],
    "desc": "This API is used to collect statistics on user receipts."
  },
  "DescribeSmsTemplateList": {
    "params": [],
    "desc": ">⚠️注意:个人认证用户不支持使用 API 查询短信正文模版,请参阅了解 [实名认证基本介绍](https://cloud.tencent.com/document/product/378/3629)."
  },
  "PullSmsReplyStatus": {
    "params": [
      {
        "name": "Limit",
        "desc": "Maximum number of pulled entries. Maximum value: 100."
      },
      {
        "name": "SmsSdkAppid",
        "desc": "SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666."
      }
    ],
    "desc": "This API is used to pull SMS reply status."
  },
  "DescribeSmsSignList": {
    "params": [],
    "desc": ">⚠️注意:个人认证用户不支持使用 API 查询短信签名,请参阅了解 [实名认证基本介绍](https://cloud.tencent.com/document/product/378/3629)."
  },
  "PullSmsSendStatusByPhoneNumber": {
    "params": [
      {
        "name": "SendDateTime",
        "desc": "Pull start time in seconds in the format of UNIX timestamp."
      },
      {
        "name": "Offset",
        "desc": "Offset.\nNote: this parameter is currently fixed at 0."
      },
      {
        "name": "Limit",
        "desc": "Maximum number of pulled entries. Maximum value: 100."
      },
      {
        "name": "PhoneNumber",
        "desc": "Target mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number)."
      },
      {
        "name": "SmsSdkAppid",
        "desc": "SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666."
      }
    ],
    "desc": "This API is used to pull SMS delivery status for one single number."
  },
  "ModifySmsTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "ID of template to be modified."
      },
      {
        "name": "TemplateName",
        "desc": "New template name."
      },
      {
        "name": "TemplateContent",
        "desc": "New template content."
      },
      {
        "name": "SmsType",
        "desc": "SMS type. 0: ordinary SMS, 1: marketing SMS."
      },
      {
        "name": "International",
        "desc": "Whether it is Global SMS:\n0: Mainland China SMS.\n1: Global SMS."
      },
      {
        "name": "Remark",
        "desc": "Template remarks, such as reason for application and use case."
      }
    ],
    "desc": "This API is used to modify an SMS template."
  },
  "PullSmsReplyStatusByPhoneNumber": {
    "params": [
      {
        "name": "SendDateTime",
        "desc": "Pull start time in seconds in the format of UNIX timestamp."
      },
      {
        "name": "Offset",
        "desc": "Offset.\nNote: this parameter is currently fixed at 0."
      },
      {
        "name": "Limit",
        "desc": "Maximum number of pulled entries. Maximum value: 100."
      },
      {
        "name": "PhoneNumber",
        "desc": "Target mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number)."
      },
      {
        "name": "SmsSdkAppid",
        "desc": "SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666."
      }
    ],
    "desc": "This API is used to pull SMS reply status for one single number."
  },
  "DeleteSmsSign": {
    "params": [
      {
        "name": "SignId",
        "desc": "ID of signature to be deleted."
      }
    ],
    "desc": "This API is used to delete an SMS signature."
  },
  "AddSmsTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "Template name."
      },
      {
        "name": "TemplateContent",
        "desc": "Template content."
      },
      {
        "name": "SmsType",
        "desc": "SMS type. 0: ordinary SMS, 1: marketing SMS."
      },
      {
        "name": "International",
        "desc": "Whether it is Global SMS:\n0: Mainland China SMS.\n1: Global SMS."
      },
      {
        "name": "Remark",
        "desc": "Template remarks, such as reason for application and use case."
      }
    ],
    "desc": "This API is used to add an SMS template."
  }
}