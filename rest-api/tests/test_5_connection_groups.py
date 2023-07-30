from api.connection_groups import *
from api.connections import get_connection_identifier_from_connection_name
from api.sharing_profiles import get_sharing_profile_identifier_from_sharing_profile_name

def test_update_connection_group():
    response = update_connection_group(get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME))
    assert response.status_code == 204 

def test_list_connection_groups():
    expected_data = {
        "name": f"{CONNECTION_GROUP_NAME}",
        "identifier": f"{get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME)}",
        "parentIdentifier": "ROOT",
        "type": "ORGANIZATIONAL",
        "activeConnections": 0,
        "attributes": {
            "max-connections": "5",
            "max-connections-per-user": "2",
            "enable-session-affinity": ""
        }
    }
    response = list_connection_groups()
    assert response.status_code == 200
    assert response.json()[f"{get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME)}"] == expected_data

def test_list_connections_and_connection_groups():
    expected_data_connection_group = {
        "name": f"{CONNECTION_GROUP_NAME}",
        "identifier": f"{get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME)}",
        "parentIdentifier": "ROOT",
        "type": "ORGANIZATIONAL",
        "activeConnections": 0,
        "attributes": {
            "max-connections": "5",
            "max-connections-per-user": "2",
            "enable-session-affinity": ""
        }
    }
    expected_data_vnc = {
        "name": f"{CONNECTION_NAME_VNC}",
        "identifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
        "parentIdentifier": "ROOT",
        "protocol": "vnc",
        "attributes": {
            "guacd-encryption": None,
            "failover-only": None,
            "weight": None,
            "max-connections": "2",
            "guacd-hostname": None,
            "guacd-port": None,
            "max-connections-per-user": "1"
        },
        "sharingProfiles": [
            {
                "name": f"{SHARING_PROFILE_NAME}",
                "identifier": f"{get_sharing_profile_identifier_from_sharing_profile_name(SHARING_PROFILE_NAME, get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC))}",
                "primaryConnectionIdentifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_VNC)}",
                "attributes": {                
                }
            }
        ],
        "activeConnections": 0
    }
    expected_data_ssh = {
        "name": f"{CONNECTION_NAME_SSH}",
        "identifier": f"{get_connection_identifier_from_connection_name(CONNECTION_NAME_SSH)}",
        "parentIdentifier": "ROOT",
        "protocol": "ssh",
        "attributes": {
            "guacd-encryption": None,
            "failover-only": None,
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
            "guacd-encryption": None,
            "failover-only": None,
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
            "guacd-encryption": None,
            "failover-only": None,
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
        "parentIdentifier":"ROOT",
        "protocol": "kubernetes",
        "attributes": {
            "guacd-encryption": None,
            "failover-only": None,
            "weight": None,
            "max-connections": "2",
            "guacd-hostname": None,
            "guacd-port": None,
            "max-connections-per-user": "1"
        },
        "activeConnections": 0
    }
    response = list_connections_and_connection_groups()
    assert response.status_code == 200
    assert expected_data_connection_group in response.json()["childConnectionGroups"]
    assert expected_data_vnc in response.json()["childConnections"]
    assert expected_data_ssh in response.json()["childConnections"]
    assert expected_data_rdp in response.json()["childConnections"]
    assert expected_data_telnet in response.json()["childConnections"]
    assert expected_data_kubernetes in response.json()["childConnections"]

def test_details_of_connection_group():
    expected_data = {
        "name": f"{CONNECTION_GROUP_NAME}",
        "identifier": f"{get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME)}",
        "parentIdentifier": "ROOT",
        "type": "ORGANIZATIONAL",
        "activeConnections": 0,
        "attributes": {
            "max-connections": "5",
            "max-connections-per-user": "2",
            "enable-session-affinity": ""
        }
    }
    response = details_of_connection_group(get_connection_group_identifier_from_connection_group_name(CONNECTION_GROUP_NAME))
    assert response.status_code == 200
    assert response.json() == expected_data
    
