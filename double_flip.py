from robot.motor import flip
import time
print('Flip 1 P1->P1...')
flip(stay=True)
time.sleep(0.5)
print('Flip 2 P1->P1...')
flip(stay=True)
time.sleep(0.5)
print('Done!')
