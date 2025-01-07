# Python script for baseline subtraction
import numpy as np

# Input and output file names
input_file = '1FSI_2pt.pwr'
output_file = 'baseline_subtracted_FSI_2pt1.pwr'

# Column index for the population data in your file (24th column, zero-based index)
population_column = 23  # Zero-based index

# Initialize list to store processed data
processed_data = []

# Open the file and process each line
with open(input_file, 'r') as file:
    line_count = 0  # Line counter for debugging
    for line in file:
        line_count += 1
        line = line.strip()  # Remove leading and trailing whitespace

        # Skip header or blank lines
        if not line or not any(char.isdigit() for char in line):
            print(f"Skipping line {line_count}: Not data")
            continue

        # Split line into columns based on whitespace
        columns = line.split()

        # Debug: Print the number of columns in the line
        print(f"Processing line {line_count}: {len(columns)} columns")

        # Ensure there are enough columns for the population data
        if len(columns) <= population_column:
            print(f"Skipping line {line_count}: Insufficient columns")
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
        except ValueError as e:
            # Skip lines that don't have valid numerical data and print error
            print(f"Skipping line {line_count}: {e}")
            continue

# Write the processed data to the output file
with open(output_file, 'w') as file:
    file.writelines(processed_data)

print(f"Processed data has been saved to {output_file}.")

