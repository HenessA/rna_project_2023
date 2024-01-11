## Script to download the fasta file of our RNA list, from the RCSB PDB database

import os

liste_ID = []

with open(file_name, "r") as ID: # replace the file_name by the file containing the list of pdb file
    # Read each line from the file
    for ligne in ID:
        # Split the line and append to liste_ID after stripping newline characters
        pdb_id = ligne.strip().replace(".pdb", "").upper()  # Get the name of the RNA from the pdb name file 
        liste_ID.append(pdb_id)

# Loop through the liste_ID and download files
for pdb_id in liste_ID:
    url = f"https://www.rcsb.org/fasta/entry/{pdb_id}/download"
    output_filename = f"{pdb_id}.fa"
    
    # Use wget to download the file from the URL  
    os.system(f"wget {url} -O {output_filename}")
    
    print(f"Downloading of {output_filename} for the PDB ID {pdb_id}")


print(f"Create {nom_fichier_sortie} for {file}")

