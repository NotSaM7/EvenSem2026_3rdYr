import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

runs = np.array([100, 120, 110, 150, 110, 140, 130, 170, 120, 220, 140, 110])

plt.figure(figsize=(15, 5))

# 1. Histogram
plt.subplot(1, 3, 1)
plt.hist(runs, bins=8, edgecolor='black', color='cornflowerblue', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Runs')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)

# 2. Box Plot
plt.subplot(1, 3, 2)
plt.boxplot(runs, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title('Box Plot')
plt.ylabel('Runs')
plt.grid(True, axis='y', alpha=0.3)

# 3. Q-Q Plot
plt.subplot(1, 3, 3)
stats.probplot(runs, dist="norm", plot=plt)
plt.title('Q-Q Plot (vs Normal)')
plt.grid(True, alpha=0.3)

plt.suptitle('Statistical Visualization of Cricket Team Runs', fontsize=16, y=1.05)
plt.tight_layout()
plt.show()