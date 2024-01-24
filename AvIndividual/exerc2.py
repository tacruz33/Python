import numpy as np

def rgb2gray(image, conversion_method='ntsc'):

    if not isinstance(image, np.ndarray) or image.shape[-1] != 3:
        raise ValueError("O argumento de entrada deve ser um ndarray RGB válido.")

 
    conversion_method = conversion_method.lower()
    if conversion_method not in ['ntsc', 'media']:
        raise ValueError("Método de conversão inválido. Escolha entre 'ntsc' ou 'media'.")

    
    ntsc_weights = np.array([0.299, 0.587, 0.114])
    media_weights = np.array([1/3, 1/3, 1/3])

 
    if conversion_method == 'ntsc':
        gray_image = np.sum(image * ntsc_weights, axis=-1)
    elif conversion_method == 'media':
        gray_image = np.mean(image, axis=-1)

    return gray_image.astype(np.uint8)

height, width = 5, 5
random_image = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)
gray_image_ntsc = rgb2gray(random_image, conversion_method='ntsc')
gray_image_media = rgb2gray(random_image, conversion_method='media')

print("Imagem RGB Original:")
print(random_image)

print("\nImagem em Tons de Cinza (Método NTSC):")
print(gray_image_ntsc)

print("\nImagem em Tons de Cinza (Método Média):")
print(gray_image_media)
