import requests
import time
from random import randint
from pymycobot import MyCobot, Angle, Coord
from pymycobot import MyCobotSocket

# URL to access model component
model_url = "http://localhost:1110/view/should_learn"


class Cobot:
    def __init__(self, ip, port):
        self.cobot = MyCobotSocket(ip, port)

    def color_blink(self, rgb):
        # Should contain either red, blue or green set to 10
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        i = 0
        while i < 25:
            self.cobot.set_color(rgb[0] * i, rgb[1] * i, rgb[2] * i)
            time.sleep(0.005)
            i += 2

    def straight(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([0, 0, 0, 0, 0, 0], 20)
        time.sleep(5)

    def curled_up(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([90, 140, -145, -60, -90, 0], 20)
        time.sleep(5)

    def curled_up_wiggle(self, rgb):
        # Default Setup for Curled state
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.curled_up(rgb)
        time.sleep(5)
        self.cobot.send_angle(Angle.J4.value, 0, 20)
        time.sleep(2)
        # Start Animation
        self.cobot.send_angle(Angle.J4.value, 45, 40)
        time.sleep(1)
        self.cobot.send_angle(Angle.J4.value, -45, 40)
        time.sleep(1)
        self.cobot.send_angle(Angle.J4.value, 45, 40)
        time.sleep(1)
        self.cobot.send_angle(Angle.J4.value, -45, 40)
        time.sleep(1)
        self.cobot.send_angle(Angle.J4.value, 45, 40)
        time.sleep(1)
        self.cobot.send_angle(Angle.J4.value, 0, 40)
        time.sleep(1)

    def hide(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([87.89, -93.6, -79.8, -98.17, -87.01, -91.4], 20)
        time.sleep(10)

    def lay_down(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([90, 140, -40, -5, -90, 0], 20)
        time.sleep(10)


def preview():
    cobot = Cobot("10.42.0.141", 9000)
    time.sleep(5)
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


def main():
    # Hardcoded ==> minimum time between request checking
    min_wait_between_calls = 30

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

        rgb = [0, 255, 0]
        # Parse current instruction
        url_state = requests.get(model_url).text
        if url_state.isnumeric():
            intended_state = float(url_state)
        else:
            intended_state = prev

        # TODO Fetch parameters from the model_url
        # Change Color to Yellow if negative and change to normale action
        if intended_state == prev:
            continue

        if intended_state < 0:
            rgb = [255, 255, 0]
            intended_state = abs(intended_state)

        # Call the respective cobot action for the given state ==>
        # Color is already set (if not color_blink, straight, lay_down)
        match intended_state:
            case intended_state if 0 <= intended_state < 0.8:
                cobot.lay_down([0, 0, 0])
                print("lay_down(black)")
            case intended_state if 0.8 <= intended_state < 1.0:
                cobot.color_blink([0, 10, 0])
                print("color_blink(green)")

            case intended_state if 1.0 <= intended_state < 2.0:
                # This should be the Pause Phase
                choice = randint(0, 1)
                match choice:
                    case 0:
                        cobot.curled_up_wiggle(rgb)
                        print(intended_state)
                    case 1:
                        cobot.hide(rgb)
                        print(intended_state)

            case intended_state if intended_state == 2.0:
                cobot.straight([255, 0, 0])
                print("Straight(red)\n")
                
            case intended_state if (2.0 < intended_state or intended_state < -2.0):
                break

        end = time.time()
        duration = round(end - start, 2)

        # Wait until nim_wait has been reached and repeat action
        if duration < min_wait_between_calls:
            time.sleep(round(min_wait_between_calls - duration, 2))
        prev = intended_state


if __name__ == '__main__':
    main()
