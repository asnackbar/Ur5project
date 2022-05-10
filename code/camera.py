
import cv2
import pyrealsense2
from realsense_depth import *
import math
import rospy
from geometry_msgs.msg import Point, Twist
from time import sleep
#ros move robot to correct pos
import rospy


#movement changes to be made
x = 0.0
y = 0.0
theta = 0.0

def newOdom (msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

rospy.init_node("speed_controller")

sub = rospy.Subscriber("/odometry/filtered", odometry, newOdom)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

speed = Twist()

r = rospy.Rate()

goal = Point ()
goal.x = 5
goal.y = 5


while not rospy.is_shutdown():
    inc_x = goal.x - x
    inc_y = goal.y - y
    
    angle_to_goal = atan2 (inc_y, inc_x)

    if abs(angle_to_goal - theta) > 0.1:
      speed.linear.x = 0.0
      speed.angular.z = 0.3
    else:
      speed.linear.x = 0.5
      speed.angular.z = 0.0
    pub.publish(speed)
    r.sleep()



# Initialize Camera Intel Realsense
dc = DepthCamera()


while True:
    ret, depth_frame, color_frame = dc.get_frame()


    cv2.imshow("Color frame", color_frame)
    cv2.waitKey(1) #press a key to save the image
    cv2.imwrite('./image/out.png', color_frame)
   
    key = cv2.waitKey(1)
    if key == 27:
        break
  #press esc to set correct picture
  
# Read the original image
img = cv2.imread('./image/out.png')
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
#cv2.imshow('Sobel X', sobelx)
#cv2.waitKey(0)
#cv2.imshow('Sobel Y', sobely)
#cv2.waitKey(0)
#cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
#cv2.waitKey(0)

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)

cv2.imwrite('./image/sobelxy.png', sobelxy)
cv2.imwrite('./image/gray.png', img_gray)
cv2.imwrite('./image/imageblur.png', img_blur)
cv2.imwrite('./image//candy.png', edges)
cv2.waitKey(0)

cv2.destroyAllWindows()

#Ros path creation moveit




#ros path planing



#ros excectuing


  
