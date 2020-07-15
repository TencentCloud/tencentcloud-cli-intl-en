# -*- coding: utf-8 -*-
DESC = "ocr-2018-11-19"
INFO = {
  "GeneralBasicOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "Base64-encoded value of image.\nThe image cannot exceed 7 MB in size after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported.\nEither `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used."
      },
      {
        "name": "ImageUrl",
        "desc": "URL address of image.\nThe image cannot exceed 7 MB in size after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported.\nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low."
      },
      {
        "name": "Scene",
        "desc": "Reserved field."
      },
      {
        "name": "LanguageType",
        "desc": "Language to be recognized.\nThe language can be automatically recognized or manually specified. Chinese-English mix (`zh`) is selected by default. Mixed characters in English and each supported language can be recognized together.\nValid values:\nzh\\auto\\jap\\kor\\nspa\\fre\\ger\\por\\nvie\\may\\rus\\ita\\nhol\\swe\\fin\\dan\\nnor\\hun\\tha\\lat\nValue meanings:\nChinese-English mix, automatic recognition, Japanese, Korean,\nSpanish, French, German, Portuguese,\nVietnamese, Malay, Russian, Italian,\nDutch, Swedish, Finnish, Danish,\nNorwegian, Hungarian, Thai, Latin."
      }
    ],
    "desc": "This API is used to detect and recognize characters in an image in the following 19 languages: Chinese, English, Japanese, Korean, Spanish, French, German, Portuguese, Vietnamese, Malay, Russian, Italian, Dutch, Swedish, Finnish, Danish, Norwegian, Hungarian, and Thai. Mixed characters in English and each supported language can be recognized together.\n\nIt can recognize printed text in paper documents, online images, ads, signboards, menus, video titles, profile photos, etc.\n\nProduct strengths: it can automatically recognize the text language, return the text box coordinate information, and automatically rotate tilted text to the upright direction.\n\nThe differences between different editions of general print recognition are as detailed below:\n<table style=\"width:715px\">\n      <thead>\n        <tr>\n          <th style=\"width:150px\"></th>\n          <th style=\"width:200px\">**(Recommended)** General Print Recognition</th>\n          <th ><a href=\"https://cloud.tencent.com/document/product/866/34937\">**(Recommended)** General Print Recognition (High-Precision)</a></th>\n          <th><a href=\"https://cloud.tencent.com/document/product/866/37831\">General Print Recognition (Simplified)</a></th>\n        </tr>\n      </thead>\n      <tbody>\n        <tr>\n          <td>Use case</td>\n          <td>It is suitable for recognition of printed text in all general scenarios</td>\n          <td>It is suitable for content with high recognition difficulty such as a large number of characters, long strings of digits, small characters, blurry characters, and tilted text</td>\n          <td>It is suitable for fast text recognition, which compromises the accuracy and recall rate but is more cost-effective</td>\n        </tr>\n        <tr>\n          <td>Recognition accuracy rate</td>\n          <td>96%</td>\n          <td>99%</td>\n          <td>91%</td>\n        </tr>\n        <tr>\n          <td>Price</td>\n          <td>Medium</td>\n          <td>High</td>\n          <td>Low</td>\n        </tr>\n        <tr>\n          <td>Supported languages</td>\n          <td>Chinese, English, Chinese-English, Japanese, Korean, Spanish, French, German, Portuguese, Vietnamese, Malay, Russian, Italian, Dutch, Swedish, Finnish, Danish, Norwegian, Hungarian, and Thai</td>\n          <td>Chinese, English, and Chinese-English</td>\n          <td>Chinese, English, and Chinese-English</td>\n        </tr>\n        <tr>\n          <td>Automatic language detection</td>\n          <td>Supported</td>\n          <td>Supported</td>\n          <td>Supported</td>\n        </tr>\n        <tr>\n          <td>Return of text line coordinates</td>\n          <td>Supported</td>\n          <td>Supported</td>\n          <td>Supported</td>\n        </tr>\n        <tr>\n          <td>Automatic rotation correction</td>\n          <td>Rotation recognition is supported, and the angle information can be returned</td>\n          <td>Rotation recognition is supported, but no angle information can be returned</td>\n          <td>Rotation recognition is supported, and the angle information can be returned</td>\n        </tr>\n      </tbody>\n    </table>"
  },
  "BankCardOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "Base64-encoded value of image.\nSupported image formats: PNG, JPG, JPEG. GIF is currently not supported.\nSupported image size: the downloaded image cannot exceed 7 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.\nEither the `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used."
      },
      {
        "name": "ImageUrl",
        "desc": "URL address of the image.\nSupported image formats: PNG, JPG, JPEG. GIF is currently not supported.\nSupported image size: the downloaded image cannot exceed 7 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.\nIt is recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.\nThe download speed and stability of non-Tencent Cloud URLs may be low."
      }
    ],
    "desc": "This API is used to detect and recognize key fields such as the card number, bank information, and expiration date on mainstream bank cards in Mainland China."
  },
  "MLIDCardOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "Base64-encoded value of an image.\nSupported image formats: PNG, JPG, JPEG. GIF is not supported at present.\nSupported image size: the downloaded image cannot exceed 3 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds."
      },
      {
        "name": "ImageUrl",
        "desc": "URL address of an image. (This field is not supported outside Mainland China)\nSupported image formats: PNG, JPG, JPEG. GIF is not supported at present.\nSupported image size: the downloaded image cannot exceed 3 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.\nIt is recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.\nThe download speed and stability of non-Tencent Cloud URLs may be low."
      },
      {
        "name": "RetImage",
        "desc": "Whether to return an image"
      }
    ],
    "desc": "This API is used to recognize a Malaysian identity card. Recognizable fields include identity card number, name, gender, and address. It has the features of cropping identity photos and alarming for photographed or photocopied documents.\nThis API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://cloud.tencent.com/about/connect).\n"
  },
  "MLIDPassportOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "Base64-encoded value of the image. The image cannot exceed 7 MB in size after being Base64-encoded. A resolution of 500x800 or above is recommended. Supported formats include PNG, JPG, JPEG, and BMP. It is recommended that the card part occupies more than 2/3 of the image.\nEither the `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used."
      },
      {
        "name": "RetImage",
        "desc": "Whether to return an image"
      }
    ],
    "desc": "This API is used to recognize a passport issued outside Mainland China. Recognizable fields include passport ID, name, date of birth, gender, expiration date, issuing country/region, and nationality. It has the features of cropping identity photos and alarming for spoofed or photocopied documents.\nThis API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://cloud.tencent.com/about/connect)."
  }
}