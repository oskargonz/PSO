# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 09:04:12 2021

@author: Asus
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#HDR
img1 = np.asarray(Image.open('01 photo 01.jpg'))
img2 = np.asarray(Image.open('01 photo 02.jpg'))
img3 = np.asarray(Image.open('01 photo 03.jpg'))
img4 = np.asarray(Image.open('01 photo 04.jpg'))
imgs=np.array([img1, img2, img3, img4])
imgsOut = np.average(imgs, axis=0)
#Gotowy obraz HDR
outImg = Image.fromarray(np.uint8(imgsOut))
outImg.save("HDR.bmp")

#Wyrównanie histogramu
img5 = np.asarray(outImg)
img5 = img5.transpose(2,0,1)

img5_RED = img5[0]
img5_GREEN = img5[1]
img5_BLUE = img5[2]

img5_RED_1 = Image.fromarray(np.uint8(img5_RED))


#Tworze nowe arrays bo nie mialem mozliwosci zapisu do poprzednich. Flaga WRITEABLE jest ustawiona na False i nie moge jej zmienic, dlatego program dziala bardzo wolno
new_img5_RED = np.zeros((2112,2816))
new_img5_GREEN = np.zeros((2112,2816))
new_img5_BLUE = np.zeros((2112,2816))

#Zakres histogramu
min1 = 7
max1 = 255

#Wyrownanie hostogramu - zmiana arrays
for i in range(2111):
    for j in range (2815):
        new_img5_RED[i][j] = int(255 * (img5_RED[i][j] - min1) / (max1 - min1))
        if new_img5_RED[i][j] > 254:
            new_img5_RED[i][j] = 254
        if new_img5_RED[i][j] < 0:
            new_img5_RED[i][j] = 0
            
        new_img5_GREEN[i][j] = int(255 * (img5_GREEN[i][j] - min1) / (max1 - min1))
        if new_img5_GREEN[i][j] > 254:
            new_img5_GREEN[i][j] = 254
            
        if new_img5_GREEN[i][j] < 0:
            new_img5_GREEN[i][j] = 0
            
        new_img5_BLUE[i][j] = int(255 * (img5_BLUE[i][j] - min1) / (max1 - min1))
        if new_img5_BLUE[i][j] > 254:
            new_img5_BLUE[i][j] = 254
        if new_img5_BLUE[i][j] < 0:
            new_img5_BLUE[i][j] = 0
        
#Tworze array 3D ze wszystkimi kolorami
imgFinalArray = np.array([new_img5_RED, new_img5_GREEN, new_img5_BLUE])
imgFinalArray = imgFinalArray.transpose(1,2,0)

imgFinal = Image.fromarray(np.uint8(imgFinalArray))
imgFinal.save("imgFinal_7_255.bmp")

#Histogram dla ostatecznego obrazu
plt.plot(imgFinal.histogram())
