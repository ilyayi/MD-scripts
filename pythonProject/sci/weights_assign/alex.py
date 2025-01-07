import pandas as pd
import numpy as np

def process_binding_to_weights(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Iterate over the columns and check for 'Binding Energy (eV)'
    for i, col in enumerate(df.columns):
        if "Binding Energy (eV)" in str(df.iloc[0, i]):  # Check the first row for the header
            # Copy the 'Binding Energy (eV)' values to the 'Weights' column (next column)
            min_value = df.iloc[1:, i].astype(float).min()


            temp_kelv = 298
            boltz = 1.380649e-23

            binding_e = df.iloc[1:, i].astype(float) * 1.602176634e-19
            min_e = min_value*1.602176634e-19


            result = np.exp(-(binding_e-min_e)/(temp_kelv*boltz))
            df.iloc[1:, i + 1] = result

    return df

# Specify the file path
file_path = 'gulp.csv'

# Process the data
processed_data = process_binding_to_weights(file_path)

# Optionally, save the processed DataFrame back to a CSV file
output_file_path = 'processed_data3.csv'
processed_data.to_csv(output_file_path, index=False)

print(f'Processed data saved to {output_file_path}')
