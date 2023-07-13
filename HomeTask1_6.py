import numpy as np
import scipy.stats as stats

S = 16
M = 80
n = 256
Z = stats.norm.ppf(0.975)
print(M - Z * (S / np.sqrt(n)), M + Z * (S / np.sqrt(n)))
