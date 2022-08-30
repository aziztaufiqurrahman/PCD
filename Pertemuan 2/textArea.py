from curses import window
import cv2
import PySimpleGUI as sg

img = cv2.imread("redd.png", cv2.IMREAD_COLOR)
scale_percent = 15 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
 
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
for row in resized:
    for pixel in row:
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        
        print = sg.Print
        print(red, green, blue)
        # print(resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
window.close()