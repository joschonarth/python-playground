import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def getColor(img, x, y):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

def setColor(img, x, y, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)

    return img


def main():
    img = cv2.imread("img/dog.jpg")
    img_pb = cv2.imread("img/dog.jpg", 0)
    altura, largura, canais_de_cor = img.shape
    print(f"Dimensões da Imagem: {largura}X{altura} \nCanais de Cor: {canais_de_cor}")
    
    for y in range(0, altura):
        for x in range(0, largura):
            # azul, verde, vermelho = img[y][x]
            # print("[" + str(x) + "," + str(y) + "] = " + str(img[y][x]))

            # azul = img.item(y, x, 0)
            # verde = img.item(y, x, 1)
            # vermelho = img.item(y, x, 2)

            # img.itemset((y, x, 1), 0)
            # img.itemset((y, x, 2), 0)

            azul, verde, vermelho = getColor(img, x, y)
            # img = setColor(img, x, y, 0, 0, vermelho) 
            img = setColor(img, x, y, azul, verde, vermelho)

    eye = img[180:180+60, 637:637+60]
    showImage(eye)
    img[165:165+eye.shape[0], 915:915+eye.shape[1]] = eye
    showImage(img)



main()




