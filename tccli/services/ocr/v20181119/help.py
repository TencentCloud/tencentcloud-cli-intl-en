# -*- coding: utf-8 -*-
DESC = "ocr-2018-11-19"
INFO = {
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
        "desc": "Base64-encoded value of an image.\nSupported image formats: PNG, JPG, JPEG. GIF is not supported at present.\nSupported image size: the downloaded image cannot exceed 3 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds."
      },
      {
        "name": "RetImage",
        "desc": "Whether to return an image"
      }
    ],
    "desc": "This API is used to recognize a Malaysian passport. Recognizable fields include passport ID, name, date of birth, gender, expiration date, issuing country, and nationality. It has the features of cropping identity photos and alarming for photographed or photocopied documents.\nThis API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://cloud.tencent.com/about/connect)."
  }
}