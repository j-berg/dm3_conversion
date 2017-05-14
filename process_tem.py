#Author: Jordan Berg
#v1.0: 13 May 2017

#This script automates the process of converting .dm3 files from TEM into 16-bit .tif files

#Instructions:
#Download the "platform independent" java file for Image-J from the following website to the directory of your choice: https://imagej.nih.gov/ij/download.html
#In Terminal, choose the directory where the zipped Image-J file is and type the following command (the file_name being the name of the Image-J file you just downloaded): unzip file_name.zip
#Copy this script into the ImageJ directory
#Copy the process_TEM.ijm script into the ImageJ/macros/ directory
#Run the script in the ImageJ directory using the following command: python process_TEM.py
#Open a new tab in Terminal
#Using Terminal, local the directory that contains the .dm3 files you want to process and type the following command: pwd
#Copy the output from the previous command and paste it in for the first input in the running python script (process_TEM.py)
#Using Terminal, local the directory that contains the ij.jar file (should be under ImageJ/ImageJ.app/Contents/Java/) and type the following command: pwd
#Copy the output from the previous command and paste it in for the second input in the running python script (process_TEM.py)
#Using Terminal, local the directory that contains the .ijm macro you previously worked with (should be under ImageJ/macros/) and type the following command: pwd
#Copy the output from the previous command and paste it in for the third input in the running python script (process_TEM.py)

#Alternatively to following the previous six steps, you can delete the lines of code in this script followed by "###", uncomment the code on line 45 and delete line 44. In the code you just uncommented, you would fill in the specifics for the file locations.

#File names cannot have spaces, be sure to use underscores in place of spaces

import sys
import os

rootdir = input("Input directory containing the .dm3 files of interest.\n-------------------------------------------\n")
print("-------------------------------------------\n")

ij_dir = input("Input directory containing the ij.jar file.\n-------------------------------------------\n") ###
print("-------------------------------------------\n") ###

macro_dir = input("Input directory containing the macro.\n-------------------------------------------\n") ###
print("-------------------------------------------\n") ###

os.system("cd " + rootdir)
os.system("mkdir " + rootdir + "/converted_files")

for subdir, dirs, files in os.walk(rootdir):

    for x in files:

        if x[-4:] == ".dm3":
            name = x[:-4]
            os.system("java -jar " + ij_dir + "/ij.jar --headless -macro " + macro_dir + "/process_TEM.ijm " + rootdir + "/" + x + "#" + rootdir + "/converted_files/" + name + ".tif")
            #os.system("java -jar /Users/User_name/Desktop_or_directories_upstream_of_ImageJ/ImageJ/ImageJ.app/Contents/Java/ij.jar --headless -macro /Users/User_name/Desktop_or_directories_upstream_of_ImageJ/ImageJ/macros/process_TEM.ijm " + rootdir + "/" + x + "#" + rootdir + "/converted_files/" + name + ".tif")

        else:
            pass
