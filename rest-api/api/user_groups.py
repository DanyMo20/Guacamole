from api.config import *
from api.functions import *
from api.connections import get_connection_identifier_from_connection_name
from api.connection_groups import get_connection_group_identifier_from_connection_group_name

# Creating a user group.
def create_user_group(user_group_identifier):
    json = {
        "identifier": user_group_identifier,
        "attributes": {
            "disabled": "false"
        }
    }    
    return request_post(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups", json)

# Updating a user group.
def update_user_group():
    json = {
        "identifier": f"{USER_GROUP_IDENTIFIER}",
        "attributes": {
            "disabled": "false"
        }
    }    
    return request_put(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}", json)

# Deleting a user group.
def delete_user_group(user_group_identifier):
    return request_delete(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{user_group_identifier}")

# Assigning permissions to a user group.
def assign_permissions_to_user_group():
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
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/permissions", json)

# Assigning a member user to a user group.
def assign_member_user_to_user_group():
    json = [
        {
            "op": "add",
            "path": "/",
            "value": f"{USERNAME}"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/memberUsers", json)

# Assigning a member user group to a user group. A member user group will inherit the permissions of the parent user group.
def assign_member_user_group_to_user_group():
    json = [
        {
            "op": "add",
            "path": "/",
            "value": f"{MEMBER_USER_GROUP_IDENTIFIER}"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/memberUserGroups", json)

# Assigning a parent user group to a user group. A member user group will inherit the permissions of the parent user group.
def assign_parent_user_group_to_user_group():
    json = [
        {
            "op": "add",
            "path": "/",
            "value": f"{PARENT_USER_GROUP_IDENTIFIER}"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/userGroups", json)

# Assigning a user group to a connection.
def assign_user_group_to_connection():
    json = [
        {
            "op": "add",
            "path": f"/connectionPermissions/{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
            "value": "READ"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/permissions", json)

# Assigning a user group to a connection group.
def assign_user_group_to_connection_group():
    json = [
        {
            "op": "add",
            "path": f"/connectionGroupPermissions/{get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME)}",
            "value": "READ"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/permissions", json)

# Revoking permissions from a user group.
def revoke_permissions_from_user_group():
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
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/permissions", json)

# Revoking a member user from a user group.
def revoke_member_user_from_user_group():
    json = [
        {
            "op": "remove",
            "path": "/",
            "value": f"{USERNAME}"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/memberUsers", json)

# Revoking a member user group from a user group.
def revoke_member_user_group_from_user_group():
    json = [
        {
            "op": "remove",
            "path": "/",
            "value": f"{MEMBER_USER_GROUP_IDENTIFIER}"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/memberUserGroups", json)

# Revoking a parent user group from a user group.
def revoke_parent_user_group_from_user_group():
    json = [
        {
            "op": "remove",
            "path": "/",
            "value": f"{PARENT_USER_GROUP_IDENTIFIER}"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/userGroups", json)

# Revoking a user group from a connection.
def revoke_user_group_from_connection():
    json = [
        {
            "op": "remove",
            "path": f"/connectionPermissions/{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
            "value": "READ"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/permissions", json)

# Revoking a user group from a connection group.
def revoke_user_group_from_connection_group():
    json = [
        {
            "op": "remove",
            "path": f"/connectionGroupPermissions/{get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME)}",
            "value": "READ"
        }
    ]
    return request_patch(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/permissions", json)

# List of all user groups.
def list_user_groups():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups")

# List of details and settings about a specific user group.
def details_of_user_group():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}")

# List of details of user group permissions.
def details_of_user_group_permissions():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/userGroups/{USER_GROUP_IDENTIFIER}/permissions")
