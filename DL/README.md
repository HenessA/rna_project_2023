# Deep Learning - Model of pseudo torsion eta'' angle prediction

The first strep of the DL part was to process the data to get  X_train,X_test, y_train, y_test:

x : the data (corresponding to the sequences)
y : the labels (corresponding to the classes already admitted) 

1/ Download the fasta file of the RNA list, form the [RCSB PDB] data base (https://www.rcsb.org) using `train_get_fasta.py`

2/ Contatenation all the fasta file in a multifasta file

```markdown
cat *.fa > train-multi.fa
```
3/ Get only the sequences from chain A (103 sequence in the final multifasta) to have the input fo the padding step for the trainning step in the file `new_train_multi.fa`

```markdown
grep -A 1 'Chain A' train-multi.fa > new_train_multi.fa
```



#(fill according to the colab file)
Padding step : 

ONE HOT ENCODING step : 

MLP :
