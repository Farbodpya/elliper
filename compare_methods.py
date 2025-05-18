import numpy as np
import matplotlib.pyplot as plt
from exact import true_perimeter, k_true
from fit_fourier import fit_fourier, make_k_fourier
from fit_chebyshev import fit_chebyshev, make_k_chebyshev
from core import perimeter_fourier, perimeter_chebyshev, ramanujan_perimeter

r_vals = np.linspace(0.2, 1.0, 50)
a_vals = np.ones_like(r_vals)
b_vals = r_vals

k_vals = k_true(r_vals)

fourier_params = fit_fourier(r_vals, k_vals, degree=10)
k_f = make_k_fourier(fourier_params)

cheb_model = fit_chebyshev(r_vals, k_vals, degree=30)
k_c = make_k_chebyshev(cheb_model)

P_true = true_perimeter(a_vals, b_vals)
P_fourier = perimeter_fourier(a_vals, b_vals, k_f)
P_chebyshev = perimeter_chebyshev(a_vals, b_vals, k_c)
P_ramanujan = ramanujan_perimeter(a_vals, b_vals)

error_fourier = 100 * np.abs(np.array(P_fourier) - P_true) / P_true
error_chebyshev = 100 * np.abs(np.array(P_chebyshev) - P_true) / P_true
error_ramanujan = 100 * np.abs(np.array(P_ramanujan) - P_true) / P_true

plt.figure(figsize=(10, 6))
plt.plot(r_vals, error_chebyshev, label='Chebyshev', color='red')
plt.plot(r_vals, error_fourier, label='Fourier', color='green')
plt.plot(r_vals, error_ramanujan, label='Ramanujan', color='blue')
plt.xlabel(r'Axis Ratio $r = b/a$')
plt.ylabel('Relative Error (%)')
plt.yscale('log')
plt.title('Relative Error Comparison')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
