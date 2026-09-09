import requests

data = {
    "name": "Updated Name",
    "email": "updated@example.com"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/1",
    json=data
)

print(response.status_code)
print(response.json())