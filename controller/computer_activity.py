from pynput import keyboard, mouse
from time import sleep, time
import requests

inactive_threshold = 5  # [sec]

learning_url = "http://localhost:1110/model/is_learning"
relaxing_url = "http://localhost:1110/model/is_relaxing"

last_input = 0


# Update last_input time
def input_action(*_):
    global last_input
    last_input = time()


# Use keyboard and mouse listener to feed model with information
def main():
    global is_learning
    with mouse.Listener(on_move=input_action, on_click=input_action, on_scroll=input_action) as mouse_listener:
        with keyboard.Listener(on_press=input_action, on_release=input_action) as keyboard_listener:
            while True:
                if time() - last_input > inactive_threshold:
                    requests.get(relaxing_url)
                else:
                    requests.get(learning_url)
                sleep(1)


if __name__ == '__main__':
    main()
