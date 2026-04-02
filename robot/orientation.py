OPPOSITE = {'W':'Y','Y':'W','G':'B','B':'G','R':'O','O':'R'}

def make_orientation():
    return {'top':'W','bottom':'Y','front':'G','back':'B','left':'O','right':'R'}

def apply_tilt(o):
    return {'top':o['right'],'bottom':o['left'],'front':o['front'],
            'back':o['back'],'left':o['top'],'right':o['bottom']}

def apply_spin_cw(o):
    return {'top':o['top'],'bottom':o['bottom'],'front':o['right'],
            'back':o['left'],'left':o['front'],'right':o['back']}

def apply_spin_ccw(o):
    return {'top':o['top'],'bottom':o['bottom'],'front':o['left'],
            'back':o['right'],'left':o['back'],'right':o['front']}

def apply_spin_180(o):
    return {'top':o['top'],'bottom':o['bottom'],'front':o['back'],
            'back':o['front'],'left':o['right'],'right':o['left']}

def apply_action(o, action):
    if action == 'TILT':     return apply_tilt(o)
    if action == 'SPIN_CW':  return apply_spin_cw(o)
    if action == 'SPIN_CCW': return apply_spin_ccw(o)
    if action == 'SPIN_180': return apply_spin_180(o)
    return o

def get_actions_to_bottom(o, target_color):
    pos = [k for k,v in o.items() if v == target_color][0]
    if pos == 'bottom':   return []
    elif pos == 'top':    return ['TILT', 'TILT']
    elif pos == 'left':   return ['TILT']
    elif pos == 'right':  return ['SPIN_180', 'TILT']
    elif pos == 'front':  return ['SPIN_CW', 'TILT']
    elif pos == 'back':   return ['SPIN_CCW', 'TILT']

def get_turn_for_move(wca_move):
    if '2' in wca_move: return 'TURN_180'
    if "'" in wca_move: return 'TURN_CCW'
    return 'TURN_CW'

MOVE_FACE_COLOR = {
    'U':'W', 'D':'Y', 'F':'G', 'B':'B', 'R':'R', 'L':'O'
}

def execute_scramble(scramble):
    o = make_orientation()
    all_actions = []
    for move in scramble.strip().split():
        face = move[0]
        target = MOVE_FACE_COLOR[face]
        turn = get_turn_for_move(move)
        setup = get_actions_to_bottom(o, target)
        for action in setup:
            o = apply_action(o, action)
        all_actions.extend(setup)
        all_actions.append(turn)
    return all_actions

if __name__ == '__main__':
    scramble = input('Enter scramble: ')
    actions = execute_scramble(scramble)
    print('Actions (' + str(len(actions)) + '):')
    for a in actions:
        print(' ', a)
