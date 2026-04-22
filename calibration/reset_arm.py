from ev3dev2.motor import LargeMotor, OUTPUT_A, SpeedPercent
tilt = LargeMotor(OUTPUT_A)
tilt.reset()
tilt.on_for_degrees(SpeedPercent(10), -180)
