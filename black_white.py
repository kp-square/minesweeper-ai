from screenshot import screenshot
import numpy as np
from PIL import Image
import time


def black_white_screenshot():
  time.sleep(3)
  a=screenshot()
  thresh =100;
  fn = lambda x : 255 if x > thresh else 0 
  img = a.convert('L').point(fn, mode='1')
  return img
	

  
if __name__=='__main__':
  black_white_screenshot()