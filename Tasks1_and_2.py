import numpy as np
import scipy.stats as stats

z = stats.norm.ppf(0.975)
n1 = 32
m1 = 17
n2 = 22
m2 = 9
p1 = m1 / n1
p2 = m2 / n2
delta = p1 - p2
P = (m1 + m2) / (n1 + n2)
SE = np.sqrt(P * (1 - P) * (1 / n1 + 1 / n2))
print(delta - z * SE, delta + z * SE)

Z = (abs(p1 - p2) - 1 / 2 * (1 / n1 + 1 / n2)) / SE
print(Z)
print(z)
