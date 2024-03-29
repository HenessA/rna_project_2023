# Discretisation of angles 

Goal : associate a class  beyond the 21 class (defined by the previous distribution graph) to each values of torsion angles of **eta''**. 

1/ Select the sequence in the 19e colomn and the **eta''** values in the 17e colum with awk command : 

```markdown
for i in $(cat train-list-pdb.txt); do awk -F',' '{print $17 "\t" $19}' ${i}-res.txt > ../header_train_21class/${i}_eta_second_seq_A.txt;done;
```

2/ Remove the header of all the files with awk command : 

```markdown
for i in $(cat train-list-pdb.txt); do awk 'NR>1' ${i}_eta_second_seq_A.txt > ../wc_header_train_binaire/${i}_eta_second_seq_B;done;
```
3/ Find the file with the maximal length of the data set (train and test) to process the padding step :

```markdown
max_lignes=0
fichier_max=""

for fichier in $(cat train-list-pdb.txt); do
    nombre_lignes=$(wc -l < "${fichier}_eta_second_seq_B")
    
    if [ "$nombre_lignes" -gt "$max_lignes" ]; then
        max_lignes=$nombre_lignes
        fichier_max="$fichier"
    
done

echo "Le fichier avec le plus grand nombre de lignes est : $fichier_max"
echo "Nombre de lignes : $max_lignes"

```

4/ Knowing the maximum length, add "X" to the other shortest sequences( length<387) to get uniform lengths :

```markdown
for fichier in $(cat train-list-pdb.txt); do
    nombre_lignes=$(wc -l < "${fichier}_eta_second_seq_B")
    
    if [ "$nombre_lignes" -lt 387 ]; then
        lignes_manquantes=$((387 - nombre_lignes))
        printf "PAD\tX\n%.0s" $(seq "$lignes_manquantes") | "${fichier}_eta_second_seq_B.txt" >  "${fichier}_eta_second_seq_B_PAD.txt"
    
done
```

5/ Replace the first column by the class defined in the dssr step after the distribution :

```markdown
for i in $(cat train-list-pdb.txt); do
    awk 'BEGIN {FS = "\t"; OFS = "\t"} {
        if ($1 == "PAD") { #if it's padding (PAD) the class will be 20
            $1 = 20;
        } else if ($1 == "NA") { #if it's a NA the class will be 19
            $1 = 19;
        } else {
            val = $1 + 0;  # Convert the first column to a float

            #all the condition for the float to assign them the right class
            if (val <= -170) $1 = 0;
            else if (val <= -160 && val > -170) $1 = 1;
            else if (val <= -150 && val > -160) $1 = 2;
            else if (val <= -140 && val > -150) $1 = 3;
            else if (val <= -130 && val > -140) $1 = 4;
            else if (val <= -120 && val > -130) $1 = 5;
            else if (val <= -110 && val > -120) $1 = 6;
            else if (val <= -100 && val > -110) $1 = 7;
            else if (val <= -90 && val > -100) $1 = 8;
            else if (val <= -80 && val > -90) $1 = 9;
            else if (val <= -70 && val > -80) $1 = 10;
            else if (val <= -60 && val > -70) $1 = 11;
            else if (val <= -50 && val > -60) $1 = 12;
            else if (val <= 20 && val > -50) $1 = 13;
            else if (val <= 40 && val > 20) $1 = 14;
            else if (val <= 100 && val > 40) $1 = 15;
            else if (val <= 140 && val > 100) $1 = 16;
            else if (val <= 160 && val > 140) $1 = 17;
            else if (val <= 180 && val > 160) $1 = 18;
        }
        print $0;
    }' "${i}_eta_second_seq_B" > "${i}_eta_second_seq_C.txt"
done

```

6/ Build a list of list with the class of angles :
   * each list in the big list represents the angles of each base of one pdb sequence
   * the file contains all the class of angle of each sequence of the training set

_create a list of the first col with the class of _angle_ for each file_

```markdown
for i in $(cat train-list-pdb.txt); do awk '{printf "%s,", $1} END {printf "\n"}' ${i}_eta_second_seq_C.txt | sed 's/,$//' | awk '{print "[" $0 "]" }' > ../vect/${i}_eta_for_y_train.txt; done;
```

_creation of the concatenate file (Y_train.txt) with initial "[" and "]"_
     
```markdown
echo -n "[" > Y_train.txt
```
_concatenation of all the file ending with ".txt"_
     
```markdown
for file in *.txt; do
    cat "$file" >> Y_train.txt
    echo -n "," >> Y_train.txt
done
```
_add the final "]"_
     
```markdown
echo "]" >> Y_train.txt
```

6/ Distribution of the 21 classes of **eta''** angles in R using `distribution_eta_angles.R`.

![image](https://github.com/HenessA/rna_project_2023/assets/94346915/f4e4eb30-e68d-47cd-b267-25c816a29ad7)

![image](https://github.com/HenessA/rna_project_2023/assets/94346915/3359da89-b32f-4c32-84fa-aeb8489edd53)


The python script `test-MAE.py` generate the mean of each classes and associate them to the real angle values. At the end we have a list of mean, to plot the distribution, but it must be changed to only get one mean ... to continue ... 



    
     

     
