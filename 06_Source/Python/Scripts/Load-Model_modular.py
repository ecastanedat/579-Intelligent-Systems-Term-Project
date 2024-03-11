'''
/*============================================================================*/
/*                        BA AN SOFTWARE GROUP                                */
/*============================================================================*/
/*                        OBJECT SPECIFICATION                                */
/*============================================================================*/
/*
 * $Source: Load-Model_modular.py $
 * $Revision: 0.1$
 * $Author: Castaneda, Luis $
 * $Date: Mar 3, 2024 8:37:38 PM $
 */
/*============================================================================*/
/*                                                                            */
/* The reproduction, transmission, or use of this document or its content is  */
/* not permitted without express written authority. Offenders will be liable  */
/* for damages.                                                               */
/* All rights, including rights created by patent grant or registration of a  */
/* utility model or design, are reserved.                                     */
/*                                                                            */
/*============================================================================*/
/* Reference documents:                                                       */
/*                                                                            */
/*============================================================================*/
/* OBJECT HISTORY                                                             */
/*============================================================================
* $Log: Load-Model_modular.py $
* Revision 0.1 2024/02/27 10:57 EST Castaneda, Luis
* Initial revision
'''

import os
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from keras.applications.mobilenet_v2 import preprocess_input


# **************************************************************
# *  Name                 :  save_image
# *  Description          :  Function to save an image.
# *  Parameters           :  frame, file_path
# *  Return               :  int
# *  Critical/explanation :  No
# **************************************************************
def save_image(frame, file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    
    cv2.imwrite(file_path, frame)
    print("Image saved as:", file_path)


# **************************************************************
# *  Name                 :  save_image
# *  Description          :  Define a function to detect faces in 
#                            the image using Haar Cascade classifierFunction 
#                            to save an image.
# *  Parameters           :  image
# *  Return               :  faces
# *  Critical/explanation :  No
# **************************************************************
def detect_faces(image):
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces


# **************************************************************
# *  Name                 :  predict
# *  Description          :  1. Starts a model.
#                            2. Captures an image.
#                            3. Formats the img to fit the model.
#                            4. Saves the output image into output_img_path.
#                            to save an image.
# *  Parameters           :  model_path, output_img_path
# *  Return               :  predicted emotion
# *  Critical/explanation :  No
# **************************************************************
def predict(model_path: str, output_img_path: str):

    # Load pre-trained Facial Emotion Recognition model
    model = load_model(model_path)

    # Open camera reference
    cap = cv2.VideoCapture(0)  # Use the default webcam
    ret, frame = cap.read()

    # Detect faces in the captured frame
    faces = detect_faces(frame)

    # Process each detected face
    for (x, y, w, h) in faces:

        face = frame[y:y+h, x:x+w]
        face_resized = cv2.resize(face, (48, 48))
        face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
        normalized = face_gray / 255.0

        # Prepare the image for the model
        normalized = np.expand_dims(normalized, axis=-1)
        normalized = np.expand_dims(normalized, axis=0)

        # Use the model to predict the emotion
        emotion_labels = ['Angry', 'Sad', 'Neutral']
        prediction = model.predict(normalized, verbose=0)
        predicted_emotion = emotion_labels[np.argmax(prediction)]

        cv2.putText(frame, predicted_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the captured frame
    # cv2.imshow('Facial Emotion Recognition', frame)
    save_image(frame, output_img_path)

    # Release the webcam and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    return 'The predicted emotion is: ' + predicted_emotion

def main():
    # Globals
    model_path = 'C:/Projects/579-Intelligent-Systems-Term-Project/06_Source/Python/Models/modelv9_Angry_Sad_Neutral.h5'
    prediction_img_output_path = 'C:/Projects/579-Intelligent-Systems-Term-Project/06_Source/Python/Dependencies/captured_image.jpg'
        
    emotion = predict(model_path, prediction_img_output_path)
    print(emotion)

if __name__=="__main__":
    main()