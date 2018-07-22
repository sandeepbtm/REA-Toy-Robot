import sys
from robot_project.robot_simulator import RobotSimulation

# visual studio needed for windows.
# link - https://www.scivision.co/python-windows-visual-c++-14-required/


def main():

    simulation = RobotSimulation()
    values = open("input_data/input-1.txt","r").read()
    for line in values.split("\n"):
        if len(line):
            simulation.run(line)
        else:
            print("Please give the input. Do not keep it empty.")

if __name__ == "__main__":
    main()