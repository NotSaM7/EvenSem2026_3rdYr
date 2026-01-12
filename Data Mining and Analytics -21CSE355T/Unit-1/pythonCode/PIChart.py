import matplotlib.pyplot as plt
#Pie Chart - Wickets Distribution by Bowler Type (2024 T20 World Cup - India)
# Data
categories = ['Fast Bowlers', 'Spinners', 'All-rounders']
wickets = [42, 28, 2]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
explode = (0.1, 0, 0)  # slightly separate the largest piece

# Create pie chart
plt.figure(figsize=(9, 9))
plt.pie(wickets,
        labels=categories,
        colors=colors,
        autopct='%1.1f%%',
        explode=explode,
        shadow=True,
        startangle=90,
        textprops={'fontsize': 12})

plt.title("India's Wickets in T20 World Cup 2024\n(by Bowler Type)", 
          fontsize=14, fontweight='bold', pad=20)

plt.axis('equal')  # equal aspect ratio ensures pie is circular
plt.show()