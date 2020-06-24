# -*- coding: utf-8 -*-
DESC = "iai-2020-03-03"
INFO = {
  "DeletePersonFromGroup": {
    "params": [
      {
        "name": "PersonId",
        "desc": "Person ID"
      },
      {
        "name": "GroupId",
        "desc": "Group ID"
      }
    ],
    "desc": "This API is used to remove a person from a specified group. This operation only affects the group. If the person exists only in the group, the person will be deleted, and all face information of the person will also be deleted."
  },
  "SearchFacesReturnsByGroup": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "List of groups to be searched in. Up to 60 groups are supported."
      },
      {
        "name": "Image",
        "desc": "Base64-encoded image data, which cannot exceed 5 MB.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "Url",
        "desc": "Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` must be provided; if both are provided, only `Url` will be used.\nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.\nThe download speed and stability of non-Tencent Cloud URLs may be low.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "MaxFaceNum",
        "desc": "Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10.\n`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized.\nFor example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized."
      },
      {
        "name": "MinFaceSize",
        "desc": "Minimum height and width of face in px. Default value: 34. A value below 34 will affect the search accuracy. You are recommended to set this parameter to 80."
      },
      {
        "name": "MaxPersonNumPerGroup",
        "desc": "Detected faces, which is corresponding to the maximum number of returned most matching persons. Default value: 5. Maximum value: 10.  \nFor example, if `MaxFaceNum` is 3 and `MaxPersonNum` is 5, up to 15 (3 * 5) persons will be returned."
      },
      {
        "name": "NeedPersonInfo",
        "desc": "Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default"
      },
      {
        "name": "QualityControl",
        "desc": "Image quality control. \n0: no control. \n1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. \n2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. \n3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. \n4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. \nDefault value: 0. \nIf the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory."
      },
      {
        "name": "FaceMatchThreshold",
        "desc": "In the output parameter `Score`, the result will be returned only if the result value is greater than or equal to the `FaceMatchThreshold` value.\nDefault value: 0.\nValue range: [0.0,100.0)."
      },
      {
        "name": "NeedRotateDetection",
        "desc": "Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled."
      }
    ],
    "desc": "This API is used to recognize top K persons in one or more groups who are similar to the person in a given image, display the results **by group**, and rank the similarity within each group in a descending order.\n\nUp to 10 faces in the image can be recognized at a time, and cross-group search is supported.\n\nThe maximum number of faces in a group that can be searched for at a time is subject to the group's algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.\n\nThis API recognizes each face of a person as an independent one. By contrast, the [SearchPersons](https://cloud.tencent.com/document/product/867/38881) and [SearchPersonsReturnsByGroup](https://cloud.tencent.com/document/product/867/38880) APIs fuse the features of all faces of a person; for example, if a person has 4 faces, they will fuse the features of the 4 faces and generate the summarized facial features of the person to make the search more accurate.\n\nThis API should be used together with the [CreateGroup API](https://cloud.tencent.com/document/product/867/32794).\n\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.\n\n"
  },
  "CreateGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "Group name, which is modifiable, must be unique, and can contain 1–60 characters."
      },
      {
        "name": "GroupId",
        "desc": "Group ID, which is unmodifiable, must be unique, and can contain letters, digits, and special symbols (-%@#&_) of up to 64B."
      },
      {
        "name": "GroupExDescriptions",
        "desc": "Custom group description field that describes the person attributes in the group, which will be applied to all persons in the group. \nUp to 5 ones can be created. \nEach custom description field can contain 1–30 characters. \nThe custom description field must be unique in the group. \nExample: if you set the \"custom description field\" of a group to [\"student ID\",\"employee ID\",\"mobile number\"], \nthen all the persons in the group will have description fields named \"student ID\", \"employee ID\", and \"mobile number\". \nYou can enter content in the corresponding field to register a person's student ID, employee ID, and mobile number."
      },
      {
        "name": "Tag",
        "desc": "Group remarks, which can contain 0–40 characters."
      },
      {
        "name": "FaceModelVersion",
        "desc": "Algorithm model version used by the Face Recognition service. Valid values: 2.0, 3.0.\nThis parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API previously, `2.0` will be used by default. \nDifferent algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is thus recommended."
      }
    ],
    "desc": "This API is used to create an empty group. If the group already exists, an error will be returned.\nCustom description fields can be created as needed to describe persons in the group.\n\nA maximum of 100,000 groups or 50 million faces can be created under one `APPID`.\n\nThe maximum number of faces that can be included in one group varies by algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0."
  },
  "GetCheckSimilarPersonJobIdList": {
    "params": [
      {
        "name": "Offset",
        "desc": "Starting number. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 10. Maximum value: 1000."
      }
    ],
    "desc": "This API is used to get the list of duplicate person check tasks and sort them in reverse order by task creation time (i.e., the newest one is at the top)\n\nOnly data in the past year is retained."
  },
  "GetPersonBaseInfo": {
    "params": [
      {
        "name": "PersonId",
        "desc": "Person ID"
      }
    ],
    "desc": "This API is used to get the information of a specified person, including name, gender, face, etc."
  },
  "DetectLiveFace": {
    "params": [
      {
        "name": "Image",
        "desc": "Base64-encoded image data, which cannot exceed 5 MB. (The aspect ratio of the image should be close to 3:4 (width:height); otherwise, the score returned for the image will be meaningless.)\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "Url",
        "desc": "Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` must be provided; if both are provided, only `Url` will be used. \n(The aspect ratio of the image should be close to 3:4 (width:height); otherwise, the score returned for the image will be meaningless.) \nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. \nThe download speed and stability of non-Tencent Cloud URLs may be low.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "FaceModelVersion",
        "desc": "Algorithm model version used by the Face Recognition service. Valid values: 2.0, 3.0.  \nThis parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API previously, `2.0` will be used by default. \nDifferent algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is thus recommended."
      }
    ],
    "desc": "This API is used to detect the liveness of a user with a user-uploaded image. Its difference from video-based liveness detection lies in that the user does not need to speak, shake their head, or wink for detection.\n\nImage-based liveness detection is suitable for scenarios where the image is a selfie or the requirement for attack defense is not high. If you have a higher security requirement for liveness detection, please use [Faceid](https://cloud.tencent.com/product/faceid).\n\n>     \n- The aspect ratio of the image should be close to 3:4 (width:height); otherwise, the score returned for the image will be meaningless. This API is suitable for selfie scenarios, and the score returned in other scenarios will be meaningless.\n\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`."
  },
  "CreateFace": {
    "params": [
      {
        "name": "PersonId",
        "desc": "Person ID."
      },
      {
        "name": "Images",
        "desc": "Base64-encoded image data, which cannot exceed 5 MB.\nThere can be up to 5 faces in one image.\nIf there are multiple faces in the image, only the face with the largest size will be selected.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "Urls",
        "desc": "Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  \nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. \nThe download speed and stability of non-Tencent Cloud URLs may be low.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.\nThere can be up to 5 faces in one image.\nIf there are multiple faces in the image, only the face with the largest size will be selected."
      },
      {
        "name": "FaceMatchThreshold",
        "desc": "Only faces whose similarity to an existing face of the person is above the value of `FaceMatchThreshold` can be added successfully. \nDefault value: 60. Value range: [0,100]."
      },
      {
        "name": "QualityControl",
        "desc": "Image quality control. \n0: no control. \n1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. \n2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. \n3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. \n4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. \nDefault value: 0. \nIf the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory."
      },
      {
        "name": "NeedRotateDetection",
        "desc": "Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled."
      }
    ],
    "desc": "This API is used to add a set of face images to a person. One person can have up to 5 images. If a person exists in multiple groups, the images will be added to all those groups for the person.\n\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`."
  },
  "GetPersonListNum": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Group ID"
      }
    ],
    "desc": "This API is used to get the number of persons in a specified group."
  },
  "GetPersonGroupInfo": {
    "params": [
      {
        "name": "PersonId",
        "desc": "Person ID"
      },
      {
        "name": "Offset",
        "desc": "Starting number. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 10. Maximum value: 100"
      }
    ],
    "desc": "This API is used to get the information of a specified person, including group, description, etc."
  },
  "AnalyzeFace": {
    "params": [
      {
        "name": "Mode",
        "desc": "Detection mode. 0: detect all faces that appear; 1: detect the largest face. Default value: 0. The facial feature localization information (facial keypoints) of up to 10 faces can be returned."
      },
      {
        "name": "Image",
        "desc": "Base64-encoded image data, which cannot exceed 5 MB.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "Url",
        "desc": "Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  \nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. \nThe download speed and stability of non-Tencent Cloud URLs may be low.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "FaceModelVersion",
        "desc": "Algorithm model version used by the Face Recognition service. Valid values: 2.0, 3.0.  \nThis parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API previously, `2.0` will be used by default.  \nDifferent algorithm model versions correspond to different face recognition algorithms. The new version has a better overall effect than the legacy version and is thus recommended."
      },
      {
        "name": "NeedRotateDetection",
        "desc": "Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled."
      }
    ],
    "desc": "This API is used to perform facial feature localization (aka facial keypoint localization) on a given image and calculate 90 facial keypoints that make up the contour of the face, including eyebrows (8 points on the left and 8 on the right), eyes (8 points on the left and 8 on the right), nose (13 points), mouth (22 points), face contour (21 points), and eyeballs or pupils (2 points).\n\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`."
  },
  "ModifyPersonBaseInfo": {
    "params": [
      {
        "name": "PersonId",
        "desc": "Person ID"
      },
      {
        "name": "PersonName",
        "desc": "Name of the person to be modified"
      },
      {
        "name": "Gender",
        "desc": "Gender of the person to be modified"
      }
    ],
    "desc": "This API is used to modify the information of a person, including name, gender, etc. The changes of person name and gender will be synced to all the groups that contain the person."
  },
  "SearchFaces": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "List of groups to be searched in. Up to 100 groups are supported."
      },
      {
        "name": "Image",
        "desc": "Base64-encoded image data, which cannot exceed 5 MB.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "Url",
        "desc": "Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  \nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. \nThe download speed and stability of non-Tencent Cloud URLs may be low.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "MaxFaceNum",
        "desc": "Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10. \n`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized. \nFor example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized."
      },
      {
        "name": "MinFaceSize",
        "desc": "Minimum height and width of face in px. Default value: 34. Face images whose value is below 34 cannot be recognized. You are recommended to set this parameter to 80."
      },
      {
        "name": "MaxPersonNum",
        "desc": "Number of the most similar persons returned for faces recognized in one single image. Default value: 5. Maximum value: 100. \nFor example, if `MaxFaceNum` is 1 and `MaxPersonNum` is 8, information of the top 8 most similar persons will be returned.\nThe greater the value, the longer the processing time. You are recommended to set a value below 10."
      },
      {
        "name": "NeedPersonInfo",
        "desc": "Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default"
      },
      {
        "name": "QualityControl",
        "desc": "Image quality control. \n0: no control. \n1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. \n2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. \n3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. \n4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. \nDefault value: 0. \nIf the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory."
      },
      {
        "name": "FaceMatchThreshold",
        "desc": "In the output parameter `Score`, the result will be returned only if the result value is above the `FaceMatchThreshold` value. Default value: 0."
      },
      {
        "name": "NeedRotateDetection",
        "desc": "Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled."
      }
    ],
    "desc": "This API is used to recognize top K persons in one or more groups who are similar to the person in a given image and rank the similarity in a descending order.\n\nUp to 10 faces in an image can be recognized at a time, and up to 100 groups can be searched in at a time.\n\nThe maximum number of faces in a group that can be searched for at a time is subject to the group's algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.\n\nThis API recognizes each face of a person as an independent one. By contrast, the [SearchPersons](https://cloud.tencent.com/document/product/867/38881) and [SearchPersonsReturnsByGroup](https://cloud.tencent.com/document/product/867/38880) APIs fuse the features of all faces of a person; for example, if a person has 4 faces, they will fuse the features of the 4 faces and generate the summarized facial features of the person to make the search more accurate.\n\n\nThis API should be used together with the [CreateGroup API](https://cloud.tencent.com/document/product/867/32794).\n\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`."
  },
  "CopyPerson": {
    "params": [
      {
        "name": "PersonId",
        "desc": "Person ID"
      },
      {
        "name": "GroupIds",
        "desc": "List of the groups to add to."
      }
    ],
    "desc": "This API is used to copy a person in a group to another group (without copying the description). One person can exist in up to 100 groups at the same time.\n>     \n- Note: if the version of the algorithm model was 2.0 when the person was created, the copy operation will fail if it is to copy to a group not on algorithm model v2.0."
  },
  "CheckSimilarPerson": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "List of groups to be checked. \nThere can be up to 2 million persons in one group and up to 10 groups."
      },
      {
        "name": "UniquePersonControl",
        "desc": "Control over the strictness of duplicate person check.\n1: archive sorting with high strictness, which can eliminate more duplicate identities but leads to higher false elimination rate for non-duplicate identities.\n2: archive sorting with low strictness, which leads to lower false elimination rate for non-duplicate identities and lower elimination rate for duplicate identities."
      }
    ],
    "desc": "This API is used to check a specified group for suspected duplicate persons and list their information.\n\nYou can use this API to check for duplicate persons in one group so as to avoid situations where the same person has multiple roles in the group. You can also use it to check for duplicate persons across multiple groups to see whether the same person exists in multiple groups at the same time.\n\nDuplicate check across algorithm model versions is not supported. Currently, this feature is available only to groups with algorithm model v3.0.\n\n>     \n- If you perform a duplicate check on the same group again, you need to wait for the last operation to complete, that is, when the `GroupIds` entered in the two requests are the same, if the first request is not completed, the second request will fail.\n\n>     \n- The status of the group on which the duplicate check is to be performed is that when the duplicate check task really starts, that is, after you initiate the duplicate check request; if your duplicate check task needs to queue up, any addition or deletion operation performed on the group during the queuing will affect the duplicate check result. Tencent Cloud will use the group status when the duplicate check task actually starts. After the task starts, any operation on the group will not affect the task execution; however, you are still recommended not to add/delete persons or faces to/from the group after the task starts."
  },
  "DeleteGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Group ID."
      }
    ],
    "desc": "This API is used to delete a group and all persons in it. Meanwhile, all face information corresponding to the persons will be deleted. If a person exists in multiple groups at the same time, deleting a group will not delete the person, but the custom description field information in the group will be deleted. Custom description field information in other groups will not be affected.\n"
  },
  "DeletePerson": {
    "params": [
      {
        "name": "PersonId",
        "desc": "Person ID"
      }
    ],
    "desc": "This API is used to delete a person from all groups. Meanwhile, all face information of the person will be deleted."
  },
  "ModifyGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Group ID"
      },
      {
        "name": "GroupName",
        "desc": "Group name"
      },
      {
        "name": "GroupExDescriptionInfos",
        "desc": "Custom description field of the group to be modified, which is a `key-value`"
      },
      {
        "name": "Tag",
        "desc": "Group remarks"
      }
    ],
    "desc": "This API is used to modify the name, tag, and custom description field of a group."
  },
  "GetSimilarPersonResult": {
    "params": [
      {
        "name": "JobId",
        "desc": "Duplicate check task ID, which is used to query and get the progress and result of the task."
      }
    ],
    "desc": "This API is used to get the result of the `CheckSimilarPerson` API."
  },
  "CreatePerson": {
    "params": [
      {
        "name": "GroupId",
        "desc": "ID of the group to add to."
      },
      {
        "name": "PersonName",
        "desc": "Person name, which can contain 1–60 characters and is modifiable and repeatable."
      },
      {
        "name": "PersonId",
        "desc": "Person ID, which is unmodifiable, must be unique under a Tencent Cloud account, and can contain letters, digits, and special symbols (-%@#&_) of up to 64B."
      },
      {
        "name": "Gender",
        "desc": "0: empty; 1: male; 2: female."
      },
      {
        "name": "PersonExDescriptionInfos",
        "desc": "Content of person description field, which is a `key-value` pair, can contain 0–60 characters, and is modifiable and repeatable."
      },
      {
        "name": "Image",
        "desc": "Base64-encoded image data, which cannot exceed 5 MB.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "Url",
        "desc": "Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  \nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. \nThe download speed and stability of non-Tencent Cloud URLs may be low.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "UniquePersonControl",
        "desc": "This parameter is used to control the judgment whether the face contained in the image in `Image` or `Url` corresponds to an existing person in the group. \nIf it is judged that a duplicate person exists in the group, no new person will be created, and information of the suspected duplicate person will be returned. \nOtherwise, the new person will be created. \n0: do not judge, i.e., the person will be created no matter whether a duplicate person exists in the group. \n1: low duplicate person judgment requirement (1% FAR); \n2: average duplicate person judgment requirement (0.1% FAR); \n3: high duplicate person judgment requirement (0.01% FAR); \n4: very high duplicate person judgment requirement (0.001% FAR). \nDefault value: 0.  \nNote: the higher the requirement, the lower the probability of duplicate person. The FARs corresponding to different requirements are for reference only and can be adjusted as needed."
      },
      {
        "name": "QualityControl",
        "desc": "Image quality control. \n0: no control. \n1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. \n2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. \n3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. \n4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. \nDefault value: 0. \nIf the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory."
      },
      {
        "name": "NeedRotateDetection",
        "desc": "Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled."
      }
    ],
    "desc": "This API is used to create a person and add face, name, gender, and other related information.\n\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`."
  },
  "GetGroupInfo": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Group ID."
      }
    ],
    "desc": "This API is used to get the group information."
  },
  "DetectFace": {
    "params": [
      {
        "name": "MaxFaceNum",
        "desc": "Maximum number of processable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 120. \nThis parameter is used to control the number of faces in the image to be detected. The smaller the value, the faster the processing."
      },
      {
        "name": "MinFaceSize",
        "desc": "Minimum height and width of face in px.\nDefault value: 34. You are recommended to keep it at or above 34.\nFaces below the `MinFaceSize` value will not be detected."
      },
      {
        "name": "Image",
        "desc": "Base64-encoded image data, which cannot exceed 5 MB.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "Url",
        "desc": "Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  \nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. \nThe download speed and stability of non-Tencent Cloud URLs may be low.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "NeedFaceAttributes",
        "desc": "Whether the face attribute information (FaceAttributesInfo) needs to be returned. 0: no; 1: yes. Default value: 0. \nIf the value is not 1, it will be deemed as no need to return, and `FaceAttributesInfo` is meaningless in this case.  \nThe face attribute information of up to 5 largest faces in the image will be returned, and `FaceAttributesInfo` of the 6th and rest faces is meaningless.  \nExtracting face attribute information is quite time-consuming. If face attribute information is not required, you are recommended to disable this feature to speed up face detection."
      },
      {
        "name": "NeedQualityDetection",
        "desc": "Whether to enable quality detection. 0: no; 1: yes. Default value: 0. \nIf the value is not 1, it will be deemed not to perform quality detection.\nThe face quality score information of up to 30 largest faces in the image will be returned, and `FaceQualityInfo` of the 31st and rest faces is meaningless.  \nYou are recommended to enable this feature for the face adding operation."
      },
      {
        "name": "FaceModelVersion",
        "desc": "Algorithm model version used by the Face Recognition service. Valid values: 2.0, 3.0.  \nThis parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API previously, `2.0` will be used by default. \nDifferent algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is thus recommended."
      },
      {
        "name": "NeedRotateDetection",
        "desc": "Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled."
      }
    ],
    "desc": "This API is used to detect the position, attributes, and quality information of a face in the given image. The position information includes (x, y, w, h); the face attributes include gender, age, expression, beauty, glass, hair, mask, and pose (pitch, roll, yaw); and the face quality information includes the overall quality score, sharpness, brightness, and completeness.\n\n \nThe face quality information is mainly used to evaluate the quality of the input face image. When using the Face Recognition service, you are recommended to evaluate the quality of the input face image first to improve the effects of subsequent processing. Application scenarios of this feature include:\n\n1). [Creating](https://cloud.tencent.com/document/product/867/32793)/[Adding](https://cloud.tencent.com/document/product/867/32795) a person in a group: this is to ensure the quality of the face information to facilitate subsequent processing.\n\n2). [Face search](https://cloud.tencent.com/document/product/867/32798): this is to ensure the quality of the input image to quickly find the corresponding person.\n\n3). [Face verification](https://cloud.tencent.com/document/product/867/32806): this is to ensure the quality of the face information to avoid cases where the verification incorrectly fails.\n\n4). [Face fusion](https://cloud.tencent.com/product/facefusion): this is to ensure the quality of the uploaded face images to improve the fusion effect.\n\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.\n\n"
  },
  "GetPersonList": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Group ID"
      },
      {
        "name": "Offset",
        "desc": "Starting number. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 10. Maximum value: 1000"
      }
    ],
    "desc": "This API is used to get the list of persons in a specified group."
  },
  "VerifyPerson": {
    "params": [
      {
        "name": "Image",
        "desc": "Base64-encoded data of image.\nIf there are multiple faces in the image, only the face with the largest size will be selected.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "Url",
        "desc": "Image URL. Either the `Url` or `Image` of the image must be provided; if both are provided, only `Url` will be used. \nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. \nThe download speed and stability of non-Tencent Cloud URLs may be low.\nIf there are multiple faces in the image, only the face with the largest size will be selected.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "PersonId",
        "desc": "ID of the person to be verified. For more information on `PersonId`, please see the group management APIs."
      },
      {
        "name": "QualityControl",
        "desc": "Image quality control. \n0: no control. \n1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. \n2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. \n3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. \n4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. \nDefault value: 0. \nIf the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory."
      },
      {
        "name": "NeedRotateDetection",
        "desc": "Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled."
      }
    ],
    "desc": "This API is used to judge whether a person in an image corresponds to a given `PersonId`. For more information on `PersonId`, please see [CreateGroup](https://cloud.tencent.com/document/product/867/32794).\nThis API fuses the features of all faces of a person; for example, if a person has 4 faces, it will fuse the features of the 4 faces and generate the summarized facial features of the person to make the person verification (i.e., judging whether the face image to be recognized is of a specified person) more accurate.\n\n Unlike the `CompareFace` API that is used to judge the similarity between two faces, this API is used to judge \"whether the person in the image is someone specified\" whose information is stored in a group. This \"someone\" may have multiple face images.\n\n\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.\n- This feature is available only to groups whose algorithm model version (`FaceModelVersion`) is 3.0."
  },
  "ModifyPersonGroupInfo": {
    "params": [
      {
        "name": "GroupId",
        "desc": "Group ID"
      },
      {
        "name": "PersonId",
        "desc": "Person ID"
      },
      {
        "name": "PersonExDescriptionInfos",
        "desc": "Custom description field of the person to be modified, which is a `key-value`"
      }
    ],
    "desc": "This API is used to modify the description of a specified person in a group."
  },
  "VerifyFace": {
    "params": [
      {
        "name": "PersonId",
        "desc": "ID of the person to be verified. For more information on `PersonId`, please see the group management APIs."
      },
      {
        "name": "Image",
        "desc": "Base64-encoded image data, which cannot exceed 5 MB.\nIf there are multiple faces in the image, only the face with the largest size will be selected.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "Url",
        "desc": "Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  \nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. \nThe download speed and stability of non-Tencent Cloud URLs may be low.\nIf there are multiple faces in the image, only the face with the largest size will be selected.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "QualityControl",
        "desc": "Image quality control. \n0: no control. \n1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. \n2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. \n3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. \n4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. \nDefault value: 0. \nIf the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory."
      },
      {
        "name": "NeedRotateDetection",
        "desc": "Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled."
      }
    ],
    "desc": "This API is used to judge whether a person in an image corresponds to a given `PersonId`. For more information on `PersonId`, please see [CreateGroup](https://cloud.tencent.com/document/product/867/32794). \n\nUnlike the [CompareFace](https://cloud.tencent.com/document/product/867/32802) API that is used to judge the similarity between two faces, this API is used to judge \"whether the person in the image is someone specified\" whose information is stored in a group. This \"someone\" may have multiple face images.\n\nThis API recognizes each face of a person as an independent one. By contrast, the [VerifyPerson](https://cloud.tencent.com/document/product/867/38879) API fuses the features of all faces of a person; for example, if a person has 4 faces, it will fuse the features of the 4 faces and generate the summarized facial features of the person to make the person verification (i.e., judging whether the face image to be recognized is of a specified person) more accurate.\n\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`."
  },
  "SearchPersons": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "List of groups to be searched in. Up to 100 groups are supported."
      },
      {
        "name": "Image",
        "desc": "Base64-encoded image data, which cannot exceed 5 MB.\nIf there are multiple faces in the image, only the face with the largest size will be selected.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "Url",
        "desc": "Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` must be provided; if both are provided, only `Url` will be used.\nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.\nThe download speed and stability of non-Tencent Cloud URLs may be low.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "MaxFaceNum",
        "desc": "Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10.\n`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized.\nFor example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized."
      },
      {
        "name": "MinFaceSize",
        "desc": "Minimum height and width of face in px. Default value: 34. A value below 34 will affect the search accuracy. You are recommended to set this parameter to 80."
      },
      {
        "name": "MaxPersonNum",
        "desc": "Number of the most similar persons returned for faces recognized in one single image. Default value: 5. Maximum value: 100.\nFor example, if `MaxFaceNum` is 1 and `MaxPersonNum` is 8, information of the top 8 most similar persons will be returned.\nThe greater the value, the longer the processing time. You are recommended to set a value below 10."
      },
      {
        "name": "QualityControl",
        "desc": "Image quality control. \n0: no control. \n1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. \n2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. \n3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. \n4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. \nDefault value: 0. \nIf the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory."
      },
      {
        "name": "FaceMatchThreshold",
        "desc": "In the output parameter `Score`, the result will be returned only if the result value is greater than or equal to the `FaceMatchThreshold` value. Default value: 0. Value range: [0.0,100.0)."
      },
      {
        "name": "NeedPersonInfo",
        "desc": "Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default"
      },
      {
        "name": "NeedRotateDetection",
        "desc": "Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled."
      }
    ],
    "desc": "This API is used to recognize top K persons in one or more groups who are similar to the person in a given image and rank the similarity in a descending order.\n\nUp to 10 faces in an image can be recognized at a time, and up to 100 groups can be searched in at a time.\n\nThe maximum number of faces in a group that can be searched for at a time is subject to the group's algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.\n\nThis API fuses the features of all faces of a person; for example, if a person has 4 faces, it will fuse the features of the 4 faces and generate the summarized facial features of the person to make the person search (i.e., judging whether the face image to be recognized is of a specified person) more accurate. By contrast, the [SearchFaces](https://cloud.tencent.com/document/product/867/32798) and [SearchFacesReturnsByGroup](https://cloud.tencent.com/document/product/867/38882) APIs recognize each face of a person as an independent one for search.\n\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.\n- This feature is available only to groups whose algorithm model version (`FaceModelVersion`) is 3.0."
  },
  "CompareFace": {
    "params": [
      {
        "name": "ImageA",
        "desc": "Base64-encoded image A data, which cannot exceed 5 MB.\nIf there are multiple faces in the image, only the face with the largest size will be selected.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "ImageB",
        "desc": "Base64-encoded image B data, which cannot exceed 5 MB.\nIf there are multiple faces in the image, only the face with the largest size will be selected.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "UrlA",
        "desc": "Image A URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` of image A must be provided; if both are provided, only `Url` will be used. \nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. \nThe download speed and stability of non-Tencent Cloud URLs may be low.\nIf there are multiple faces in the image, only the face with the largest size will be selected.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "UrlB",
        "desc": "Image B URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` of image B must be provided; if both are provided, only `Url` will be used. \nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. \nThe download speed and stability of non-Tencent Cloud URLs may be low.\nIf there are multiple faces in the image, only the face with the largest size will be selected.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "FaceModelVersion",
        "desc": "Algorithm model version used by the Face Recognition service. Valid values: 2.0, 3.0. \nThis parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API previously, `2.0` will be used by default. \nDifferent algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is thus recommended."
      },
      {
        "name": "QualityControl",
        "desc": "Image quality control. \n0: no control. \n1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. \n2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. \n3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. \n4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. \nDefault value: 0. \nIf the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory."
      },
      {
        "name": "NeedRotateDetection",
        "desc": "Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled."
      }
    ],
    "desc": "This API is used to calculate the similarity of faces in two images and return the face similarity score.\n\nIf you need to judge \"whether the person in the image is someone specified\" in scenarios such as face login, i.e., checking whether the person in a given image is someone with a known identity, you are recommended to use the [VerifyFace](https://cloud.tencent.com/document/product/867/32806) or [VerifyPerson](https://cloud.tencent.com/document/product/867/38879) API.\n\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`."
  },
  "SearchPersonsReturnsByGroup": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "List of groups to be searched in. Up to 60 groups are supported."
      },
      {
        "name": "Image",
        "desc": "Base64-encoded image data, which cannot exceed 5 MB.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "Url",
        "desc": "Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.\nEither `Url` or `Image` must be provided; if both are provided, only `Url` will be used.\nYou are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.\nThe download speed and stability of non-Tencent Cloud URLs may be low.\n.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not."
      },
      {
        "name": "MaxFaceNum",
        "desc": "Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10.\n`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized.\nFor example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized."
      },
      {
        "name": "MinFaceSize",
        "desc": "Minimum height and width of face in px. Default value: 34. A value below 34 will affect the search accuracy. You are recommended to set this parameter to 80."
      },
      {
        "name": "MaxPersonNumPerGroup",
        "desc": "Detected faces, which is corresponding to the maximum number of returned most matching persons. Default value: 5. Maximum value: 10.  \nFor example, if `MaxFaceNum` is 3, `MaxPersonNumPerGroup` is 3, and the `GroupIds` length is 3, up to 45 (3 * 5 * 3) persons will be returned."
      },
      {
        "name": "QualityControl",
        "desc": "Image quality control. \n0: no control. \n1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. \n2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. \n3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. \n4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. \nDefault value: 0. \nIf the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory."
      },
      {
        "name": "FaceMatchThreshold",
        "desc": "In the output parameter `Score`, the result will be returned only if the result value is above the `FaceMatchThreshold` value. Default value: 0."
      },
      {
        "name": "NeedPersonInfo",
        "desc": "Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default"
      },
      {
        "name": "NeedRotateDetection",
        "desc": "Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled."
      }
    ],
    "desc": "This API is used to recognize top K persons in one or more groups who are similar to the person in a given image, display the results **by group**, and rank the similarity within each group in a descending order.\n\nUp to 10 faces in the image can be recognized at a time, and cross-group search is supported.\n\nThe maximum number of faces in a group that can be searched for at a time is subject to the group's algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.\n\nThis API fuses the features of all faces of a person; for example, if a person has 4 faces, it will fuse the features of the 4 faces and generate the summarized facial features of the person to make the person search (i.e., judging whether the face image to be recognized is of a specified person) more accurate. By contrast, the [SearchFaces](https://cloud.tencent.com/document/product/867/32798) and [SearchFacesReturnsByGroup](https://cloud.tencent.com/document/product/867/38882) APIs recognize each face of a person as an independent one for search.\n>     \n- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.\n- This feature is available only to groups whose algorithm model version (`FaceModelVersion`) is 3.0."
  },
  "GetGroupList": {
    "params": [
      {
        "name": "Offset",
        "desc": "Starting number. Default value: 0"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 10. Maximum value: 1000"
      }
    ],
    "desc": "This API is used to get the list of groups."
  },
  "EstimateCheckSimilarPersonCostTime": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "List of groups to be checked. \nThere can be up to 2 million persons in one group and up to 10 groups."
      }
    ],
    "desc": "This API is used to get the estimated duration of a duplicate person check task.\n\nIf the `EndTimestamp` meets your expectations, please initiate the duplicate person check request as soon as possible; otherwise, the task may take more time.\n\nIf the estimated duration is more than 5 hours, the duplicate person check feature cannot be used."
  },
  "DeleteFace": {
    "params": [
      {
        "name": "PersonId",
        "desc": "Person ID"
      },
      {
        "name": "FaceIds",
        "desc": "List of IDs of the faces to be deleted"
      }
    ],
    "desc": "This API is used to delete the face images of a person. If the person has only one face image, an error will be returned."
  }
}