# Connections

# Table of Contents
- [Create VNC Connection](#create-vnc-connection)
- [Create SSH Connection](#create-ssh-connection)
- [Create RDP Connection](#create-rdp-connection)
- [Create Telnet Connection](#create-telnet-connection)
- [Create Kubernetes Connection](#create-kubernetes-connection)
- [Update VNC Connection](#update-vnc-connection)
- [Update SSH Connection](#update-ssh-connection)
- [Update RDP Connection](#update-rdp-connection)
- [Update Telnet Connection](#update-telnet-connection)
- [Update Kubernetes Connection](#update-kubernetes-connection)
- [Delete Connection](#delete-connection)
- [Kill Active Connection](#kill-active-connection)
- [List Connections](#list-connections)
- [List History of Connections](#list-history-of-connections)
- [List Active Connections](#list-active-connections)
- [Details of Connection](#details-of-connection)
- [Details of Connection Parameters](#details-of-connection-parameters)
- [Details of Connection History](#details-of-connection-history)
- [Details of Connection Sharing Profiles](#details-of-connection-sharing-profiles)

## Create VNC Connection
- Creating a VNC connection.

### Request

#### Method
- POST

#### Endpoint
- /api/session/data/{dataSource}/connections

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                       | Type     | Description                                                                                                                                                |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| parentIdentifier           | string   | Connection group identifier. Must be ROOT if no connection group is used. Required.                                                                        |
| name                       | string   | Connection name. Required.                                                                                                                                 |
| protocol                   | string   | Connection protocol. Must be vnc. Required.                                                                                                                |
| parameters                 | object   | Parameters of the connection.                                                                                                                              |
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
| attributes                 | object   | Contains connection's information and settings.                                                                                                            |
| max-connections            | integer  | Maximum number of concurrent connections.                                                                                                                  |
| max-connections-per-user   | integer  | Maximum number of concurrent connections per user.                                                                                                         |
| weight                     | integer  | It used for weighted load balancing algorithms.                                                                                                            |
| failover-only              | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred.                                                 |
| guacd-hostname             | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                                                                        |
| guacd-port                 | integer  | Port for connecting to guacd. Default: 4822.                                                                                                               |
| guacd-encryption           | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                                                                        |

#### Example of Body
```json
{
    "parentIdentifier": "ROOT",                                               
    "name": "VNC-example",                                        
    "protocol": "vnc",                                      
    "parameters": {
        "hostname": "192.168.1.52",
        "port": "5900",
        "username": "",                                     
        "password": "test",                           
        "read-only": "",                                   
        "swap-red-blue": "",                                
        "cursor": "",                                       
        "color-depth": "",                                  
        "force-lossless": "",                               
        "encodings": "",                                    
        "clipboard-encoding": "",                           
        "disable-copy": "",                                                     
        "disable-paste": "",                                
        "dest-host": "",                                    
        "dest-port": "",                                    
        "recording-path": "/home/guacd/${HISTORY_UUID}",    
        "recording-name": "",                               
        "recording-exclude-output": "",                     
        "recording-exclude-mouse": "",                      
        "recording-include-keys": "",                       
        "create-recording-path": "true",                    
        "enable-sftp": "true",                                                         
        "sftp-hostname": "192.168.1.52",                        
        "sftp-port": "",                                    
        "sftp-host-key": "",                                  
        "sftp-username": "test",                           
        "sftp-password": "test",                                
        "sftp-private-key": "",                   
        "sftp-passphrase": "",                              
        "sftp-root-directory": "",                                            
        "sftp-directory": "",                               
        "sftp-server-alive-interval": "",                   
        "sftp-disable-download": "",                        
        "sftp-disable-upload": "",                          
        "enable-audio": "",
        "audio-servername": "",                          
        "wol-send-packet": "",
        "wol-mac-addr": "",
        "wol-broadcast-addr": "",
        "wol-udp-port": "",
        "wol-wait-time": ""                          
    },
    "attributes": {
        "max-connections": "1",
        "max-connections-per-user": "1",
        "weight": "",
        "failover-only": "",
        "guacd-hostname": "",                          
        "guacd-port": "",
        "guacd-encryption": ""                  
    }
}
```

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name               | Type     | Description                   |
| ------------------ | -------- | ----------------------------- |
| identifier         | integer  | Connection identifier.        |
| activeConnections  | integer  | Number of active connections. |

#### Example of Body
```json
{
    "name": "VNC-example",
    "identifier": "1",
    "parentIdentifier": "ROOT",
    "protocol": "vnc",
    "parameters": {
        "hostname": "192.168.1.52",
        "port": "5900",
        "username": "",
        "password": "test",
        "read-only": "",
        "swap-red-blue": "",
        "cursor": "",
        "color-depth": "",
        "force-lossless": "",
        "encodings": "",
        "clipboard-encoding": "",
        "disable-copy": "",
        "disable-paste": "",
        "dest-host": "",
        "dest-port": "",
        "recording-path": "/home/guacd/${HISTORY_UUID}",
        "recording-name": "",
        "recording-exclude-output": "",
        "recording-exclude-mouse": "",
        "recording-include-keys": "",
        "create-recording-path": "true",
        "enable-sftp": "true",
        "sftp-hostname": "192.168.1.52",
        "sftp-port": "",
        "sftp-host-key": "",
        "sftp-username": "test",
        "sftp-password": "test",
        "sftp-private-key": "",
        "sftp-passphrase": "",
        "sftp-root-directory": "",
        "sftp-directory": "",
        "sftp-server-alive-interval": "",
        "sftp-disable-download": "",
        "sftp-disable-upload": "",
        "enable-audio": "",
        "audio-servername": "",
        "wol-send-packet": "",
        "wol-mac-addr": "",
        "wol-broadcast-addr": "",
        "wol-udp-port": "",
        "wol-wait-time": ""
    },
    "attributes": {
        "failover-only": "",
        "guacd-encryption": "",
        "weight": "",
        "max-connections": "1",
        "guacd-hostname": "",
        "guacd-port": "",
        "max-connections-per-user": "1"
    },
    "activeConnections": 0
}
```

## Create SSH Connection
- Creating a SSH connection.

### Request

#### Method
- POST

#### Endpoint
- /api/session/data/{dataSource}/connections

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                      | Type     | Description                                                                                                                                            |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| parentIdentifier          | string   | Connection group identifier. Must be ROOT if no connection group is used. Required.                                                                    |
| name                      | string   | Connection name. Required.                                                                                                                             |
| protocol                  | string   | Connection protocol. Must be ssh. Required.                                                                                                            |
| parameters                | object   | Parameters of the connection.                                                                                                                          |
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
| attributes                | object   | Contains connection's information and settings.                                                                                                        |
| max-connections           | integer  | Maximum number of concurrent connections.                                                                                                              |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                                                                                     |
| weight                    | integer  | It used for weighted load balancing algorithms.                                                                                                        |
| failover-only             | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred.                                             |
| guacd-hostname            | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                                                                    |
| guacd-port                | integer  | Port for connecting to guacd. Default: 4822.                                                                                                           |
| guacd-encryption          | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                                                                    |

#### Example of Body
```json
{
    "parentIdentifier": "ROOT",                                     
    "name": "SSH-example",                                         
    "protocol": "ssh",                                      
    "parameters": {
        "hostname": "192.168.1.52",                             
        "port": "",                                         
        "host-key": "",                                     
        "username": "test",                                
        "password": "test",                                     
        "private-key": "",                      
        "passphrase": "",                                            
        "color-scheme": "",                                 
        "font-name": "",                                    
        "font-size": "",                                    
        "scrollback": "",                                  
        "read-only": "",                                            
        "disable-copy": "",                                                      
        "disable-paste": "",                                        
        "command": "",                                      
        "locale": "",                                       
        "timezone": "",                                    
        "server-alive-interval": "",                        
        "backspace": "",                                    
        "terminal-type": "",                                
        "typescript-path": "/home/guacd/${HISTORY_UUID}",   
        "typescript-name": "",                              
        "create-typescript-path": "true",                   
        "recording-path": "/home/guacd/${HISTORY_UUID}",    
        "recording-name": "",                              
        "recording-exclude-output": "",                     
        "recording-exclude-mouse": "",                      
        "recording-include-keys": "",                      
        "create-recording-path": "true",                    
        "enable-sftp": "true",                                                           
        "sftp-root-directory": "",                                        
        "sftp-disable-download": "",                       
        "sftp-disable-upload": "",                         
        "wol-send-packet": "",                               
        "wol-mac-addr": "",                                 
        "wol-broadcast-addr": "",                           
        "wol-udp-port": "",                                 
        "wol-wait-time": ""                                                    
    },
    "attributes": {
        "max-connections": "1",                              
        "max-connections-per-user": "1",                    
        "weight": "",                                       
        "failover-only": "",                                
        "guacd-hostname": "",                                                          
        "guacd-port": "",                                   
        "guacd-encryption": ""                                                
    }
}
```

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name               | Type     | Description                   |
| ------------------ | -------- | ----------------------------- |
| identifier         | integer  | Connection identifier.        |
| activeConnections  | integer  | Number of active connections. |

#### Example of Body
```json
{
    "name": "SSH-example",
    "identifier": "2",
    "parentIdentifier": "ROOT",
    "protocol": "ssh",
    "parameters": {
        "hostname": "192.168.1.52",
        "port": "",
        "host-key": "",
        "username": "test",
        "password": "test",
        "private-key": "",
        "passphrase": "",
        "color-scheme": "",
        "font-name": "",
        "font-size": "",
        "scrollback": "",
        "read-only": "",
        "disable-copy": "",
        "disable-paste": "",
        "command": "",
        "locale": "",
        "timezone": "",
        "server-alive-interval": "",
        "backspace": "",
        "terminal-type": "",
        "typescript-path": "/home/guacd/${HISTORY_UUID}",
        "typescript-name": "",
        "create-typescript-path": "true",
        "recording-path": "/home/guacd/${HISTORY_UUID}",
        "recording-name": "",
        "recording-exclude-output": "",
        "recording-exclude-mouse": "",
        "recording-include-keys": "",
        "create-recording-path": "true",
        "enable-sftp": "true",
        "sftp-root-directory": "",
        "sftp-disable-download": "",
        "sftp-disable-upload": "",
        "wol-send-packet": "",
        "wol-mac-addr": "",
        "wol-broadcast-addr": "",
        "wol-udp-port": "",
        "wol-wait-time": ""
    },
    "attributes": {
        "failover-only": "",
        "guacd-encryption": "",
        "weight": "",
        "max-connections": "1",
        "guacd-hostname": "",
        "guacd-port": "",
        "max-connections-per-user": "1"
    },
    "activeConnections": 0
}
```

## Create RDP Connection
- Creating a RDP connection.

### Request

#### Method
- POST

#### Endpoint
- /api/session/data/{dataSource}/connections

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                       | Type     | Description                                                                                                                                                |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| parentIdentifier           | string   | Connection group identifier. Must be ROOT if no connection group is used. Required.                                                                        |
| name                       | string   | Connection name. Required.                                                                                                                                 |
| protocol                   | string   | Connection protocol. Must be rdp. Required.                                                                                                                |
| parameters                 | object   | Parameters of the connection.                                                                                                                              |
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
| attributes                 | object   | Contains connection's information and settings.                                                                                                            |
| max-connections            | integer  | Maximum number of concurrent connections.                                                                                                                  |
| max-connections-per-user   | integer  | Maximum number of concurrent connections per user.                                                                                                         |
| weight                     | integer  | It used for weighted load balancing algorithms.                                                                                                            |
| failover-only              | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred.                                                 |
| guacd-hostname             | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                                                                        |
| guacd-port                 | integer  | Port for connecting to guacd. Default: 4822.                                                                                                               |
| guacd-encryption           | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                                                                        |

#### Example of Body
```json
{   
    "parentIdentifier": "ROOT",
    "name": "RDP-example",
    "protocol": "rdp",
    "parameters": {
        "hostname": "192.168.1.52",
        "port": "",
        "username": "test",
        "password": "test",
        "domain": "",
        "security": "",
        "disable-auth": "",
        "ignore-cert": "",
        "gateway-hostname": "",
        "gateway-port": "",
        "gateway-username": "",
        "gateway-password": "",
        "gateway-domain": "",
        "initial-program": "",
        "client-name": "",
        "server-layout": "",
        "timezone": "",
        "enable-touch": "",
        "console": "",
        "width": "",
        "height": "",
        "dpi": "",
        "color-depth": "",
        "force-lossless": "",
        "resize-method": "",
        "read-only": "",
        "normalize-clipboard": "",
        "disable-copy": "",
        "disable-paste": "",
        "console-audio": "",
        "disable-audio": "",
        "enable-audio-input": "",
        "enable-printing": "",
        "printer-name": "",
        "enable-drive": "",
        "drive-name": "",
        "disable-download": "",
        "disable-upload": "",
        "drive-path": "",
        "create-drive-path": "",
        "static-channels": "",
        "enable-wallpaper": "",
        "enable-theming": "",
        "enable-font-smoothing": "",
        "enable-full-window-drag": "",
        "enable-desktop-composition": "",
        "enable-menu-animations": "",
        "disable-bitmap-caching": "",
        "disable-offscreen-caching": "",
        "disable-glyph-caching": "",
        "disable-gfx": "",
        "remote-app": "",
        "remote-app-dir": "",
        "remote-app-args": "",
        "preconnection-id": "",
        "preconnection-blob": "",
        "load-balance-info": "",
        "recording-path": "/home/guacd/${HISTORY_UUID}",
        "recording-name": "",
        "recording-exclude-output": "",
        "recording-exclude-mouse": "",
        "recording-exclude-touch": "",
        "recording-include-keys": "",
        "create-recording-path": "true",
        "enable-sftp": "true",                                                         
        "sftp-hostname": "192.168.1.52",                        
        "sftp-port": "",                                    
        "sftp-host-key": "",                                  
        "sftp-username": "test",                           
        "sftp-password": "test",                                
        "sftp-private-key": "",                   
        "sftp-passphrase": "",                              
        "sftp-root-directory": "",                                            
        "sftp-directory": "",                               
        "sftp-server-alive-interval": "",                   
        "sftp-disable-download": "",                        
        "sftp-disable-upload": "",                                 
        "wol-send-packet": "",
        "wol-mac-addr": "",
        "wol-broadcast-addr": "",
        "wol-udp-port": "",
        "wol-wait-time": ""
    },
    "attributes": {
        "max-connections": "1",
        "max-connections-per-user": "1",
        "weight": "",
        "failover-only": "",
        "guacd-hostname": "",                          
        "guacd-port": "",
        "guacd-encryption": ""
    }
}
```

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name               | Type     | Description                   |
| ------------------ | -------- | ----------------------------- |
| identifier         | integer  | Connection identifier.        |
| activeConnections  | integer  | Number of active connections. |

#### Example of Body
```json
{
    "name": "RDP-example",
    "identifier": "3",
    "parentIdentifier": "ROOT",
    "protocol": "rdp",
    "parameters": {
        "hostname": "192.168.1.52",
        "port": "",
        "username": "test",
        "password": "test",
        "domain": "",
        "security": "",
        "disable-auth": "",
        "ignore-cert": "",
        "gateway-hostname": "",
        "gateway-port": "",
        "gateway-username": "",
        "gateway-password": "",
        "gateway-domain": "",
        "initial-program": "",
        "client-name": "",
        "server-layout": "",
        "timezone": "",
        "enable-touch": "",
        "console": "",
        "width": "",
        "height": "",
        "dpi": "",
        "color-depth": "",
        "force-lossless": "",
        "resize-method": "",
        "read-only": "",
        "normalize-clipboard": "",
        "disable-copy": "",
        "disable-paste": "",
        "console-audio": "",
        "disable-audio": "",
        "enable-audio-input": "",
        "enable-printing": "",
        "printer-name": "",
        "enable-drive": "",
        "drive-name": "",
        "disable-download": "",
        "disable-upload": "",
        "drive-path": "",
        "create-drive-path": "",
        "static-channels": "",
        "enable-wallpaper": "",
        "enable-theming": "",
        "enable-font-smoothing": "",
        "enable-full-window-drag": "",
        "enable-desktop-composition": "",
        "enable-menu-animations": "",
        "disable-bitmap-caching": "",
        "disable-offscreen-caching": "",
        "disable-glyph-caching": "",
        "disable-gfx": "",
        "remote-app": "",
        "remote-app-dir": "",
        "remote-app-args": "",
        "preconnection-id": "",
        "preconnection-blob": "",
        "load-balance-info": "",
        "recording-path": "/home/guacd/${HISTORY_UUID}",
        "recording-name": "",
        "recording-exclude-output": "",
        "recording-exclude-mouse": "",
        "recording-exclude-touch": "",
        "recording-include-keys": "",
        "create-recording-path": "true",
        "enable-sftp": "true",
        "sftp-hostname": "192.168.1.52",
        "sftp-port": "",
        "sftp-host-key": "",
        "sftp-username": "test",
        "sftp-password": "test",
        "sftp-private-key": "",
        "sftp-passphrase": "",
        "sftp-root-directory": "",
        "sftp-directory": "",
        "sftp-server-alive-interval": "",
        "sftp-disable-download": "",
        "sftp-disable-upload": "",
        "wol-send-packet": "",
        "wol-mac-addr": "",
        "wol-broadcast-addr": "",
        "wol-udp-port": "",
        "wol-wait-time": ""
    },
    "attributes": {
        "failover-only": "",
        "guacd-encryption": "",
        "weight": "",
        "max-connections": "1",
        "guacd-hostname": "",
        "guacd-port": "",
        "max-connections-per-user": "1"
    },
    "activeConnections": 0
}
```

## Create Telnet Connection
- Creating a Telnet connection.

### Request

#### Method
- POST

#### Endpoint
- /api/session/data/{dataSource}/connections

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                      | Type     | Description                                                                                                                                            |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| parentIdentifier          | string   | Connection group identifier. Must be ROOT if no connection group is used. Required.                                                                    |
| name                      | string   | Connection name. Required.                                                                                                                             |
| protocol                  | string   | Connection protocol. Must be telnet. Required.                                                                                                         |
| parameters                | object   | Parameters of the connection.                                                                                                                          |
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
| attributes                | object   | Contains connection's information and settings.                                                                                                        |
| max-connections           | integer  | Maximum number of concurrent connections.                                                                                                              |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                                                                                     |
| weight                    | integer  | It used for weighted load balancing algorithms.                                                                                                        |
| failover-only             | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred.                                             |
| guacd-hostname            | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                                                                    |
| guacd-port                | integer  | Port for connecting to guacd. Default: 4822.                                                                                                           |
| guacd-encryption          | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                                                                    |

#### Example of Body
```json
{
    "parentIdentifier": "ROOT",                                     
    "name": "Telnet-example",                                         
    "protocol": "telnet",                                      
    "parameters": {
        "hostname": "192.168.1.52",                             
        "port": "",                                                                              
        "username": "test",                                
        "password": "test",                                     
        "username-regex": "",
        "password-regex": "",
        "login-success-regex": "",
        "login-failure-regex": "",                                  
        "color-scheme": "",                                 
        "font-name": "",                                    
        "font-size": "",                                    
        "scrollback": "",                                  
        "read-only": "",                                            
        "disable-copy": "",                                                      
        "disable-paste": "",                                                                 
        "backspace": "",                                    
        "terminal-type": "",                                
        "typescript-path": "/home/guacd/${HISTORY_UUID}",   
        "typescript-name": "",                              
        "create-typescript-path": "true",                   
        "recording-path": "/home/guacd/${HISTORY_UUID}",    
        "recording-name": "",                              
        "recording-exclude-output": "",                     
        "recording-exclude-mouse": "",                      
        "recording-include-keys": "",                      
        "create-recording-path": "true",                                             
        "wol-send-packet": "",                               
        "wol-mac-addr": "",                                 
        "wol-broadcast-addr": "",                           
        "wol-udp-port": "",                                 
        "wol-wait-time": ""                                                    
    },
    "attributes": {
        "max-connections": "1",                              
        "max-connections-per-user": "1",                    
        "weight": "",                                       
        "failover-only": "",                                
        "guacd-hostname": "",                                                          
        "guacd-port": "",                                   
        "guacd-encryption": ""                                                
    }
}
```

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name               | Type     | Description                   |
| ------------------ | -------- | ----------------------------- |
| identifier         | integer  | Connection identifier.        |
| activeConnections  | integer  | Number of active connections. |

#### Example of Body
```json
{
    "name": "Telnet-example",
    "identifier": "4",
    "parentIdentifier": "ROOT",
    "protocol": "telnet",
    "parameters": {
        "hostname": "192.168.1.52",
        "port": "",
        "username": "test",
        "password": "test",
        "username-regex": "",
        "password-regex": "",
        "login-success-regex": "",
        "login-failure-regex": "",
        "color-scheme": "",
        "font-name": "",
        "font-size": "",
        "scrollback": "",
        "read-only": "",
        "disable-copy": "",
        "disable-paste": "",
        "backspace": "",
        "terminal-type": "",
        "typescript-path": "/home/guacd/${HISTORY_UUID}",
        "typescript-name": "",
        "create-typescript-path": "true",
        "recording-path": "/home/guacd/${HISTORY_UUID}",
        "recording-name": "",
        "recording-exclude-output": "",
        "recording-exclude-mouse": "",
        "recording-include-keys": "",
        "create-recording-path": "true",
        "wol-send-packet": "",
        "wol-mac-addr": "",
        "wol-broadcast-addr": "",
        "wol-udp-port": "",
        "wol-wait-time": ""
    },
    "attributes": {
        "failover-only": "",
        "guacd-encryption": "",
        "weight": "",
        "max-connections": "1",
        "guacd-hostname": "",
        "guacd-port": "",
        "max-connections-per-user": "1"
    },
    "activeConnections": 0
}
```

## Create Kubernetes Connection
- Creating a Kubernetes connection.

### Request

#### Method
- POST

#### Endpoint
- /api/session/data/{dataSource}/connections

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                      | Type     | Description                                                                                                                                            |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| parentIdentifier          | string   | Connection group identifier. Must be ROOT if no connection group is used. Required.                                                                    |
| name                      | string   | Connection name. Required.                                                                                                                             |
| protocol                  | string   | Connection protocol. Must be kubernetes. Required.                                                                                                     |
| parameters                | object   | Parameters of the connection.                                                                                                                          |
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
| attributes                | object   | Contains connection's information and settings.                                                                                                        |
| max-connections           | integer  | Maximum number of concurrent connections.                                                                                                              |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                                                                                     |
| weight                    | integer  | It used for weighted load balancing algorithms.                                                                                                        |
| failover-only             | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred.                                             |
| guacd-hostname            | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                                                                    |
| guacd-port                | integer  | Port for connecting to guacd. Default: 4822.                                                                                                           |
| guacd-encryption          | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                                                                    |

#### Example of Body
```json
{
    "parentIdentifier": "ROOT",                                     
    "name": "Kubernetes-example",                                         
    "protocol": "kubernetes",                                      
    "parameters": {
        "hostname": "192.168.1.52",                             
        "port": "",                                         
        "use-ssl": "",                                     
        "ignore-cert": "",                                
        "ca-cert": "",                                                           
        "namespace": "",                                            
        "pod": "test",                                 
        "container": "",
        "exec-command": "",
        "client-cert": "",
        "client-key": "",
        "color-scheme": "",
        "font-name": "",                                 
        "font-size": "",                                    
        "scrollback": "",                                  
        "read-only": "",
        "backspace": "",
        "typescript-path": "/home/guacd/${HISTORY_UUID}",   
        "typescript-name": "",                              
        "create-typescript-path": "true",
        "recording-path": "/home/guacd/${HISTORY_UUID}",    
        "recording-name": "",                              
        "recording-exclude-output": "",                     
        "recording-exclude-mouse": "",                      
        "recording-include-keys": "",                      
        "create-recording-path": "true"                                                    
    },
    "attributes": {
        "max-connections": "1",                              
        "max-connections-per-user": "1",                    
        "weight": "",                                       
        "failover-only": "",                                
        "guacd-hostname": "",                                                          
        "guacd-port": "",                                   
        "guacd-encryption": ""                                                
    }
}
```

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name               | Type     | Description                   |
| ------------------ | -------- | ----------------------------- |
| identifier         | integer  | Connection identifier.        |
| activeConnections  | integer  | Number of active connections. |

#### Example of Body
```json
{
    "name": "Kubernetes-example",
    "identifier": "5",
    "parentIdentifier": "ROOT",
    "protocol": "kubernetes",
    "parameters": {
        "hostname": "192.168.1.52",
        "port": "",
        "use-ssl": "",
        "ignore-cert": "",
        "ca-cert": "",
        "namespace": "",
        "pod": "test",
        "container": "",
        "exec-command": "",
        "client-cert": "",
        "client-key": "",
        "color-scheme": "",
        "font-name": "",
        "font-size": "",
        "scrollback": "",
        "read-only": "",
        "backspace": "",
        "typescript-path": "/home/guacd/${HISTORY_UUID}",
        "typescript-name": "",
        "create-typescript-path": "true",
        "recording-path": "/home/guacd/${HISTORY_UUID}",
        "recording-name": "",
        "recording-exclude-output": "",
        "recording-exclude-mouse": "",
        "recording-include-keys": "",
        "create-recording-path": "true"
    },
    "attributes": {
        "failover-only": "",
        "guacd-encryption": "",
        "weight": "",
        "max-connections": "1",
        "guacd-hostname": "",
        "guacd-port": "",
        "max-connections-per-user": "1"
    },
    "activeConnections": 0
}
```

## Update VNC Connection
- Updating a VNC connection.

### Request

#### Method
- PUT

#### Endpoint
- /api/session/data/{dataSource}/connections/{connectionIdentifier}

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |
| connectionIdentifier (Required) | integer | The identifier of the connection.         |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                       | Type     | Description                                                                                                                                                |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| parentIdentifier           | string   | Connection group identifier. Must be ROOT if no connection group is used. Required.                                                                        |
| name                       | string   | Connection name. Required.                                                                                                                                 |
| protocol                   | string   | Connection protocol. Must be vnc. Required.                                                                                                                |
| parameters                 | object   | Parameters of the connection.                                                                                                                              |
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
| attributes                 | object   | Contains connection's information and settings.                                                                                                            |
| max-connections            | integer  | Maximum number of concurrent connections.                                                                                                                  |
| max-connections-per-user   | integer  | Maximum number of concurrent connections per user.                                                                                                         |
| weight                     | integer  | It used for weighted load balancing algorithms.                                                                                                            |
| failover-only              | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred.                                                 |
| guacd-hostname             | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                                                                        |
| guacd-port                 | integer  | Port for connecting to guacd. Default: 4822.                                                                                                               |
| guacd-encryption           | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                                                                        |

#### Example of Body
```json
{
    "parentIdentifier": "ROOT",                                               
    "name": "VNC-example",                                        
    "protocol": "vnc",                                      
    "parameters": {
        "hostname": "192.168.1.52",
        "port": "5900",
        "username": "",                                     
        "password": "test",                           
        "read-only": "",                                   
        "swap-red-blue": "",                                
        "cursor": "",                                       
        "color-depth": "",                                  
        "force-lossless": "",                               
        "encodings": "",                                    
        "clipboard-encoding": "",                           
        "disable-copy": "",                                                     
        "disable-paste": "",                                
        "dest-host": "",                                    
        "dest-port": "",                                    
        "recording-path": "/home/guacd/${HISTORY_UUID}",    
        "recording-name": "",                               
        "recording-exclude-output": "",                     
        "recording-exclude-mouse": "",                      
        "recording-include-keys": "",                       
        "create-recording-path": "true",                    
        "enable-sftp": "true",                                                         
        "sftp-hostname": "192.168.1.52",                        
        "sftp-port": "",                                    
        "sftp-host-key": "",                                  
        "sftp-username": "test",                           
        "sftp-password": "test",                                
        "sftp-private-key": "",                   
        "sftp-passphrase": "",                              
        "sftp-root-directory": "",                                            
        "sftp-directory": "",                               
        "sftp-server-alive-interval": "",                   
        "sftp-disable-download": "",                        
        "sftp-disable-upload": "",                          
        "enable-audio": "",
        "audio-servername": "",                          
        "wol-send-packet": "",
        "wol-mac-addr": "",
        "wol-broadcast-addr": "",
        "wol-udp-port": "",
        "wol-wait-time": ""                          
    },
    "attributes": {
        "max-connections": "2",
        "max-connections-per-user": "1",
        "weight": "",
        "failover-only": "",
        "guacd-hostname": "",                          
        "guacd-port": "",
        "guacd-encryption": ""                  
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

## Update SSH Connection
- Updating a SSH connection.

### Request

#### Method
- PUT

#### Endpoint
- /api/session/data/{dataSource}/connections/{connectionIdentifier}

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |
| connectionIdentifier (Required) | integer | The identifier of the connection.         |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                      | Type     | Description                                                                                                                                            |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| parentIdentifier          | string   | Connection group identifier. Must be ROOT if no connection group is used. Required.                                                                    |
| name                      | string   | Connection name. Required.                                                                                                                             |
| protocol                  | string   | Connection protocol. Must be ssh. Required.                                                                                                            |
| parameters                | object   | Parameters of the connection.                                                                                                                          |
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
| attributes                | object   | Contains connection's information and settings.                                                                                                        |
| max-connections           | integer  | Maximum number of concurrent connections.                                                                                                              |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                                                                                     |
| weight                    | integer  | It used for weighted load balancing algorithms.                                                                                                        |
| failover-only             | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred.                                             |
| guacd-hostname            | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                                                                    |
| guacd-port                | integer  | Port for connecting to guacd. Default: 4822.                                                                                                           |
| guacd-encryption          | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                                                                    |

#### Example of Body
```json
{
    "parentIdentifier": "ROOT",                                     
    "name": "SSH-example",                                         
    "protocol": "ssh",                                      
    "parameters": {
        "hostname": "192.168.1.52",                             
        "port": "",                                         
        "host-key": "",                                     
        "username": "test",                                
        "password": "test",                                     
        "private-key": "",                      
        "passphrase": "",                                            
        "color-scheme": "",                                 
        "font-name": "",                                    
        "font-size": "",                                    
        "scrollback": "",                                  
        "read-only": "",                                            
        "disable-copy": "",                                                      
        "disable-paste": "",                                        
        "command": "",                                      
        "locale": "",                                       
        "timezone": "",                                    
        "server-alive-interval": "",                        
        "backspace": "",                                    
        "terminal-type": "",                                
        "typescript-path": "/home/guacd/${HISTORY_UUID}",   
        "typescript-name": "",                              
        "create-typescript-path": "true",                   
        "recording-path": "/home/guacd/${HISTORY_UUID}",    
        "recording-name": "",                              
        "recording-exclude-output": "",                     
        "recording-exclude-mouse": "",                      
        "recording-include-keys": "",                      
        "create-recording-path": "true",                    
        "enable-sftp": "true",                                                           
        "sftp-root-directory": "",                                        
        "sftp-disable-download": "",                       
        "sftp-disable-upload": "",                         
        "wol-send-packet": "",                               
        "wol-mac-addr": "",                                 
        "wol-broadcast-addr": "",                           
        "wol-udp-port": "",                                 
        "wol-wait-time": ""                                                    
    },
    "attributes": {
        "max-connections": "2",                              
        "max-connections-per-user": "1",                    
        "weight": "",                                       
        "failover-only": "",                                
        "guacd-hostname": "",                                                          
        "guacd-port": "",                                   
        "guacd-encryption": ""                                                
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

## Update RDP Connection
- Updating a RDP connection.

### Request

#### Method
- PUT

#### Endpoint
- /api/session/data/{dataSource}/connections/{connectionIdentifier}

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |
| connectionIdentifier (Required) | integer | The identifier of the connection.         |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                       | Type     | Description                                                                                                                                                |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| parentIdentifier           | string   | Connection group identifier. Must be ROOT if no connection group is used. Required.                                                                        |
| name                       | string   | Connection name. Required.                                                                                                                                 |
| protocol                   | string   | Connection protocol. Must be rdp. Required.                                                                                                                |
| parameters                 | object   | Parameters of the connection.                                                                                                                              |
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
| attributes                 | object   | Contains connection's information and settings.                                                                                                            |
| max-connections            | integer  | Maximum number of concurrent connections.                                                                                                                  |
| max-connections-per-user   | integer  | Maximum number of concurrent connections per user.                                                                                                         |
| weight                     | integer  | It used for weighted load balancing algorithms.                                                                                                            |
| failover-only              | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred.                                                 |
| guacd-hostname             | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                                                                        |
| guacd-port                 | integer  | Port for connecting to guacd. Default: 4822.                                                                                                               |
| guacd-encryption           | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                                                                        |

#### Example of Body
```json
{   
    "parentIdentifier": "ROOT",
    "name": "RDP-example",
    "protocol": "rdp",
    "parameters": {
        "hostname": "192.168.1.52",
        "port": "",
        "username": "test",
        "password": "test",
        "domain": "",
        "security": "",
        "disable-auth": "",
        "ignore-cert": "",
        "gateway-hostname": "",
        "gateway-port": "",
        "gateway-username": "",
        "gateway-password": "",
        "gateway-domain": "",
        "initial-program": "",
        "client-name": "",
        "server-layout": "",
        "timezone": "",
        "enable-touch": "",
        "console": "",
        "width": "",
        "height": "",
        "dpi": "",
        "color-depth": "",
        "force-lossless": "",
        "resize-method": "",
        "read-only": "",
        "normalize-clipboard": "",
        "disable-copy": "",
        "disable-paste": "",
        "console-audio": "",
        "disable-audio": "",
        "enable-audio-input": "",
        "enable-printing": "",
        "printer-name": "",
        "enable-drive": "",
        "drive-name": "",
        "disable-download": "",
        "disable-upload": "",
        "drive-path": "",
        "create-drive-path": "",
        "static-channels": "",
        "enable-wallpaper": "",
        "enable-theming": "",
        "enable-font-smoothing": "",
        "enable-full-window-drag": "",
        "enable-desktop-composition": "",
        "enable-menu-animations": "",
        "disable-bitmap-caching": "",
        "disable-offscreen-caching": "",
        "disable-glyph-caching": "",
        "disable-gfx": "",
        "remote-app": "",
        "remote-app-dir": "",
        "remote-app-args": "",
        "preconnection-id": "",
        "preconnection-blob": "",
        "load-balance-info": "",
        "recording-path": "/home/guacd/${HISTORY_UUID}",
        "recording-name": "",
        "recording-exclude-output": "",
        "recording-exclude-mouse": "",
        "recording-exclude-touch": "",
        "recording-include-keys": "",
        "create-recording-path": "true",
        "enable-sftp": "true",                                                         
        "sftp-hostname": "192.168.1.52",                        
        "sftp-port": "",                                    
        "sftp-host-key": "",                                  
        "sftp-username": "test",                           
        "sftp-password": "test",                                
        "sftp-private-key": "",                   
        "sftp-passphrase": "",                              
        "sftp-root-directory": "",                                            
        "sftp-directory": "",                               
        "sftp-server-alive-interval": "",                   
        "sftp-disable-download": "",                        
        "sftp-disable-upload": "",                                 
        "wol-send-packet": "",
        "wol-mac-addr": "",
        "wol-broadcast-addr": "",
        "wol-udp-port": "",
        "wol-wait-time": ""
    },
    "attributes": {
        "max-connections": "2",
        "max-connections-per-user": "1",
        "weight": "",
        "failover-only": "",
        "guacd-hostname": "",                          
        "guacd-port": "",
        "guacd-encryption": ""
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

## Update Telnet Connection
- Updating a Telnet connection.

### Request

#### Method
- PUT

#### Endpoint
- /api/session/data/{dataSource}/connections/{connectionIdentifier}

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |
| connectionIdentifier (Required) | integer | The identifier of the connection.         |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                      | Type     | Description                                                                                                                                            |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| parentIdentifier          | string   | Connection group identifier. Must be ROOT if no connection group is used. Required.                                                                    |
| name                      | string   | Connection name. Required.                                                                                                                             |
| protocol                  | string   | Connection protocol. Must be telnet. Required.                                                                                                         |
| parameters                | object   | Parameters of the connection.                                                                                                                          |
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
| attributes                | object   | Contains connection's information and settings.                                                                                                        |
| max-connections           | integer  | Maximum number of concurrent connections.                                                                                                              |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                                                                                     |
| weight                    | integer  | It used for weighted load balancing algorithms.                                                                                                        |
| failover-only             | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred.                                             |
| guacd-hostname            | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                                                                    |
| guacd-port                | integer  | Port for connecting to guacd. Default: 4822.                                                                                                           |
| guacd-encryption          | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                                                                    |

#### Example of Body
```json
{
    "parentIdentifier": "ROOT",                                     
    "name": "Telnet-example",                                         
    "protocol": "telnet",                                      
    "parameters": {
        "hostname": "192.168.1.52",                             
        "port": "",                                                                              
        "username": "test",                                
        "password": "test",                                     
        "username-regex": "",
        "password-regex": "",
        "login-success-regex": "",
        "login-failure-regex": "",                                  
        "color-scheme": "",                                 
        "font-name": "",                                    
        "font-size": "",                                    
        "scrollback": "",                                  
        "read-only": "",                                            
        "disable-copy": "",                                                      
        "disable-paste": "",                                                                 
        "backspace": "",                                    
        "terminal-type": "",                                
        "typescript-path": "/home/guacd/${HISTORY_UUID}",   
        "typescript-name": "",                              
        "create-typescript-path": "true",                   
        "recording-path": "/home/guacd/${HISTORY_UUID}",    
        "recording-name": "",                              
        "recording-exclude-output": "",                     
        "recording-exclude-mouse": "",                      
        "recording-include-keys": "",                      
        "create-recording-path": "true",                                             
        "wol-send-packet": "",                               
        "wol-mac-addr": "",                                 
        "wol-broadcast-addr": "",                           
        "wol-udp-port": "",                                 
        "wol-wait-time": ""                                                    
    },
    "attributes": {
        "max-connections": "2",                              
        "max-connections-per-user": "1",                    
        "weight": "",                                       
        "failover-only": "",                                
        "guacd-hostname": "",                                                          
        "guacd-port": "",                                   
        "guacd-encryption": ""                                                
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

## Update Kubernetes Connection
- Updating a Kubernetes connection.

### Request

#### Method
- PUT

#### Endpoint
- /api/session/data/{dataSource}/connections/{connectionIdentifier}

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |
| connectionIdentifier (Required) | integer | The identifier of the connection.         |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name                      | Type     | Description                                                                                                                                            |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| parentIdentifier          | string   | Connection group identifier. Must be ROOT if no connection group is used. Required.                                                                    |
| name                      | string   | Connection name. Required.                                                                                                                             |
| protocol                  | string   | Connection protocol. Must be kubernetes. Required.                                                                                                     |
| parameters                | object   | Parameters of the connection.                                                                                                                          |
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
| attributes                | object   | Contains connection's information and settings.                                                                                                        |
| max-connections           | integer  | Maximum number of concurrent connections.                                                                                                              |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                                                                                     |
| weight                    | integer  | It used for weighted load balancing algorithms.                                                                                                        |
| failover-only             | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred.                                             |
| guacd-hostname            | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                                                                    |
| guacd-port                | integer  | Port for connecting to guacd. Default: 4822.                                                                                                           |
| guacd-encryption          | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                                                                    |

#### Example of Body
```json
{
    "parentIdentifier": "ROOT",                                     
    "name": "Kubernetes-example",                                         
    "protocol": "kubernetes",                                      
    "parameters": {
        "hostname": "192.168.1.52",                             
        "port": "",                                         
        "use-ssl": "",                                     
        "ignore-cert": "",                                
        "ca-cert": "",                                                           
        "namespace": "",                                            
        "pod": "test",                                 
        "container": "",
        "exec-command": "",
        "client-cert": "",
        "client-key": "",
        "color-scheme": "",
        "font-name": "",                                 
        "font-size": "",                                    
        "scrollback": "",                                  
        "read-only": "",
        "backspace": "",
        "typescript-path": "/home/guacd/${HISTORY_UUID}",   
        "typescript-name": "",                              
        "create-typescript-path": "true",
        "recording-path": "/home/guacd/${HISTORY_UUID}",    
        "recording-name": "",                              
        "recording-exclude-output": "",                     
        "recording-exclude-mouse": "",                      
        "recording-include-keys": "",                      
        "create-recording-path": "true"                                                    
    },
    "attributes": {
        "max-connections": "2",                              
        "max-connections-per-user": "1",                    
        "weight": "",                                       
        "failover-only": "",                                
        "guacd-hostname": "",                                                          
        "guacd-port": "",                                   
        "guacd-encryption": ""                                                
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

## Delete Connection
- Deleting a connection.

### Request

#### Method
- DELETE

#### Endpoint
- /api/session/data/{dataSource}/connections/{connectionIdentifier}

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |
| connectionIdentifier (Required) | integer | The identifier of the connection.         |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

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

## Kill Active Connection
- Killing an active connection.

### Request

#### Method
- PATCH

#### Endpoint
- /api/session/data/{dataSource}/activeConnections

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |

#### Query Parameters
| Name             | Type    | Description                                                            |
| ---------------- | ------- | ---------------------------------------------------------------------- |
| token (Required) | string  | authToken. The token used to access Apache Guacamole via the REST API. |

#### Headers
| Name         | Type             |
| ------------ | ---------------- | 
| Content-Type | application/json |

#### Body
| Name     | Type    | Description                                                                                               |
| -------- | ------- | --------------------------------------------------------------------------------------------------------- |
| op       | string  | Indicates the killing of an active connection.                                                            |
| path     | string  | The path to kill an active connection and the active connection identifier (uuid) which should be killed. | 

#### Example of Body
```json
[
    {
        "op": "remove",
        "path": "/d16a2f32-6722-341b-8cfd-dbd7b9061b74"
    }
]
```

### Response

#### Normal Response Code
- 200 OK

#### Body
| Name       | Type    | Description                                                                                         |
| ---------- | ------- | --------------------------------------------------------------------------------------------------- |
| op         | string  | Indicates the killing of an active connection.                                                      |
| identifier | string  | Active connection identifier (uuid) which was killed.                                               |
| path       | string  | The path to kill an active connection and the active connection identifier (uuid) which was killed. |

#### Example of Body
```json
{
    "patches": [
        {
            "op": "remove",
            "identifier": "d16a2f32-6722-341b-8cfd-dbd7b9061b74",
            "path": "/d16a2f32-6722-341b-8cfd-dbd7b9061b74"
        }
    ]
}
```

## List Connections
- List of connections. List of all connections including their details and settings.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/connections

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
| name                      | string   | Connection name.                                                                                           |
| identifier                | integer  | Connection identifier.                                                                                     |
| parentIdentifier          | string   | Connection group identifier. Must be ROOT if no connection group is used.                                  |
| protocol                  | string   | Connection protocol.                                                                                       |
| attributes                | object   | Contains connection's information and settings.                                                            |
| guacd-encryption          | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                        |
| failover-only             | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred. |
| weight                    | integer  | It used for weighted load balancing algorithms.                                                            |
| max-connections           | integer  | Maximum number of concurrent connections.                                                                  |
| guacd-hostname            | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                        |
| guacd-port                | integer  | Port for connecting to guacd. Default: 4822.                                                               |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                                         |
| activeConnections         | integer  | Number of active connections.                                                                              |
| lastActive                | integer  | Date and time that this connection was last used, or null if this connection has never been used.          |

#### Example of Body
```json
{
    "1": {
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
        "activeConnections": 0,
        "lastActive": 1686504267000
    }
}
```

## List History of Connections
- List of history of connections.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/history/connections

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
| Name                     | Type     | Description                                                                         |
| ------------------------ | -------- | ----------------------------------------------------------------------------------- |
| startDate                | integer  | Date and time the connection began.                                                 |
| endDate                  | integer  | Date and time the connection ended, or null if the connection is still in progress. |
| remoteHost               | string   | Hostname or IP address of the remote host who performed the connection.             |
| username                 | string   | User who performed the connection.                                                  |
| active                   | boolean  | Connection status (if the connection is still in progres).                          |
| identifier               | integer  | Unique identifier assigned to this record.                                          |
| uuid                     | string   | Unique identifier assigned to this record used for the history record.              |
| attributes               | object   | All attributes associated with this record.                                         |
| logs                     | object   | All logs related to this record.                                                    |
| connectionIdentifier     | integer  | Connection identifier.                                                              |
| connectionName           | string   | Connection name.                                                                    |
| sharingProfileIdentifier | integer  | Sharing profile identifier.                                                         |
| sharingProfileName       | string   | Sharing profile name.                                                               |

#### Example of Body
```json
[
    {
        "startDate": 1686504244000,
        "endDate": 1686504244000,
        "remoteHost": "192.168.56.1",
        "username": "johnexample",
        "active": false,
        "identifier": "1",
        "uuid": "d16a2f32-6722-341b-8cfd-dbd7b9061b74",
        "attributes": {},
        "logs": {},
        "connectionIdentifier": "1",
        "connectionName": "VNC-example",
        "sharingProfileIdentifier": "1",
        "sharingProfileName": "sharingProfile-example"
    }
]
```

## List Active Connections
- List of all active connections.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/activeConnections

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |

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
| Name                     | Type     | Description                                                             |
| ------------------------ | -------- | ----------------------------------------------------------------------- |
| identifier               | string   | Active connection identifier.                                           |
| connectionIdentifier     | string   | Identifier of the connection associated with this active connection.    |
| startDate                | integer  | Date and time the connection began.                                     |
| remoteHost               | string   | Hostname or IP address of the remote host who performed the connection. |
| username                 | string   | User who performed the connection.                                      |
| connectable              | boolean  | Active connection may be connected to, just as a normal connection.     |

#### Example of Body
```json
{
    "d16a2f32-6722-341b-8cfd-dbd7b9061b74": {
        "identifier": "d16a2f32-6722-341b-8cfd-dbd7b9061b74",
        "connectionIdentifier": "1",
        "startDate": 1688983284750,
        "remoteHost": "192.168.56.1",
        "username": "johnexample",
        "connectable": true
    }
}
```

## Details of Connection
- List of details and settings about a specific connection.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/connections/{connectionIdentifier}

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |
| connectionIdentifier (Required) | integer | The identifier of the connection.         |

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
| name                      | string   | Connection name.                                                                                           |
| identifier                | integer  | Connection identifier.                                                                                     |
| parentIdentifier          | string   | Connection group identifier. Must be ROOT if no connection group is used.                                  |
| protocol                  | string   | Connection protocol.                                                                                       |
| attributes                | object   | Contains connection's information and settings.                                                            |
| guacd-encryption          | string   | Encryption method for connecting to guacd. Valid options: none, ssl. Default: none.                        |
| failover-only             | boolean  | Spar only connection. All other non-spare connections within the same balancing group should be preferred. |
| weight                    | integer  | It used for weighted load balancing algorithms.                                                            |
| max-connections           | integer  | Maximum number of concurrent connections.                                                                  |
| guacd-hostname            | string   | Hostname or IP address for connecting to guacd. Default: localhost.                                        |
| guacd-port                | integer  | Port for connecting to guacd. Default: 4822.                                                               |
| max-connections-per-user  | integer  | Maximum number of concurrent connections per user.                                                         |
| activeConnections         | integer  | Number of active connections.                                                                              |
| lastActive                | integer  | Date and time that this connection was last used, or null if this connection has never been used.          |

#### Example of Body
```json
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
    "activeConnections": 0,
    "lastActive": 1686504267000
}
```

## Details of Connection Parameters
- List of parameters of a specific connection.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/connections/{connectionIdentifier}/parameters

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |
| connectionIdentifier (Required) | integer | The identifier of the connection.         |

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
- More can be found in the specific protocols: VNC, SSH, RDP, Telnet, Kubernetes.

| Name                      | Type        | Description                                                                |
| ------------------------- | ----------- | -------------------------------------------------------------------------- |
| hostname                  | string      | IP adresa nebo hostname hostitele, ke kterému se Guacamole připojuje.      |
| password                  | string      | Heslo pro automatické přihlášení ke spojení (SFTP...).                     |
| port                      | string      | Port spojení.                                                              |
| create-recording-path     | string      | Automatické vytvoření posledního adresáře pro uložení grafického záznamuí. |
| recording-path            | string      | Cesta pro ukládání grafických záznamů.                                     |
| username                  | string      | Uživatelské jméno pro automatické přihlášení ke spojení (SFTP...).         |

#### Example of Body
```json
{
    "hostname": "192.168.1.52",
    "port": "5900",
    "password": "test",
    "recording-path": "/home/guacd/${HISTORY_UUID}",
    "create-recording-path": "true",
    "enable-sftp": "true",
    "sftp-hostname": "192.168.1.52",
    "sftp-username": "test",
    "sftp-password": "test"
}
```

## Details of Connection History
- List of details of a connection history.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/connections/{connectionIdentifier}/history

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |
| connectionIdentifier (Required) | integer | The identifier of the connection.         |

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
| Name                     | Type     | Description                                                                         |
| ------------------------ | -------- | ----------------------------------------------------------------------------------- |
| startDate                | integer  | Date and time the connection began.                                                 |
| endDate                  | integer  | Date and time the connection ended, or null if the connection is still in progress. |
| remoteHost               | string   | Hostname or IP address of the remote host who performed the connection.             |
| username                 | string   | User who performed the connection.                                                  |
| active                   | boolean  | Connection status (if the connection is still in progres).                          |
| identifier               | integer  | Unique identifier assigned to this record.                                          |
| uuid                     | string   | Unique identifier assigned to this record used for the history record.              |
| attributes               | object   | All attributes associated with this record.                                         |
| logs                     | object   | All logs related to this record.                                                    |
| connectionIdentifier     | integer  | Connection identifier.                                                              |
| connectionName           | string   | Connection name.                                                                    |
| sharingProfileIdentifier | integer  | Sharing profile identifier.                                                         |
| sharingProfileName       | string   | Sharing profile name.                                                               |

#### Example of Body
```json
[
    {
        "startDate": 1686504244000,
        "endDate": 1686504244000,
        "remoteHost": "192.168.56.1",
        "username": "johnexample",
        "active": false,
        "identifier": "1",
        "uuid": "d16a2f32-6722-341b-8cfd-dbd7b9061b74",
        "attributes": {},
        "logs": {},
        "connectionIdentifier": "1",
        "connectionName": "VNC-example",
        "sharingProfileIdentifier": "1",
        "sharingProfileName": "sharingProfile-example"
    }
]
```

## Details of Connection Sharing Profiles
- List of details of connection sharing profiles.

### Request

#### Method
- GET

#### Endpoint
- /api/session/data/{dataSource}/connections/{connectionIdentifier}/sharingProfiles

#### Path Parameters
| Name                            | Type    | Description                               |
| ------------------------------- | ------- | ----------------------------------------- |
| dataSource (Required)           | string  | The data source used by Apache Guacamole. |
| connectionIdentifier (Required) | integer | The identifier of the connection.         |

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
| name                        | string   | Sharing profile name.                                              |
| identifier                  | integer  | Sharing profile identifier.                                        |
| primaryConnectionIdentifier | string   | Identifier of the connection associated with this sharing profile. |
| attributes                  | obejct   | All attributes associated with this record.                        |

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
