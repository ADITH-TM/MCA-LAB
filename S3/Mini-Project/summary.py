import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('fabric_defect_detection_model.h5')

# Print the model summary
model.summary()
