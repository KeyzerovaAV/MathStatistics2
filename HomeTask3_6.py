import numpy as np
import scipy.stats as stats

mothers_height = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
daughters_height = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
n1 = len(mothers_height)
n2 = len(daughters_height)
D = (np.var(mothers_height) + np.var(daughters_height)) / 2
SE = np.sqrt(D / n1 + D / n2)
delta = np.mean(mothers_height) - np.mean(daughters_height)
t = stats.t.ppf(0.975, n1 + n2 - 2)
print(delta - t * SE, delta + t * SE)
