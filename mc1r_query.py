#this is mc1_query.py


#imported libraries
import requests
import json

def get_database():

    url = "https://mygene.info/v3/query"

    ext = {
        "q": "symbol:MC1R", "species": "human"
    }

    response = requests.get(url, ext=ext)

    data = response.json()

    print(data)

if __name__ == "__main__":
    get_database()