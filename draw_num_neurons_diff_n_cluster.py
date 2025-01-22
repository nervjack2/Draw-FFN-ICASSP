import matplotlib.pyplot as plt

layer = list(range(1, 13))

data = {
    "SSL": {
        "k=3": [464, 599, 885, 1077, 1003, 554, 560, 914, 978, 777, 452, 188],
        "k=39": [192, 185, 193, 159, 183, 301, 334, 224, 247, 290, 420, 330],
        "k=100": [120, 100, 74, 59, 56, 195, 174, 77, 98, 155, 269, 245]
    },
    "ivector": {
        "k=3": [518, 316, 175, 131, 94, 84, 82, 90, 94, 105, 162, 151],
        "k=39": [71, 30, 10, 5, 3, 3, 2, 2, 2, 0, 14, 106],
        "k=100": [28, 15, 2, 3, 2, 1, 2, 0, 1, 0, 4, 76]
    }
}

colors = ['C0', 'C1', 'C2', 'C3']
for k in ["SSL", "ivector"]:
    # Plotting
    plt.figure(figsize=(8, 3))
    d = data[k] 
    for i, (key, values) in enumerate(d.items()):
        plt.plot(layer, values, label=key, marker='o', color=colors[i])
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.xlabel('Layer', fontsize=16)
    plt.ylabel(f'Number of\n{k} cluster neurons', fontsize=16)
    plt.legend(loc='upper center', ncol=4, fontsize=12, bbox_to_anchor=(0.5, 1.33))
    plt.savefig(f'fig/num-{k}-neurons-diff-n-clusters.png', bbox_inches='tight', dpi=500)
    plt.clf()