from robot.motor import tilt_forward, turn_cw
import time

print("Tilt 1...")
tilt_forward()
time.sleep(0.5)
print("Turn CW...")
turn_cw()
time.sleep(0.5)
print("Tilt 2...")
tilt_forward()
print("Done!")
