# -*- coding: utf-8 -*-
DESC = "ssl-2019-12-05"
INFO = {
  "DescribeCertificateOperateLogs": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of requested logs. The default value is 20."
      },
      {
        "name": "StartTime",
        "desc": "Start time. The default value is 15 days ago."
      },
      {
        "name": "EndTime",
        "desc": "End time. The default value is the current time."
      }
    ],
    "desc": "This API is used to obtain certificate operation logs in the current account."
  },
  "DescribeCertificates": {
    "params": [
      {
        "name": "Offset",
        "desc": "Pagination offset, starting from 0."
      },
      {
        "name": "Limit",
        "desc": "Number of certificates on each page. The default value is 20."
      },
      {
        "name": "SearchKey",
        "desc": "Keyword for search, which can be a certificate ID, alias, or domain name. For example, a8xHcaIs."
      },
      {
        "name": "CertificateType",
        "desc": "Certificate type. CA: client certificate; SVR: server certificate."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID."
      },
      {
        "name": "ExpirationSort",
        "desc": "Sorting by expiration time. DESC: descending; ASC: ascending."
      },
      {
        "name": "CertificateStatus",
        "desc": "Certificate status."
      },
      {
        "name": "Deployable",
        "desc": "Whether the certificate can be deployed. 1: yes; 0: no."
      }
    ],
    "desc": "This API is used to obtain the certificate list."
  },
  "DescribeCertificate": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "Certificate ID."
      }
    ],
    "desc": "This API is used to obtain certificate information."
  },
  "CancelCertificateOrder": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "Certificate ID."
      }
    ],
    "desc": "This API is used to cancel a certificate order."
  },
  "CommitCertificateInformation": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "Certificate ID."
      }
    ],
    "desc": "This API is used to submit a certificate order."
  },
  "DeleteCertificate": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "Certificate ID."
      }
    ],
    "desc": "This API is used to delete a certificate."
  },
  "DescribeCertificateDetail": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "Certificate ID."
      }
    ],
    "desc": "This API is used to obtain certificate details."
  },
  "UploadCertificate": {
    "params": [
      {
        "name": "CertificatePublicKey",
        "desc": "Public key of the certificate."
      },
      {
        "name": "CertificatePrivateKey",
        "desc": "Private key content. This parameter is required when the certificate type is SVR, and not required when the certificate type is CA."
      },
      {
        "name": "CertificateType",
        "desc": "Certificate type. CA: client certificate; SVR: server certificate. The default value is SVR."
      },
      {
        "name": "Alias",
        "desc": "Alias."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID."
      }
    ],
    "desc": "This API is used to upload a certificate."
  },
  "ReplaceCertificate": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "Certificate ID."
      },
      {
        "name": "ValidType",
        "desc": "Verification type. DNS_AUTO: automatic DNS verification; DNS: manual DNS verification; FILE: verification by file."
      },
      {
        "name": "CsrType",
        "desc": "Type. Original: original certificate CSR; upload: uploaded manually; online: generated online. The default value is original."
      },
      {
        "name": "CsrContent",
        "desc": "CSR content."
      },
      {
        "name": "CsrkeyPassword",
        "desc": "Password of the key."
      }
    ],
    "desc": "This API is used to reissue a certificate. Note that if you have applied for a free certificate, only an RSA-2048 certificate will be reissued, and the certificate can be reissued only once."
  },
  "ApplyCertificate": {
    "params": [
      {
        "name": "DvAuthMethod",
        "desc": "Verification type. DNS_AUTO: automatic DNS verification; DNS: manual DNS verification; FILE: verification by file."
      },
      {
        "name": "DomainName",
        "desc": "Domain name."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID."
      },
      {
        "name": "PackageType",
        "desc": "Certificate type. Currently, the only supported value is 2, which indicates TrustAsia TLS RSA CA."
      },
      {
        "name": "ContactEmail",
        "desc": "Email address."
      },
      {
        "name": "ContactPhone",
        "desc": "Mobile number."
      },
      {
        "name": "ValidityPeriod",
        "desc": "Validity period. The default value is 12 months, which is the only supported value currently."
      },
      {
        "name": "CsrEncryptAlgo",
        "desc": "Encryption algorithm. Only RSA is supported."
      },
      {
        "name": "CsrKeyParameter",
        "desc": "Key pair parameter. Only the 2048-bit key pair is supported."
      },
      {
        "name": "CsrKeyPassword",
        "desc": "CSR encryption password."
      },
      {
        "name": "Alias",
        "desc": "Alias."
      },
      {
        "name": "OldCertificateId",
        "desc": "Original certificate ID, which is used to apply for a new certificate."
      }
    ],
    "desc": "This API is used to apply for a free certificate."
  },
  "DownloadCertificate": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "Certificate ID."
      }
    ],
    "desc": "This API is used to download a certificate."
  },
  "SubmitCertificateInformation": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "Certificate ID."
      },
      {
        "name": "CsrType",
        "desc": "CSR generation mode. Online: generated online; parse: uploaded manually."
      },
      {
        "name": "CsrContent",
        "desc": "Uploaded CSR content."
      },
      {
        "name": "CertificateDomain",
        "desc": "Domain name bound with the certificate."
      },
      {
        "name": "DomainList",
        "desc": "Uploaded domain name array (can be uploaded for a multi-domain certificate)."
      },
      {
        "name": "KeyPassword",
        "desc": "Password of the private key."
      },
      {
        "name": "OrganizationName",
        "desc": "Organization name."
      },
      {
        "name": "OrganizationDivision",
        "desc": "Division name."
      },
      {
        "name": "OrganizationAddress",
        "desc": "Detailed address of the organization."
      },
      {
        "name": "OrganizationCountry",
        "desc": "Country where the organization is located. For example, CN (China)."
      },
      {
        "name": "OrganizationCity",
        "desc": "City where the organization is located."
      },
      {
        "name": "OrganizationRegion",
        "desc": "Province where the organization is located."
      },
      {
        "name": "PostalCode",
        "desc": "Postal code of the organization."
      },
      {
        "name": "PhoneAreaCode",
        "desc": "Area code of the fixed-line phone number of the organization."
      },
      {
        "name": "PhoneNumber",
        "desc": "Fixed-line phone number of the organization."
      },
      {
        "name": "VerifyType",
        "desc": "Certificate verification method."
      },
      {
        "name": "AdminFirstName",
        "desc": "Last name of the admin."
      },
      {
        "name": "AdminLastName",
        "desc": "First name of the admin."
      },
      {
        "name": "AdminPhoneNum",
        "desc": "Mobile number of the admin."
      },
      {
        "name": "AdminEmail",
        "desc": "Email of the admin."
      },
      {
        "name": "AdminPosition",
        "desc": "Position of the admin."
      },
      {
        "name": "ContactFirstName",
        "desc": "Last name of the contact."
      },
      {
        "name": "ContactLastName",
        "desc": "First name of the contact."
      },
      {
        "name": "ContactEmail",
        "desc": "Email of the contact."
      },
      {
        "name": "ContactNumber",
        "desc": "Mobile number of the contact."
      },
      {
        "name": "ContactPosition",
        "desc": "Position of the contact."
      }
    ],
    "desc": "This API is used to submit certificate information."
  },
  "ModifyCertificateProject": {
    "params": [
      {
        "name": "CertificateIdList",
        "desc": "ID list of certificates whose projects need to be modified. A maximum 100 certificate IDs are supported."
      },
      {
        "name": "ProjectId",
        "desc": "Project ID."
      }
    ],
    "desc": "This API is used to modify the projects of multiple certificates."
  },
  "ModifyCertificateAlias": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "Certificate ID."
      },
      {
        "name": "Alias",
        "desc": "Alias."
      }
    ],
    "desc": "This API is used to modify certificate alias by inputting the certificate ID and new alias."
  }
}