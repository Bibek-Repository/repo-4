# Optical Character Recognition (OCR) using TensorFlow
# use set TF_ENABLE_ONEDNN_OPTS=0 to disable oneDNN Optimizations
# Remember to add path variable to the advance setting and the python interpreter from Command Pallette

import numpy as np
import cv2
import tensorflow as tf
import os
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dense, Dropout, LSTM, Bidirectional, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend as K
from tensorflow.keras.utils import to_categorical

# turning the environmental variable off
os.environ.pop('VARIABLE_NAME', None)  # The 'None' here prevents errors if the variable isn't set

# Set input dimensions
img_width, img_height = 128, 32
max_label_length = 16 # Maximum length of the text output

# Define input layer
inputs = Input(shape=(img_height, img_width,1))

# Define a simple CNN for feature extraction
x= Conv2D(32, (3,3), activation='relu', padding='same')(inputs)
x=MaxPooling2D((2,2))(x)
x=Conv2D((2,2))(x)
x=Conv2D(64, (3,3), activation='relu', padding='same')(x)
x=MaxPooling2D((2,2))(x)
x=Flatten()(x)

# Add RNN (LSTM) layers for sequence modeling
x=Dense(64,activation='relu')(x)
x=tf.expand_dims(x, axis=1) # Adjust dimensions for LSTM input
x=Bidirectional(LSTM(128, return_sequences=True))(x)
x=Bidirectional(LSTM(128, return_sequences=True))(x)
x=Bidirectional(LSTM(128, return_sequences=True))(x)

# Output layer
num_classes=26 # Assuming recognition of A-z oly
outputs= Dense(num_classes + 1, activation='softmax')(x)

#Define and compile the model
model=Model(inputs, outputs)
model.compile(optimizer=Adam(), loss='categorical_crossentropy')

# Summary of the model
model.summary()

# Data Preparation

def preprocess_image(image_path):
    img=cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (img_width, img_height))
    img = img / 255.0 # Normalize pixel values
    img= np.expand_dims(img, axis =-1)  # Add a channel dimension
    return img

def preprocess_label(label, max_length):
    label_encoded = [ord(char) - ord('A') for char in label] # Encode characters as intergers (A-Z)
    label_encoded=label_encoded + [0] * (max_length - len(label_encoded))  # Pad with Zeros
    return to_categorical(label_encoded, num_classes=num_classes + 1)

# Example Usage
image = preprocess_image('path/to/image.png')
label = preprocess_label('HELLO', max_label_length)

# Convert data to numpy arrays for training
images=np.array([image])
labels=np.array([label])

# Training the model using above data and model:
model.fit(
    images,
    labels,
    batch_size=32,
    epochs=10,
    validation_split=0.2
)

# Inference: using the trained model for predicting text from a new image
def predict_text(model, image_path):
    # Predict text from an image using the trained model.
    img=preprocess_image(image_path)
    img=np.expand_dims(img, axis=0)  # Add batch dimension
    prediction = model.predict(img)
    predicted_indices=np.argmax(prediction, axis=2)
    predicted_text=''.join([chr(index + ord('A')) for index in predicted_indices[0] if index > 0])
    return predicted_text

# Example usage
text=predict_text(model, 'path/to/new_image.png')
print("Predicted Text:", text)

# Notes: For better performance, pre-trained model like Tesseract OCR. 
# tf.data API can be used for efficient data loading and augmentation.
# CRNN(Convolutional Recurrent Neural Network) with CTC loss can be used to improve accuracy.


