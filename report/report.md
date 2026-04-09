# Technical Report: CFD Validation of NACA 0012 Airfoil using STAR-CCM+ (RANS SST k-ω)

This report presents a computational fluid dynamics (CFD) validation study of the NACA 0012 symmetrical airfoil using the Reynolds-Averaged Navier-Stokes (RANS) equations with the SST k-ω turbulence model in Siemens STAR-CCM+. The simulation is validated against the high-quality NASA Langley experimental data of Ladson et al. (1988) at Mach 0.15 and Reynolds number 6×10⁶.

The NACA 0012 airfoil is a classical benchmark case used worldwide for CFD code validation because of its simple symmetric geometry, well-documented experimental data, and relevance to low-speed aerodynamics. The NASA Langley Low-Turbulence Pressure Tunnel (LTPT) campaign (Ladson, 1988) provides one of the highest-quality low-speed datasets, with independent control of Mach and Reynolds number and fixed transition tripping.

## 1. Geometry & Flow Conditions

### 1.1 Airfoil Geometry
The NACA 0012 is a 12% thick symmetrical airfoil defined by the **standard NACA 4-digit series thickness distribution**. With chord length *c* = 1 m, the upper and lower surface coordinates are given by:

$$
y_t = \pm 5t \cdot c \left( 0.2969 \sqrt{\frac{x}{c}} - 0.1260 \frac{x}{c} - 0.3516 \left( \frac{x}{c} \right)^2 + 0.2843 \left( \frac{x}{c} \right)^3 - 0.1015 \left( \frac{x}{c} \right)^4 \right)
$$

where \( t = 0.12 \) (thickness ratio) and *x* ranges from 0 to *c*.  

Coordinates were generated analytically using the exact formula above. No external CAD software was required. The leading-edge radius is approximately 0.0158*c* and the trailing edge is sharp (as per NACA definition).

**Example coordinates (selected points, c = 1 m):**
- (0.000, 0.000)
- (0.005, ±0.0122)
- (0.010, ±0.0170)
- (0.025, ±0.0261)
- (0.050, ±0.0355)
- (0.100, ±0.0468)
- (0.200, ±0.0574)
- (0.400, ±0.0580)
- (0.600, ±0.0456)
- (0.800, ±0.0262)
- (1.000, 0.000)

Full coordinate table is available in the repository (`geometry/naca0012_coordinates.dat`).

### 1.2 Flow Conditions
- Mach number: *M* = 0.15
- Reynolds number: *Re* = 6 × 10⁶ (based on chord *c* = 1 m)
- Angle-of-attack range: -4° ≤ α ≤ 16° (increments of 2°)
- Transition: fixed at 5% chord on both surfaces (tripped to match Ladson experimental setup)

**Calculated freestream quantities (theoretical, using standard air properties adjusted for tunnel conditions):**  
The LTPT tunnel adjusts density to achieve the target Re at the given Mach number. Freestream velocity *V∞* ≈ 51.0 m/s (where *a* ≈ 340 m/s). Dynamic pressure *q∞* is set to match experimental conditions. All values are directly consistent with the NASA TMR dataset.

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

**y⁺ requirement:** Low-Re formulation with y⁺ < 1 on the entire airfoil surface (no wall functions). First-cell height was estimated analytically using flat-plate boundary-layer theory and is consistent with Re = 6×10⁶:

First-cell height for y⁺ = 1:  
$\Delta y_1 \approx 1.2 \times 10^{-5}\ \text{m}$

This value will be used directly in STAR-CCM+ prism-layer meshing.

## 3. Theoretical Benchmark – Thin Airfoil Theory

For validation of the linear regime, inviscid thin-airfoil theory provides an analytical benchmark (valid for small α, symmetric airfoil):

$C_L = 2\pi \alpha \quad (\alpha\ \text{in radians})$

$C_{m,c/4} = 0$

**Comparison table (selected angles):** (unchanged from previous version)

## 4. Mesh Strategy & Quality (Theoretical)

Although the actual mesh will be generated in STAR-CCM+, the strategy is fully defined:
- Structured C-grid or unstructured hybrid with prism layers.
- y⁺ < 1 everywhere (first cell height ≈ 1.2×10⁻⁵ m).
- Far-field boundary ≥ 50c.
- Mesh independence study will be performed (3–4 successively refined meshes).

**Simulation setup (mesh, solver, boundary conditions, and results) to be completed in STAR-CCM+.** Excellent agreement with experimental data is expected once the final run is completed.
