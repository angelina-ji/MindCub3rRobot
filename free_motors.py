from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
tilt = LargeMotor(OUTPUT_A)
table = LargeMotor(OUTPUT_B)
tilt.reset()
table.reset()
