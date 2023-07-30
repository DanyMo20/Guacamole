# Users

# Table of Contents
- [Create User](#create-user)
- [Update User](#update-user)
- [Change User Password](#change-user-password)
- [Delete User](#delete-user)
- [Assign Permissions to User](#assign-permissions-to-user)
- [Assign User to User Group](#assign-user-to-user-group)
- [Assign User to Connection](#assign-user-to-connection)
- [Assign User to Connection Group](#assign-user-to-connection-group)
- [Revoke Permissions from User](#revoke-permissions-from-user)
- [Revoke User from User Group](#revoke-user-from-user-group)
- [Revoke User from Connection](#revoke-user-from-connection)
- [Revoke User from Connection Group](#revoke-user-from-connection-group)
- [List Users](#list-users)
- [List History of Users](#list-history-of-users)
- [List of User Groups to Which the User Is Assigned](#list-of-user-groups-to-which-the-user-is-assigned)
- [Details of User](#details-of-user)
- [Details of Self](#details-of-self)
- [Details of User Permissions](#details-of-user-permissions)
- [Details of User Effective Permissions](#details-of-user-effective-permissions)
- [Details of User History](#details-of-user-history)

## Create User
- Creating a Guacamole user.

### Request

#### Method
- POST

#### Endpoint
- /api/session/data/{dataSource}/users

#### Path Parameters
| Name                  | Type    | Description                               |
| --------------------- | ------- | ----------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                      | Type    | Description                                                                                       |
| ------------------------- | ------- | ------------------------------------------------------------------------------------------------- |
| username                  | string  | User's username for accessing Apache Guacamole.                                                   |
| password                  | string  | User's password used for authentication.                                                          |
| attributes                | object  | Contains detailed user information and settings.                                                  |
| guac-full-name            | string  | User's full name.                                                                                 |
| guac-email-address        | string  | User's email address.                                                                             |
| guac-organization         | string  | User's organization.                                                                              |
| guac-organizational-role  | string  | User's organizational role.                                                                       |
| disabled                  | boolean | Disabling login. The user cannot log in.                                                          |
| expired                   | boolean | Password expiration. The user needs to change the password after the first login.                 |
| access-window-start       | string  | Allowing access after a certain period of time. The account can be accessed after a certain time. |
| access-window-end         | string  | Disabling access after a certain time. The account cannot be accessed after a certain time.       |
| valid-from                | string  | The account is valid from a certain date.                                                         |
| valid-until               | string  | The account is valid until a certain date.                                                        |
| timezone                  | string  | User's time zone.                                                                                 |

#### Example of Body
```json
{
    "username": "johnexample",                           
    "password": "1234",                   
    "attributes": {
        "guac-full-name": "John Example",               
        "guac-email-address": "johnexample@email.com",           
        "guac-organization": "Example",            
        "guac-organizational-role": "Tester",     
        "disabled": "false",                     
        "expired": "true",                      
        "access-window-start": "12:22:00",          
        "access-window-end": "15:55:00",            
        "valid-from": "2023-05-25",                   
        "valid-until": "2026-06-30",                  
        "timezone": "Europe/Prague"                 
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
    "username": "johnexample",
    "password": "1234",
    "attributes": {
        "guac-email-address": "johnexample@email.com",
        "guac-organizational-role": "Tester",
        "guac-full-name": "John Example",
        "expired": "true",
        "timezone": "Europe/Prague",
        "access-window-start": "12:22:00",
        "guac-organization": "Example",
        "access-window-end": "15:55:00",
        "disabled": "false",
        "valid-until": "2026-06-30",
        "valid-from": "2023-05-25"
    }
}
```

## Update User
- Updating a user except the password.

### Request

#### Method
- PUT

#### Endpoint
- /api/session/data/{dataSource}/users/{username}

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                      | Type    | Description                                                                                       |
| ------------------------- | ------- | ------------------------------------------------------------------------------------------------- |
| username                  | string  | User's username for accessing Apache Guacamole.                                                   |
| attributes                | object  | Contains detailed user information and settings.                                                  |
| guac-full-name            | string  | User's full name.                                                                                 |
| guac-email-address        | string  | User's email address.                                                                             |
| guac-organization         | string  | User's organization.                                                                              |
| guac-organizational-role  | string  | User's organizational role.                                                                       |
| disabled                  | boolean | Disabling login. The user cannot log in.                                                          |
| expired                   | boolean | Password expiration. The user needs to change the password after the first login.                 |
| access-window-start       | string  | Allowing access after a certain period of time. The account can be accessed after a certain time. |
| access-window-end         | string  | Disabling access after a certain time. The account cannot be accessed after a certain time.       |
| valid-from                | string  | The account is valid from a certain date.                                                         |
| valid-until               | string  | The account is valid until a certain date.                                                        |
| timezone                  | string  | User's time zone.                                                                                 |

#### Example of Body
```json
{
    "username": "johnexample",                                             
    "attributes": {
        "guac-full-name": "John Example",               
        "guac-email-address": "johnexample@email.com",           
        "guac-organization": "Example",            
        "guac-organizational-role": "Developer",     
        "disabled": "false",                     
        "expired": "true",                      
        "access-window-start": "12:22:00",          
        "access-window-end": "15:55:00",            
        "valid-from": "2023-05-25",                   
        "valid-until": "2026-06-30",                  
        "timezone": "Europe/Prague"                 
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

## Change User Password
- Changing the user password.

### Request

#### Method
- PUT

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/password

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name         | Type        | Description        |
| ------------ | ----------- | ------------------ |
| oldPassword  | string      | Old user password. |
| newPassword  | string      | New user password. |

#### Example of Body
```json
{
    "oldPassword": "1234",
    "newPassword": "abcd"
}
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Delete User
- Deleting a user.

### Request

#### Method
- DELETE

#### Endpoint
- /api/session/data/{dataSource}/users/{username}

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

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

## Assign Permissions to User
- Assigning permissions to a user.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/permissions

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                        |
| -------- | ------- | -------------------------------------------------- |
| op       | string  | Indicates the assignment of permissions to a user. |
| path     | string  | The path for assigning permissions to a user.      |
| value    | string  | Type of user permissions. <br> CREATE_USER - Creating new users. <br> CREATE_USER_GROUP - Creating new user groups. <br> CREATE_CONNECTION - Creating new connections. <br> CREATE_CONNECTION_GROUP - Creating new connection groups. <br> CREATE_SHARING_PROFILE - Creating new sharing profiles. <br> ADMINISTER - System administration. |

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
    },
    {
        "op": "add",
        "path": "/userPermissions/johnexample",
        "value": "UPDATE"
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

## Assign User to User Group
- Assigning a user to a user group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/userGroups

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

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
| -------- | ------  | ---------------------------------------------------------------- |
| op       | string  | Indicates the user's assignment to a user group.                 |
| path     | string  | The path to assign a user to a user group.                       |
| value    | string  | The name of the user group to which the user should be assigned. |                         

#### Example of Body
```json
[
    {
        "op": "add",
        "path": "/",
        "value": "userGroup-example"
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

## Assign User to Connection
- Assigning a user to a connection.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/permissions

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                                                                   |
| -------- | ------- | ------------------------------------------------------------------------------------------------------------- |
| op       | string  | Indicates the user's assignment to a connection.                                                              |
| path     | string  | The path to assign a user to a connection and the connection identifier to which the user should be assigned. |
| value    | string  | Access to the connection.                                                                                     | 

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

## Assign User to Connection Group
- Assigning a user to a connection group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/permissions

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type        | Description                                                                                                               |
| -------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- |
| op       | string      | Indicates the user's assignment to a connection group.                                                                    |
| path     | string      | The path to assign a user to a connection group and the connection group identifier to which the user should be assigned. |
| value    | string      | Access to the connection group.                                                                                           | 

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

## Revoke Permissions from User
- Revoking permissions from a user.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/permissions

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                          |
| -------- | ------- | ---------------------------------------------------- |
| op       | string  | Indicates the revocation of permissions from a user. |
| path     | string  | The path for revoking permissions from a user.       |
| value    | string  | Type of user permissions. <br> CREATE_USER - Creating new users. <br> CREATE_USER_GROUP - Creating new user groups. <br> CREATE_CONNECTION - Creating new connections. <br> CREATE_CONNECTION_GROUP - Creating new connection groups. <br> CREATE_SHARING_PROFILE - Creating new sharing profiles. <br> ADMINISTER - System administration. |

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
    },
    {
        "op": "remove",
        "path": "/userPermissions/johnexample",
        "value": "UPDATE"
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

## Revoke User from User Group
- Revoking a user from a user group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/userGroups

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type        | Description                                                       |
| -------- | ----------- | ----------------------------------------------------------------- |
| op       | string      | Indicates the revocation of a user from a user group.             |
| path     | string      | The path to revoke a user from a user group.                      |
| value    | string      | The name of the user group from which the user should be revoked. | 

#### Example of Body
```json
[
    {
        "op": "remove",
        "path": "/",
        "value": "userGroup-example"
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

## Revoke User from Connection
- Revoking a user from a connection.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/permissions

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                                                                      |
| -------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
| op       | string  | Indicates the user's revocation from a connection.                                                               |
| path     | string  | The path to revoke a user from a connection and the connection identifier from which the user should be revoked. |
| value    | string  | Access to the connection.                                                                                        |

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

## Revoke User from Connection Group
- Revoking a user from a connection group.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/permissions

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type        | Description                                                                                                                  |
| -------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------- |
| op       | string      | Indicates the user's revocation from a connection group.                                                                     |
| path     | string      | The path to revoke a user from a connection group and the connection group identifier from which the user should be revoked. |
| value    | string      | Access to the connection group.                                                                                              |

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

## List Users
- List of users. List of all users including their details and settings.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/users

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
| Name                      | Type    | Description                                                                                       |
| ------------------------- | ------- | ------------------------------------------------------------------------------------------------- |
| username                  | string  | User's username for accessing Apache Guacamole.                                                   |
| attributes                | object  | Contains detailed user information and settings.                                                  |
| guac-full-name            | string  | User's full name.                                                                                 |
| guac-email-address        | string  | User's email address.                                                                             |
| guac-organization         | string  | User's organization.                                                                              |
| guac-organizational-role  | string  | User's organizational role.                                                                       |
| disabled                  | boolean | Disabling login. The user cannot log in.                                                          |
| expired                   | boolean | Password expiration. The user needs to change the password after the first login.                 |
| access-window-start       | string  | Allowing access after a certain period of time. The account can be accessed after a certain time. |
| access-window-end         | string  | Disabling access after a certain time. The account cannot be accessed after a certain time.       |
| valid-from                | string  | The account is valid from a certain date.                                                         |
| valid-until               | string  | The account is valid until a certain date.                                                        |
| timezone                  | string  | User's time zone.                                                                                 |
| lastActive                | integer | Date and time that this user was last logged in, or null if this user has never logged in.        |

#### Example of Body
```json
{
    "johnexample": {
        "username": "johnexample",
        "attributes": {
            "guac-email-address": "johnexample@email.com",
            "guac-organizational-role": "Developer",
            "guac-full-name": "John Example",
            "expired": "true",
            "timezone": "Europe/Prague",
            "access-window-start": "12:22:00",
            "guac-organization": "Example",
            "access-window-end": "15:55:00",
            "disabled": null,
            "valid-until": "2026-06-30",
            "valid-from": "2023-05-25"
        }
    },
    "guacadmin": {
        "username": "guacadmin",
        "attributes": {
            "guac-email-address": null,
            "guac-organizational-role": null,
            "guac-full-name": null,
            "expired": null,
            "timezone": null,
            "access-window-start": null,
            "guac-organization": null,
            "access-window-end": null,
            "disabled": null,
            "valid-until": null,
            "valid-from": null
        },
        "lastActive": 1688808425000
    }
}
```

## List History of Users
- List of history of users.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/history/users

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |

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
| Name        | Type    | Description                                                                                 |
| ----------- | --------| ------------------------------------------------------------------------------------------- |
| startDate   | integer | Date and time the activity began.                                                           |
| endDate     | integer | Date and time the activity ended, or null if the activity is still in progress.             |
| remoteHost  | string  | Hostname or IP address of the remote host who performed the activity.                       | 
| username    | string  | User who performed the activity.                                                            |
| active      | boolean | Connection status (if the connection is still in progres).                                  |
| identifier  | integer | Unique identifier assigned to this record.                                                  |
| uuid        | string  | Unique identifier assigned to this record used for the history record.                      |
| attributes  | object  | All attributes associated with this record.                                                 |
| logs        | object  | All logs related to this record.                                                            |

#### Example of Body
```json
[
    {
        "startDate": 1686504089000,
        "endDate": null,
        "remoteHost": "192.168.56.1",
        "username": "guacadmin",
        "active": false,
        "identifier": "1",
        "uuid": "d16a2f32-6722-341b-8cfd-dbd7b9061b74",
        "attributes": {},
        "logs": {}
    }
]
```

## List of User Groups to Which the User Is Assigned
- List of user groups to which the user is assigned.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/userGroups

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

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
| Name       | Type    | Description                                   |
| ---------- | ------- | --------------------------------------------- |
| userGroup  | string  | The user group to which the user is assigned. |

#### Example of Body
```json
[
    "userGroup-example"
]
```

## Details of User
- List of details and settings about a specific user.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/users/{username}

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

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
| Name                      | Type    | Description                                                                                       |
| ------------------------- | ------- | ------------------------------------------------------------------------------------------------- |
| username                  | string  | User's username for accessing Apache Guacamole.                                                   |
| attributes                | object  | Contains detailed user information and settings.                                                  |
| guac-full-name            | string  | User's full name.                                                                                 |
| guac-email-address        | string  | User's email address.                                                                             |
| guac-organization         | string  | User's organization.                                                                              |
| guac-organizational-role  | string  | User's organizational role.                                                                       |
| disabled                  | boolean | Disabling login. The user cannot log in.                                                          |
| expired                   | boolean | Password expiration. The user needs to change the password after the first login.                 |
| access-window-start       | string  | Allowing access after a certain period of time. The account can be accessed after a certain time. |
| access-window-end         | string  | Disabling access after a certain time. The account cannot be accessed after a certain time.       |
| valid-from                | string  | The account is valid from a certain date.                                                         |
| valid-until               | string  | The account is valid until a certain date.                                                        |
| timezone                  | string  | User's time zone.                                                                                 |
| lastActive                | integer | Date and time that this user was last logged in, or null if this user has never logged in.        |

#### Example of Body
```json
{
    "username": "johnexample",
    "attributes": {
        "guac-email-address": "johnexample@email.com",
        "guac-organizational-role": "Developer",
        "guac-full-name": "John Example",
        "expired": "true",
        "timezone": "Europe/Prague",
        "access-window-start": "12:22:00",
        "guac-organization": "Example",
        "access-window-end": "15:55:00",
        "disabled": null,
        "valid-until": "2026-06-30",
        "valid-from": "2023-05-25"
    },
    "lastActive": 1688808425000
}
```

## Details of Self
- List of details about self.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/self

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |

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
| Name                      | Type    | Description                                                                                |
| ------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| username                  | string  | User's username for accessing Apache Guacamole.                                            |
| attributes                | object  | Contains detailed user information and settings.                                           |
| guac-full-name            | string  | User's full name.                                                                          |
| guac-email-address        | string  | User's email address.                                                                      |
| guac-organization         | string  | User's organization.                                                                       |
| guac-organizational-role  | string  | User's organizational role.                                                                |
| lastActive                | integer | Date and time that this user was last logged in, or null if this user has never logged in. |

#### Example of Body
```json
{
    "username": "guacadmin",
    "attributes": {
        "guac-email-address": null,
        "guac-organizational-role": null,
        "guac-full-name": null,
        "guac-organization": null
    },
    "lastActive": 1688731576000
}
```

## Details of User Permissions 
- List of details of user permissions.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/permissions

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

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
| connectionPermissions        | object      | Contains the types of user permissions for the connections. <br> READ - Accessing to the connections. <br> UPDATE - Editing connections. <br> DELETE - Deleting connections. <br> ADMINISTER - Connections administration. |
| connectionGroupPermissions   | object      | Contains the types of user permissions for the connection groups. <br> READ - Accessing to the connection groups. <br> UPDATE - Editing connection groups. <br> DELETE - Deleting connection groups. <br> ADMINISTER - Connection groups administration. |
| sharingProfilePermissions    | object      | Contains the types of user permissions for the sharing profiles. <br> READ - Accessing to the sharing profiles. <br> UPDATE - Editing sharing profiles. <br> DELETE - Deleting sharing profiles. <br> ADMINISTER - Sharing profiles administration. |
| activeConnectionPermissions  | object      | Contains the types of user permissions for the active connections. <br> READ - Accessing to the active connections. <br> DELETE - Deleting active connections. |
| userPermissions              | object      | Contains the types of permissions a user has to other users. <br> READ - Accessing to the user accounts. <br> UPDATE - Editing user accounts. <br> DELETE - Deleting user accounts. <br> ADMINISTER - User accounts administration. |
| userGroupPermissions         | object      | Contains the types of user permissions for the user groups. <br> READ - Accessing to the user groups. <br> UPDATE - Editing user groups. <br> DELETE - Deleting user groups. <br> ADMINISTER - User groups administration. |
| systemPermissions            | array       | Contains the user's system permissions. <br> CREATE_USER - Creating new users. <br> CREATE_USER_GROUP - Creating new user groups. <br> CREATE_CONNECTION - Creating new connections. <br> CREATE_CONNECTION_GROUP - Creating new connection groups. <br> CREATE_SHARING_PROFILE - Creating new sharing profiles. <br> ADMINISTER - System administration. |

#### Example of Body
```json
{
    "connectionPermissions": {
        "1": [
            "READ",
            "UPDATE",
            "DELETE",
            "ADMINISTER"
        ]
    },
    "connectionGroupPermissions": {
        "1": [
            "READ",
            "UPDATE",
            "DELETE",
            "ADMINISTER"
        ]
    },
    "sharingProfilePermissions": {
        "1": [
            "READ",
            "UPDATE",
            "DELETE",
            "ADMINISTER"
        ]
    },
    "activeConnectionPermissions": {
        "3c1501f5-df64-31df-a140-a7b68cb7aad3": [
            "READ",
            "DELETE"
        ]
    },
    "userPermissions": {
        "johnexample": [
            "READ",
            "UPDATE",
            "DELETE",
            "ADMINISTER"
        ],
        "guacadmin": [
            "READ",
            "UPDATE",
            "ADMINISTER"
        ]
    },
    "userGroupPermissions": {
        "userGroup-example": [
            "READ",
            "UPDATE",
            "DELETE",
            "ADMINISTER"
        ]
    },
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

## Details of User Effective Permissions 
- List of details of user effective permissions.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/effectivePermissions

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

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
| connectionPermissions        | object      | Contains the types of user permissions for the connections. <br> READ - Accessing to the connections. <br> UPDATE - Editing connections. <br> DELETE - Deleting connections. <br> ADMINISTER - Connections administration. |
| connectionGroupPermissions   | object      | Contains the types of user permissions for the connection groups. <br> READ - Accessing to the connection groups. <br> UPDATE - Editing connection groups. <br> DELETE - Deleting connection groups. <br> ADMINISTER - Connection groups administration. |
| sharingProfilePermissions    | object      | Contains the types of user permissions for the sharing profiles. <br> READ - Accessing to the sharing profiles. <br> UPDATE - Editing sharing profiles. <br> DELETE - Deleting sharing profiles. <br> ADMINISTER - Sharing profiles administration. |
| activeConnectionPermissions  | object      | Contains the types of user permissions for the active connections. <br> READ - Accessing to the active connections. <br> DELETE - Deleting active connections. |
| userPermissions              | object      | Contains the types of permissions a user has to other users. <br> READ - Accessing to the user accounts. <br> UPDATE - Editing user accounts. <br> DELETE - Deleting user accounts. <br> ADMINISTER - User accounts administration. |
| userGroupPermissions         | object      | Contains the types of user permissions for the user groups. <br> READ - Accessing to the user groups. <br> UPDATE - Editing user groups. <br> DELETE - Deleting user groups. <br> ADMINISTER - User groups administration. |
| systemPermissions            | array       | Contains the user's system permissions. <br> CREATE_USER - Creating new users. <br> CREATE_USER_GROUP - Creating new user groups. <br> CREATE_CONNECTION - Creating new connections. <br> CREATE_CONNECTION_GROUP - Creating new connection groups. <br> CREATE_SHARING_PROFILE - Creating new sharing profiles. <br> ADMINISTER - System administration. |

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
    "userPermissions": {
        "johnexample": [
            "READ",
            "UPDATE"
        ]
    },
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

## Details of User History
- Details of user history.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/users/{username}/history

#### Path Parameters
| Name                  | Type    | Description                                     |
| --------------------- | ------- | ----------------------------------------------- |
| dataSource (Required) | string  | The data source used by Apache Guacamole.       |
| username (Required)   | string  | User's username for accessing Apache Guacamole. |

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
| Name        | Type    | Description                                                                                 |
| ----------- | --------| ------------------------------------------------------------------------------------------- |
| startDate   | integer | Date and time the activity began.                                                           |
| endDate     | integer | Date and time the activity ended, or null if the activity is still in progress.             |
| remoteHost  | string  | Hostname or IP address of the remote host who performed the activity.                       | 
| username    | string  | User who performed the activity.                                                            |
| active      | boolean | Connection status (if the connection is still in progres).                                  |
| identifier  | integer | Unique identifier assigned to this record.                                                  |
| uuid        | string  | Unique identifier assigned to this record used for the history record.                      |
| attributes  | object  | All attributes associated with this record.                                                 |
| logs        | object  | All logs related to this record.                                                            |

#### Example of Body
```json
[
    {
        "startDate": 1686504089000,
        "endDate": 1688808440000,
        "remoteHost": "192.168.56.1",
        "username": "guacadmin",
        "active": false,
        "identifier": "1",
        "uuid": "d16a2f32-6722-341b-8cfd-dbd7b9061b74",
        "attributes": {},
        "logs": {}
    }
]
```

