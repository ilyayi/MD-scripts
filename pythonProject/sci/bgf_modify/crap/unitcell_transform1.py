import re

def transform_coordinates(input_file, output_file, ag_distance=4.0854158401, au_distance=4.1216025300):
    scale_factor = au_distance / ag_distance

    with open(input_file, 'r') as f, open(output_file, 'w') as out_f:
        for line in f:
            if line.startswith('HETATM'):
                parts = re.split(r'\s+', line.rstrip())
                atom_number = int(parts[1])

                # Check and transform coordinates that start with 35
                coords = [parts[5], parts[6], parts[7]]
                new_coords = []
                for coord in coords:
                    if coord.strip().startswith('35'):
                        new_coord = str(round(float(coord) * scale_factor, 5))
                        new_coords.append(new_coord.rjust(10))
                    else:
                        new_coords.append(coord.rjust(10))

                # Reconstruct line with new coordinates while preserving original formatting
                parts[5] = new_coords[0]
                parts[6] = new_coords[1]
                parts[7] = new_coords[2]

                # Adjust atom number and 'X' formatting
                parts[1] = f"{atom_number:>6}"
                parts[3] = f"X{parts[3]:>5}"

                out_f.write(''.join(parts) + '\n')
            else:
                out_f.write(line)

transform_coordinates('30-angstrom-cube-center-Au-corrected.txt', 'transformed_coordinates1.txt')