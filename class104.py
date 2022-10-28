import cv2

#reads and stores image
img = cv2.imread("poster.jpg")
#copies the image at the indexs stated of the image above
#           column |   row -
rocket = img[120:360, 400:500]
#paste image at these indexes in the poster image
img[0:240, 500:600] = rocket
#creates a variable for text
text_show = "Hello, I'm an astronaut"
#puts the text in the image
#          image  text  index of pixels to place at  font                     size of text    color of text
cv2.putText(img, text_show, (20,220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,0,0)) 

#renders and displays the image
#        window name   image to show
cv2.imshow("output", img)

#delay for image (makes a timer for the image in milliseconds)
# 0 makes the image stay up forever, until user close out
# 1 second = 1000 milliseconds
cv2.waitKey(0)