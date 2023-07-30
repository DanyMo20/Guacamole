from api.tokens import create_token
from api.users import create_user
from api.user_groups import create_user_group
from api.connections import *
from api.connection_groups import create_connection_group
from api.sharing_profiles import create_sharing_profile

def test_create_token():
    response = create_token()
    assert response.status_code == 200

def test_create_user():
    expected_data = {
        "username": f"{USERNAME}",
        "password": "1234",
        "attributes": {
            "guac-email-address": "johnexample@email.com",
            "guac-organizational-role": "Tester",
            "guac-full-name": "John Example",
            "expired": "true",
            "timezone": "Europe/Prague",
            "access-window-start": "12:22:00",
            "guac-organization": "Example",
            "access-window-end": "15:55:00",
            "disabled": "false",
            "valid-until": "2026-06-30",
            "valid-from": "2023-05-25"
        }
    }
    response = create_user()
    assert response.status_code == 200
    assert response.json() == expected_data

def test_create_user_group():
    user_group_expected_data = {
        "identifier": f"{USER_GROUP_IDENTIFIER}",
        "attributes": {
            "disabled": "false"
        }
    }
    member_user_group_expected_data = {
        "identifier": f"{MEMBER_USER_GROUP_IDENTIFIER}",
        "attributes": {
            "disabled": "false"
        }
    }
    parent_user_group_expected_data = {
        "identifier": f"{PARENT_USER_GROUP_IDENTIFIER}",
        "attributes": {
            "disabled": "false"
        }
    }
    user_group_response = create_user_group(USER_GROUP_IDENTIFIER)
    member_user_group_response = create_user_group(MEMBER_USER_GROUP_IDENTIFIER)
    parent_user_group_response = create_user_group(PARENT_USER_GROUP_IDENTIFIER)
    assert user_group_response.status_code == 200
    assert member_user_group_response.status_code == 200
    assert parent_user_group_response.status_code == 200
    assert user_group_response.json() == user_group_expected_data
    assert member_user_group_response.json() == member_user_group_expected_data
    assert parent_user_group_response.json() == parent_user_group_expected_data

def test_create_vnc_connection():
    response = create_vnc_connection()
    assert response.status_code == 200
    assert response.json()["name"] == CONNECTION_NAME_VNC
    assert response.json()["protocol"] == "vnc"

def test_create_ssh_connection():
    response = create_ssh_connection()
    assert response.status_code == 200
    assert response.json()["name"] == CONNECTION_NAME_SSH
    assert response.json()["protocol"] == "ssh"

def test_create_rdp_connection():
    response = create_rdp_connection()
    assert response.status_code == 200
    assert response.json()["name"] == CONNECTION_NAME_RDP
    assert response.json()["protocol"] == "rdp"         

def test_create_telnet_connection():
    response = create_telnet_connection()
    assert response.status_code == 200
    assert response.json()["name"] == CONNECTION_NAME_TELNET
    assert response.json()["protocol"] == "telnet"

def test_create_kubernetes_connection():
    response = create_kubernetes_connection()
    assert response.status_code == 200
    assert response.json()["name"] == CONNECTION_NAME_KUBERNETES
    assert response.json()["protocol"] == "kubernetes"    
    
def test_create_connection_group():
    response = create_connection_group()
    assert response.status_code == 200
    assert response.json()["name"] == CONNECTION_GROUP_NAME
        
def test_create_sharing_profile():
    response = create_sharing_profile()
    assert response.status_code == 200
    assert response.json()["name"] == SHARING_PROFILE_NAME
