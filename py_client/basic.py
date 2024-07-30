import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, params={'abc':123}, json={'title':"Sport_wear"})
print(get_response.text)
print(get_response.status_code)

print(get_response.json())