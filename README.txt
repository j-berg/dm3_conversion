Author: Jordan Berg
v1.0: 13 May 2017

The following scripts:

process_TEM.py
process_TEM.ijm

are for the purpose of converting Electron Microscopy images from 32-bit .dm3 files to 16-bit .tif files.

Instructions:

1. Download the "platform independent" java file for Image-J from the following website to the directory of your choice: https://imagej.nih.gov/ij/download.html

2. In Terminal, choose the directory where the zipped Image-J file is and type the following command (the file_name being the name of the Image-J file you just downloaded): unzip file_name.zip

3. Copy this script into the ImageJ directory

4. Copy the process_TEM.ijm script into the ImageJ/macros/ directory

5. Run the script in the ImageJ directory using the following command: python process_TEM.py

6. Follow the remaining steps listed within the process_TEM.py script