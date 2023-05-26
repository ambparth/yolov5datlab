#%% IMPORT THE REQUIRED LIBRARIES HERE. 
import os 
import cv2

#%% PART 1: PARTITION INTO FRAMES
os.mkdir('/SAVED/PATH/') # create the folder 
KPS = 1 # target FPS rate is given here 
VIDEO_PATH = "/VIDEO/PATH/" # path of the video file 
IMAGE_PATH = "/IMAGE/PATH/"  # path where the images are to be saved
EXTENSION = ".jpg" # extension in which the images are to be saved. 
cap = cv2.VideoCapture(VIDEO_PATH)  
fps = round(cap.get(cv2.CAP_PROP_FPS))
print(fps) # print the fps rate. 
# exit()
hop = round(fps / KPS) 
curr_frame = 0 
i = 0; # temporatory variable 
while(True): 
    ret, frame = cap.read() # read the frame. 
    frame = frame[0:1080,0:1920] # crop the region 1080x1920 
    #print(curr_frame)
    if not ret: break # if there is no frame then break the loop
    if curr_frame % hop == 0: # condition
        print([curr_frame,i]); # for verification if the route is correct or not. 
        name = IMAGE_PATH + "/" + str(i) + EXTENSION # note the path 
        cv2.imwrite(name, frame) # write the image and to the directory specified
        i+=1 # increment the count
    curr_frame += 1  #increment the frame
cap.release() # once the reading is done, release or come out of the loop. 

#%% PART2; TRANSFER LEARNING

!python <PATH OF THE detect.py file>  --weights yolov5s.pt --source <PATH/OF/FRAMES/> --conf-thres <THRESH> --save-txt
