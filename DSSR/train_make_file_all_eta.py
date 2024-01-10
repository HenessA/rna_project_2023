## script to concatenate all the value of eta to make the R distribution

import os

#Change the current working directory
os.chdir("path/to/the/folder/containing/the/results/of/DSSR/calculation")

# List all files in the specified directory
list_eta_file = os.listdir("path/to/the/folder/containing/the/results/of/DSSR/calculation")

#List to store the content of all relevant files
contenu = []

#Iterate through each file in the directory
for file in list_eta_file:
    if ".pdb-all_eta.txt" in file:
        # Read the content of the file and add it to the list
        with open(file, 'r') as fichier_a_lire:
            contenu.extend(fichier_a_lire.readlines())

#Output file name
nom_fichier_sortie = "train-eta-concatene.txt"

#Write the concatenated content to the output file
with open(nom_fichier_sortie, 'w') as fichier_sortie:
    fichier_sortie.writelines(contenu)

print("File concatenated successfully.")

