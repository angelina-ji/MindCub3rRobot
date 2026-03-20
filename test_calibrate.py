from ev3dev2.motor import LargeMotor, OUTPUT_B
from ev3dev2.motor import SpeedPercent
import time

table = LargeMotor(OUTPUT_B)

degrees = int(input("Enter degrees to test: "))
table.on_for_degrees(SpeedPercent(30), degrees)
