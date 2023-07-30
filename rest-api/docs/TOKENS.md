# Tokens

# Table of Contents
- [Generate Token](#generate-token)
- [Delete Token](#delete-token)

## Generate Token
- Generating an access token. The token used to access Apache Guacamole via the REST API.

### Request

#### Method
- POST

#### Endpoint
- /api/tokens

#### Path Parameters
- \-

#### Query Parameters
- \-

#### Headers
| Name         | Type                              |
| ------------ | --------------------------------- | 
| Content-Type | application/x-www-form-urlencoded |

#### Body
- x-www-form-urlencoded

- | Key         | Value       |
  | ----------- | ----------- |
  | username    | guacadmin   |
  | password    | guacadmin   |

#### Example of Body
- \-

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name                 | Type        | Description                                             |
| -------------------- | ----------- | ------------------------------------------------------- |
| authToken            | string      | Token used to access Apache Guacamole via the REST API. |
| username             | string      | User's name for whom the access token is generated.     |
| dataSource           | string      | Primary data source. It used for storing all data.      |
| availableDataSources | array       | Additional available data sources.                      |

#### Example of Body
```json
{
    "authToken": "6FCF9799FC771913B6A29CC0839848CB6FEEB906C333E285EBE221B240DD1222",
    "username": "guacadmin",
    "dataSource": "mysql",
    "availableDataSources": [
        "mysql",
        "mysql-shared"
    ]
}
```
## Delete Token
- Deleting an access token.

### Request

#### Method
- DELETE

#### Endpoint
- /api/tokens/{token}

#### Path Parameters
| Name                 | Type        | Description                                                            |
| -------------------- | ----------- | ---------------------------------------------------------------------- |
| token (Required)     | string      | authToken. The token used to access Apache Guacamole via the REST API. |

#### Query Parameters
- \-

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