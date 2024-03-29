# https://processecology.com/articles/the-step-by-step-guide-double-pipe-heat-exchanger-design
# Solving Double Pipe Heat Exchanger problems in python using numerical methods and energy balance equations.

import numpy as np

# Parameters
T_cold_in = float(input("Inlet temperature of cold fluid (in °C) : ")) # Inlet temperature of cold fluid (in °C)
T_hot_in = float(input("Inlet temperature of hot fluid (in °C) : ")) # Inlet temperature of hot fluid (in °C)
m_cold = float(input("Mass flow rate of cold fluid (in kg/s) : ")) # Mass flow rate of cold fluid (in kg/s)
m_hot = float(input("Mass flow rate of hot fluid (in kg/s) : ")) # Mass flow rate of hot fluid (in kg/s)
Cp_cold = float(input("Specific heat capacity of cold fluid (in kJ/kg°C) : ")) # Specific heat capacity of cold fluid (in kJ/kg°C)
Cp_hot = float(input("Specific heat capacity of hot fluid (in kJ/kg°C) : ")) # Specific heat capacity of hot fluid (in kJ/kg°C)

# Calculate the outlet temperatures using energy balance equations
T_cold_out = ((m_cold * Cp_cold * T_cold_in) + (m_hot * Cp_hot * T_hot_in)) / (m_cold * Cp_cold + m_hot * Cp_hot)
T_hot_out = T_cold_out + (T_hot_in - T_cold_in) * (m_cold * Cp_cold) / (m_hot * Cp_hot)

# Calculate heat transfer rate
Q = m_cold * Cp_cold * (T_cold_out - T_cold_in)

# Print the results
print(f"Cold fluid outlet temperature: {T_cold_out:.2f} °C")
print(f"Hot fluid outlet temperature: {T_hot_out:.2f} °C")
print(f"Heat transfer rate: {Q:.2f} kW")