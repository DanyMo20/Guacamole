from api.config import *
from api.functions import *
from api.connections import get_connection_identifier_from_connection_name
from api.connection_groups import get_connection_group_identifier_from_connection_group_name

# Creating a Guacamole user.
def create_user():
    json = {
        "username": f"{USERNAME}",                           
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
    return request_post(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users", json)

# Updating a user except the password.
def update_user():
    json = {
        "username": f"{USERNAME}",                                            
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
    return request_put(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}", json)

# Changing the user password.
def change_user_password():
    json = {
        "oldPassword": "1234",
        "newPassword": "abcd"
    }   
    return request_put(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/password", json)

# Deleting a user.
def delete_user():
    return request_delete(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}")

# Assigning permissions to a user.
def assign_permissions_to_user():
    json = [
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
            "path": f"/userPermissions/{USERNAME}",
            "value": "UPDATE"
        }
    ] 
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/permissions", json)

# Assigning a user to a user group.
def assign_user_to_user_group():
    json = [
        {
            "op": "add",
            "path": "/",
            "value": f"{USER_GROUP_IDENTIFIER}"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/userGroups", json)

# Assigning a user to a connection.
def assign_user_to_connection():
    json = [
        {
            "op": "add",
            "path": f"/connectionPermissions/{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
            "value": "READ"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/permissions", json)

# Assigning a user to a connection group.
def assign_user_to_connection_group():
    json = [
        {
            "op": "add",
            "path": f"/connectionGroupPermissions/{get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME)}",
            "value": "READ"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/permissions", json)

# Revoking permissions from a user.
def revoke_permissions_from_user():
    json = [
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
            "path": f"/userPermissions/{USERNAME}",
            "value": "UPDATE"
        }
    ] 
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/permissions", json)

# Revoking a user from a user group.
def revoke_user_from_user_group():
    json = [
        {
            "op": "remove",
            "path": "/",
            "value": f"{USER_GROUP_IDENTIFIER}"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/userGroups", json)

# Revoking a user from a connection.
def revoke_user_from_connection():
    json = [
        {
            "op": "remove",
            "path": f"/connectionPermissions/{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
            "value": "READ"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/permissions", json)

# Revoking a user from a connection group.
def revoke_user_from_connection_group():
    json = [
        {
            "op": "remove",
            "path": f"/connectionGroupPermissions/{get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME)}",
            "value": "READ"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/permissions", json)

# List of users. List of all users including their details and settings.
def list_users():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users")

# List of history of users.
def list_history_of_users():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/history/users")

# List of user groups to which the user is assigned.
def list_users_user_groups():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/userGroups")

# List of details and settings about a specific user.
def details_of_user():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}")

# List of details about self.
def details_of_self():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/self")

# List of details of user permissions.    
def details_of_user_permissions():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/permissions")

# List of details of user effective permissions.
def details_of_user_effective_permissions():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/effectivePermissions")

# Details of user history.
def details_of_user_history():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/users/{USERNAME}/history")
