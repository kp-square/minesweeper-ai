from PIL import ImageGrab
import time
import pyautogui

def screenshot():
	pyautogui.keyDown('alt')
	pyautogui.press('prtscr')
	pyautogui.keyUp('alt')
	img = ImageGrab.grabclipboard()
	return img
	
if __name__=='__main__':
	screenshot()