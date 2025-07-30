import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

# Görsel yolu
IMAGE_PATH = "/content/cat-6706393_1280.jpg"
NUM_SHUFFLED = 3 # Her boyut için 3 karışık puzzle

# Görseli parçalara ayır
def split_image(img, grid_size):
    h, w = img.shape[:2]
    tile_h, tile_w = h // grid_size, w // grid_size
    tiles = []
    for i in range(grid_size):
        for j in range(grid_size):
            tile = img[i * tile_h:(i + 1) * tile_h, j * tile_w:(j + 1) * tile_w, :]
            tiles.append(tile)
    return tiles

# Puzzle parçalarını birleştir
def assemble_jigsaw(tiles_ordered, grid_size):
    rows = []
    for i in range(grid_size):
        row = np.concatenate(tiles_ordered[i * grid_size: (i + 1) * grid_size], axis=1)
        rows.append(row)
    return np.concatenate(rows, axis=0)

# Görseli yükle ve kare boyutlandır
image = Image.open(IMAGE_PATH).convert("RGB")
image = image.resize((256, 256)) # Kare yap

# Her grid boyutu için jigsaw üret
grid_sizes = [3, 4] # 3x3 ve 4x4
fig, axs = plt.subplots(len(grid_sizes), NUM_SHUFFLED + 1, figsize=(15, 6))

for row_idx, grid_size in enumerate(grid_sizes):
    image_np = np.array(image)
    tiles = split_image(image_np, grid_size)

    # 1. Orijinal sırayla
    ordered_puzzle = assemble_jigsaw(tiles, grid_size)
    axs[row_idx, 0].imshow(ordered_puzzle)
    axs[row_idx, 0].axis("off")
    axs[row_idx, 0].set_title(f"{grid_size}x{grid_size} Orijinal")

    # 3 tane karışık
    for i in range(NUM_SHUFFLED):
        shuffled_tiles = tiles.copy()
        random.shuffle(shuffled_tiles)
        puzzle = assemble_jigsaw(shuffled_tiles, grid_size)
        axs[row_idx, i + 1].imshow(puzzle)
        axs[row_idx, i + 1].axis("off")
        axs[row_idx, i + 1].set_title(f"Karışık {i + 1}")

plt.suptitle("3x3 ve 4x4 Puzzle", fontsize=16)
plt.tight_layout()
plt.show()