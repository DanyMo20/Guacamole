from api.connections import *
from api.sharing_profiles import get_sharing_profile_identifier_from_sharing_profile_name

def test_update_vnc_connection():
    response = update_vnc_connection()
    assert response.status_code == 204

def test_update_ssh_connection():
    response = update_ssh_connection()
    assert response.status_code == 204

def test_update_rdp_connection():
    response = update_rdp_connection()
    assert response.status_code == 204         

def test_update_telnet_connection():
    response = update_telnet_connection()
    assert response.status_code == 204

def test_update_kubernetes_connection():
    response = update_kubernetes_connection()
    assert response.status_code == 204

# TODO How to test?
# def test_kill_active_connection():
#     response = kill_active_connection(activeConnectionIdentifier)
#     assert response.status_code == 200

def test_list_connections():
    expected_data_vnc = {
        "name": f"{CONNECTION_NAME_VNC}",
        "identifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
        "parentIdentifier": "ROOT",
        "protocol": "vnc",
        "attributes": {
            "failover-only": None,
            "guacd-encryption": None,
            "weight": None,
            "max-connections": "2",
            "guacd-hostname": None,
            "guacd-port": None,
            "max-connections-per-user": "1"
        },
        "activeConnections": 0
    }
    expected_data_ssh = {
        "name": f"{CONNECTION_NAME_SSH}",
        "identifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_SSH)}",
        "parentIdentifier": "ROOT",
        "protocol": "ssh",
        "attributes": {
            "failover-only": None,
            "guacd-encryption": None,
            "weight": None,
            "max-connections": "2",
            "guacd-hostname": None,
            "guacd-port": None,
            "max-connections-per-user": "1"
        },
        "activeConnections": 0
    }
    expected_data_rdp = {
        "name": f"{CONNECTION_NAME_RDP}",
        "identifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_RDP)}",
        "parentIdentifier": "ROOT",
        "protocol": "rdp",
        "attributes": {
            "failover-only": None,
            "guacd-encryption": None,
            "weight": None,
            "max-connections": "2",
            "guacd-hostname": None,
            "guacd-port": None,
            "max-connections-per-user": "1"
        },
        "activeConnections": 0
    }
    expected_data_telnet = {
        "name": f"{CONNECTION_NAME_TELNET}",
        "identifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_TELNET)}",
        "parentIdentifier": "ROOT",
        "protocol": "telnet",
        "attributes": {
            "failover-only": None,
            "guacd-encryption": None,
            "weight": None,
            "max-connections": "2",
            "guacd-hostname": None,
            "guacd-port": None,
            "max-connections-per-user": "1"
        },
        "activeConnections": 0
    }
    expected_data_kubernetes = {
        "name": f"{CONNECTION_NAME_KUBERNETES}",
        "identifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_KUBERNETES)}",
        "parentIdentifier": "ROOT",
        "protocol": "kubernetes",
        "attributes": {
            "failover-only": None,
            "guacd-encryption": None,
            "weight": None,
            "max-connections": "2",
            "guacd-hostname": None,
            "guacd-port": None,
            "max-connections-per-user": "1"
        },
        "activeConnections": 0
    }

    response = list_connections()
    assert response.status_code == 200
    assert response.json()[f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}"] == expected_data_vnc
    assert response.json()[f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_SSH)}"] == expected_data_ssh
    assert response.json()[f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_RDP)}"] == expected_data_rdp
    assert response.json()[f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_TELNET)}"] == expected_data_telnet
    assert response.json()[f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_KUBERNETES)}"] == expected_data_kubernetes

# TODO
def test_list_history_of_connections():
    response = list_history_of_connections()
    assert response.status_code == 200

# TODO
def test_list_active_connections():
    response = list_active_connections()
    assert response.status_code == 200    

def test_details_of_connection():
    expected_data_vnc = {
        "name": f"{CONNECTION_NAME_VNC}",
        "identifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
        "parentIdentifier": "ROOT",
        "protocol": "vnc",
        "attributes": {
            "failover-only": None,
            "guacd-encryption": None,
            "weight": None,
            "max-connections": "2",
            "guacd-hostname": None,
            "guacd-port": None,
            "max-connections-per-user": "1"
        },
        "activeConnections": 0
    }
    response = details_of_connection(get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC))
    assert response.status_code == 200 
    assert response.json() == expected_data_vnc

def test_details_of_connection_parameters():
    expected_data_vnc = {
        "hostname": "192.168.1.52",
        "port": "5900",
        "password": "test",
        "recording-path": "/home/guacd/${HISTORY_UUID}",
        "create-recording-path": "true",
        "enable-sftp": "true",
        "sftp-hostname": "192.168.1.52",
        "sftp-username": "test",
        "sftp-password": "test"
    }
    response = details_of_connection_parameters(get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC))
    assert response.status_code == 200
    assert response.json() == expected_data_vnc

def test_details_of_connection_history():
    expected_data_vnc = []
    response = details_of_connection_history(get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC))
    assert response.status_code == 200
    assert response.json() == expected_data_vnc

def test_details_of_connection_sharing_profiles():
    expected_data = {
        "name": f"{SHARING_PROFILE_NAME}",
        "identifier": f"{get_sharing_profile_identifier_from_sharing_profile_name(SHARING_PROFILE_NAME, get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC))}",
        "primaryConnectionIdentifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
        "attributes": {}
    }
    response = details_of_connection_sharing_profiles(get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC))
    assert response.status_code == 200
    assert response.json()[f"{get_sharing_profile_identifier_from_sharing_profile_name(SHARING_PROFILE_NAME, get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC))}"] == expected_data





           