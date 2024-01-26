import os 

true_angle = []
pred_angle = []
mean_class = []

# Get the list of intervals that make the class
for i in range(-185, -115, 5):
    if i + 20 <= -105:
        mean_class_value = (i + (i + 20)) / 2
        mean_class.append(mean_class_value)

additional_values = [-15, 30, 70, 120, 150, 170]

mean_class.extend(additional_values)
print(mean_class)

with open("train-fichier-concatene_20class.txt", "r") as class_data:
    for line in class_data:
        line = line.split()
        #print(line[0])
        if line[0] == '0':  # Corrected comparison to string '1'
            pred_angle.append(mean_class[0])
        elif line[0] == '1':
            pred_angle.append(mean_class[1])
        elif line[0] == '2':
            pred_angle.append(mean_class[2])
        elif line[0] == '3':
            pred_angle.append(mean_class[3])
        elif line[0] == '4':
            pred_angle.append(mean_class[4])	
        elif line[0] == '5':
            pred_angle.append(mean_class[5])	
        elif line[0] == '6':
            pred_angle.append(mean_class[6])	
        elif line[0] == '7':
            pred_angle.append(mean_class[7])		
        elif line[0] == '8':
            pred_angle.append(mean_class[8])	
        elif line[0] == '9':
            pred_angle.append(mean_class[9])
        elif line[0] == '10':
            pred_angle.append(mean_class[10])	
        elif line[0] == '11':
            pred_angle.append(mean_class[11])									
        elif line[0] == '12':
            pred_angle.append(mean_class[17])
        

with open("train-eta-concatene.txt", 'r') as data:
    for line in data:
        columns = line.split()  # Split the line into columns
        
        # Check if there are at least three columns in the line
        if len(columns) >= 3:
            third_column = columns[2]  # Extract the third column (index 2 since indexing is 0-based)
            
            if '"eta"""' not in third_column:
                try:
                    third_column_float = float(third_column)  # Convert the third column value to float
                    
                    # Append the third column value to the list true_angle
                    true_angle.append(third_column_float)
                except ValueError:
                    print(f"Could not convert string to float: {third_column} on line: {line}")

# Now true_angle contains all the valid values from the third column as floats
# ...

resultat = []
for val1, val2 in zip(pred_angle, true_angle):
    resultat.append(val1 - val2)
resultat_arrondi = [round(diff, 2) for diff in resultat]  # Round each element to 2 decimal places

#print(resultat_arrondi)


MAE= []
 
for diff in resultat_arrondi:
    absolute_diff = abs(diff)
    complementary_diff = abs(360 - absolute_diff)
    MAE.append(min(absolute_diff, complementary_diff))

print("Individual Mean Absolute Errors:")
for mae_value in MAE:
    print(mae_value)


