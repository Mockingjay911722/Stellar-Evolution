import matplotlib.pyplot as plt
import numpy as np


def mass_evolution_of_gas_1(G, S,BH,WD,NS,steps, current_step=0, G_values=None, S_values = None, BH_values = None, WD_values = None, NS_values = None):
    # Initialize the array if it's not provided
    if G_values is None:
        G_values = np.zeros(steps)
    if S_values is None:
        S_values =  np.zeros(steps)
    if BH_values is None:
        BH_values = np.zeros(steps)
    if WD_values is None:
        WD_values = np.zeros(steps)
    if NS_values is None:
        NS_values = np.zeros(steps)

    # Store the current values of G,S,BH,WD and NS in the arrays
    G_values[current_step] = G
    S_values[current_step] = S
    BH_values[current_step] = BH
    WD_values[current_step] = WD
    NS_values[current_step] = NS


    # Base case: if we've reached the desired number of steps, return the array and final G,S,BH,WD and NS.
    if current_step == steps - 1:
        return G_values, S_values, BH_values, WD_values, NS_values,  G, S, BH, WD, NS
    # if current_step == steps - 2:
    #     return BH_values, WD_values, NS_values, BH, WD, NS

    # Update G and S by 1% of the current G
    #Update BH, WD and NS, 1%, 2% and 3%, respectively.
    G_new = G * (1 - 0.01) + S * 0.01
    S_new = S + (G * 0.01) - S * 0.01 - S * 0.01 - S * 0.02 -S * 0.03
    BH_new = BH + (S * 0.01)
    WD_new = WD + (S * 0.02)
    NS_new = NS + (S * 0.03)

    # Recursively call the function for the next step
    return mass_evolution_of_gas_1(G_new, S_new, BH_new, WD_new, NS_new, steps, current_step + 1, G_values, S_values, BH_values, WD_values, NS_values)


# Example usage:
steps = 500
# G_values, S_values, BH_values, WD_values, NS_values, final_G, final_S = mass_evolution_of_gas_1(1, 0, 0, 0, 0, steps)
G_values, S_values, BH_values, WD_values, NS_values, final_G, final_S, final_BH, final_WD, final_NS = mass_evolution_of_gas_1(1, 0, 0, 0, 0, steps)

print(G_values)
print(S_values)
print(BH_values)
print(WD_values)
print(NS_values)
final_sum_check = final_G + final_S + final_BH + final_WD + final_NS
print(final_sum_check)
# PLOT OF G(t), S(t), BH(t), WD(t), NS(t)
t_1d = np.arange(500)
# G(t)
plt.plot(t_1d, G_values, linewidth=4, color='#0077be',label = r'Gas')
plt.title(r'G(t)')
plt.xlabel(r'Evolution Time ')
plt.ylabel(r'Gas')
plt.legend()
plt.show()
# S(t)
plt.plot(t_1d, S_values,linewidth = 4, label = r'S_total')
plt.title(r'S(t)')

plt.xlabel(r'Evolution Time ')
plt.ylabel(r'Total Stars')
plt.legend()
plt.show()
# BH(t)
plt.plot(t_1d, BH_values,linewidth = 4, label = r'BH_total')
plt.title(r'BH(t)')
plt.xlabel(r'Evolution Time ')
plt.ylabel(r'Total Blackhole')
plt.legend()
plt.show()
# WD(t)
plt.plot(t_1d, WD_values,linewidth = 4, label = r'WD_total')
plt.title(r'WD(t)')
plt.xlabel(r'Evolution Time ')
plt.ylabel(r'Total White Dwarfs')
plt.legend()
plt.show()
# NS(t)
plt.plot(t_1d, NS_values,linewidth = 4, label = r'NS_total')
plt.title(r'NS(t)')
plt.xlabel(r'Evolution Time ')
plt.ylabel(r'Total Neutron Stars')
plt.legend()
plt.show()
# Plot overall
plt.plot(t_1d, G_values, linewidth=4, color='#0077be', label = r'Gas')
plt.plot(t_1d, S_values,linewidth = 4, color='#b1a7a6', label = r'S_total')
plt.plot(t_1d, BH_values,linewidth = 4, color='#c1440e', label = r'BH_total')
plt.plot(t_1d, WD_values,linewidth = 4, color = '#32CD32', label = r'WD_total')
plt.plot(t_1d, NS_values,linewidth = 4, color = '#8B008B', label = r'NS_total')
plt.title(r'Stellar Evolution')
plt.xlabel(r'Evolution Time ')
plt.ylabel(r'Mass Evolution')
plt.legend()
plt.show()
#ok~
