import requests

product_id = input("Which product's id do you want to delete?\n")
try:
    product_id = int(product_id)
except:
    print(f'{product_id} is not valid id')
    

if product_id:   
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)
    