#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
get_ipython().system('{sys.executable} -m pip install opencv-python')


# In[2]:


pip install cvzone


# In[3]:


pip install --user mediapipe


# In[4]:


import cv2


# In[5]:


# Hand detector-to detect our hands and to see if we have clicked on button or not
from cvzone.HandTrackingModule import HandDetector
class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN,
                    2, (50, 50, 50), 2)
    def checkClick(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and \
                self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, (self.pos[0] + 3, self.pos[1] + 3),
                          (self.pos[0] + self.width - 3, self.pos[1] + self.height - 3),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN,
                        5, (0, 0, 0), 5)
            return True
        else:
            return False

      
    


# In[6]:


# Adding webcam
cap = cv2.VideoCapture(0) #web cam no
cap.set(3,1280)# is used to set the width of the video capture object (cap) to 1280 pixels.
#property index 3 corresponds to the property CV_CAP_PROP_FRAME_WIDTH, which is used in older versions of OpenCV
cap.set(4,720)
#property index 4 corresponds to CV_CAP_PROP_FRAME_HEIGHT (or cv2.CAP_PROP_FRAME_HEIGHT in recent versions of OpenCV)
detector=HandDetector(detectionCon=0.8,maxHands=1) #if it is 80 per confident that it is hand than only it will detect hence detection confidence=0.8
#creating button
# Buttons
buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '/', '.', '=']]
buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x * 100 + 800
        ypos = y * 100 + 150

        buttonList.append(Button((xpos, ypos), 100, 100, buttonListValues[y][x]))
#variables
myEquation = ''
delayCounter = 0


# In[ ]:


#loop
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    # Draw All
    cv2.rectangle(img, (800, 50), (800 + 400, 70 + 100),
                  (225, 225, 225), cv2.FILLED)

    cv2.rectangle(img, (800, 50), (800 + 400, 70 + 100),
                  (50, 50, 50), 3)
    for button in buttonList:
        button.draw(img)
    if hands:
        lmList = hands[0]['lmList']
        length, _, img = detector.findDistance((lmList[8][0], lmList[8][1]), (lmList[12][0], lmList[12][1]), img)
        print(length)
        x, y = lmList[8][0], lmList[8][1]
        if length < 50 and delayCounter == 0:
            for i, button in enumerate(buttonList):
                if button.checkClick(x, y):
                    myValue = buttonListValues[int(i % 4)][int(i / 4)]  # get correct number
                    if myValue == '=':
                        myEquation = str(eval(myEquation))
                    else:
                        myEquation += myValue
                    delayCounter = 1
    # avoid delay counter
    # to avoid multiple clicks
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0
    cv2.putText(img, myEquation, (810, 130), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 0, 0), 3)

    key = cv2.waitKey(1)
    cv2.imshow("Image", img)
    if key == ord('c'):
        myEquation = ''








# In[ ]:







# In[ ]:




