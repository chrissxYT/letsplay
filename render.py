#!/usr/bin/env python3
from subprocess import run
from sys import argv

with open('%s.txt' % argv[1], 'r') as f:
    lines = [l for L in f.readlines() if (l := L.strip()) != '']

infile = '%s.mp4' % argv[1]
timestart = lines[0]
for l in lines[1:]:
    outfile = '%s_%s-%s.mp4' % (argv[1], timestart, l)
    run(['ffmpeg', '-to', l,
        '-i', infile,
        '-ss', timestart,
        '-ac', '1',
        '-c:v', 'libx265',
        '-c:a', 'aac',
        '-b:a', '128k',
        '-crf', '26',
        outfile])
    timestart = l
