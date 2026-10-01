#this is mc1_query.py


#imported libraries
import requests

url = "https://mygene.info/v3/query"

ext = {
    "q": "MC1R", "species": "human"
}

response = requests.get(url, ext=ext)

data = response.json()

print(data)