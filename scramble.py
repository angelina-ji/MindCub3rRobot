from robot.motor import turn_cw, turn_ccw, turn_180, tilt_forward
from robot.move_mapper import MOVE_MAP
import time

def execute_move(move):
    actions = MOVE_MAP[move]
    for action in actions:
        if action == 'TURN_CW':
            turn_cw()
        elif action == 'TURN_CCW':
            turn_ccw()
        elif action == 'TURN_180':
            turn_180()
        elif action == 'TILT_FRONT':
            tilt_forward()
        time.sleep(0.3)

scramble = input("Enter scramble: ").strip().split()
print("Executing " + str(len(scramble)) + " moves...")

for move in scramble:
    print("Move: " + move)
    execute_move(move)
    time.sleep(0.2)

print("Done!")
