import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print(response)
print(response.status_code)
print(response.text)

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

data = response.json()

print(data[0])
print(data[0]["name"])
print(data[0]["email"])