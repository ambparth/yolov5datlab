import os 
import cv2

os.mkdir('/SAVED/PATH/')
KPS = 1
VIDEO_PATH = "/VIDEO/PATH/" 
IMAGE_PATH = "/IMAGE/PATH/" 
EXTENSION = ".jpg" 
cap = cv2.VideoCapture(VIDEO_PATH) 
fps = round(cap.get(cv2.CAP_PROP_FPS))
print(fps)
# exit()
hop = round(fps / KPS) 
curr_frame = 0 
i = 0;
while(True): 
    ret, frame = cap.read()
    frame = frame[0:1080,0:1920] 
    #print(curr_frame)
    if not ret: break 
    if curr_frame % hop == 0: 
        print([curr_frame,i]); 
        name = IMAGE_PATH + "" + str(i) + EXTENSION 
        cv2.imwrite(name, frame) 
        i+=1
    curr_frame += 1  
cap.release() 
