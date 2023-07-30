from api.users import *

def test_update_user():
    response = update_user()
    assert response.status_code == 204  

def test_change_user_password():
    response = change_user_password()
    assert response.status_code == 204

def test_assign_permissions_to_user():
    response = assign_permissions_to_user()
    assert response.status_code == 204

def test_assign_user_to_user_group():
    response = assign_user_to_user_group()
    assert response.status_code == 204

def test_list_users_user_groups():
    expected_data = f"{USER_GROUP_IDENTIFIER}"
    response = list_users_user_groups()
    assert response.status_code == 200
    assert expected_data in response.json()   

def test_assign_user_to_connection():
    response = assign_user_to_connection()
    assert response.status_code == 204

def test_assign_user_to_connection_group():
    response = assign_user_to_connection_group()
    assert response.status_code == 204  

def test_details_of_user_permissions():
    expected_data_connections = [
        "READ"
    ]
    expected_data_users = [
        "READ",
        "UPDATE"
    ]
    expected_data_system_permissions = [
        "CREATE_USER",
        "CREATE_USER_GROUP",
        "CREATE_CONNECTION",
        "CREATE_CONNECTION_GROUP",
        "CREATE_SHARING_PROFILE",
        "ADMINISTER"
    ]
    response = details_of_user_permissions()
    assert response.status_code == 200
    assert response.json()["connectionPermissions"][f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}"] == expected_data_connections
    assert response.json()["connectionGroupPermissions"][f"{get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME)}"] == expected_data_connections
    assert response.json()["userPermissions"][f"{USERNAME}"] == expected_data_users
    assert response.json()["systemPermissions"] == expected_data_system_permissions

def test_details_of_user_effective_permissions():
    expected_data_connections = [
        "READ"
    ]
    expected_data_users = [
        "READ",
        "UPDATE"
    ]
    expected_data_system_permissions = [
        "CREATE_USER",
        "CREATE_USER_GROUP",
        "CREATE_CONNECTION",
        "CREATE_CONNECTION_GROUP",
        "CREATE_SHARING_PROFILE",
        "ADMINISTER"
    ]
    response = details_of_user_effective_permissions()
    assert response.status_code == 200
    assert response.json()["connectionPermissions"][f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}"] == expected_data_connections
    assert response.json()["connectionGroupPermissions"][f"{get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME)}"] == expected_data_connections
    assert response.json()["userPermissions"][f"{USERNAME}"] == expected_data_users
    assert response.json()["systemPermissions"] == expected_data_system_permissions

def test_revoke_permissions_from_user():
    response = revoke_permissions_from_user()
    assert response.status_code == 204

def test_revoke_user_from_user_group():
    response = revoke_user_from_user_group()
    assert response.status_code == 204

def test_revoke_user_from_connection():
    response = revoke_user_from_connection()
    assert response.status_code == 204

def test_revoke_user_from_connection_group():
    response = revoke_user_from_connection_group()
    assert response.status_code == 204

def test_list_users():
    expected_data = {
        "username": f"{USERNAME}",
        "attributes": {
            "guac-email-address": "johnexample@email.com",
            "guac-organizational-role": "Developer",
            "guac-full-name": "John Example",
            "expired": "true",
            "timezone": "Europe/Prague",
            "access-window-start": "12:22:00",
            "guac-organization": "Example",
            "access-window-end": "15:55:00",
            "disabled": None,
            "valid-until": "2026-06-30",
            "valid-from": "2023-05-25"
        }
    }
    response = list_users()
    assert response.status_code == 200
    assert f"{USERNAME}" in response.json()
    assert response.json()[f"{USERNAME}"] == expected_data

def test_list_history_of_users():
    response = list_history_of_users()
    assert response.status_code == 200

def test_details_of_user():
    expected_data = {
        "username": f"{USERNAME}",
        "attributes": {
            "guac-email-address": "johnexample@email.com",
            "guac-organizational-role": "Developer",
            "guac-full-name": "John Example",
            "expired": "true",
            "timezone": "Europe/Prague",
            "access-window-start": "12:22:00",
            "guac-organization": "Example",
            "access-window-end": "15:55:00",
            "disabled": None,
            "valid-until": "2026-06-30",
            "valid-from": "2023-05-25"
        }
    }
    response = details_of_user()
    assert response.status_code == 200
    assert response.json() == expected_data

def test_details_of_self():
    response = details_of_self()
    assert response.status_code == 200
    assert response.json()["username"] == AUTH_USERNAME

def test_details_of_user_history():
    response = details_of_user_history()
    assert response.status_code == 200
    for username in response.json():
        assert username["username"] == USERNAME
        assert username["username"] == AUTH_USERNAME
        
