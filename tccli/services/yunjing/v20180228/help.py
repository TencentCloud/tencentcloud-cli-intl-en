# -*- coding: utf-8 -*-
DESC = "yunjing-2018-02-28"
INFO = {
  "DescribeVulScanResult": {
    "params": [],
    "desc": "This API is used to get the vulnerability detection result.\n"
  },
  "TrustMalwares": {
    "params": [
      {
        "name": "Ids",
        "desc": "Trojan ID array."
      }
    ],
    "desc": "This API is used to trust an identified trojan file."
  },
  "DescribeComponentStatistics": {
    "params": [
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\nComponentName - String - Required: No - Component name"
      }
    ],
    "desc": "This API is used to get the component statistics list."
  },
  "DeleteMachineTag": {
    "params": [
      {
        "name": "Rid",
        "desc": "Associated tag ID"
      }
    ],
    "desc": "This API is used to remove a tag from a server."
  },
  "DescribeHistoryAccounts": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Username - String - Required: No - Account name</li>"
      }
    ],
    "desc": "This API is used to get the account change history list."
  },
  "RecoverMalwares": {
    "params": [
      {
        "name": "Ids",
        "desc": "Trojan ID array. Up to 200 IDs can be deleted at a time"
      }
    ],
    "desc": "This API is used to recover isolated trojan files in a batch."
  },
  "ExportMalwares": {
    "params": [],
    "desc": "This API is used to export trojan records into a CSV file."
  },
  "DescribeProcessStatistics": {
    "params": [
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>ProcessName - String - Required: No - Process name</li>"
      }
    ],
    "desc": "This API is used to get the process statistics list."
  },
  "DescribeWeeklyReportBruteAttacks": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "Weekly CWP Pro report start time."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to get the brute force attack data in the weekly CWP Pro report."
  },
  "DescribeBruteAttacks": {
    "params": [
      {
        "name": "Uuid",
        "desc": "Agent `Uuid`."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Keywords - String - Required: No - Query keywords</li>\n<li>Status - String - Required: No - Query status (FAILED: brute force attack failed, SUCCESS: brute force attack succeeded)</li>"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      }
    ],
    "desc": "This API is used to get the brute force attack event list."
  },
  "DescribeWeeklyReportVuls": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "Weekly CWP Pro report start time."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to get the vulnerability data in the weekly CWP Pro report.\n"
  },
  "UntrustMalwares": {
    "params": [
      {
        "name": "Ids",
        "desc": "Trojan event ID array. Up to 200 IDs can be processed at a time."
      }
    ],
    "desc": "This API is used to untrust a trojan file."
  },
  "DescribeMachines": {
    "params": [
      {
        "name": "MachineType",
        "desc": "Server type.\n<li>CVM: CVM</li>\n<li>BM: BM</li>"
      },
      {
        "name": "MachineRegion",
        "desc": "Server region, such as ap-guangzhou or ap-shanghai"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Keywords - String - Required: No - Query keywords</li>\n<li>Status - String - Required: No - Agent status (OFFLINE: offline, ONLINE: online)</li>\n<li>Version - String  Required: No - Current CWP edition (PRO_VERSION: Pro, BASIC_VERSION: Basic)</li>\nEach filter supports only one value. Query with multiple values in \"OR\" relationship is not supported for the time being"
      }
    ],
    "desc": "This API is used to get the list of servers in a specified region."
  },
  "DescribeWeeklyReportMalwares": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "Weekly CWP Pro report start time."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to get the trojan data in the weekly CWP Pro report."
  },
  "DescribeMaliciousRequests": {
    "params": [
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, TRUSTED: trusted, UN_TRUSTED: untrusted)</li>\n<li>Domain - String - Required: No - Malicious request domain name</li>\n<li>MachineIp - String - Required: No - Private IP of server</li>"
      },
      {
        "name": "Uuid",
        "desc": "CWP agent `UUID`."
      }
    ],
    "desc": "This API is used to get malicious request data."
  },
  "DescribeComponentInfo": {
    "params": [
      {
        "name": "ComponentId",
        "desc": "Component ID."
      }
    ],
    "desc": "This API is used to get the component information."
  },
  "DescribeVulInfo": {
    "params": [
      {
        "name": "VulId",
        "desc": "Vulnerability category ID."
      }
    ],
    "desc": "This API is used to get vulnerability details."
  },
  "DeleteUsualLoginPlaces": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`"
      },
      {
        "name": "CityIds",
        "desc": "Added usual login city ID array"
      }
    ],
    "desc": "This API is used to delete one or more usual login locations."
  },
  "DeleteNonlocalLoginPlaces": {
    "params": [
      {
        "name": "Ids",
        "desc": "Unusual login location event ID array."
      }
    ],
    "desc": "This API is used to delete unusual login location records."
  },
  "DescribeOpenPorts": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`. Either `Port` or `Uuid` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server."
      },
      {
        "name": "Port",
        "desc": "Open port number. Either `Port` or `Uuid` must be specified. If `Port` is specified, it indicates to query the information list under the specified port."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Port - Uint64 - Required: No - Port number</li>\n<li>ProcessName - String - Required: No - Process name</li>\n<li>MachineIp - String - Required: No - Private IP of server</li>"
      }
    ],
    "desc": "This API is used to get the port list.\n"
  },
  "MisAlarmNonlocalLoginPlaces": {
    "params": [
      {
        "name": "Ids",
        "desc": "Unusual login location event ID array."
      }
    ],
    "desc": "This API is used to set the current location as the usual login location."
  },
  "ModifyProVersionRenewFlag": {
    "params": [
      {
        "name": "RenewFlag",
        "desc": "Auto-renewal flag. Valid values:\n<li>NOTIFY_AND_AUTO_RENEW: notifies of expiration and auto-renews</li>\n<li>NOTIFY_AND_MANUAL_RENEW: notifies of expiration but does not auto-renew</li>\n<li>DISABLE_NOTIFY_AND_MANUAL_RENEW: does not notify of expiration or auto-renew</li>"
      },
      {
        "name": "Quuid",
        "desc": "Unique server ID, corresponding to `uuid` for CVM or `instanceId` for BM."
      }
    ],
    "desc": "This API is used to modify the renewal flag of CWP Pro."
  },
  "ExportMaliciousRequests": {
    "params": [],
    "desc": "This API is used to export the malicious request file into a CSV file for download."
  },
  "SeparateMalwares": {
    "params": [
      {
        "name": "Ids",
        "desc": "Trojan event ID array."
      }
    ],
    "desc": "This API is used to isolate trojans."
  },
  "DescribeTagMachines": {
    "params": [
      {
        "name": "Id",
        "desc": "Tag ID"
      }
    ],
    "desc": "This API is used to get the information of servers associated with a specified tag."
  },
  "AddMachineTag": {
    "params": [
      {
        "name": "Quuid",
        "desc": "Server ID"
      },
      {
        "name": "TagId",
        "desc": "Tag ID"
      },
      {
        "name": "MRegion",
        "desc": "Server region"
      },
      {
        "name": "MArea",
        "desc": "Server type (`CVM` or `BM`)"
      }
    ],
    "desc": "This API is used to add a tag to a server."
  },
  "ModifyAutoOpenProVersionConfig": {
    "params": [
      {
        "name": "Status",
        "desc": "Auto-Activation status.\n<li>CLOSE: disabled</li>\n<li>OPEN: enabled</li>"
      }
    ],
    "desc": "This API is used to set whether to automatically activate CWP Pro for newly added servers."
  },
  "AddLoginWhiteList": {
    "params": [
      {
        "name": "Rules",
        "desc": "Whitelist rule"
      }
    ],
    "desc": "This API is used to add a allowlist rule."
  },
  "DescribeNonlocalLoginPlaces": {
    "params": [
      {
        "name": "Uuid",
        "desc": "Agent `Uuid`."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Keywords - String - Required: No - Query keywords</li>\n<li>Status - String - Required: No - Login status (NON_LOCAL_LOGIN: unusual login location, NORMAL_LOGIN: intended login)</li>"
      }
    ],
    "desc": "This API is used to get unusual login events."
  },
  "DeleteMachine": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`."
      }
    ],
    "desc": "This API is used to uninstall the CWP agent."
  },
  "DescribeProcessTaskStatus": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`."
      }
    ],
    "desc": "This API is used to get the status of a real-time process pulling task."
  },
  "DescribeOverviewStatistics": {
    "params": [],
    "desc": "This API is used to get the overview statistics of CWP under the current account."
  },
  "UntrustMaliciousRequest": {
    "params": [
      {
        "name": "Id",
        "desc": "Trusted record ID."
      }
    ],
    "desc": "This API is used to untrust a malicious request."
  },
  "DescribeUsualLoginPlaces": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `UUID`"
      }
    ],
    "desc": "This API is used to query usual login locations."
  },
  "DescribeMachineInfo": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`."
      }
    ],
    "desc": "This API is used to get server details."
  },
  "ExportNonlocalLoginPlaces": {
    "params": [],
    "desc": "This API is used to export unusual login location events into a CSV file."
  },
  "DescribeWeeklyReportInfo": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "Weekly CWP Pro report start time."
      }
    ],
    "desc": "This API is used to get the details in the weekly CWP Pro report."
  },
  "DescribeOpenPortTaskStatus": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`."
      }
    ],
    "desc": "This API is used to get the status of a real-time port pulling task."
  },
  "DescribeSecurityDynamics": {
    "params": [
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to get the security event message data."
  },
  "DeleteMaliciousRequests": {
    "params": [
      {
        "name": "Ids",
        "desc": "Malicious request record ID array. Maximum value: 100 entries."
      }
    ],
    "desc": "This API is used to delete malicious request records."
  },
  "RescanImpactedHost": {
    "params": [
      {
        "name": "Id",
        "desc": "Vulnerability ID."
      }
    ],
    "desc": "This API is used to re-scan for vulnerabilities."
  },
  "DescribeLoginWhiteList": {
    "params": [
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Keywords - String - Required: No - Query keywords</li>"
      }
    ],
    "desc": "This API is used to get the list of login allowlist entries."
  },
  "DescribeImpactedHosts": {
    "params": [
      {
        "name": "VulId",
        "desc": "Vulnerability category ID."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)</li>"
      }
    ],
    "desc": "This API is used to get the list of servers affected by a vulnerability."
  },
  "DescribeTags": {
    "params": [
      {
        "name": "MachineType",
        "desc": ""
      },
      {
        "name": "MachineRegion",
        "desc": ""
      }
    ],
    "desc": "This API is used to get all server tags."
  },
  "DescribeSecurityTrends": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "Start time."
      },
      {
        "name": "EndDate",
        "desc": "End time."
      }
    ],
    "desc": "This API is used to get the security event statistics."
  },
  "DeleteMalwares": {
    "params": [
      {
        "name": "Ids",
        "desc": "Trojan record ID array"
      }
    ],
    "desc": "This API is used to delete trojan records."
  },
  "CloseProVersion": {
    "params": [
      {
        "name": "Quuid",
        "desc": "Server `Uuid`.\n`InstanceId` for BM or `Uuid` for CVM"
      }
    ],
    "desc": "This API is used to deactivate CWP Pro."
  },
  "DescribeWeeklyReportNonlocalLoginPlaces": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "Weekly CWP Pro report start time."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to get the unusual login location data in the weekly CWP Pro report."
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`. Either `Username` or `Uuid` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server."
      },
      {
        "name": "Username",
        "desc": "CWP agent `Uuid`. Either `Username` or `Uuid` must be specified. If `Username` is specified, it indicates to query the information list under the specified username."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Username - String - Required: No - Account name</li>\n<li>Privilege - String - Required: No - Account name (ORDINARY: ordinary account, SUPPER: super admin account)</li>\n<li>MachineIp - String - Required: No - Private IP of server</li>"
      }
    ],
    "desc": "This API is used to get the account list."
  },
  "DescribeVuls": {
    "params": [
      {
        "name": "VulType",
        "desc": "Vulnerability type.\n<li>WEB: web application vulnerability</li>\n<li>SYSTEM: system component vulnerability</li>\n<li>BASELINE: security baseline</li>"
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)\n\nOnly one value is allowed for the `Status` filter, and \"OR\" logic is not supported."
      }
    ],
    "desc": "This API is used to get the vulnerability list."
  },
  "DescribeWeeklyReports": {
    "params": [
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      }
    ],
    "desc": "This API is used to get the weekly report list."
  },
  "DeleteLoginWhiteList": {
    "params": [
      {
        "name": "Ids",
        "desc": "Whitelist ID"
      }
    ],
    "desc": "This API is used to delete a allowlist rule."
  },
  "CreateOpenPortTask": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`."
      }
    ],
    "desc": "This API is used to create a real-time port acquisition task."
  },
  "ModifyLoginWhiteList": {
    "params": [
      {
        "name": "Rules",
        "desc": "Whitelist rule"
      }
    ],
    "desc": "This API is used to edit a allowlist rule."
  },
  "DescribeProVersionInfo": {
    "params": [],
    "desc": "This API is used to get the CWP Pro information."
  },
  "IgnoreImpactedHosts": {
    "params": [
      {
        "name": "Ids",
        "desc": "Vulnerability ID array."
      }
    ],
    "desc": "This API is used to ignore one or more vulnerabilities."
  },
  "DeleteBruteAttacks": {
    "params": [
      {
        "name": "Ids",
        "desc": "Brute force attack event ID array."
      }
    ],
    "desc": "This API is used to delete brute force attack records."
  },
  "DescribeAgentVuls": {
    "params": [
      {
        "name": "VulType",
        "desc": "Vulnerability type.\n<li>WEB: web application vulnerability</li>\n<li>SYSTEM: system component vulnerability</li>\n<li>BASELINE: security baseline</li>"
      },
      {
        "name": "Uuid",
        "desc": "Agent `UUID`."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)"
      }
    ],
    "desc": "This API is used to get the list of vulnerabilities on a single server."
  },
  "OpenProVersion": {
    "params": [
      {
        "name": "MachineType",
        "desc": "Server type.\n<li>CVM: CVM</li>\n<li>BM: BM</li>"
      },
      {
        "name": "MachineRegion",
        "desc": "Server region\nExamples: ap-guangzhou, ap-shanghai"
      },
      {
        "name": "Quuids",
        "desc": "Server `Uuid` array.\n`InstanceId` for BM or `Uuid` for CVM"
      },
      {
        "name": "ActivityId",
        "desc": "Event ID."
      }
    ],
    "desc": "This API is used to activate CWP Pro."
  },
  "DescribeAccountStatistics": {
    "params": [
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Username - String - Required: No - Account username</li>"
      }
    ],
    "desc": "This API is used to get the account statistics list."
  },
  "CreateProcessTask": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`."
      }
    ],
    "desc": "This API is used to create a real-time process pulling task."
  },
  "ModifyAlarmAttribute": {
    "params": [
      {
        "name": "Attribute",
        "desc": "Alarm item.\n<li>Offline: CWP is offline</li>\n<li>Malware: trojan event</li>\n<li>NonlocalLogin: unusual login location discovered</li>\n<li>CrackSuccess: brute force attack succeeded</li>"
      },
      {
        "name": "Value",
        "desc": "Alarm item attributes.\n<li>CLOSE: disabled</li>\n<li>OPEN: enabled</li>"
      }
    ],
    "desc": "This API is used to modify alarm settings."
  },
  "EditTags": {
    "params": [
      {
        "name": "Name",
        "desc": "Tag name"
      },
      {
        "name": "Id",
        "desc": "Tag ID"
      },
      {
        "name": "Quuids",
        "desc": "CVM instance ID"
      }
    ],
    "desc": "This API is used to add or edit tags."
  },
  "DescribeAlarmAttribute": {
    "params": [],
    "desc": "This API is used to get the alarm settings."
  },
  "DescribeOpenPortStatistics": {
    "params": [
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Port - Uint64 - Required: No - Port number</li>"
      }
    ],
    "desc": "This API is used to get the statistics on port usage"
  },
  "CreateUsualLoginPlaces": {
    "params": [
      {
        "name": "Uuids",
        "desc": "CWP agent `UUID` array."
      },
      {
        "name": "Places",
        "desc": "Login region information array."
      }
    ],
    "desc": "This API is used to add one or more usual login locations."
  },
  "DescribeComponents": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`. Either `Uuid` or `ComponentId` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server."
      },
      {
        "name": "ComponentId",
        "desc": "Component ID. Either `Uuid` or `ComponentId` must be specified. If `ComponentId` is specified, it indicates to query the information list under the specified component."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>ComponentVersion - String - Required: No - Component version number</li>\n<li>MachineIp - String - Required: No - Private IP of server</li>"
      }
    ],
    "desc": "This API is used to get the component list."
  },
  "ExportBruteAttacks": {
    "params": [],
    "desc": "This API is used to export brute force attack records into a CSV file."
  },
  "DescribeProcesses": {
    "params": [
      {
        "name": "Uuid",
        "desc": "CWP agent `Uuid`. Either `Uuid` or `ProcessName` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server."
      },
      {
        "name": "ProcessName",
        "desc": "Process name. Either `Uuid` or `ProcessName` must be specified. If `ProcessName` is specified, it indicates to query the information list under the specified process."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>ProcessName - String - Required: No - Process name</li>\n<li>MachineIp - String - Required: No - Private IP of server</li>"
      }
    ],
    "desc": "This API is used to get the process list."
  },
  "TrustMaliciousRequest": {
    "params": [
      {
        "name": "Id",
        "desc": "Malicious request record ID."
      }
    ],
    "desc": "This API is used to trust a malicious request."
  },
  "DescribeMalwares": {
    "params": [
      {
        "name": "Uuid",
        "desc": "Agent `Uuid`."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 10. Maximum value: 100."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Filters",
        "desc": "Filter.\n<li>Keywords - String - Required: No - Query keywords</li>\n<li>Status - String - Required: No - Trojan status (UN_OPERATED: not processed, SEGREGATED: isolated, TRUSTED: trusted)</li>\nEach filter supports only one value. Query with multiple values in \"OR\" relationship is not supported for the time being."
      }
    ],
    "desc": "This API is used to get the list of trojan events."
  }
}