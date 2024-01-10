# Project on RNA torsion angles 2023

by Henes AMROUCHE and Kamély LUMIÈRE

This repository contains all the script and command lines used to do this project, aimed to build a model which is able to predict the pseudo torsion angle etha second from a fasta file.

The different steps of this project was:

* 1/ prediction of the true torsion of angle and pseudo angle from a pdb file using dssr_wrapper.py script (selection of chain A only in multi-stranded RNA)

* 2/ distribution of pseudo torsion angle of eta, eta' and eta '' using the output of dssr in a R script to see the values of the angles

* 3/ Define class for value of angles

* 4/ selection of the colum containning the sequence and the value of eta'' angles and replace the angle value by the class defined previously

* 5/ Concatenation of all value of angles and base to make a distribution

* 6/







