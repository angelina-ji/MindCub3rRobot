from ev3dev2.motor import MediumMotor, OUTPUT_C
from ev3dev2.motor import SpeedPercent
import time

scanner = MediumMotor(OUTPUT_C)

degrees = int(input("Enter degrees: "))
print("Moving scanner...")
scanner.on_for_degrees(SpeedPercent(30), -degrees)
time.sleep(1)
print("Moving back...")
scanner.on_for_degrees(SpeedPercent(30), degrees)
