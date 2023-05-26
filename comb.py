#%% importing the modules
import os
import shutil

#%% saving the txt files and copying it into the frames directory. 

txt_files = "/PATH/OF/TXT-FILES/" # the path where the text files (labels) are saved
frames_files = "/PATH/OF/FRAMES/" # the path where the frames extracted from the video are saved. 

files = os.listdir(txt_files) # the directory of the files. (labels)
files_frame = os.listdir(frames_file) # the directory of the frames. 
os.mkdir('</SEPERATE/PATH>') # make use of a separate path. 
seprt_file = "/SEPERATE/PATH" # path as made in above line of code. 
# Fetching all the files to directory
for file_name in files:
   shutil.copy(txt_files+file_name, seprt_file+file_name) # copy the text file (label) to the separate directory. 
print('Done copying txt files');
for f1 in files_frame:
   shutil.copy(frames_files+f1, seprt_file+f1) # copy the frame file to the separate directory. 
print('Done copying the frames');
