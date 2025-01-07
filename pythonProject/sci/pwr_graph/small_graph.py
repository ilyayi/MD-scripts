import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def create_plot(excel_file, x_column_index, y_column_index, sheet_name=0):
    """
    Create a line plot from Excel data

    Parameters:
    excel_file (str): Path to the Excel file
    x_column_index (int): Index of the column for x-axis data (0-based)
    y_column_index (int): Index of the column for y-axis data (0-based)
    sheet_name: Sheet to read from (0 by default for first sheet)
    """
    try:
        # Read the Excel file, skipping the first row
        # header=None means don't use first row as column names
        df = pd.read_excel(excel_file,
                           sheet_name=sheet_name,
                           header=None,
                           skiprows=1)

        # Extract the specified columns by index
        x = df.iloc[:, x_column_index].values
        y = df.iloc[:, y_column_index].values

        # Create the figure and axis
        fig, ax = plt.subplots(figsize=(8, 3))

        # Plot the data
        ax.plot(x, y, color='#FFA500', linewidth=1)

        # Customize the plot
        ax.set_title('C4LT', loc='right', pad=10)

        # Add grid
        ax.grid(True, linestyle='-', alpha=0.2)

        # Customize axes
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        # Set axis limits with a bit more padding
        x_padding = (max(x) - min(x)) * 0.05  # 5% padding
        y_padding = (max(y) - min(y)) * 0.05  # 5% padding

        ax.set_xlim(min(x) - x_padding, max(x) + x_padding)
        ax.set_ylim(min(y) - y_padding, max(y) + y_padding)

        # Adjust layout
        plt.tight_layout()

        # Show the plot
        plt.show()

        # Optionally save the plot
        # plt.savefig('c4lt_plot.png', dpi=300, bbox_inches='tight')

    except FileNotFoundError:
        print(f"Error: Could not find the file '{excel_file}'")
    except IndexError:
        print(f"Error: Column index {max(x_column_index, y_column_index)} is out of bounds")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Replace with your actual Excel file path and column indices
    excel_file = "LT_Raman_data.xlsx"
    x_column_index = 2  # First column (0-based index)
    y_column_index = 3  # Second column

    create_plot(excel_file, x_column_index, y_column_index)