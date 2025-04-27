def replace_xyz_with_new_values(input_file, replacement_file, output_file):
    """
    Replace the X, Y, and Z coordinates in a file with new values from another file.

    Parameters:
    - input_file (str): Path to the input file with the original structure.
    - replacement_file (str): Path to the file with new X, Y, Z values.
    - output_file (str): Path to the output file with updated coordinates.
    """
    with open(input_file, 'r') as infile, open(replacement_file, 'r') as refile, open(output_file, 'w') as outfile:
        replacement_lines = refile.readlines()
        replacement_idx = 0

        for line in infile:
            if line.strip().startswith("Au"):  # Process only lines with atomic data
                columns = line.strip().split()
                if replacement_idx < len(replacement_lines):
                    # Replace X, Y, Z with values from the replacement file
                    new_values = replacement_lines[replacement_idx].strip().split()
                    columns[1:4] = new_values[:3]  # Replace columns 1, 2, and 3
                    replacement_idx += 1
                outfile.write("       ".join(columns) + "\n")
            else:
                # Write unchanged lines (e.g., header)
                outfile.write(line)

# Example usage
input_file = "transformed.txt"  # Original structure file
replacement_file = "transformed_coordinates.txt"  # File with new X, Y, Z values
output_file = "output.txt"  # File to save the updated structure

replace_xyz_with_new_values(input_file, replacement_file, output_file)
