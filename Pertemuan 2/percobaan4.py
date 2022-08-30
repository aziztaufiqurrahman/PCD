import cv2
import numpy as np

path = r'redd.png'

img = cv2.imread(path, cv2.IMREAD_COLOR)

# Displaying the image
# Code ini digunakan untuk menampilkan gambar
# cv2.imshow('image', img) 
# cv2.waitKey(0)
# cv2.destroyAllWindows()

blue=img[:,:,0]
green=img[:,:,1]
red=img[:,:,2]
b=np.average(blue)
g=np.average(green)
r=np.average(red)
print('warna biru : ', b)
print('warna hijau : ', g)
print('warna merah : ', r)

if b>g:
    if b>=r:
        result=print('warna dominan: blue')
        print(b)
else:
    if g>=r:
        result=print('warna dominan: green')
        print(g)
    else:
        result=print('warna dominan: red')
        print(r)