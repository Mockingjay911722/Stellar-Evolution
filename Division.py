import numpy as np
import matplotlib.pyplot as plt
# steps j and bins i are indices also with physical meanings of time and certain collection of masses
def mass_evolution_gas_stars(G, S, steps, current_step = 0, G_values = None, S_values = None):
    # Initialise empty array to store Gas and Stars values
    if G_values is None:
        G_values = np.zeros(steps)
    if S_values is None:
        S_values = np.zeros(steps)

    # store the values in current step
    G_values[current_step] = G
    S_values[current_step] = S


    #Make the recursion
    if current_step == steps-1:
        return G_values, S_values, G, S
    ## evolve according certain percentage
    G_new = G * (1 - 0.01) + S * 0.01
    S_new = S + (G * 0.01) - S * 0.01 - S * 0.01 - S * 0.02 -S * 0.03

    return mass_evolution_gas_stars(G_new, S_new, steps, current_step+1, G_values, S_values)

def stars_division(s_values, steps, bins, s_values_division = None ):
    if s_values_division is None:
        s_values_division = np.zeros((bins,steps))

    # For each s_values_, we divide into 30 equal ones storing in a new (30,) array. In the end, there will be 100 arries
    for j in range(steps):
        for i in range(bins):
            s_values_division[i,j] = s_values[j]/30
    return s_values_division

def plots_stars(s_values_division, steps, bins):
    plt.figure(figsize=(12, 6))
    for i in range(bins):
        plt.plot(range(steps), s_values_division[i], label = f'Curve {i+1}')
    plt.title("Stars Evolution 100 time steps 30 bins", fontsize=14)
    plt.xlabel("Steps", fontsize=12)
    plt.ylabel("Values", fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)  # Place legend outside
    plt.tight_layout()
    plt.grid(True)
    plt.show()
    return

def stars_to_remants(s_values_division, steps, bins, BH_values = None, NS_values = None, WD_values = None):
    if BH_values is None:
        BH_values = np.zeros((bins, steps))
    if NS_values is None:
        NS_values = np.zeros((bins, steps))
    if WD_values is None:
        WD_values = np.zeros((bins,steps))

    for i in range(bins):
        for j in range(steps):
            BH_values[i, j] = s_values_division[i, j] * 0.01
            NS_values[i, j] = s_values_division[i, j] * 0.02
            WD_values[i, j] = s_values_division [i, j] * 0.03
    return BH_values, NS_values, WD_values


def calculate_total_mass(s_values_division, G_values, BH_values, NS_values, WD_values, steps):
    # Total stellar mass across bins for each step
    total_stellar_mass = np.sum(s_values_division, axis=0)  # Sum over bins (rows)

    # Total gas mass (G_values is already a 1D array for each step)
    total_gas_mass = G_values

    # Total mass of remnants across bins for each step
    total_bh_mass = np.sum(BH_values, axis=0)  # Sum over bins (rows)
    total_ns_mass = np.sum(NS_values, axis=0)  # Sum over bins (rows)
    total_wd_mass = np.sum(WD_values, axis=0)  # Sum over bins (rows)

    # Combine all into a dictionary
    total_mass_dict = {
        "step": np.arange(steps),  # Time steps
        "stellar_mass": total_stellar_mass,
        "gas_mass": total_gas_mass,
        "BH_mass": total_bh_mass,
        "NS_mass": total_ns_mass,
        "WD_mass": total_wd_mass,
        "total_mass": total_stellar_mass + total_gas_mass + total_bh_mass + total_ns_mass + total_wd_mass
    }
    return total_mass_dict


# Try an example
G_values, S_values, G, S = mass_evolution_gas_stars(100,0,100)

s_values_division = stars_division(S_values, 100, 30)

plots_stars(s_values_division,100,30)

BH_values, NS_values, WD_values = stars_to_remants(s_values_division, 100, 30)

# Calculate total masses for all time steps
total_mass = calculate_total_mass(s_values_division, G_values, BH_values, NS_values, WD_values, 100)

# Print total mass at each step
for step in range(100):
    print(f"Step {step}: Total Mass = {total_mass['total_mass'][step]:.2f}")
