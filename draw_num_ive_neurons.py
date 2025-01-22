
import matplotlib.pyplot as plt

layer = list(range(1, 13))
data = {
    "proposed": [518, 316, 175, 131, 94, 84, 82, 90, 94, 105, 162, 151], 
    "Alternative 1": [763, 685, 508, 410, 257, 144, 176, 285, 340, 435, 395, 173], 
    "Alternative 2": [709, 612, 456, 445, 280, 138, 199, 282, 349, 339, 341, 152], 
    "Alternative 3": [200, 97, 25, 14, 8, 1, 5, 8, 4, 6, 18, 25]
}

colors = ['C0', 'C1', 'C2', 'C3']
# Plotting
plt.figure(figsize=(8, 3))
for i, (key, values) in enumerate(data.items()):
    plt.plot(layer, values, label=key, marker='o', color=colors[i])

plt.tick_params(axis='both', which='major', labelsize=14)
plt.xlabel('Layer', fontsize=16)
plt.ylabel('Number of\nivector cluster neurons', fontsize=16)
plt.legend(loc='upper center', ncol=4, fontsize=12, bbox_to_anchor=(0.5, 1.33))
plt.savefig('fig/num-ivector-neurons.png', bbox_inches='tight', dpi=500)
