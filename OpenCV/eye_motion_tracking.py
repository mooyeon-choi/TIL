import numpy as np
import cv2

def getLeftmostEye(eyes):
    leftmost = 99999999
    leftmostIndex = -1
    for i in range(len(eyes)):
        if eyes[i][0] < leftmost:
            leftmost = eyes[i][0]
            leftmostIndex = i
    try:
        return eyes[leftmostIndex]
    except:
        return eyes

def getEyeball(eye, circles):
    for y in range(len(eye[0])):
        for x in range(len(eye)):
            for i in range(len(circles)):
                cv2.Pointround(circles[i][0])

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        eyeRect = getLeftmostEye(eyes)
        # for (ex,ey,ew,eh) in eyeRect:
        #     eye = roi_color[ey:ey+eh, ex:ex+ew]
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            eye = roi_gray[ey:ey+eh, ex:ex+ew]
            circles = ()
            cv2.HoughCircles(eye, cv2.HOUGH_GRADIENT, 1, eh // 8, circles, 250, 15, ew // 8, ew // 3)
            eyeball = getEyeball(eye, circles)
            break
    cv2.imshow('img',img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()