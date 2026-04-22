from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.motor import SpeedPercent
import time

tilt  = LargeMotor(OUTPUT_A)
table = LargeMotor(OUTPUT_B)

def turn_cw():
    table.on_for_degrees(SpeedPercent(30), 270)

def turn_ccw():
    table.on_for_degrees(SpeedPercent(30), -270)

def tilt_forward():
    tilt.on_for_degrees(SpeedPercent(30), 360)
    time.sleep(0.5)
    tilt.on_for_degrees(SpeedPercent(15), -360)

print("Executing D move...")
turn_cw()
print("Done!")
