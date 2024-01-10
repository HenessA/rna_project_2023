# DDSR 


1/ Download the [dssr](https://github.com/EvryRNA/rna_angles_prediction_dssr/tree/main) folder from the github link + download the pdb file

2/ Run the script select_chainA.py

3/Removal of empty pdbfile (whose don't contain chain A) with bash command line

 ```markdown
  $ find . -type f -size 0 -delete
  ```


4/ Launch the  `train_dssr_calcul.py` then `test_dssr_calcul.py`

5/ Extraction of the seudo torsion angles (eta, eta',eta'') to make the distribution using the following awk command line with the file train-list-pdb.txt (file with all the pdb names)

 ```markdown
  $ for i in $(cat ../train-list-pdb.txt); do awk -F',' '{print $13 "\t" $15 "\t" $17}' $i-res.txt > $i-all_eta.txt;done;
  ```
6/ Concatenation of all the etha value to vizualize the distribution in R with the script  `train_make_file_all_eta.py`

7/ Distribution

![image](https://github.com/HenessA/rna_project_2023/assets/105880255/83a153be-ba98-49c0-ab3b-86da05ca21ca)





 
