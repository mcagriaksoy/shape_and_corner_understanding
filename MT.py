# Mehmet Cagri Aksoy - SW Eng.
# All codeblock belongs to my work.
# More Info can be seen on my github page: https://github.com/mcagriaksoy/

#Desired Library Definitions:
import numpy as np
import cv2

# Definitions:
PATH = "/test.jpg"
low_threshold = 20
high_threshold = 130

#Reading the Input Image
img = cv2.imread(PATH,0)
cv2.imshow('image',img)

# Defining the number of rows and columns of the image 
height,width=img.shape 

# Defining Averaging filter(3, 3) mask with Ones (1,1,1:1,1,1:1,1,1)*1/5
mask = np.ones([3, 3], dtype = int) 
mask = mask / 5

cv2.imshow('Original Input Image',img)

#define img filtered array.
img_filtered = np.zeros([height, width]) 
#for 2d matrix, two for loop check whole Image for filtering and multiplying with mask.
for i in range(height-1):
    for j in range(width-1):
        img_filtered[i, j] = (img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*
        mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*
        mask[2, 1]+img[i + 1, j + 1]*mask[2, 2] )
        #I added addiational threshold check for removing some undesired non-black values on the image.
        if img[i,j] > low_threshold:
            img[i,j] = 255

cv2.imshow('Thresholded Image',img_filtered)

edges = cv2.Canny(img,low_threshold,high_threshold,apertureSize = 3)
cv2.imshow('Found canny-edges',edges)

# This part is optional but its quite helpful for show me while investigating
# how to handle corner detection
# It visualizes the corners on image.
CornerDisplayed_img = cv2.cornerHarris(edges, 3, 3, 0.05)
CornerDisplayed_img = cv2.dilate(CornerDisplayed_img,None)
for i in range(height-1):
    for j in range(width-1):
        if CornerDisplayed_img[i,j] > 0.04:
            CornerDisplayed_img[i,j] = 255

cv2.imshow('Found Corners',CornerDisplayed_img)

#To find the length, corners and/or the lines on the shape, we need to 
# contour the image via opencv function of findcontours.
found_contoured_img = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour_loopVar in found_contoured_img[0]:
    #This is using Aspect Ratio Approximation for the detecting the
    #shapes. Each unique solution represents the our image shapes.
    #This function computes a curve length or a closed contour perimeter.
    contour_perimeter = cv2.arcLength(contour_loopVar, True)
    #Moves a curve or polygon closer to another curve
    #polygon with less angles so that the distance between them is less
    #than or equal to the specified precision.
    approx_corner_num = cv2.approxPolyDP(contour_loopVar, 0.04 * contour_perimeter, True)
    # Printing The result:
    if len(approx_corner_num) == 3:
        print("The Shape is: triangle")

    elif len(approx_corner_num) == 4:
        print("The Shape is: rectangle")

    else:
        print("The Shape is: circle")

cv2.waitKey(0)
cv2.destroyAllWindows()