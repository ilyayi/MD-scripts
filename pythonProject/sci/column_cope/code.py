def parse_lammpstrj_coords(content):
    """Parse coordinates from lammpstrj format"""
    coords = {}
    lines = content.split('\n')
    # Skip header until we find "ITEM: ATOMS"
    for i, line in enumerate(lines):
        if "ITEM: ATOMS" in line:
            start_line = i + 1
            break

    # Parse coordinates
    for line in lines[start_line:]:
        if line.strip():
            parts = line.split()
            if len(parts) >= 5:  # Make sure we have enough columns
                atom_id = int(parts[0])
                coords[atom_id] = (float(parts[2]), float(parts[3]), float(parts[4]))

    return coords


def parse_dmp_file(content):
    """Parse the dmp file content and return header, atoms section header, and atom lines"""
    lines = content.split('\n')
    header = []
    atoms_header = []
    atoms_section = []
    in_atoms_section = False

    for line in lines:
        if line.strip() == "Atoms":
            in_atoms_section = True
            atoms_header.append(line)
            atoms_header.append("")  # Add empty line after "Atoms"
            continue

        if not in_atoms_section:
            header.append(line)
        elif line.strip():  # If we're in atoms section and line is not empty
            atoms_section.append(line)

    return header, atoms_header, atoms_section


def update_coordinates(atom_line, new_coords):
    """Update coordinates in an atom line while preserving formatting"""
    parts = atom_line.split()
    if len(parts) >= 7:  # Make sure we have enough columns
        atom_id = int(parts[0])
        if atom_id in new_coords:
            # Reconstruct the line with new coordinates but preserve formatting
            new_line = f"{parts[0]:>8}{parts[1]:>9}{parts[2]:>9}{parts[3]:>12}"
            new_line += f"{new_coords[atom_id][0]:>11.5f}"
            new_line += f"{new_coords[atom_id][1]:>11.5f}"
            new_line += f"{new_coords[atom_id][2]:>11.5f}"
            new_line += "    0    0    0"
            return new_line
    return atom_line


def process_files(dmp_content, lammpstrj_content):
    """Process both files and create updated content"""
    # Parse the coordinates from lammpstrj file
    new_coords = parse_lammpstrj_coords(lammpstrj_content)

    # Parse the dmp file
    header, atoms_header, atoms_section = parse_dmp_file(dmp_content)

    # Update coordinates in atoms section
    updated_atoms = []
    for line in atoms_section:
        updated_line = update_coordinates(line, new_coords)
        updated_atoms.append(updated_line)

    # Combine all parts
    updated_content = '\n'.join(header + atoms_header + updated_atoms + [''])
    return updated_content


# Example usage
if __name__ == "__main__":
    import sys

    # Read input files
    with open('data.dmp-np', 'r') as f:
        dmp_content = f.read()

    with open('test2.lammpstrj', 'r') as f:
        lammpstrj_content = f.read()

    # Process files and get updated content
    updated_content = process_files(dmp_content, lammpstrj_content)

    # Write output
    with open('updated_data.dmp-np', 'w') as f:
        f.write(updated_content)