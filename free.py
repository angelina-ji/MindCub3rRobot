from ev3dev2.motor import LargeMotor, OUTPUT_A
tilt = LargeMotor(OUTPUT_A)
tilt.stop_action = 'coast'
tilt.stop()
tilt.reset()
print('State:', tilt.state)
print('Position:', tilt.position)
