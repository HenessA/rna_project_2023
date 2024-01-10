# Classification step 

The aim is to associate a class (defined by the previous distribution graph) to each values of torsion angles. 

First, select the sequence colomn and the angle colomn choosen : 
```markdown
for i in $(cat train-list-pdb.txt); do awk -F',' '{print $17 "\t" $19}' ${i}-res.txt > ../header_train_20class/${i}.pdb_eta_second_seq_A.txt;done;
```

Then, get the maximum length of the sequence of the data set (train and test), to process the padding step :

```markdown
for i in $(cat train-list-pdb.txt); do awk 'NR>1' ${i}_eta_second_seq_A.txt > ../wc_header_train_binaire/${i}_eta_second_seq_B;done;


#bash command to find the file with the maximal length for the padding=> 3IGI=>387nt

max_lignes=0
fichier_max=""

for fichier in $(cat train-list-pdb.txt); do
    nombre_lignes=$(wc -l < "${fichier}_eta_second_seq_B")

    if [ "$nombre_lignes" -gt "$max_lignes" ]; then
        max_lignes=$nombre_lignes
        fichier_max="$fichier"

```
Knowing the maximum length, add "X" to the shortest sequences to get uniform lengths :

```markdown
```
