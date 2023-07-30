from api.config import *
from api.functions import *

# Creating a VNC connection.
def create_vnc_connection():
    json = {
        "parentIdentifier": "ROOT",                                               
        "name": CONNECTION_NAME_VNC,                                        
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
    return request_post(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections", json)

# Creating a SSH connection.
def create_ssh_connection():
    json = {
        "parentIdentifier": "ROOT",                                     
        "name": CONNECTION_NAME_SSH,                                         
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
    return request_post(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections", json)

# Creating a RDP connection.
def create_rdp_connection():
    json = {   
        "parentIdentifier": "ROOT",
        "name": CONNECTION_NAME_RDP,
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
    return request_post(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections", json)

# Creating a Telnet connection.
def create_telnet_connection():
    json = {
        "parentIdentifier": "ROOT",                                     
        "name": CONNECTION_NAME_TELNET,                                         
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
    return request_post(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections", json)

# Creating a Kubernetes connection.
def create_kubernetes_connection():
    json = {
        "parentIdentifier": "ROOT",                                     
        "name": CONNECTION_NAME_KUBERNETES,                                         
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
    return request_post(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections", json)

# Updating a VNC connection.
def update_vnc_connection():
    json = {
        "parentIdentifier": "ROOT",                                               
        "name": CONNECTION_NAME_VNC,                                        
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
    return request_put(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections/{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}", json)

# Updating a SSH connection.
def update_ssh_connection():
    json = {
        "parentIdentifier": "ROOT",                                     
        "name": CONNECTION_NAME_SSH,                                         
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
    return request_put(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections/{get_connection_identifier_from_connection_name(CONNECTION_NAME_SSH)}", json)

# Updating a RDP connection.
def update_rdp_connection():
    json = {   
        "parentIdentifier": "ROOT",
        "name": CONNECTION_NAME_RDP,
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
    return request_put(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections/{get_connection_identifier_from_connection_name(CONNECTION_NAME_RDP)}", json)

# Updating a Telnet connection.
def update_telnet_connection():
    json = {
        "parentIdentifier": "ROOT",                                     
        "name": CONNECTION_NAME_TELNET,                                         
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
    return request_put(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections/{get_connection_identifier_from_connection_name(CONNECTION_NAME_TELNET)}", json)

# Updating a Kubernetes connection.
def update_kubernetes_connection():
    json = {
        "parentIdentifier": "ROOT",                                     
        "name": CONNECTION_NAME_KUBERNETES,                                         
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
    return request_put(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections/{get_connection_identifier_from_connection_name(CONNECTION_NAME_KUBERNETES)}", json)

# Deleting a connection.
def delete_connection(connection_identifier):
    return request_delete(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections/{connection_identifier}")

# Killing an active connection.
def kill_active_connection(active_connection_identifier):
    json = [
        {
            "op": "remove",
            "path": f"/{active_connection_identifier}"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/activeConnections", json)

# List of connections. List of all connections including their details and settings.
def list_connections():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections")

# List of history of connections.
def list_history_of_connections():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/history/connections")

# List of all active connections.
def list_active_connections():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/activeConnections")

# List of details and settings about a specific connection.
def details_of_connection(connection_identifier):
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections/{connection_identifier}")

# List of parameters of a specific connection.
def details_of_connection_parameters(connection_identifier):
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections/{connection_identifier}/parameters")

# List of details of a connection history.
def details_of_connection_history(connection_identifier):
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections/{connection_identifier}/history")

# List of details of connection sharing profiles.
def details_of_connection_sharing_profiles(connection_identifier):
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connections/{connection_identifier}/sharingProfiles")

# Getting a connection identifier from a connection name.
def get_connection_identifier_from_connection_name(connection_name):
    for connection_identifier, connection_data in list_connections().json().items():
        if connection_name == connection_data['name']:               
            return connection_identifier