import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 0.01  # Thermal diffusivity
Lx = 1.0      # Length of the x-dimension
Ly = 1.0      # Length of the y-dimension
T = 1.0       # Total time
Nx = 100      # Number of grid points in the x-dimension
Ny = 100      # Number of grid points in the y-dimension
M = 1000      # Number of time steps

# Grid spacing and time step
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)
dt = T / M

# Initialize the temperature array
u = np.zeros((Nx, Ny, M))

# Initial condition: u(x, y, 0) = sin(pi*x)*sin(pi*y)
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)
u[:, :, 0] = np.sin(np.pi * X) * np.sin(np.pi * Y)

# Solve the heat equation
for k in range(0, M - 1):
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            u[i, j, k + 1] = u[i, j, k] + alpha * (
                (u[i - 1, j, k] - 2 * u[i, j, k] + u[i + 1, j, k]) / dx**2 +
                (u[i, j - 1, k] - 2 * u[i, j, k] + u[i, j + 1, k]) / dy**2
            ) * dt

# Plot the results
t = np.linspace(0, T, M)
plt.figure()
plt.imshow(u[:, :, -1], origin='lower', extent=[0, Lx, 0, Ly], aspect='auto')
plt.colorbar(label='Temperature')
plt.xlabel('x')
plt.ylabel('y')
plt.title('2D Heat Equation')
plt.show()