# -*- coding: utf-8 -*-
DESC = "ocr-2018-11-19"
INFO = {
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
    "desc": "This API is used to detect and recognize key fields such as the card number, bank information, and expiration date on mainstream bank cards in Mainland China.\n\nThis API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales)."
  },
  "TableOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "Base64-encoded value of image.\nSupported image formats: PNG, JPG, JPEG. GIF is not supported at present.\nSupported image size: the downloaded image cannot exceed 3 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.\nEither `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used."
      },
      {
        "name": "ImageUrl",
        "desc": "URL address of image.\nSupported image formats: PNG, JPG, JPEG. GIF is not supported at present.\nSupported image size: the downloaded image cannot exceed 3 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.\nWe recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.\nThe download speed and stability of non-Tencent Cloud URLs may be low."
      }
    ],
    "desc": "This API is used to detect and recognize Chinese and English forms in images. It can return the text content of each cell and save the recognition result as Excel.\n\nThis API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales)."
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
    "desc": "This API is used to recognize a Malaysian identity card. Recognizable fields include identity card number, name, gender, and address. It has the features of cropping identity photos and alarming for photographed or photocopied documents.\n\nThis API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales)."
  },
  "MLIDPassportOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "Base64-encoded value of image. The image cannot exceed 7 MB in size after being Base64-encoded. A resolution above 500x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies more than 2/3 area of the image."
      },
      {
        "name": "RetImage",
        "desc": "Whether to return an image. Default value: false."
      }
    ],
    "desc": "This API is used to recognize a passport issued in Hong Kong/Macao/Taiwan (China) or other countries/regions. Recognizable fields include passport ID, name, date of birth, gender, expiration date, issuing country/region, and nationality. It has the features of cropping identity photos and alarming for photographed or photocopied documents.\n\nThis API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales)."
  },
  "GeneralAccurateOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "Base64-encoded value of image.\nThe image cannot exceed 7 MB in size after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported.\nEither `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used."
      },
      {
        "name": "ImageUrl",
        "desc": "URL address of image.\nThe image cannot exceed 7 MB in size after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported.\nWe recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low."
      }
    ],
    "desc": "This API is used to detect and recognize characters in an image. It can recognize Chinese, English, Chinese-English, digits, and special symbols and return the text box positions and characters.\n\nIt is suitable for scenarios with a lot of characters in complex layouts and requiring high recognition accuracy, such as examination papers, online images, signboards, and legal documents.\n\nStrengths: compared with general print recognition, it provides higher-precision character recognition services. Its accuracy and recall rate are higher in difficult scenarios such as a large number of characters, long strings of digits, small characters, blurry characters, and tilted text.\n\nThis API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales)."
  },
  "HKIDCardOCR": {
    "params": [
      {
        "name": "DetectFake",
        "desc": "Whether to check for authenticity."
      },
      {
        "name": "ReturnHeadImage",
        "desc": "Whether to return identity photo."
      },
      {
        "name": "ImageBase64",
        "desc": "Base64-encoded value of image.\nSupported image formats: PNG, JPG, JPEG. GIF is currently not supported.\nSupported image size: the downloaded image cannot exceed 3 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds."
      },
      {
        "name": "ImageUrl",
        "desc": "URL of the image.\nSupported image formats: PNG, JPG, JPEG. GIF is currently not supported.\nSupported image size: the downloaded image cannot exceed 3 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.\nWe recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.\nThe download speed and stability of non-Tencent Cloud URLs may be low."
      }
    ],
    "desc": "This API is used to recognize key fields on the photo side of a Hong Kong (China) identity card, including name in Chinese, name in English, telecode for name, date of birth, gender, document symbol, date of the first issue, date of the last receipt, identity card number, and permanent residency attribute. It can check for card authenticity and crop the identity photo.\n\nThis API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).\n"
  },
  "GeneralBasicOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "Base64-encoded value of image/PDF.\nThe image/PDF cannot exceed 7 MB in size after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.\nEither `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used."
      },
      {
        "name": "ImageUrl",
        "desc": "URL address of image/PDF.\nThe image/PDF cannot exceed 7 MB in size after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.\nWe recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low."
      },
      {
        "name": "Scene",
        "desc": "Reserved field."
      },
      {
        "name": "LanguageType",
        "desc": "Language to be recognized.\nThe language can be automatically recognized or manually specified. Chinese-English mix (`zh`) is selected by default. Mixed characters in English and each supported language can be recognized together.\nValid values:\nzh\\auto\\jap\\kor\\\nspa\\fre\\ger\\por\\\nvie\\may\\rus\\ita\\\nhol\\swe\\fin\\dan\\\nnor\\hun\\tha\\lat\\ara\nValue meanings:\nChinese-English mix, automatic recognition, Japanese, Korean,\nSpanish, French, German, Portuguese,\nVietnamese, Malay, Russian, Italian,\nDutch, Swedish, Finnish, Danish,\nNorwegian, Hungarian, Thai, Latin,\nArabic."
      },
      {
        "name": "IsPdf",
        "desc": "Whether to enable PDF recognition. Default value: false. After this feature is enabled, both images and PDF files can be recognized at the same time."
      },
      {
        "name": "PdfPageNumber",
        "desc": "Page number of the PDF page that needs to be recognized. Only one single PDF page can be recognized. This parameter is valid if the uploaded file is a PDF and the value of the `IsPdf` parameter is `true`. Default value: 1."
      }
    ],
    "desc": "This API is used to detect and recognize characters in an image in the following 20 languages: Chinese, English, Japanese, Korean, Spanish, French, German, Portuguese, Vietnamese, Malay, Russian, Italian, Dutch, Swedish, Finnish, Danish, Norwegian, Hungarian, Thai, and Arabic. Mixed characters in English and each supported language can be recognized together.\n\nIt can recognize printed text in paper documents, online images, ads, signboards, menus, video titles, profile photos, etc.\n\nStrengths: it can automatically recognize the text language, return the text box coordinate information, and automatically rotate tilted text to the upright direction.\n\nThis API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales)."
  }
}