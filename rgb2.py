import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Görüntü boyutu
width, height = 256, 256
x = np.linspace(0, 1, width)
y = np.linspace(0, 1, height)
X, Y = np.meshgrid(x, y)

#R kanalı (8-bit ölçekli)
Z = 128 + 127 * np.sin(2 * np.pi * x) # 0-255 arası değer

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
surf = ax.plot_surface(X * 255, Y * 255, Z, cmap='plasma')

# Eksen ve başlıklar
ax.set_title('R Kanalı: 128 + 127 * sin(2πx)', fontsize=12)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('R Değeri')

plt.tight_layout()
plt.show()