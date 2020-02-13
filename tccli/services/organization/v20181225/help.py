# -*- coding: utf-8 -*-
DESC = "organization-2018-12-25"
INFO = {
  "DenyOrganizationInvitation": {
    "params": [
      {
        "name": "Id",
        "desc": "Invitation ID"
      }
    ],
    "desc": "This API is used to decline an invitation to an organization."
  },
  "ListOrganizationInvitations": {
    "params": [
      {
        "name": "Invited",
        "desc": "Whether to list the invitations you received or the invitations you sent. `1`: list the invitations you received; `0`: list the invitations you sent."
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Limit"
      }
    ],
    "desc": "This API is used to obtain an invitation list."
  },
  "UpdateOrganizationNode": {
    "params": [
      {
        "name": "NodeId",
        "desc": "Organizational unit ID"
      },
      {
        "name": "Name",
        "desc": "Name"
      },
      {
        "name": "ParentNodeId",
        "desc": "Parent organizational unit ID"
      }
    ],
    "desc": "This API is used to update organizational units."
  },
  "AcceptOrganizationInvitation": {
    "params": [
      {
        "name": "Id",
        "desc": "Invitation ID"
      }
    ],
    "desc": "This API is used to accept an invitation to an organization."
  },
  "DeleteOrganization": {
    "params": [],
    "desc": "This API is used to delete an organization."
  },
  "GetOrganization": {
    "params": [],
    "desc": "This API is used to obtain information on organizations."
  },
  "ListOrganizationNodes": {
    "params": [],
    "desc": "This API is used to obtain a list of organizational units."
  },
  "UpdateOrganizationMember": {
    "params": [
      {
        "name": "MemberUin",
        "desc": "Member UIN"
      },
      {
        "name": "Name",
        "desc": "Name"
      },
      {
        "name": "Remark",
        "desc": "Notes"
      }
    ],
    "desc": "This API is used to update information on organization members."
  },
  "QuitOrganization": {
    "params": [
      {
        "name": "OrgId",
        "desc": "Organization ID"
      }
    ],
    "desc": "This API is used to quit an organization."
  },
  "DeleteOrganizationNodes": {
    "params": [
      {
        "name": "NodeIds",
        "desc": "Organizational unit ID list"
      }
    ],
    "desc": "This API is used to delete multiple organizational units in a single request."
  },
  "ListOrganizationMembers": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Limit"
      }
    ],
    "desc": "This API is used to obtain a list of organization members."
  },
  "DeleteOrganizationMemberFromNode": {
    "params": [
      {
        "name": "MemberUin",
        "desc": "UIN of the member to be deleted"
      },
      {
        "name": "NodeId",
        "desc": "Organizational unit ID"
      }
    ],
    "desc": "This API is used to delete an organization member."
  },
  "AddOrganizationNode": {
    "params": [
      {
        "name": "ParentNodeId",
        "desc": "Parent organizational unit ID"
      },
      {
        "name": "Name",
        "desc": "Organizational unit name"
      }
    ],
    "desc": "This API is used to add an organizational unit."
  },
  "SendOrganizationInvitation": {
    "params": [
      {
        "name": "InviteUin",
        "desc": "UIN of the invitee"
      },
      {
        "name": "Name",
        "desc": "Name"
      },
      {
        "name": "Remark",
        "desc": "Notes"
      }
    ],
    "desc": "This API is used to send an invitation to join an organization."
  },
  "MoveOrganizationMembersToNode": {
    "params": [
      {
        "name": "NodeId",
        "desc": "Organizational unit ID"
      },
      {
        "name": "Uins",
        "desc": "Member UIN list"
      }
    ],
    "desc": "This API is used to move members to a specified organizational unit."
  },
  "GetOrganizationMember": {
    "params": [
      {
        "name": "MemberUin",
        "desc": "Organization member UIN"
      }
    ],
    "desc": "This API is used to obtain information on organization members."
  },
  "DeleteOrganizationMembers": {
    "params": [
      {
        "name": "Uins",
        "desc": "List of UINs of members to be deleted"
      }
    ],
    "desc": "This API is used to delete multiple organization members in a single request."
  },
  "ListOrganizationNodeMembers": {
    "params": [
      {
        "name": "NodeId",
        "desc": "Organizational unit ID"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Limit"
      }
    ],
    "desc": "This API is used to obtain a list of organizational unit members."
  },
  "CancelOrganizationInvitation": {
    "params": [
      {
        "name": "Id",
        "desc": "Invitation ID"
      }
    ],
    "desc": "This API is used to cancel an invitation to an organization."
  },
  "CreateOrganization": {
    "params": [
      {
        "name": "OrgType",
        "desc": "Organization type; currently its value is fixed as `1`"
      }
    ],
    "desc": "This API is used to create an organization."
  }
}