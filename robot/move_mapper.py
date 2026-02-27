"""
robot/move_mapper.py
--------------------
Translates standard WCA notation moves into physical robot action sequences.

MindCub3r hardware constraint:
  Only the BOTTOM layer rotates.
  To execute a move on any other face, the robot must first tilt/rotate
  the cube so that face becomes the bottom, perform the turn, then
  optionally restore orientation.

Cube orientation convention (matches csTimer + PyCuber default):
  White = top (U), Yellow = bottom (D), Green = front (F)

Physical actions (will call motor.py when on EV3):
  TILT_FRONT   → tilt cube toward front (U→F, F→D, D→B, B→U)
  TILT_BACK    → tilt cube toward back  (U→B, B→D, D→F, F→U)
  TILT_RIGHT   → tilt cube toward right (U→R, R→D, D→L, L→U)
  TILT_LEFT    → tilt cube toward left  (U→L, L→D, D→R, R→U)
  SPIN_CW      → rotate whole cube clockwise when viewed from top (U stays)
  SPIN_CCW     → rotate whole cube counter-clockwise from top
  TURN_CW      → bottom layer 90° clockwise  (D face CW from below)
  TURN_CCW     → bottom layer 90° counter-clockwise
  TURN_180     → bottom layer 180°

Each WCA move maps to a sequence of these physical actions.
"""

# ── Physical action constants ──────────────────────────────────────────────

TILT_FRONT  = "TILT_FRONT"
TILT_BACK   = "TILT_BACK"
TILT_RIGHT  = "TILT_RIGHT"
TILT_LEFT   = "TILT_LEFT"
SPIN_CW     = "SPIN_CW"
SPIN_CCW    = "SPIN_CCW"
TURN_CW     = "TURN_CW"
TURN_CCW    = "TURN_CCW"
TURN_180    = "TURN_180"


# ── Move map ────────────────────────────────────────────────────────────────
# Each key is a WCA move string.
# Each value is a list of physical actions to perform in order.
#
# Logic for each face:
#   D  → bottom layer already, just turn
#   U  → tilt twice (flip upside-down), turn, tilt twice back
#   F  → tilt forward (F becomes bottom), turn, tilt back
#   B  → tilt backward (B becomes bottom), turn, tilt forward
#   R  → tilt right (R becomes bottom), turn, tilt left
#   L  → tilt left (L becomes bottom), turn, tilt right

MOVE_MAP: dict[str, list[str]] = {

    # ── D face (bottom) — no tilt needed ──────────────────────
    "D":  [TURN_CW],
    "D'": [TURN_CCW],
    "D2": [TURN_180],

    # ── U face (top) — tilt front twice to flip upside-down ───
    "U":  [TILT_FRONT, TILT_FRONT, TURN_CW,  TILT_FRONT, TILT_FRONT],
    "U'": [TILT_FRONT, TILT_FRONT, TURN_CCW, TILT_FRONT, TILT_FRONT],
    "U2": [TILT_FRONT, TILT_FRONT, TURN_180, TILT_FRONT, TILT_FRONT],

    # ── F face (front) — tilt forward once ────────────────────
    "F":  [TILT_FRONT, TURN_CW,  TILT_BACK],
    "F'": [TILT_FRONT, TURN_CCW, TILT_BACK],
    "F2": [TILT_FRONT, TURN_180, TILT_BACK],

    # ── B face (back) — tilt back once ────────────────────────
    "B":  [TILT_BACK, TURN_CCW, TILT_FRONT],   # B CW from front = CCW from bottom
    "B'": [TILT_BACK, TURN_CW,  TILT_FRONT],
    "B2": [TILT_BACK, TURN_180, TILT_FRONT],

    # ── R face (right) — tilt right once ──────────────────────
    "R":  [TILT_RIGHT, TURN_CCW, TILT_LEFT],   # R CW from front = CCW from bottom
    "R'": [TILT_RIGHT, TURN_CW,  TILT_LEFT],
    "R2": [TILT_RIGHT, TURN_180, TILT_LEFT],

    # ── L face (left) — tilt left once ────────────────────────
    "L":  [TILT_LEFT, TURN_CW,  TILT_RIGHT],
    "L'": [TILT_LEFT, TURN_CCW, TILT_RIGHT],
    "L2": [TILT_LEFT, TURN_180, TILT_RIGHT],
}


def scramble_to_actions(scramble: str) -> list[str]:
    """
    Convert a full WCA scramble string into a flat list of physical actions.

    Args:
        scramble: e.g. "U F' D2 R L"

    Returns:
        List of action strings, e.g. ["TILT_FRONT", "TILT_FRONT", "TURN_CW", ...]

    Raises:
        KeyError: if a move in the scramble is not in MOVE_MAP.
    """
    actions = []
    for move in scramble.strip().split():
        if move not in MOVE_MAP:
            raise KeyError(f"Unknown move: '{move}'. Valid moves: {list(MOVE_MAP.keys())}")
        actions.extend(MOVE_MAP[move])
    return actions