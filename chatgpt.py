import os

eta= ["eta"]
eta1= ["eta'"]
eta2= ["eta''"]
# Ouvre le fichier d'entrée en mode lecture
with open('list-res.txt', 'r') as fichier_entree:
    # Lit chaque ligne du fichier
    for numero_iteration, ligne in enumerate(fichier_entree, start=1):
        # Supprime les espaces, tabulations et sauts de ligne à la fin de la ligne
        nom_fichier = ligne.strip()

        # Vérifie si le nom de fichier est vide après la suppression des espaces
        if not nom_fichier:
            continue  # Passe à la prochaine itération s'il y a une ligne vide

        # Ouvre le fichier à lire en mode lecture
        with open(nom_fichier, 'r') as fichier_a_lire:
            # Lit le contenu du fichier
            contenu = fichier_a_lire.read()

            # Extrait le nom du fichier sans l'extension
            nom_sans_extension = os.path.splitext(nom_fichier)[0]

            # Crée un fichier de sortie avec le nom correspondant
            nom_fichier_sortie = f"output_{numero_iteration}_{nom_sans_extension}.txt"
            with open(nom_fichier_sortie, 'w') as fichier_sortie:
            	for line in fichier_sortie: 
            		if line[0] != "r": 
            			coordinates = line.split(',')
            			eta.append(coordinates[12])
            			eta1.append(coordinates[15])
            			eta1.append(coordinates[17])
            			
               

