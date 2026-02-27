"""
robot/motor.py
--------------
Low-level EV3 motor commands.

THIS FILE ONLY RUNS ON THE EV3 BRICK.
On a laptop, importing this will work but calling any function will raise
RuntimeError — by design, so you get a clear message instead of a cryptic
ev3dev import error.

When you're ready to run on the EV3:
  1. Install ev3dev: https://www.ev3dev.org/
  2. Uncomment the ev3dev imports below.
  3. Set the correct port names for your motor wiring.

Motor layout (adjust ports to match your build):
  OUTPUT_A → bottom layer turntable
  OUTPUT_B → tilt arm (tilts cube forward/back)
  OUTPUT_C → (optional) second tilt axis or scan arm
"""

_ON_EV3 = False  # flip to True once running on the brick

# ── Uncomment when on EV3 ─────────────────────────────────────────────────
# from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B
# from ev3dev2.motor import SpeedPercent, MoveSteering
# _turntable = LargeMotor(OUTPUT_A)
# _tilt      = LargeMotor(OUTPUT_B)
# _ON_EV3    = True


def _require_ev3():
    if not _ON_EV3:
        raise RuntimeError(
            "motor.py: Not running on EV3. "
            "This function only works on the physical robot."
        )


# ── Turntable (bottom layer) ───────────────────────────────────────────────

def turn_bottom_cw() -> None:
    """Rotate bottom layer 90° clockwise."""
    _require_ev3()
    # _turntable.on_for_degrees(SpeedPercent(30), 90)


def turn_bottom_ccw() -> None:
    """Rotate bottom layer 90° counter-clockwise."""
    _require_ev3()
    # _turntable.on_for_degrees(SpeedPercent(30), -90)


def turn_bottom_180() -> None:
    """Rotate bottom layer 180°."""
    _require_ev3()
    # _turntable.on_for_degrees(SpeedPercent(30), 180)


# ── Tilt arm (cube orientation) ───────────────────────────────────────────

def tilt_front() -> None:
    """Tilt cube forward: U→F, F→D, D→B, B→U."""
    _require_ev3()
    # _tilt.on_for_degrees(SpeedPercent(30), 90)


def tilt_back() -> None:
    """Tilt cube backward: U→B, B→D, D→F, F→U."""
    _require_ev3()
    # _tilt.on_for_degrees(SpeedPercent(30), -90)


def tilt_right() -> None:
    """Tilt cube right: U→R, R→D, D→L, L→U."""
    _require_ev3()
    # implement with your hardware's tilt mechanism


def tilt_left() -> None:
    """Tilt cube left: U→L, L→D, D→R, R→U."""
    _require_ev3()


def spin_cw() -> None:
    """Rotate whole cube clockwise viewed from top (U stays U)."""
    _require_ev3()


def spin_ccw() -> None:
    """Rotate whole cube counter-clockwise viewed from top."""
    _require_ev3()