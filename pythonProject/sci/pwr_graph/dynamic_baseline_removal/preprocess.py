import numpy as np

# Define input and output file names
input_file = '1FSI_2pt.pwr'
output_file = 'processed_FSI_2pt.pwr'

# Column index for the population data in your file (24th column starting from 1)
population_column = 23  # Zero-based index

# Initialize list to store processed data
processed_data = []

# Open the file and process each line
with open(input_file, 'r') as file:
    for line in file:
        # Strip whitespace and skip empty lines
        line = line.strip()
        if not line or not any(char.isdigit() for char in line):
            continue

        # Split line into columns
        columns = line.split()

        # Ensure there are enough columns for the population data
        if len(columns) <= population_column:
            continue

        # Parse frequency and population value
        try:
            frequency = float(columns[0])
            population = float(columns[population_column])

            # Calculate baseline as the minimum value of each row's data (excluding frequency)
            row_data = [float(value) for value in columns[1:]]
            baseline = min(row_data)
            adjusted_population = population - baseline

            # Append frequency and adjusted population to processed data
            processed_data.append(f"{frequency:.4f} {adjusted_population:.4f}\n")
        except ValueError:
            # Skip lines that don't have valid numerical data
            continue

# Write the processed data to the output file
with open(output_file, 'w') as file:
    file.writelines(processed_data)

print(f"Processed data has been saved to {output_file}.")
