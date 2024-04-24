# https://www.w3resource.com/python-exercises/os/index.php

import os
import platform
from pathlib import Path
# print(os.name)  # name of os
# print(platform.uname()) # informatio of curr os
# print(os.getcwd()) # curr working dir
# print(os.listdir()) # list all dirs and files

# curr_dir_path = os.getcwd()

# for name in os.listdir():
#     if os.path.isdir(os.path.join(curr_dir_path,name)):
#         print('Folder name is: ',name)
#     else:
#         print('File name is: ',name)


# root = os.getcwd()
# for entry in os.scandir(root):
#    if entry.is_dir():
#        typ = 'dir'
#    elif entry.is_file():
#        typ = 'file'
#    elif entry.is_symlink():
#        typ = 'link'
#    else:
#        typ = 'unknown'
#    print('{name} {typ}'.format(
#        name=entry.name,
#        typ=typ,
#    ))

# print('Exist:', os.access('c:\\Users\\Public\\C programming library.docx', os.F_OK))
# print('Readable:', os.access('c:\\Users\\Public\\C programming library.docx', os.R_OK))
# print('Writable:', os.access('c:\\Users\\Public\\C programming library.docx', os.W_OK))
# print('Executable:', os.access('c:\\Users\\Public\\C programming library.docx', os.X_OK))

# os.stat(os.getcwd()) # all statistics

# Let us start by going through the documentation of execvp - os. execvp(file, args)These functions all execute a new program,
# replacing the current process; 
# they do not return. On Unix, the new executable is loaded into the current process, and will have the same process id as the caller
# program = "python"
# arguments = ["python.py"]
# print(os.execvp(program, (program,) + tuple(arguments)))
# print("Goodbye")

# execute an os command through python script
# command = ''
# if os.name == 'nt':
#     command = 'dir'
# else:
#     command = 'ls'

# os.system(command)

# import io
# # Write a string to a buffer
# output = io.StringIO()
# output.write('Python Exercises, Practice, Solution')
# # Retrieve the value written
# print(output.getvalue())
# # Discard buffer memory
# output.close()

# create, write and rename a file 

# with open('new.txt','w+') as file:
#     file.write('This is a new file created for test purposes.')

# srcPath = Path(Path.cwd()/'new.txt')
# destPath = Path(Path.cwd()/'new1.txt')

# os.rename(srcPath,destPath)

# print(os.getppid())
# print(os.pardir)

# environment variables 
# print(os.environ)
# print(os.environ['PATH'])

# check whether a path exists or not
# path = Path.cwd() / 'new1.txt'
# print(os.path.exists(path))
# print(path.exists())
# print(Path.exists(path))

# def double(n):
#     return n*2

# func = double

# print(isinstance(double,object))
# print(double == func)
