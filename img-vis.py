import numpy as np
import random
import ast
from PIL import Image
def show_image():
	file1 = open('file10.txt','r')
	for line1 in file1.readlines():
		print(line1)
		if len(line1)<10:
			continue
		line1=line1.rstrip()
		img_data = line1.split('#')
		img_data = img_data[1]
		
		data = eval(img_data)
		print('what')
		im = Image.fromarray(np.array(data, dtype=np.uint8))
		num1 = random.randint(0,1000)
		num2 = random.randint(0,1000)
		im.save('img'+str(num1)+str(num2)+'.png')


if __name__=='__main__':
	show_image()