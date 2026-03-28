import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

sns.set_style("whitegrid")

# === DOWNLOAD THESE FILES FROM TMR (links in README) ===
# Place them in data/experimental/
ladson = pd.read_csv('../data/experimental/CLCD_Ladson_expdata.dat', delim_whitespace=True, comment='#', names=['alpha', 'CL', 'CD'])

# Example simulation data placeholder (replace with your STAR-CCM+ CSV)
# sim = pd.read_csv('../data/simulation/starccm_clcd.csv')

plt.figure(figsize=(10, 4))

# Lift curve
plt.subplot(1, 2, 1)
plt.plot(ladson['alpha'], ladson['CL'], 'o-', label='Ladson (exp, tripped)', markersize=4)
# plt.plot(sim['alpha'], sim['CL'], 's--', label='STAR-CCM+ SST k-ω')
plt.xlabel('Angle of Attack α [°]')
plt.ylabel('Lift Coefficient C_L')
plt.legend()
plt.grid(True)

# Drag polar
plt.subplot(1, 2, 2)
plt.plot(ladson['CD'], ladson['CL'], 'o-', label='Ladson (exp)')
# plt.plot(sim['CD'], sim['CL'], 's--', label='STAR-CCM+')
plt.xlabel('Drag Coefficient C_D')
plt.ylabel('Lift Coefficient C_L')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('../figures/exp_vs_sim_Cl_Cd.png', dpi=300)
plt.show()

print("✅ Plots saved to figures/ folder – ready for GitHub!")
