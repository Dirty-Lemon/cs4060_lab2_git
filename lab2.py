import cv2
import matplotlib.pyplot as plt

class imgProcessing:
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
    def showImg(self, img, imgName):
        print("Loading", imgName, "...")
        plt.imshow(img)
        plt.show()
    
    # Get image with alpha mask
    def alphaMask(self, fileName):
        print("Applyting alpha mask to", fileName, "...")
        cv2Img = self.readcv(fileName)
        
        print("Image Dimension ={}".format(cv2Img.shape))
        imgBGR = cv2Img[:, :, 0:3]
        imgMask = cv2Img[:, :, 3]
        
        plt.figure(figsize = [15, 15])
        plt.subplot(121); plt.imshow(imgBGR[:, :, ::-1]); plt.title('Colour channels')
        plt.subplot(122); plt.imshow(imgMask, cmap = 'gray'); plt.title('Alpha channel')
        
    # Resize the image if the size is different 
    def imgResize():
        return 0
        
class main:
    i = imgProcessing()
    
    # # Apply alpha mask to panther.png
    # pName = 'panther.png'
    # i.alphaMask(pName)
    # plt.show()
    
    # Test for savana.jpg
    bgName = 'savana.jpg'
    bgImg = i.img2Rgb(bgName)
    # i.showImg(bgImg, bgName)
    
    # Show the height, width, and channels of the background image
    height, width, channels = bgImg.shape
    print(height, width, channels)

if __name__ == "__main__":
    main()