import numpy as np

def geradorImagens(height=720, width=1280):
    
    random_image = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)
    return random_image

print(geradorImagens().shape)       # Deve retornar (720, 1280, 3)
print(geradorImagens(10).shape)     # Deve retornar (10, 1280, 3)
print(geradorImagens(10, 10).shape) # Deve retornar (10, 10, 3)
print(geradorImagens(5, 5))          # Deve retornar uma matriz 5x5x3