"""
cube/solver.py
--------------
CFOP solver — not yet implemented.

CFOP stands for:
  Cross        → solve the white cross on the bottom
  F2L          → fill in the first two layers (4 corner-edge pairs)
  OLL          → orient all pieces on the top layer (57 cases)
  PLL          → permute all pieces on the top layer (21 cases)

This file will eventually contain:
  - solve_cross(cube)  → list of moves
  - solve_f2l(cube)    → list of moves
  - solve_oll(cube)    → list of moves
  - solve_pll(cube)    → list of moves
  - solve_full(cube)   → combined move list for all 4 phases

For now each function raises NotImplementedError so the rest of the
project can import and call them without breaking — you'll fill them
in one phase at a time.
"""

import pycuber as pc


def solve_cross(cube: pc.Cube) -> list[str]:
    """Return move list to solve the white cross."""
    raise NotImplementedError("Cross solver not yet implemented")


def solve_f2l(cube: pc.Cube) -> list[str]:
    """Return move list to solve the first two layers (after cross)."""
    raise NotImplementedError("F2L solver not yet implemented")


def solve_oll(cube: pc.Cube) -> list[str]:
    """Return move list to orient the last layer."""
    raise NotImplementedError("OLL solver not yet implemented")


def solve_pll(cube: pc.Cube) -> list[str]:
    """Return move list to permute the last layer."""
    raise NotImplementedError("PLL solver not yet implemented")


def solve_full(cube: pc.Cube) -> list[str]:
    """
    Return the full CFOP solution as a flat list of move strings.
    Runs all 4 phases in sequence on a copy of the cube.
    """
    raise NotImplementedError("Full CFOP solver not yet implemented")