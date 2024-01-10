## script to calcul all the angles from the pdb file with dssr for the test set
import os


with open("test-list-pdb.txt", "r") as struc:
    for ligne in struc:
        if len(ligne.strip()) != 0:
            input_path = "/Users/henes/Desktop/rna_project_bureau/rna_angles_prediction_dssr/test-file/" + ligne.strip()
            output_path = ligne.strip() + "-res.txt"

            # Utilisez .format() pour inclure les variables dans la chaîne de commande
            command = "python3 -m src.dssr_wrapper --input_path {} --output_path {} --to_csv".format(input_path, output_path)
            
	else: 
		print("No file found") 

