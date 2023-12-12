import requests

endpoint = 'http://localhost:8000/api/tickets/'

data = {
    'author': 'steve',
    'pub_date': '12/12/2023',
    'content': 'cannot login properly',
}

res = requests.post(endpoint, json=data)
print(res.json())
