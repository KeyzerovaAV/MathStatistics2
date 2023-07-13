import numpy as np
import scipy.stats as stats

print(71.2 - stats.norm.ppf(0.95) * (np.sqrt(3.6) / np.sqrt(100)), 
      71.2 + stats.norm.ppf(0.95) * (np.sqrt(3.6) / np.sqrt(100)))
