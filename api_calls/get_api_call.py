import requests

url = 'http://localhost:5000/cakes'


newrequest = requests.get(url)
print(newrequest)