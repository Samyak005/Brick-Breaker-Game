import random
import time
import sys
from random import randint
from colorama import init, Fore, Back, Style
import config

# x_coor_brick = [3 + (4*i) for i in range(0,17)]
# y_coor_brick = [i for i in range(3, 23)]
class Brick():
	def __init__(self, obj, a=-1, b=-1):

		self._strength = 3
		if(a!=-1): # checking whether values were passed or not
			self._x = a
			self._y = b
		else:
			self._x = ((random.randint(1,100000000) % 12) * 2) + 3 
			self._y = (random.randint(1,100000000) % 68) + 3
	
	def clear(self, obj):
		for i in range(-3,3):
			obj.Matrix[self._x][i + self._y] = " "

	def print_brick(self, obj):
		for i in range (4):
				obj.Matrix[self._x][i + self._y] = (config.colour6 + config.shape4[i])

	def dec_strength(self, obj):
		self._strength -= 1
		if(self._strength == 0):
			self.clear(obj) 

class Brick1(Brick):
	def __init__(self, obj):
		super().__init__(obj)
		self._strength = 1
		
	def print_brick(self, obj):
		for i in range (4):
			obj.Matrix[self._x][i + self._y] = (config.colour1 + config.shape1[i])

class Brick2(Brick):
	def __init__(self, obj):
		super().__init__(obj)
		self._strength = 2
	
	def print_brick(self, obj):
		for i in range (4):	
			obj.Matrix[self._x][i + self._y] = (config.colour2 + config.shape2[i])

class Unbreakable(Brick):
	def __init__(self, obj):
		super().__init__(obj)
		self._strength = -1
	
	def print_brick(self, obj):
		for i in range (4):
			obj.Matrix[self._x][i + self._y] = (config.colour3 + config.shape3[i])

class Super(Brick):
	def __init__(self, obj, a, b):
		super().__init__(obj)
		self._strength = -1
		self._x = a
		self._y = b