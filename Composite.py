import numpy as np
import matplotlib.pyplot as plt

# Material properties for PLA
pla_properties = {
    'E': 5.2e9,  # Young's modulus in Pa
    'nu': 0.3,  # Poisson's ratio
    'density': 1250,  # Density in kg/m^3
    'alpha': 70e-6,  # Coefficient of thermal expansion in 1/degC
    'Q11': 2.5e9,  # Stiffness matrix component in Pa
    'Q12': 0.3e9,
    'Q16': 0,
    'Q22': 2.5e9,
    'Q26': 0,
    'Q66': 0.1e9,
    'Tsai_Hill_Xt': 39.9,  
    'Tsai_Hill_Xc': 48.2,
    'Tsai_Hill_S': 52.5
}

# Material properties for CFRP
cfrp_properties = {
    'E': 181e9,
    'nu': 0.27,
    'density': 1600,
    'alpha': 1e-6,
    'Q11': 200.12e9,
    'Q12': 0.6e9,
    'Q16': 0,
    'Q22': 200.12e9,
    'Q26': 0,
    'Q66': 5e9,
    'Tsai_Hill_Xt': 1000,
    'Tsai_Hill_Xc': 500,
    'Tsai_Hill_S': 30
}

# Beam properties
beam_length = 0.095  # Length of the beam in meters
live_load = 61.84  # Live load in Newtons
temperature_difference = 15.0  # Temperature difference in degrees Celsius
beam_volume = beam_length*0.020*0.018
beam_mass_CFRP = cfrp_properties['density']*beam_volume
beam_mass_PLA = pla_properties['density']*beam_volume
print("Mass of PLA:",beam_mass_PLA)
print("Mass of CFRP:",beam_mass_CFRP)

# Given moment of inertia
given_moment_of_inertia = 12000  # in mm^4

# Calculate the deflection for PLA and CFRP beams using the given moment of inertia
def calculate_deflection_with_given_inertia(E, I, L, load):
    return (load * L**3) / (48 * E * I)

# Calculate the deflection for PLA and CFRP beams
pla_deflection = calculate_deflection_with_given_inertia(pla_properties['E'], given_moment_of_inertia, beam_length, live_load)
cfrp_deflection = calculate_deflection_with_given_inertia(cfrp_properties['E'], given_moment_of_inertia, beam_length, live_load)

# Calculate the temperature-induced deflection
pla_temperature_deflection = pla_properties['alpha'] * temperature_difference * beam_length
cfrp_temperature_deflection = cfrp_properties['alpha'] * temperature_difference * beam_length

# Plot the results
labels = ['PLA', 'CFRP']
deflections = [pla_deflection + pla_temperature_deflection, cfrp_deflection + cfrp_temperature_deflection]

plt.bar(labels, deflections, color=['blue', 'green'])
plt.ylabel('Total Deflection (mm)')
plt.title('Comparison of Deflection for PLA and CFRP Beams')
plt.show()

# Compare Tsai-Hill results
tsai_hill_pla = (
    pla_properties['Tsai_Hill_Xt'],
    pla_properties['Tsai_Hill_Xc'],
    pla_properties['Tsai_Hill_S']
)
tsai_hill_cfrp = (
    cfrp_properties['Tsai_Hill_Xt'],
    cfrp_properties['Tsai_Hill_Xc'],
    cfrp_properties['Tsai_Hill_S']
)

labels_tsai_hill = ['Tsai-Hill Xt', 'Tsai-Hill Xc', 'Tsai-Hill S']
values_pla = [tsai_hill_pla[0], tsai_hill_pla[1], tsai_hill_pla[2]]
values_cfrp = [tsai_hill_cfrp[0], tsai_hill_cfrp[1], tsai_hill_cfrp[2]]

plt.figure(figsize=(10, 6))

plt.bar(labels_tsai_hill, values_pla, width=0.4, label='PLA', color='blue')
plt.bar(labels_tsai_hill, values_cfrp, width=0.4, label='CFRP', color='green', alpha=0.5)

plt.ylabel('Tsai-Hill Values')
plt.title('Comparison of Tsai-Hill Parameters for PLA and CFRP')
plt.legend()
plt.show()

# Given values
sigma_1 = 4.89
tau_12 = -1.03

# Tsai-Hill parameters for PLA
Xt_pla = pla_properties['Tsai_Hill_Xt']
Xc_pla = pla_properties['Tsai_Hill_Xc']
S_pla = pla_properties['Tsai_Hill_S']

# Tsai-Hill parameters for CFRP
Xt_cfrp = cfrp_properties['Tsai_Hill_Xt']
Xc_cfrp = cfrp_properties['Tsai_Hill_Xc']
S_cfrp = cfrp_properties['Tsai_Hill_S']

# Calculate Tsai-Hill for PLA
tsai_hill_pla = (
    (sigma_1 / Xt_pla)*2 + (tau_12 / S_pla)*2
)

# Calculate Tsai-Hill for CFRP
tsai_hill_cfrp = (
    (sigma_1 / Xt_cfrp)*2 + (tau_12 / S_cfrp)*2
)

print("Tsai-Hill for PLA:", tsai_hill_pla)
print("Tsai-Hill for CFRP:", tsai_hill_cfrp)

# Plot the results in a bar chart
labels = ['PLA', 'CFRP']
tsai_hill_values = [tsai_hill_pla, tsai_hill_cfrp]

plt.bar(labels, tsai_hill_values, color=['blue', 'green'])
plt.ylabel('Tsai-Hill Values')
plt.title('Comparison of Tsai-Hill Values for PLA and CFRP')
plt.show()

# Plot the results in a bar chart
labels = ['CFRP', 'PLA']
beam_mass = [beam_mass_CFRP,beam_mass_PLA]

plt.bar(labels, beam_mass, color=['blue', 'green'])
plt.ylabel('Mass')
plt.title('Comparison the mass for PLA and CFRP')
plt.show()