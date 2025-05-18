from mpmath import mp, mpf, sqrt, ellipe, pi
from tqdm import tqdm  # <--- added tqdm

mp.dps = 10000
PI = mp.pi

def true_perimeter(a, b):
    results = []
    for a_, b_ in tqdm(zip(a, b), total=len(a), desc="Calculating true perimeter"):
        a_mp, b_mp = mpf(a_), mpf(b_)
        if b_mp > a_mp:
            a_mp, b_mp = b_mp, a_mp
        e = sqrt(1 - (b_mp / a_mp)**2)
        results.append(float(4 * a_mp * ellipe(e**2)))
    return results

def k_true(r):
    results = []
    for ri in tqdm(r, total=len(r), desc="Calculating k_true"):
        a, b = mpf(1), mpf(ri)
        if b > a:
            a, b = b, a
        e = sqrt(1 - (b / a)**2)
        k = 4 * a * ellipe(e**2) / (PI * (a + b))
        results.append(float(k))
    return results
