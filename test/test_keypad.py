from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.button import Button

btn = Button()

print("Press any EV3 button...")
while True:
    if btn.up:
        print("UP pressed")
    if btn.down:
        print("DOWN pressed")
    if btn.left:
        print("LEFT pressed")
    if btn.right:
        print("RIGHT pressed")
    if btn.enter:
        print("ENTER pressed")
    if btn.backspace:
        print("BACK pressed")
        break
