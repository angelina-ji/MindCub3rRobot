"""
robot/scanner.py
----------------
Reads cube sticker colours from the EV3 colour sensor and builds
a cube state string that can be loaded into PyCuber.

THIS FILE ONLY RUNS ON THE EV3 BRICK.
On a laptop, all functions raise RuntimeError.

Scanning order (standard for MindCub3r):
  The robot scans each face by tilting the cube into a fixed scan position.
  Faces are scanned in this order: U, R, F, D, L, B
  Each face is scanned row by row, left to right, top to bottom.

Output format:
  A 54-character string in the order: U R F D L B (9 stickers each)
  Letters: W Y G B R O
  Example solved: "WWWWWWWWW RRRRRRRRR GGGGGGGGG YYYYYYYYY OOOOOOOOO BBBBBBBBB"
"""

_ON_EV3 = False

# ── Uncomment when on EV3 ─────────────────────────────────────────────────
# from ev3dev2.sensor.lego import ColorSensor
# from ev3dev2.sensor import INPUT_1
# _colour_sensor = ColorSensor(INPUT_1)
# _ON_EV3 = True

# Maps EV3 colour sensor integer codes → single letters
# ev3dev2 ColorSensor.color returns an int 0-7:
#   0=no colour, 1=black, 2=blue, 3=green, 4=yellow, 5=red, 6=white, 7=brown
_EV3_COLOUR_CODE_MAP = {
    6: "W",  # white
    4: "Y",  # yellow
    3: "G",  # green
    2: "B",  # blue
    5: "R",  # red
    0: "O",  # orange (ev3dev may return 0 for orange; calibrate per your sensor)
}


def _require_ev3():
    if not _ON_EV3:
        raise RuntimeError(
            "scanner.py: Not running on EV3. "
            "Scanning only works on the physical robot."
        )


def read_sticker() -> str:
    """
    Read the current sticker under the sensor and return its letter.
    Robot must be positioned correctly before calling.
    """
    _require_ev3()
    # code = _colour_sensor.color
    # return _EV3_COLOUR_CODE_MAP.get(code, "?")


def scan_full_cube() -> str:
    """
    Scan all 54 stickers by tilting through all 6 faces.
    Returns a 54-character state string in U R F D L B order.

    Not yet implemented — will require motor.py tilt sequences.
    """
    raise NotImplementedError("Full cube scan not yet implemented")