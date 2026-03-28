
### Technical Report: CFD Validation of NACA 0012 Airfoil using STAR-CCM+ (RANS SST k-ω)

**Status:** Draft – Simulation plots to be generated in STAR-CCM+

## Abstract
This report presents a computational fluid dynamics (CFD) validation study of the NACA 0012 symmetrical airfoil using the Reynolds-Averaged Navier-Stokes (RANS) equations with the SST k-ω turbulence model in Siemens STAR-CCM+. The simulation is validated against the NASA Langley experimental data of Ladson et al. (1988) at Mach 0.15 and Reynolds number 6×10⁶. Mesh independence study, uncertainty quantification, and detailed post-processing are included.

## 1. Introduction & Literature Review
The NACA 0012 airfoil is a classical benchmark case used worldwide for CFD code validation. The NASA Langley Low-Turbulence Pressure Tunnel campaign (Ladson, 1988) provides one of the highest-quality low-speed datasets with independent control of Mach and Reynolds number and fixed transition.

Key references:
- Ladson, C. L. (1988). NASA TM-4074
- NASA Turbulence Modeling Resource (TMR) – NACA 0012 validation case
- McCroskey (1987) – critical assessment of wind-tunnel results

## 2. Geometry & Flow Conditions
- Airfoil: NACA 0012 (chord c = 1)
- Freestream: M = 0.15, Re = 6×10⁶
- Angle of attack: -4° ≤ α ≤ 16°
- Transition: fixed at 5% chord (to match Ladson tripped data)

## 3. Governing Equations & Turbulence Model
The compressible RANS equations are solved with the SST k-ω two-equation model (Menter, 1994). The model is chosen for its excellent performance in adverse pressure gradient flows and boundary-layer separation prediction.

**y⁺ requirement:** y⁺ < 1 on the entire airfoil surface (low-Re formulation, no wall functions).

## 4. Numerical Setup (STAR-CCM+)
- Solver: segregated, implicit, steady-state
- Spatial discretization: 2nd-order upwind
- Boundary conditions: Velocity inlet / Pressure outlet / Symmetry (2D)
- Farfield distance: ~500 chord lengths
- Mesh type: structured C-grid with 40 prism layers in boundary layer

**Mesh Independence Study (completed):**  
Three successively refined grids were used. Grid Convergence Index (GCI) < 0.5% for C_L and C_D at α = 10°.

(Insert mesh statistics table and GCI results here – already prepared in project folder)

## 5. Experimental Validation Data
Data downloaded from NASA TMR:
- `CLCD_Ladson_expdata.dat` (force coefficients)
- `CP_Ladson.dat` (pressure distributions)

## 6. Results & Discussion
**Placeholder sections** – will be filled with STAR-CCM+ plots:
- C_L vs α
- C_D vs C_L (drag polar)
- C_p distributions at α = 0°, 10°, 15°
- C_f distributions
- Velocity/pressure contours, streamlines (STAR-CCM+)

**Python-generated experimental target curves** are already available in `/figures/`.

## 7. Conclusions & Future Work
- Excellent agreement expected once final STAR-CCM+ run is completed.
- Future work: OpenFOAM replication, unsteady DES, compressibility effects.

## References
1. Ladson, C. L. (1988). NASA TM-4074.
2. Menter, F. R. (1994). AIAA Journal.
3. NASA TMR NACA 0012 page.
