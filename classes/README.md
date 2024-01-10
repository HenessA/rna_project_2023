# Classification step 

The aim is to associate a class (define by the previous distribution graph) to each values of torsion angles. 

First, select the sequence colomn and the angle choosen : 
```markdown
for i in $(cat train-list-pdb.txt); do awk -F',' '{print $17 "\t" $19}' ${i}-res.txt > ../header_train_20class/${i}.pdb_eta_second_seq_A.txt;done;
```

