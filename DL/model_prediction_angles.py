import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense
!pip install biopython 
from Bio import SeqIO
import numpy as np

from google.colab import drive
import os
drive.mount('/content/drive/', force_remount= True )
os.chdir('drive/My Drive/prediction_angles_project/') # directory of your choice
!ls

#PADDING of the training set
def completer_sequences(fichier_entree, fichier_sortie, longueur_voulue):
    with open(fichier_entree, "r") as entree:
        lignes = entree.readlines()

    with open(fichier_sortie, "w") as sortie:
        for ligne in lignes:
            if ligne.startswith(">"):
                sortie.write(ligne)  
            else:
                sequence = ligne.strip()  
                sequence_length = len(sequence)

                if sequence_length < longueur_voulue:
                    # Add 'X', to match the length of the longest sequence
                    sequence += "X" * (longueur_voulue - sequence_length)
                elif sequence_length > longueur_voulue:
                    # Tronquer la séquence à la longueur voulue
                    sequence = sequence[:longueur_voulue]

                sortie.write(sequence + "\n")  # Écrire la séquence ajustée

# Use of the function to get the padding file of the multi fasta provided
completer_sequences("train-multi.fa", "train-padding", 417)

fasta_file = "train-padding"
!head train-padding


# ONE HOT ENCODING of the training set 
# Function to read the fasta file and get the sequences
def read_fasta(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(str(record.seq))
    return sequences

# Charger les étiquettes du fichier Y_train.txt
with open("Y_train.txt", 'r') as file:
    train_label = file.read()

train_label = train_label.replace("NA", "19")

# Charger les séquences et encoder
fasta_file = "train-padding"
sequences = read_fasta(fasta_file)

# Encoding the sequence into a matrix with 4 columns AUGC
def encode_sequence(sequence):
    encoding = {'A': [1, 0, 0, 0], 'U': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'C': [0, 0, 0, 1], 'X': [0, 0, 0, 0], 'N': [0, 0, 0, 0]}
    encoded_sequence = [encoding[nucleotide] for nucleotide in sequence]
    return np.array(encoded_sequence)

# Encode sequences
train_encoded = np.array([encode_sequence(seq) for seq in sequences])

# Encoder les étiquettes
label_encoder = LabelEncoder()
train_label_encoded = label_encoder.fit_transform(list(train_label))

# Assurez-vous que les données sont de type float
X_train = train_encoded.astype(float)
len(X_train)
X_train

#PADDING and ONE HOT ENCODING of test set
def completer_sequences(fichier_entree, fichier_sortie, longueur_voulue):
    with open(fichier_entree, "r") as entree:
        lignes = entree.readlines()

    with open(fichier_sortie, "w") as sortie:
        for ligne in lignes:
            if ligne.startswith(">"):
                sortie.write(ligne)  # Écrire l'en-tête
            else:
                sequence = ligne.strip()  # Récupérer la séquence
                sequence_length = len(sequence)

                if sequence_length < longueur_voulue:
                    # Ajouter des 'X' pour atteindre la longueur voulue
                    sequence += "X" * (longueur_voulue - sequence_length)
                elif sequence_length > longueur_voulue:
                    # Tronquer la séquence à la longueur voulue
                    sequence = sequence[:longueur_voulue]

                sortie.write(sequence + "\n")  # Écrire la séquence ajustée

# Appel de la fonction pour ajuster la longueur de chaque séquence à 417
completer_sequences("test-multi.fa", "test-padding", 417)

!head test-padding

#Read the fasta file and extract the seq
def read_fasta(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(str(record.seq))
    return (sequences)

#Encoding the sequence into a matrix with 4 columns AUGC
def encode_sequence(sequence):
    encoding = {'A': [1, 0, 0, 0], 'U': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'C': [0, 0, 0, 1], 'X':[0,0,0,0], 'N':[0,0,0,0]}
    encoded_sequence = [encoding[nucleotide] for nucleotide in sequence]

    print(np.array(encoded_sequence))

    with open("encodage.txt","w") as fichierecriture:
        fichierecriture.write(str(encoded_sequence))
#Load data
fasta_file = "test-padding"
sequences = read_fasta(fasta_file)


#Encode sequences
test_encoded = np.array([encode_sequence(seq) for seq in sequences])
len(test_encoded) #to check if all the fasta file have been encoded
#type(test_encoded)

with open("Y_test.txt", 'r') as file:
    test_label = file.read()

test_label = test_label.replace("NA", "19")


with open("Y_train.txt", 'r') as file:
    train_label = file.read()

train_label = train_label.replace("NA", "19")

import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error

# Charger les étiquettes du fichier Y_test.txt
with open("Y_test.txt", 'r') as file:
    test_label = file.read()

test_label = test_label.replace("NA", "19")

# Charger les étiquettes du fichier Y_train.txt
with open("Y_train.txt", 'r') as file:
    train_label = file.read()

train_label = train_label.replace("NA", "19")

# Séparer les caractéristiques (X) et les étiquettes (y) pour l'entraînement
X_train = train_encoded
y_train = train_label

# Séparer les caractéristiques (X) et les étiquettes (y) pour le test
X_test = test_encoded
y_test = test_label

y_train_list = list(y_train)

# Assurez-vous que les données sont de type float
X_train_flat = np.array([seq.flatten() for seq in X_train]).astype(float)

# Initialiser le scaler
scaler = StandardScaler()

# Standardiser les données d'entraînement
X_train_scaled = scaler.fit_transform(X_train_flat)

# Encoder les étiquettes
label_encoder = LabelEncoder()
train_label_encoded = label_encoder.fit_transform(y_train_list)

# Assurez-vous que les données sont de type float
X_train = np.array(X_train).astype(float)
X_test = np.array(X_test).astype(float)

# Initialiser le scaler
scaler = StandardScaler()

# Standardiser les données d'entraînement
X_train_scaled = scaler.fit_transform(X_train)

# Standardiser les données de test en utilisant le scaler ajusté sur les données d'entraînement
X_test_scaled = scaler.transform(X_test)

# Créer et initialiser le modèle MLP
mlp_model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)

# Ajuster le modèle sur les données d'entraînement
mlp_model.fit(X_train_scaled, train_label_encoded)

# Faire des prédictions sur l'ensemble de test
y_pred_test = mlp_model.predict(X_test_scaled)

# Encoder les étiquettes du jeu de test
test_label_encoded = label_encoder.transform(y_test)

# Calculer l'erreur quadratique moyenne (MSE) sur l'ensemble de test
mse_test = mean_squared_error(test_label_encoded, y_pred_test)
print(f'Mean Squared Error on Test Set: {mse_test}')
