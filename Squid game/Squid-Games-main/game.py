import os
import random
import time
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import mediapipe

folderpath='frames'
mylist = os.listdir(folderpath)
graphic = [cv.imread(f'(folderpath)/(impath)') for impath in mylist ]
green = graphic[0]
red = graphic[1]
dead = graphic[2]
winner = graphic[3]
intro = graphic[4]

cv.imshow('Squid game', cv.resize(intro,(0,0), fx=0.69, fy=0.69))
cv.waitkey(1)
while True:
    cv.imshow('Squid game', cv.resize(intro,(0,0), fx=0.69, fy=0.69))
    if cv.waitkey(1) & 0xFF==ord('a'):
        break
TIMER_MAX = 45
TIMER= TIMER_MAX
maxMove = 7
font = cv.FONT_HERSHEY_COMPLEX_SMALL
cap = cv.VideoCapture(0)
frameHeight = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
frameWidth = cap.get(cv.CAP_PROP_FRAME_WIDTH)

win = False

prev = time.time()
prevDoll = prev
showFrame = cv.resize(green, (0,0), fx = 0.69, fy = 0.69)
isgreen = True

while cap.isOpened() and TIMER >= 0:
    if isgreen and (cv.waitkey(10) & 0xFF==ord('w')):
        win = True
        break

    ret, frame = cap.read()

    cv.putText(showFrame, str(TIMER), (50,50), font 1, (0, int(255*(TIMER)/TIMER_MAX)), 4, cv.LINE_AA)
    
    cur = time.time()
    
    no = random.randint(3,8)
    if cur-prev >= no:
        prev = cur
        TIMER = TIMER - no
        if cv.waitkey(10) & 0xFF==ord('w'):
            win = True
            break
        if isgreen:
            showFrame= cv.resize(red, (0,0),fx = 0.69, fy = 0.69)
            isgreen = False
            ref= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        else:
            showFrame= cv.resize(green, (0,0), fx = 0.69, fy = 0.69)
            isgreen= True
    if not isgreen:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frameDelta = cv.absdiff(ref.gray)
        thresh = cv.threshold(frameDelta, 20, 255, cv.THRESH_BINARY)[1]
        change = np.sum(thresh)



