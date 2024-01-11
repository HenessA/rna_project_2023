# Project on RNA torsion angles 2023

_by Henes AMROUCHE and Kamély LUMIÈRE_

This repository contains all the script and command lines used to do this project, aimed to build a model which is able to predict the pseudo torsion angle etha second from a fasta file. Find all the README file corresponding to each step, in the corresponding folder.

Pseudo torsion angle :** &eta;'**

The different steps of this project was :

 1/  `DSSR` : preprocessing the data (keep RNA pdb file with a chain A), prediction of the true angles values, from a pdb file using `dssr_wrapper.py` script and a python script `dssr_calcul.py`.  Plot the distribution of **eta, eta', eta''** in RStudio. 

 2/ `classes` : Define class from distribution plot,  replace the continious values of **eta''** by the class \in {0..20}, padding preparation to get the same lengths for each sequences (and make sure of the uniform dimension for the future matrix in DL part), distribution of the class for **eta''** angles to confirm the classification step.

 3/  `DL`: Deep learning part of the project ; get X_train, X_test, y_train, y_test from the previous step and by downloading the fasta file (input of the model) on  [RCSB PDB](https://www.rcsb.org) database, padding, ONE HOT encoding, MLP (with training step, evaluation step). 

 






