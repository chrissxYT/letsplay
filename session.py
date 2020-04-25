#!/usr/bin/python3
from sys import argv
from subprocess import run
from os import remove

listfilehandle = open('tmpsession', 'w')
output = argv[1]
for i in range(2, len(argv)):
	listfilehandle.write("file '{}'\n".format(argv[i]))
listfilehandle.close()
run(['ffmpeg', '-safe', '0', '-f', 'concat', '-i', 'tmpsession',
	 '-crf', '5', '-b:a', '320k', '-filter:v', 'scale=2560:1440', '-r', '30', output])
remove('tmpsession')
