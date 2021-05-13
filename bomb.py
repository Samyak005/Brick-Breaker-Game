import sys
from colorama import init, Fore, Back, Style
import config
import logging
from random import randint
import os

class Bomb():
	def __init__(self, obj, a, b):
		self.x = a
		self.y = b
		self.vx = 1
		self._shape = config.bomb_shape

	def __eq__(self, other):
		return self.x == other.x

	def bomb_collision_check(self, obj, pos_y):
		if(self.x > 30):
			# del(self)
			# del config.bullet_list[self.no]
			self.clear(obj)
			self.x = 4
			self.y = pos_y
			return
		if((obj.Matrix[self.x][self.y] == (config.colour5+"A")) or (obj.Matrix[self.x][self.y] == (config.shooting_paddle_color+"A"))):
			config.lives -= 1
			os.system('aplay -q ./sounds/lose_life.wav&')
			return
		if((obj.Matrix[self.x][self.y] == (config.colour5+"B")) or (obj.Matrix[self.x][self.y] == (config.shooting_paddle_color+"B"))):
			config.lives -= 1
			os.system('aplay -q ./sounds/lose_life.wav&')
			return
		if((obj.Matrix[self.x][self.y] == (config.colour5+"C")) or (obj.Matrix[self.x][self.y] == (config.shooting_paddle_color+"C"))):
			config.lives -= 1
			os.system('aplay -q ./sounds/lose_life.wav&')
			return
		if((obj.Matrix[self.x][self.y] == (config.colour5+"D")) or (obj.Matrix[self.x][self.y] == (config.shooting_paddle_color+"D"))):
			config.lives -= 1
			os.system('aplay -q ./sounds/lose_life.wav&')
			return

		if((obj.Matrix[self.x][self.y] == (config.colour5+"E")) or (obj.Matrix[self.x][self.y] == (config.shooting_paddle_color+"E"))):
			config.lives -= 1
			os.system('aplay -q ./sounds/lose_life.wav&')
			return

		if((obj.Matrix[self.x][self.y] == (config.colour5+"F")) or (obj.Matrix[self.x][self.y] == (config.shooting_paddle_color+"F"))):
			config.lives -= 1
			os.system('aplay -q ./sounds/lose_life.wav&')
			return

		if((obj.Matrix[self.x][self.y] == (config.colour5+"G")) or (obj.Matrix[self.x][self.y] == (config.shooting_paddle_color+"G"))):
			config.lives -= 1
			os.system('aplay -q ./sounds/lose_life.wav&')
			return

	def bomb_movement(self, obj): # first clear then move then show
		if(obj.Matrix[self.x][self.y] == (Fore.CYAN + self._shape)):
			self.clear(obj)
		
		self.x += self.vx
		
		if(obj.Matrix[self.x][self.y] == " "):
			obj.Matrix[self.x][self.y] = (Fore.CYAN + self._shape)

	def print_bomb(self, obj, a, b):
		obj.Matrix[self.x][self.y] = (Fore.CYAN + self._shape)
		# self.clear(obj)

	def clear(self, obj):
		obj.Matrix[self.x][self.y] = " "