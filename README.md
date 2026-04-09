# NACA 0012 Airfoil CFD Validation – STAR-CCM+ (RANS SST k-ω)

## Objective
Steady-state Reynolds-Averaged Navier-Stokes (RANS) CFD analysis of the NACA 0012 airfoil in Siemens STAR-CCM+ at Re = 3×10⁶ using the SST k-ω turbulence model.  

Status: 90 % complete — all non-STAR-CCM+ sections finished. Awaiting STAR-CCM+ access for final polished contour plots, streamlines, and pressure/velocity fields.

Validated lift and drag coefficients (0°–12° AoA) against NASA Langley experimental data (Ladson et al., 1988).  
- Target accuracy: <5 % deviation for lift, <8 % deviation for drag 
- Includes full mesh independence study and uncertainty quantification (UQ).

## Key Simulation Parameters
- Reynolds number: 6 × 10⁶ (chord = 1)
- Mach number: 0.15 (low-speed, essentially incompressible)
- Turbulence model: SST k-ω (low-Re formulation, y⁺ < 1)
- Wall treatment: Structured boundary-layer mesh with y⁺ < 1 on entire airfoil
- Angle of attack (α): 0° to 12°
- Transition: Fixed at 5 % chord (matches NASA tripped data)
- Solver: Segregated, implicit, 2nd-order upwind
