#this is mc1_query.py


#imported libraries
import requests


def get_database():

    url = "https://mygene.info/v3/query"

    params = {
        "q": "symbol:MC1R",
        "species": "human"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        gene = data["hits"][0]

        print(f"Gene ID: {gene['_id']}")
        print(f"Gene Symbol: {gene['symbol']}")
        print(f"Gene Name: {gene['name']}")

    else:
        print("Request failed with code:", response.status_code)


if __name__ == "__main__":
    get_database()