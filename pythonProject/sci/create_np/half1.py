# Load the new file and delete every other line to reduce the file size by half

# Define file path
input_file_path = 'relaxed-ag-unitcell-nanocluster.cube.xyz'

# Read the contents of the file
with open(input_file_path, 'r') as input_file:
    file_content = input_file.readlines()

# Select every other line from the file
reduced_content = file_content[::2]

# Write the reduced content to a new file
output_reduced_file_path = 'reduced_relaxed_ag_unitcell_nanocluster.cube.xyz'
with open(output_reduced_file_path, 'w') as output_file:
    output_file.writelines(reduced_content)

