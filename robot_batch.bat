@echo off

set "script_path=D:\PyCharm_Workspace\REA-Toy-Robot\robot_project\"
set "script_path=%script_path%__main__.py"

echo %script_path%

python %script_path% input_data %*