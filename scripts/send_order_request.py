import json
import requests
from request_builders.order_requests import generate_order_request


orders_url = 'http://localhost:8080/api/v1/orders'
headers = {'accept': 'application/json'}
request_body = generate_order_request("0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d")

# Here is our current error
# {"errorType":"SameBuyAndSellToken","description":"Buy token is the same as the sell token."}
try:
    response = requests.post(
        orders_url, 
        headers=headers, 
        data=json.dumps(request_body)
        )
    response.raise_for_status()
    
    print(response)

except requests.exceptions.RequestException as e:
    print(response.text)
except json.JSONDecodeError:
    print(response.text)

