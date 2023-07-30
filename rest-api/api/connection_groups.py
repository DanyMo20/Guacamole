from api.config import *
from api.functions import *

# Creating a connection group.
def create_connection_group():
    json = {
        "name": f"{CONNECTION_GROUP_NAME}",
        "parentIdentifier": "ROOT",
        "type": "ORGANIZATIONAL",
        "attributes": {
            "max-connections": "5",
            "max-connections-per-user": "1",
            "enable-session-affinity": ""
        }
    }  
    return request_post(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connectionGroups", json)

# Updating a connection group.
def update_connection_group(connection_group_identifier):
    json = {
        "name": f"{CONNECTION_GROUP_NAME}",
        "parentIdentifier": "ROOT",
        "type": "ORGANIZATIONAL",
        "attributes": {
            "max-connections": "5",
            "max-connections-per-user": "2",
            "enable-session-affinity": ""
        }
    }  
    return request_put(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connectionGroups/{connection_group_identifier}", json)

# Deleting a connection group.
def delete_connection_group(connection_group_identifier):
    return request_delete(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connectionGroups/{connection_group_identifier}")

# List of connection groups. List of all connection groups including their details and settings.
def list_connection_groups():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connectionGroups")

# List of connections and connection groups. List of all connection and connection groups including their details and settings.
def list_connections_and_connection_groups():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connectionGroups/ROOT/tree")

# List of details and settings about a specific connection group.
def details_of_connection_group(connection_group_identifier):
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/connectionGroups/{connection_group_identifier}")

# Getting a connection group identifier from a connection group name.
def get_connection_group_identifier_from_connection_group_name(connection_group_name):
    for connection_group_identifier, connection_group_data in list_connection_groups().json().items():
        if connection_group_name == connection_group_data['name']:               
            return connection_group_identifier