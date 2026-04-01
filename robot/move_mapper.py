# Physical action constants
TILT    = "TILT"       # arm tilts cube left (U->L->D->R->U)
SPIN_CW  = "SPIN_CW"   # whole cube spins CW from top
SPIN_CCW = "SPIN_CCW"  # whole cube spins CCW from top
SPIN_180 = "SPIN_180"  # whole cube spins 180
TURN_CW  = "TURN_CW"   # bottom layer CW
TURN_CCW = "TURN_CCW"  # bottom layer CCW
TURN_180 = "TURN_180"  # bottom layer 180

T = TILT

MOVE_MAP = {
    # D face - bottom, just turn
    "D":  [TURN_CW],
    "D'": [TURN_CCW],
    "D2": [TURN_180],

    # U face - tilt x2, turn, tilt x2
    "U":  [T,T, TURN_CW,  T,T],
    "U'": [T,T, TURN_CCW, T,T],
    "U2": [T,T, TURN_180, T,T],

    # L face - tilt x1, turn, tilt x3
    "L":  [T, TURN_CW,  T,T,T],
    "L'": [T, TURN_CCW, T,T,T],
    "L2": [T, TURN_180, T,T,T],

    # R face - spin 180, tilt x1, turn, tilt x3, spin 180
    "R":  [SPIN_180, T, TURN_CW,  T,T,T, SPIN_180],
    "R'": [SPIN_180, T, TURN_CCW, T,T,T, SPIN_180],
    "R2": [SPIN_180, T, TURN_180, T,T,T, SPIN_180],

    # F face - spin CW 90, tilt x1, turn, tilt x3, spin CCW 90
    "F":  [SPIN_CW, T, TURN_CW,  T,T,T, SPIN_CCW],
    "F'": [SPIN_CW, T, TURN_CCW, T,T,T, SPIN_CCW],
    "F2": [SPIN_CW, T, TURN_180, T,T,T, SPIN_CCW],

    # B face - spin CCW 90, tilt x1, turn, tilt x3, spin CW 90
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
