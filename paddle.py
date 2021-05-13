import random
import config
from random import randint
import sys, time, os
from colorama import init, Fore, Back, Style

class Paddle():
	def __init__(self, obj):
		self.shape = ["A","B","C","D","E"]
		self.length = 5
		self._x = 30
		self._y = 38
		self.print_paddle(obj)

	def get_x(self):
		return self._x
	
	def get_y(self):
		return self._y
		
	def print_paddle(self, obj):
		# if(obj.Matrix[self.x][self.y] == " "):
		if(config.shooting_paddle is 0):
			for i in range(self.length):
				# obj.Matrix[self.x][i + self.y] = self.shape[i]
				obj.Matrix[self._x][i + self._y] = (config.colour5 + self.shape[i])
		else:
			for i in range(self.length):
				# obj.Matrix[self.x][i + self.y] = self.shape[i]
				obj.Matrix[self._x][i + self._y] = (config.shooting_paddle_color + self.shape[i])
	def motion(self, input, obj):
		if(input == 'q'):
			sys.exit(0)

		if((config.powerup_array[0] == 1) and (config.powerup_array[1] == 1)):
			self.clear(obj)
			self.shape = ["A","B","C","D","E"]
			self.length = 5
			self.print_paddle(obj)

		elif((config.powerup_array[0] == 1) and (config.powerup_array[1] == 0)):
			self.clear(obj)
			self.shape = ["A","B","C","D","E","F","G"]
			self.length = 7
			self.print_paddle(obj)

		elif((config.powerup_array[0] == 0) and (config.powerup_array[1] == 1)):
			self.clear(obj)
			self.shape = ["A","B","C"]
			self.length = 3
			self.print_paddle(obj)

		elif((config.powerup_array[0] == 0) and (config.powerup_array[1] == 0)):
			self.clear(obj)
			self.shape = ["A","B","C","D","E"]
			self.length = 5
			self.print_paddle(obj)

		if(input == 'd'):
			if(self._y < (73 - self.length)):
				self.clear(obj)
				self._y += 3
				self.print_paddle(obj)
				if(config.ball_release == 0):
					for ball in config.ball_mul:
						if(ball.on_paddle_grab == 1):  # locating which ball is on paddle
							ball.clear(obj)
							ball.x = self._x - 1
							ball.y += 3                # dont want ball to always start from centre of paddle
							ball.print_ball(obj, 0, 0)

		if(input == 'a'):
			if(self._y >= self.length):
				self.clear(obj)
				self._y -= 3
				self.print_paddle(obj)
				if(config.ball_release == 0):
					for ball in config.ball_mul:
						if(ball.on_paddle_grab == 1):  # locating which ball is on paddle
							ball.clear(obj)
							ball.x = self._x - 1
							ball.y -= 3                # dont want ball to always start from centre of paddle
							ball.print_ball(obj, 0, 0)

		if((input == 'w') and (config.shooting_paddle)):
			config.bullet_list.append(Bullet(obj, self._x, self._y, config.no_of_bullets))
			config.no_of_bullets += 1
			os.system('aplay -q ./sounds/shoot.wav&')
	def clear(self, obj):
		for i in range (self.length):
			obj.Matrix[self._x][i + self._y] = " "
			# obj.Matrix[self.x + 1][i + self.y] = " "

from bullet import *