import numpy as np
import matplotlib.pyplot as plt


def huckel_solver(H):
    # Solve the Hückel matrix for eigenvalues (MO energies) and eigenvectors (MO coefficients)
    energies, coefficients = np.linalg.eigh(H)

    # Sort the energies and corresponding coefficients
    idx = np.argsort(energies)
    energies = energies[idx]
    coefficients = coefficients[:, idx]

    return energies, coefficients


def plot_energy_levels(energies, coefficients):
    # Identify degeneracies by rounding the energies and grouping them
    rounded_energies = np.round(energies, 4)
    unique_energies, counts = np.unique(rounded_energies, return_counts=True)

    # Create the plot
    plt.figure(figsize=(4, 8))

    # Loop over each unique energy level and plot it
    for i, energy in enumerate(unique_energies):
        # Find indices of the degenerate orbitals
        degenerate_indices = np.where(rounded_energies == energy)[0]
        for j, idx in enumerate(degenerate_indices):
            plt.hlines(energy, 0.2 + 0.2 * j, 0.4 + 0.2 * j, color='black', lw=2)

            # Draw arrows for occupied orbitals (assuming π-electrons fill the lowest energy levels)
            if energy < 0:
                plt.arrow(0.3 + 0.2 * j, energy - 0.05, 0, 0.2, head_width=0.05, head_length=0.1, fc='black',
                          ec='black')

    # Add labels for the energy levels
    labels = [f'{energy:.4f}' for energy in unique_energies]
    for i, energy in enumerate(unique_energies):
        plt.text(0.1, energy, labels[i], verticalalignment='center')

    # Customize the plot
    plt.xlim(0, 1)
    plt.ylim(min(energies) - 0.5, max(energies) + 0.5)
    plt.gca().get_xaxis().set_visible(False)
    plt.ylabel('Energy (in units of beta)')
    plt.title('Molecular Orbital Energy Levels')

    # Show the plot
    plt.show()


# Example usage with a benzene matrix
benzene_matrix = np.array([
    [0, -1, 0, 0, 0, -1],  # C1 connected to C2 and C6
    [-1, 0, -1, 0, 0, 0],  # C2 connected to C1 and C3
    [0, -1, 0, -1, 0, 0],  # C3 connected to C2 and C4
    [0, 0, -1, 0, -1, 0],  # C4 connected to C3 and C5
    [0, 0, 0, -1, 0, -1],  # C5 connected to C4 and C6
    [-1, 0, 0, 0, -1, 0]  # C6 connected to C1 and C5
])

# Solve the Hückel problem for benzene
energies, coefficients = huckel_solver(benzene_matrix)

# Plot the energy levels
plot_energy_levels(energies, coefficients)
