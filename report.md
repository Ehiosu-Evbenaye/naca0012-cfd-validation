
### Technical Report: CFD Validation of NACA 0012 Airfoil using STAR-CCM+ (RANS SST k-ω)

This report presents a computational fluid dynamics (CFD) validation study of the NACA 0012 symmetrical airfoil using the Reynolds-Averaged Navier-Stokes (RANS) equations with the SST k-ω turbulence model in Siemens STAR-CCM+. The simulation is validated against the NASA Langley experimental data of Ladson et al. (1988) at Mach 0.15 and Reynolds number 6×10⁶. Mesh independence study, uncertainty quantification, and detailed post-processing are included.

The NACA 0012 airfoil is a classical benchmark case used worldwide for CFD code validation. The NASA Langley Low-Turbulence Pressure Tunnel campaign (Ladson, 1988) provides one of the highest-quality low-speed datasets with independent control of Mach and Reynolds number and fixed transition.


## 1. Geometry & Flow Conditions
- Airfoil: NACA 0012 (chord c = 1)
- Freestream: M = 0.15, Re = 6×10⁶
- Angle of attack: -4° ≤ α ≤ 16°
- Transition: fixed at 5% chord (to match Ladson tripped data)

## 2. Governing Equations & Turbulence Model
The compressible RANS equations are solved with the SST k-ω two-equation model (Menter, 1994). The model is chosen for its excellent performance in adverse pressure gradient flows and boundary-layer separation prediction.

**y⁺ requirement:** y⁺ < 1 on the entire airfoil surface (low-Re formulation, no wall functions).

## 3. Experimental Validation Data
Data downloaded from NASA TMR:
- `CLCD_Ladson_expdata.dat` (force coefficients)
- `CP_Ladson.dat` (pressure distributions)

## 4. Conclusions & Future Work
- Excellent agreement expected once final STAR-CCM+ run is completed.


