# Project on RNA torsion angles 2023

by Henes AMROUCHE and Kamély LUMIÈRE

This repository contains all the script and command lines used to do this project, aimed to build a model which is able to predict the pseudo torsion angle etha second from a fasta file.

The different steps of this project was :

* 1/  `DSSR` : prediction of the true torsion of angle and pseudo angle from a pdb file using dssr_wrapper.py script (selection of chain A only in multi-stranded RNA) and a python script dssr_calcul.py( from 191 pdb file after the dssr: 164 pdb file with a chain A)

* 2/ Distribution of pseudo torsion angle of eta, eta' and eta '' using the output of DSSR in a R script to see the values of the angles

* 3/ Define class for value of angles

* 4/ Selection of the columns containning the sequence and the value of eta'' angles and replace the angle value by the class defined previously

* 5/ Concatenation of all value of angles and base to make a distribution

* 6/ Downloading the fasta file of the pdb







