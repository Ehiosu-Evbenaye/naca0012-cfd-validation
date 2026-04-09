import numpy as np

def naca0012(x_over_c, t=0.12):
    term = (0.2969 * np.sqrt(x_over_c) -
            0.1260 * x_over_c -
            0.3516 * x_over_c**2 +
            0.2843 * x_over_c**3 -
            0.1015 * x_over_c**4)
    return 5 * t * term

# Generate coordinates (cosine spacing for better LE resolution)
n_points = 201
beta = np.linspace(0, np.pi, n_points)
x = 0.5 * (1 - np.cos(beta))          # x/c
y = naca0012(x)

print("NACA 0012 Airfoil Coordinates (chord c = 1 m)")
print("Generated analytically from standard NACA 4-digit series")
print("Formula: y_t = ±5*t*(0.2969√(x/c) - 0.1260(x/c) - ... ) with t=0.12")
print("Columns: x/c    y_upper    y_lower")
print("Note: Leading edge at (0,0), trailing edge forced to (1,0)")

for i in range(len(x)):
    yu = y[i]
    yl = -y[i]
    if i == len(x)-1:          # force sharp TE
        yu = yl = 0.0
    print(f"{x[i]:.6f}    {yu:.6f}    {yl:.6f}")
