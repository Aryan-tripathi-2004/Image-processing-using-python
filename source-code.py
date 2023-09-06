import cv2
import numpy as np

image1 = cv2.imread('Images\pika.jpg')
image2 = cv2.imread('Images\dore2.jpg')


def grayimage(image1):
    grayImage = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    return grayImage

def blackandwhite(image1):
    (thresh,blackAndWhiteImage) = cv2.threshold(grayimage(image1), 127, 255,cv2.THRESH_BINARY)
    return blackAndWhiteImage

def whiteandblack(image1):
    wb = 255 - blackandwhite(image1)
    return wb
    

def contrast(image1):
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
    lab = cv2.cvtColor(image1, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l2 = clahe.apply(l)
    lab = cv2.merge((l2,a,b))
    img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    return img2
    

def resize(v):
    down_width = 300
    down_height = 300
    down_points = (down_width, down_height)
    resized1 = cv2.resize(v, down_points, interpolation=cv2.INTER_LINEAR)
    return resized1
    
def hori_concatenatedimage(image1,image2):
    bkg=np.concatenate((resize(image1),resize(image2)), axis=0)
    return bkg
    

def ver_concatenatedimage(image1,image2):
    bkg=np.concatenate((resize(image1),resize(image2)), axis=1)
    return bkg

def invertedimage(image1):
    inverted_image = 255 - grayimage(image1)
    return inverted_image
    

def blurredimage(image1):
    blurred = cv2.GaussianBlur(invertedimage(image1), (21, 21), 0)
    return blurred
    

def invertedblurredimage(image1):
    inverted_blurred = 255 - blurredimage(image1)
    return inverted_blurred
   

def pencilsketch(image1):
    pencil_sketch = cv2.divide(grayimage(image1), invertedblurredimage(image1), scale=256.0)
    return pencil_sketch
    
    
def concat_vh(list_2d):
    return cv2.vconcat([cv2.hconcat(list_h) 
                        for list_h in list_2d])

img1_s = cv2.resize(resize(image1), dsize = (0,0), fx = 0.5, fy = 0.5)
img2_s = cv2.resize(resize(image2),dsize = (0,0),fx = 0.5, fy = 0.5)

img_tile = concat_vh([[img2_s, img1_s, img1_s],
                      [img1_s, img2_s, img1_s],
                      [img1_s, img1_s, img2_s]])

    
def hconcat_resize(img_list, interpolation  = cv2.INTER_CUBIC):
    h_min = min(img.shape[0] for img in img_list)
    im_list_resize = [cv2.resize(img, (int(img.shape[1] * h_min / img.shape[0]),
    h_min), interpolation  = interpolation)
     for img in img_list]
    return cv2.hconcat(im_list_resize)

img_h_resize = hconcat_resize([resize(v=image1), resize(v=image2), resize(v=image1)])



        
print('*******BASIC IMAGE PROCESSING USING PYTHON*******')
print("                                                ")
print("                                               ")
print("press 1 for showing your first input image: ")
print("press 2 for showing your second input image: ")
print("press 3 for change your image to gray image: ")
print("press 4 for change your image to black and white image: ")
print("press 5 for change your image to white and black image: ")
print("press 6 for contrast your image: ")
print("press 7 for resize your image: ")
print("press 8 for concatenate your image horizontally: ")
print("press 9 for concatenate your image vertically: ")
print("press 10 for change your image to inverted image: ")
print("press 11 for change your image to blurr image: ")
print("press 12 for change your image to inverted blurr image: ")
print("press 13 for pencil sketch of your image: ")
print("press 14 for making 1*3 collage of your images: ")
print("press 15 for making 3*3 collage of your images: ")
print("                                                ")
print("press 0 to terminate the program: ")

while True:
   A=int(input("enter value corresponding to your operation: "))

   if(A==0):
       print("Thanks you..!!")
       print("Hope you like my work")
       print("(❁´◡`❁)")
       break;
    
   if(A==1):
        cv2.imshow('Original image',image1)
        cv2.waitKey(0)

   elif(A==2):
        cv2.imshow('image2',image2)
        cv2.waitKey(0)

   elif(A==3):
        x=grayimage(image1)
        cv2.imshow('gray image',x)
        cv2.waitKey(0)

   elif(A==4):
        x= blackandwhite(image1)
        cv2.imshow('blackandwhite',x)
        cv2.waitKey(0)

   elif(A==5):
        x=whiteandblack(image1)
        cv2.imshow('whiteandblack',x)
        cv2.waitKey(0)

   elif(A==6):
        x=contrast(image1)
        cv2.imshow('contrasted image',x)
        cv2.waitKey(0)

   elif(A==7):
        print("press 1 for resize the 1st image: ")
        print("press 2 for resize the 2nd image: ")
     
        w=int(input("enter your value: "))
    
        if(w==1):
            x=resize(image1)
        elif(w==2):
            x=resize(image2)
        else:
          print("invalid value")
       
        cv2.imshow('resized image',x)
        cv2.waitKey(0)

   elif(A==8):
       x=hori_concatenatedimage(image1,image2)
       cv2.imshow('hori_concatenate',x)
       cv2.waitKey(0)

   elif(A==9):
       x=ver_concatenatedimage(image1,image2)
       cv2.imshow('ver_concatenate',x)
       cv2.waitKey(0)
    
   elif(A==10):
       x=invertedimage(image1)
       cv2.imshow('invertedimage',x)
       cv2.waitKey(0)

   elif(A==11):
       x=blurredimage(image1)
       cv2.imshow('blurr_image',x)
       cv2.waitKey(0)

   elif(A==12):
       x=invertedblurredimage(image1)
       cv2.imshow('invertedblurr',x)
       cv2.waitKey(0)

   elif(A==13):
       x=pencilsketch(image1)
       cv2.imshow('pencilsketch',x)
       cv2.waitKey(0)

   elif(A==14):
       x=img_h_resize
       cv2.imshow('1*3 collage',x)
       cv2.waitKey(0)

   elif(A==15):
       x=img_tile
       cv2.imshow('3*3 collage',x)
       cv2.waitKey(0)
    
   else:
        print("please..!! give the right input")

















