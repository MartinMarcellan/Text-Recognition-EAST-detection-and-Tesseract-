import cv2
import pytesseract

img = cv2.imread('real_images/img3.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Recognizing Characters
# hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     b = b.split(' ')
#     x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0,0,255), 3)
#     cv2.putText(img, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

#Recognizing Characters
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img)
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        
        if len(b)==12:
            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0,0,255), 3)
            cv2.putText(img, b[11], (x, y-5), cv2.FONT_HERSHEY_COMPLEX, min(wImg,hImg)/(500), (0, 0, 255), 1)
# img = cv2.resize(img, (640, 320), interpolation = cv2.INTER_AREA)
cv2.imshow('Result', img)
cv2.waitKey(0)