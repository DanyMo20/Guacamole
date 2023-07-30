import requests
from api.tokens import get_token

# Headers application/json.
def json_headers():
    return {
        "Content-Type": "application/json"
    }

# Query parameter token.
def token_params():
    token = get_token()
    return {
        "token": token
    }

# Request GET.
def request_get(url):
    params = token_params()
    return requests.get(url=url, params=params)

# Request POST.
def request_post(url, json):
    params = token_params()
    headers = json_headers()
    return requests.post(url=url, params=params, headers=headers, json=json)

# Request PUT.
def request_put(url, json):
    params = token_params()
    headers = json_headers()
    return requests.put(url=url, params=params, headers=headers, json=json)

# Request PATCH.
def request_patch(url, json):
    params = token_params()
    headers = json_headers()
    return requests.patch(url=url, params=params, headers=headers, json=json)

# Request DELETE.
def request_delete(url):
    params = token_params()
    return requests.delete(url=url, params=params)

