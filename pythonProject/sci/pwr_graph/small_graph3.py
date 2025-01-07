import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline


def clean_signal(signal, threshold=2000, start_index=1750):
    """
    Clean a signal by removing low-amplitude noise after a certain index

    Parameters:
    signal (array-like): Input signal to clean
    threshold (float): Amplitude threshold below which to zero out the signal
    start_index (int): Index after which to apply the threshold

    Returns:
    array: Cleaned signal
    """
    cleaned = signal.copy()

    # Find the index in x that corresponds to start_index
    mask = cleaned > start_index
    cleaned[mask][cleaned[mask] < threshold] = 0

    return cleaned


def create_smooth_plot(excel_file, x_column_index, y_column_index, sheet_name=0):
    """
    Create a smooth line plot from Excel data

    Parameters:
    excel_file (str): Path to the Excel file
    x_column_index (int): Index of the column for x-axis data (0-based)
    y_column_index (int): Index of the column for y-axis data (0-based)
    sheet_name: Sheet to read from (0 by default for first sheet)
    """
    try:
        # Read the Excel file, skipping the first row
        df = pd.read_excel(excel_file,
                           sheet_name=sheet_name,
                           header=None,
                           skiprows=1)

        # Extract the specified columns by index
        x = df.iloc[:, x_column_index].values
        y = df.iloc[:, y_column_index].values

        # Clean data: remove rows with NaN, infinite, or negative values
        valid_mask = ~(np.isnan(x) | np.isnan(y) | np.isinf(x) | np.isinf(y) | (y < 0))
        x = x[valid_mask]
        y = y[valid_mask]

        # Check if we have enough valid data points
        if len(x) < 4:
            raise ValueError("Not enough valid data points after cleaning")

        # Sort the values based on x to ensure strictly increasing sequence
        sort_indices = np.argsort(x)
        x = x[sort_indices]
        y = y[sort_indices]

        # Remove duplicate x values (keep the first occurrence)
        unique_mask = np.concatenate(([True], np.diff(x) > 0))
        x = x[unique_mask]
        y = y[unique_mask]

        # Apply noise removal
        # Find indices where x > 1750
        noise_mask = x > 1750
        y[noise_mask] = np.where(y[noise_mask] < 2000, 0, y[noise_mask])

        # Create the figure and axis with a white background
        plt.style.use('default')
        fig, ax = plt.subplots(figsize=(10, 4))
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')

        # Plot the line (using the actual data points instead of smoothing)
        line, = ax.plot(x, y, color='#8B0000', linewidth=1, label='C8LT')

        # Add grid
        ax.grid(True, linestyle='-', alpha=0.2)

        # Customize axes
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        # Force y-axis to start at 0
        ax.set_ylim(bottom=0)

        # Add legend with larger text and custom style
        legend = ax.legend(
            loc='upper right',
            frameon=True,
            fancybox=True,
            framealpha=1.0,
            bbox_to_anchor=(1.0, 1.0),
            handlelength=1.0,
            handletextpad=0.5,
            prop={'size': 14},
            borderpad=0.8,
            labelspacing=0.5,
        )

        # Make the legend line thicker for better visibility
        legend.get_lines()[0].set_linewidth(2.0)

        # Adjust layout
        plt.tight_layout()

        plt.xlim(500, 2000)
        # Show the plot
        plt.show()

        # Print summary of data cleaning
        print(f"Original data points: {len(df)}")
        print(f"Valid data points after cleaning: {len(x)}")

    except FileNotFoundError:
        print(f"Error: Could not find the file '{excel_file}'")
    except IndexError:
        print(f"Error: Column index {max(x_column_index, y_column_index)} is out of bounds")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    excel_file = "LT_Raman_data2.xlsx"
    x_column_index =0  # First column
    y_column_index = 1  # Second column

    create_smooth_plot(excel_file, x_column_index, y_column_index)
