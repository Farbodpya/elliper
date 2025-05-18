import numpy as np
from scipy.optimize import curve_fit
from numpy import pi

def map_r_to_theta(r):
    return pi * (r - 0.2) / 0.8

def fourier_series(theta, *a):
    N = (len(a) - 1) // 2
    result = a[0]
    for n in range(1, N + 1):
        result += a[n] * np.cos(n * theta) + a[n + N] * np.sin(n * theta)
    return result

def fit_fourier(r_vals, k_vals, degree=10):
    theta_vals = map_r_to_theta(r_vals)
    p0 = np.zeros(2 * degree + 1)
    params, _ = curve_fit(fourier_series, theta_vals, k_vals, p0=p0)
    return params

def make_k_fourier(params):
    def k(r):
        theta = map_r_to_theta(r)
        return fourier_series(theta, *params)
    return k
