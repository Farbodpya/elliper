from numpy.polynomial.chebyshev import Chebyshev

def normalize_r(r):
    return 2 * (r - 0.2) / 0.8 - 1

def fit_chebyshev(r_vals, k_vals, degree=30):
    return Chebyshev.fit(normalize_r(r_vals), k_vals, deg=degree)

def make_k_chebyshev(cheb_fit):
    def k(r):
        return cheb_fit(normalize_r(r))
    return k
