import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class imgProcessing():
    
    # Load image in RGB
    def img2Rgb(self, fileName):
        cv2Img = cv2.imread(fileName, -1)
        imgRgb = cv2.cvtColor(cv2Img, cv2.COLOR_BGR2RGB)
        
        return imgRgb
    
    # Display image
    def showImg(self, fileName, img):
        print("Loading", fileName, "...")
        plt.imshow(img); plt.title(fileName)
        plt.show()
    
    # Get image with alpha mask
    def getAlphaMask(self, fileName):
        print("Applying alpha mask to", fileName, "...")
        cv2Img = cv2.imread(fileName, -1)
        
        imgBGR = cv2Img[:, :, 0:3]
        imgMask = cv2Img[:, :, 3:4]
        
        # Show RGB and alpha mask versions of image
        plt.figure(figsize = [10, 5])
        plt.subplot(121); plt.imshow(imgBGR[:, :, ::-1]); plt.title(fileName + ' (Colour Channels)')
        plt.subplot(122); plt.imshow(imgMask, cmap = 'gray'); plt.title(fileName + ' (Alpha Channels)')
        
        return imgMask
        
    # Resize image
    def myResize(self, img, newWidth, newHeight):
        print("Resizing image...")
        newImg = cv2.resize(img, (newWidth, newHeight))
        return newImg
    
    # Properly overlay foreground image on to background using an alpha mask
    def applyMask(self, fgImg, bgImg, mask):
        
        # Convert images to data type usable in an equation
        fgFloat = fgImg.astype(float)
        bgFloat = bgImg.astype(float)
        alpha = mask.astype(float)/255
        
        # Apply masking formula to overlay foreground on to background
        newImg = alpha * fgFloat + (1 - alpha) * bgFloat
        
        return newImg/255