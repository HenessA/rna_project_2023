# Project on RNA torsion angles 2023

by Henes AMROUCHE and Kamély LUMIÈRE

This repository contains all the script and command lines used to do this project, aimed to build a model which is able to predict the pseudo torsion angle etha second from a fasta file.

The different steps of this project was :

 1/  `DSSR` : prediction of the true torsion of angle and pseudo angle from a pdb file using dssr_wrapper.py script (selection of chain A only in multi-stranded RNA) and a python script dssr_calcul.py( from 191 pdb file after the dssr: 164 pdb file with a chain A), distribution of eta, eta', eta'' in R

 2/ `classes` : replace the continious values of eta'' by the class \in {0..20}, preparation of Y_train with the step of padding (add X to sequences with length <387nt), distribution of the class for eta'' angles

 3/  `DL`: Deep learning part of the project=> get X_train, X_test, y_train, y_test from the previous step and  [RCSB PDB] data base (https://www.rcsb.org), padding, ONE HOT encoding, build MLP

 






