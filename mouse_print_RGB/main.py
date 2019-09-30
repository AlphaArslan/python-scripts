############################ IMPORT
import cv2

############################ FUNC
def show_rgb(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        b, g, r = img[y, x]
        print(r, g, b)
        
############################ MAIN
# create a window and bind event to it
cv2.namedWindow('image')
cv2.setMouseCallback('image',show_rgb)

# Read the image
# img = cv2.imread("img2.jpg")
img = cv2.imread("rgb.png")

# show image and wait for ESC key
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
