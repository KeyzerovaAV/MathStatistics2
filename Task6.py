import numpy as np
import scipy.stats as stats

n1 = 21
n2 = 21
x1 = 1.8
x2 = 2.3
D = (0.4 ** 2 + 0.6 ** 2) / 2
SE = np.sqrt(D / n1 + D / n2)
delta = x1 - x2
t = stats.t.ppf(0.975, n1 + n2 - 2)
print(delta - t * SE, delta + t * SE)
