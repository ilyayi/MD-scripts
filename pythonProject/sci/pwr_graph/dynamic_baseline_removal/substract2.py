import numpy as np
from scipy.signal import savgol_filter

# Input and output file names
input_file = '1FSI_2pt.pwr'
output_file = 'baseline_subtracted_FSI_2pt2.pwr'

# Parameters for baseline correction
window_size = 501  # Should be odd number, adjust based on your peak widths
poly_order = 3  # Polynomial order for smoothing
percentile = 1  # Percentile for baseline estimation


def read_spectrum_data(filename, pop_column=23):  # 24th column (0-based indexing)
    frequencies = []
    intensities = []

    with open(filename, 'r') as file:
        for line in file:
            try:
                values = line.strip().split()
                if len(values) > pop_column:
                    freq = float(values[0])
                    intensity = float(values[pop_column])
                    frequencies.append(freq)
                    intensities.append(intensity)
            except (ValueError, IndexError):
                continue

    return np.array(frequencies), np.array(intensities)


def subtract_baseline(frequencies, intensities):
    # Create a rolling window to find local minima
    half_window = window_size // 2
    baseline = np.zeros_like(intensities)

    for i in range(len(intensities)):
        start_idx = max(0, i - half_window)
        end_idx = min(len(intensities), i + half_window)
        window_data = intensities[start_idx:end_idx]
        baseline[i] = np.percentile(window_data, percentile)

    # Smooth the baseline
    baseline = savgol_filter(baseline, window_size, poly_order)

    # Subtract baseline and ensure no negative values
    corrected = intensities - baseline
    corrected = np.maximum(corrected, 0)

    return corrected, baseline


def main():
    # Read data
    print("Reading spectrum data...")
    frequencies, intensities = read_spectrum_data(input_file)

    # Process data
    print("Subtracting baseline...")
    corrected_intensities, baseline = subtract_baseline(frequencies, intensities)

    # Save results
    print("Saving processed data...")
    with open(output_file, 'w') as f:
        for freq, intensity in zip(frequencies, corrected_intensities):
            if intensity > 0.01 * np.max(corrected_intensities):  # Filter out noise
                f.write(f"{freq:.6f} {intensity:.6f}\n")

    print(f"Processing complete. Results saved to {output_file}")

    # Return arrays for plotting if needed
    return frequencies, corrected_intensities, baseline


if __name__ == "__main__":
    frequencies, corrected, baseline = main()

