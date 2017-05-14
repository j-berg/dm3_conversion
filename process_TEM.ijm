//Author: Jordan Berg
//v1.0: 13 May 2017

filelist = getArgument();
file = split(filelist,'#');

open(file[0]);
run("16-bit");
saveAs("Tiff", file[1]);
close();
run("Quit");
