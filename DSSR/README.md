# DDSR step


1/ Download the [dssr](https://github.com/EvryRNA/rna_angles_prediction_dssr/tree/main) folder from the github link + download the pdb file

2/ Run the script select_chainA.py

3/ Launch the  `train_dssr_calcul.py` then `test_dssr_calcul.py`

4/ Extraction of the angles to make the distribution


###### bash command to remove the empty pdb file (whose don't contain chain A)

  ```markdown
  $ find . -type f -size 0 -delete
  ```
