from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.motor import SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2
import math, time

tilt  = LargeMotor(OUTPUT_A)
table = LargeMotor(OUTPUT_B)
scanner_motor = MediumMotor(OUTPUT_C)
sensor = ColorSensor(INPUT_2)

KNOWN = {}

def read_rgb():
    scanner_motor.on_for_degrees(SpeedPercent(30), -420)
    time.sleep(0.5)
    rgb = sensor.rgb
    scanner_motor.on_for_degrees(SpeedPercent(30), 420)
    time.sleep(0.3)
    return rgb

def tilt_ccw():
    tilt.on_for_degrees(SpeedPercent(30), 275)
    time.sleep(0.1)
    tilt.on_for_degrees(SpeedPercent(30), -275)
    time.sleep(0.3)

def rotate_whole_cube_cw():
    table.on_for_degrees(SpeedPercent(40), -270)
    time.sleep(0.5)

def rotate_whole_cube_ccw():
    table.on_for_degrees(SpeedPercent(40), 270)
    time.sleep(0.5)

print("Starting scan - place cube white up, green front")
input("Press enter to start...")

print("Scanning U (white)...")
KNOWN['W'] = read_rgb()
print("W =", KNOWN['W'])

tilt_ccw()
print("Scanning R (red)...")
KNOWN['R'] = read_rgb()
print("R =", KNOWN['R'])

tilt_ccw()
print("Scanning D (yellow)...")
KNOWN['Y'] = read_rgb()
print("Y =", KNOWN['Y'])

tilt_ccw()
print("Scanning L (orange)...")
KNOWN['O'] = read_rgb()
print("O =", KNOWN['O'])

tilt_ccw()
rotate_whole_cube_cw()

tilt_ccw()
print("Scanning F (green)...")
KNOWN['G'] = read_rgb()
print("G =", KNOWN['G'])

tilt_ccw()
tilt_ccw()
print("Scanning B (blue)...")
KNOWN['B'] = read_rgb()
print("B =", KNOWN['B'])

tilt_ccw()
rotate_whole_cube_ccw()

print("\nScan complete!")
for color, rgb in KNOWN.items():
    print(color + ": " + str(rgb))
