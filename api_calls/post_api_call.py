import requests

url = 'http://localhost:5000/cakes'

new_cake_data = {
    'name': 'Lemon Drizzle Cake',
    'comment': 'A sweet and tangy lemon cake',
    'image_url': 'http://example.com/lemoncake.jpg',
    'yum_factor': 4
}

newrequest = requests.post(url, json=new_cake_data)
print(newrequest)