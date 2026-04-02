from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.motor import SpeedPercent
import time

tilt  = LargeMotor(OUTPUT_A)
table = LargeMotor(OUTPUT_B)

def grip():
    tilt.on_for_degrees(SpeedPercent(30), 90)

def release():
    tilt.on_for_degrees(SpeedPercent(15), -90)

def tilt_forward():
    tilt.on_for_degrees(SpeedPercent(30), 275)
    time.sleep(0.1)
    tilt.on_for_degrees(SpeedPercent(30), -275)

def turn_cw():
    grip()
    table.on_for_degrees(SpeedPercent(60), -270)
    release()

def turn_ccw():
    grip()
    table.on_for_degrees(SpeedPercent(60), 270)
    release()

def turn_180():
    grip()
    table.on_for_degrees(SpeedPercent(60), 540)
    release()

def spin_cw():
    table.on_for_degrees(SpeedPercent(40), 270)
    time.sleep(0.3)

def spin_ccw():
    table.on_for_degrees(SpeedPercent(40), -270)
    time.sleep(0.3)

def spin_180():
    table.on_for_degrees(SpeedPercent(40), 540)
    time.sleep(0.3)
