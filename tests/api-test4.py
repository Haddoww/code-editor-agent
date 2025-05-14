import requests

def get_data_from_api(api_url, params=None, headers=None):
    response = requests.get(api_url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()