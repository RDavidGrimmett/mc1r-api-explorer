# This is mc1r_query.py


# Imported libraries
import requests
import json
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
def get_sequence(ensembl_id):
    
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

        # Attaches the start and end codons to sequence
        orfs.append(match.group(1) + match.group(2))

    # Captures the longest orf using max length of the list
    longest_orf = max(orfs, key=len, default=None)

    return longest_orf


# Translates the longest ORF into an amino acid sequence
def get_amino_acids(longest_orf):
    longest_orf_seq = Seq(longest_orf) 

    # Translates the longest orf to amino acids
    amino_acids = longest_orf_seq.translate()

    return amino_acids


# Appends Amino Acid Sequence to the FASTA file
def append_fasta(amino_acid_seq):
    # Appends the follwoing to a new line on FASTA file
        with open("mc1r_sequence.fasta", "a") as file:
            file.write(f"\n{amino_acid_seq}")


# Identify Homologous Genes
def get_homologous_species(ensembl_id):
    url = f"https://rest.ensembl.org/homology/id/human/{ensembl_id}"
    
    params = {
         "type": "orthologues",
         "sequence": "none"
    }

    headers = {
         "Content-Type": "application/json"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:

        data = response.json()

        species = []

        for homology in data["data"][0]["homologies"]:

            species.append(homology["target"]["species"])

        return species

# Creates and writes the list of species to TXT file
def create_txt(species):
    with open ("mc1r_homology_list.txt", "w") as file:
        file.write(species)


# Runs functions in sequential order
if __name__ == "__main__":

    ensembl_id = get_ensembl_id()

    sequence = get_sequence(ensembl_id)

    create_fasta(ensembl_id, sequence)

    longest_orf = find_longest_orf(sequence)

    amino_acids = get_amino_acids(longest_orf)

    append_fasta(amino_acids)

    species = get_homologous_species(ensembl_id)

print("Ensembl ID:", ensembl_id)
print("Sequence:", sequence)
print("Longest_ORF:", longest_orf)
print("Amino Acids:", amino_acids)
print(species)