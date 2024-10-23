import sys
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Load the model
model = tf.keras.models.load_model('model/fabric_defect_detection_model.h5')

# Define the class labels based on your training directory structure
#class_labels = list(os.listdir('.\\preprocessed_data'))  # Update this path
class_labels = list(os.listdir("D:\\fbd\\fdd\\brandixdataset\\preprocessed_data"))

def predict_class(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))  # Use the same size as during training
    img_array = image.img_to_array(img)  # Convert to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Rescale to [0, 1]

    # Make prediction
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions, axis=1)[0]  # Get the index of the predicted class
    class_label = class_labels[class_index]  # Map index to class label
    class_index = np.argmax(predictions, axis=1)[0]
    print("confidence: ",predictions[0][class_index])

    return class_label

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    detected_class = predict_class(image_path)
    print(f"The predicted class for the image '{image_path}' is: {detected_class}")
