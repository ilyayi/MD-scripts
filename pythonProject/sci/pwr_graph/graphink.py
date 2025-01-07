import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

import pandas as pd

# Read the data file, skipping the first line
df = pd.read_csv('baseline_subtracted_FSI_2pt2.txt', skiprows=3, delim_whitespace=True)

# Check the column names and structure
print(df.columns)
print(df.head())  # Check the first few rows of the data

# Now, assuming column 24 is correctly indexed, extract the x and y data
x_data = df.iloc[:, 0]  # First column (freq(cm-1))
y_data = df.iloc[:, 1]  # 24th column (PWRRmnS[G002])

print(x_data, y_data)




# Read the data file
# Skip the first line (title) and use the second line as header
# df = pd.read_csv('rerun_2pt.txt', skiprows=1, delim_whitespace=True)
#
# # Extract x and y data
# x_data = df.iloc[:, 0]  # First column (freq(cm-1))
# y_data = df.iloc[:, 23]  # Column 24 (PWRRmnS[G002])
#
# print (x_data, y_data)
# # Remove NaN values
mask = ~np.isnan(y_data)
x_data = x_data[mask]
y_data = y_data[mask]

# Apply Savitzky-Golay filter for smoothing
window_length = 51  # Must be odd number
poly_order = 0
y_smooth = savgol_filter(y_data, window_length, poly_order)

# Create more points for smoother curve
X_smooth = np.linspace(x_data.min(), x_data.max(), 300)
spl = make_interp_spline(x_data, y_smooth, k=3)
Y_smooth = spl(X_smooth)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(X_smooth, Y_smooth, 'b-', linewidth=2)

# Add labels and title
plt.xlabel('Frequency (cm⁻¹)', fontsize=12)
plt.ylabel('Power Spectrum (PWRRmnS[G002])', fontsize=12)
plt.title('Power Spectrum vs Frequency', fontsize=14)

# Add grid
plt.grid(True, linestyle='--', alpha=0.7)

# Customize the appearance
plt.style.use('seaborn-v0_8-bright')
plt.tight_layout()

# Show the plot
plt.show()