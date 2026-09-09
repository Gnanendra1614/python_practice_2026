import requests

data = {
    "name": "Gnanendra",
    "email": "gnanendra@example.com"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=data
)

print(response.status_code)
print(response.json())