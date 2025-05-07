import matplotlib.pyplot as plt
import numpy as np

regions = [
    'NCR', 'Cordillera', 'Region 1', 'Region 2', 'Region 3', 'Region 4A', 'MIMAROPA',
    'Region 5', 'Region 6', 'Region 7', 'Region 8', 'Region 9', 'Region 10',
    'Region 11', 'Region 12', 'Caraga', 'ARMM'
]

of = [9.2, 11.0, 11.8, 16.1, 8.8, 7.6, 5.9, 4.6, 13.2, 6.0, 6.3, 7.1, 6.5, 7.3, 12.4, 5.9, 6.9]
ofw = [17.3, 16.0, 18.0, 21.9, 7.2, 13.3, 6.6, 8.5, 14.2, 10.2, 8.3, 9.9, 10.5, 11.0, 9.4, 5.4, 23.8]
emigrants = [1.2, 2.9, 2.4, 1.5, 0.8, 3.5, 0.9, 0.3, 0.9, 1.0, 0.3, 0.3, 0.4, 0.3, 2.2, 2.0, 1.6]

x = np.arange(len(regions))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 8))
bars1 = ax.barh(x - width, of, height=width, label='With OF', color='skyblue')
bars2 = ax.barh(x, ofw, height=width, label='With OFW', color='orange')
bars3 = ax.barh(x + width, emigrants, height=width, label='With Emigrants', color='green')

def add_labels(bars):
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.3, bar.get_y() + bar.get_height()/2,
                f'{width:.1f}%', va='center', fontsize=8)

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

ax.set_yticks(x)
ax.set_yticklabels(regions)
ax.set_xlabel('Percentage')
ax.set_title('2018 National Migration Survey by Region')
ax.legend()
ax.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()