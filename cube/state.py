"""
cube/state.py
-------------
WCA-correct cube engine. Does NOT use PyCuber for move execution —
PyCuber's move definitions do not match WCA/csTimer standard for complex
scrambles, producing wrong sticker positions.

Orientation (matches csTimer default):
  U=White, D=Yellow, F=Green, B=Blue, L=Orange, R=Red
"""

import copy

SOLVED_COLOURS = {
    "U": "W", 
    "D": "Y", 
    "F": "G",
    "B": "B", 
    "L": "O", 
    "R": "R",
}

VALID_MOVES = {
    "U", "U'", 
    "U2", "D", 
    "D'", "D2",
    "F", "F'", 
    "F2", "B", 
    "B'", "B2",
    "L", "L'", 
    "L2", "R", 
    "R'", "R2",
}

CubeState = dict

def make_solved() -> CubeState:
    return {f: [[c]*3 for _ in range(3)] for f, c in SOLVED_COLOURS.items()}

def _rot_cw(face):
    return [[face[2-j][i] for j in range(3)] for i in range(3)]

def _rot_ccw(face):
    return [row[::-1] for row in _rot_cw(face)[::-1]]

def _apply_once(c, face, inv):
    c = copy.deepcopy(c)
    c[face] = _rot_ccw(c[face]) if inv else _rot_cw(c[face])

    if face == "U":
            f0, r0, b0, l0 = c["F"][0][:], c["R"][0][:], c["B"][0][:], c["L"][0][:]
            if not inv: 
                # Clockwise: Front gets Right, Right gets Back, etc.
                c["F"][0] = r0
                c["R"][0] = b0
                c["B"][0] = l0
                c["L"][0] = f0
            else:       
                # Counter-clockwise: Front gets Left, Left gets Back, etc.
                c["F"][0] = l0
                c["L"][0] = b0
                c["B"][0] = r0
                c["R"][0] = f0
    elif face == "D":
            f2, r2, b2, l2 = c["F"][2][:], c["R"][2][:], c["B"][2][:], c["L"][2][:]
            if not inv: 
                # Clockwise D: Front -> Right -> Back -> Left -> Front
                c["R"][2] = f2
                c["B"][2] = r2
                c["L"][2] = b2
                c["F"][2] = l2
            else:       
                # Counter-clockwise D': Front -> Left -> Back -> Right -> Front
                c["L"][2] = f2
                c["B"][2] = l2
                c["R"][2] = b2
                c["F"][2] = l2
    elif face == "F":
        u2=[c["U"][2][i] for i in range(3)]; r0=[c["R"][i][0] for i in range(3)]
        d0=[c["D"][0][i] for i in range(3)]; l2=[c["L"][i][2] for i in range(3)]
        if not inv:
            for i in range(3): c["R"][i][0]=u2[i]
            c["D"][0]=list(r0)
            for i in range(3): c["L"][i][2]=d0[2-i]
            for i in range(3): c["U"][2][i]=l2[2-i]
        else:
            for i in range(3): c["L"][i][2]=u2[2-i]
            c["D"][0]=[l2[2],l2[1],l2[0]]
            for i in range(3): c["R"][i][0]=d0[i]
            c["U"][2]=list(r0)
    elif face == "B":
        u0=[c["U"][0][i] for i in range(3)]; l0=[c["L"][i][0] for i in range(3)]
        d2=[c["D"][2][i] for i in range(3)]; r2=[c["R"][i][2] for i in range(3)]
        if not inv:
            for i in range(3): c["L"][i][0]=u0[2-i]
            c["D"][2]=list(l0)
            for i in range(3): c["R"][i][2]=d2[2-i]
            c["U"][0]=list(r2)
        else:
            for i in range(3): c["R"][i][2]=u0[2-i]
            c["D"][2]=list(r2)
            for i in range(3): c["L"][i][0]=d2[2-i]
            c["U"][0]=list(l0)
    elif face == "R":
        u2=[c["U"][i][2] for i in range(3)]; f2=[c["F"][i][2] for i in range(3)]
        d2=[c["D"][i][2] for i in range(3)]; b0=[c["B"][i][0] for i in range(3)]
        if not inv:
            for i in range(3): c["U"][i][2]=f2[i]
            for i in range(3): c["B"][i][0]=u2[2-i]
            for i in range(3): c["D"][i][2]=b0[2-i]
            for i in range(3): c["F"][i][2]=d2[i]
        else:
            for i in range(3): c["F"][i][2]=u2[i]
            for i in range(3): c["D"][i][2]=f2[i]
            for i in range(3): c["B"][i][0]=d2[2-i]
            for i in range(3): c["U"][i][2]=b0[2-i]
    elif face == "L":
        u0=[c["U"][i][0] for i in range(3)]; f0=[c["F"][i][0] for i in range(3)]
        d0=[c["D"][i][0] for i in range(3)]; b2=[c["B"][i][2] for i in range(3)]
        if not inv:
            for i in range(3): c["F"][i][0]=u0[i]
            for i in range(3): c["D"][i][0]=f0[i]
            for i in range(3): c["B"][i][2]=d0[2-i]
            for i in range(3): c["U"][i][0]=b2[2-i]
        else:
            for i in range(3): c["U"][i][0]=f0[i]
            for i in range(3): c["F"][i][0]=d0[i]
            for i in range(3): c["D"][i][0]=b2[2-i]
            for i in range(3): c["B"][i][2]=u0[2-i]
    return c

def apply_move(state: CubeState, move: str) -> CubeState:
    if move not in VALID_MOVES:
        raise ValueError("Invalid move: '" + move + "'. Valid: " + str(sorted(VALID_MOVES)))
    face = move[0]
    inv  = "'" in move
    dbl  = "2" in move
    if dbl:
        state = _apply_once(state, face, False)
        state = _apply_once(state, face, False)
    else:
        state = _apply_once(state, face, inv)
    return state

def apply_scramble(scramble: str) -> CubeState:
    """Apply a WCA scramble string to a solved cube. Returns CubeState."""
    state = make_solved()
    for move in scramble.strip().split():
        state = apply_move(state, move)
    return state

def get_face_grid(state: CubeState, face: str) -> list:
    """Return the 3x3 grid for a face. Compatible with display.py."""
    return state[face]