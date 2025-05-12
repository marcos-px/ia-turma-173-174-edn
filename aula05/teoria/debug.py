import requests

response = requests.get("https://www.python.org")

if response.status_code == 200:
    print("Deu certim!")

    print(response.text[:100])
else:
    print(F"Deu ruim! Erro {response.status_code}")