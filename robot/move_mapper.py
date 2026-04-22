TILT    = "TILT"
SPIN_CW  = "SPIN_CW"
SPIN_CCW = "SPIN_CCW"
SPIN_180 = "SPIN_180"
TURN_CW  = "TURN_CW"
TURN_CCW = "TURN_CCW"
TURN_180 = "TURN_180"

T = TILT

MOVE_MAP = {
    "D":  [TURN_CW],
    "D'": [TURN_CCW],
    "D2": [TURN_180],

    "U":  [T,T, TURN_CW,  T,T],
    "U'": [T,T, TURN_CCW, T,T],
    "U2": [T,T, TURN_180, T,T],

    "L":  [T, TURN_CW,  T,T,T],
    "L'": [T, TURN_CCW, T,T,T],
    "L2": [T, TURN_180, T,T,T],

    "R":  [SPIN_180, T, TURN_CW,  T,T,T, SPIN_180],
    "R'": [SPIN_180, T, TURN_CCW, T,T,T, SPIN_180],
    "R2": [SPIN_180, T, TURN_180, T,T,T, SPIN_180],

    "F":  [SPIN_CW, T, TURN_CW,  T,T,T, SPIN_CCW],
    "F'": [SPIN_CW, T, TURN_CCW, T,T,T, SPIN_CCW],
    "F2": [SPIN_CW, T, TURN_180, T,T,T, SPIN_CCW],

    "B":  [SPIN_CCW, T, TURN_CW,  T,T,T, SPIN_CW],
    "B'": [SPIN_CCW, T, TURN_CCW, T,T,T, SPIN_CW],
    "B2": [SPIN_CCW, T, TURN_180, T,T,T, SPIN_CW],
}

def scramble_to_actions(scramble):
    actions = []
    for move in scramble.strip().split():
        if move not in MOVE_MAP:
            raise KeyError("Unknown move: '" + move + "'")
        actions.extend(MOVE_MAP[move])
    return actions
