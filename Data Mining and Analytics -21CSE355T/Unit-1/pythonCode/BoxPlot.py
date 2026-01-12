import matplotlib.pyplot as plt

# Same cricket runs data
runs = [100, 120, 110, 150, 110, 140, 130, 170, 120, 220, 140, 110]

plt.figure(figsize=(8, 6))
plt.boxplot(runs, vert=True, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='blue'),
            capprops=dict(color='blue'),
            flierprops=dict(marker='o', markerfacecolor='red', markersize=8))

plt.title('Box Plot of Runs Scored by the Team', fontsize=14)
plt.ylabel('Runs', fontsize=12)
plt.grid(True, axis='y', alpha=0.3, linestyle='--')

# Add some annotation
plt.text(1.1, 220, 'Outlier: 220', fontsize=10, color='red')

plt.tight_layout()
plt.show()