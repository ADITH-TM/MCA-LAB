from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from predict import predict_class

# Initialize the Flask application
app = Flask(__name__)

# Configure the upload folder
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the pre-trained model
model = tf.keras.models.load_model('model/fabric_defect_detection_model.h5')

# Define the class labels

@app.route('/')
def home():
    """
    Render the home page with the image upload form.
    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle image upload and prediction.
    """
    # Check if a file was uploaded
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    # Check if the file has a valid filename
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        class_label = predict_class(filepath)

        return render_template('result.html', prediction=class_label, image_path=filepath)


if __name__ == "__main__":
    app.run(debug=True)
