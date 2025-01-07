import numpy as np
from scipy.signal import savgol_filter
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def advanced_baseline_correction(x_data, y_data):
    # Parameters for baseline estimation
    window_points = 1001  # Large window to capture the broad background
    poly_degree = 2  # For curved baseline

    # First smoothing to reduce noise
    y_smooth = savgol_filter(y_data, 51, 3)

    # Find baseline using rolling minimum
    baseline = np.zeros_like(y_smooth)
    half_window = window_points // 2

    for i in range(len(y_smooth)):
        start_idx = max(0, i - half_window)
        end_idx = min(len(y_smooth), i + half_window)
        window_data = y_smooth[start_idx:end_idx]
        baseline[i] = np.percentile(window_data, 5)  # Using 5th percentile instead of minimum

    # Smooth the baseline
    baseline = savgol_filter(baseline, window_points, poly_degree)

    # Subtract baseline
    y_corrected = y_smooth - baseline

    # Ensure no negative values
    y_corrected = np.maximum(y_corrected, 0)

    return y_corrected, baseline


# Read the data
df = pd.read_csv('baseline_subtracted_FSI_2pt2.txt', skiprows=3, delim_whitespace=True)
x_data = df.iloc[:, 0].values
y_data = df.iloc[:, 1].values

# Apply baseline correction
y_corrected, baseline = advanced_baseline_correction(x_data, y_data)

# Create visualization
plt.figure(figsize=(12, 8))

# Plot original and corrected data
plt.subplot(211)
plt.plot(x_data, y_data, 'b-', label='Original', linewidth=1)
plt.plot(x_data, baseline, 'r--', label='Estimated Baseline', linewidth=1)
plt.xlabel('Frequency (cm⁻¹)')
plt.ylabel('Intensity')
plt.title('Original Spectrum with Estimated Baseline')
plt.grid(True, alpha=0.3)
plt.legend()

plt.subplot(212)
plt.plot(x_data, y_corrected, 'b-', linewidth=1)
plt.xlabel('Frequency (cm⁻¹)')
plt.ylabel('Intensity')
plt.title('Baseline Corrected Spectrum')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Save corrected data
output_file = 'fully_corrected_spectrum.txt'
with open(output_file, 'w') as f:
    for x, y in zip(x_data, y_corrected):
        f.write(f"{x:.6f} {y:.6f}\n")

print(f"Corrected spectrum saved to {output_file}")