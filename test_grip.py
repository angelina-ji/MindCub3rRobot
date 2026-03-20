from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.motor import SpeedPercent
import time

tilt  = LargeMotor(OUTPUT_A)
table = LargeMotor(OUTPUT_B)

grip = int(input("Enter grip degrees: "))
print("Gripping...")
tilt.on_for_degrees(SpeedPercent(30), grip)
time.sleep(0.5)
print("Rotating table...")
table.on_for_degrees(SpeedPercent(60), 270)
time.sleep(0.5)
print("Releasing...")
tilt.on_for_degrees(SpeedPercent(15), -grip)
