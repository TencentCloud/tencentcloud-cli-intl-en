# -*- coding: utf-8 -*-
DESC = "kms-2019-01-18"
INFO = {
  "Encrypt": {
    "params": [],
    "desc": "本接口用于加密最多为4KB任意数据，可用于加密数据库密码，RSA Key，或其它较小的敏感信息。对于应用的数据加密，使用GenerateDataKey生成的DataKey进行本地数据的加解密操作"
  },
  "DeleteImportedKeyMaterial": {
    "params": [
      {
        "name": "KeyId",
        "desc": "Specifies the EXTERNAL CMK for which to delete the key material."
      }
    ],
    "desc": "This API is used to delete the imported key material. It is only valid for EXTERNAL CMKs. Specifically, it puts a CMK into `PendingImport` status instead of deleting the CMK, so that the CMK can be used again after key material is reimported. To delete the CMK completely, please call the `ScheduleKeyDeletion` API."
  },
  "UpdateAlias": {
    "params": [],
    "desc": "This API is used to modify the alias of a CMK. CMKs in `PendingDelete` status cannot be modified."
  },
  "ImportKeyMaterial": {
    "params": [
      {
        "name": "EncryptedKeyMaterial",
        "desc": "Base64-encoded key material that encrypted with the `PublicKey` returned by `GetParametersForImport`. For the KMS of SM-CRYPTO version, the length of the key material should be 128 bits, while for KMS of FIPS-compliant version, the length should be 256 bits."
      },
      {
        "name": "ImportToken",
        "desc": "Import token obtained by calling `GetParametersForImport`."
      },
      {
        "name": "KeyId",
        "desc": "Specifies the CMK into which to import key material, which must be the same as the one specified by `GetParametersForImport`."
      },
      {
        "name": "ValidTo",
        "desc": "Unix timestamp of the key material’s expiration time. If this value is empty or 0, the key material will never expire. To specify the expiration time, it should be later than the current time. Maximum value: 2147443200."
      }
    ],
    "desc": "This API is used to import key material into an EXTERNAL CMK. The key obtained through the `GetParametersForImport` API is used to encrypt the key material. You can only reimport the same key material into the specified CMK and set a new expiration time. After the CMK key material is imported, it cannot be replaced. After the key material is expired or deleted, the CMK will remain unavailable until the same key material is reimported. CMKs are independent, which means that the same key material can be imported into different CMKs, but data encrypted by one CMK cannot be decrypted by another one.\nKey material can only be imported into CMKs in `Enabled` and `PendingImport` status."
  },
  "DisableKey": {
    "params": [],
    "desc": "本接口用于禁用一个主密钥，处于禁用状态的Key无法用于加密、解密操作。"
  },
  "GenerateDataKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": ""
      },
      {
        "name": "KeySpec",
        "desc": "Specifies the encryption algorithm and size of the `DataKey`. Valid values: AES_128, AES_256. Either `KeySpec` or `NumberOfBytes` must be specified."
      },
      {
        "name": "NumberOfBytes",
        "desc": "Length of the `DataKey`. If both `NumberOfBytes` and `KeySpec` are specified, `NumberOfBytes` will prevail. Minimum value: 1; maximum value: 1024. Either `KeySpec` or `NumberOfBytes` must be specified."
      },
      {
        "name": "EncryptionContext",
        "desc": ""
      }
    ],
    "desc": "本接口生成一个数据密钥，您可以用这个密钥进行本地数据的加密。"
  },
  "CancelKeyDeletion": {
    "params": [],
    "desc": "取消CMK的计划删除操作"
  },
  "GetKeyRotationStatus": {
    "params": [],
    "desc": "查询指定的CMK是否开启了密钥轮换功能。"
  },
  "DisableKeys": {
    "params": [],
    "desc": "该接口用于批量禁止CMK的使用。"
  },
  "ReEncrypt": {
    "params": [],
    "desc": "使用指定CMK对密文重新加密。"
  },
  "ListKeys": {
    "params": [],
    "desc": "This API is used to list the KeyIds of CMKs in `Enabled`, `Disabled`, and `PendingImport` status under the account."
  },
  "GenerateRandom": {
    "params": [
      {
        "name": "NumberOfBytes",
        "desc": "Length of the random number. Minimum value: 1. Maximum value: 1024"
      }
    ],
    "desc": "This API is used to generate a random number."
  },
  "CreateKey": {
    "params": [
      {
        "name": "Alias",
        "desc": ""
      },
      {
        "name": "Description",
        "desc": ""
      },
      {
        "name": "KeyUsage",
        "desc": ""
      },
      {
        "name": "Type",
        "desc": "Specifies the key type. Default value: 1. Valid value: 1 - default type, indicating that the CMK is created by KMS; 2 - EXTERNAL type, indicating that you need to import key material. For more information, please see the `GetParametersForImport` and `ImportKeyMaterial` API documents."
      }
    ],
    "desc": "创建用户管理数据密钥的主密钥CMK（Custom Master Key）。"
  },
  "GetParametersForImport": {
    "params": [
      {
        "name": "KeyId",
        "desc": "Unique ID of a CMK. The CMK for which to get the key parameters must be of the `EXTERNAL` type, i.e., Type = 2 when the CMK is created by the `CreateKey` API."
      },
      {
        "name": "WrappingAlgorithm",
        "desc": "Specifies the algorithm for key material encryption. Currently, `RSAES_PKCS1_V1_5`, `RSAES_OAEP_SHA_1`, and `RSAES_OAEP_SHA_256` are supported."
      },
      {
        "name": "WrappingKeySpec",
        "desc": "Specifies the type of wrapping key. Currently, only `RSA_2048` is supported."
      }
    ],
    "desc": "This API is used to obtain the parameters of the material to be imported into a CMK. The returned `Token` is used as one of the parameters to execute `ImportKeyMaterial`, and the returned `PublicKey` is used to encrypt the key material. The `Token` and `PublicKey` are valid for 24 hours. If they are expired, you will need to call the API again to get a new `Token` and `PublicKey`."
  },
  "ListKeyDetail": {
    "params": [
      {
        "name": "Offset",
        "desc": ""
      },
      {
        "name": "Limit",
        "desc": ""
      },
      {
        "name": "Role",
        "desc": ""
      },
      {
        "name": "OrderType",
        "desc": ""
      },
      {
        "name": "KeyState",
        "desc": "Filters by CMK status. 0: all CMKs; 1: CMKs in `Enabled` status only; 2: CMKs in `Disabled` status only; 3: CMKs in `PendingDelete` status only (i.e., keys with schedule deletion enabled); 4: CMKs in `PendingImport` status only."
      },
      {
        "name": "SearchKeyAlias",
        "desc": ""
      },
      {
        "name": "Origin",
        "desc": "Filters by CMK type. \"TENCENT_KMS\" indicates to filter CMKs whose key materials are created by KMS; \"EXTERNAL\" indicates to filter CMKs of `EXTERNAL` type whose key materials are imported by users; \"ALL\" or empty indicates to filter CMKs of both types. This value is case-sensitive."
      }
    ],
    "desc": "根据指定Offset和Limit获取主密钥列表详情。"
  },
  "DisableKeyRotation": {
    "params": [],
    "desc": "对指定的CMK禁止密钥轮换功能。"
  },
  "EnableKeys": {
    "params": [],
    "desc": "该接口用于批量启用CMK。"
  },
  "ScheduleKeyDeletion": {
    "params": [],
    "desc": "CMK计划删除接口，用于指定CMK删除的时间，可选时间区间为[7,30]天"
  },
  "EnableKeyRotation": {
    "params": [],
    "desc": "对指定的CMK开启密钥轮换功能。"
  },
  "EnableKey": {
    "params": [],
    "desc": "用于启用一个指定的CMK。"
  },
  "Decrypt": {
    "params": [
      {
        "name": "CiphertextBlob",
        "desc": "The ciphertext data to be decrypted."
      },
      {
        "name": "EncryptionContext",
        "desc": ""
      }
    ],
    "desc": "本接口用于解密密文，得到明文数据。"
  },
  "UpdateKeyDescription": {
    "params": [],
    "desc": "This API is used to modify the description of the specified CMK. CMKs in `PendingDelete` status cannot be modified."
  },
  "GetServiceStatus": {
    "params": [],
    "desc": "用于查询该用户是否已开通KMS服务"
  }
}