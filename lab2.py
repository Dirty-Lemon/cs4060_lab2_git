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
    def showImg(self, img):
        print("Loading image...")
        plt.imshow(img)
        plt.show()
    
    # Get image with alpha mask
    def alphaMask(self, fileName):
        print("Applyting alpha mask to ", fileName, "...")
        cv2Img = self.readcv(fileName)
        
        print("Image Dimension ={}".format(cv2Img.shape))
        imgBGR = cv2Img[:, :, 0:3]
        imgMask = cv2Img[:, :, 3]
        
        plt.figure(figsize = [15, 15])
        plt.subplot(121); plt.imshow(imgBGR[:, :, ::-1]); plt.title('Colour channels');
        plt.subplot(122); plt.imshow(imgMask, cmap = 'gray'); plt.title('Alpha channel');
        
class main:
    i = imgProcessing()
    
    pName = 'panther.png'
    i.alphaMask(pName)
    plt.show()
    
    bgName = 'savana.jpg'
    bgImg = i.img2Rgb(bgName)
    i.showImg(bgImg)

if __name__ == "__main__":
    main()