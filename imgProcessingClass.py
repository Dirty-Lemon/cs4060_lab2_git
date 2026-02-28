import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class imgProcessing():
    
    # Convert image to a cv2 readable image
    def readcv(self, fileName):
        cv2Img = cv2.imread(fileName, -1)
        return cv2Img
    
    # Load image in RGB
    def img2Rgb(self, fileName):
        cv2Img = self.readcv(fileName)
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
        cv2Img = self.readcv(fileName)
        
        # print("Image Dimension ={}".format(cv2Img.shape))
        imgBGR = cv2Img[:, :, 0:3]
        imgMask = cv2Img[:, :, 3]
        
        plt.figure(figsize = [15, 15])
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
        
        # # Extract the RGB channels from original image
        # fgFloat = fgImg[:, :, 0]
        # G_orig = origImg[:, :, 1]
        # B_orig = origImg[:, :, 2]
        
        # # Extract the RGB channels from mask image
        # R_mask = maskImg[0]
        # G_mask = maskImg[1]
        # B_mask = maskImg[2]
        
        # # Add alpha mask image channels to the original image channels
        # newImg = (R_orig + alpha) + (G_orig + alpha) + (B_orig + alpha)
        
        # Extract RGB values from images to apply mask
        # fgFloat = fgImg[:, :, :]
        # bgFloat = bgImg[:, :, :]
        # alpha = mask[:, :]
        # fgImg = cv2.imread("panther.jpg")
        # bgImg = cv2.imread("savana.jpg")
        
        fgFloat = fgImg.astype(float)
        bgFloat = bgImg.astype(float)
        alpha = mask.astype(float)/255
        
        # Apply masking formula to over lay foreground on background
        # newImg = alpha * fgFloat + (1 - alpha) * bgFloat
        fgVal = cv2.multiply(alpha, fgFloat)
        bgVal = cv2.multiply((1 - alpha), bgFloat)
        newImg = cv2.add(fgVal, bgVal)
        cv2.imshow("outImg", newImg/255)
        
        return newImg