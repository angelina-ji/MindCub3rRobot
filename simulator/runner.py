"""
simulator/runner.py
-------------------
Laptop-side simulation runner.
Ties together:
  cube/state.py    → apply scramble, read face grids
  cube/display.py  → print csTimer-style layout
  robot/move_mapper.py → show what physical actions the robot would take
"""

# Import your custom engine functions
from cube.state   import apply_scramble, make_solved
from cube.display import print_cube
from robot.move_mapper import scramble_to_actions

def run_simulator() -> None:
    """
    Main simulator loop.
    Prompts for a scramble, shows the resulting cube state,
    and optionally shows the robot action sequence.
    """
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
            scramble = input("Scramble (e.g. U F' D2 R L): ").strip()
            try:
                # Uses your WCA-correct engine
                cube = apply_scramble(scramble)
                label = f"After: {scramble}" if scramble else "Solved cube"
                print_cube(cube, label=label)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            scramble = input("Scramble (e.g. U F' D2 R L): ").strip()
            try:
                cube = apply_scramble(scramble)
                print_cube(cube, label=f"After: {scramble}")
                
                # Maps the scramble to physical motor movements
                actions = scramble_to_actions(scramble)
                print(f"Robot actions ({len(actions)} steps):")
                for i, action in enumerate(actions, 1):
                    print(f"  {i:3}. {action}")
                print()
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")

        elif choice == "3":
            # FIXED: Uses your engine's solved state instead of PyCuber
            print_cube(make_solved(), label="Solved cube:")

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_simulator()