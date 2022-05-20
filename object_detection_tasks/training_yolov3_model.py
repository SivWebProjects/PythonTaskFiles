# Connecting to the google drive
from google.colab import drive
drive.mount('/content/drive')

# Unzipping the zip file
# !unzip '/content/drive/MyDrive/yolo_custom_model_training/custom_dataset.zip' 
  -d '/content/drive/MyDrive/yolo_custom_model_training/'

# !git clone 'https://github.com/AlexeyAB/darknet.git' '/content/drive/MyDrive/yolo_custom_model_training/darknet'

# Changing the directory to the darknet
%cd /content/drive/MyDrive/yolo_custom_model_training/darknet

# running make file
# !make
# While running the make file multiple times, a permission denied error will occur. 
# To resolve the above error, the following four lines should be run.
%cd darknet
!sed -i 's/GPU=0/GPU=1/g' Makefile
!sed -i 's/OPENCV=0/OPENCV=1/g' Makefile
!make

# Changing the directory to the root folder
%cd /content/drive/MyDrive/yolo_custom_model_training

# Creating files labelled_data.data and classes.names
# for training in Darknet framework
!python custom_dataset/creating-files-data-and-name.py

# Creating files train.txt and test.txt
# for training in Darknet framework
!python custom_dataset/creating-train-and-test-txt-files.py

# Training the model   
!darknet/darknet detector train custom_dataset/labelled_data.data darknet/cfg/yolov3_custom.cfg 
custom_weight/darknet53.conv.74 -dont_show
