# Importing the libraries
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator

# Step 1 - Data Preprocessing
# a) Preprocessing the Training set
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
training_set = train_datagen.flow_from_directory('/home/neosoft/Documents/Github/PythonTaskFiles/cnn_mask_detection/mask_dataset/train',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')
# b) Preprocessing the Test set
test_datagen = ImageDataGenerator(rescale = 1./255)
test_set = test_datagen.flow_from_directory('/home/neosoft/Documents/Github/PythonTaskFiles/cnn_mask_detection/mask_dataset/test',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

# Step 2 - Building the CNN
cnn = tf.keras.models.Sequential()
# a) Convolution
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))
# b) Pooling
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
# Adding a second convolutional layer
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
# c) Flattening
cnn.add(tf.keras.layers.Flatten())
# d) Full Connection
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))
# e) Output Layer
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Step 3 - Training the CNN
# Compiling the CNN
cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# Training the CNN on the Training set and evaluating it on the Test set
cnn.fit(x = training_set, validation_data = test_set, epochs = 25)

# Step 4 - Making a single prediction
import cv2
from matplotlib import pyplot as plt
import numpy as np
from keras.preprocessing import image

# Reading image using opencv imread() 
image_path = "/home/neosoft/Documents/Github/PythonTaskFiles/cnn_mask_detection/mask_dataset/images.jpeg"
predict_image = cv2.imread(image_path)
predict_image = cv2.cvtColor(predict_image, cv2.COLOR_BGR2RGB)
plt.imshow(predict_image)

predict_image = image.load_img(image_path, target_size = (64, 64))
predict_image = image.img_to_array(predict_image)
predict_image = np.expand_dims(predict_image, axis = 0)
result = cnn.predict(predict_image)
# show indices of classes
training_set.class_indices
if result[0][0] == 1:
  prediction_class = 'Properly worn mask'
else:
  prediction_class = 'Improperly worn mask'

print(prediction_class)
