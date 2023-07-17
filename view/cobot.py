import requests
import time
from random import randint
from pymycobot import MyCobot, Angle, Coord
from pymycobot import MyCobotSocket

# URL to access model component
model_url = "http://localhost:1110/view/should_learn"


class Cobot:
    cobot = {}

    def __init__(self, ip, port):
        self.cobot = MyCobotSocket(ip, port)

    def color_blink(self, rgb):
        # Should contain either red, blue or green set to 10
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        i = 0
        while i < 24:
            self.cobot.set_color(rgb[0] * i, rgb[1] + (i * 10), rgb[2] * i)
            time.sleep(0.005)
            i += 2

    def inverse_color_blink(self, rgb):
        # Should contain either red, blue or green set to 250
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        i = 0
        while i <= 25:
            self.cobot.set_color(rgb[0] * i, rgb[1] - (i * 10), rgb[2] * i)
            time.sleep(0.005)
            i += 2
        self.cobot.set_color(0, 0, 0)

    def straight(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([0, 0, 0, 0, 0, 0], 20)
        time.sleep(2)

    def curled_up(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([90, 140, -145, -60, -90, 0], 20)
        time.sleep(2)

    def curled_up_wiggle(self, rgb):
        # Default Setup for Curled state
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.curled_up(rgb)
        self.cobot.send_angle(Angle.J4.value, 0, 20)
        time.sleep(3)
        # Start Animation
        self.cobot.send_angle(Angle.J4.value, 45, 40)
        time.sleep(1)
        self.cobot.send_angle(Angle.J4.value, -45, 40)
        time.sleep(1)
        self.cobot.send_angle(Angle.J4.value, 45, 40)
        time.sleep(1)
        self.cobot.send_angle(Angle.J4.value, -45, 40)
        time.sleep(1)

    def hide(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([87.89, -93.6, -79.8, -98.17, -87.01, -91.4], 20)
        time.sleep(2)

    def lay_down(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([90, 135, -40, -5, -90, 0], 20)
        time.sleep(2)


def preview_v1():
    cobot = Cobot("10.42.0.141", 9000)
    print("Straight")
    cobot.straight([0, 0, 255])
    print("Color_Blink")
    cobot.color_blink([0, 10, 0])
    print("Curled up straight wiggle")
    cobot.curled_up_wiggle([0, 255, 0])
    print("Hide")
    cobot.hide([0, 0, 255])
    print("Lay Down")
    cobot.lay_down([0, 0, 0])
    print("Straight")
    cobot.straight([255, 0, 0])


def preview_v2():
    cobot = Cobot("10.42.0.141", 9000)
    print("Start: Hide")
    cobot.hide([0, 0, 0])
    # Reset
    time.sleep(5)
    cobot.hide([0, 0, 255])
    time.sleep(3)
    print("Start: Lay_Down")
    cobot.lay_down([0, 0, 0])
    # Reset
    time.sleep(5)
    cobot.hide([0, 0, 255])
    time.sleep(3)
    print("Start: Lay_Down[Yellow]")
    cobot.lay_down([0, 0, 0])
    cobot.lay_down([255, 255, 0])
    # Reset
    time.sleep(5)
    cobot.hide([0, 0, 255])
    time.sleep(3)
    print("Start: Wake Up")
    cobot.lay_down([0, 0, 0])
    cobot.color_blink([0, 10, 0])
    # Reset
    time.sleep(5)
    cobot.hide([0, 0, 255])
    time.sleep(3)
    print("Start: Straight")
    cobot.straight([255, 0, 0])
    # Reset
    time.sleep(5)
    cobot.hide([0, 0, 255])
    time.sleep(3)
    print("Start: Wiggle")
    cobot.curled_up_wiggle([0, 255, 0])
    # Reset
    time.sleep(5)
    cobot.hide([0, 0, 255])
    time.sleep(3)
    print("Start Inverse Wake Up")
    cobot.curled_up([0, 255, 0])
    cobot.inverse_color_blink([0, 255, 0])
    # Reset
    time.sleep(5)
    cobot.hide([0, 0, 255])
    time.sleep(3)
    print("Finish")


def preview_v3():
    cobot = Cobot("10.42.0.141", 9000)
    cobot.hide([0, 0, 0])
    print("Starting in 5s...")
    time.sleep(3)
    print("Thumbs up")
    time.sleep(3)
    cobot.lay_down([0, 0, 0])
    print("Work 5s...")
    time.sleep(10)
    print("Use Phone")
    time.sleep(5)
    cobot.lay_down([255, 255, 0])
    time.sleep(2)
    print("Put Phone down...")
    time.sleep(2)
    cobot.lay_down([0, 0, 0])
    time.sleep(3)
    cobot.color_blink([0, 10, 0])
    print("Hand...")
    time.sleep(5)
    cobot.lay_down([0, 0, 0])
    time.sleep(2)
    cobot.color_blink([0, 10, 0])
    time.sleep(3)
    print("Pause...")
    cobot.straight([255, 0, 0])
    time.sleep(3)
    print("Pause...")
    cobot.curled_up_wiggle([0, 255, 0])
    time.sleep(5)
    cobot.inverse_color_blink([0, 255, 0])
    time.sleep(3)
    print("Work...")
    cobot.lay_down([0, 0, 0])
    print("Thumbs down")
    time.sleep(5)
    cobot.hide([0, 0, 0])
    print("Finish")



def main():
    preview_v3()
    exit(0)
    # Hardcoded ==> minimum time between request checking
    min_wait_between_calls = 1

    cobot = Cobot("10.42.0.141", 9000)
    # Intended State < 0 --> Same Action with Yellow Light
    # Intended State >= 0 && <= 1.0 --> Intended State = Concentrated
    # Intended State > 1.0 && < 2.0 --> Intended State = Pause
    # Intended State == 2.0 --> Red Sraight
    prev = -2.0
    intended_state = 0.0
    rgb = [0, 255, 0]

    while True:
        start = time.time()

        # Default Lighting
        rgb = [0, 255, 0]
        # Parse current instruction
        url_state = requests.get(model_url).text
        print(url_state)
        if url_state.replace("-", "").replace(".", "").isnumeric():
            intended_state = float(url_state)
        else:
            intended_state = prev

        # Change Color to Yellow if negative and map to normal action
        if intended_state < 0:
            rgb = [255, 255, 0]
            intended_state = abs(intended_state)

        print("Intended State: " + str(intended_state) + ", rgb: " + str(rgb))

        # Call the respective cobot action for the given state ==>
        # Color is already set (if not color_blink, straight, lay_down)

        # User should learn and is either doing it or should shortly take a break (and is doing that)
        if intended_state != prev:
            match intended_state:
                # Pause Cobot (Still regularly parse upcoming action)
                case intended_state if intended_state == 0:
                    cobot.hide([0, 0, 0])
                    print("Pause Cobot")

                # User should be concentrated
                case intended_state if 0 < intended_state < 0.8:
                    if rgb == [0, 255, 0]:
                        rgb = [0, 0, 0]
                    cobot.lay_down(rgb)
                    print("lay_down(yellow or black)")
                case intended_state if 0.8 <= intended_state < 1.0:
                    cobot.color_blink([0, 10, 0])
                    print("color_blink(green)")

                # User should take a pause (and is actually taking it)
                case intended_state if 1.0 <= intended_state < 1.8:
                    cobot.curled_up_wiggle(rgb)
                    print("curled_up_wiggle(set_color)")
                case intended_state if 1.8 <= intended_state < 2.0:
                    cobot.inverse_color_blink([0, 250, 0])
                    print("inverse_color_blink(green)")

                # Straight Red --> User is not adhering to intended state
                case intended_state if intended_state == 2.0:
                    cobot.straight([255, 0, 0])
                    print("Straight(red)")

                case intended_state if (2.0 < intended_state or intended_state < -2.0):
                    break

        end = time.time()
        duration = round(end - start, 2)

        # Wait until min_wait has been reached and repeat action
        if duration < min_wait_between_calls:
            time.sleep(round(min_wait_between_calls - duration, 2))
        prev = intended_state


if __name__ == '__main__':
    main()
