def process_file(input_file, output_file, divide_by, multiply_by):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_num, line in enumerate(infile):
            # Write the first two lines (header) unchanged
            if line_num < 2:
                outfile.write(line)
            else:
                # Split the line into parts
                parts = line.strip().split()

                # Assume the first part is the atom symbol; process only the coordinates
                atom_symbol = parts[0]
                processed_coords = []

                for coord in parts[1:]:  # Only process numeric coordinates
                    try:
                        # Convert to float, divide, then multiply
                        value = float(coord)
                        processed_value = (value / divide_by) * multiply_by
                        processed_coords.append(f"{processed_value:.6f}")
                    except ValueError:
                        # If part isn't a number, keep it as is
                        processed_coords.append(coord)

                # Write the processed line in the original format
                outfile.write(f"{atom_symbol} {' '.join(processed_coords)}\n")


# Usage example
input_file = 'au_np.cube.xyz'  # Path to the input file
output_file = 'output.xyz'  # Path to the output file
divide_by = 4.068001  # Replace with the actual divisor
multiply_by = 4.085416  # Replace with the actual multiplier

process_file(input_file, output_file, divide_by, multiply_by)
