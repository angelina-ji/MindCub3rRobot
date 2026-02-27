"""
main.py
-------
Entry point for the MindCub3r project.

Run this file on your laptop to start the simulator:
    python main.py

When running on the EV3:
    python main.py --robot
    (robot mode not yet implemented — will call motor.py directly)
"""

import sys

def main():
    if "--robot" in sys.argv:
        # Future: robot mode will go here
        print("Robot mode not yet implemented.")
        print("Connect the EV3 and implement robot/motor.py first.")
        sys.exit(1)
    else:
        # Default: run the laptop simulator
        from simulator.runner import run_simulator
        run_simulator()


if __name__ == "__main__":
    main()