import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# Same cricket runs data
runs = np.array([100, 120, 110, 150, 110, 140, 130, 170, 120, 220, 140, 110])

plt.figure(figsize=(8, 8))

# Q-Q plot against normal distribution
stats.probplot(runs, dist="norm", plot=plt)

plt.title("Q-Q Plot: Checking Normality of Runs Scored", fontsize=14)
plt.xlabel("Theoretical Quantiles (Standard Normal)", fontsize=12)
plt.ylabel("Sample Quantiles (Runs)", fontsize=12)

# Add a nice reference line (already included by probplot)
# Customize grid
plt.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()
plt.show()