# OBJECT DETECTION
## ABOUT:
**In this task, I have done object detection in video using opencv and numpy in python language**

### Merging Video 
```py
  cap = cv2.VideoCapture("E:\AUV\6.m4v")
  while True:
    ret, frame = cap.read()
    if ret :
    cv2.imshow("task2",frame)
    key = cv2.waitKey(1)
        if key == 27 & 0xff == ord('q') :
            break
    else :
        break
```

### Object Detection 
```py
  from objectdetection import ObjectDetection
  od = ObjectDetection()
  while True:
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes:
        (x, y, w, h) = box
        cv2.rectangle(frame, (x, y), (x + w, y + h),(0, 225 ,0),2)
```

