
import cv2
import pyrealsense2
from realsense_depth import *
import math
import rospy

#ros move robot to correct pos


# Initialize Camera Intel Realsense
dc = DepthCamera()


while True:
    ret, depth_frame, color_frame = dc.get_frame()


    cv2.imshow("Color frame", color_frame)
    cv2.waitKey(1) #press a key to save the image
    cv2.imwrite('./out.png', color_frame)
   
    key = cv2.waitKey(1)
    if key == 27:
        break
  #press esc to set correct picture
  
# Read the original image
img = cv2.imread('out.png')
# Display original image
cv2.imshow('Original', img)

cv2.waitKey(0)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
 #Display Sobel Edge Detection Images
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)

cv2.imwrite('./sobelxy.png', sobelxy)
cv2.imwrite('./gray.png', img_gray)
cv2.imwrite('./imageblur.png', img_blur)
cv2.imwrite('./candy.png', edges)
cv2.waitKey(0)

cv2.destroyAllWindows()

#Ros path creation moveit




#ros path planing



#ros excectuing


  
