import itertools
import random
import numpy as np
##import tensorflow as tf
from screenshot import screenshot
import pyautogui
import find_box
from save_image import get_value
from minesweeper_csp import csp_model
from propagators import *
from cspbase import *
import time
import sys
from nnpredict import Model 
class Button:
	def __init__(self,box,i,j):
		self.x=i
		self.y=j
		self.i,self.j=box.coordinate
		self.corners = box.corners
		self.is_visible = False
		self.is_flagged = False
		self.value = None


	def set_value(self, val):
		if val== -1:
			pass
		elif val==9:
			# self.is_flagged=True
			# self.is_mine=True
			# self.is_visible=True
			self.value = -1
		else:
			
			self.value = val
			if self.value==6:
				self.value=2
			if self.value==7:
				self.value=1
			self.is_visible=True
			
		

	def is_flag(self):
		return self.is_flagged

	def flag(self):
		self.is_flagged, self.is_mine = True,True

	def is_show(self):
		return self.is_visible

	def lclick(self):
		if self.is_show():
			return
		self.is_visible = True
		pyautogui.click((self.j,self.i),button='left')

	def rclick(self):
		if self.is_show():
			return
		self.is_flagged=True
		pyautogui.click((self.j,self.i),button='right')

class Minesweeper:
	def __init__(self,mine_model):

		self.row_size=int()
		self.col_size=int()
		self.board=list() #all indices
		#board[row][col] = button
		self.buttons=list() #all box coordinates
		self.remaining_mines = int(sys.argv[1])
		self.initialize(mine_model)

	def initialize(self,mine_model):
		self.row_size = len(mine_model)
		self.col_size = len(mine_model[0])
		i=0
		for row in mine_model:
			j=0
			board_row=[]
			for col in row:
				btn = Button(col, i, j)
				self.buttons.append(btn)
				board_row.append(btn)
				j+=1
			self.board.append(board_row)
			i+=1


	def get_surrounding_buttons(self,btn):
		sur_btns=[]
		x_i, y_i = btn.x, btn.y
		scope=itertools.product([-1,0,1],[-1,0,1])
		for foo in scope:
			if foo != (0,0):
				temp_x = x_i + foo[0]
				temp_y = y_i + foo[1]
				if (0 <= temp_x < self.row_size and 0 <= temp_y < self.col_size):
					sur_btns.append(self.board[temp_x][temp_y])

		return sur_btns


	def update_minesweeper(self):
		img = np.array(screenshot())
		my_file = open('file10.txt','w+')
		##new_model = tf.keras.models.load_model('mines.model')
		new_model = Model('model2')
		for k in range(len(self.buttons)):
			btn=self.buttons[k]
			val = get_value(btn, 8, img, new_model, my_file)
			my_file.flush()
			self.buttons[k].set_value(val)


	def is_over(self):
		print(self.remaining_mines)
		if self.remaining_mines < 2:
			

			return True
		return False


def solve_complete(minesweeper_):
	'''Solve current game completely.
	'''
	if minesweeper_.is_over():
		
		return
	# # Unflag all buttons.
	# for button in minesweeper_.buttons:
	#     if button.is_flag():
	# 	    button.flag()
	# 	    self.flags -= 1
	count = 0
	while not minesweeper_.is_over():
		count += 1
		assigned = solve_step(minesweeper_)
		# No variable assigned by CSP.
		if not assigned:
			choose_button = guess_move(minesweeper_)
			choose_button.lclick()
		minesweeper_.update_minesweeper()
		if count == 100:
			
			return


def guess_move(minesweeper_):
	unclicked=[]
	for i in range(len(minesweeper_.buttons)):
		if not minesweeper_.buttons[i].is_show() and not minesweeper_.buttons[i].is_flag():
			unclicked.append(minesweeper_.buttons[i])
	return random.choice(unclicked)



def solve_step(minesweeper_):
	my_model = csp_model(minesweeper_)
	is_assigned = False
	

	solver = BT(my_model)
	solver.bt_search_MS(prop_GAC)
	

	for var in my_model.get_all_vars():

		try:
			cell = var.name.split()
			row = int(cell[0])
			col = int(cell[1])
		except:
		    # continue if it's not a vriable in board.
		    # in board variable name's format: row, col
			continue

		if var.get_assigned_value() == 1:
			if not minesweeper_.board[row][col].is_flag():
				time.sleep(0.1)
				minesweeper_.board[row][col].rclick()
				minesweeper_.remaining_mines -= 1
				is_assigned = True
				

		elif var.get_assigned_value() == 0:
			if not minesweeper_.board[row][col].is_show():
				if minesweeper_.remaining_mines > 1:
					time.sleep(0.1)
					minesweeper_.board[row][col].lclick()
					is_assigned = True
	return is_assigned


def ai():
	mine_model = find_box.func()
	minesweeper_ = Minesweeper(mine_model)
	#my_model = csp_model(minesweeper_)
	solve_complete(minesweeper_)


if __name__=='__main__':
	ai()
