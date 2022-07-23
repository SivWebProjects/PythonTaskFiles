# Import necessary packages
import mediapipe as mp
import cv2
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

# Initialize the Pose Detection Model
# Initialize the media pipe pose main class.
# Stored the instance of pose detection class in mp_pose variable
mp_pose = mp.solutions.pose
# Set up the Pose function for images independently for the images standalone processing.
# mp_pose will use to call the Pose method.
pose = mp_pose.Pose(static_image_mode=True)
# Initialize mediapipe drawing class to draw the landmarks points.
# It draws key points
mp_draw = mp.solutions.drawing_utils
# Detect 33 Landmarks
points = mp_pose.PoseLandmark

# Print 33 keypoint names
print(len(points))
for i in points:
    print(i)

# Create an empty data frame and enter the names of the columns
data = []
for p in points:
        x = str(p)[13:]  # Takes PoseLandmark object characters from 13 to end
        data.append(x + "_x")
        data.append(x + "_y")
        data.append(x + "_z")
        data.append(x + "_vis")
# Dependent variable
data.append("OUTPUT")
data = pd.DataFrame(columns=data)
print(data.shape)


# Extract key points from each image and store them in respective columns
def extract_keypoints(folder_path, csv_file_path):
    """
    By looping through each image, 33 landmarks are extracted,
    each with four values, and the data is saved in a csv file.

    Parameters:
        folder_path: The path to the folder containing the images.
        csv_file_path: The path to the csv file
    """
    # listdir() method in python is used to get the list of all files and directories in the specified directory.
    # Loop over each image
    for img_path in os.listdir(folder_path):
        temp = []
        img = cv2.imread(path + "/" + img_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(img_rgb)
        print(results.pose_landmarks)
        if results.pose_landmarks:
            # Access data from landmark dictionary
            landmarks = results.pose_landmarks.landmark
            for i, j in zip(points, landmarks):
                temp = temp + [j.x, j.y, j.z, j.visibility]
            data.loc[count] = temp + [4]
    print(img_count)
    # Append data into the csv file
    # data.to_csv(csv_file_path)


# train dataset path
folder_path = "/home/Documents/CSVFiles/yoga_poses_dataset/train/tree"
# csv file path
csv_file_path = "/home/Documents/CSVFiles/yoga_poses_dataset/yoga_data_csv_files/yoga_tree_data.csv"
extract_keypoints(folder_path, csv_file_path)

# Create a CSV File
file_path = "/home/Documents/CSVFiles/yoga_poses_dataset/yoga_5_poses_data.csv"

# Combine the data from five asanas and save it in a csv file
file_path = "/home/Documents/CSVFiles/yoga_poses_dataset/yoga_5_poses_data.csv"
folder_path = "/home/Documents/CSVFiles/yoga_poses_dataset/yoga_data_csv_files"
# chdir() change the current working directory to specified path.
os.chdir(folder_path)
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)
# Combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# Export to csv
combined_csv.to_csv(file_path, index=False)
