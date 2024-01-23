import numpy as np
import matplotlib.pyplot as plt

def calculate_reynolds(U, rho, mu, L):
    # Calculate Reynolds number
    # U: Velocity [units: m/s]
    # rho: Density [units: kg/m^3]
    # mu: Viscosity [units: Pa·s or kg/m·s]
    # L: Length [units: meters]
    Re = (U * L) / mu
    return Re

def discretize_blasius(num_nodes, eta_max, U, rho, mu, L):
    Re = calculate_reynolds(U, rho, mu, L)

    if Re >= 500000: #Re can't exceed 500,000, and if it does the code will stop
        print("Reynolds number exceeds 500,000. Blasius solution is not applicable.")
        return

    eta = np.linspace(0, eta_max, num_nodes)

    d_eta = eta[1] - eta[0]  # Step size in dimensionless space [no unit]

    f = np.zeros(num_nodes)
    f_prime = np.zeros(num_nodes)
    f_dbl_prime = np.zeros(num_nodes)
    f_triple_prime = np.zeros(num_nodes)

    f[0] = 0  # Dimensionless quantity [no unit]
    f_prime[0] = 0  # Dimensionless quantity [no unit]
    f_dbl_prime[0] = 0.332  # Blasius solution initial condition for f''(0) [no unit]

    # Newton's method iteration
    max_iter = 1000
    tolerance = 1e-6
    for _ in range(max_iter):
        f_old = f.copy()

        # Update using central difference scheme
        for i in range(1, num_nodes):
            f_triple_prime[i] = -0.5 * f[i] * f_dbl_prime[i]  # Dimensionless quantity [no unit]
            f_dbl_prime[i] = f_dbl_prime[i - 1] + d_eta * f_triple_prime[i]  # Dimensionless quantity [no unit]
            f_prime[i] = f_prime[i - 1] + d_eta * f_dbl_prime[i]  # Dimensionless quantity [no unit]
            f[i] = f[i - 1] + 0.5 * d_eta * (f_prime[i] + f_prime[i - 1])  # Dimensionless quantity [no unit]

        # Check for convergence
        if np.max(np.abs(f - f_old)) < tolerance:
            break

    plt.plot(eta, f_prime, label="f'(\u03B7)")
    plt.legend()
    plt.grid(True)
    plt.show()

# User inputs
U = float(input("Enter the free stream velocity (U) [units: m/s]: "))
rho = float(input("Enter the density (\u03C1) [units: kg/m^3]: "))
mu = float(input("Enter the viscosity (\u03BC) [units: Pa·s or kg/m·s]: "))
L = float(input("Enter the length of the plate (L) [units: meters]: "))
num_nodes = int(input("Enter the number of nodes [no unit]: "))
eta_max = float(input("Enter the maximum \u03B7 value [no unit]: "))

discretize_blasius(num_nodes, eta_max, U, rho, mu, L)