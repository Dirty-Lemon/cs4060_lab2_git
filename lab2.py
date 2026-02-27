import cv2
import matplotlib.pyplot as plt

class imgProcessing:
    
    # read image
    def readcv(self, fileName):
        cv2Img = cv2.imread(fileName, -1)
        return cv2Img
    
    # Convert image to RGB
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
        
        print("Image Dimension ={}".format(cv2Img.shape))
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
    
    # Add image values to create a proper background
    def applyMask(self, fgImg, bgImg, mask):
        
        # # Extract the RGB channels from original image
        # fgRGB = fgImg[:, :, 0]
        # G_orig = origImg[:, :, 1]
        # B_orig = origImg[:, :, 2]
        
        # # Extract the RGB channels from mask image
        # R_mask = maskImg[0]
        # G_mask = maskImg[1]
        # B_mask = maskImg[2]
        
        # # Add alpha mask image channels to the original image channels
        # newImg = (R_orig + alpha) + (G_orig + alpha) + (B_orig + alpha)
        
        # Extract RGB values from images to apply mask
        fgRGB = fgImg[:, :, :]
        bgRGB = bgImg[:, :, :]
        alpha = mask.astype(float)/255
        
        # Apply masking formula to over lay foreground on background
        newImg = alpha * fgRGB + (1 - alpha) * bgRGB
        
        return newImg
        
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
    i.showImg('Panther x Savana', maskedBg)
    

if __name__ == "__main__":
    main()