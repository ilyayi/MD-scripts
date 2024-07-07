import pandas as pd
import numpy as np

def binding_to_morse(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Iterate over the columns and check for 'Binding Energy (eV)'
    for i, col in enumerate(df.columns):

        if "17" in str(df.iloc[0, i]):  # Check the first row for the header
            # print(df.iloc[0:, i])
            result = df.iloc[0:, i].astype(float)
            df.iloc[0:, 1] = result
            print(df)

    return df

# Specify the file path
file_path = 'test.csv'

# Process the data
processed_data = binding_to_morse(file_path)

# Optionally, save the processed DataFrame back to a CSV file
# output_file_path = 'processed_data.csv'
# processed_data.to_csv(output_file_path, index=False)
#
# print(f'Processed data saved to {output_file_path}')
