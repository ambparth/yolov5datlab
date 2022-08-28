#%% import all the required python libraries here. 
import os  
import json 
import shutil
from google.colab import files

#%% This is for setting up the environment as the drives portal itself. Run this only once. THIS IS MAINLY DONE IN THE GOOGLE COLAB ENVIRONMENT !! 

from google.colab import drive
drive.mount('/content/drive') 

#%% clone the yolov5 model here. Transfer Learning approach. 
!git clone https://github.com/ultralytics/yolov5

  
#%% install the requirements for the model and also the repo file path is set. Run this only once. 
!pip install -r yolov5/requirements.txt # for running the file once. 
!cd /content/yolov5

#%% this is for running and finding out the list of arguments in the code
!python /content/yolov5/detect.py -h

# single line code for converting the source and the weight and saving the results in the .txt file. 
!python /content/yolov5/detect.py --source /content/drive/MyDrive/test/ --weights yolov5s.pt --conf 0.25  --save-txt --save-conf --save-crop 
# run the above code with the pretrained weights of the same size, and with thresholds. 







#%% Conversion of the text file to the json file is done here. 

file_path = '/content/yolov5/runs/detect/exp2/labels/'

destination_folder = '/content/yolov5/runs/detect/json/'

#os.mkdir(destination_folder);  #uncomment this folder once you run this cell. Even if the output gives an error. 
dict1 = {}
files = os.listdir(file_path) # lists the file in the path. 
for f in files:
  print(file_path+f)
  with open(file_path+f) as fh:
    for line in fh:
      command, description = line.strip().split(None, 1)
      f1 = os.path.splitext(f)[0] # removes the extension of the file
      dict1[command] = description.strip()
  out_file = open(destination_folder+f1+".json", "w")
  json.dump(dict1, out_file, indent = 4, sort_keys = False)
  out_file.close()
  
