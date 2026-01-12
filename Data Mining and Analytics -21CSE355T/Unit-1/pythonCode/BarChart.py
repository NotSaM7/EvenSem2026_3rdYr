import matplotlib.pyplot as plt
#Bar Chart - Top 5 Indian Bowlers by T20 World Cup Wickets (Career)
# Data
bowlers = ['R. Ashwin', 'J. Bumrah', 'Arshdeep', 'Y. Chahal', 'H. Pandya']
wickets = [32, 30, 27, 26, 22]

# Colors for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create figure
plt.figure(figsize=(10, 6))

# Vertical bar chart
bars = plt.bar(bowlers, wickets, color=colors, edgecolor='black', linewidth=1.2)

# Add value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, 
             yval + 0.5, 
             str(yval),
             ha='center', 
             va='bottom',
             fontsize=11,
             fontweight='bold')

# Customization
plt.title('Top 5 Indian Bowlers - T20 World Cup Wickets (Career)', 
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Bowler', fontsize=12)
plt.ylabel('Wickets Taken', fontsize=12)
plt.ylim(0, 38)  # some headroom
plt.grid(axis='y', linestyle='--', alpha=0.4)

# Optional: rotate x labels if they are long
plt.xticks(rotation=15)

plt.tight_layout()
plt.show()