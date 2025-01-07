import pandas as pd
import numpy as np

def xyz_to_df(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    df1 = df.iloc[1:, :]
#
#
#     print(df1)
#     # Iterate over the columns and check for 'Binding Energy (eV)'
#     # for i, col in enumerate(df.columns):
#     #     print(df.iloc[6, i])
#     #     if "V(r)" in str(df.iloc[6, i]):  # Check the first row for the header
#     #         # Copy the 'Binding Energy (eV)' values to the 'Weights' column (next column)
#     #
#     #         dE = float(df.iloc[1, i])
#     #         a = float(df.iloc[2, i])
#     #         r0 = float(df.iloc[3, i])
#     #         # kE = float(df.iloc[4, i])
#     #         #
#     #         r1 = df.iloc[7:, i-1].astype(float)
#     #
#     #         # print(r1)
#     #         result = dE*((1-(np.exp(-a*(r1-r0))))**2)
#     #         print(result)
#     #         df.iloc[7:7+len(result), i] = result
#     #
#
#     return df1

# Specify the file path
file_path = 'ilya-relaxed.xyz'
file_path2 = 'ilya-not-relaxed.bgf'

# Process the data
# processed_data = xyz_to_df(file_path)


def df_to_bgf(filepath):
    df2 = pd.read_table(file_path2)
    # df = df2.iloc[2:76, :3]

    print(df2)

    return df2

pro_data = df_to_bgf(file_path2)

# # Optionally, save the processed DataFrame back to a CSV file
# output_file_path = 'processed_data.bgf'
# processed_data.to_csv(output_file_path, index=False)
# #
# print(f'Processed data saved to {output_file_path}')