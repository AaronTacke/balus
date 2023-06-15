import os
import time

import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model


class HandGestureRecognizer:

    def __init__(self):
        # initialize mediapipe
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils

        # Load the gesture recognizer model
        self.script_dir = os.path.dirname(__file__)  # Get the directory of the current script
        self.model = load_model(os.path.join(self.script_dir, 'mp_hand_gesture'))

        # Load class names
        f = open(os.path.join(self.script_dir, 'gesture.names'), 'r')
        self.classNames = f.read().split('\n')
        f.close()
        print(self.classNames)

        # Initialize the webcam
        self.cap = cv2.VideoCapture(1)

    def get_current_gesture(self):
        # Read each frame from the webcam
        _, frame = self.cap.read()

        x, y, c = frame.shape

        # Flip the frame vertically
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get hand landmark prediction
        result = self.hands.process(framergb)

        className = ''

        # post process the result
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])

                # Predict gesture
                prediction = self.model.predict([landmarks])
                classID = np.argmax(prediction)
                className = self.classNames[classID]

        return className
