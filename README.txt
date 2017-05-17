Author: Jordan Berg
v1.0: 13 May 2017
v1.1: 17 May 2017, automation added for greater ease in executing

dm3_conversion consists of the following scripts:

process_TEM.sh
process_TEM.py
process_TEM.ijm

for the purpose of converting Electron Microscopy images from 32-bit .dm3 files to 16-bit .tif files.

Instructions:

1. Download the "platform independent" java file for Image-J from the following website to the directory of your choice: https://imagej.nih.gov/ij/download.html

2. In Terminal, choose the directory where the zipped Image-J file is and type the following command (the file_name being the name of the Image-J file you just downloaded): unzip file_name.zip

3. Copy these scripts into the ImageJ parent directory that was just unzipped

4. In Terminal, go to the ImageJ parent directory and run the scripts using the following command: sh process_TEM.sh

5. Follow the prompts that appear in the Terminal window
