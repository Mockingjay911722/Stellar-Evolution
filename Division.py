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

def stars_to_remants(s_values_division, current_step = 0, steps, bins,  BH_values = None, NS_values = None, WD_values = None):
    if BH_values is None:
        BH_values = np.zeros((bins, steps))
    if NS_values is None:
        NS_values = np.zeros((bins, steps))
    if WD_values is None:
        WD_values = np.zeros((bins,steps))

    # We do this from each entry to each entry

    for i in range(bins):
        BH_values[j, i] = s_values_division[j, i] * 0.01
        NS_values[j, i] = s_values_division[j, i] * 0.02
        WD_values[j, i] = s_values_division [j, i] * 0.03
    #
    # if current_step == steps - 1:
    #     return BH_values, NS_values, WD_values
    #
    # return stars_to_remants(s_values_division)
    # if current_step == steps - 1 :
    #     return BH_values, NS_values, WD_values
    
    # for j in range(steps):
    #     for i in range(bins):
    #         BH_values[j,i] = s_values_division[j,i] * 0.01
    #         NS_values[j,i] = s_values_division[j,i] * 0.02
    #         WD_values[j,i] = s_values_division [j,i] * 0.03
    # steps         



# Try an example
G_values, S_values, G, S = mass_evolution_gas_stars(100,0,100)

s_values_division = stars_division(S_values, 100, 30)

plots_stars(s_values_division,100,30)

stars_to_remants(s_values_division, 100, 30)