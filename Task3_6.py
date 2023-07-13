import numpy as np
import scipy.stats as stats

print(2 - stats.t.ppf(0.95, 150) * (1.4 / np.sqrt(151)), 2 + stats.t.ppf(0.95, 150) * (1.4 / np.sqrt(151)))
print(2 - stats.t.ppf(0.975, 150) * (1.4 / np.sqrt(151)), 2 + stats.t.ppf(0.975, 150) * (1.4 / np.sqrt(151)))

print(2.3 - stats.t.ppf(0.95, 148) * (1.6 / np.sqrt(149)), 2.3 + stats.t.ppf(0.95, 148) * (1.6 / np.sqrt(149)))
print(2.3 - stats.t.ppf(0.975, 148) * (1.6 / np.sqrt(149)), 2.3 + stats.t.ppf(0.975, 148) * (1.6 / np.sqrt(149)))

print(2.8 - stats.t.ppf(0.95, 156) * (1.2 / np.sqrt(157)), 2.8 + stats.t.ppf(0.95, 156) * (1.2 / np.sqrt(157)))
print(2.8 - stats.t.ppf(0.975, 156) * (1.2 / np.sqrt(157)), 2.8 + stats.t.ppf(0.975, 156) * (1.2 / np.sqrt(157)))

print(4.9 - stats.t.ppf(0.95, 154) * (7.3 / np.sqrt(155)), 4.9 + stats.t.ppf(0.95, 154) * (7.3 / np.sqrt(155)))
print(4.9 - stats.t.ppf(0.975, 154) * (7.3 / np.sqrt(155)), 4.9 + stats.t.ppf(0.975, 154) * (7.3 / np.sqrt(155)))
