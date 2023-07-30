import requests
from api.config import *

# Username and password used to authenticate and obtain an access token.
def token_auth():       
    return (
        AUTH_USERNAME, 
        AUTH_PASSWORD
    )

# Headers application/x-www-form-urlencoded. It used to obtain an access token.
def token_headers(): 
    return {
        "Content-Type": "application/x-www-form-urlencoded"
    }

# Generating an access token. The token used to access Apache Guacamole via the REST API.
def create_token():
    headers = token_headers()
    auth = token_auth()
    return requests.post(ENDPOINT + "/api/tokens", headers=headers, auth=auth)

# Deleting an access token.
def delete_token():
    token = get_token()
    return requests.delete(ENDPOINT + f"/api/tokens/{token}")

# Obtaining an access token from response.json().
def get_token():
    create_token_data = create_token()
    token = create_token_data.json()["authToken"]
    return token

