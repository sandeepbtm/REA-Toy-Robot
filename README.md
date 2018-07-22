# REA-Toy-Robot

## Description 
  
  Object - To create a toy robot that can move withtin 5*5 dimension along with some conditions.

- The application is a simulation of a toy robot moving on a square tabletop,
  of dimensions 5 units x 5 units.
- There are no other obstructions on the table surface.
- The robot is free to roam around the surface of the table, but must be
  prevented from falling to destruction. Any movement that would result in the
  robot falling from the table must be prevented, however further valid
  movement commands must still be allowed.

Create an application that can read in commands of the following (textual) form:

    PLACE X,Y,F
    MOVE
    LEFT
    RIGHT
    REPORT

- PLACE will put the toy robot on the table in position X,Y and facing NORTH,
  SOUTH, EAST or WEST.
- The origin (0,0) can be considered to be the SOUTH WEST most corner.
- The first valid command to the robot is a PLACE command, after that, any
  sequence of commands may be issued, in any order, including another PLACE
  command. The application should discard all commands in the sequence until
  a valid PLACE command has been executed.
- MOVE will move the toy robot one unit forward in the direction it is
  currently facing.
- LEFT and RIGHT will rotate the robot 90 degrees in the specified direction
  without changing the position of the robot.
- REPORT will announce the X,Y and F of the robot. This can be in any form,
  but standard output is sufficient.

- A robot that is not on the table can choose the ignore the MOVE, LEFT, RIGHT
  and REPORT commands.
- Input can be from a file, or from standard input, as the developer chooses.
- Provide test data to exercise the application.
- The application must be a command line application.

  
### Developement Enviroment
  
   ```Windows-10, Python ==3.5, Visual Studio C++ 14, Pip3- build tool, IDE - Pycharm```
   
   To check your version for python and pip
   
   ``` python -V and pip -V```

# Database 
  There is no database for toy robot application
  
## Input/Test Data
  For test data, input_data folder has been provided along with incorrect_data folder for incorrect data.
  
# Dependency 
  
  Go to --> robot_project directory run following command.

  ```pip3 install -r dependency.txt ```

  This will download all the dependency required for the project.
  
## Project clone and run
  
### For running the project please clone or download the .zip using

  ```git clone repository```
  
  After clone install the dependency as mentioned above.
  
# Running Toy_Robot

    ``` python __main__.py```

    Please provide the directory name either input_data or incorrect_data using (stdin) command line parameter.

    It accepts input file with the valid parameter. Hence some testing files have been attached for reference within the input_data.
    

# Testing

    ``` python __main__.py directory_name```

    This accepts a directory where all the text files reside either incorrect or correct.

    If incorrect data provided it terminates the program with the exception raised.

    For eg.- ```python __main__.py input_data```  for correct data
             ```python __main__.py incorrect_data``` for incorrect data
    
## Conclusion
   
   After successfully running the application it will show the output as required which is provided into the input.txt files.
