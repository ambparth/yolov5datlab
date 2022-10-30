#%% importing the modules
import os
import shutil

#%% saving the txt files and copying it into the frames directory. 

txt_files = "/PATH/OF/TXT-FILES/"
frames_files = "/PATH/OF/FRAMES/"

files = os.listdir(txt_files)
files_frame = os.listdir(frames_file)
os.mkdir('</SEPERATE/PATH>')
seprt_file = "/SEPERATE/PATH"
# Fetching all the files to directory
for file_name in files:
   shutil.copy(txt_files+file_name, seprt_file+file_name)
print('Done copying txt files');
for f1 in files_frame:
   shutil.copy(frames_files+f1, seprt_file+f1)
print('Done copying the frames');
