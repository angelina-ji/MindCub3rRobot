"""
simulator/runner.py
"""
from cube.state   import apply_scramble, make_solved
from cube.display import print_cube
from robot.move_mapper import scramble_to_actions

def run_simulator():
    print("=" * 50)
    print("  MindCub3r Simulator")
    print("  Orientation: White top, Green front")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  [1] Enter scramble and show cube state")
        print("  [2] Enter scramble and show robot actions")
        print("  [3] Show solved cube")
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
                print("Robot actions (" + str(len(actions)) + " steps):")
                for i, action in enumerate(actions, 1):
                    print("  " + str(i) + ". " + action)
            except (ValueError, KeyError) as e:
                print("Error: " + str(e))
        elif choice == "3":
            print_cube(make_solved(), label="Solved cube:")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_simulator()
