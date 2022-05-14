from lib.actions import init, on, off, play, wait, waitForFace

init()
# Those are the outlet's URIs
A = 'http://delock-0077.local/'
B = 'http://delock-2592.local/'
# The number of the webcam, should be something between 0 and 2
WEBCAM = -1

# This will repeat the intended line forever.
while True:
    # There must be 4 spaces before each command.
    # Filenames must be in single quotes.
    play('A.mp3')
    on(A)
    waitForFace(WEBCAM)
    off(A)
    on(B)
    play('B.wav')
    wait(3)
    off(B)
