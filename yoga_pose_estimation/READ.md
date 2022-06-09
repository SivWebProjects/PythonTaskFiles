I gathered image dataset for 5 asans (tree, plank, goddess, warrior 2 and downdog). I used the mediapipe library to extract landmarks, 
and each landmark has four values: x, y, and z coordinates, as well as a visibility score. I found landmarks for each image in the dataset 
and saved them in a csv file with 133 columns. Later, that data was divided into train and test sets, and the svm classifier model was trained 
on train data and evaluated on test data, yielding a 95 percent accuracy. I executed a 3D single estimation pose. For prediction, I took a 
single image and first found landmarks, which I then fed into the model, which gives a name performed by a person in the image. The input image, 
asan detected image, landmarks drawn on the image, and the asan name are all drawn in the output.

![Screenshot from 2022-05-27 17-12-07](https://user-images.githubusercontent.com/99475439/172769474-eb7fd263-da45-4133-8637-b8dd135d3d86.png)
![Screenshot from 2022-05-27 17-19-36](https://user-images.githubusercontent.com/99475439/172769481-6a0a54e4-7e1a-4f0a-8058-57fe3c9acd6c.png)
![Screenshot from 2022-05-27 17-20-29](https://user-images.githubusercontent.com/99475439/172769486-4355e12e-2b4b-4ad4-a0ea-2c3cb517073d.png)
