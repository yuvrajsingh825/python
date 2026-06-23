import requests

data = {
    "name": "Yuvraj",
    "age": 19
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.status_code)
print(response.json())