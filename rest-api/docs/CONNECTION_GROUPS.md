# Connection Groups

# Table of Contents
- [Create Connection Group](#create-connection-group)
- [Update Connection Group](#update-connection-group)
- [Delete Connection Group](#delete-connection-group)
- [List Connection Groups](#list-connection-groups)
- [List Connections and Connection Groups](#list-connections-and-connection-groups)
- [Details of Connection Group](#details-of-connection-group)
- [Details of Connection Group Tree](#details-of-connection-group-tree)

## Create Connection Group
- Creating a connection group.

### Request

#### Method
- POST

#### Endpoint
- /api/session/data/{dataSource}/connectionGroups

#### Path Parameters
| Name                                 | Type    | Description                               |
| ------------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)                | string  | The data source used by Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                      | Type     | Description                                                                                    |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------- |
| name                      | string   | Name of the connection group.                                                                  |
| parentIdentifier          | string   | Identifier of the parent connection group. Must be ROOT if no parent connection group is used. |
| type                      | string   | Type of the connection group, such as organizational or balancing.                             |
| attributes                | object   | Information and settings of the connection group.                                              |
| max-connections           | integer  | Maximum number of concurrent connections.                                                      |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                             |
| enable-session-affinity   | boolean  | Assigning of the same connection to the users within a balancing group until they log out.     |

#### Example of Body
```json
{
    "name": "connectionGroup-example",
    "parentIdentifier": "ROOT",
    "type": "ORGANIZATIONAL",
    "attributes": {
        "max-connections": "5",
        "max-connections-per-user": "1",
        "enable-session-affinity": ""
    }
}
```
### Response

#### Normal Response Code
- 200 OK

#### Body
| Name                      | Type     | Description                                                                                    |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------- |
| name                      | string   | Name of the connection group.                                                                  |
| identifier                | integer  | Identifier of the connection group.                                                            |
| parentIdentifier          | string   | Identifier of the parent connection group. Must be ROOT if no parent connection group is used. |
| type                      | string   | Type of the connection group, such as organizational or balancing.                             |
| activeConnections         | integer  | Number of active connections.                                                                  |
| attributes                | object   | Information and settings of the connection group.                                              |
| max-connections           | integer  | Maximum number of concurrent connections.                                                      |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                             |
| enable-session-affinity   | boolean  | Assigning of the same connection to the users within a balancing group until they log out.     |

#### Example of Body
```json
{
    "name": "connectionGroup",
    "identifier": "1",
    "parentIdentifier": "ROOT",
    "type": "ORGANIZATIONAL",
    "activeConnections": 0,
    "attributes": {
        "max-connections": "5",
        "max-connections-per-user": "1",
        "enable-session-affinity": ""
    }
}
```

## Update Connection Group
- Updating a connection group.

### Request

#### Method
- PUT

#### Endpoint
- /api/session/data/{dataSource}/connectionGroups/{connectionGroupIdentifier}

#### Path Parameters
| Name                                 | Type    | Description                               |
| ------------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)                | string  | The data source used by Apache Guacamole. |
| connectionGroupIdentifier (Required) | integer | The identifier of the connection group.   |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                      | Type     | Description                                                                                    |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------- |
| name                      | string   | Name of the connection group.                                                                  |
| identifier                | integer  | Identifier of the connection group.                                                            |
| parentIdentifier          | string   | Identifier of the parent connection group. Must be ROOT if no parent connection group is used. |
| type                      | string   | Type of the connection group, such as organizational or balancing.                             |
| activeConnections         | integer  | Number of active connections.                                                                  |
| attributes                | object   | Information and settings of the connection group.                                              |
| max-connections           | integer  | Maximum number of concurrent connections.                                                      |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                             |
| enable-session-affinity   | boolean  | Assigning of the same connection to the users within a balancing group until they log out.     |

#### Example of Body
```json
{
    "name": "connectionGroup-example",
    "parentIdentifier": "ROOT",
    "type": "ORGANIZATIONAL",
    "attributes": {
        "max-connections": "5",
        "max-connections-per-user": "2",
        "enable-session-affinity": ""
    }
}
```
### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Delete Connection Group
- Deleting a connection group.

### Request

#### Method
- DELETE

#### Endpoint
- /api/session/data/{dataSource}/connectionGroups/{connectionGroupIdentifier}

#### Path Parameters
| Name                                 | Type    | Description                               |
| ------------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)                | string  | The data source used by Apache Guacamole. |
| connectionGroupIdentifier (Required) | integer | The identifier of the connection group.   |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
- \-

#### Body
- \-

#### Example of Body
- \-

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## List Connection Groups
- List of connection groups. List of all connection groups including their details and settings.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/connectionGroups

#### Path Parameters
| Name                  | Type    | Description                               |
| --------------------- | ------- | ----------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
- \-

#### Body
- \-

#### Example of Body
- \-

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name                      | Type     | Description                                                                                    |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------- |
| name                      | string   | Name of the connection group.                                                                  |
| identifier                | integer  | Identifier of the connection group.                                                            |
| parentIdentifier          | string   | Identifier of the parent connection group. Must be ROOT if no parent connection group is used. |
| type                      | string   | Type of the connection group, such as organizational or balancing.                             |
| activeConnections         | integer  | Number of active connections.                                                                  |
| attributes                | object   | Information and settings of the connection group.                                              |
| max-connections           | integer  | Maximum number of concurrent connections.                                                      |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                             |
| enable-session-affinity   | boolean  | Assigning of the same connection to the users within a balancing group until they log out.     |

#### Example of Body
```json
{
    "1": {
        "name": "connectionGroup-example",
        "identifier": "1",
        "parentIdentifier": "ROOT",
        "type": "ORGANIZATIONAL",
        "activeConnections": 0,
        "attributes": {
            "max-connections": "5",
            "max-connections-per-user": "2",
            "enable-session-affinity": ""
        }
    }
}
```

## List Connections and Connection Groups
- List of connections and connection groups. List of all connection and connection groups including their details and settings.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/connectionGroups/ROOT/tree

#### Path Parameters
| Name                  | Type    | Description                               |
| --------------------- | ------- | ----------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
- \-

#### Body
- \-

#### Example of Body
- \-

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name                      | Type     | Description                                                                                                |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
| name                      | string   | Name of the ROOT (default) connection group, connection group or connection.                               |
| identifier                | integer  | Identifier of the ROOT (default) connection group, connection group or connection.                         |
| type                      | string   | Type of the connection group, such as organizational or balancing.                                         |
| activeConnections         | integer  | Number of active connections.                                                                              |
| childConnectionGroups     | array    | List of child connection groups.                                                                           |
| parentIdentifier          | string   | Identifier of the parent connection group. Must be ROOT if no parent connection group is used.             |
| attributes                | object   | Information and settings of the connection group or connection.                                            |
| max-connections           | integer  | Maximum number of concurrent connections.                                                                  |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                                         |
| enable-session-affinity   | boolean  | Assigning of the same connection to the users within a balancing group until they log out.                 |
| childConnections          | array    | List of child connections.                                                                                 |
| protocol                  | string   | Connection protocol.                                                                                       |
| guacd-encryption          | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                        |
| failover-only             | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred. |
| weight                    | integer  | It used for weighted load balancing algorithms.                                                            |
| guacd-hostname            | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                        |
| guacd-port                | integer  | Port for connecting to guacd. Default: 4822.                                                               |
| lastActive                | integer  | Date and time that this connection was last used, or null if this connection has never been used.          |

#### Example of Body
```json
{
    "name": "ROOT",
    "identifier": "ROOT",
    "type": "ORGANIZATIONAL",
    "activeConnections": 0,
    "childConnectionGroups": [
        {
            "name": "connectionGroup-example",
            "identifier": "1",
            "parentIdentifier": "ROOT",
            "type": "ORGANIZATIONAL",
            "activeConnections": 0,
            "attributes": {
                "max-connections": "5",
                "max-connections-per-user": "2",
                "enable-session-affinity": ""
            }
        }
    ],
    "childConnections": [
        {
            "name": "VNC-example",
            "identifier": "1",
            "parentIdentifier": "ROOT",
            "protocol": "vnc",
            "attributes": {
                "guacd-encryption": null,
                "failover-only": null,
                "weight": null,
                "max-connections": "2",
                "guacd-hostname": null,
                "guacd-port": null,
                "max-connections-per-user": "1"
            },
            "sharingProfiles": [
                {
                    "name": "sharingProfile-example",
                    "identifier": "1",
                    "primaryConnectionIdentifier": "1",
                    "attributes": {                
                    }
                }
            ],
            "activeConnections": 0,
            "lastActive": 1686504267000
        }
    ],
    "attributes": {}
}
```

## Details of Connection Group
- List of details and settings about a specific connection group.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/connectionGroups/{connectionGroupIdentifier}

#### Path Parameters
| Name                                 | Type    | Description                               |
| ------------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)                | string  | The data source used by Apache Guacamole. |
| connectionGroupIdentifier (Required) | integer | The identifier of the connection group.   |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
- \-

#### Body
- \-

#### Example of Body
- \-

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name                      | Type     | Description                                                                                    |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------- |
| name                      | string   | Name of the connection group.                                                                  |
| identifier                | integer  | Identifier of the connection group.                                                            |
| parentIdentifier          | string   | Identifier of the parent connection group. Must be ROOT if no parent connection group is used. |
| type                      | string   | Type of the connection group, such as organizational or balancing.                             |
| activeConnections         | integer  | Number of active connections.                                                                  |
| attributes                | object   | Information and settings of the connection group.                                              |
| max-connections           | integer  | Maximum number of concurrent connections.                                                      |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                             |
| enable-session-affinity   | boolean  | Assigning of the same connection to the users within a balancing group until they log out.     |

#### Example of Body
```json
{
    "name": "connectionGroup-example",
    "identifier": "1",
    "parentIdentifier": "ROOT",
    "type": "ORGANIZATIONAL",
    "activeConnections": 0,
    "attributes": {
        "max-connections": "5",
        "max-connections-per-user": "2",
        "enable-session-affinity": ""
    }
}
```

## Details of Connection Group Tree
- List of connections and connection groups of connection group tree.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/connectionGroups/{connectionGroupIdentifier}/tree

#### Path Parameters
| Name                                 | Type    | Description                               |
| ------------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)                | string  | The data source used by Apache Guacamole. |
| connectionGroupIdentifier (Required) | integer | The identifier of the connection group.   |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
- \-

#### Body
- \-

#### Example of Body
- \-

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name                      | Type     | Description                                                                                                |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
| name                      | string   | Name of the  connection group or connection.                                                               |
| identifier                | integer  | Identifier of the connection group or connection.                                                          |
| parentIdentifier          | string   | Identifier of the parent connection group. Must be ROOT if no parent connection group is used.             |
| type                      | string   | Type of the connection group, such as organizational or balancing.                                         |
| activeConnections         | integer  | Number of active connections.                                                                              |
| childConnectionGroups     | array    | List of child connection groups.                                                                           |
| childConnections          | array    | List of child connections.                                                                                 |
| protocol                  | string   | Connection protocol.                                                                                       |
| attributes                | object   | Information and settings of the connection group or connection.                                            |
| guacd-encryption          | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                        |
| failover-only             | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred. |
| weight                    | integer  | It used for weighted load balancing algorithms.                                                            |
| max-connections           | integer  | Maximum number of concurrent connections.                                                                  |
| guacd-hostname            | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                        |
| guacd-port                | integer  | Port for connecting to guacd. Default: 4822.                                                               |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                                         |
| enable-session-affinity   | boolean  | Assigning of the same connection to the users within a balancing group until they log out.     |

#### Example of Body
```json
{
    "name": "connectionGroup-example",
    "identifier": "1",
    "parentIdentifier": "ROOT",
    "type": "ORGANIZATIONAL",
    "activeConnections": 0,
    "childConnections": [
        {
            "name": "SSH-example",
            "identifier": "2",
            "parentIdentifier": "1",
            "protocol": "ssh",
            "attributes": {
                "guacd-encryption": null,
                "failover-only": null,
                "weight": null,
                "max-connections": "2",
                "guacd-hostname": null,
                "guacd-port": null,
                "max-connections-per-user": "1"
            },
            "activeConnections": 0
        }
    ],
    "attributes": {
        "max-connections": "5",
        "max-connections-per-user": "2",
        "enable-session-affinity": ""
    }
}
```
