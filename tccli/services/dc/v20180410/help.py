# -*- coding: utf-8 -*-
DESC = "dc-2018-04-10"
INFO = {
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
      }
    ],
    "desc": "This API is used to create a dedicated tunnel."
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
      }
    ],
    "desc": "This API is used to modify the dedicated tunnel attributes."
  }
}