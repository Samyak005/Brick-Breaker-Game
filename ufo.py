import random
import config
from random import randint
import sys, time
from colorama import init, Fore, Back, Style

class UFO():
	def __init__(self, obj):
		self.shape = ["/","/","/","/","/"]
		self.length = 5
		self._x = 4
		self._y = 38
		# self.print_ufo(obj)
		self.bomb1 = Bomb(obj, 5, 34)

	def get_x(self):
		return self._x
	
	def get_y(self):
		return self._y
		
	def print_ufo(self, obj):
		# if(obj.Matrix[self.x][self.y] == " "):
			for i in range(self.length):
				# obj.Matrix[self.x][i + self.y] = self.shape[i]
				obj.Matrix[self._x][i + self._y] = (config.colour5 + self.shape[i])

	def motion(self, input, obj):

		self.bomb1.bomb_movement(obj)
		self.bomb1.bomb_collision_check(obj, self._y + 2)

		if(input == 'd'):
			if(self._y < (73 - self.length)):
				self.clear(obj)
				self._y += 3
				self.print_ufo(obj)

		if(input == 'a'):
			if(self._y >= self.length):
				self.clear(obj)
				self._y -= 3
				self.print_ufo(obj)

		if((config.ufo_health < 10) and (config.ufo_coverup>0)):
			config.ufo_coverup -= 1
			obj.ufo_defense()

	def clear(self, obj):
		for i in range (self.length):
			obj.Matrix[self._x][i + self._y] = " "
			# obj.Matrix[self.x + 1][i + self.y] = " "

	# def shoot(self):
from bomb import *
