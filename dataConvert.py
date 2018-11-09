box = [0.38720414201183434, 0.391025641025641, 0.0643491124260355, 0.046351084812623275]


import os
import sys
import cv2
import numpy as np
from PIL import Image

video_capture = cv2.VideoCapture('footage/GOPR2356.MP4')

w = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH )
h = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

c_x = box[0] * w
c_y = box[1] * h

ww = box[2]* w
hh = box[3]* h

x = abs(c_x - ww/2)
y = abs(c_y - hh/2)
xx = c_x + ww/2
yy = c_y + hh/2

i = 0
while(True):
	ret, frame = video_capture.read(i)
	i= i +1
	if i >= 200:
		break

cv2.rectangle(frame, (int(x), int(y)), (int(xx), int(yy)),(0,0,0), 2)

cv2.imshow('',frame)

cv2.imwrite( "test.jpg", frame );

# Press Q to stop!
while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
