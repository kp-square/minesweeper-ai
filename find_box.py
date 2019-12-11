import numpy as np
from PIL import Image
from black_white import black_white_screenshot
import time
from screenshot import screenshot
	
	
class Box(object):
	def __init__(self, coordinate, corners, count=None, mine=None):
		self.coordinate=coordinate
		self.corners=corners
		self.count=count
		self.mine=mine

	def __str__(self):
		return str(self.coordinate) + ',' + str(count) + ',' + str(mine)


def func():
	img = black_white_screenshot()
	mat = np.array(img)
	rows,cols = mat.shape
	
	boxes = list()
	next_i = 0
	rows_t = rows - 100
	
	i=100
	j=0
	#Detect the boxes and save the coordinates of vertices
	while i < rows_t:
		box_row = list()
		
		while j < cols:
		
			if mat[i][j] == True:
				A = np.array([i,j])
				while mat[i][j]==True and i < rows_t:
					i=i+1
					
				i = i-1
				C=np.array([i,j])
				while mat[i][j]==True and j < cols:
					j = j + 1
					
				j=j-1
				D=np.array([i,j])
				while mat[i][j]==True and i > 0:
					i = i - 1
					
				i = i + 1
				B=np.array([i,j])
				while mat[i][j]==True and j < cols:
					j = j + 1
					
				temp=[A,C,B,D]
				point = (int(sum(i[0] for i in temp)/4.0), int(sum(i[1] for i in temp)/4.0))
				box_row.append(Box(tuple(point), temp))
				if len(box_row)==1:
					temp_A = C

			j += 1
		
		if len(box_row) > 0:
			i,j = temp_A
			i=i+1
		
			while mat[i][j]==False and i < rows_t:	
				i = i + 1

			i=i-1
			boxes.append(box_row)
		else:
			j=0
		
		i = i + 1
		
	return boxes
	# tot = 0
	# k=len(boxes)
	# i,j,k,c=0,0,0,1
	# img=np.array(screenshot())
	# for i in boxes:
		# for j in i:
			# saveImage(j, 16, img)
			# c += 1
		
		
	
if __name__=='__main__':
	func()