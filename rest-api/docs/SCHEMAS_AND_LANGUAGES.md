# Schemas and Languages

# Table of Contents
- [List User Attributes](#list-user-attributes)
- [List User Group Attributes](#list-user-group-attributes)
- [List Connection Attributes](#list-connection-attributes)
- [List Connection Group Attributes](#list-connection-group-attributes)
- [List Sharing Profile Attributes](#list-sharing-profile-attributes)
- [List Protocol Attributes](#list-protocol-attributes)
- [List Languages](#list-languages)

## List User Attributes
- List of all user attributes.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/schema/userAttributes

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
| Name                      | Type    | Description                                                                                       |
| ------------------------- | ------- | ------------------------------------------------------------------------------------------------- |
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
[
    {
        "name": "profile",
        "fields": [
            {
                "name": "guac-full-name",
                "type": "TEXT"
            },
            {
                "name": "guac-email-address",
                "type": "EMAIL"
            },
            {
                "name": "guac-organization",
                "type": "TEXT"
            },
            {
                "name": "guac-organizational-role",
                "type": "TEXT"
            }
        ]
    },
    {
        "name": "restrictions",
        "fields": [
            {
                "name": "disabled",
                "type": "BOOLEAN",
                "options": [
                    "true"
                ]
            },
            {
                "name": "expired",
                "type": "BOOLEAN",
                "options": [
                    "true"
                ]
            },
            {
                "name": "access-window-start",
                "type": "TIME"
            },
            {
                "name": "access-window-end",
                "type": "TIME"
            },
            {
                "name": "valid-from",
                "type": "DATE"
            },
            {
                "name": "valid-until",
                "type": "DATE"
            },
            {
                "name": "timezone",
                "type": "TIMEZONE"
            }
        ]
    }
]
```

## List User Group Attributes
- List of all user group attributes.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/schema/userGroupAttributes

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
| Name          | Type     | Description                                             |
| --------------| -------- | ------------------------------------------------------- |
| disabled      | boolean  | Disabling a user group.                                 |

#### Example of Body
```json
[
    {
        "name": "restrictions",
        "fields": [
            {
                "name": "disabled",
                "type": "BOOLEAN",
                "options": [
                    "true"
                ]
            }
        ]
    }
]
```

## List Connection Attributes
- List of all connection attributes.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/schema/connectionAttributes

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
| Name                      | Type     | Description                                                                                                |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
| max-connections           | integer  | Maximum number of concurrent connections.                                                                  |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                                         |
| weight                    | integer  | It used for weighted load balancing algorithms.                                                            |
| failover-only             | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred. |
| guacd-hostname            | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                        |
| guacd-port                | integer  | Port for connecting to guacd. Default: 4822.                                                               |
| guacd-encryption          | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                        |

#### Example of Body
```json
[
    {
        "name": "concurrency",
        "fields": [
            {
                "name": "max-connections",
                "type": "NUMERIC"
            },
            {
                "name": "max-connections-per-user",
                "type": "NUMERIC"
            }
        ]
    },
    {
        "name": "load-balancing",
        "fields": [
            {
                "name": "weight",
                "type": "NUMERIC"
            },
            {
                "name": "failover-only",
                "type": "BOOLEAN",
                "options": [
                    "true"
                ]
            }
        ]
    },
    {
        "name": "guacd",
        "fields": [
            {
                "name": "guacd-hostname",
                "type": "TEXT"
            },
            {
                "name": "guacd-port",
                "type": "NUMERIC"
            },
            {
                "name": "guacd-encryption",
                "type": "ENUM",
                "options": [
                    "",
                    "none",
                    "ssl"
                ]
            }
        ]
    }
]
```

## List Connection Group Attributes
- List of all connection group attributes.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/schema/connectionGroupAttributes

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
| Name                      | Type     | Description                                                                                |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------ |
| max-connections           | integer  | Maximum number of concurrent connections.                                                  |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                         |
| enable-session-affinity   | boolean  | Assigning of the same connection to the users within a balancing group until they log out. |

#### Example of Body
```json
[
    {
        "name": "concurrency",
        "fields": [
            {
                "name": "max-connections",
                "type": "NUMERIC"
            },
            {
                "name": "max-connections-per-user",
                "type": "NUMERIC"
            },
            {
                "name": "enable-session-affinity",
                "type": "BOOLEAN",
                "options": [
                    "true"
                ]
            }
        ]
    }
]
```

## List Sharing Profile Attributes
- List of all sharing profile attributes.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/schema/sharingProfileAttributes

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
| Name                      | Type     | Description                                                                                                |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |

#### Example of Body
```json
[]
```

## List Protocol Attributes
- List of attributes of all protocols.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/schema/protocols

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

#### Body (Kubernetes)
| Name                      | Type     | Description                                                                                                                                            |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| hostname                  | string   | Hostname or IP address of the Kubernetes server Guacamole should connect to. Required.                                                                 |
| port                      | integer  | Port the Kubernetes server is listening on. Default: 8080. Optional.                                                                                   |
| use-ssl                   | boolean  | Using SSL-TLS to connect to the Kubernetes server. Optional.                                                                                           |
| ignore-cert               | boolean  | Ignoring validity of the SSL/TLS certificate used by the Kubernetes server. Optional.                                                                  |
| ca-cert                   | string   | Certificate of the certificate authority that signed the certificate of the Kubernetes server, in PEM format. Optional.                                |
| namespace                 | string   | Name of the Kubernetes namespace of the pod containing the container being attached to. Default: default. Optional.                                    |
| pod                       | string   | Name of the Kubernetes pod containing with the container being attached to. Required.                                                                  |
| container                 | string   | Name of the container to attach to. Optional.                                                                                                          |
| exec-command              | string   | Command to run within the container, with input and output attached to this command’s process. Optional.                                               |
| client-cert               | string   | Certificate to use if performing SSL/TLS client authentication to authenticate with the Kubernetes server, in PEM format. Optional.                    |
| client-key                | string   | Key to use if performing SSL/TLS client authentication to authenticate with the Kubernetes server, in PEM format. Optional.                            |
| color-scheme              | string   | Color scheme to use for the terminal session. Valid options: black-white, gray-black, green-black, white-black. Default: gray-black. Optional.         |
| font-name                 | string   | Name of the font to use. Default: monospace. Optional.                                                                                                 |
| font-size                 | integer  | Size of the font to use, in points. Valid options: 8, 9, 10, 11, 12, 14, 18, 24, 30, 36, 48, 60, 72, 96. Default: 12. Optional.                        |
| scrollback                | integer  | Maximum number of rows to allow within the terminal scrollback buffer. Default: 1000. Optional.                                                        |
| read-only                 | boolean  | Read-only connection. Optional.                                                                                                                        |
| backspace                 | integer  | ASCII code of the backspace key which is sent to the remote system. Valid options: 8, 127. Default: 127. Optional.                                     |
| typescript-path           | string   | Directory for saving typescripts. Required if a typescript needs to be created. Optional.                                                              |
| typescript-name           | string   | Name of the saved typescript. Default: typescript. Optional.                                                                                           |
| create-typescript-path    | boolean  | Automatic creation of the final directory in the path to save the typescript. Optional.                                                                |
| recording-path            | string   | Directory for saving graphic records. Required if a graphical recording needs to be created.                                                           |
| recording-name            | string   | Name of the saved recording. Default: recording. Optional.                                                                                             |
| recording-exclude-output  | boolean  | Excluding a graphical output from the recording. Optional.                                                                                             |
| recording-exclude-mouse   | boolean  | Excluding a visible mouse cursor from the recording. Optional.                                                                                         |
| recording-include-keys    | boolean  | Including key events in the recording. Optional.                                                                                                       |
| create-recording-path     | boolean  | Automatic creation of the final directory in the path to save the recording. Optional.                                                                 |
| read-only sharing profile | boolean  | Read-only sharing profile. Optional.                                                                                                                   |

#### Body (Telnet)
| Name                      | Type     | Description                                                                                                                                            |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| hostname                  | string   | Hostname or IP address of the telnet server Guacamole should connect to. Required.                                                                     |
| port                      | integer  | Port the telnet server is listening on. Default: 23. Optional.                                                                                         |
| username                  | string   | Username to authenticate, if any. Optional.                                                                                                            |
| password                  | string   | Password to authenticate, if any. Optional.                                                                                                            |
| username-regex            | string   | Regular expression to use when waiting for the username prompt. Optional.                                                                              |
| password-regex            | string   | Regular expression to use when waiting for the password prompt. Optional.                                                                              |
| login-success-regex       | string   | Regular expression to use when detecting that the login attempt has succeeded. Optional.                                                               |
| login-failure-regex       | string   | Regular expression to use when detecting that the login attempt has failed. Optional.                                                                  |
| color-scheme              | string   | Color scheme to use for the terminal session. Valid options: black-white, gray-black, green-black, white-black. Default: gray-black. Optional.         |
| font-name                 | string   | Name of the font to use. Default: monospace. Optional.                                                                                                 |
| font-size                 | integer  | Size of the font to use, in points. Valid options: 8, 9, 10, 11, 12, 14, 18, 24, 30, 36, 48, 60, 72, 96. Default: 12. Optional.                        |
| scrollback                | integer  | Maximum number of rows to allow within the terminal scrollback buffer. Default: 1000. Optional.                                                        |
| read-only                 | boolean  | Read-only connection. Optional.                                                                                                                        |
| disable-copy              | boolean  | Disabling copying from a remote desktop. Optional.                                                                                                     |
| disable-paste             | boolean  | Disabling pasting from the browser side to the remote desktop. Optional.                                                                               |
| backspace                 | integer  | ASCII code of the backspace key which is sent to the remote system. Valid options: 8, 127. Default: 127. Optional.                                     |
| terminal-type             | string   | Terminal emulator type string that is passed to the server. Valid options: ansi, linux, vt100, vt220, xterm, xterm-256color. Default: linux. Optional. |
| typescript-path           | string   | Directory for saving typescripts. Required if a typescript needs to be created. Optional.                                                              |
| typescript-name           | string   | Name of the saved typescript. Default: typescript. Optional.                                                                                           |
| create-typescript-path    | boolean  | Automatic creation of the final directory in the path to save the typescript. Optional.                                                                |
| recording-path            | string   | Directory for saving graphic records. Required if a graphical recording needs to be created.                                                           |
| recording-name            | string   | Name of the saved recording. Default: recording. Optional.                                                                                             |
| recording-exclude-output  | boolean  | Excluding a graphical output from the recording. Optional.                                                                                             |
| recording-exclude-mouse   | boolean  | Excluding a visible mouse cursor from the recording. Optional.                                                                                         |
| recording-include-keys    | boolean  | Including key events in the recording. Optional.                                                                                                       |
| create-recording-path     | boolean  | Automatic creation of the final directory in the path to save the recording. Optional.                                                                 |
| wol-send-packet           | boolean  | Sending the Wake-On-LAN packet prior to establishing a connection. Optional.                                                                           |
| wol-mac-addr              | string   | MAC address in the magic WoL packet to attempt to wake the remote system. Required if wol-send-packet is enabled.                                      |
| wol-broadcast-addr        | string   | IPv4 broadcast address or IPv6 multicast address for sending the WoL packet to in order to wake the host. Default: 255.255.255.255. Optional.          |
| wol-udp-port              | integer  | UDP port in the WoL packet. Default: 9. Optional.                                                                                                      |
| wol-wait-time             | integer  | Delay in seconds between sending WoL packet and connecting to the remote host. Default: 0. Optional.                                                   |
| read-only sharing profile | boolean  | Read-only sharing profile. Optional.                                                                                                                   |

#### Body (SSH)
| Name                      | Type     | Description                                                                                                                                            |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| hostname                  | string   | Hostname or IP address of the SSH server Guacamole should connect to. Required.                                                                        |
| port                      | integer  | Port the SSH server is listening on. Default: 22. Optional.                                                                                            |
| host-key                  | string   | Known hosts entry for the SSH server. Optional.                                                                                                        |
| username                  | string   | Username to authenticate, if any. Optional. If not specified, you will be prompted for the username upon connecting.                                   |
| password                  | string   | Password to authenticate, if any. Optional. If not specified, you will be prompted for the password upon connecting.                                   |
| private-key               | string   | Private key for using public key authentication. Optional. If not specified, public key authentication will not be used.                               |
| passphrase                | string   | Passphrase to use to decrypt the private key for use in public key authentication. Required if a private key require a passphrase.                     |
| color-scheme              | string   | Color scheme to use for the terminal session. Valid options: black-white, gray-black, green-black, white-black. Default: gray-black. Optional.         |
| font-name                 | string   | Name of the font to use. Default: monospace. Optional.                                                                                                 |
| font-size                 | integer  | Size of the font to use, in points. Valid options: 8, 9, 10, 11, 12, 14, 18, 24, 30, 36, 48, 60, 72, 96. Default: 12. Optional.                        |
| scrollback                | integer  | Maximum number of rows to allow within the terminal scrollback buffer. Default: 1000. Optional.                                                        |
| read-only                 | boolean  | Read-only connection. Optional.                                                                                                                        |
| disable-copy              | boolean  | Disabling copying from a remote desktop. Optional.                                                                                                     |
| disable-paste             | boolean  | Disabling pasting from the browser side to the remote desktop. Optional.                                                                               |
| command                   | string   | Command to execute over the SSH session, if any. Default: user's default shell. Optional.                                                              |
| locale                    | string   | Specific locale to request for the SSH session. Deafult: SSH server’s default locale. Optional.                                                        |
| timezone                  | string   | Timezone that is sent to the server over the SSH connection, which will change the way local time is displayed on the server. Optional.                |
| server-alive-interval     | integer  | Interval in seconds at which to send keepalive packets to the SSH server. Default: 0. Optional.                                                        |
| backspace                 | integer  | ASCII code of the backspace key which is sent to the remote system. Valid options: 8, 127. Default: 127. Optional.                                     |
| terminal-type             | string   | Terminal emulator type string that is passed to the server. Valid options: ansi, linux, vt100, vt220, xterm, xterm-256color. Default: linux. Optional. |
| typescript-path           | string   | Directory for saving typescripts. Required if a typescript needs to be created. Optional.                                                              |
| typescript-name           | string   | Name of the saved typescript. Default: typescript. Optional.                                                                                           |
| create-typescript-path    | boolean  | Automatic creation of the final directory in the path to save the typescript. Optional.                                                                |
| recording-path            | string   | Directory for saving graphic records. Required if a graphical recording needs to be created.                                                           |
| recording-name            | string   | Name of the saved recording. Default: recording. Optional.                                                                                             |
| recording-exclude-output  | boolean  | Excluding a graphical output from the recording. Optional.                                                                                             |
| recording-exclude-mouse   | boolean  | Excluding a visible mouse cursor from the recording. Optional.                                                                                         |
| recording-include-keys    | boolean  | Including key events in the recording. Optional.                                                                                                       |
| create-recording-path     | boolean  | Automatic creation of the final directory in the path to save the recording. Optional.                                                                 |
| enable-sftp               | boolean  | Enabling file transfer using sftp. Optional.                                                                                                           |
| sftp-root-directory       | string   | Directory to expose to connected users via Guacamole’s Using the file browser. Default: Root directory. Optional.                                      |
| sftp-disable-download     | boolean  | Disabling downloads from the remote system to the client (browser). Optional.                                                                          |
| sftp-disable-upload       | boolean  | Disabling uploads from the client (browser) to the remote system. Optional.                                                                            |
| wol-send-packet           | boolean  | Sending the Wake-On-LAN packet prior to establishing a connection. Optional.                                                                           |
| wol-mac-addr              | string   | MAC address in the magic WoL packet to attempt to wake the remote system. Required if wol-send-packet is enabled.                                      |
| wol-broadcast-addr        | string   | IPv4 broadcast address or IPv6 multicast address for sending the WoL packet to in order to wake the host. Default: 255.255.255.255. Optional.          |
| wol-udp-port              | integer  | UDP port in the WoL packet. Default: 9. Optional.                                                                                                      |
| wol-wait-time             | integer  | Delay in seconds between sending WoL packet and connecting to the remote host. Default: 0. Optional.                                                   |
| read-only sharing profile | boolean  | Read-only sharing profile. Optional.                                                                                                                   |

#### Body (VNC)
| Name                       | Type     | Description                                                                                                                                                |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hostname                   | string   | Hostname or IP address of the VNC server Guacamole should connect to. Required.                                                                            |
| port                       | integer  | Port the VNC server is listening on, usually 5900 or 5900 + display number. Required.                                                                      |
| username                   | string   | Username to use when attempting authentication, if any. Optional.                                                                                          |
| password                   | string   | Password to use when attempting authentication, if any. Optional.                                                                                          |
| read-only                  | boolean  | Read-only connection. Optional.                                                                                                                            |
| swap-red-blue              | boolean  | Swapping red and blue components. Optional.                                                                                                                |
| cursor                     | string   | Type of cursor. Valid options: remote, local. Default: local. Optional.                                                                                    |
| color-depth                | integer  | Color depth of display. Valid options: 8, 16, 24, 32. Default: 8. Optional.                                                                                |
| force-lossless             | boolean  | Lossless compression for graphical updates. Optional.                                                                                                      |
| encodings                  | string   | Space-delimited list of VNC encodings to use. Default: Any supported encoding. Optional.                                                                   |
| clipboard-encoding         | string   | VNC clipboard. Valid options: CP1252, ISO8859-1, UTF-16, UTF-8. Default: ISO8859-1. Optional.                                                              |
| disable-copy               | boolean  | Disabling copying from a remote desktop. Optional.                                                                                                         |
| disable-paste              | boolean  | Disabling pasting from the browser side to the remote desktop. Optional.                                                                                   |
| dest-host                  | string   | Destination host when connecting to a VNC proxy. Necessary if the VNC proxy in use requires the connecting user to specify which VNC server to connect to. |
| dest-port                  | integer  | Destination port when connecting to a VNC proxy. Necessary if the VNC proxy in use requires the connecting user to specify which VNC server to connect to. |
| recording-path             | string   | Directory for saving graphic records. Required if a graphical recording needs to be created.                                                               |
| recording-name             | string   | Name of the saved recording. Default: recording. Optional.                                                                                                 |
| recording-exclude-output   | boolean  | Excluding a graphical output from the recording. Optional.                                                                                                 |
| recording-exclude-mouse    | boolean  | Excluding a visible mouse cursor from the recording. Optional.                                                                                             |
| recording-include-keys     | boolean  | Including key events in the recording. Optional.                                                                                                           |
| create-recording-path      | boolean  | Automatic creation of the final directory in the path to save the recording. Optional.                                                                     |
| enable-sftp                | boolean  | Enabling file transfer using sftp. Optional.                                                                                                               |
| sftp-hostname              | string   | Hostname or IP address of the server hosting SFTP. Optional.                                                                                               |
| sftp-port                  | integer  | Port the SSH server providing SFTP is listening on. Default: 22. Optional.                                                                                 |
| sftp-host-key              | string   | Known hosts entry for the SFTP server. Optional.                                                                                                           |
| sftp-username              | string   | Username to authenticate as when connecting to the specified SSH server for SFTP. Optional if a username is specified for the remote desktop connection.   |
| sftp-password              | string   | Password to use when authenticating with the specified SSH server for SFTP.                                                                                |
| sftp-private-key           | string   | Private key for using public key authentication. If not specified, public key authentication will not be used.                                             |
| sftp-passphrase            | string   | Passphrase to use to decrypt the private key for use in public key authentication. Required if a private key require a passphrase.                         |
| sftp-root-directory        | string   | Directory to expose to connected users via Guacamole’s Using the file browser. Default: Root directory. Optional.                                          |
| sftp-directory             | string   | Directory to upload files to if they are simply dragged and dropped. Default: Home directory of logged user. Optional.                                     |
| sftp-server-alive-interval | integer  | Interval in seconds at which to send keepalive packets to the SSH server for the SFTP. Default: 0. Optional.                                               |
| sftp-disable-download      | boolean  | Disabling downloads from the remote system to the client (browser). Optional.                                                                              |
| sftp-disable-upload        | boolean  | Disabling uploads from the client (browser) to the remote system. Optional.                                                                                |
| enable-audio               | boolean  | Enabling audio support (PulseAudio). Optional.                                                                                                             |
| audio-servername           | string   | Hostname or IP address of the PulseAudio server to connect to. Optional.                                                                                   |
| wol-send-packet            | boolean  | Sending the Wake-On-LAN packet prior to establishing a connection. Optional.                                                                               |
| wol-mac-addr               | string   | MAC address in the magic WoL packet to attempt to wake the remote system. Required if wol-send-packet is enabled.                                          |
| wol-broadcast-addr         | string   | IPv4 broadcast address or IPv6 multicast address for sending the WoL packet to in order to wake the host. Default: 255.255.255.255. Optional.              |
| wol-udp-port               | integer  | UDP port in the WoL packet. Default: 9. Optional.                                                                                                          |
| wol-wait-time              | integer  | Delay in seconds between sending WoL packet and connecting to the remote host. Default: 0. Optional.                                                       |
| read-only sharing profile  | boolean  | Read-only sharing profile. Optional.                                                                                                                       |

#### Body (RDP)
| Name                       | Type     | Description                                                                                                                                                |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hostname                   | string   | Hostname of the RDP server Guacamole should connect to. Required.                                                                                          |
| port                       | integer  | Port the RDP server is listening on. Default: 3389 for RDP, 2179 for VMConnect, depending on the security mode selected. Optional.                         |
| username                   | string   | Username to authenticate, if any. Optional.                                                                                                                |
| password                   | string   | Password to authenticate, if any. Optional.                                                                                                                |
| domain                     | string   | Domain to authenticate, if any. Optional.                                                                                                                  |
| security                   | string   | Security mode to use for the RDP connection. Valid options: any, nla, rdp, tls, vmconnect. Default: any. Optional.                                         |
| disable-auth               | boolean  | Disabling an authentication. Authentication must be enabled by definition if NLA is used. Optional.                                                        |
| ignore-cert                | boolean  | Ignoring certificate returned by the server. Optional.                                                                                                     |
| gateway-hostname           | string   | Hostname or IP address of the remote desktop gateway that should be used as an intermediary for the remote desktop connection. Optional.                   |
| gateway-port               | integer  | Port of the remote desktop gateway that should be used as an intermediary for the remote desktop connection. Default: 443. Optional.                       |
| gateway-username           | string   | Username of the user authenticating with the remote desktop gateway, if a gateway is being used.                                                           |
| gateway-password           | string   | Password to provide when authenticating with the remote desktop gateway, if a gateway is being used.                                                       |
| gateway-domain             | string   | Domain of the user authenticating with the remote desktop gateway, if a gateway is being used.                                                             |
| initial-program            | string   | Path to the program to run immediately upon connecting. Optional.                                                                                          |
| client-name                | string   | Name of the client. Default: hostname. Optional.                                                                                                           |
| server-layout              | string   | Server-side keyboard layout. More information in the Apache Guacamole documentation. Optional.                                                             |
| timezone                   | string   | Timezone that is sent to the server over the RDP connection, which will change the way local time is displayed on the server. Optional.                    |
| enable-touch               | boolean  | Enabling multi-touch events. Optional.                                                                                                                     |
| console                    | boolean  | Connecting to the console (admin) session of the RDP server. Optional.                                                                                     |
| width                      | integer  | Width of the display to request, in pixels. Default: Width of the connecting client display. Optional.                                                     |
| height                     | integer  | Height of the display to request, in pixels. Default: Height of the connecting client display. Optional.                                                   |
| dpi                        | integer  | Desired effective resolution of the client display, in DPI. Optional.                                                                                      |
| color-depth                | integer  | Color depth of display. Valid options: 8, 16, 24, 32. Default: 8. Optional.                                                                                |
| force-lossless             | boolean  | Lossless compression for graphical updates. Optional.                                                                                                      |
| resize-method              | string   | Method to update the RDP server when the width or height of the client display change. Valid options: display-update, reconnect. Default: No action. Optional.  |
| read-only                  | boolean  | Read-only connection. Optional.                                                                                                                            |
| normalize-clipboard        | string   | Type of line ending normalization to apply to text within the clipboard, if any. Valid options: preserve, windows, unix. Default: Not applied. Optional.   |
| disable-copy               | boolean  | Disabling copying from a remote desktop. Optional.                                                                                                         |
| disable-paste              | boolean  | Disabling pasting from the browser side to the remote desktop. Optional.                                                                                   |
| console-audio              | boolean  | Enabling audio in the console (admin) session of the RDP server Optional.                                                                                  |
| disable-audio              | boolean  | Disabling sound for a better bandwidth usage. Optional.                                                                                                    |
| enable-audio-input         | boolean  | Enabling audio input support (microphone). Optional.                                                                                                       |
| enable-printing            | boolean  | Enabling printing to a virtual printer. Printing support requires GhostScript. Optional.                                                                   |
| printer-name               | string   | Name of the redirected printer device that the user will see in, for example, the Devices and Printers control panel. Optional.                            |
| enable-drive               | boolean  | Enabling file transfer using rdp. Optional.                                                                                                                |
| drive-name                 | string   | Name of the filesystem for file transfer that users will see in their Computer/My Computer. Optional.                                                      |
| disable-download           | boolean  | Disabling downloads from the remote system to the client (browser). Optional.                                                                              |
| disable-upload             | boolean  | Disabling uploads from the client (browser) to the remote system. Optional.                                                                                |
| drive-path                 | string   | Directory on the Guacamole server in which transferred files should be stored. Optional.                                                                   |
| create-drive-path          | boolean  | Automatic creation of the final directory specified by the drive-path parameter. Optional.                                                                 |
| static-channels            | boolean  | Comma-separated list of static channel names to open and expose as pipes. Optional.                                                                        |
| enable-wallpaper           | boolean  | Enabling rendering of the desktop wallpaper. Optional.                                                                                                     |
| enable-theming             | boolean  | Enabling using of theming of windows and controls. Optional.                                                                                               |
| enable-font-smoothing      | boolean  | Enabling rendering with smooth edges. Optional.                                                                                                            |
| enable-full-window-drag    | boolean  | Enabling contents of windows to be displayed when windows are moved. Optional.                                                                             |
| enable-desktop-composition | boolean  | Enabling graphical effects such as transparent windows and shadows. Optional.                                                                              |
| enable-menu-animations     | boolean  | Enabling menu open and close animations. Optional.                                                                                                         |
| disable-bitmap-caching     | boolean  | Disabling RDP’s built-in bitmap caching functionality. Optional.                                                                                           |
| disable-offscreen-caching  | boolean  | Disabling caching of regions of the screen that are currently not visible in the client. Optional.                                                         |
| disable-glyph-caching      | boolean  | Disabling glyph caching in the RDP session. Glyph caching is currently universally disabled.                                                               |
| disable-gfx                | boolean  | Disabling graphics pipeline extension. Optional.                                                                                                           |
| remote-app                 | string   | RemoteApp to be start on the remote desktop. Optional.                                                                                                     |
| remote-app-dir             | string   | Working directory, if any, for the remote application. Optional.                                                                                           |
| remote-app-args            | string   | Command-line arguments, if any, for the remote application. Optional.                                                                                      |
| preconnection-id           | integer  | Numeric ID of the RDP source. Optional.                                                                                                                    |
| preconnection-blob         | string   | Arbitrary string which identifies the RDP source. Optional.                                                                                                |
| load-balance-info          | string   | Load balancing information or cookie which should be provided to the connection broker. If no connection broker is being used, this should be left blank.  |
| recording-path             | string   | Directory for saving graphic records. Required if a graphical recording needs to be created.                                                               |
| recording-name             | string   | Name of the saved recording. Default: recording. Optional.                                                                                                 |
| recording-exclude-output   | boolean  | Excluding a graphical output from the recording. Optional.                                                                                                 |
| recording-exclude-mouse    | boolean  | Excluding a visible mouse cursor from the recording. Optional.                                                                                             |
| recording-exclude-touch    | boolean  | Excluding a visible mouse cursor from the recording. Optional.                                                                                             |
| recording-include-keys     | boolean  | Including key events in the recording. Optional.                                                                                                           |
| create-recording-path      | boolean  | Automatic creation of the final directory in the path to save the recording. Optional.                                                                     |
| enable-sftp                | boolean  | Enabling file transfer using sftp. Optional.                                                                                                               |
| sftp-hostname              | string   | Hostname or IP address of the server hosting SFTP. Optional.                                                                                               |
| sftp-port                  | integer  | Port the SSH server providing SFTP is listening on. Default: 22. Optional.                                                                                 |
| sftp-host-key              | string   | Known hosts entry for the SFTP server. Optional.                                                                                                           |
| sftp-username              | string   | Username to authenticate as when connecting to the specified SSH server for SFTP. Optional if a username is specified for the remote desktop connection.   |
| sftp-password              | string   | Password to use when authenticating with the specified SSH server for SFTP.                                                                                |
| sftp-private-key           | string   | Private key for using public key authentication. If not specified, public key authentication will not be used.                                             |
| sftp-passphrase            | string   | Passphrase to use to decrypt the private key for use in public key authentication. Required if a private key require a passphrase.                         |
| sftp-root-directory        | string   | Directory to expose to connected users via Guacamole’s Using the file browser. Default: Root directory. Optional.                                          |
| sftp-directory             | string   | Directory to upload files to if they are simply dragged and dropped. Default: Home directory of logged user. Optional.                                     |
| sftp-server-alive-interval | integer  | Interval in seconds at which to send keepalive packets to the SSH server for the SFTP. Default: 0. Optional.                                               |
| sftp-disable-download      | boolean  | Disabling downloads from the remote system to the client (browser). Optional.                                                                              |
| sftp-disable-upload        | boolean  | Disabling uploads from the client (browser) to the remote system. Optional.                                                                                |
| wol-send-packet            | boolean  | Sending the Wake-On-LAN packet prior to establishing a connection. Optional.                                                                               |
| wol-mac-addr               | string   | MAC address in the magic WoL packet to attempt to wake the remote system. Required if wol-send-packet is enabled.                                          |
| wol-broadcast-addr         | string   | IPv4 broadcast address or IPv6 multicast address for sending the WoL packet to in order to wake the host. Default: 255.255.255.255. Optional.              |
| wol-udp-port               | integer  | UDP port in the WoL packet. Default: 9. Optional.                                                                                                          |
| wol-wait-time              | integer  | Delay in seconds between sending WoL packet and connecting to the remote host. Default: 0. Optional.                                                       |
| read-only sharing profile  | boolean  | Read-only sharing profile. Optional.                                                                                                                       |

#### Example of Body
```json
{
    "kubernetes": {
        "name": "kubernetes",
        "connectionForms": [
            {
                "name": "network",
                "fields": [
                    {
                        "name": "hostname",
                        "type": "TEXT"
                    },
                    {
                        "name": "port",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "use-ssl",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "ignore-cert",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "ca-cert",
                        "type": "MULTILINE"
                    }
                ]
            },
            {
                "name": "container",
                "fields": [
                    {
                        "name": "namespace",
                        "type": "TEXT"
                    },
                    {
                        "name": "pod",
                        "type": "TEXT"
                    },
                    {
                        "name": "container",
                        "type": "TEXT"
                    },
                    {
                        "name": "exec-command",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "name": "authentication",
                "fields": [
                    {
                        "name": "client-cert",
                        "type": "MULTILINE"
                    },
                    {
                        "name": "client-key",
                        "type": "MULTILINE"
                    }
                ]
            },
            {
                "name": "display",
                "fields": [
                    {
                        "name": "color-scheme",
                        "type": "TERMINAL_COLOR_SCHEME",
                        "options": [
                            "",
                            "black-white",
                            "gray-black",
                            "green-black",
                            "white-black"
                        ]
                    },
                    {
                        "name": "font-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "font-size",
                        "type": "ENUM",
                        "options": [
                            "",
                            "8",
                            "9",
                            "10",
                            "11",
                            "12",
                            "14",
                            "18",
                            "24",
                            "30",
                            "36",
                            "48",
                            "60",
                            "72",
                            "96"
                        ]
                    },
                    {
                        "name": "scrollback",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "read-only",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "behavior",
                "fields": [
                    {
                        "name": "backspace",
                        "type": "ENUM",
                        "options": [
                            "",
                            "127",
                            "8"
                        ]
                    }
                ]
            },
            {
                "name": "typescript",
                "fields": [
                    {
                        "name": "typescript-path",
                        "type": "TEXT"
                    },
                    {
                        "name": "typescript-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "create-typescript-path",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "recording",
                "fields": [
                    {
                        "name": "recording-path",
                        "type": "TEXT"
                    },
                    {
                        "name": "recording-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "recording-exclude-output",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "recording-exclude-mouse",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "recording-include-keys",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "create-recording-path",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            }
        ],
        "sharingProfileForms": [
            {
                "name": "display",
                "fields": [
                    {
                        "name": "read-only",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            }
        ]
    },
    "telnet": {
        "name": "telnet",
        "connectionForms": [
            {
                "name": "network",
                "fields": [
                    {
                        "name": "hostname",
                        "type": "TEXT"
                    },
                    {
                        "name": "port",
                        "type": "NUMERIC"
                    }
                ]
            },
            {
                "name": "authentication",
                "fields": [
                    {
                        "name": "username",
                        "type": "USERNAME"
                    },
                    {
                        "name": "password",
                        "type": "PASSWORD"
                    },
                    {
                        "name": "username-regex",
                        "type": "TEXT"
                    },
                    {
                        "name": "password-regex",
                        "type": "TEXT"
                    },
                    {
                        "name": "login-success-regex",
                        "type": "TEXT"
                    },
                    {
                        "name": "login-failure-regex",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "name": "display",
                "fields": [
                    {
                        "name": "color-scheme",
                        "type": "TERMINAL_COLOR_SCHEME",
                        "options": [
                            "",
                            "black-white",
                            "gray-black",
                            "green-black",
                            "white-black"
                        ]
                    },
                    {
                        "name": "font-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "font-size",
                        "type": "ENUM",
                        "options": [
                            "",
                            "8",
                            "9",
                            "10",
                            "11",
                            "12",
                            "14",
                            "18",
                            "24",
                            "30",
                            "36",
                            "48",
                            "60",
                            "72",
                            "96"
                        ]
                    },
                    {
                        "name": "scrollback",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "read-only",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "clipboard",
                "fields": [
                    {
                        "name": "disable-copy",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "disable-paste",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "behavior",
                "fields": [
                    {
                        "name": "backspace",
                        "type": "ENUM",
                        "options": [
                            "",
                            "127",
                            "8"
                        ]
                    },
                    {
                        "name": "terminal-type",
                        "type": "ENUM",
                        "options": [
                            "",
                            "xterm",
                            "xterm-256color",
                            "vt220",
                            "vt100",
                            "ansi",
                            "linux"
                        ]
                    }
                ]
            },
            {
                "name": "typescript",
                "fields": [
                    {
                        "name": "typescript-path",
                        "type": "TEXT"
                    },
                    {
                        "name": "typescript-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "create-typescript-path",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "recording",
                "fields": [
                    {
                        "name": "recording-path",
                        "type": "TEXT"
                    },
                    {
                        "name": "recording-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "recording-exclude-output",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "recording-exclude-mouse",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "recording-include-keys",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "create-recording-path",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "wol",
                "fields": [
                    {
                        "name": "wol-send-packet",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "wol-mac-addr",
                        "type": "TEXT"
                    },
                    {
                        "name": "wol-broadcast-addr",
                        "type": "TEXT"
                    },
                    {
                        "name": "wol-udp-port",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "wol-wait-time",
                        "type": "NUMERIC"
                    }
                ]
            }
        ],
        "sharingProfileForms": [
            {
                "name": "display",
                "fields": [
                    {
                        "name": "read-only",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            }
        ]
    },
    "ssh": {
        "name": "ssh",
        "connectionForms": [
            {
                "name": "network",
                "fields": [
                    {
                        "name": "hostname",
                        "type": "TEXT"
                    },
                    {
                        "name": "port",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "host-key",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "name": "authentication",
                "fields": [
                    {
                        "name": "username",
                        "type": "USERNAME"
                    },
                    {
                        "name": "password",
                        "type": "PASSWORD"
                    },
                    {
                        "name": "private-key",
                        "type": "MULTILINE"
                    },
                    {
                        "name": "passphrase",
                        "type": "PASSWORD"
                    }
                ]
            },
            {
                "name": "display",
                "fields": [
                    {
                        "name": "color-scheme",
                        "type": "TERMINAL_COLOR_SCHEME",
                        "options": [
                            "",
                            "black-white",
                            "gray-black",
                            "green-black",
                            "white-black"
                        ]
                    },
                    {
                        "name": "font-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "font-size",
                        "type": "ENUM",
                        "options": [
                            "",
                            "8",
                            "9",
                            "10",
                            "11",
                            "12",
                            "14",
                            "18",
                            "24",
                            "30",
                            "36",
                            "48",
                            "60",
                            "72",
                            "96"
                        ]
                    },
                    {
                        "name": "scrollback",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "read-only",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "clipboard",
                "fields": [
                    {
                        "name": "disable-copy",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "disable-paste",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "session",
                "fields": [
                    {
                        "name": "command",
                        "type": "TEXT"
                    },
                    {
                        "name": "locale",
                        "type": "TEXT"
                    },
                    {
                        "name": "timezone",
                        "type": "TIMEZONE"
                    },
                    {
                        "name": "server-alive-interval",
                        "type": "NUMERIC"
                    }
                ]
            },
            {
                "name": "behavior",
                "fields": [
                    {
                        "name": "backspace",
                        "type": "ENUM",
                        "options": [
                            "",
                            "127",
                            "8"
                        ]
                    },
                    {
                        "name": "terminal-type",
                        "type": "ENUM",
                        "options": [
                            "",
                            "xterm",
                            "xterm-256color",
                            "vt220",
                            "vt100",
                            "ansi",
                            "linux"
                        ]
                    }
                ]
            },
            {
                "name": "typescript",
                "fields": [
                    {
                        "name": "typescript-path",
                        "type": "TEXT"
                    },
                    {
                        "name": "typescript-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "create-typescript-path",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "recording",
                "fields": [
                    {
                        "name": "recording-path",
                        "type": "TEXT"
                    },
                    {
                        "name": "recording-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "recording-exclude-output",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "recording-exclude-mouse",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "recording-include-keys",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "create-recording-path",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "sftp",
                "fields": [
                    {
                        "name": "enable-sftp",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "sftp-root-directory",
                        "type": "TEXT"
                    },
                    {
                        "name": "sftp-disable-download",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "sftp-disable-upload",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "wol",
                "fields": [
                    {
                        "name": "wol-send-packet",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "wol-mac-addr",
                        "type": "TEXT"
                    },
                    {
                        "name": "wol-broadcast-addr",
                        "type": "TEXT"
                    },
                    {
                        "name": "wol-udp-port",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "wol-wait-time",
                        "type": "NUMERIC"
                    }
                ]
            }
        ],
        "sharingProfileForms": [
            {
                "name": "display",
                "fields": [
                    {
                        "name": "read-only",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            }
        ]
    },
    "vnc": {
        "name": "vnc",
        "connectionForms": [
            {
                "name": "network",
                "fields": [
                    {
                        "name": "hostname",
                        "type": "TEXT"
                    },
                    {
                        "name": "port",
                        "type": "NUMERIC"
                    }
                ]
            },
            {
                "name": "authentication",
                "fields": [
                    {
                        "name": "username",
                        "type": "USERNAME"
                    },
                    {
                        "name": "password",
                        "type": "PASSWORD"
                    }
                ]
            },
            {
                "name": "display",
                "fields": [
                    {
                        "name": "read-only",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "swap-red-blue",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "cursor",
                        "type": "ENUM",
                        "options": [
                            "",
                            "local",
                            "remote"
                        ]
                    },
                    {
                        "name": "color-depth",
                        "type": "ENUM",
                        "options": [
                            "",
                            "8",
                            "16",
                            "24",
                            "32"
                        ]
                    },
                    {
                        "name": "force-lossless",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "encodings",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "name": "clipboard",
                "fields": [
                    {
                        "name": "clipboard-encoding",
                        "type": "ENUM",
                        "options": [
                            "",
                            "ISO8859-1",
                            "UTF-8",
                            "UTF-16",
                            "CP1252"
                        ]
                    },
                    {
                        "name": "disable-copy",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "disable-paste",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "repeater",
                "fields": [
                    {
                        "name": "dest-host",
                        "type": "TEXT"
                    },
                    {
                        "name": "dest-port",
                        "type": "NUMERIC"
                    }
                ]
            },
            {
                "name": "recording",
                "fields": [
                    {
                        "name": "recording-path",
                        "type": "TEXT"
                    },
                    {
                        "name": "recording-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "recording-exclude-output",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "recording-exclude-mouse",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "recording-include-keys",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "create-recording-path",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "sftp",
                "fields": [
                    {
                        "name": "enable-sftp",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "sftp-hostname",
                        "type": "TEXT"
                    },
                    {
                        "name": "sftp-port",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "sftp-host-key",
                        "type": "TEXT"
                    },
                    {
                        "name": "sftp-username",
                        "type": "USERNAME"
                    },
                    {
                        "name": "sftp-password",
                        "type": "PASSWORD"
                    },
                    {
                        "name": "sftp-private-key",
                        "type": "MULTILINE"
                    },
                    {
                        "name": "sftp-passphrase",
                        "type": "PASSWORD"
                    },
                    {
                        "name": "sftp-root-directory",
                        "type": "TEXT"
                    },
                    {
                        "name": "sftp-directory",
                        "type": "TEXT"
                    },
                    {
                        "name": "sftp-server-alive-interval",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "sftp-disable-download",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "sftp-disable-upload",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "audio",
                "fields": [
                    {
                        "name": "enable-audio",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "audio-servername",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "name": "wol",
                "fields": [
                    {
                        "name": "wol-send-packet",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "wol-mac-addr",
                        "type": "TEXT"
                    },
                    {
                        "name": "wol-broadcast-addr",
                        "type": "TEXT"
                    },
                    {
                        "name": "wol-udp-port",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "wol-wait-time",
                        "type": "NUMERIC"
                    }
                ]
            }
        ],
        "sharingProfileForms": [
            {
                "name": "display",
                "fields": [
                    {
                        "name": "read-only",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            }
        ]
    },
    "rdp": {
        "name": "rdp",
        "connectionForms": [
            {
                "name": "network",
                "fields": [
                    {
                        "name": "hostname",
                        "type": "TEXT"
                    },
                    {
                        "name": "port",
                        "type": "NUMERIC"
                    }
                ]
            },
            {
                "name": "authentication",
                "fields": [
                    {
                        "name": "username",
                        "type": "USERNAME"
                    },
                    {
                        "name": "password",
                        "type": "PASSWORD"
                    },
                    {
                        "name": "domain",
                        "type": "TEXT"
                    },
                    {
                        "name": "security",
                        "type": "ENUM",
                        "options": [
                            "",
                            "rdp",
                            "tls",
                            "nla",
                            "vmconnect",
                            "any"
                        ]
                    },
                    {
                        "name": "disable-auth",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "ignore-cert",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "gateway",
                "fields": [
                    {
                        "name": "gateway-hostname",
                        "type": "TEXT"
                    },
                    {
                        "name": "gateway-port",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "gateway-username",
                        "type": "USERNAME"
                    },
                    {
                        "name": "gateway-password",
                        "type": "PASSWORD"
                    },
                    {
                        "name": "gateway-domain",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "name": "basic-parameters",
                "fields": [
                    {
                        "name": "initial-program",
                        "type": "TEXT"
                    },
                    {
                        "name": "client-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "server-layout",
                        "type": "ENUM",
                        "options": [
                            "",
                            "de-ch-qwertz",
                            "de-de-qwertz",
                            "en-gb-qwerty",
                            "en-us-qwerty",
                            "es-es-qwerty",
                            "es-latam-qwerty",
                            "failsafe",
                            "fr-be-azerty",
                            "fr-fr-azerty",
                            "fr-ca-qwerty",
                            "fr-ch-qwertz",
                            "hu-hu-qwertz",
                            "it-it-qwerty",
                            "ja-jp-qwerty",
                            "no-no-qwerty",
                            "pl-pl-qwerty",
                            "pt-br-qwerty",
                            "pt-pt-qwerty",
                            "ro-ro-qwerty",
                            "sv-se-qwerty",
                            "da-dk-qwerty",
                            "tr-tr-qwerty"
                        ]
                    },
                    {
                        "name": "timezone",
                        "type": "TIMEZONE"
                    },
                    {
                        "name": "enable-touch",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "console",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "display",
                "fields": [
                    {
                        "name": "width",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "height",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "dpi",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "color-depth",
                        "type": "ENUM",
                        "options": [
                            "",
                            "8",
                            "16",
                            "24",
                            "32"
                        ]
                    },
                    {
                        "name": "force-lossless",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "resize-method",
                        "type": "ENUM",
                        "options": [
                            "",
                            "reconnect",
                            "display-update"
                        ]
                    },
                    {
                        "name": "read-only",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "clipboard",
                "fields": [
                    {
                        "name": "normalize-clipboard",
                        "type": "ENUM",
                        "options": [
                            "",
                            "preserve",
                            "unix",
                            "windows"
                        ]
                    },
                    {
                        "name": "disable-copy",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "disable-paste",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "device-redirection",
                "fields": [
                    {
                        "name": "console-audio",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "disable-audio",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "enable-audio-input",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "enable-printing",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "printer-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "enable-drive",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "drive-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "disable-download",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "disable-upload",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "drive-path",
                        "type": "TEXT"
                    },
                    {
                        "name": "create-drive-path",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "static-channels",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "name": "performance",
                "fields": [
                    {
                        "name": "enable-wallpaper",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "enable-theming",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "enable-font-smoothing",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "enable-full-window-drag",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "enable-desktop-composition",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "enable-menu-animations",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "disable-bitmap-caching",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "disable-offscreen-caching",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "disable-glyph-caching",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "disable-gfx",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "remoteapp",
                "fields": [
                    {
                        "name": "remote-app",
                        "type": "TEXT"
                    },
                    {
                        "name": "remote-app-dir",
                        "type": "TEXT"
                    },
                    {
                        "name": "remote-app-args",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "name": "preconnection-pdu",
                "fields": [
                    {
                        "name": "preconnection-id",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "preconnection-blob",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "name": "load-balancing",
                "fields": [
                    {
                        "name": "load-balance-info",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "name": "recording",
                "fields": [
                    {
                        "name": "recording-path",
                        "type": "TEXT"
                    },
                    {
                        "name": "recording-name",
                        "type": "TEXT"
                    },
                    {
                        "name": "recording-exclude-output",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "recording-exclude-mouse",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "recording-exclude-touch",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "recording-include-keys",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "create-recording-path",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "sftp",
                "fields": [
                    {
                        "name": "enable-sftp",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "sftp-hostname",
                        "type": "TEXT"
                    },
                    {
                        "name": "sftp-port",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "sftp-host-key",
                        "type": "TEXT"
                    },
                    {
                        "name": "sftp-username",
                        "type": "USERNAME"
                    },
                    {
                        "name": "sftp-password",
                        "type": "PASSWORD"
                    },
                    {
                        "name": "sftp-private-key",
                        "type": "MULTILINE"
                    },
                    {
                        "name": "sftp-passphrase",
                        "type": "PASSWORD"
                    },
                    {
                        "name": "sftp-root-directory",
                        "type": "TEXT"
                    },
                    {
                        "name": "sftp-directory",
                        "type": "TEXT"
                    },
                    {
                        "name": "sftp-server-alive-interval",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "sftp-disable-download",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "sftp-disable-upload",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            },
            {
                "name": "wol",
                "fields": [
                    {
                        "name": "wol-send-packet",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    },
                    {
                        "name": "wol-mac-addr",
                        "type": "TEXT"
                    },
                    {
                        "name": "wol-broadcast-addr",
                        "type": "TEXT"
                    },
                    {
                        "name": "wol-udp-port",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "wol-wait-time",
                        "type": "NUMERIC"
                    }
                ]
            }
        ],
        "sharingProfileForms": [
            {
                "name": "display",
                "fields": [
                    {
                        "name": "read-only",
                        "type": "BOOLEAN",
                        "options": [
                            "true"
                        ]
                    }
                ]
            }
        ]
    }
}
```

# Languages

## List Languages
- List of all available languages.

### Request

#### Method
- GET

#### Endpoint
- /api/languages

#### Path Parameters
- \-

#### Query Parameters
- \-

#### Headers
- \-

#### Body
- \-

#### Example of Body

### Response

#### Normal Response Code
- 200 OK

#### Body
- \-

#### Example of Body
```json
{
    "de": "Deutsch",
    "no": "Norsk Bokmål",
    "ru": "Русский",
    "ko": "한국어",
    "pt": "Português",
    "en": "English",
    "it": "Italiano",
    "fr": "Français",
    "zh": "简体中文",
    "es": "Spanish",
    "cs": "Čeština",
    "ja": "日本語",
    "pl": "Polski",
    "nl": "Nederlands",
    "ca": "Catalan"
}
```
