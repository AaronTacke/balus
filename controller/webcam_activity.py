import time
from hand_gestures.hand_gesture_class import HandGestureRecognizer
import requests

mad_url = "http://localhost:1110/model/is_mad"
leaving_url = "http://localhost:1110/model/is_leaving"
back_url = "http://localhost:1110/model/is_back"


# Check steps time whether the result of getter is the same
def multiple_checks(getter, steps):
    res = getter()
    for _ in range(steps):
        if getter() != res:
            res = ""
            break
    return res


# Call the model if a relevant hand gesture was detected
def main():
    recognizer = HandGestureRecognizer()
    while True:
        gesture = multiple_checks(recognizer.get_current_gesture, 15)
        if gesture == "stop" or gesture == "live long":
            requests.get(mad_url)
        if gesture == "thumbs up":
            requests.get(back_url)
        if gesture == "thumbs down":
            requests.get(leaving_url)


if __name__ == '__main__':
    main()
