import requests

response = requests.get("https://api.github.com/users/yuvrajsingh825")
print(response.json().get("name"))
if response.status_code == 200:
    data = response.json()
    print("Authorized")
else:
    print("Request Failed")

    