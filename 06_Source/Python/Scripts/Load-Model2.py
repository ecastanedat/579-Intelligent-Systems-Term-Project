import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from keras.applications.mobilenet_v2 import preprocess_input

# Load pre-trained Facial Emotion Recognition model
model = load_model('C:/Projects/579-Intelligent-Systems-Term-Project/06_Source/Python/Models/modelv9_Angry_Sad_Neutral.h5')  # Path to your model file

# Define a function to detect faces in the image using Haar Cascade classifier
def detect_faces(image):
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Continuously capture images from the webcam
cap = cv2.VideoCapture(0)  # Use the default webcam

while True:
    ret, frame = cap.read()

    # Detect faces in the captured frame
    faces = detect_faces(frame)

    # Process each detected face
    for (x, y, w, h) in faces:

        # Crop the face region from the frame
        face = frame[y:y+h, x:x+w]

        # Resize the cropped face to 48x48
        face_resized = cv2.resize(face, (48, 48))

        # Convert the cropped face to grayscale
        face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)

        # Normalize pixel values to range between 0 and 1
        normalized = face_gray / 255.0

        # Prepare the image for the model
        normalized = np.expand_dims(normalized, axis=-1)
        normalized = np.expand_dims(normalized, axis=0)

        # Use the model to predict the emotion
        # emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
        emotion_labels = ['Angry', 'Sad', 'Neutral']
        prediction = model.predict(normalized, verbose=0)
        predicted_emotion = emotion_labels[np.argmax(prediction)]

        # Display the captured frame with the detected emotion
        cv2.putText(frame, predicted_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the captured frame
    cv2.imshow('Facial Emotion Recognition', frame)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
