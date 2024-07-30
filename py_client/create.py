import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'Sport_wear', 
    'content': 'gym fit', 
    'price': 1999.99
}

get_response = requests.post(endpoint, json=data)
print(get_response.status_code)
print(get_response.json())