# -*- coding: utf-8 -*-
DESC = "kms-2019-01-18"
INFO = {
  "Encrypt": {
    "params": [],
    "desc": "This API is used to encrypt any data up to 4KB. It can be used to encrypt database passwords, RSA Key, or other small sensitive information. For application data encryption, use the DataKey generated by GenerateDataKey to perform local data encryption and decryption operations"
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
    "desc": "This API is used to decrypt the ciphertext and obtain the plaintext data."
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
  "GetPublicKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "Unique CMK ID."
      }
    ],
    "desc": "This API is used to get the information of the public key that is encrypted with the asymmetric cryptographic algorithm and of which the `KeyUsage` is `ASYMMETRIC_DECRYPT_RSA_2048` or `ASYMMETRIC_DECRYPT_SM2`. This public key can be used to encrypt data locally, and the data encrypted with it can only be decrypted with the corresponding private key through KMS. The public key can only be obtained from the asymmetric key in `Enabled` state."
  },
  "DisableKey": {
    "params": [],
    "desc": "This API is used to disable a master key. The disabled key cannot be used for encryption and decryption operations."
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
    "desc": "This API generates a data key, which you can use to encrypt local data."
  },
  "AsymmetricSm2Decrypt": {
    "params": [
      {
        "name": "KeyId",
        "desc": "Unique CMK ID"
      },
      {
        "name": "Ciphertext",
        "desc": "Base64-encoded ciphertext encrypted with `PublicKey`, whose length cannot exceed 256 bytes."
      }
    ],
    "desc": "This API is used to decrypt data with the specified private key that is encrypted with SM2 asymmetric cryptographic algorithm. The ciphertext must be encrypted with the corresponding public key. The asymmetric key must be in `Enabled` state for decryption. The length of the ciphertext passed in cannot exceed 256 bytes."
  },
  "CancelKeyDeletion": {
    "params": [],
    "desc": "Cancel the scheduled deletion of CMK"
  },
  "GetKeyRotationStatus": {
    "params": [],
    "desc": "Query whether the specified CMK has the key rotation function."
  },
  "DisableKeys": {
    "params": [],
    "desc": "This API is used to batch prohibit the use of CMK."
  },
  "ListAlgorithms": {
    "params": [],
    "desc": "This API is used to list the encryption methods supported in the current region."
  },
  "DescribeKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "Globally unique CMK ID"
      }
    ],
    "desc": "This API is used to get the attribute details of the CMK with a specified `KeyId`."
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
        "desc": "Unique alias that makes a key more recognizable and understandable. This parameter cannot be empty, can contain 1–60 letters, digits, `-`, and `_`, and must begin with a letter or digit. The `kms-` prefix is used for Tencent Cloud products."
      },
      {
        "name": "Description",
        "desc": ""
      },
      {
        "name": "KeyUsage",
        "desc": "Key purpose. The default value is `ENCRYPT_DECRYPT` (creating a symmetric key for encryption and decryption). Other valid values include `ASYMMETRIC_DECRYPT_RSA_2048` (creating an RSA2048 asymmetric key for encryption and decryption) and `ASYMMETRIC_DECRYPT_SM2` (creating an SM2 asymmetric key for encryption and decryption)."
      },
      {
        "name": "Type",
        "desc": "Specifies the key type. Default value: 1. Valid value: 1 - default type, indicating that the CMK is created by KMS; 2 - EXTERNAL type, indicating that you need to import key material. For more information, please see the `GetParametersForImport` and `ImportKeyMaterial` API documents."
      }
    ],
    "desc": "Create a master key CMK (Custom Master Key) for user management data keys"
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
        "desc": "This parameter has the same meaning of the `Limit` in an SQL query, indicating that up to `Limit` value elements can be obtained in this request. The default value is 10 and the maximum value is 200."
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
      },
      {
        "name": "KeyUsage",
        "desc": "Filter by `KeyUsage` of CMKs. If this parameter is left empty, it means to filter all CMKs. Valid values: ENCRYPT_DECRYPT, ASYMMETRIC_DECRYPT_RSA_2048, ASYMMETRIC_DECRYPT_SM2"
      }
    ],
    "desc": "Get the master key list details according to the specified Offset and Limit."
  },
  "AsymmetricRsaDecrypt": {
    "params": [
      {
        "name": "KeyId",
        "desc": "Unique CMK ID"
      },
      {
        "name": "Ciphertext",
        "desc": "Base64-encoded ciphertext encrypted with `PublicKey`"
      },
      {
        "name": "Algorithm",
        "desc": "Corresponding algorithm when a public key is used for encryption. Valid values: RSAES_PKCS1_V1_5, RSAES_OAEP_SHA_1, RSAES_OAEP_SHA_256"
      }
    ],
    "desc": "This API is used to decrypt data with the specified private key that is encrypted with RSA asymmetric cryptographic algorithm. The ciphertext must be encrypted with the corresponding public key. The asymmetric key must be in `Enabled` state for decryption."
  },
  "DisableKeyRotation": {
    "params": [],
    "desc": "Disabled key rotation for the specified CMK."
  },
  "EnableKeys": {
    "params": [],
    "desc": "This API is used to enable CMK in batches."
  },
  "ScheduleKeyDeletion": {
    "params": [],
    "desc": "CMK planned deletion API, used to specify the time of CMK deletion, the optional time interval is [7,30] days"
  },
  "ReEncrypt": {
    "params": [],
    "desc": "Re-encrypt the ciphertext using the specified CMK."
  },
  "EnableKeyRotation": {
    "params": [],
    "desc": "Turn on the key rotation function for the specified CMK."
  },
  "EnableKey": {
    "params": [],
    "desc": "Enable a specified CMK."
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
  "DescribeKeys": {
    "params": [
      {
        "name": "KeyIds",
        "desc": "List of IDs of the CMKs to be queried in batches. Up to 100 `KeyId` values are supported in one query."
      }
    ],
    "desc": "This API is used to get the attribute information of CMKs in batches."
  },
  "UpdateKeyDescription": {
    "params": [
      {
        "name": "Description",
        "desc": ""
      },
      {
        "name": "KeyId",
        "desc": "ID of the CMK for which to modify the description"
      }
    ],
    "desc": "This API is used to modify the description of the specified CMK. CMKs in `PendingDelete` status cannot be modified."
  },
  "GetServiceStatus": {
    "params": [],
    "desc": "Used to query whether the user has activated the KMS service."
  }
}