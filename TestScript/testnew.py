#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     29-12-2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))

print("dir_path")
print(os.path.dirname(os.path.realpath(__file__)))

print("folder_path")
print(os.path.abspath(os.path.join(dir_path, os.pardir)))

print("Library_path")
print(sys.path.insert(0,dir_path))

#os.path.dirname(os.path.realpath(__file__))
#os.path.abspath(os.path.join(dir_path, os.pardir))
#sys.path.insert(0,folder_path+"\Library")