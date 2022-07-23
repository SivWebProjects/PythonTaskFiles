# Import necessary packages
import mediapipe as mp
import cv2
import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
from sklearn.svm import SVC

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

# Import the dataset
csv_file_path = "/home/Documents/CSVFiles/yoga_poses_dataset/yoga_5_poses_data.csv"
data = pd.read_csv(csv_file_path)
x, y = data.iloc[:, :132], data['OUTPUT']

# Training the Support Vector Machine model on the imported dataset
model = SVC(kernel='poly')
model.fit(x, y)


# Prediction on a single image
def detect_pose(image, pose):
    """
     It will perform the pose detection on the person who is
     closely associated with the image and draw all the landmarks
     points in the pose which will be detected in the image.
     Arguments:
        image: The image in which the person is there to be detected.
        pose: The pose function which we created for the image

    Output:
        image(array): input image
        image_copy(array): contains name of the yoga pose detected on the input image
        black_image(array): black image with the landmarks which were
                      detected in the person’s pose and yoga name
        asana(str): name of the yoga pose
    """
    image_copy = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    black_image = np.zeros(image.shape)
    resultant = pose.process(image)
    temp = []
    if resultant.pose_landmarks:
        landmarks = resultant.pose_landmarks.landmark
        # Extract 33 key points of an image
        for j in landmarks:
            temp = temp + [j.x, j.y, j.z, j.visibility]
        y = model.predict([temp])
        if y == 0:
            asan = "downdog"
        elif y == 1:
            asan = "warrior2"
        elif y == 2:
            asan = "plank"
        elif y == 3:
            asan = "goddess"
        else:
            asan = "tree"

        mp_draw.draw_landmarks(image=black_image, landmark_list=resultant.pose_landmarks,
                               connections=mp_pose.POSE_CONNECTIONS,
                               landmark_drawing_spec=mp_draw.DrawingSpec(color=(0, 0, 255),
                                                                         thickness=3, circle_radius=3),
                               connection_drawing_spec=mp_draw.DrawingSpec(color=(0, 255, 0),
                                                                           thickness=2, circle_radius=2))
    return image, image_copy, black_image, asan


# Read the image from the specified path to detect the pose
images_path = ["/home/Documents/CSVFiles/yoga_poses_dataset/test/downdog/00000101.jpg",
               "/home/Documents/CSVFiles/yoga_poses_dataset/test/plank/00000028.jpg",
               "/home/Documents/CSVFiles/yoga_poses_dataset/test/warrior2/00000102.jpg",
               "/home/Documents/CSVFiles/yoga_poses_dataset/test/goddess/00000058.jpg",
               "/home/Documents/CSVFiles/yoga_poses_dataset/test/tree/00000045.jpg"]
# Read image using opencv
results = []
length = len(images_path)
for i in range(length):
    image = cv2.imread(images_path[i])
    result = detect_pose(image, pose)
    results.append(result)


def display_images(result):
    """
    Displaying the input image, the image with the detected
    name, and the landmarks drawn on the image.

    Parameters:
        result (list): It is a list containing the input image,
                       asan detected image, landmarks drawn on
                       the image, and the asan name.
    """
    image, image_copy, black_image, asana = result[0:]
    plt.figure(figsize=[30, 10])
    plt.subplot(131)
    plt.imshow(image)
    plt.rcParams['figure.figsize'] = (10, 10)
    plt.title("Input Image")
    plt.axis('off')
    plt.subplot(132)
    cv2.putText(image_copy, asana, (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (15, 255, 124), 3)
    plt.imshow(image_copy[:, :, ::-1])
    plt.rcParams['figure.figsize'] = (10, 10)
    plt.title("Asana Detected Image")
    plt.axis('off')
    plt.subplot(133)
    cv2.putText(black_image, asana, (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (15, 255, 124), 3)
    plt.imshow(black_image[:, :, ::-1])
    plt.rcParams['figure.figsize'] = (10, 10)
    plt.title("Pose and Asana Detected Image")
    plt.axis('off')


for i in range(length):
    display_images(results[i])
