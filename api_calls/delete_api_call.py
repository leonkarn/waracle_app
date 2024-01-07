import requests

delete_url = 'http://localhost:5000/cakes/{id}'.format(id=str(2))
newdelete = requests.delete(delete_url)
print(newdelete)