import matplotlib.pyplot as plt
import numpy as np

# Cricket team runs data
runs = [100, 120, 110, 150, 110, 140, 130, 170, 120, 220, 140, 110]

plt.figure(figsize=(10, 6))
plt.hist(runs, bins=8, edgecolor='black', color='skyblue', alpha=0.7)

plt.title('Distribution of Runs Scored in 12 Matches', fontsize=14, pad=15)
plt.xlabel('Runs Scored', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')

# Optional: add mean and median lines
plt.axvline(np.mean(runs), color='red', linestyle='dashed', linewidth=2, label=f'Mean = {np.mean(runs):.1f}')
plt.axvline(np.median(runs), color='green', linestyle='solid', linewidth=2, label=f'Median = {np.median(runs):.1f}')

plt.legend()
plt.tight_layout()
plt.show()