I gathered image dataset for 5 asans (tree, plank, goddess, warrior 2 and downdog). I used the mediapipe library to extract landmarks, 
and each landmark has four values: x, y, and z coordinates, as well as a visibility score. I found landmarks for each image in the dataset 
and saved them in a csv file with 133 columns. Later, that data was divided into train and test sets, and the svm classifier model was trained 
on train data and evaluated on test data, yielding a 95 percent accuracy. I executed a 3D single estimation pose. For prediction, I took a 
single image and first found landmarks, which I then fed into the model, which gives a name performed by a person in the image. The input image, 
asan detected image, landmarks drawn on the image, and the asan name are all drawn in the output.
