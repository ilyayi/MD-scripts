import numpy as np

# Gold atom coordinates
au_coords = np.array([
    [54.239552, 50.274750, 49.868160],
    [54.239552, 50.274750, 53.936161],
    [54.239552, 50.274750, 58.004162],
    [54.239552, 50.274750, 62.072159],
    [54.239552, 50.274750, 66.140160],
    [54.239552, 50.274750, 70.208160],
    [54.239552, 50.274750, 74.276161],
    [54.239552, 54.342751, 49.868160],
    [54.239552, 54.342751, 53.936161]
])

# Silver atom coordinates
ag_coords = np.array([
    [-20.427079, -12.256248, -12.256248],
    [-20.427079, -12.256248, -8.170832],
    [-20.427079, -12.256248, -4.085416],
    [-20.427079, -12.256248, 0.000000],
    [-20.427079, -12.256248, 4.085416],
    [-20.427079, -12.256248, 8.170832],
    [-20.427079, -12.256248, 12.256248]
])

# Calculate the range of positions for each axis
x_min = min(np.min(au_coords[:, 0]), np.min(ag_coords[:, 0]))
x_max = max(np.max(au_coords[:, 0]), np.max(ag_coords[:, 0]))
y_min = min(np.min(au_coords[:, 1]), np.min(ag_coords[:, 1]))
y_max = max(np.max(au_coords[:, 1]), np.max(ag_coords[:, 1]))
z_min = min(np.min(au_coords[:, 2]), np.min(ag_coords[:, 2]))
z_max = max(np.max(au_coords[:, 2]), np.max(ag_coords[:, 2]))

# Create a grid of positions for the nanoparticle
x = np.linspace(x_min, x_max, 40)
y = np.linspace(y_min, y_max, 40)
z = np.linspace(z_min, z_max, 40)
grid_x, grid_y, grid_z = np.meshgrid(x, y, z)

# Flatten the grid and select approximately 2000 points for each metal
total_points = 4000
au_indices = np.random.choice(len(x)*len(y)*len(z), size=total_points//2, replace=False)
ag_indices = np.random.choice(len(x)*len(y)*len(z), size=total_points//2, replace=False)

# Create the nanoparticle coordinates
nanoparticle = np.zeros((total_points, 3))
nanoparticle[0:total_points//2, 0] = grid_x.flatten()[au_indices]
nanoparticle[0:total_points//2, 1] = grid_y.flatten()[au_indices]
nanoparticle[0:total_points//2, 2] = grid_z.flatten()[au_indices]
nanoparticle[total_points//2:, 0] = grid_x.flatten()[ag_indices]
nanoparticle[total_points//2:, 1] = grid_y.flatten()[ag_indices]
nanoparticle[total_points//2:, 2] = grid_z.flatten()[ag_indices]

# Write the nanoparticle coordinates to a file
with open("nanoparticle.txt", "w") as f:
    for i in range(total_points):
        f.write(f"{'Au' if i < total_points//2 else 'Ag'} {nanoparticle[i,0]:.6f} {nanoparticle[i,1]:.6f} {nanoparticle[i,2]:.6f}\n")

print("Nanoparticle coordinates saved to 'nanoparticle.txt'.")