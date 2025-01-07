import pandas as pd
import numpy as np

def binding_to_morse(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Iterate over the columns and check for 'Binding Energy (eV)'
    for i, col in enumerate(df.columns):
        print(df.iloc[6, i])
        if "V(r)" in str(df.iloc[6, i]):  # Check the first row for the header
            # Copy the 'Binding Energy (eV)' values to the 'Weights' column (next column)

            dE = float(df.iloc[1, i])
            a = float(df.iloc[2, i])
            r0 = float(df.iloc[3, i])
            # kE = float(df.iloc[4, i])
            #
            r1 = df.iloc[7:, i-1].astype(float)

            # print(r1)
            result = dE*((1-(np.exp(-a*(r1-r0))))**2)
            print(result)
            df.iloc[7:7+len(result), i] = result


    return df

# Specify the file path
file_path = 'morse.csv'

# Process the data
processed_data = binding_to_morse(file_path)

# Optionally, save the processed DataFrame back to a CSV file
output_file_path = 'processed_data5.csv'
processed_data.to_csv(output_file_path, index=False)
#
print(f'Processed data saved to {output_file_path}')
