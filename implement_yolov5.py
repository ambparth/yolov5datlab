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

  
