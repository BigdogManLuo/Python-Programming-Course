import numpy as np
import imageio
import matplotlib.pyplot as plt

def mosaic_effect(image, block_size):
    rows, cols, _ = image.shape
    mosaic_image = np.zeros_like(image)

    for i in range(0, rows, block_size):
        for j in range(0, cols, block_size):
            block = image[i:i+block_size, j:j+block_size]
            avg_color = block.mean(axis=(0, 1))
            mosaic_image[i:i+block_size, j:j+block_size] = avg_color

    return mosaic_image

image = imageio.imread('img/example.jpg')
