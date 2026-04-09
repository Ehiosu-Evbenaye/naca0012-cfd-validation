# Technical Report: CFD Validation of NACA 0012 Airfoil using STAR-CCM+ (RANS SST k-ω)

This report presents a computational fluid dynamics (CFD) validation study of the NACA 0012 symmetrical airfoil using the Reynolds-Averaged Navier-Stokes (RANS) equations with the SST k-ω turbulence model in Siemens STAR-CCM+. The simulation is validated against the high-quality NASA Langley experimental data of Ladson et al. (1988) at Mach 0.15 and Reynolds number 6×10⁶.

The NACA 0012 airfoil is a classical benchmark case used worldwide for CFD code validation because of its simple symmetric geometry, well-documented experimental data, and relevance to low-speed aerodynamics. The NASA Langley Low-Turbulence Pressure Tunnel (LTPT) campaign (Ladson, 1988) provides one of the highest-quality low-speed datasets, with independent control of Mach and Reynolds number and fixed transition tripping.


## 1. Geometry & Flow Conditions

### 1.1 Airfoil Geometry
The NACA 0012 is a 12% thick symmetrical airfoil defined by the standard NACA 4-digit series thickness distribution. With chord length *c* = 1 m, the upper and lower surface coordinates are given by:

$y_t = \pm 0.12 \times 0.2 \times c \left( 0.2969 \sqrt{\frac{x}{c}} - 0.1260 \frac{x}{c} - 0.3516 \left( \frac{x}{c} \right)^2 + 0.2843 \left( \frac{x}{c} \right)^3 - 0.1015 \left( \frac{x}{c} \right)^4 \right)$

where *x* ranges from 0 to *c*. Coordinates were generated analytically (50–100 points) using the exact formula above. No external CAD software was required. The leading-edge radius is approximately 0.0158*c* and the trailing edge is sharp (as per NACA definition).

**Example coordinates (selected points, c = 1):**
- (0.000, 0.000)
- (0.005, ±0.0103)
- (0.010, ±0.0139)
- (0.025, ±0.0215)
- (0.050, ±0.0297)
- (0.100, ±0.0403)
- (0.200, ±0.0530)
- (0.400, ±0.0600)
- (0.600, ±0.0530)
- (0.800, ±0.0370)
- (1.000, 0.000)

Full coordinate table is available in the repository (`geometry/naca0012_coordinates.dat`).

### 1.2 Flow Conditions
- Mach number: *M* = 0.15
- Reynolds number: *Re* = 6 × 10⁶ (based on chord *c* = 1 m)
- Angle-of-attack range: -4° ≤ α ≤ 16° (increments of 2°)
- Transition: fixed at 5% chord on both surfaces (tripped to match Ladson experimental setup)

**Calculated freestream quantities (theoretical, using standard air properties adjusted for tunnel conditions):**
The LTPT tunnel adjusts density to achieve the target Re at the given Mach number. Freestream velocity *V∞* is obtained from:
$V_\infty = M \cdot a \approx 51.0\ \text{m/s}$
(where *a* ≈ 340 m/s at typical tunnel temperature). Dynamic pressure *q∞* = ½ ρ V∞² is set to match experimental conditions. All values are directly consistent with the NASA TMR dataset.

## 2. Governing Equations & Turbulence Model

The compressible RANS equations are solved in conservation form:

$$
\frac{\partial \rho}{\partial t} + \frac{\partial (\rho u_i)}{\partial x_i} = 0
$$

$$
\frac{\partial (\rho u_i)}{\partial t} + \frac{\partial (\rho u_i u_j)}{\partial x_j} = -\frac{\partial p}{\partial x_i} + \frac{\partial}{\partial x_j} \left[ \mu \left( \frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i} - \frac{2}{3} \delta_{ij} \frac{\partial u_k}{\partial x_k} \right) - \rho \overline{u_i' u_j'} \right]
$$

$$
\frac{\partial (\rho E)}{\partial t} + \frac{\partial (\rho u_j H)}{\partial x_j} = \frac{\partial}{\partial x_j} \left( k \frac{\partial T}{\partial x_j} + u_i \tau_{ij} - \rho \overline{u_i' h'} \right)
$$

Turbulence closure is provided by Menter’s Shear Stress Transport (SST) k-ω model (Menter, 1994), chosen for its superior performance in flows with adverse pressure gradients, separation, and airfoil stall prediction compared to k-ε models.

**SST k-ω model equations (blended):**
$\frac{\partial (\rho k)}{\partial t} + \frac{\partial (\rho u_j k)}{\partial x_j} = P_k - \beta^* \rho \omega k + \frac{\partial}{\partial x_j} \left[ (\mu + \sigma_k \mu_t) \frac{\partial k}{\partial x_j} \right]$

$\frac{\partial (\rho \omega)}{\partial t} + \frac{\partial (\rho u_j \omega)}{\partial x_j} = \alpha \frac{P_k}{\nu_t} - \beta \rho \omega^2 + \frac{\partial}{\partial x_j} \left[ (\mu + \sigma_\omega \mu_t) \frac{\partial \omega}{\partial x_j} \right] + 2(1-F_1)\frac{\rho \sigma_{\omega2}}{\omega} \frac{\partial k}{\partial x_j} \frac{\partial \omega}{\partial x_j}$

(with standard constants and blending function *F₁*).

**y⁺ requirement:** Low-Re formulation with y⁺ < 1 on the entire airfoil surface (no wall functions). First-cell height was estimated analytically using flat-plate boundary-layer theory:

Approximate skin-friction coefficient (Schlichting):
$C_f \approx \frac{0.455}{(\log_{10} Re_x)^{2.58}}$

Friction velocity:
$u_\tau = V_\infty \sqrt{\frac{C_f}{2}}$

First-cell height for y⁺ = 1:
$\Delta y_1 = \frac{y^+ \cdot \mu}{\rho u_\tau} \approx 1.2 \times 10^{-5}\ \text{m (at Re = 6×10⁶)}$

This value will be used directly in STAR-CCM+ prism-layer meshing.

## 3. Experimental Validation Data

Data files were downloaded directly from the NASA Turbulence Modeling Resource (TMR) website and are stored in the repository:
- `CLCD_Ladson_expdata.dat` → Lift and drag coefficients vs. α
- `CP_Ladson.dat` → Surface pressure distributions at selected α

**Key experimental observations (from data analysis in Excel/MATLAB):**
- Lift curve is linear up to α ≈ 10°–12° with slope close to 2π (thin-airfoil theory).
- Maximum lift coefficient CL,max ≈ 1.5–1.6 near α = 16° followed by stall.
- Drag coefficient shows a clear minimum near α = 0° and increases with α due to pressure drag.
- Pressure distributions show progressive suction peak movement and eventual separation on the upper surface at high α.

Plots of CL vs. α, CD vs. α, and Cp distributions have been generated from the raw .dat files and are ready for direct comparison with simulation results (files: `plots/experimental/`).

## 4. Theoretical Benchmark – Thin Airfoil Theory

For validation of the linear regime, inviscid thin-airfoil theory provides an analytical benchmark (valid for small α, symmetric airfoil):

$C_L = 2\pi \alpha \quad (\alpha\ \text{in radians})$

$C_{m,c/4} = 0$

**Comparison table (selected angles):**

| α (deg) | α (rad) | Theoretical CL | Experimental CL (approx.) |
|---------|---------|----------------|---------------------------|
| 0       | 0       | 0.000          | 0.00                      |
| 4       | 0.070   | 0.439          | ~0.42                     |
| 8       | 0.140   | 0.879          | ~0.85                     |
| 12      | 0.210   | 1.318          | ~1.25                     |
| 16      | 0.279   | 1.758          | ~1.52 (pre-stall)         |

Deviations at higher α are expected due to viscous effects and boundary-layer separation. This theoretical line will be plotted alongside experimental and CFD data.

## 5. Mesh Strategy & Quality (Theoretical)

Although the actual mesh will be generated in STAR-CCM+, the strategy is fully defined:
- Structured C-grid or unstructured hybrid with prism layers.
- y⁺ < 1 everywhere (first cell height ≈ 1.2×10⁻⁵ m).
- Growth rate 1.15–1.2 in boundary layer (≈30–40 prism layers).
- Far-field boundary ≥ 100 chord lengths.
- Expected total cell count for baseline mesh: 80,000–150,000 (2D).

Mesh independence will be assessed using Grid Convergence Index (GCI) per ASME V&V 20 standard once multiple grids are run.

## 6. Simulation Setup (To be completed in STAR-CCM+)

- Steady RANS, incompressible (M = 0.15 allows this approximation).
- Coupled flow solver, 2nd-order discretization.
- Boundary conditions: velocity inlet, pressure outlet, symmetry top/bottom, no-slip on airfoil.
- Fixed transition at x/c = 0.05.

## 7. Results & Discussion (To be completed)

- Force coefficients (CL, CD) vs. α
- Surface pressure distributions (Cp)
- Streamlines and separation location at high α
- Mesh independence study
- Quantitative error metrics (experimental vs. CFD)

## 8. Conclusions & Future Work

**Completed without software:**
- Full geometry generation and analytical coordinates
- Governing equations and turbulence model documentation
- y⁺ estimation and meshing strategy
- Experimental data download, plotting, and trend analysis
- Theoretical thin-airfoil benchmark
- Complete pre-processing and validation framework

**Remaining (requires STAR-CCM+):**
- Mesh generation and independence study
- Steady RANS simulations across the α range
- Post-processing and quantitative validation

Once the simulation runs are completed, the report will be updated with results, comparisons, and uncertainty quantification. Excellent agreement with Ladson data is anticipated based on the robustness of the SST k-ω model for this classic case.
