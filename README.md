# A Semi-Manual Data Labeling Approach

This is an implementation of the YOLOv5 model on the custom datasets as implemented by @ultralytics. The results of the model that is the labels and the detected bounding boxes of the particular labels can also be saved in the .txt file. This method is important in the case of data-labelling where custom datasets are acquired and also processed. 

So in most cases in order to reduce the manual work load, one of the relatively easier way is to be implement a pre-trained model and get the results of the detected objects and the corresponding bounding box coordinates. Though there would be some false detections in the process these can be corrected manually, which therefore reduces the load on the manual work. 

Now in the other cases most of the labelling tool such as the labelImg, LabelBox and even the VGG-Annotator make use of the information of the image along with the corresponding text file, the bounding boxes are drawn automatically by the pre-trained model itself instead of doing it manually. 
 
## Pre-Processing Stages
### Re-formatted Frames
The first step is the video and partition it into frames/images. Usually for a second, frames as high as 20 to 30 will be acquired. The higher data gives more completeness of the image but on the other it consumes more computational memory and further in the case of autonomous vehicular data, all these data aren't required. The data that is to be selected depends on the speed of the vehicle, wherein frame rate selection should be low in the case of lower speeds and higher when the speed is increased. But in this analysis, the 1 frame per second is usually effective when the speed of the vehicle is less. The code of converting the video frames to the desired 1 frame a second can be achieved with 'fps_1.py' file.

### Re-Sized Frames
This step would be required to make the image size compactible to that of the model that is used. Each of the Deep Learning Model have their own obligatory size of input images. It is to be noted that the model that is used here is the You-Only-Learn-Once (YOLO) version '5'. Though there are retrofitted models of YOLOv5 which can be used, but this analysis is restricted only the fifth version. Also for the fact the resizing is also required to remove some of the artifacts in the frames or the images, for instance in the autonomous vehicle data, if the data is collected with the image of the car parts such as the bonnet etc, this should be required, as it would increase the percentage of false detections. 
 
### Transfer Learning
Once the frames are resized, the other processing stage is using the transfer learning approach to detect the different objects in the frame. This is the point where the bounding box are drawn by the model and not down manually. The result of the bounding boxes especially the coordinates and also the labels are saved in the relavant text file. The model is trained on a COCO datasets that contains upto 80 classes, further the resized frames can be concatenated with the text files together in a separate file whose analysis can be done using the Data-Labeling toolkit. 

The YOLOv5 model can be clone from the following link. https://github.com/ultralytics/yolov5.git 

Similarly the LabelImg data labeling toolkit can be cloned from the following link. https://github.com/heartexlabs/labelImg.git

