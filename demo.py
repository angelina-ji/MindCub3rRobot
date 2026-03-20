from robot.motor import tilt_forward, turn_cw, turn_ccw, release
import time

print("MindCub3r Demo")
print("==============")
input("Press enter to start...")

print("Move 1: Rotating bottom layer...")
turn_cw()
time.sleep(1)

print("Move 2: Rotating bottom layer back...")
turn_ccw()
time.sleep(1)

print("Move 3: Flipping cube...")
tilt_forward()
time.sleep(1)

print("Resetting arm...")
release()

print("Done!")
