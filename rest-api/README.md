# Guacamole REST API

# Table of Contents
- [Structure](#structure)
- [Api Modules](#api-modules)
- [Tests Modules](#tests-modules)
- [How to Run Tests](#how-to-run-tests)
- [Documentation](#documentation)
    - [General Structure of Request and Response](#general-structure-of-request-and-response)
    - [Reference to Documentation](#reference-to-documentation)

# Structure
```
    guacamole-rest-api
    ├── api
    │   ├── config.py
    │   ├── connection_groups.py
    │   ├── connections.py
    │   ├── functions.py
    │   ├── schemes_and_languages.py
    │   ├── sharing_profiles.py
    │   ├── tokens.py
    │   ├── user_groups.py
    │   └── users.py
    ├── docs
    │   ├── CONNECTION_GROUPS.md
    │   ├── CONNECTIONS.md
    │   ├── SCHEMES_AND_LANGUAGES.md
    │   ├── SHARING_PROFILES.md
    │   ├── TOKENS.md
    │   ├── USER_GROUPS.md
    │   └── USERS.md
    ├── tests
    │   ├── test_1_create_all.py
    │   ├── test_2_users.py
    │   ├── test_3_user_groups.py
    │   ├── test_4_connections.py
    │   ├── test_5_connection_groups.py
    │   ├── test_6_sharing_profiles.py
    │   ├── test_7_schemes_and_languages.py
    │   └── test_8_delete_all.py
    ├── README.md
    └── requirements.txt
```

# Api Modules

- **config** - It contains variables which must be changed according to the deployed Apache Guacamole.

- **connection_groups** - It contains requests related to the connection groups and helper function.

- **connection** - It contains requests related to the connections and helper function.

- **functions** - It contains helper functions.

- **schemes_and_languages** - It contains requests related to the schemes and languages.

- **sharing_profiles** - It contains requests related to the sharing profiles and helper function.

- **tokens** - It contains requests related to the tokens and helper functions.

- **user_groups** - It contains requests related to the user groups.

- **users** - It contains requests related to the users.

# Tests Modules
- **test_1_create_all** - It contains tests for creating token, user, user groups, connections, connection group and sharing profile.

- **test_2_users** - It contains tests related to the user requests.

- **test_3_user_groups** - It contains tests related to the user group requests.

- **test_4_connections** - It contains tests related to the connection requests.

- **test_5_connection_groups** - It contains tests related to the connection group requests.

- **test_6_sharing_profiles** - It contains tests related to the sharing profile requests.

- **test_7_schemes_and_languages** - It contains tests related to the schemes and languages requests.

- **test_8_delete_all** - It contains tests deleting of token, user, user groups, connections, connection group and sharing profile.

# How to Run Tests

## Windows
A Python virtual environment is being used for running the tests. <br>

**1.** Install Python 3 (tested in Python 3.11.4). <br>

**2.** Install virtualenv if not already installed.
```powershell
pip install virtualenv
```

**3.** Create the virtual environment.
```powershell
python -m venv C:\path\to\myenv
```

**4.** Change directory into the folder C:\path\to\myenv.
```powershell
cd C:\path\to\myenv
```

**5.** Activate the virtual environment.
```powershell
.\Scripts\Activate
```

**6.** Change directory into the folder where you want to clone repository.

**7.** Clone repository
```powershell
git clone https://gitlab.com/apache-guacamole/guacamole-rest-api.git
```

**8.** Change directory into the folder C:\path\to\guacamole-rest-api.
```powershell
cd C:\path\to\guacamole-rest-api
```

**9.** Install the dependencies for the virtual environment and tests.
```powershell
pip install -r requirements.txt
```

**10.** Open the file \api\config.py and change it according to parameters of your Apache Guacamole.
```powershell
ENDPOINT = "http://192.168.56.102:8080/guacamole"
AUTH_USERNAME = "guacadmin"
AUTH_PASSWORD = "guacadmin"
DATA_SOURCE = "mysql"
```

**11.** Run tests
```powershell
python -m pytest -vv -ra

tests/test_1_create_all.py::test_create_token PASSED                                    [  1%]
tests/test_1_create_all.py::test_create_user PASSED                                     [  2%]
tests/test_1_create_all.py::test_create_user_group PASSED                               [  3%]
tests/test_1_create_all.py::test_create_vnc_connection PASSED                           [  5%]
tests/test_1_create_all.py::test_create_ssh_connection PASSED                           [  6%]
tests/test_1_create_all.py::test_create_rdp_connection PASSED                           [  7%]
tests/test_1_create_all.py::test_create_telnet_connection PASSED                        [  9%]
tests/test_1_create_all.py::test_create_kubernetes_connection PASSED                    [ 10%]
tests/test_1_create_all.py::test_create_connection_group PASSED                         [ 11%]
tests/test_1_create_all.py::test_create_sharing_profile PASSED                          [ 13%]
tests/test_2_users.py::test_update_user PASSED                                          [ 14%]
tests/test_2_users.py::test_change_user_password PASSED                                 [ 15%]
tests/test_2_users.py::test_assign_permissions_to_user PASSED                           [ 17%]
tests/test_2_users.py::test_assign_user_to_user_group PASSED                            [ 18%]
tests/test_2_users.py::test_list_users_user_groups PASSED                               [ 19%]
tests/test_2_users.py::test_assign_user_to_connection PASSED                            [ 21%]
tests/test_2_users.py::test_assign_user_to_connection_group PASSED                      [ 22%]
tests/test_2_users.py::test_details_of_user_permissions PASSED                          [ 23%]
tests/test_2_users.py::test_details_of_user_effective_permissions PASSED                [ 25%]
tests/test_2_users.py::test_revoke_permissions_from_user PASSED                         [ 26%]
tests/test_2_users.py::test_revoke_user_from_user_group PASSED                          [ 27%]
tests/test_2_users.py::test_revoke_user_from_connection PASSED                          [ 28%]
tests/test_2_users.py::test_revoke_user_from_connection_group PASSED                    [ 30%]
tests/test_2_users.py::test_list_users PASSED                                           [ 31%]
tests/test_2_users.py::test_list_history_of_users PASSED                                [ 32%]
tests/test_2_users.py::test_details_of_user PASSED                                      [ 34%]
tests/test_2_users.py::test_details_of_self PASSED                                      [ 35%]
tests/test_2_users.py::test_details_of_user_history PASSED                              [ 36%]
tests/test_3_user_groups.py::test_update_user_group PASSED                              [ 38%]
tests/test_3_user_groups.py::test_assign_permissions_to_user_group PASSED               [ 39%]
tests/test_3_user_groups.py::test_assign_member_user_to_user_group PASSED               [ 40%]
tests/test_3_user_groups.py::test_assign_member_user_group_to_user_group PASSED         [ 42%]
tests/test_3_user_groups.py::test_assign_parent_user_group_to_user_group PASSED         [ 43%]
tests/test_3_user_groups.py::test_assign_user_group_to_connection PASSED                [ 44%]
tests/test_3_user_groups.py::test_assign_user_group_to_connection_group PASSED          [ 46%]
tests/test_3_user_groups.py::test_details_of_user_group_permissions PASSED              [ 47%]
tests/test_3_user_groups.py::test_revoke_permissions_from_user_group PASSED             [ 48%]
tests/test_3_user_groups.py::test_revoke_member_user_from_user_group PASSED             [ 50%]
tests/test_3_user_groups.py::test_revoke_member_user_group_from_user_group PASSED       [ 51%]
tests/test_3_user_groups.py::test_revoke_parent_user_group_from_user_group PASSED       [ 52%]
tests/test_3_user_groups.py::test_revoke_user_group_from_connection PASSED              [ 53%]
tests/test_3_user_groups.py::test_revoke_user_group_from_connection_group PASSED        [ 55%]
tests/test_3_user_groups.py::test_list_user_groups PASSED                               [ 56%]
tests/test_3_user_groups.py::test_details_of_user_group PASSED                          [ 57%]
tests/test_4_connections.py::test_update_vnc_connection PASSED                          [ 59%]
tests/test_4_connections.py::test_update_ssh_connection PASSED                          [ 60%]
tests/test_4_connections.py::test_update_rdp_connection PASSED                          [ 61%]
tests/test_4_connections.py::test_update_telnet_connection PASSED                       [ 63%]
tests/test_4_connections.py::test_update_kubernetes_connection PASSED                   [ 64%]
tests/test_4_connections.py::test_list_connections PASSED                               [ 65%]
tests/test_4_connections.py::test_list_history_of_connections PASSED                    [ 67%]
tests/test_4_connections.py::test_list_active_connections PASSED                        [ 68%]
tests/test_4_connections.py::test_details_of_connection PASSED                          [ 69%]
tests/test_4_connections.py::test_details_of_connection_parameters PASSED               [ 71%]
tests/test_4_connections.py::test_details_of_connection_history PASSED                  [ 72%]
tests/test_4_connections.py::test_details_of_connection_sharing_profiles PASSED         [ 73%]
tests/test_5_connection_groups.py::test_update_connection_group PASSED                  [ 75%]
tests/test_5_connection_groups.py::test_list_connection_groups PASSED                   [ 76%]
tests/test_5_connection_groups.py::test_list_connections_and_connection_groups PASSED   [ 77%]
tests/test_5_connection_groups.py::test_details_of_connection_group PASSED              [ 78%]
tests/test_6_sharing_profiles.py::test_update_sharing_profile PASSED                    [ 80%]
tests/test_6_sharing_profiles.py::test_list_sharing_profiles PASSED                     [ 81%]
tests/test_6_sharing_profiles.py::test_details_of_sharing_profile PASSED                [ 82%]
tests/test_7_schemes_and_languages.py::test_list_user_attributes PASSED                 [ 84%]
tests/test_7_schemes_and_languages.py::test_list_user_group_attributes PASSED           [ 85%]
tests/test_7_schemes_and_languages.py::test_list_connection_attributes PASSED           [ 86%]
tests/test_7_schemes_and_languages.py::test_list_connection_group_attributes PASSED     [ 88%]
tests/test_7_schemes_and_languages.py::test_list_sharing_profile_attributes PASSED      [ 89%]
tests/test_7_schemes_and_languages.py::test_list_protocol_attributes PASSED             [ 90%]
tests/test_7_schemes_and_languages.py::test_list_languages PASSED                       [ 92%]
tests/test_8_delete_all.py::test_delete_token PASSED                                    [ 93%]
tests/test_8_delete_all.py::test_delete_user PASSED                                     [ 94%]
tests/test_8_delete_all.py::test_delete_user_group PASSED                               [ 96%]
tests/test_8_delete_all.py::test_delete_sharing_profile PASSED                          [ 97%]
tests/test_8_delete_all.py::test_delete_connection PASSED                               [ 98%]
tests/test_8_delete_all.py::test_delete_connection_group PASSED                         [100%]
===================================== 76 passed in 7.96s ===================================== 
```

**11.** Deactivate the virtual environment
```powershell
deactivate
```

# Documentation
This documentation describes in detail how to use the Apache Guacamole REST API. 
<br> It contains a total of 7 sections related to tokens, users, user groups, connections, connection groups, shared profiles, schemas and languages.
<br> 
<br> The documentation is based on Apache Guacamole version 1.5.2.

## General Structure of Request and Response
- **Name of the request**

    - **Request**
        - **Method** - The type of method is specified (GET, POST, PUT, PATCH, DELETE).

        - **Endpoint** - The endpoint is specified.

        - **Path parameters** - The path parameters are specified with their name,  type and description. They are in {} in the URL as well.

        - **Query parameters** - The query parameters are specified with their name, type and description.

        - **Headers** - The type of headers is specified.

        - **Body** - All options are specified with their type and description.

        - **Example of body** - A possible example of request body is shown in the example of body in json format.

    - **Response**

        - **Normal response code** - The normal response status code is specified (200, 204).

        - **Body** - All options are specified with their type and description.

        - **Example of body** - A possible example of response body is shown in the example of body in json format.

## Reference to Documentation
- Tokens
- Users
- User groups
- Connections
- Connection groups
- Sharing profiles
- Schemes and languages

