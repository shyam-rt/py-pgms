import requests

r=requests.get('http://go.codeschool.com/spamvanmenu')

menu=r.json()
print(menu)
