from api.sharing_profiles import *
from api.connections import get_connection_identifier_from_connection_name

def test_update_sharing_profile():
    response = update_sharing_profile(get_sharing_profile_identifier_from_sharing_profile_name(SHARING_PROFILE_NAME, get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)))
    assert response.status_code == 204 

def test_list_sharing_profiles():
    expected_data = {
        "name": f"{SHARING_PROFILE_NAME}",
        "identifier": f"{get_sharing_profile_identifier_from_sharing_profile_name(SHARING_PROFILE_NAME, get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC))}",
        "primaryConnectionIdentifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
        "attributes": {}
    }
    response = list_sharing_profiles()
    assert response.status_code == 200
    assert response.json()[f"{get_sharing_profile_identifier_from_sharing_profile_name(SHARING_PROFILE_NAME, get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC))}"] == expected_data

def test_details_of_sharing_profile():
    expected_data = {
        "name": f"{SHARING_PROFILE_NAME}",
        "identifier": f"{get_sharing_profile_identifier_from_sharing_profile_name(SHARING_PROFILE_NAME, get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC))}",
        "primaryConnectionIdentifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
        "attributes": {}
    }
    response = details_of_sharing_profile(get_sharing_profile_identifier_from_sharing_profile_name(SHARING_PROFILE_NAME, get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)))
    assert response.status_code == 200 
    assert response.json() == expected_data


