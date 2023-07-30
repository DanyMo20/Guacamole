# Sharing Profiles

# Table of Contents
- [Create Sharing Profile](#create-sharing-profile)
- [Update Sharing Profile](#update-sharing-profile)
- [Delete Sharing Profile](#delete-sharing-profile)
- [List Sharing Profiles](#list-sharing-profiles)
- [Details of Sharing Profile](#details-of-sharing-profile)

## Create Sharing Profile
- Creating a sharing profile.

### Request

#### Method
- POST

#### Endpoint
- /api/session/data/{dataSource}/sharingProfiles

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
| Name                        | Type     | Description                                                        |
| --------------------------- | -------- | ------------------------------------------------------------------ |
| name                        | string   | Name of the sharing profile.                                       |
| primaryConnectionIdentifier | string   | Identifier of the connection associated with this sharing profile. |
| parameters                  | object   | Parameters of the sharing profile.                                 |
| read-only                   | boolean  | Read-only sharing profile.                                         |
| attributes                  | object   | All attributes associated with this sharing profile.               |

#### Example of Body
```json
{
    "name": "sharingProfile-example",
    "primaryConnectionIdentifier": "1",
    "parameters": {
        "read-only": "true"
    },
    "attributes": {}
}
```

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name                        | Type     | Description                                                        |
| --------------------------- | -------- | ------------------------------------------------------------------ |
| name                        | string   | Name of the sharing profile.                                       |
| identifier                  | integer  | Identifier of the sharing profile.                                 |
| primaryConnectionIdentifier | string   | Identifier of the connection associated with this sharing profile. |
| parameters                  | object   | Parameters of the sharing profile.                                 |
| read-only                   | boolean  | Read-only sharing profile.                                         |
| attributes                  | object   | All attributes associated with this sharing profile.               |

#### Example of Body
```json
{
    "name": "sharingProfile-example",
    "identifier": "1",
    "primaryConnectionIdentifier": "1",
    "parameters": {
        "read-only": "true"
    },
    "attributes": {}
}
```

## Update Sharing Profile
- Updating a sharing profile.

### Request

#### Method
- PUT

#### Endpoint
- /api/session/data/{dataSource}/sharingProfiles/{sharingProfileIdentifier}

#### Path Parameters
| Name                                 | Type    | Description                               |
| ------------------------------------ | ------- | ----------------------------------------- |
| dataSource (Required)                | string  | The data source used by Apache Guacamole. |
| sharingProfileIdentifier (Required)  | integer | The identifier of the sharing profile.    |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                        | Type     | Description                                                        |
| --------------------------- | -------- | ------------------------------------------------------------------ |
| name                        | string   | Name of the sharing profile.                                       |
| primaryConnectionIdentifier | string   | Identifier of the connection associated with this sharing profile. |
| parameters                  | object   | Parameters of the sharing profile.                                 |
| read-only                   | boolean  | Read-only sharing profile.                                         |
| attributes                  | object   | All attributes associated with this sharing profile.               |

#### Example of Body
```json
{
    "name": "sharingProfile-example",
    "primaryConnectionIdentifier": "1",
    "parameters": {
        "read-only": "false"
    },
    "attributes": {}
}
```

### Response

#### Normal Response Code
- 204 No Content

#### Body
- \-

#### Example of Body
- \-

## Delete Sharing Profile
- Deleting a sharing profile.

### Request

#### Method
- DELETE

#### Endpoint
- /api/session/data/{dataSource}/sharingProfiles/{sharingProfileIdentifier}

#### Path Parameters
| Name                                | Type    | Description                               |
| ----------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)               | string  | The data source used by Apache Guacamole. |
| sharingProfileIdentifier (Required) | integer | The identifier of the sharing profile.    |

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

## List Sharing Profiles
- List of all sharing profiles.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/sharingProfiles

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
| Name                        | Type     | Description                                                        |
| --------------------------- | -------- | ------------------------------------------------------------------ |
| name                        | string   | Name of the sharing profile.                                       |
| identifier                  | integer  | Identifier of the sharing profile.                                 |
| primaryConnectionIdentifier | string   | Identifier of the connection associated with this sharing profile. |
| attributes                  | object   | All attributes associated with this sharing profile.               |

#### Example of Body
```json
{
    "1": {
        "name": "sharingProfile-example",
        "identifier": "1",
        "primaryConnectionIdentifier": "1",
        "attributes": {}
    }
}
```

## Details of Sharing Profile
- List of details about a specific sharing profile.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/sharingProfiles/{sharingProfileIdentifier}

#### Path Parameters
| Name                                | Type    | Description                               |
| ----------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)               | string  | The data source used by Apache Guacamole. |
| sharingProfileIdentifier (Required) | integer | The identifier of the sharing profile.    |

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
| Name                        | Type     | Description                                                        |
| --------------------------- | -------- | ------------------------------------------------------------------ |
| name                        | string   | Name of the sharing profile.                                       |
| identifier                  | integer  | Identifier of the sharing profile.                                 |
| primaryConnectionIdentifier | string   | Identifier of the connection associated with this sharing profile. |
| attributes                  | object   | All attributes associated with this sharing profile.               |

#### Example of Body
```json
{
    "name": "sharingProfile-example",
    "identifier": "1",
    "primaryConnectionIdentifier": "1",
    "attributes": {}
}
```
