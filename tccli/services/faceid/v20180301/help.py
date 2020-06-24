# -*- coding: utf-8 -*-
DESC = "faceid-2018-03-01"
INFO = {
  "LivenessCompare": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "Base64 value of a photo for face comparison;\nBase64-encoded image data is up to 3 MB. Only JPG and PNG formats are supported."
      },
      {
        "name": "VideoBase64",
        "desc": "Base64 value of a video for liveness detection;\nThe size after Base64-encoding cannot exceed 5 MB. MP4, AVI, and FLV formats are supported."
      },
      {
        "name": "LivenessType",
        "desc": "Liveness detection type. Valid values: LIP/ACTION/SILENT.\nLIP: numeric mode; ACTION: motion mode; SILENT: silent mode. You need to select a mode to input."
      },
      {
        "name": "ValidateData",
        "desc": "Input parameter for the numeric mode: numeric verification code (1234). An API needs to be called first to get a numeric verification code;\nInput parameter for the motion mode: motion order (2,1 or 1,2). An API needs to be called first to get the motion order;\nInput parameter for silent mode: empty."
      },
      {
        "name": "Optional",
        "desc": "This parameter does not need to be passed in for this API."
      }
    ],
    "desc": "This API is used to pass in a video and a photo, determine whether the person in the video is real, and if yes, then determine whether the person in the video is the same as that in the photo."
  }
}