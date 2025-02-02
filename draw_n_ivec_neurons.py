import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# 資料設定
layer = list(range(1, 13))

# 程式碼1的 ivector 資料
data1 = {
    "kₛₛₗ=3": [518, 316, 175, 131, 94, 84, 82, 90, 94, 105, 162, 151],
    "kₛₛₗ=39": [71, 30, 10, 5, 3, 3, 2, 2, 2, 0, 14, 106],
    "kₛₛₗ=100": [28, 15, 2, 3, 2, 1, 2, 0, 1, 0, 4, 76]
}

# 程式碼2的資料
data2 = {
    "proposed": [518, 316, 175, 131, 94, 84, 82, 90, 94, 105, 162, 151],
    "Alternative 1": [763, 685, 508, 410, 257, 144, 176, 285, 340, 435, 395, 173],
    "Alternative 2": [709, 612, 456, 445, 280, 138, 199, 282, 349, 339, 341, 152],
    "Alternative 3": [200, 97, 25, 14, 8, 1, 5, 8, 4, 6, 18, 25]
}

colors = ['C0', 'C1', 'C2', 'C3']

# 建立圖表
fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 1])

# 上半部：程式碼1的 ivector 圖片
ax1 = plt.subplot(gs[0])
for i, (key, values) in enumerate(data1.items()):
    ax1.plot(layer, values, label=key, marker='o', color=colors[i])

ax1.tick_params(axis='both', which='major', labelsize=14)
ax1.set_xlabel('Layer', fontsize=16)
ax1.set_ylabel('Number of\ni=vector cluster neurons', fontsize=20)
ax1.legend(loc='upper right', ncol=2, fontsize=25)

# 下半部：程式碼2的圖片
ax2 = plt.subplot(gs[1])
for i, (key, values) in enumerate(data2.items()):
    ax2.plot(layer, values, label=key, marker='o', color=colors[i])

ax2.tick_params(axis='both', which='major', labelsize=14)
ax2.set_xlabel('Layer', fontsize=16)
ax2.set_ylabel('Number of\ni-vector cluster neurons', fontsize=20)
ax2.legend(loc='upper right', ncol=2, fontsize=20)

plt.tight_layout()
plt.savefig('fig/num-ive-neurons.png', dpi=500, bbox_inches='tight')
