#!/usr/bin/env python3
from lib.actions import init, on, off, play, wait, waitForFace, volume, stop

init()
# Those are the outlet's URIs
# No trailing slashes!
A = 'http://delock-0077.local'
B = 'http://delock-2592.local'
# The number of the webcam, should be something between -1 and 2
WEBCAM = -1

# Actions

# play('song.mp3')
# Plays a file with the name song.mp3 located in the help folder.

# on(A)
# on(B)
# off(A)
# on(B)
# Turns outlet A or B on and off.

# waitForFace(WEBCAM)
# Pauses the programm until a face appers in the webcam.
# You can ignore the parameter 'WEBCAM' as long it is working.

# volume(1.0)
# Sets the volume of the audio output.
# Any number between 0.0 and 1.0 is allowed.

# stop()
# Stops the music!


# This will repeat the intended line forever.
# There must be 4 spaces before each command.
while True:
    play('A.mp3')
    on(A)
    waitForFace(WEBCAM)
    off(A)
    on(B)
    volume(1.0)
    play('B.wav')
    wait(10)
    off(B)
