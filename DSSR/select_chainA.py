### Script to select only the chain A in PDB files 

import os

# Set the directory to the folder which contain your pdb file previously download from the database
pdb_directory = "path/to/your/train/file/directory"

# Iterate through all files in the directory
for file in os.listdir(pdb_directory):
    if file.endswith(".pdb"):
        # Build the full path of the input file
        input_file_path = os.path.join(pdb_directory, file)

        # Build the full path of the output file
        output_file_path = os.path.join(pdb_directory, f"{file}")

        # List to store lines for chain "A"
        chain_a_lines = []

        # Open the PDB file and read lines
        with open(input_file_path, 'r') as pdb_file:
            for line in pdb_file:
                # Check if the line is for chain "A"
                if line[21:22] == "A":
                    chain_a_lines.append(line.strip())

        # Write the lines for chain "A" to the output file
        with open(output_file_path, 'w') as output_file:
            for line in chain_a_lines:
                output_file.write(line + "\n")

# Now, an output file named "file.pdb" will be created for each PDB file in the output directory

