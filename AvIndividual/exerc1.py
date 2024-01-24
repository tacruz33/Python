import numpy as np

def geradorImagens(height=720, width=1280):
    
    random_image = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)
    return random_image