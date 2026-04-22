from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.motor import SpeedPercent
import time

tilt  = LargeMotor(OUTPUT_A)
table = LargeMotor(OUTPUT_B)

print("Testing turntable - 90 degrees CW...")
table.on_for_degrees(SpeedPercent(30), 90)
time.sleep(1)

print("Testing turntable - 90 degrees back...")
table.on_for_degrees(SpeedPercent(30), -90)
time.sleep(1)

print("Done!")
