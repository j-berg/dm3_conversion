#!/bin/bash

#Author: Jordan Berg
#v1.0: 17 May 2017

#INSTRUCTIONS:
#Instructions:
#Download the "platform independent" java file for Image-J from the following website to the directory of your choice: https://imagej.nih.gov/ij/download.html
#In Terminal, choose the directory where the zipped Image-J file is and type the following command (the file_name being the name of the Image-J file you just downloaded): unzip file_name.zip
#Place this script, the process_tem.py, and the process_tem.ijm files in the main ImageJ directory just unzipped
#Open Terminal, locate the folder this file is in, type "sh process_TEM.sh", execute, and follow prompts

#Save current directory to run ImageJ
export curr_dir=$(pwd)

#Make sure all file names have no spaces
echo "Input working directory for image files"
read image_dir
cd $image_dir
for f in *\ *; do mv "$f" "${f// /_}"; done

#Run python
cd $curr_dir
python process_TEM.py $image_dir
