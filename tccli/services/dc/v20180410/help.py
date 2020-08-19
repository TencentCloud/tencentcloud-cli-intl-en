# -*- coding: utf-8 -*-
DESC = "dc-2018-04-10"
INFO = {
  "ModifyDirectConnectAttribute": {
    "params": [
      {
        "name": "DirectConnectId",
        "desc": "Connection ID."
      },
      {
        "name": "DirectConnectName",
        "desc": "Connection name."
      },
      {
        "name": "CircuitCode",
        "desc": "Circuit code of connection, which is provided by the ISP or connection provider."
      },
      {
        "name": "Vlan",
        "desc": "VLAN for connection debugging."
      },
      {
        "name": "TencentAddress",
        "desc": "Tencent-side IP address for connection debugging."
      },
      {
        "name": "CustomerAddress",
        "desc": "User-side IP address for connection debugging."
      },
      {
        "name": "CustomerName",
        "desc": "Name of connection applicant, which is obtained from the account system by default."
      },
      {
        "name": "CustomerContactMail",
        "desc": "Email address of connection applicant, which is obtained from the account system by default."
      },
      {
        "name": "CustomerContactNumber",
        "desc": "Contact number of connection applicant, which is obtained from the account system by default."
      },
      {
        "name": "FaultReportContactPerson",
        "desc": "Fault reporting contact person."
      },
      {
        "name": "FaultReportContactNumber",
        "desc": "Fault reporting contact number."
      },
      {
        "name": "SignLaw",
        "desc": "Whether the connection applicant has signed the service agreement."
      }
    ],
    "desc": "This API is used to modify connection attributes."
  },
  "CreateDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectId",
        "desc": "Direct Connect ID, such as `dc-kd7d06of`."
      },
      {
        "name": "DirectConnectTunnelName",
        "desc": "Dedicated tunnel name."
      },
      {
        "name": "DirectConnectOwnerAccount",
        "desc": "Connection owner, who is the current customer by default.\nThe developer account ID should be entered for shared connections."
      },
      {
        "name": "NetworkType",
        "desc": "Network type. Valid values: VPC, BMVPC, CCN. Default value: VPC.\nVPC: Virtual Private Cloud.\nBMVPC: BM VPC.\nCCN: Cloud Connect Network."
      },
      {
        "name": "NetworkRegion",
        "desc": "Network region."
      },
      {
        "name": "VpcId",
        "desc": "Unified VPC ID or BMVPC ID."
      },
      {
        "name": "DirectConnectGatewayId",
        "desc": "Direct connect gateway ID, such as `dcg-d545ddf`."
      },
      {
        "name": "Bandwidth",
        "desc": "Direct Connect bandwidth in Mbps.\nDefault value: connection bandwidth value."
      },
      {
        "name": "RouteType",
        "desc": "BGP: BGP routing.\nSTATIC: Static routing.\nDefault value: BGP routing."
      },
      {
        "name": "BgpPeer",
        "desc": "BgpPeer, which is BGP information on the user side and includes Asn and AuthKey."
      },
      {
        "name": "RouteFilterPrefixes",
        "desc": "Static routing, i.e., IP range of the user's IDC."
      },
      {
        "name": "Vlan",
        "desc": "VLAN. Value range: 0-3,000.\n0: sub-interface not enabled.\nDefault value: Non-zero."
      },
      {
        "name": "TencentAddress",
        "desc": "TencentAddress: Tencent-side IP address."
      },
      {
        "name": "CustomerAddress",
        "desc": "CustomerAddress: User-side IP address."
      },
      {
        "name": "TencentBackupAddress",
        "desc": "TencentBackupAddress, i.e., Tencent-side standby IP address"
      }
    ],
    "desc": "This API is used to create a dedicated tunnel."
  },
  "DeleteDirectConnect": {
    "params": [
      {
        "name": "DirectConnectId",
        "desc": "Connection ID."
      }
    ],
    "desc": "This API is used to delete a connection.\nOnly connected connections can be deleted."
  },
  "AcceptDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "The connection owner accepts an application for sharing the dedicated tunnel"
      }
    ],
    "desc": "This API is used to accept an application for a dedicated tunnel."
  },
  "DeleteDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "Dedicated tunnel ID."
      }
    ],
    "desc": "This API is used to delete a dedicated tunnel."
  },
  "CreateDirectConnect": {
    "params": [
      {
        "name": "DirectConnectName",
        "desc": "Connection name."
      },
      {
        "name": "AccessPointId",
        "desc": "Access point of connection.\nYou can call `DescribeAccessPoints` to get the region ID. The selected access point must exist and be available."
      },
      {
        "name": "LineOperator",
        "desc": "ISP that provides connections. Valid values: ChinaTelecom (China Telecom), ChinaMobile (China Mobile), ChinaUnicom (China Unicom), In-houseWiring (in-house wiring), ChinaOther (other Chinese ISPs), InternationalOperator (international ISPs)."
      },
      {
        "name": "PortType",
        "desc": "Port type of connection. Valid values: 100Base-T (100-Megabit electrical Ethernet interface), 1000Base-T (1-Gigabit electrical Ethernet interface), 1000Base-LX (1-Gigabit single-module optical Ethernet interface; 10 KM), 10GBase-T (10-Gigabit electrical Ethernet interface), 10GBase-LR (10-Gigabit single-module optical Ethernet interface; 10 KM). Default value: 1000Base-LX."
      },
      {
        "name": "CircuitCode",
        "desc": "Circuit code of connection, which is provided by the ISP or connection provider."
      },
      {
        "name": "Location",
        "desc": "Local IDC location."
      },
      {
        "name": "Bandwidth",
        "desc": "Connection port bandwidth in Mbps. Value range: [2,10240]. Default value: 1000."
      },
      {
        "name": "RedundantDirectConnectId",
        "desc": "ID of redundant connection."
      },
      {
        "name": "Vlan",
        "desc": "VLAN for connection debugging, which is enabled and automatically assigned by default."
      },
      {
        "name": "TencentAddress",
        "desc": "Tencent-side IP address for connection debugging, which is automatically assigned by default."
      },
      {
        "name": "CustomerAddress",
        "desc": "User-side IP address for connection debugging, which is automatically assigned by default."
      },
      {
        "name": "CustomerName",
        "desc": "Name of connection applicant, which is obtained from the account system by default."
      },
      {
        "name": "CustomerContactMail",
        "desc": "Email address of connection applicant, which is obtained from the account system by default."
      },
      {
        "name": "CustomerContactNumber",
        "desc": "Contact number of connection applicant, which is obtained from the account system by default."
      },
      {
        "name": "FaultReportContactPerson",
        "desc": "Fault reporting contact person."
      },
      {
        "name": "FaultReportContactNumber",
        "desc": "Fault reporting contact number."
      },
      {
        "name": "SignLaw",
        "desc": "Whether the connection applicant has signed the service agreement. Default value: true."
      }
    ],
    "desc": "This API is used to apply for a connection.\nWhen calling this API, please note that:\nYou need to complete identity verification for your account; otherwise, you cannot apply for a connection;\nIf there is any connection in arrears under your account, you cannot apply for more connections."
  },
  "DescribeDirectConnectTunnels": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions:\nThis parameter does not support specifying `DirectConnectTunnelIds` and `Filters` at the same time.\n<li> direct-connect-tunnel-name: Dedicated tunnel name.</li>\n<li> direct-connect-tunnel-id: Dedicated tunnel instance ID, such as `dcx-abcdefgh`.</li>\n<li>direct-connect-id: Connection instance ID, such as `dc-abcdefgh`.</li>"
      },
      {
        "name": "DirectConnectTunnelIds",
        "desc": "Array of dedicated tunnel IDs."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      }
    ],
    "desc": "This API is used to query the list of dedicated tunnels."
  },
  "DescribeAccessPoints": {
    "params": [
      {
        "name": "RegionId",
        "desc": "Access point region, which can be queried through `DescribeRegions`.\n\nYou can call `DescribeRegions` to get the region ID."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of results to be returned. Default value: 20. Maximum value: 100."
      }
    ],
    "desc": "This API is used to query connection access points.\n"
  },
  "RejectDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "None."
      }
    ],
    "desc": "This API is used to reject an application for a dedicated tunnel."
  },
  "DescribeDirectConnects": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions:"
      },
      {
        "name": "DirectConnectIds",
        "desc": "Array of connection IDs."
      },
      {
        "name": "Offset",
        "desc": "Offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 20. Maximum value: 100."
      }
    ],
    "desc": "This API is used to query the list of connections."
  },
  "ModifyDirectConnectTunnelAttribute": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "Dedicated tunnel ID."
      },
      {
        "name": "DirectConnectTunnelName",
        "desc": "Dedicated tunnel name."
      },
      {
        "name": "BgpPeer",
        "desc": "User-side BGP, including Asn and AuthKey."
      },
      {
        "name": "RouteFilterPrefixes",
        "desc": "User-side IP range."
      },
      {
        "name": "TencentAddress",
        "desc": "Tencent-side IP address."
      },
      {
        "name": "CustomerAddress",
        "desc": "User-side IP address."
      },
      {
        "name": "Bandwidth",
        "desc": "Bandwidth value of a dedicated tunnel in Mbps."
      },
      {
        "name": "TencentBackupAddress",
        "desc": "Tencent-side standby IP address"
      }
    ],
    "desc": "This API is used to modify the dedicated tunnel attributes."
  }
}