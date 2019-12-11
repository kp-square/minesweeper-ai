import numpy as np
import tensorflow as tf
import math
import pyautogui

def get_value(btn, pix_size, img, new_model, my_file):
	point = (btn.i,btn.j)
	#pyautogui.click(point.coordinate[::-1], button='right')

	corners = btn.corners

	img_box = list()
	top_left=[i - math.floor(pix_size/2) for i in point]
	avr = lambda rgb:int(sum(rgb)/3)
	rgb_avr = tuple(np.zeros(3, dtype=np.uint16))
	count = 0
	for i in range(0,pix_size,1):
		img_box_row=list()
		for j in range(0,pix_size,1):
			rgb = img[top_left[0] + i][top_left[1] + j]
			if 100 < sum(rgb) < 600:
				rgb_avr = tuple(sum(x) for x in zip(rgb, rgb_avr))
				count += 1
	if count==0:
		return 0
	elif count > (pix_size**2 - pix_size) and (rgb_avr[2]/count) > 150:
		return -1  			
	else:
		
		test1=np.array(rgb_avr)/(count*255)
		test2=np.array([1,1,1])
		test = np.array([test1,test2])
		# my_file.write(str(test1))

		# when using tf replace test1 by test
		prediction = new_model.predict(list(test1))
		val= np.argmax(prediction)
		
		if val==0: val = 9
		temp=val
		if val==6:
			temp=2
		if val==7:
			temp=1
		my_file.write(str(temp))
		print(val)
		bw = lambda rgb : 255 if rgb > 180 else 0

		A,C,B,D = corners
		width_ = B[1] - A[1]
		height_ = C[0] - A[0]
		w_ = width_ -4
		h_ = height_ -4
		top_left = [A[0]+2 , A[1]+2]
		img_=[]
		for i in range(h_):
			row=[]
			for j in range(w_):
				rgb = img[top_left[0] + i][top_left[1] + j]
				row.append(avr(rgb))
			img_.append(row)
		my_file.write('#'+str(img_)+'\n')
		#A----B
		#
		#C----D
		return val
	
	