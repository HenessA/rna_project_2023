# Deep Learning - Model of pseudo torsion **&eta;''** angles prediction

The first step of the DL part was to process the data to get  X_train,X_test, y_train, y_test :

x : the data (corresponding to the sequences)
y : the labels (corresponding to the classes already admitted) 

1/ Download the fasta file of the RNA list, form the [RCSB PDB] data base (https://www.rcsb.org) using `train_get_fasta.py`. (Do it also for the test set). 

2/ Contatenation all the fasta file in a multifasta file

```markdown
cat *.fa > train-multi.fa
```
3/ Get only the sequences from chain A (103 sequence in the final multifasta) to have the input fo the padding step for the trainning step in the file `new_train_multi.fa`

```markdown
grep -A 1 'Chain A' train-multi.fa > new_train_multi.fa
```
4/ Padding of the sequences to have a matrices with the same size for all sequences

5/ Encoding with ONE HOT encoding:
 A: 1 0 0 0
 U: 0 1 0 0
 G: 0 0 1 0
 C: 0 0 0 1  
 N (one base among AUGC): 0 0 0 0
 X (fictiv nt for the padding): 0 0 0 0 

6/ Construction of the MLP using the script `model_prediction_angles.py`
