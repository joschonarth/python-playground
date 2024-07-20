from PIL import Image
import os

image = Image.open("miniatura.jpg")

print(image.getpixel((500,500)))

image.show()

# https://github.com/programacaodinamica/processamento-imagens