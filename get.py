#Send GET request with timeout.
import requests

#Create custom headers.
headers = {
    "User-Name": "Yuvraj"
}

#Use query parameters.
params ={
    "search_query":"request+library+python+tutorial"
}

response = requests.get(
    # Error fixed: URL must be inside quotes because it is a string.
    "https://www.youtube.com/results",
    # Error fixed: comma was missing after params=params.
    params=params,
    headers=headers,
    timeout=2
)

print(response.status_code)
print(response.request.headers["User-Name"])
print(params["search_query"])
print(response.url)
