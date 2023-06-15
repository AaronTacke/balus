import time
from hand_gestures.hand_gesture_class import HandGestureRecognizer
import requests

mad_url = "http://localhost:1110/model/is_mad"
leaving_url = "http://localhost:1110/model/is_leaving"
back_url = "http://localhost:1110/model/is_back"


# Call the model if a relevant hand gesture was detected
def main():
    recognizer = HandGestureRecognizer()
    while True:
        gesture = recognizer.get_current_gesture()
        if gesture == "stop" or gesture == "live long":
            requests.get(mad_url)
        if gesture == "thumbs up":
            requests.get(back_url)
        if gesture == "thumbs down":
            requests.get(leaving_url)
        time.sleep(1)


if __name__ == '__main__':
    main()
