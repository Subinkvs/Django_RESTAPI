import requests

endpoint = "http://localhost:8000/api/products/35/update/"

data = {
    'title': 'Inner_Wear', 
    'content': 'gym fit', 
    'price': 999.99
}

get_response = requests.put(endpoint, json=data)
print(get_response.status_code)
print(get_response.json())