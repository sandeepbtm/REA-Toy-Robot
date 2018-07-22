import sys
from robot_project.robot_simulator import RobotSimulation
import filemapper as fm

# visual studio needed for windows.
# link - https://www.scivision.co/python-windows-visual-c++-14-required/
#values = open("input_data/input-1.txt","r").read()

def main():
    """
        This file is the main method call. Execution starts from here.
        It accepts input data either correct or incorrect data.
        :return: Output of the data provided.
        :param: It accepts file directory,which contains input_data.txt file.
    """
    simulation = RobotSimulation()
    # correct_files = fm.load("input_data","r")
    # for correct_file in correct_files:
    #     print("\n")
    #     print("FIle executed - ", correct_file)
    #     for values in fm.read(correct_file):
    #         for line in values.split("\n"):
    #             if len(line):
    #                 simulation.run(line)

    incorrect_files = fm.load("incorrect_data")
    for incorrect_file in incorrect_files:
        print("\n")
        print("FIle executed - ", incorrect_file)
        for values in fm.read(incorrect_file):
            for line in values.split("\n"):
                if len(line):
                    simulation.run(line)

if __name__ == "__main__":
    main()
