Basic OCR pipeline is created that can read characters from images. In this project, I trained a model using the TensorFlow.

<pip install tensorflow>
make sure that the tensorflow is added in the path

Dataset Preparation:
OCR-Specific dataset: IAM Handwriting Database or Synthetic Word Datasets. Custom Dataset can be built too.

Data Preprocessing:
I resized and normalized the images. Then the lables are converted to a suitable format

Model Selection:
I used Convolutional Neural Network(CNN) for feature extraction. Recurrent Neural Network like LSTM is used for sequence modeling. Connectionsist Temporal Classification (CTC) Loss is used to handle variable-length outputs.

Training the Model:
I compiled the model with an optimizer Adam and the CTC loss. Model.fit() function is used for training the data.

Inference:
Then, these trained model are used to predict text from new images


