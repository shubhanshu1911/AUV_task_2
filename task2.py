import cv2 
import numpy as np
from objectdetection import ObjectDetection

# initilize Object detelction
od = ObjectDetection()

# capturing the video 
cap = cv2.VideoCapture("E:\AUV\AUV_Task _2\6.m4v")

while True:
    ret, frame = cap.read()
    if ret : 
        # detect objects on frames
        (class_ids, scores, boxes) = od.detect(frame)
        for box in boxes:
            (x, y, w, h) = box
            cv2.rectangle(frame, (x, y), (x + w, y + h),(0, 225 ,0),2)
        
        cv2.imshow("task2",frame)

        key = cv2.waitKey(1)
        if key == 27 & 0xff == ord('q') :
            break
    else :
        break 

cap.release()
cv2.destroyAllWindows()

