import cv2
import numpy as np
import tensorflow as tf
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Load the pre-trained model
model = tf.keras.models.load_model('C:/Projects/579-Intelligent-Systems-Term-Project/07_Sandbox/modelv7.h5')

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TensorFlow Lite model to disk
with open('C:/Projects/579-Intelligent-Systems-Term-Project/07_Sandbox/modelv7.tflite', 'wb') as f:
    f.write(tflite_model)

# Define the emotions
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Define a function to detect emotions from the webcam feed
def detect_emotion():
    interpreter = tf.lite.Interpreter(model_path="C:/Projects/579-Intelligent-Systems-Term-Project/07_Sandbox/modelv7.tflite")
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    cap = cv2.VideoCapture(0)  # Open the webcam (change 0 to another number if you have multiple cameras)

    while True:
        ret, frame = cap.read()  # Read a frame from the webcam

        # Convert the image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Resize the image to match the input size of the model (if necessary)
        # (Replace the width and height with your model's input size)
        resized = cv2.resize(gray, (48, 48))

        # Normalize the image
        normalized = resized / 255.0

        # Reshape the image to match the input shape of the model
        reshaped = np.reshape(normalized, (1, 48, 48, 1))

        # Set the input tensor
        interpreter.set_tensor(input_details[0]['index'], reshaped.astype(np.float32))

        # Run inference
        interpreter.invoke()

        # Get the output tensor
        output_data = interpreter.get_tensor(output_details[0]['index'])

        # Get the predicted emotion label
        emotion_label = emotions[np.argmax(output_data)]

        # Detect faces in the frame
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml').detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw green frame around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the emotion label on the frame
        cv2.putText(frame, emotion_label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Convert the frame to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to PIL Image
        pil_img = Image.fromarray(rgb_frame)

        # Convert the PIL Image to Tkinter PhotoImage
        img = ImageTk.PhotoImage(image=pil_img)

        # Update the label with the new image
        panel.config(image=img)
        panel.image = img

        # Update the GUI
        root.update()

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release the webcam
    cv2.destroyAllWindows()  # Close all OpenCV windows

# Create a tkinter window
root = tk.Tk()
root.geometry('800x500')
root.title("Facial Emotion Recognition")


# Create a button to launch the model
btnframe = tk.Frame(root)
btnframe.columnconfigure(0, weight=1)

btn_launch = tk.Button(btnframe, text="Launch Model", command=detect_emotion)
btn_launch.grid(row=0, column=0, sticky=tk.W+tk.E)

button1 = tk.Button(btnframe, text="Button 1")
button1.grid(row=1, column=0, sticky=tk.W+tk.E)

button2 = tk.Button(btnframe, text="Button 2")
button2.grid(row=2, column=0, sticky=tk.W+tk.E)

button3 = tk.Button(btnframe, text="Button 3")
button3.grid(row=3, column=0, sticky=tk.W+tk.E)

btnframe.pack(fill='x')

# Create a label to display the webcam feed
#panel = tk.Label(root)
#panel.pack()

# Start the tkinter main loop
root.mainloop()
