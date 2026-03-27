from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2
import math

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

while True:
    rgb = sensor.rgb
    color = detect_color(rgb)
    print("RGB: " + str(rgb) + " -> Detected: " + color)
    input("Press enter for next sticker...")
