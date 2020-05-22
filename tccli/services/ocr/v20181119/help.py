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
    "desc": "This API is used to detect and recognize key fields such as the card number, bank information, and expiration date on mainstream bank cards in Mainland China."
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
  }
}