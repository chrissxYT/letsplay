ffmpeg -i %1 -crf 5 -b:a 320k -filter:v scale=2560:1440 -r 30 %1.mp4