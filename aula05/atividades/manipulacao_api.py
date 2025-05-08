import requests

url = "https://randomuser.me/api"

#Fazendo a requisição GET
response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    user = data['results'][0]
    name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
    email = user['email']
    country = user ['location']['country']

    print(f"Nome: {name}")
    print(f"Email: {email}")
    print(f"País: {country}")
else:
    print("Erro de chamada à API: {response.status_code}")