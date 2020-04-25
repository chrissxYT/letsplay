#!/usr/bin/python3
from sys import argv
from subprocess import run

def readl(f):
	line = f.readline()
	if line == '':
		f.close()
		raise Exception('EOF')
	line = line.rstrip()
	if line == '':
		return readl(f)
	return line

f = open('{}.txt'.format(argv[1]), 'r')
infile = '{}.mp4'.format(argv[1])
timestart = '00:00:00'
while True:
	try:
		split = readl(f).split(' ')
	except:
		break
	timeend = split[0]
	outfile = '{}.mp4'.format(split[1])
	run(['ffmpeg', '-to', timeend,
		'-i', infile,
		'-ss', timestart,
		'-c:v', 'libx265',
		'-c:a', 'copy',
		'-r', '30', outfile])
	timestart = timeend
