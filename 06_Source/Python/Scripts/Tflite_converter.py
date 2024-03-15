import tensorflow as tf

# Load the Keras model
model = tf.keras.models.load_model('C:/Projects/579-Intelligent-Systems-Term-Project/06_Source/Python/Models/modelv12_Angry_Sad_Neutral_pruned.h5')

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TensorFlow Lite model to a file
with open('C:/Projects/579-Intelligent-Systems-Term-Project/06_Source/Python/Models/modelv12_Angry_Sad_Neutral_pruned.tflite', 'wb') as f:
    f.write(tflite_model)
