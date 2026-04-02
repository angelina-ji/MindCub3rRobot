from robot.orientation import execute_scramble
from robot.motor import tilt_forward, spin_cw, spin_ccw, spin_180, turn_cw, turn_ccw, turn_180
import time

ACTION_MAP = {
    'TILT':     tilt_forward,
    'SPIN_CW':  spin_cw,
    'SPIN_CCW': spin_ccw,
    'SPIN_180': spin_180,
    'TURN_CW':  turn_cw,
    'TURN_CCW': turn_ccw,
    'TURN_180': turn_180,
}

scramble = input('Enter scramble: ').strip()
actions = execute_scramble(scramble)
print('Executing ' + str(len(actions)) + ' actions...')

for action in actions:
    print(action)
    ACTION_MAP[action]()
    time.sleep(0.2)

print('Done!')
