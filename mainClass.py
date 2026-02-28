import cv2
import matplotlib.pyplot as plt
from imgProcessingClass import imgProcessing

class main:
    i = imgProcessing()
    
    # Task 1 - Load image
    bgName = 'savana.jpg'
    bgImg = i.img2Rgb(bgName)
    i.showImg(bgName, bgImg)
    
    # Task 2 - Extract alpha mask
    pName = 'panther.png'
    pImg = i.img2Rgb(pName)
    pMask = i.getAlphaMask(pName)
    plt.show()
    
    # Task 3 - Resize image    
    # image.shape = [height, width, channels]
    bgImg_fitted = i.myResize(bgImg, pImg.shape[1], pImg.shape[0])
    i.showImg(bgName, bgImg_fitted)
    
    # Task 4 - Put panther on background image
    # Logic for adding the values of the mask to the values of the background image and relayering the panther on the foreground
    maskedBg = i.applyMask(pImg, bgImg_fitted, pMask)
    # i.showImg('Panther x Savana', maskedBg)
    

if __name__ == "__main__":
    main()