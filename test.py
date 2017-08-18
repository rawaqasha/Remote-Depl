#!/usr/bin/env python
import os
import sys
import subprocess
from contextlib import contextmanager

@contextmanager
def working_directory(newPath):
    owd = os.getcwd()
    try:
        print ("Hi")
        os.chdir(newPath)
        yield newPath
    finally:
        os.chdir(owd)

print ("First argument: %s" % str(sys.argv[1]))
repo= str(sys.argv[1])
#os.system("git clone "+str(sys.argv[1]))
newPath = os.path.expanduser(str(sys.argv[2]))
print (os.path.dirname(os.getcwd()+"/"+str(sys.argv[2])))
os.chdir("tasks") #os.path.dirname(os.getcwd()+"/"+sys.argv[2]))
os.path.dirname(sys.argv[2])
os.system(". "+os.getcwd()+"/"+"test.sh")

working_directory(newPath)




