from ev3dev2.motor import LargeMotor, OUTPUT_A, SpeedPercent
tilt = LargeMotor(OUTPUT_A)
print('State:', tilt.state)
print('Position:', tilt.position)
tilt.on_for_degrees(SpeedPercent(50), 100)
print('Done')
