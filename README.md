# A Semi-Manual Data Labeling Approach

This is an implementation of the YOLOv5 model on the custom datasets as implemented by @ultralytics. The results of the model that is the labels and the detected bounding boxes of the particular labels can also be saved in the .txt file. This method is important in the case of data-labelling where custom datasets are acquired and also processed. 

So in most cases in order to reduce the manual work load, one of the relatively easier way is to be implement a pre-trained model and get the results of the detected objects and the corresponding bounding box coordinates. Though there would be some false detections in the process these can be corrected manually, which therefore reduces the load on the manual work. 

Now in the other cases most of the labelling tool such as the labelImg, LabelBox and even the VGG-Annotator make use of the information of the image along with the corresponding text file, the bounding boxes are drawn automatically by the pre-trained model itself instead of doing it manually. 
 
## Pre-Processing Stages

The first step is the video and partition it into frames/images. Usually for a second, frames as high as 20 to 30 will be acquired. The higher data gives more completeness of the image but on the other it consumes more computational memory and further in the case of autonomous vehicular data, all these data aren't required. The data that is to be selected depends on the speed of the vehicle, wherein frame rate selection should be low in the case of lower speeds and higher when the speed is increased. But in this analysis, the 1 frame per second is usually effective when the speed of the vehicle is less. The code of converting the video frames to the desired 1 frame a second can be achieved with 'fps_1.py' file.
