############################ IMPORT
import cv2
import numpy as np
import random
import math

############################ GLOBAL
point_list = []

############################ FUNC
# Event calls
def draw_rect(event,x,y,flags,param):
    global point_list
    if event == cv2.EVENT_LBUTTONDBLCLK:
        point_list.append((x,y))
        if len(point_list) is 2:
            cv2.rectangle(img, point_list[0], point_list[1],random_color(),4)
            point_list = []

def draw_tri(event,x,y,flags,param):
    global point_list
    if event == cv2.EVENT_LBUTTONDBLCLK:
        point_list.append((x,y))
        if len(point_list) is 3:
            color = random_color()
            cv2.line(img, point_list[0], point_list[1], color, 4)
            cv2.line(img, point_list[1], point_list[2], color, 4)
            cv2.line(img, point_list[2], point_list[0], color, 4)
            point_list = []

def draw_circle(event,x,y,flags,param):
    global point_list
    if event == cv2.EVENT_LBUTTONDBLCLK:
        point_list.append((x,y))
        if len(point_list) is 2:
            rad = distance(point_list[0], point_list[1])
            cv2.circle(img, point_list[0], rad, random_color(), 4)
            point_list = []

# secondary functions
def random_color():
    r = random.randrange(50, 255, 1)
    g = random.randrange(50, 255, 1)
    b = random.randrange(50, 255, 1)
    return (r, g, b)

def distance(p1, p2):
    return int(math.sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 ))

############################ MAIN
while True:
    # Create a black image
    img = np.zeros((512,512,3), np.uint8)

    # ask the user to choose his shape
    while True:
        print("\n\n")
        print("0: Exit")
        print("1: Rectangle")
        print("2: Triangle")
        print("3: Circle")

        try:
            select = int(input("Please select the shape you want [1~3]: "))
        except:
            print("Wrong selection")
        else:
            break

    if not select:                  # user chose to exit
        exit()

    # create a window and bind event to it
    cv2.namedWindow('image')
    if select is 1:
        cv2.setMouseCallback('image',draw_rect)
    elif select is 2:
        cv2.setMouseCallback('image',draw_tri)
    elif select is 3:
        cv2.setMouseCallback('image',draw_circle)

    # start drawing the selected shape
    # close the window if ESC is clicked
    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
