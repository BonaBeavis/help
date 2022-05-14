import pygame
import cv2
import face_recognition

import os
import time
from pathlib import Path
from urllib.error import URLError, HTTPError
from urllib.request import urlopen


def log(message):
    print('----')
    print(message)


def waitForFace(webcam_number):
    '''
    Exit when a face is detected.
    '''
    log('Wait for face')
    video_capture = cv2.VideoCapture(webcam_number)
    # video_capture.set(cv2.CAP_PROP_EXPOSURE, 8000)
    face_locations = []

    while not face_locations:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(
            rgb_frame, model='hog')
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()


def play(file_name):
    script_path = Path(os.path.join(os.path.dirname(__file__)))
    absolute_file_path = Path.joinpath(script_path.parent, file_name)
    log('Play: ' + str(absolute_file_path))
    pygame.mixer.music.load(absolute_file_path)
    pygame.mixer.music.play()


def stop():
    log('Stop music')
    pygame.mixer.music.stop()


def wait(seconds):
    log('Wait for ' + str(seconds) + ' seconds')
    time.sleep(seconds)


def on(url):
    log('Turn on ' + url)
    switch_outlet(url + '/cm?cmnd=Power%20On')


def off(url):
    log('Turn off ' + url)
    switch_outlet(url + '/cm?cmnd=Power%20Off')


def switch_outlet(url):
    try:
        urlopen(url).read()
    except HTTPError as e:
        print('Error code: ', e.code)
    except URLError as e:
        print('Could reach the outlet!')
        print('Reason: ', e.reason)


def init():
    pygame.mixer.init()
