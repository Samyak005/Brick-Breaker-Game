import random
import time
import sys
from random import randint
from colorama import init, Fore, Back, Style
import config
import math
import time

class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

# https://stackoverflow.com/questions/4109552/python-class-definition-syntax#:~:text=In%20Python%2C%20the%20preferred%20syntax,and%20use%20classes%20in%20Python.
# https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python 
# https://stackoverflow.com/questions/32362148/typeerror-type-object-is-not-iterable-iterating-over-object-instances/32362984#32362984
# class Person(object):
#     __metaclass__ = IterRegistry
#     _registry = []

#     def __init__(self, name):
#         self._registry.append(self)
#         self.name = name

class Powerup(metaclass = IterRegistry):
	_registry = []

	def __init__(self, obj, ball_vx, ball_vy):
		self._registry.append(self)
		self._speedx = 1 # was used initially when not dependent on ball's speed
		self._x = 0
		self._y = 0
		self._vx = ball_vx
		self._vy = ball_vy
		self._gravity_acceleration = 1
		self._no = 1
		self._shape =[" ", " "]
		self._start_time = time.time()
		self._end_time = self._start_time + 10
		
	def clear(self, obj):
		if( (obj.Matrix[self._x][self._y] == (config.colour4 + "e")) or (obj.Matrix[self._x][self._y] == (config.colour4 + "s"))
		or (obj.Matrix[self._x][self._y] == (config.colour4 + "m")) or (obj.Matrix[self._x][self._y] == (config.colour4 + "f"))
		or (obj.Matrix[self._x][self._y] == (config.colour4 + "t")) or (obj.Matrix[self._x][self._y] == (config.colour4 + "p"))):
			for i in range(0, 2):
				obj.Matrix[self._x][i + self._y] = " "

	def show(self, obj, obj1): # initial call when ball hits brick
		for i in range(0,2):
			obj.Matrix[self._x][i + self._y] = (config.colour4 + self._shape[i])
		self._x = obj1.x + 1
		self._y = obj1.y

	def move(self, obj):
		if(self._x > 30): # removed del(self) becz timeup implementation
			self.clear(obj)
			return 

		self.clear(obj)
		self._x += self._vx
		self._y += self._vy

		if(config.gravity == 1):
			self._vx += self._gravity_acceleration

		if(self._x > 30):
			self.clear(obj)
			return 

		if(self._x < 3):
			self._vx = (-1) * (self._vx)

		if(self._y < 3 or self._y > 72):
			self._vy = -1 * self._vy

		if(obj.Matrix[self._x][self._y] == " " and obj.Matrix[self._x][1 + self._y] == " "):
			for i in range(0,2):
				obj.Matrix[self._x][i + self._y] = (config.colour4 + self._shape[i])

		look_ahead_x = self._x + self._vx # look ahead only for paddle
		look_ahead_y = self._y + self._vy

		if((obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "A")) or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "B"))
		or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "C")) or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "D"))
		or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "E")) or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "F"))
		or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "G"))
		or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "A")) or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "B"))
		or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "C")) or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "D"))
		or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "E")) or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "F"))
		or (obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "G"))):
			os.system('aplay -q ./sounds/power_up.wav&')
			config.powerup_array[self._no - 1] = 1 
			if(self._no == 3):
				i = 0
				j = config.no_of_balls # initial number of balls before multiply
				for ball in config.ball_mul:
					ball.duplicate(obj)
					i += 1
					if(i==j):
						break

			elif(self._no == 4):
				for ball in config.ball_mul:
					if(ball.vy>0):
						ball.vy += 1
					elif(ball.vy<0):
						ball.vy -= 1
				
			elif(self._no == 5):
				for ball in config.ball_mul:
					ball.thru = 1
			
			elif(self._no == 6):
				config.ball_release = 0

			elif(self._no == 7):
				config.shooting_paddle = 1

			elif(self._no == 8):
				config.fireball = 1
class Powerup1(Powerup):
	def __init__(self, obj, ball_vx, ball_vy):
		super().__init__(obj, ball_vx, ball_vy)
		self._no = 1
		self._shape = ["e", "x"]

	def times_up(self, val, obj, obj1):
		if(val > self._end_time):
			config.powerup_array[self._no - 1] = 0
			# if(config.powerup_array[1] == 1): # check if shrink is on
			# 	obj1.clear(obj)
			# 	obj1.shape = ["A", "B", "C"]
			# 	obj1.length = 3
			# 	obj1.print_paddle(obj)
			# else:
			# 	obj1.clear(obj)
			# 	obj1.shape = ["A", "B", "C", "D", "E"]
			# 	obj1.length = 5
			# 	obj1.print_paddle(obj)

class Powerup2(Powerup):
	def __init__(self, obj, ball_vx, ball_vy):
		super().__init__(obj, ball_vx, ball_vy)
		self._no = 2
		self._shape = ["s", "h"]

	def times_up(self, val, obj, obj1):
		if(val > self._end_time):
			config.powerup_array[self._no - 1] = 0
			# if(config.powerup_array[0] == 1): # check if expand is on
			# 	obj1.clear(obj)
			# 	obj1.shape = ["A", "B", "C", "D", "E", "F", "G"]
			# 	obj1.length = 7
			# 	obj1.print_paddle(obj)
			# else:
			# 	obj1.clear(obj)
			# 	obj1.shape = ["A", "B", "C", "D", "E"]
			# 	obj1.length = 5
			# 	obj1.print_paddle(obj)

class Powerup3(Powerup):
	def __init__(self, obj, ball_vx, ball_vy):
		super().__init__(obj, ball_vx, ball_vy)
		self._no = 3
		self._shape = ["m", "u"]

	# no times up for multiplier
	def times_up(self, val, obj, obj1):
		pass

class Powerup4(Powerup):
	def __init__(self, obj, ball_vx, ball_vy):
		super().__init__(obj, ball_vx, ball_vy)
		self._no = 4
		self._shape = ["f", "a"]

	# no times up for fast ball
	def times_up(self, val, obj, obj1):
		pass

class Powerup5(Powerup):
	def __init__(self, obj, ball_vx, ball_vy):
		super().__init__(obj, ball_vx, ball_vy)
		self._no = 5
		self._shape = ["t", "h"]
	
	def times_up(self, val, obj, obj1):
		if(val > self._end_time):
			config.powerup_array[self._no - 1] = 0
			for ball in config.ball_mul:
				ball.thru = 0
				
class Powerup6(Powerup):
	def __init__(self, obj, ball_vx, ball_vy):
		super().__init__(obj, ball_vx, ball_vy)
		self._no = 6
		self._shape = ["p", "g"]

	def times_up(self, val, obj, obj1):
		if(val > self._end_time):
			config.powerup_array[self._no - 1] = 0
			config.ball_release = 1

class Powerup7(Powerup):
	def __init__(self, obj, ball_vx, ball_vy):
		super().__init__(obj, ball_vx, ball_vy)
		self._no = 7
		self._shape = ["s", "p"]

	def times_up(self, val, obj, obj1):
		if(val > self._end_time):
			config.powerup_array[self._no - 1] = 0
			config.shooting_paddle = 0

class Powerup8(Powerup):
	def __init__(self, obj, ball_vx, ball_vy):
		super().__init__(obj, ball_vx, ball_vy)
		self._no = 8
		self._shape = ["f", "b"]

	def times_up(self, val, obj, obj1):
		if(val > self._end_time):
			config.powerup_array[self._no - 1] = 0
			config.fireball = 0

from ball import *