#this is mc1r_query.py


#imported libraries
import requests
from pprint import pprint


def get_ensembl_id():

    url = "https://mygene.info/v3/query"

    params = {
        "q": "symbol:MC1R",
        "species": "human",
        "fields": "symbol,ensembl"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        ensembl_id = data["hits"][0]["ensembl"]["gene"]


        return ensembl_id


def retrieve_data(ensembl_id):
    url = f"https://rest.ensembl.org/sequence/id/{ensembl_id}"

    params = {
        "type": "genomic"
    }

    headers = {
        "Content-type": "text/plain"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        sequence = response.text

        return sequence

    else:
        print("Reuest failed:", response.status_code)
        print(response.text)
        return None


def create_fasta(ensembl_id, sequence):
    with open("mc1r_sequence.fasta", "w") as file:
        file.write(f">{ensembl_id}\n")
        file.write(sequence)


if __name__ == "__main__":

    ensembl_id = get_ensembl_id()

    sequence = retrieve_data(ensembl_id)

    create_fasta(ensembl_id, sequence)

print("Ensembl ID:", ensembl_id)
print("Sequence:", sequence)
