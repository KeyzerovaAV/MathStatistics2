import numpy as np
import scipy.stats as stats

X = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
n = len(X)
M = np.mean(X)
S = np.std(X, ddof=1)
t = stats.t.ppf(0.975, n - 1)
print(M - t * (S / np.sqrt(n)), M + t * (S / np.sqrt(n)))
