# DDSR 


1/ Download the [dssr](https://github.com/EvryRNA/rna_angles_prediction_dssr/tree/main) folder from the github link + download the pdb file

2/ Run the script select_chainA.py

3/Removal of empty pdbfile (whose don't contain chain A) with bash command line

 ```markdown
  $ find . -type f -size 0 -delete
  ```


4/ Launch the  `train_dssr_calcul.py` then `test_dssr_calcul.py`

5/ Extraction of the angles to make the distribution




 
