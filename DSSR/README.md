# DDSR 

Concerning the output file that shows some exemples of results, we only consider as exemple the 1CSL.pdb file. 

1/ Download the [dssr](https://github.com/EvryRNA/rna_angles_prediction_dssr/tree/main) folder from the github link + download the pdb file on the RCSB PDB database. 

2/ Run the script select_chainA.py, which allows us to only keep the chain A contained in the pdb file. 

3/ Removal of empty pdb file (whose don't contain chain A) with bash command line :

 ```markdown
  $ find . -type f -size 0 -delete
  ```


4/ Launch the `train_dssr_calcul.py` then `test_dssr_calcul.py` to get the real values of all the angles calculated by the DSSR script, here those script automatize the calculation for all the pdb file in training and test set. 

5/ Extraction of the pseudo torsion angles (eta, eta',eta'') to make the histogram of the distribution (on RStudio) using the following awk command line with the file train-list-pdb.txt (file with all the pdb names):

 ```markdown
  $ for i in $(cat ../train-list-pdb.txt); do awk -F',' '{print $13 "\t" $15 "\t" $17}' $i-res.txt > $i-all_eta.txt;done;
  ```
6/ Concatenation of all the eta value in on file, to vizualize the distribution in RStudio with the script  `train_make_file_all_eta.py`

7/ Distribution of the eta, eta', eta'' of the training dataset :

![image](https://github.com/HenessA/rna_project_2023/assets/105880255/61f3e23c-27fe-422e-a1c4-d483dd25c9dc)


![image](https://github.com/HenessA/rna_project_2023/assets/105880255/0323da36-4c16-48f6-a31e-a02989ff0748)


![image](https://github.com/HenessA/rna_project_2023/assets/105880255/5fbbac23-9b62-4ebf-8818-124812d6500d)





 
