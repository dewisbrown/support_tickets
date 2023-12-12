import requests
from datetime import datetime

endpoint = 'http://localhost:8000/api/tickets/'
res = requests.get(endpoint)
print(res.json())
