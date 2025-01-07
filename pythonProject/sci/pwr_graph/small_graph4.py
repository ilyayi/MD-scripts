import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.signal import savgol_filter

def create_smooth_plot(excel_file, x_column_index, y_column_index, sheet_name=0):
    """
    Create a smooth line plot from Excel data with enhanced noise removal
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

        # Enhanced noise removal
        # First pass: remove low amplitude signals after x=1750
        noise_mask = x > 1750
        y[noise_mask] = np.where(y[noise_mask] < 3000, 0, y[noise_mask])

        # Second pass: apply Savitzky-Golay filter for smoothing
        y_smooth = savgol_filter(y, window_length=11, polyorder=3)

        # Third pass: remove remaining noise
        # Find the main signal end point (where values consistently drop to near zero)
        signal_end_mask = x > 1750
        y_smooth[signal_end_mask] = np.where(y_smooth[signal_end_mask] < 1000, 0, y_smooth[signal_end_mask])

        # Fourth pass: clean up any remaining isolated peaks
        window_size = 5
        for i in range(len(y_smooth)-window_size):
            if x[i] > 1750:  # Only apply to the latter part of the signal
                window = y_smooth[i:i+window_size]
                if np.mean(window) < 1000:  # If the window average is low
                    y_smooth[i:i+window_size] = 0  # Zero out the entire window

        # Create the figure and axis with a white background
        plt.style.use('default')
        fig, ax = plt.subplots(figsize=(10, 4))
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')

        # Plot the smoothed line
        line, = ax.plot(x, y_smooth, color='#8B0000', linewidth=1, label='C8LT')

        # Customize the plot
        ax.set_title('C8LT', loc='right', pad=10)

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

        # plt.xlim(500, 2500)
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
    x_column_index = 2  # First column
    y_column_index = 3  # Second column

    create_smooth_plot(excel_file, x_column_index, y_column_index)