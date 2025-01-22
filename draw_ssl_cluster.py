import matplotlib.pyplot as plt
import numpy as np

# Provided data
data = {
    'cluster 0': {
        'vowels': 77.96,
        'semi-vowels': 13.77,
        'voiced-consonants': 3.72,
        'unvoiced-consonants': 4.55,
    },
    'cluster 1': {
        'vowels': 56.56,
        'semi-vowels': 9.53,
        'voiced-consonants': 27.05,
        'unvoiced-consonants': 6.86,
    },
    'cluster 2': {
        'vowels': 11.27,
        'semi-vowels': 9.49,
        'voiced-consonants': 32.86,
        'unvoiced-consonants': 46.22,
    },
}

# Extracting data
categories = ['vowels', 'semi-vowels', 'voiced consonants', 'unvoiced consonants']  # Split longer names
clusters = list(data.keys())
values = [list(cluster.values()) for cluster in data.values()]

# Setting up the plot
fig, axs = plt.subplots(1, 3, figsize=(10, 4), sharey=True)  # Creating subplots for each cluster

# Colors for each category
colors = ['C0', 'C1', 'C2', 'C3']

# Plotting each cluster
for i, ax in enumerate(axs):
    bars = ax.bar(categories, values[i], color=colors)
    ax.set_title(f"SSL Cluster {i+1}", fontsize=16)
    if i == 0:
        ax.set_ylabel('Percentage', fontsize=18)
    ax.set_xticks([])  # Remove x-axis labels
    ax.grid(False)  # Remove grid
    ax.tick_params(axis='y', labelsize=16)  # Increase y-axis tick label size

# Adding a legend at the top
fig.legend(bars, categories, loc='upper center', ncol=2, fontsize=18, bbox_to_anchor=(0.5, 1.13))

# Adjusting layout to accommodate the legend
plt.tight_layout(rect=[0, 0, 1, 0.9])

# Saving the figure
plt.savefig('fig/ssl-cluster.png', bbox_inches='tight', dpi=500)