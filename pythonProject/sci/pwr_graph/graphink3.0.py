import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Read the data file, skipping header rows
df = pd.read_csv('baseline_subtracted_FSI_2pt2.txt', skiprows=3, delim_whitespace=True)

# Extract frequency and intensity data
x_data = df.iloc[:, 0]  # Frequency column
y_data = df.iloc[:, 1]  # Intensity column

# Remove any NaN values if present
mask = ~np.isnan(y_data)
x_data = x_data[mask]
y_data = y_data[mask]

# Apply minimal smoothing with Savitzky-Golay filter
window_length = 51  # Must be odd number
poly_order = 0
y_smooth = savgol_filter(y_data, window_length, poly_order)

# Create plot
plt.figure(figsize=(12, 6))

# Plot raw data with minimal processing
plt.plot(x_data, y_smooth, 'b-', linewidth=2)

# Customize plot appearance
plt.xlabel('Frequency (cm⁻¹)', fontsize=12)
plt.ylabel('Intensity', fontsize=12)
plt.title('Raman Spectrum', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.style.use('seaborn-v0_8-bright')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()