# def replace_column_data(source_path, target_path, column_index, start_row, end_row):
#     # Read source data
#     with open(source_path, 'r') as file:
#         source_lines = file.readlines()
#
#     # Extract column data from source
#     column_data = [
#         line.split()[column_index] if len(line.split()) > column_index else None
#         for line in source_lines[start_row-1:end_row]  # Adjusting for zero-based indexing
#     ]
#
#     print(column_data)
#
#     # Read target data
#     with open(target_path, 'r') as file:
#         target_lines = file.readlines()
#
#     # Replace column data in target
#     for i, line in enumerate(target_lines[start_row-1:end_row]):
#         parts = line.split()
#         if len(parts) > column_index:
#             parts[column_index] = column_data[i]  # Replace the data in the specified column
#         target_lines[i+start_row-1] = ' '.join(parts) + '\n'  # Reconstruct the line and add newline
#
#     # Write the modified data back to the target file
#     with open(target_path, 'w') as file:
#         file.writelines(target_lines)
#
# # Paths to your source and target files
# source_file = '4-chain-dmp-au-edge.bgf'
# target_file = 'comb_dmp_edge.bgf'
#
# # Replace column 10, from row 12 to 83
# replace_column_data(source_file, target_file, 9, 13, 85)  # Column index adjusted for zero-based indexing
#
# print("Column replacement completed successfully.")
def replace_multiple_columns_fixed_width1(source_path, target_path, columns, start_row, end_row, widths):
    # Read source data
    with open(source_path, 'r') as file:
        source_lines = file.readlines()

    # Read target data
    with open(target_path, 'r') as file:
        target_lines = file.readlines()

    # Iterate over each pair of source and target lines within the specified range
    for i, (src_line, tgt_line) in enumerate(
            zip(source_lines[start_row - 1:end_row], target_lines[start_row - 1:end_row])):
        src_parts = src_line.split()
        tgt_parts = tgt_line.split()

        # Replace specified columns if available in both source and target parts
        for col_index in columns:
            if len(src_parts) > col_index and len(tgt_parts) > col_index:
                tgt_parts[col_index] = src_parts[col_index]

        # Reformat each line according to fixed widths
        formatted_line = ""
        current_pos = 0
        for j, part in enumerate(tgt_parts):
            if j >= len(widths):
                print(f"Error: Not enough widths specified for column {j}. Needed at least {j + 1} widths.")
                break
            next_pos = current_pos + widths[j]
            formatted_line += part.ljust(next_pos - len(formatted_line))
            current_pos = next_pos

        # Update the target lines with the newly formatted line
        target_lines[i + start_row - 1] = formatted_line + '\n'

    # Write the modified data back to the target file
    with open(target_path, 'w') as file:
        file.writelines(target_lines)


# Example usage of the function with paths and widths
source_file = 'dmp-au-edge.bgf'
target_file = 'comb_step_dmp_ag.bgf'
columns_to_replace = [9, 10, 11, 12]
column_widths = [11, 2, 8, 2, 6, 3, 10, 10, 9, 7, 2, 3, 10]  # Adjust this based on your file's actual column count

replace_multiple_columns_fixed_width1(source_file, target_file, columns_to_replace, 13, 21, column_widths)

print("Column replacement with fixed-width formatting attempted.")


def replace_multiple_columns_fixed_width(source_path, target_path, columns, start_row, end_row, widths):
    # Read source data
    with open(source_path, 'r') as file:
        source_lines = file.readlines()

    # Read target data
    with open(target_path, 'r') as file:
        target_lines = file.readlines()

    # Iterate over each pair of source and target lines within the specified range
    for i, (src_line, tgt_line) in enumerate(
            zip(source_lines[start_row - 1:end_row], target_lines[start_row - 1:end_row])):
        src_parts = src_line.split()
        tgt_parts = tgt_line.split()

        # Replace specified columns if available in both source and target parts
        for col_index in columns:
            if len(src_parts) > col_index and len(tgt_parts) > col_index:
                tgt_parts[col_index] = src_parts[col_index]

        # Reformat each line according to fixed widths
        formatted_line = ""
        current_pos = 0
        for j, part in enumerate(tgt_parts):
            if j >= len(widths):
                print(f"Error: Not enough widths specified for column {j}. Needed at least {j + 1} widths.")
                break
            next_pos = current_pos + widths[j]
            formatted_line += part.ljust(next_pos - len(formatted_line))
            current_pos = next_pos

        # Update the target lines with the newly formatted line
        target_lines[i + start_row - 1] = formatted_line + '\n'

    # Write the modified data back to the target file
    with open(target_path, 'w') as file:
        file.writelines(target_lines)


# Example usage of the function with paths and widths
source_file = 'dmp-au-edge.bgf'
target_file = 'comb_step_dmp_ag.bgf'
columns_to_replace = [9, 10, 11, 12]
column_widths = [10, 3, 8, 2, 6, 3, 10, 10, 9, 7, 2, 3, 10]  # Adjust this based on your file's actual column count

replace_multiple_columns_fixed_width(source_file, target_file, columns_to_replace, 22, 63, column_widths)

print("Column replacement with fixed-width formatting attempted1.")

