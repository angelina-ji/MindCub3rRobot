from ev3dev2.motor import LargeMotor, OUTPUT_A
from ev3dev2.motor import SpeedPercent
import time

tilt = LargeMotor(OUTPUT_A)

print("Tilting forward...")
tilt.on_for_degrees(SpeedPercent(30), 360)
time.sleep(0.5)
print("Returning slowly...")
tilt.on_for_degrees(SpeedPercent(15), -360)
