"""
simulator/runner.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cube.state        import apply_scramble, make_solved
from cube.display      import print_cube
from robot.move_mapper import scramble_to_actions
from robot.orientation import execute_scramble

def _print_actions(actions):
    for i, action in enumerate(actions, 1):
        print("  " + str(i) + ". " + action)

def run_simulator():
    print("=" * 50)
    print("  MindCub3r Simulator")
    print("  Orientation: White top, Green front")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  [1] Enter scramble and show cube state")
        print("  [2] Enter scramble and show robot actions (naive)")
        print("  [3] Enter scramble and show robot actions (orientation-aware)")
        print("  [4] Enter scramble and compare naive vs orientation-aware")
        print("  [5] Show solved cube")
        print("  [q] Quit")

        choice = input("\nChoice: ").strip().lower()

        if choice == "q":
            print("Bye!")
            break
        elif choice == "1":
            scramble = input("Scramble: ").strip()
            try:
                cube = apply_scramble(scramble)
                label = "After: " + scramble if scramble else "Solved cube"
                print_cube(cube, label=label)
            except ValueError as e:
                print("Error: " + str(e))
        elif choice == "2":
            scramble = input("Scramble: ").strip()
            try:
                cube = apply_scramble(scramble)
                print_cube(cube, label="After: " + scramble)
                actions = scramble_to_actions(scramble)
                print("Naive actions (" + str(len(actions)) + " steps):")
                _print_actions(actions)
            except (ValueError, KeyError) as e:
                print("Error: " + str(e))
        elif choice == "3":
            scramble = input("Scramble: ").strip()
            try:
                cube = apply_scramble(scramble)
                print_cube(cube, label="After: " + scramble)
                actions = execute_scramble(scramble)
                print("Orientation-aware actions (" + str(len(actions)) + " steps):")
                _print_actions(actions)
            except (ValueError, KeyError) as e:
                print("Error: " + str(e))
        elif choice == "4":
            scramble = input("Scramble: ").strip()
            try:
                naive   = scramble_to_actions(scramble)
                efficient = execute_scramble(scramble)
                moves = scramble.strip().split()
                print("\n  Scramble : " + scramble)
                print("  Moves    : " + str(len(moves)))
                print("  Naive    : " + str(len(naive)) + " actions")
                print("  Efficient: " + str(len(efficient)) + " actions")
                print("  Saved    : " + str(len(naive) - len(efficient)) + " actions")
                print("\n--- Naive ---")
                _print_actions(naive)
                print("\n--- Orientation-aware ---")
                _print_actions(efficient)
            except (ValueError, KeyError) as e:
                print("Error: " + str(e))
        elif choice == "5":
            print_cube(make_solved(), label="Solved cube:")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_simulator()
