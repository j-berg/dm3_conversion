#Author: Jordan Berg
#v1.0: 13 May 2017
#v1.1: 17 May 2017, more automation added

#This script automates the process of converting .dm3 files from TEM into 16-bit .tif files

import sys
import os

rootdir = sys.argv[1]

ij_dir = "." #Input ij.jar working directory path between quotes

macro_dir = "./macros" #Input process_TEM.ijm working directory path between quotes

os.system("cd " + rootdir)
os.system("mkdir " + rootdir + "/converted_files")

#Run ImageJ macro on each file in rootdir
for subdir, dirs, files in os.walk(rootdir):

    for x in files:

        if x[-4:] == ".dm3":
            name = x[:-4]
            os.system("java -jar " + ij_dir + "/ij.jar --headless -macro " + macro_dir + "/process_TEM.ijm " + rootdir + "/" + x + "#" + rootdir + "/converted_files/" + name + ".tif")

        else:
            pass

print("COMPLETE")
