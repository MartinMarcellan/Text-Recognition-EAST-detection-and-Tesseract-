import cv2
import pytesseract
import time

def text_detector(img):
    boxes = pytesseract.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            
            if len(b)==12:
                x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w+x, h+y), (0,0,255), 3)
                cv2.putText(img, b[11], (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
    return img


# img = cv2.imread('images/img5.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

image1 = cv2.imread('real_images/img1.jpg')
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image2 = cv2.imread('real_images/img2.jpg')
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
image3 = cv2.imread('real_images/img3.jpg')
image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)
# image4 = cv2.imread('images2/img5.png')
# image4 = cv2.cvtColor(image4, cv2.COLOR_BGR2RGB)
# image5 = cv2.imread('images2/img6.png')
# image5 = cv2.cvtColor(image5, cv2.COLOR_BGR2RGB)
array = [image1,image2,image3]#,image4,image5]

for i in range(0,2):
	for img in array:
		imageO = img
		# orig = img
		textDetected = text_detector(imageO)
		# cv2.imshow("Orig Image",orig)
		cv2.imshow("Text Detection", textDetected)
		time.sleep(2)
		k = cv2.waitKey(30)
		if k == 27:
			break

cv2.destroyAllWindows()
#Recognizing Words

# cv2.imshow('Result', img)
# cv2.waitKey(0)