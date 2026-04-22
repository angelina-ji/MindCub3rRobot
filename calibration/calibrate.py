from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2

sensor = ColorSensor(INPUT_2)

colors = ['White', 'Yellow', 'Green', 'Blue', 'Red', 'Orange']
readings = {}

for color in colors:
    input("Hold sensor to " + color + " sticker, then press enter...")
    rgb = sensor.rgb
    readings[color] = rgb
    print(color + ": " + str(rgb))

print("\nAll readings:")
for color, rgb in readings.items():
    print(color + ": " + str(rgb))
