#%% importing the modules
import os
import shutil


!cd <DIRECTORY POINTED TO YOLOv5 FOLDER>

#%% detection of the objects in the frame. 
!python <PATH OF THE detect.py file>  --weights yolov5s.pt --source <PATH/OF/FRAMES/> --conf-thres <THRESH> --save-txt 

#%% saving the txt files and copying it into the frames directory. 

txt_files = "/PATH/OF/TXT-FILES/"
frames_files = "/PATH/OF/FRAMES/"

files = os.listdir(txt_files)

# Fetching all the files to directory
for file_name in files:
   shutil.copy(txt_files+file_name, frames_files+file_name)
