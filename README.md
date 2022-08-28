# Implementation of YOLOv5 on Custom datasets
This is an implementation of the YOLOv5 model on the custom datasets as implemented by @ultralytics. The results of the model that is the labels and the detected bounding boxes of the particular labels can also be saved in the .txt file. This method is important in the case of data-labelling where custom datasets are acquired and also processed. 

So in most cases in order to reduce the manual work load, one of the relatively easier way is to be implement a pre-trained model and get the results of the detected objects and the corresponding bounding box coordinates. Though there would be some false detections in the process these can be corrected manually, which therefore reduces the load on the manual work. 

Now in the other cases most of the labelling tool such as [mention the lablling tools here] accept .json files as the input. As the model inputs .txt files, therefore the conversion of the txt file to the corresponding .json file is required. 

