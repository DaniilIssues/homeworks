import time
class TrafficLights():
    def __init__(self, red_t, yellow_t, green_t):
        self.red_t = red_t
        self.yellow_t = yellow_t
        self.green_t = green_t
    def on(self):
        print("Red ON!")
        time.sleep(self.red_t)
        print("Red OFF!")
        time.sleep(0.5)
        print("Yellow ON!")
        time.sleep(self.yellow_t)
        print("Yellow OFF!")
        time.sleep(0.5)
        print("Green ON!")
        time.sleep(self.green_t)
        print("Green OFF!")

light = TrafficLights(int(input("Red:")), int(input("Yellow:")), int(input("Green:")))

print(light.on())

