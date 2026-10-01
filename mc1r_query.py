# This is mc1r_query.py


# Imported libraries
import requests
import re
from pprint import pprint
from Bio.Seq import Seq

# Get ensembl_id from mygene.info
def get_ensembl_id():

    # Target url and parameters
    url = "https://mygene.info/v3/query"
    
    params = {
        "q": "symbol:MC1R",
        "species": "human",
        "fields": "symbol,ensembl"
    }

    # Captures data from database in response variable
    response = requests.get(url, params=params)

    # If connection successful, do the following
    if response.status_code == 200:
        data = response.json()

        # Captures ensmbl_id as variable
        ensembl_id = data["hits"][0]["ensembl"]["gene"]

        # Returns the ensembl_id
        return ensembl_id

    # If connection is unsuccessful, print error
    else:
            print("Reuest failed:", response.status_code)
            print(response.text)
            return None


# Get DNA sequences from ensembl.org
def retrieve_data(ensembl_id):
    
    # Target url, parameters, and headers
    url = f"https://rest.ensembl.org/sequence/id/{ensembl_id}"
    
    params = {
        "type": "genomic"
    }

    headers = {
        "Content-type": "text/plain"
    }

    # Captures data from database in response variable
    response = requests.get(url, params=params, headers=headers)

    # If connection successful, do the following
    if response.status_code == 200:
        sequence = response.text

        return sequence
    
    # If connection is unsuccessful, print error
    else:
        print("Reuest failed:", response.status_code)
        print(response.text)
        return None


# Creates a FASTA file with ensembl_id and DNA sequence
def create_fasta(ensembl_id, sequence):
    
    # Writes the follwoing to a FASTA file
    with open("mc1r_sequence.fasta", "w") as file:
        file.write(f">{ensembl_id}\n")
        file.write(sequence)


# Finds the longest open reading frame (ORF) in DNA seqeunce 
def find_longest_orf(sequence):

    # Creating list of all matching sequences
    pattern = re.compile(r'(?=(ATG(?:...)*?)(TAG|TGA|TAA))')
    orfs = []
    
    # Find all matches in sequence
    for match in pattern.finditer(sequence):
        orfs.append(match.group(1) + match.group(2))

    # Captures the longest orf using max length of the list
    return max(orfs, key=len, default=None)
    

# Appends longest ORF to the FASTA file
def append_fasta():

# Runs functions in sequential order
if __name__ == "__main__":

    ensembl_id = get_ensembl_id()

    sequence = retrieve_data(ensembl_id)

    create_fasta(ensembl_id, sequence)

    longest = find_longest_orf(sequence)

print("Ensembl ID:", ensembl_id)
print("Sequence:", sequence)

