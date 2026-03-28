import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set plot style
sns.set_style("whitegrid")

# Load NASA Langley experimental data (Ladson et al. 1988)
# Data file: CLCD_Ladson_expdata.dat from NASA TMR
ladson = pd.read_csv('../data/experimental/CLCD_Ladson_expdata.dat', 
                     delim_whitespace=True, 
                     comment='#', 
                     names=['alpha', 'CL', 'CD'])

# TODO: When STAR-CCM+ results are ready, load them here
# sim = pd.read_csv('../data/simulation/starccm_clcd.csv')

# Create figure with two subplots
plt.figure(figsize=(10, 4))

# Lift curve (Cl vs alpha)
plt.subplot(1, 2, 1)
plt.plot(ladson['alpha'], ladson['CL'], 'o-', 
         label='NASA Langley (Ladson 1988)', markersize=4)
# plt.plot(sim['alpha'], sim['CL'], 's--', label='STAR-CCM+ SST k-ω')
plt.xlabel('Angle of Attack α [°]')
plt.ylabel('Lift Coefficient C_L')
plt.legend()
plt.grid(True)

# Drag polar (Cl vs Cd)
plt.subplot(1, 2, 2)
plt.plot(ladson['CD'], ladson['CL'], 'o-', 
         label='NASA Langley (Ladson 1988)')
# plt.plot(sim['CD'], sim['CL'], 's--', label='STAR-CCM+')
plt.xlabel('Drag Coefficient C_D')
plt.ylabel('Lift Coefficient C_L')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('../figures/exp_vs_sim_Cl_Cd.png', dpi=300)
plt.show()

print("Plots saved to figures/ folder")
