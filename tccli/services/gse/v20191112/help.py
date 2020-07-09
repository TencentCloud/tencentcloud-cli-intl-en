# -*- coding: utf-8 -*-
DESC = "gse-2019-11-12"
INFO = {
  "UpdateGameServerSession": {
    "params": [
      {
        "name": "GameServerSessionId",
        "desc": "Game server session ID"
      },
      {
        "name": "MaximumPlayerSessionCount",
        "desc": "Maximum number of players"
      },
      {
        "name": "Name",
        "desc": "Game server session name"
      },
      {
        "name": "PlayerSessionCreationPolicy",
        "desc": "Player session creation policy. Valid values: ACCEPT_ALL, DENY_ALL"
      },
      {
        "name": "ProtectionPolicy",
        "desc": "Protection policy. Valid values: NoProtection, TimeLimitProtection, FullProtection"
      }
    ],
    "desc": "This API is used to update a game server session."
  },
  "StopGameServerSessionPlacement": {
    "params": [
      {
        "name": "PlacementId",
        "desc": "Unique ID of game server session placement"
      }
    ],
    "desc": "This API is used to stop placing a game server session."
  },
  "DescribeGameServerSessions": {
    "params": [
      {
        "name": "AliasId",
        "desc": "Alias ID"
      },
      {
        "name": "FleetId",
        "desc": "Fleet ID"
      },
      {
        "name": "GameServerSessionId",
        "desc": "Game server session ID"
      },
      {
        "name": "Limit",
        "desc": "Maximum number of entries in a single query"
      },
      {
        "name": "NextToken",
        "desc": "Pagination offset, which is used for querying the next page"
      },
      {
        "name": "StatusFilter",
        "desc": "Game server session status. Valid values: ACTIVE, ACTIVATING, TERMINATED, TERMINATING, ERROR"
      }
    ],
    "desc": "This API is used to query the list of game server sessions."
  },
  "GetInstanceAccess": {
    "params": [
      {
        "name": "FleetId",
        "desc": "Service deployment ID"
      },
      {
        "name": "InstanceId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to get the credentials required for instance login."
  },
  "JoinGameServerSession": {
    "params": [
      {
        "name": "GameServerSessionId",
        "desc": "Game server session ID"
      },
      {
        "name": "PlayerId",
        "desc": "Player ID"
      },
      {
        "name": "PlayerData",
        "desc": "Custom player information"
      }
    ],
    "desc": "This API is used to join a game server session."
  },
  "DescribeGameServerSessionPlacement": {
    "params": [
      {
        "name": "PlacementId",
        "desc": "Unique ID of game server session placement"
      }
    ],
    "desc": "This API is used to query the placement of a game server session."
  },
  "DescribeGameServerSessionDetails": {
    "params": [
      {
        "name": "AliasId",
        "desc": "Alias ID"
      },
      {
        "name": "FleetId",
        "desc": "Fleet ID"
      },
      {
        "name": "GameServerSessionId",
        "desc": "Game server session ID"
      },
      {
        "name": "Limit",
        "desc": "Maximum number of entries in a single query"
      },
      {
        "name": "NextToken",
        "desc": "Pagination offset, which is used for querying the next page"
      },
      {
        "name": "StatusFilter",
        "desc": "Game server session status. Valid values: ACTIVE, ACTIVATING, TERMINATED, TERMINATING, ERROR"
      }
    ],
    "desc": "This API is used to query the list of game server session details."
  },
  "StartGameServerSessionPlacement": {
    "params": [
      {
        "name": "PlacementId",
        "desc": "Unique ID of starting game server session placement"
      },
      {
        "name": "GameServerSessionQueueName",
        "desc": "Game server session queue name"
      },
      {
        "name": "MaximumPlayerSessionCount",
        "desc": "Maximum number of concurrent players allowed by the game server to connect to the game session"
      },
      {
        "name": "DesiredPlayerSessions",
        "desc": "Player game session information"
      },
      {
        "name": "GameProperties",
        "desc": "Player game session attributes"
      },
      {
        "name": "GameServerSessionData",
        "desc": "Game server session data"
      },
      {
        "name": "GameServerSessionName",
        "desc": "Game server session name"
      },
      {
        "name": "PlayerLatencies",
        "desc": "Player latency"
      }
    ],
    "desc": "This API is used to start placing a game server session."
  },
  "DescribePlayerSessions": {
    "params": [
      {
        "name": "GameServerSessionId",
        "desc": "Game server session ID"
      },
      {
        "name": "Limit",
        "desc": "Maximum number of entries in a single query"
      },
      {
        "name": "NextToken",
        "desc": "Pagination offset, which is used for querying the next page"
      },
      {
        "name": "PlayerId",
        "desc": "Player ID"
      },
      {
        "name": "PlayerSessionId",
        "desc": "Player session ID"
      },
      {
        "name": "PlayerSessionStatusFilter",
        "desc": "Player session status. Valid values: RESERVED, ACTIVE, COMPLETED, TIMEDOUT"
      }
    ],
    "desc": "This API is used to get the list of player sessions."
  },
  "GetGameServerSessionLogUrl": {
    "params": [
      {
        "name": "GameServerSessionId",
        "desc": "Game server session ID"
      }
    ],
    "desc": "This API is used to get the log URL of a game server session."
  },
  "SearchGameServerSessions": {
    "params": [
      {
        "name": "AliasId",
        "desc": "Alias ID"
      },
      {
        "name": "FleetId",
        "desc": "Fleet ID"
      },
      {
        "name": "Limit",
        "desc": "Maximum number of entries in a single query"
      },
      {
        "name": "NextToken",
        "desc": "Pagination offset, which is used for querying the next page"
      },
      {
        "name": "FilterExpression",
        "desc": "Search filter expression. Valid values:\ngameServerSessionName: game session name in `String` type\ngameServerSessionId: game session ID in `String` type\nmaximumSessions: maximum number of player sessions in `Number` type\ncreationTimeMillis: creation time in milliseconds in `Number` type\nplayerSessionCount: current number of player sessions in `Number` type\nhasAvailablePlayerSessions: whether there is available player session in `String` type. Valid values: true, false\ngameServerSessionProperties: game session attributes in `String` type\n\nExpressions in `String` type support = and <> for judgment\nExpressions in `Number` type support =, <>, >, >=, <, and <= for judgment"
      },
      {
        "name": "SortExpression",
        "desc": "Sorting keyword\nValid values:\ngameServerSessionName: game session name in `String` type\ngameServerSessionId: game session ID in `String` type\nmaximumSessions: maximum number of player sessions in `Number` type\ncreationTimeMillis: creation time in milliseconds in `Number` type\nplayerSessionCount: current number of player sessions in `Number` type"
      }
    ],
    "desc": "This API is used to search in the list of game server sessions."
  },
  "CreateGameServerSession": {
    "params": [
      {
        "name": "MaximumPlayerSessionCount",
        "desc": "Maximum number of players"
      },
      {
        "name": "AliasId",
        "desc": "Alias ID"
      },
      {
        "name": "CreatorId",
        "desc": "Creator ID"
      },
      {
        "name": "FleetId",
        "desc": "Fleet ID"
      },
      {
        "name": "GameProperties",
        "desc": "Game attributes"
      },
      {
        "name": "GameServerSessionData",
        "desc": "Game server session attribute details"
      },
      {
        "name": "GameServerSessionId",
        "desc": "Custom ID of game server session"
      },
      {
        "name": "IdempotencyToken",
        "desc": "Idempotency token"
      },
      {
        "name": "Name",
        "desc": "Game server session name"
      }
    ],
    "desc": "This API is used to create a game server session."
  }
}