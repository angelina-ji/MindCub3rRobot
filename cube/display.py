"""
cube/display.py
---------------
Prints a cube state in csTimer-style layout:

         U U U
         U U U
         U U U

 L L L   F F F   R R R   B B B
 L L L   F F F   R R R   B B B
 L L L   F F F   R R R   B B B

         D D D
         D D D
         D D D

Orientation: White=U (top), Yellow=D (bottom), Green=F (front),
             Blue=B (back), Orange=L (left), Red=R (right).
Matches csTimer default.
"""

from cube.state import CubeState, make_solved

_INDENT     = "        "   # 8 spaces — aligns top/bottom under F face
_MIDDLE_PAD = " "          # shifts middle strip 1 space right
_GAP        = "  "         # gap between faces in middle row


def print_cube(state: CubeState, label: str = "") -> None:
    """
    Print all 54 stickers in csTimer cross layout.

    Args:
        state: A CubeState dict from cube/state.py.
        label: Optional heading printed above the cube.
    """
    U = state["U"]; D = state["D"]
    F = state["F"]; B = state["B"]
    L = state["L"]; R = state["R"]

    if label:
        print("\n" + str(label))

    # ── Top face ───────────────────────────────────────────────
    print()
    for row in U:
        print(_INDENT + " ".join(row))
    print()

    # ── Middle strip: L  F  R  B ──────────────────────────────
    for i in range(3):
        print(
            _MIDDLE_PAD +
            " ".join(L[i]) + _GAP +
            " ".join(F[i]) + _GAP +
            " ".join(R[i]) + _GAP +
            " ".join(B[i])
        )

    # ── Bottom face ────────────────────────────────────────────
    print()
    for row in D:
        print(_INDENT + " ".join(row))
    print()


def print_solved() -> None:
    """Convenience: print a fresh solved cube."""
    print_cube(make_solved(), label="Solved cube:")