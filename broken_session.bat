REM @echo off
DEL /Q session_tempfile
:Loop
IF "%2"=="" GOTO Continue
ECHO file "%2" >> session_tempfile
SHIFT
GOTO Loop
:Continue
ffmpeg -safe 0 -f concat -i session_tempfile -c copy outfile.mp4
REM DEL /Q session_tempfile