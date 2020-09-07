# -*- coding: utf-8 -*-
DESC = "cfs-2019-07-19"
INFO = {
  "CreateCfsFileSystem": {
    "params": [
      {
        "name": "Zone",
        "desc": "AZ name, such as \"ap-beijing-1\". For the list of regions and AZs, please see [Overview](https://intl.cloud.tencent.com/document/product/582/13225?from_cn_redirect=1)"
      },
      {
        "name": "NetInterface",
        "desc": "Network type. Valid values: VPC (VPC), BASIC (basic network)"
      },
      {
        "name": "PGroupId",
        "desc": "Permission group ID"
      },
      {
        "name": "Protocol",
        "desc": "File system protocol type. Valid values: NFS, CIFS. If this parameter is left empty, NFS will be used by default"
      },
      {
        "name": "StorageType",
        "desc": "File system storage class. Valid values: SD (standard), HP (high-performance)"
      },
      {
        "name": "VpcId",
        "desc": "VPC ID. This field is required if network type is VPC."
      },
      {
        "name": "SubnetId",
        "desc": "Subnet ID. This field is required if network type is VPC."
      },
      {
        "name": "MountIP",
        "desc": "Specifies an IP address, which is supported only for VPC. If this parameter is left empty, a random IP will be assigned in the subnet"
      },
      {
        "name": "FsName",
        "desc": "Custom file system name"
      },
      {
        "name": "ResourceTags",
        "desc": "File system tag"
      }
    ],
    "desc": "This API is used to create a file system."
  },
  "DeleteCfsPGroup": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "Permission group ID"
      }
    ],
    "desc": "This API is used to delete a permission group."
  },
  "DeleteMountTarget": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "File system ID"
      },
      {
        "name": "MountTargetId",
        "desc": "Mount target ID"
      }
    ],
    "desc": "This API is used to delete a mount target."
  },
  "DescribeCfsRules": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "Permission group ID"
      }
    ],
    "desc": "This API is used to query the list of permission group rules."
  },
  "UpdateCfsFileSystemPGroup": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "Permission group ID"
      },
      {
        "name": "FileSystemId",
        "desc": "File system ID"
      }
    ],
    "desc": "This API is used to update the permission group used by a file system."
  },
  "DescribeAvailableZoneInfo": {
    "params": [],
    "desc": "This API is used to query the availability of a region."
  },
  "UpdateCfsFileSystemName": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "File system ID"
      },
      {
        "name": "FsName",
        "desc": "Custom file system name"
      }
    ],
    "desc": "This API is used to update a file system name."
  },
  "DescribeCfsPGroups": {
    "params": [],
    "desc": "This API is used to query the list of permission groups."
  },
  "CreateCfsPGroup": {
    "params": [
      {
        "name": "Name",
        "desc": "Permission group name, which can contain 1-64 Chinese characters, letters, numbers, underscores, or dashes"
      },
      {
        "name": "DescInfo",
        "desc": "Permission group description, which can contain 1-255 characters"
      }
    ],
    "desc": "This API is used to create a permission group."
  },
  "DescribeMountTargets": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "File system ID"
      }
    ],
    "desc": "This API is used to query the mount targets of a file system."
  },
  "UpdateCfsFileSystemSizeLimit": {
    "params": [
      {
        "name": "FsLimit",
        "desc": "File system capacity limit in GB. Value range: 0-1,073,741,824. If 0 is entered, no limit will be imposed on the file system capacity."
      },
      {
        "name": "FileSystemId",
        "desc": "File system ID"
      }
    ],
    "desc": "This API is used to update the capacity limit of a file system."
  },
  "DescribeCfsFileSystems": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "File system ID"
      },
      {
        "name": "VpcId",
        "desc": "VPC ID"
      },
      {
        "name": "SubnetId",
        "desc": "Subnet ID"
      }
    ],
    "desc": "This API is used to query file systems."
  },
  "SignUpCfsService": {
    "params": [],
    "desc": "This API is used to activate the CFS service."
  },
  "CreateCfsRule": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "Permission group ID"
      },
      {
        "name": "AuthClientIp",
        "desc": "You can enter a single IP or IP range, such as 10.1.10.11 or 10.10.1.0/24. The default visiting address is `*`, indicating that all IPs are allowed. Please note that you need to enter the CVM instance's private IP here."
      },
      {
        "name": "Priority",
        "desc": "Rule priority. Value range: 1-100. 1 represents the highest priority, while 100 the lowest"
      },
      {
        "name": "RWPermission",
        "desc": "Read/write permission. Valid values: RO (read-only), RW (read & write). Default value: RO"
      },
      {
        "name": "UserPermission",
        "desc": "User permission. Valid values: all_squash, no_all_squash, root_squash, no_root_squash. Specifically, all_squash: any visiting user will be mapped to an anonymous user or user group; no_all_squash: a visiting user will be first matched with a local user, and if the match fails, it will be mapped to an anonymous user or user group; root_squash: a visiting root user will be mapped to an anonymous user or user group; no_root_squash: a visiting root user will be allowed to maintain root account permissions. Default value: root_squash."
      }
    ],
    "desc": "This API is used to create a permission group rule."
  },
  "DeleteCfsFileSystem": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "File system ID. Note: please call the `DeleteMountTarget` API to delete the mount target first before deleting a file system; otherwise, the delete operation will fail."
      }
    ],
    "desc": "This API is used to delete a file system."
  },
  "UpdateCfsRule": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "Permission group ID"
      },
      {
        "name": "RuleId",
        "desc": "Rule ID"
      },
      {
        "name": "AuthClientIp",
        "desc": "You can enter a single IP or IP range, such as 10.1.10.11 or 10.10.1.0/24. The default visiting address is `*`, indicating that all IPs are allowed. Please note that you need to enter the CVM instance's private IP here."
      },
      {
        "name": "RWPermission",
        "desc": "Read/write permission. Valid values: RO (read-only), RW (read & write). Default value: RO"
      },
      {
        "name": "UserPermission",
        "desc": "User permission. Valid values: all_squash, no_all_squash, root_squash, no_root_squash. Specifically, all_squash: any visiting user will be mapped to an anonymous user or user group; no_all_squash: a visiting user will be first matched with a local user, and if the match fails, it will be mapped to an anonymous user or user group; root_squash: a visiting root user will be mapped to an anonymous user or user group; no_root_squash: a visiting root user will be allowed to maintain root account permissions. Default value: root_squash."
      },
      {
        "name": "Priority",
        "desc": "Rule priority. Value range: 1-100. 1 represents the highest priority, while 100 the lowest"
      }
    ],
    "desc": "This API is used to update a permission rule."
  },
  "UpdateCfsPGroup": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "Permission group ID"
      },
      {
        "name": "Name",
        "desc": "Permission group name, which can contain 1-64 Chinese characters, letters, numbers, underscores, or dashes"
      },
      {
        "name": "DescInfo",
        "desc": "Permission group description, which can contain 1-255 characters"
      }
    ],
    "desc": "This API is used to update the information of a permission group."
  },
  "DeleteCfsRule": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "Permission group ID"
      },
      {
        "name": "RuleId",
        "desc": "Rule ID"
      }
    ],
    "desc": "This API is used to delete a permission group rule."
  },
  "DescribeCfsFileSystemClients": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "File system ID"
      }
    ],
    "desc": "This API is used to query clients on which this file system is mounted. To do so, the client needs to have the CFS monitoring plugin installed."
  },
  "DescribeCfsServiceStatus": {
    "params": [],
    "desc": "This API is used to query the status of the CFS service."
  }
}