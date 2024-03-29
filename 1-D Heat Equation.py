import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 0.01  # Thermal diffusivity
L = 1.0       # Length of the rod
T = 10.0       # Total time
N = 100       # Number of grid points
M = 1000      # Number of time steps

# Grid spacing and time step
dx = L / (N - 1)
dt = T / M

# Initialize the temperature array
u = np.zeros((N, M))

# Initial condition: u(x, 0) = sin(pi*x)
x = np.linspace(0, L, N)
u[:, 0] = np.sin(np.pi * x)

# Solve the heat equation
for j in range(0, M - 1):
    for i in range(1, N - 1):
        u[i, j + 1] = u[i, j] + alpha * (u[i - 1, j] - 2 * u[i, j] + u[i + 1, j]) * dt / dx**2

# Plot the results
t = np.linspace(0, T, M)
plt.figure()
plt.imshow(u.T, origin='lower', extent=[0, L, 0, T], aspect='auto')
plt.colorbar(label='Temperature')
plt.xlabel('Position')
plt.ylabel('Time')
plt.title('1D Heat Equation')
plt.show()
