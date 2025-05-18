from numpy import pi
from tqdm import tqdm  # added tqdm

def ramanujan_perimeter(a, b):
    return pi * (3 * (a + b) - ((3 * a + b) * (a + 3 * b))**0.5)

def perimeter_fourier(a, b, k_func):
    return [k_func(bi / ai) * pi * (ai + bi) for ai, bi in tqdm(zip(a, b), total=len(a), desc="Fourier perimeter")]

def perimeter_chebyshev(a, b, k_func):
    return [k_func(bi / ai) * pi * (ai + bi) for ai, bi in tqdm(zip(a, b), total=len(a), desc="Chebyshev perimeter")]
