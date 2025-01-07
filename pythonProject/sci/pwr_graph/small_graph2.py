import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline


def create_smooth_plot(excel_file, x_column_index, y_column_index, sheet_name=0):
    try:
        # Read the Excel file, skipping the first row
        df = pd.read_excel(excel_file,
                           sheet_name=sheet_name,
                           header=None,
                           skiprows=1)

        # Extract the specified columns by index
        x = df.iloc[:, x_column_index].values
        y = df.iloc[:, y_column_index].values

        # Sort the values based on x to ensure strictly increasing sequence
        sort_indices = np.argsort(x)
        x = x[sort_indices]
        y = y[sort_indices]

        # Generate a larger number of points for smoother curve
        x_smooth = np.linspace(min(x), max(x), 300)

        # Create B-spline
        spl = make_interp_spline(x, y, k=3)  # k=3 means cubic spline
        y_smooth = spl(x_smooth)

        # Create the figure and axis
        fig, ax = plt.subplots(figsize=(8, 3))

        # Plot the smooth line
        line, = ax.plot(x_smooth, y_smooth, color='#AA4A44', linewidth=1, label='C8LT')

        # Add grid
        ax.grid(True, linestyle='-', alpha=0.2)

        # Customize axes
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        # Set axis limits with padding
        x_padding = (max(x) - min(x)) * 0.05
        y_padding = (max(y) - min(y)) * 0.05

        ax.set_xlim(min(x) - x_padding, max(x) + x_padding)
        ax.set_ylim(min(y) - y_padding, max(y) + y_padding)

        # Add legend with custom style
        legend = ax.legend(
            loc='upper right',  # Position of legend
            frameon=True,  # Show legend frame
            fancybox=True,  # Round corners
            framealpha=1.0,  # Fully opaque background
            bbox_to_anchor=(1.0, 1.0),  # Position relative to plot
            handlelength=3.0,  # Length of legend lines
            handletextpad=2.0,  # Space between line and text
            prop={'size': 14},  # Increase font size
            labelspacing=0.5,
        )

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



# Usage
if __name__ == "__main__":
    excel_file = "LT_Raman_data2.xlsx"
    x_column_index = 0  # First column
    y_column_index = 1  # Second column

    create_smooth_plot(excel_file, x_column_index, y_column_index)
    # print(x_column_index, y_column_index)