#INITIAL SETUP
#----------------------------------------------------------------
import os
import random
import time
import numpy as np
import cv2
import matplotlib.pyplot as plt
from cvzone.HandTrackingModule import HandDetector
import mediapipe
from PIL import Image

# Addition of image
folderPath = 'frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]
intro = graphic[0];
kill = graphic[1];
winner = graphic[2];
sqr_img = Image.open(r'C:\Squid game\CookieCutter-main\img\sqr(2).png') # read img\sqr (1) in the sqr_img variable
mlsa =  Image.open(r'C:\Squid game\CookieCutter-main\img\mlsa.png') # read img\mlsa in the mlsa variable

#---------------------------------------------------------------------





#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------

#Making intro screen
cv2.imshow('Cookie cutter', cv2.resize(intro, (0,0), fx= 0.59, fy = 0.59))
cv2.waitKey(1)





#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED
while True:
     cv2.imshow('Cookie cutter', cv2.resize(intro,(0,0), fx=0.59, fy= 0.59))
     if cv2.waitKey(1) & 0xFF==ord('q'):
          break
#------------------------------------------------------------------------------------------------




#Setting up classes

#-------------------------------------------





gameOver = False
NotWon =True
#-------------------------------------------------------------------------------------------




#Setting up the timer
TIMER_MAX = 45
TIMER= TIMER_MAX
MaxMove = 650000000
#--------------------------------------------------------------------------------------------




#Capturing the hand
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector= HandDetector(detectionCon=0.2, maxHands=1)

while True:
     success, img = cap.read()
     img = cv2.flip(img, 1)
     hands, img= detector.findHands(img, flipType= False)


     #Square generator
     cv2.rectangle(img, (150,250), (800,800),(50,50,50), 3)
     #--------------------------------------------------------------------
     if hands:
          lmlist = hands[0]['lmList']
          pointIndex = lmlist[8][0:2]
          x, y ,z= lmlist[8]
          
          cv2.circle(img, pointIndex, 10, (100,0,100), cv2.FILLED)
          if x == 150 & y== 250:
            cv2.circle(img, pointIndex, 10, (0,110,0), cv2.FILLED)
     
     cv2.imshow("Image", img)
     cv2.waitKey(1)
     

     
          
     #----------------------------------------------------------




     
     


     

            


     
     
     









#GAME LOGIC UPTO THE TEAMS
#-----------------------------------------------------------------------------------------
while gameOver != True:
        HandCapture()
        continue
#LOSS SCREEN
if NotWon:
    for i in range(10):
       cv2.imshow('Cookie cutter', cv2.resize(kill, (0,0), fx=0.5,fy=0.5))
       #show the loss screen from the kill image read before
    while True:
         cv2.imshow('Cookie cutter', cv2.resize(kill, (0,0), fx=0.5,fy=0.5))
         cv2.waitKey(10) & 0xFF==ord('q')   
        #show the loss screen from the kill image read before and end it after we press q
#----------------------------------------------------------------------------------------------




#WIN SCREEN
else:
    cv2.imshow('Cookie cutter', cv2.resize(winner, (0,0), fx = 0.5, fy= 0.5))
    cv2.waitkey(125)

    while True:
        cv2.imshow('Cookie cutter', cv2.resize(winner, (0,0), fx = 0.5, fy= 0.5))
        if cv2.waitkey(10) & 0xFF==ord('q'):
             break
#show the win screen from the winner image read before
#--------------------------------------------------------------------------------------------------

#destroy all the windows
cv2.destroyAllWindows()
