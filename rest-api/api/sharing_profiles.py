from api.config import *
from api.functions import *
from api.connections import get_connection_identifier_from_connection_name

# Creating a sharing profile.
def create_sharing_profile():
    json = {
        "name": f"{SHARING_PROFILE_NAME}",
        "primaryConnectionIdentifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
        "parameters": {
            "read-only": "true"
        },
        "attributes": {}
    }  
    return request_post(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/sharingProfiles", json)

# Updating a sharing profile.
def update_sharing_profile(sharing_profile_identifier):
    json = {
        "name": f"{SHARING_PROFILE_NAME}",
        "primaryConnectionIdentifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
        "parameters": {
            "read-only": "false"
        },
        "attributes": {}
    }
    return request_put(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/sharingProfiles/{sharing_profile_identifier}", json)

# Deleting a sharing profile.
def delete_sharing_profile(sharing_profile_identifier):
    return request_delete(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/sharingProfiles/{sharing_profile_identifier}")

# List of all sharing profiles.
def list_sharing_profiles():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/sharingProfiles")

# List of details about a specific sharing profile.
def details_of_sharing_profile(sharingProfileIdentifier):
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/sharingProfiles/{sharingProfileIdentifier}")

# Getting a sharing profile identifier from a sharing profile name and from a connection identifier.
def get_sharing_profile_identifier_from_sharing_profile_name(sharing_profile_name, primary_connection_identifier):
    for sharing_profile_identifier, sharing_profile_data in list_sharing_profiles().json().items():
        if sharing_profile_name == sharing_profile_data['name'] and primary_connection_identifier == sharing_profile_data['primaryConnectionIdentifier']:               
            return sharing_profile_identifier