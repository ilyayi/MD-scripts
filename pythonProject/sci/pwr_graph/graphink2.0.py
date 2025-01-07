import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

df_slice = pd.read_csv('rerun_2pt.txt', skiprows=3, delim_whitespace=True)
x_data = df_slice.iloc[:, 0]
y_data = df_slice.iloc[:, 23]

mask = ~np.isnan(y_data)
x_data = x_data[mask]
y_data = y_data[mask]

# Set the 'sharpness'
window_length = 51
poly_order = 7
y_smooth = savgol_filter(y_data, window_length, poly_order)

# Create more points for smoother curve
X_smooth = np.linspace(x_data.min(), x_data.max(), 1000)
spl = make_interp_spline(x_data, y_smooth, k=3)
Y_smooth = spl(X_smooth)

# Create the plot with matching style
plt.figure(figsize=(12, 8))

# Plot with specific style
plt.plot(X_smooth, Y_smooth, '-', color='purple', linewidth=1,
         label='4-chain DMP')

# Set title and labels
plt.title('Simulated Raman Spectra', y=1.02, fontsize=12)
plt.xlabel('Frequency (cm^{-1})', fontsize=15)
plt.ylabel('Population', fontsize=15)

# Set axis ranges
plt.xlim(0, 3500)
plt.ylim(-1.3e10, 0)

# Format y-axis to use scientific notation
plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.1e'))

# Customize grid
plt.grid(True, linestyle='-', alpha=0.2)

# Move legend to bottom right
plt.legend(loc='lower right', frameon=True, fontsize=18)

# Set white background with frame
plt.gca().set_facecolor('white')
for spine in plt.gca().spines.values():
    spine.set_color('black')
    spine.set_linewidth(1.0)

# Add minor ticks
plt.minorticks_on()
plt.tick_params(which='both', direction='in')
plt.tick_params(which='major', length=6)
plt.tick_params(which='minor', length=3)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()