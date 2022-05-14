#!/usr/bin/env python3

from lib.actions import init, on, off, play, wait, waitForFace, volume

init()
# Those are the outlet's URIs
A = 'http://delock-0077.local/'
B = 'http://delock-2592.local/'
# The number of the webcam, should be something between 0 and 2
WEBCAM = -1

# This will repeat the intended line forever.
# There must be 4 spaces before each command.
while True:
    play('A.mp3')  # Filenames must be in single quotes.
    on(A)
    waitForFace(WEBCAM)
    off(A)
    on(B)
    volume(1.0)  # Any number between 0.0 and 1.0.
    play('B.wav')
    wait(10)
    off(B)
