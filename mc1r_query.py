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

    if response.status_code == 200:
        data = response.json()
        print(f"Gene ID: {data['id']}")
        print(f"Location: Chromosome {data['seq_region_name']}, Start: {data['start']}")
    else:
        print("Request failed with code:", response.status_code)


if __name__ == "__main__":
    get_database()