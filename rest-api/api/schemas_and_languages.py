from api.config import *
from api.functions import *

# List of all user attributes.
def list_user_attributes():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/schema/userAttributes")

# List of all user group attributes.
def list_user_group_attributes():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/schema/userGroupAttributes")

# List of all connection attributes.
def list_connection_attributes():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/schema/connectionAttributes")

# List of all connection group attributes.
def list_connection_group_attributes():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/schema/connectionGroupAttributes")

# List of all sharing profile attributes.
def list_sharing_profile_attributes():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/schema/sharingProfileAttributes")

# List of attributes of all protocols.
def list_protocol_attributes():
    return request_get(ENDPOINT + f"/api/session/data/{DATA_SOURCE}/schema/protocols")

# List of all available languages.
def list_languages():
    return request_get(ENDPOINT + f"/api/languages")