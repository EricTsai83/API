import requests

response = requests.get(
    "http://127.0.0.1:8000/api/winners",
    params={"country": "Austria"},
)
print(response.json())
