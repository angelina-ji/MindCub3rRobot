from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.motor import SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2
import math, time

tilt  = LargeMotor(OUTPUT_A)
table = LargeMotor(OUTPUT_B)
scanner_motor = MediumMotor(OUTPUT_C)
sensor = ColorSensor(INPUT_2)

KNOWN = {
    'W': (238, 255, 192),
    'Y': (198, 238, 204),
    'G': (37, 127, 84),
    'B': (25, 70, 79),
    'R': (132, 99, 34),
    'O': (164, 195, 159),
}

def detect_color(rgb):
    best = None
    best_dist = float('inf')
    for name, ref in KNOWN.items():
        dist = math.sqrt(sum((a-b)**2 for a,b in zip(rgb, ref)))
        if dist < best_dist:
            best_dist = dist
            best = name
    return best

def scan():
    scanner_motor.on_for_degrees(SpeedPercent(30), -420)
    time.sleep(0.5)
    rgb = sensor.rgb
    color = detect_color(rgb)
    time.sleep(0.3)
    scanner_motor.on_for_degrees(SpeedPercent(30), 420)
    time.sleep(0.5)
    return color

def tilt_ccw():
    tilt.on_for_degrees(SpeedPercent(30), 275)
    time.sleep(0.3)
    tilt.on_for_degrees(SpeedPercent(10), -275)
    time.sleep(0.5)

def rotate_whole_cube_cw():
    table.on_for_degrees(SpeedPercent(40), -270)
    time.sleep(0.5)

def rotate_whole_cube_ccw():
    table.on_for_degrees(SpeedPercent(40), 270)
    time.sleep(0.5)

print("Starting scan - place cube white up, green front")
input("Press enter to start...")

results = {}

print("Scanning U (white)...")
results['U'] = scan()

tilt_ccw()
print("Scanning R (red)...")
results['R'] = scan()

tilt_ccw()
print("Scanning D (yellow)...")
results['D'] = scan()

tilt_ccw()
print("Scanning L (orange)...")
results['L'] = scan()

tilt_ccw()
rotate_whole_cube_cw()

tilt_ccw()
print("Scanning F (green)...")
results['F'] = scan()

tilt_ccw()
tilt_ccw()
print("Scanning B (blue)...")
results['B'] = scan()

tilt_ccw()
rotate_whole_cube_ccw()

print("\nScan complete!")
print("U (white face):", results['U'])
print("R (red face):  ", results['R'])
print("D (yellow face):", results['D'])
print("L (orange face):", results['L'])
print("B (blue face): ", results['B'])
print("F (green face):", results['F'])
