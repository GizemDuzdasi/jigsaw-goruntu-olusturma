import numpy as np
import matplotlib.pyplot as plt

#Görüntü boyutu ve grid
size = 500
x = np.linspace(-2 * np.pi, 2 * np.pi, size)
y = np.linspace(-2 * np.pi, 2 * np.pi, size)
X, Y = np.meshgrid(x, y)

#Renk kanallarının tanımlanması (normalize'e gerek yok çünkü zaten 0-1 aralığında)
R = (1 + np.sin(X + Y)) / 2
G = (1 + np.cos(X - Y)) / 2
B = (1 + np.sin(X) * np.cos(Y)) / 2

#RGB görseli oluştur
RGB = np.stack((R, G, B), axis=2)

#Görselleştirme
plt.figure(figsize=(8, 8))
plt.imshow(RGB)
plt.title("Sinüs ve Kosinüs Kombinasyonlu RGB Görsel")
plt.axis('off')
plt.show()