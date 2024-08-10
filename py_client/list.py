import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("Enter your username\n")
password = getpass("Enter your password\n")

data = {
    'username': username,
    'password': password
}

auth_response = requests.post(auth_endpoint, json=data)
print(auth_response.status_code)
print(auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization":f"Bearer {token}"
    }
    
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.status_code)
    print(get_response.json())
    print(len(get_response.json()))
    print(f'Bearer')