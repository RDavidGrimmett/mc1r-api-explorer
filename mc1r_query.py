
# Imported libraries
import requests
import json
import re
from Bio.Seq import Seq

# Get ensembl_id from mygene.info
def get_ensembl_id():

    # Target url and search parameters
    url = "https://mygene.info/v3/query"
    
    params = {
        "q": "symbol:MC1R",
        "species": "human",
        "fields": "symbol,ensembl"
    }

    # Captures data from database in response variable
    response = requests.get(url, params=params)

    # If connection successful, captures database as variable
    if response.status_code == 200:
        data = response.json()

        # Captures just the ensmbl_id as variable
        ensembl_id = data["hits"][0]["ensembl"]["gene"]

        # Returns the ensembl_id
        return ensembl_id

    # If connection is unsuccessful, print error
    else:
        print("Request failed:", response.status_code)
        print(response.text)


# Get DNA sequences from ensembl.org
def get_sequence(ensembl_id):
    
    # Target url, parameters, and headers
    url = f"https://rest.ensembl.org/sequence/id/{ensembl_id}"
    
    params = {
        "type": "genomic"
    }

    headers = {
        "Content-type": "application/json"
    }

    # Captures data from database in response variable
    response = requests.get(url, params=params, headers=headers)

    # If connection successful, captures the data as variable
    if response.status_code == 200:
        data = response.json()

        # Sets the DNA sequence to a variable
        sequence = data["seq"]

        return sequence
    
    # If connection is unsuccessful, print error
    else:
        print("Request failed:", response.status_code)
        print(response.text)
        

# Creates a FASTA file with ensembl_id and DNA sequence
def create_fasta(ensembl_id, sequence):
    
    # Writes the following to a FASTA file in FASTA format
    with open("mc1r_sequence.fasta", "w") as file:
        file.write(f">{ensembl_id}\n")
        file.write(sequence)


# Finds the longest open reading frame (ORF) in DNA seqeunce 
def find_longest_orf(sequence):

    # Creates a regular expression and a list to hold all the open frames
    # RegEx: Starts with ATG, followed by any number of three chracter sets, then stops with TAG, TGA, or TAA.
    pattern = re.compile(r'(?=(ATG(?:...)*?)(TAG|TGA|TAA))')
    orfs = []
    
    # Finds all matches in sequence
    for match in pattern.finditer(sequence):

        # Attaches the start and end codons to each sequence
        orfs.append(match.group(1) + match.group(2))

    # Captures only the longest ORF using max length of the list
    longest_orf = max(orfs, key=len, default=None)

    return longest_orf


# Translates the longest ORF into an amino acid sequence
def get_amino_acids(longest_orf):

    # Converts the longest ORF DNA string into a Biopython object
    longest_orf_seq = Seq(longest_orf) 

    # Translates the longest ORF to amino acids using Biopython
    amino_acids = longest_orf_seq.translate()

    return amino_acids


# Appends Amino Acid Sequence to the FASTA file
def append_fasta(amino_acid_seq):
        
    # Appends the following to a new line on FASTA file
        with open("mc1r_sequence.fasta", "a") as file:
            file.write(f"\n{amino_acid_seq}")


# Get homologous genes from ensembl.org
def get_homologous_genes(ensembl_id):
    
    # Target url, parameters, and headers
    url = f"https://rest.ensembl.org/homology/id/human/{ensembl_id}"
    
    params = {
         "type": "orthologues",
         "sequence": "none"
    }

    headers = {
         "Content-Type": "application/json"
    }

    # Captures data from database in response variable 
    response = requests.get(url, params=params, headers=headers)

    # If connection successful, captures all the homologous genes as variable
    if response.status_code == 200:

        homologous_genes = response.json()

        return homologous_genes

        # If connection is unsuccessful, print error
    else:
        print("Request failed:", response.status_code)
        print(response.text)
            
# Creates list of unique species from homologous genes
def get_unique_species(homologous_genes):

        # List to hold all the species
        species_list = []

        # Creates loop for each set of data in homologous genes variable
        for homology in homologous_genes["data"][0]["homologies"]:

            # Capturing only the species names
            species_list.append(homology["target"]["species"])

            # Removes duplicates from the list
            unique_species_list = list(set(species_list))

            # Converting list into string
            unique_species_str = ", ".join(unique_species_list)

        return unique_species_str


# Creates and writes the list of species to TXT file
def create_txt(unique_species_str):
    with open ("mc1r_homology_list.txt", "w") as file:
        file.write(unique_species_str)


# Runs functions in sequential order
if __name__ == "__main__":

    ensembl_id = get_ensembl_id()

    sequence = get_sequence(ensembl_id)

    create_fasta(ensembl_id, sequence)

    longest_orf = find_longest_orf(sequence)

    amino_acids = get_amino_acids(longest_orf)

    append_fasta(amino_acids)

    homologous_genes = get_homologous_genes(ensembl_id)

    unique_species_str = get_unique_species (homologous_genes)

    create_txt(unique_species_str)
