import requests

data = {
    "email": "newemail@example.com"
}

response = requests.patch(
    "https://jsonplaceholder.typicode.com/users/1",
    json=data
)

print(response.status_code)
print(response.json())