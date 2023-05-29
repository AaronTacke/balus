import requests
from time import sleep
from pymycobot import MyCobot, Angle, Coord
from pymycobot import MyCobotSocket

# URL to access model component
model_url = "http://localhost:1110/view/should_learn"


class Cobot:
    def __init__(self, ip, port):
        self.cobot = MyCobotSocket(ip, port);

    def color_blink(self, rgb):
        # Should contain either red, blue or green set to 10
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        i = 0
        while i < 25:
            self.cobot.set_color(rgb[0] * i, rgb[1] * i, rgb[2] * i)
            # sleep(0.005)
            i += 2

    def straight(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([0, 0, 0, 0, 0, 0], 20)
        sleep(5)

    def curled_up(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([90, 140, -145, -60, -90, 0], 20)
        sleep(5)

    def curled_up_wiggle(self, rgb):
        # Default Setup for Curled state
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.curled_up(rgb)
        sleep(5)
        self.cobot.send_angle(Angle.J4.value, 0, 20)
        sleep(2)
        # Start Animation
        self.cobot.send_angle(Angle.J4.value, 45, 40)
        sleep(1)
        self.cobot.send_angle(Angle.J4.value, -45, 40)
        sleep(1)
        self.cobot.send_angle(Angle.J4.value, 45, 40)
        sleep(1)
        self.cobot.send_angle(Angle.J4.value, -45, 40)
        sleep(1)
        self.cobot.send_angle(Angle.J4.value, 45, 40)
        sleep(1)
        self.cobot.send_angle(Angle.J4.value, 0, 40)
        sleep(1)

    def hide(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([87.89, -93.6, -79.8, -98.17, -87.01, -91.4], 20)
        sleep(10)

    def lay_down(self, rgb):
        self.cobot.set_color(rgb[0], rgb[1], rgb[2])
        self.cobot.send_angles([90, 140, -40, -5, -90, 0], 20)
        sleep(10)


# Print response every second
def main():
    cobot = Cobot("10.42.0.141", 9000)

    sleep(5)
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
    # while True:
    #    print(requests.get(model_url).text)
    #    sleep(1)


if __name__ == '__main__':
    main()
