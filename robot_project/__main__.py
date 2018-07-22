import sys
from robot_simulator import RobotSimulation
import filemapper as fm
from sys import stdin

# visual studio needed for windows.
# link - https://www.scivision.co/python-windows-visual-c++-14-required/


def main():
    """
        This file is the main method call. Execution starts from here.
        It accepts input data either correct or incorrect data.
        :return: Output of the data provided.
        :param: It accepts file directory,which contains input_data.txt file.
    """
    simulation = RobotSimulation()
    execute_directory = stdin.readline()
    if len(execute_directory)-1 == len("input_data"):
        correct_files = fm.load("input_data", "r")
        for correct_file in correct_files:
            print("\n")
            print("FIle executed from Input Directory - ", correct_file)
            for values in fm.read(correct_file):
                for line in values.split("\n"):
                    if len(line):
                        simulation.run(line)

    elif len(execute_directory)-1 == len("incorrect_data"):
        incorrect_files = fm.load("incorrect_data")
        for incorrect_file in incorrect_files:
            print("\n")
            print("FIle executed from Incorrect Directory - ", incorrect_file)
            for values in fm.read(incorrect_file):
                for line in values.split("\n"):
                    if len(line):
                        simulation.run(line)
    else:
        print("Please provide the exact directory")


if __name__ == "__main__":
    main()
