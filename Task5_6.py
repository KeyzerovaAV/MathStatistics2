import numpy as np
import scipy.stats as stats

z = stats.norm.ppf(0.975)
SE1 = np.sqrt((24 / 30 * (1 - 24 / 30)) / 30)
print(24 / 30 - z * SE1, 24 / 30 + z * SE1)
