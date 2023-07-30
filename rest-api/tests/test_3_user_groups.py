from api.user_groups import *

def test_update_user_group():
    response = update_user_group()
    assert response.status_code == 204

def test_assign_permissions_to_user_group():
    response = assign_permissions_to_user_group()
    assert response.status_code == 204

def test_assign_member_user_to_user_group():
    response = assign_member_user_to_user_group()
    assert response.status_code == 204

def test_assign_member_user_group_to_user_group(): 
    response = assign_member_user_group_to_user_group()
    assert response.status_code == 204

def test_assign_parent_user_group_to_user_group(): 
    response = assign_parent_user_group_to_user_group()
    assert response.status_code == 204

def test_assign_user_group_to_connection():
    response = assign_user_group_to_connection()
    assert response.status_code == 204

def test_assign_user_group_to_connection_group():
    response = assign_user_group_to_connection_group()
    assert response.status_code == 204

def test_details_of_user_group_permissions():
    expected_data = [
        "READ"
    ]
    expected_data_system_permissions = [
        "CREATE_USER",
        "CREATE_USER_GROUP",
        "CREATE_CONNECTION",
        "CREATE_CONNECTION_GROUP",
        "CREATE_SHARING_PROFILE",
        "ADMINISTER"
    ]
    response = details_of_user_group_permissions()
    assert response.status_code == 200
    assert response.json()["connectionPermissions"][f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}"] == expected_data
    assert response.json()["connectionGroupPermissions"][f"{get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME)}"] == expected_data
    assert response.json()["systemPermissions"] == expected_data_system_permissions

def test_revoke_permissions_from_user_group():
    response = revoke_permissions_from_user_group()
    assert response.status_code == 204    

def test_revoke_member_user_from_user_group():
    response = revoke_member_user_from_user_group()
    assert response.status_code == 204 

def test_revoke_member_user_group_from_user_group():
    response = revoke_member_user_group_from_user_group()
    assert response.status_code == 204 

def test_revoke_parent_user_group_from_user_group():
    response = revoke_parent_user_group_from_user_group()
    assert response.status_code == 204

def test_revoke_user_group_from_connection():
    response = revoke_user_group_from_connection()
    assert response.status_code == 204

def test_revoke_user_group_from_connection_group():
    response = revoke_user_group_from_connection_group()
    assert response.status_code == 204

def test_list_user_groups():
    expected_data = {
            "identifier": f"{USER_GROUP_IDENTIFIER}",
            "attributes": {
                "disabled": None
            }
        }
    response = list_user_groups()
    assert response.status_code == 200
    assert f"{USER_GROUP_IDENTIFIER}" in response.json()
    assert response.json()[f"{USER_GROUP_IDENTIFIER}"] == expected_data

def test_details_of_user_group():
    expected_data = {
            "identifier": f"{USER_GROUP_IDENTIFIER}",
            "attributes": {
                "disabled": None
            }
        }
    response = details_of_user_group()
    assert response.status_code == 200
    assert response.json() == expected_data


