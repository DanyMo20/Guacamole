from api.tokens import delete_token
from api.users import delete_user
from api.user_groups import delete_user_group
from api.connections import *
from api.connection_groups import *
from api.sharing_profiles import *

def test_delete_token():
    response = delete_token()
    assert response.status_code == 204
      
def test_delete_user():
    response = delete_user()
    assert response.status_code == 204  

def test_delete_user_group():
    user_group_response = delete_user_group(USER_GROUP_IDENTIFIER)
    member_user_group_response = delete_user_group(MEMBER_USER_GROUP_IDENTIFIER)
    parent_user_group_response = delete_user_group(PARENT_USER_GROUP_IDENTIFIER) 
    assert user_group_response.status_code == 204
    assert member_user_group_response.status_code == 204
    assert parent_user_group_response.status_code == 204

def test_delete_sharing_profile():
    response = delete_sharing_profile(get_sharing_profile_identifier_from_sharing_profile_name(SHARING_PROFILE_NAME, get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)))
    assert response.status_code == 204

def test_delete_connection():
    vnc_response = delete_connection(get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC))
    ssh_response = delete_connection(get_connection_identifier_from_connection_name(CONNECTION_NAME_SSH))
    rdp_response = delete_connection(get_connection_identifier_from_connection_name(CONNECTION_NAME_RDP))
    telnet_response = delete_connection(get_connection_identifier_from_connection_name(CONNECTION_NAME_TELNET))
    kubernetes_response = delete_connection(get_connection_identifier_from_connection_name(CONNECTION_NAME_KUBERNETES))
    assert vnc_response.status_code == 204
    assert ssh_response.status_code == 204
    assert rdp_response.status_code == 204
    assert telnet_response.status_code == 204
    assert kubernetes_response.status_code == 204   

def test_delete_connection_group():
    response = delete_connection_group(get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME))
    assert response.status_code == 204    
         