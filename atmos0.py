# atmos0.py, B. Harmon 11/25/2025
# US Std Atmosphere up to 11 km altitude (about 36,000 ft.)
# mks units. Pa is same as N/m^2

import math

def standard_atmosphere(altitude_m):
    """
    Compute temperature (K), pressure (Pa), and density (kg/m^3)
    for a given altitude in meters using the International Standard Atmosphere
    
    Valid up to 11 km (troposphere).
    """
    T0 = 288.15       # Sea level standard temperature (K)
    P0 = 101325       # Sea level standard pressure (Pa)
    rho0 = 1.225      # Sea level standard density (kg/m^3)
    L = -0.0065       # Temperature lapse rate (K/m) up to 11 km
    R = 287.058       # Specific gas constant for dry air (J/kg*K)
    g0 = 9.80665      # Gravity (m/s^2)

    if altitude_m <= 11000:  # Troposphere
        T = T0 + L * altitude_m
        P = P0 * (T / T0) ** (-g0 / (L * R))
    else:
        # For simplicity, only troposphere implemented
        raise ValueError("Model valid only up to 11 km altitude")

    rho = P / (R * T)
    return T, P, rho

alts = [0, 3000, 6000, 9000]
for alt in alts:
    T, P, rho = standard_atmosphere(alt)
    print(f"At {alt} m: T={T:.2f} K, P={P:.2f} Pa, rho={rho:.4f} kg/m^3")
