import os
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

from labelClass import Label

def ssd():
	result_list = []
	return result_list

def open_data(file_name):

	image_List = []
	path = 'data/' + file_name

	if os.path.isdir(path):
		files= os.listdir(path)

		for f in files:
			## file_name,file_data
			image_List.append([f, cv2.imread(path + '/' + f)])

	elif os.path.isfile(path):
		## splite video to image

		return 0
	else:
		assert("path is neith a file or a dir\n")

	return image_List


def update(image,label_list):

	name = image[0]
	image = image[1]

	#label_list = []

	image_name_label = Label(image,[0,0],name)
	image_name_label.draw()

	label_list.append(image_name_label)


	## show image
	#newX,newY = int(image.shape[1]*image_scale), int(image.shape[0]*image_scale)
	#cv2.resize(image,(newX,newY))

	cv2.imshow(windows_name,image)
	#cv2.resizeWindow(windows_name, newX, newY);

	# plt.imshow(image[1])
	# plt.xticks([]), plt.yticks([])
	# plt.show()

	return image



def image_flow(image_List,label_dic,now_frame):

	img = image_List[now_frame]

	# if not label_dic.has_key(img[0]):
	# 	label_dic.fromkeys(img[0],[])

	label_dic.setdefault(img[0],[])
	print(label_dic.keys)
	update(img,label_dic.get(img[0]))


def mouseCallBack(event,x,y,flags,param):

	if event == cv2.EVENT_LBUTTONDOWN:
		print(x,y)

#########################################
video_name = '345'
frame_step = 1
frame = 0
windows_name = 'boxxs'
image_scale = 0.5
### raw image data, never change in array
image_List = open_data(video_name)	

## all the label, change with the update
label_dic = {}




### set windows
## can adjust the size of the window
cv2.namedWindow(windows_name,cv2.WINDOW_NORMAL)

### mouth event
cv2.setMouseCallback(windows_name,mouseCallBack)

## show first image
image_flow(image_List,label_dic, 0)


### keyboad event
while(1):
    k = chr(cv2.waitKey())

    if k == 'a':
    	frame += -frame_step
    	image_flow(image_List,label_dic,frame)

    elif k == 'd':
    	frame += frame_step
        image_flow(image_List,label_dic,frame)

    elif k == 'm':
        break

    elif k == 'l':
    	## hide all the label
        break
cv2.destroyAllWindows()


