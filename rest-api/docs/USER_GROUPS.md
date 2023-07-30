# User Groups

# Table of Contents
- [Create User Group](#create-user-group)
- [Update User Group](#update-user-group)
- [Delete User Group](#delete-user-group)
- [Assign Permissions to a User Group](#assign-permissions-to-user-group)
- [Assign Member User to User Group](#assign-member-user-to-user-group)
- [Assign Member User Group to User Group](#assign-member-user-group-to-user-group)
- [Assign Parent User Group to User Group](#assign-parent-user-group-to-user-group)
- [Assign User Group to Connection](#assign-user-group-to-connection)
- [Assign User Group to Connection Group](#assign-user-group-to-connection-group)
- [Revoke Permissions from a User Group](#revoke-permissions-from-a-user-group)
- [Revoke Member User from User Group](#revoke-member-user-from-user-group)
- [Revoke Member User Group from User Group](#revoke-member-user-group-from-user-group)
- [Revoke Parent User Group from User Group](#revoke-parent-user-group-from-user-group)
- [Revoke User Group from Connection](#revoke-user-group-from-connection)
- [Revoke User Group from Connection Group](#revoke-user-group-from-connection-group)
- [List User Groups](#list-user-groups)
- [Details of User Group](#details-of-user-group)
- [Details of User Group Permissions](#details-of-user-group-permissions)

## Create User Group
- Creating a user group.

### Request

#### Method
- POST

#### Endpoint
- /api/session/data/{dataSource}/userGroups

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name          | Type        | Description                                             |
| --------------| ----------- | ------------------------------------------------------- |
| identifier    | string      | The identifier (name) of the user group.                |
| attributes    | object      | Contains detailed user groups information and settings. |
| disabled      | boolean     | Disabling a user group.                                 |

#### Example of Body
```json
{
    "identifier": "userGroup-example",
    "attributes": {
        "disabled": "false"
    }
}
```

### Response

#### Normal Response Code
- 200 OK

#### Body
- \-

#### Example of Body
```json
{
    "identifier": "userGroup-example",
    "attributes": {
        "disabled": "false"
    }
}
```

## Update User Group
- Updating a user group.

### Request

#### Method
- PUT

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name          | Type        | Description                                             |
| --------------| ----------- | ------------------------------------------------------- |
| identifier    | string      | The identifier (name) of the user group.                |
| attributes    | object      | Contains detailed user groups information and settings. |
| disabled      | boolean     | Disabling a user group.                                 |

#### Example of Body
```json
{
    "identifier": "userGroup-example",
    "attributes": {
        "disabled": "true"
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

## Delete User Group
- Deleting a user group.

### Request

#### Method
- DELETE

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

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

## Assign Permissions to User Group
- Assigning permissions to a user group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/permissions

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                              |
| -------- | ------- | -------------------------------------------------------- |
| op       | string  | Indicates the assignment of permissions to a user group. |
| path     | string  | The path for assigning permissions to a user group.      |
| value    | string  | Type of user group permissions. <br> CREATE_USER - Creating new users. <br> CREATE_USER_GROUP - Creating new user groups. <br> CREATE_CONNECTION - Creating new connections. <br> CREATE_CONNECTION_GROUP - Creating new connection groups. <br> CREATE_SHARING_PROFILE - Creating new sharing profiles. <br> ADMINISTER - System administration. |

#### Example of Body
```json
[
    {
        "op": "add",
        "path": "/systemPermissions",
        "value": "ADMINISTER"
    },
    {
        "op": "add",
        "path": "/systemPermissions",
        "value": "CREATE_USER"
    },
    {
        "op": "add",
        "path": "/systemPermissions",
        "value": "CREATE_USER_GROUP"
    },
    {
        "op": "add",
        "path": "/systemPermissions",
        "value": "CREATE_CONNECTION"
    },
    {
        "op": "add",
        "path": "/systemPermissions",
        "value": "CREATE_CONNECTION_GROUP"
    },
    {
        "op": "add",
        "path": "/systemPermissions",
        "value": "CREATE_SHARING_PROFILE"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Assign Member User to User Group
- Assigning a member user to a user group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/memberUsers

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                        |
| -------- | ------- | ------------------------------------------------------------------ |
| op       | string  | Indicates the user's assignment to a user group.                   |
| path     | string  | The path to assign a user to a user group.                         |
| value    | string  | The username of the user who should be assigned to the user group. | 

#### Example of Body
```json
[
    {
        "op": "add",
        "path": "/",
        "value": "johnexample"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Assign Member User Group to User Group
- Assigning a member user group to a user group. A member user group will inherit the permissions of the parent user group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/memberUserGroups

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                      |
| -------- | ------- | ---------------------------------------------------------------- |
| op       | string  | Indicates the assignment of a member user group to a user group. |
| path     | string  | The path to assing a member user group to a user group.          |
| value    | string  | The identifier (name) of the member user group.                  | 

#### Example of Body
```json
[
    {
        "op": "add",
        "path": "/",
        "value": "memberUserGroup-example"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Assign Parent User Group to User Group
- Assigning a parent user group to a user group. A member user group will inherit the permissions of the parent user group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/userGroups

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                      |
| -------- | ------- | ---------------------------------------------------------------- |
| op       | string  | Indicates the assignment of a parent user group to a user group. |
| path     | string  | The path to assing a parent user group to a user group.          |
| value    | string  | The identifier (name) of the parent user group.                  |

#### Example of Body
```json
[
    {
        "op": "add",
        "path": "/",
        "value": "parentUserGroup-example"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Assign User Group to Connection
- Assigning a user group to a connection.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/permissions

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                                                                               |
| -------- | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| op       | string  | Indicates the assignment of the user group to a connection.                                                               |
| path     | string  | The path to assign a user group to a connection and the connection identifier to which the user group should be assigned. |
| value    | string  | Access to the connection.                                                                                                 |

#### Example of Body
```json
[
    {
        "op": "add",
        "path": "/connectionPermissions/1",
        "value": "READ"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Assign User Group to Connection Group
- Assigning a user group to a connection group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/permissions

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                                                                                           |
| -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| op       | string  | Indicates the assignment of the user group to a connection group.                                                                     |
| path     | string  | The path to assign a user group to a connection group and the connection group identifier to which the user group should be assigned. |
| value    | string  | Access to the connection group.                                                                                                       |

#### Example of Body
```json
[
    {
        "op": "add",
        "path": "/connectionGroupPermissions/1",
        "value": "READ"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Revoke Permissions from a User Group
- Revoking permissions from a user group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/permissions

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                |
| -------- | ------- | ---------------------------------------------------------- |
| op       | string  | Indicates the revocation of permissions from a user group. |
| path     | string  | The path for revoking permissions from a user group.       |
| value    | string  | Type of user group permissions. <br> CREATE_USER - Creating new users. <br> CREATE_USER_GROUP - Creating new user groups. <br> CREATE_CONNECTION - Creating new connections. <br> CREATE_CONNECTION_GROUP - Creating new connection groups. <br> CREATE_SHARING_PROFILE - Creating new sharing profiles. <br> ADMINISTER - System administration. |

#### Example of Body
```json
[
    {
        "op": "remove",
        "path": "/systemPermissions",
        "value": "ADMINISTER"
    },
    {
        "op": "remove",
        "path": "/systemPermissions",
        "value": "CREATE_USER"
    },
    {
        "op": "remove",
        "path": "/systemPermissions",
        "value": "CREATE_USER_GROUP"
    },
    {
        "op": "remove",
        "path": "/systemPermissions",
        "value": "CREATE_CONNECTION"
    },
    {
        "op": "remove",
        "path": "/systemPermissions",
        "value": "CREATE_CONNECTION_GROUP"
    },
    {
        "op": "remove",
        "path": "/systemPermissions",
        "value": "CREATE_SHARING_PROFILE"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Revoke Member User from User Group
- Revoking a member user from a user group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/memberUsers

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                         |
| -------- | ------- | ------------------------------------------------------------------- |
| op       | string  | Indicates the user's revocation from a user group.                  |
| path     | string  | The path to revoke a user from a user group.                        |
| value    | string  | The username of the user who should be revoked from the user group. |

#### Example of Body
```json
[
    {
        "op": "remove",
        "path": "/",
        "value": "johnexample"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Revoke Member User Group from User Group
- Revoking a member user group from a user group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/memberUserGroups

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                        |
| -------- | ------- | ------------------------------------------------------------------ |
| op       | string  | Indicates the revocation of a member user group from a user group. |
| path     | string  | The path to revoke a member user group from a user group.          |
| value    | string  | The identifier (name) of the member user group.                    |

#### Example of Body
```json
[
    {
        "op": "remove",
        "path": "/",
        "value": "memberUserGroup-example"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Revoke Parent User Group from User Group
- Revoking a parent user group from a user group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/userGroups

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                        |
| -------- | ------- | ------------------------------------------------------------------ |
| op       | string  | Indicates the revocation of a parent user group from a user group. |
| path     | string  | The path to revoke a parent user group from a user group.          |
| value    | string  | The identifier (name) of the parent user group.                    |

#### Example of Body
```json
[
    {
        "op": "remove",
        "path": "/",
        "value": "parentUserGroup-example"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Revoke User Group from Connection
- Revoking a user group from a connection.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/permissions

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |
 
#### Body
| Name     | Type    | Description                                                                                                                  |
| -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| op       | string  | Indicates the revocation of the user group from a connection.                                                                |
| path     | string  | The path to revoke a user group from a connection and the connection identifier from which the user group should be revoked. |
| value    | string  | Access to the connection.                                                                                                    |

#### Example of Body
```json
[
    {
        "op": "remove",
        "path": "/connectionPermissions/1",
        "value": "READ"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Revoke User Group from Connection Group
- Revoking a user group from a connection group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/permissions

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |
 
#### Body
| Name     | Type    | Description                                                                                                                              |
| -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| op       | string  | Indicates the revocation of the user group from a connection group.                                                                      |
| path     | string  | The path to revoke a user group from a connection group and the connection group identifier from which the user group should be revoked. |
| value    | string  | Access to the connection group.                                                                                                          |

#### Example of Body
```json
[
    {
        "op": "remove",
        "path": "/connectionGroupPermissions/1",
        "value": "READ"
    }
]
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## List User Groups
- List of all user groups.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/userGroups

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
| Name          | Type        | Description                                             |
| --------------| ----------- | ------------------------------------------------------- |
| identifier    | string      | The identifier (name) of the user group.                |
| attributes    | object      | Contains detailed user groups information and settings. |
| disabled      | boolean     | Disabling a user group.                                 |

#### Example of Body
```json
{
    "Admins": {
        "identifier": "userGroup-example",
        "attributes": {
            "disabled": null
        }
    }
}
```

## Details of User Group
- List of details and settings about a specific user group.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

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
| Name          | Type        | Description                                             |
| --------------| ----------- | ------------------------------------------------------- |
| identifier    | string      | The identifier (name) of the user group.                |
| attributes    | object      | Contains detailed user groups information and settings. |
| disabled      | boolean     | Disabling a user group.                                 |

#### Example of Body
```json
{
    "identifier": "userGroup-example",
    "attributes": {
        "disabled": null
    }
}
```

## Details of User Group Permissions 
- List of details of user group permissions.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/userGroups/{userGroupIdentifier}/permissions

#### Path Parameters
| Name                           | Type    | Description                               |
| ------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)          | string  | The data source used by Apache Guacamole. |
| userGroupIdentifier (Required) | string  | The identifier (name) of the user group.  |

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
| Name                         | Type        | Description                                                                     |
| ---------------------------- | ----------- | ------------------------------------------------------------------------------- |
| connectionPermissions        | object      | Contains the types of user group permissions for the connections. <br> READ - Accessing to the connections. <br> UPDATE - Editing connections. <br> DELETE - Deleting connections. <br> ADMINISTER - Connections administration. |
| connectionGroupPermissions   | object      | Contains the types of user group permissions for the connection groups. <br> READ - Accessing to the connection groups. <br> UPDATE - Editing connection groups. <br> DELETE - Deleting connection groups. <br> ADMINISTER - Connection groups administration. |
| sharingProfilePermissions    | object      | Contains the types of user group permissions for the sharing profiles. <br> READ - Accessing to the sharing profiles. <br> UPDATE - Editing sharing profiles. <br> DELETE - Deleting sharing profiles. <br> ADMINISTER - Sharing profiles administration. |
| activeConnectionPermissions  | object      | Contains the types of user group permissions for the active connections. <br> READ - Accessing to the active connections. <br> DELETE - Deleting active connections. |
| userPermissions              | object      | Contains the types of user group permissions for the users. <br> READ - Accessing to the user accounts. <br> UPDATE - Editing user accounts. <br> DELETE - Deleting user accounts. <br> ADMINISTER - User accounts administration. |
| userGroupPermissions         | object      | Contains the types of permissions a user group has to other user groups. <br> READ - Accessing to the user groups. <br> UPDATE - Editing user groups. <br> DELETE - Deleting user groups. <br> ADMINISTER - User groups administration. |
| systemPermissions            | array       | Contains the system permissions of the user group. <br> CREATE_USER - Creating new users. <br> CREATE_USER_GROUP - Creating new user groups. <br> CREATE_CONNECTION - Creating new connections. <br> CREATE_CONNECTION_GROUP - Creating new connection groups. <br> CREATE_SHARING_PROFILE - Creating new sharing profiles. <br> ADMINISTER - System administration. |                                          |

#### Example of Body
```json
{
    "connectionPermissions": {
        "1": [
            "READ"
        ]
    },
    "connectionGroupPermissions": {
        "1": [
            "READ"
        ]
    },
    "sharingProfilePermissions": {},
    "activeConnectionPermissions": {},
    "userPermissions": {},
    "userGroupPermissions": {},
    "systemPermissions": [
        "CREATE_USER",
        "CREATE_USER_GROUP",
        "CREATE_CONNECTION",
        "CREATE_CONNECTION_GROUP",
        "CREATE_SHARING_PROFILE",
        "ADMINISTER"
    ]
}
```