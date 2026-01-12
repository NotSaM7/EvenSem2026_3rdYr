import matplotlib.pyplot as plt

# Sample data (approximate real stats for Indian bowlers in T20 WC)
bowlers = ['Ashwin', 'Arshdeep', 'Bumrah', 'Chahal', 'Pandya', 'Bhuvneshwar', 'Axar']
matches = [24, 15, 22, 19, 26, 17, 11]
wickets = [32, 27, 30, 26, 22, 19, 15]

plt.figure(figsize=(10, 6))
plt.scatter(matches, wickets, color='blue', s=120, alpha=0.8, edgecolor='black')

# Add labels for each point
for i, bowler in enumerate(bowlers):
    plt.annotate(bowler, (matches[i], wickets[i]), 
                 textcoords="offset points", xytext=(5,5), ha='left', fontsize=10)

# Trend line (optional linear fit)
import numpy as np
z = np.polyfit(matches, wickets, 1)
p = np.poly1d(z)
plt.plot(matches, p(matches), color='red', linestyle='--', linewidth=1.5, 
         label='Trend Line')

plt.title("Indian Bowlers in ICC T20 World Cup: Matches Played vs Wickets Taken", fontsize=14, pad=15)
plt.xlabel("Matches Played", fontsize=12)
plt.ylabel("Wickets Taken", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()