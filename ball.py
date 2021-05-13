import sys
from colorama import init, Fore, Back, Style
import config
import logging
from random import randint
import os
logging.basicConfig(filename='logname',
					filemode='a',
					format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
					datefmt='%H:%M:%S',
					level=logging.DEBUG)
def yay():
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " __     __                             _ ".center(40))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " \ \   / /                            | |".center(40))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "  \ \_/ /_ _  __ _  __ _  __ _ _   _  | |".center(40))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "   \   / _` |/ _` |/ _` |/ _` | | | | | |".center(40))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "    | | (_| | (_| | (_| | (_| | |_| | |_|".center(40))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "    |_|\__,_|\__,_|\__,_|\__,_|\__, | (_)".center(40)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                __/ |    ".center(40)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                               |___/     ".center(40)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                         ".center(40)+Style.RESET_ALL)
objs = list()

# class IterRegistry2(type):
#     def __iter__(cls):
#         return iter(cls._registry2)

class Ball():#(metaclass = IterRegistry2):
	# _registry2 = []

	def __init__(self, obj, a=29, b=40):
		# self._registry2.append(self)
		self.x = a
		self.y = b
		self.vx = -1
		self.vy = 1
		self._shape = "@"
		self.thru = 0
		self.on_paddle_grab = 1 # initially 1 as ball is on paddle at beginning of game

	def __eq__(self, other):
		return self.x == other.x

	def dfs(self, obj, a, b):
		if(a<2 or b<2 or b>73):
			return

		if(obj.Matrix2[a][b]==1):
			return

		if((obj.Matrix[a][b]==(Fore.RED + "X")) or (obj.Matrix[a][b]==(Fore.RED + "Y"))):
			logging.warning("reached red area dont do dfs")
			return 
		
		obj.Matrix2[a][b] = 1
		if((obj.Matrix[a][b] == (config.colour1 + "<")) or (obj.Matrix[a][b] == (config.colour2 + "[")) or 
		(obj.Matrix[a][b] == (config.colour3 + "{")) or (obj.Matrix[a][b] == (config.colour6 + "("))):
			obj.Matrix[a][b] = " "
			# for i in range(0,4):
			# 	obj.Matrix[a][i+b] = " "

		elif((obj.Matrix[a][b] == (config.colour1 + "%")) or (obj.Matrix[a][b] == (config.colour2 + "%")) or 
		(obj.Matrix[a][b] == (config.colour3 + "%")) or (obj.Matrix[a][b] == (config.colour6 + "%"))):
			obj.Matrix[a][b] = " "
			# for i in range(-1,3):
			# 	obj.Matrix[a][i+b] = " "

		elif((obj.Matrix[a][b] == (config.colour1 + "$")) or (obj.Matrix[a][b] == (config.colour2 + "$")) or 
		(obj.Matrix[a][b] == (config.colour3 + "$")) or (obj.Matrix[a][b] == (config.colour6 + "$"))):
			obj.Matrix[a][b] = " "
			# for i in range(-2,2):
			# 	obj.Matrix[a][i+b] = " "

		elif((obj.Matrix[a][b] == (config.colour1 + ">")) or (obj.Matrix[a][b] == (config.colour2 + "]")) or 
		(obj.Matrix[a][b] == (config.colour3 + "}")) or (obj.Matrix[a][b] == (config.colour6 + ")"))):
			obj.Matrix[a][b] = " "
			# for i in range(-3,1):
			# 	obj.Matrix[a][i+b] = " "

		if(obj.Matrix[a+1][b+1]!=" "):
			self.dfs(obj, a+1, b+1)
		if(obj.Matrix[a][b+1]!=" "):
			self.dfs(obj, a, b+1)
		if(obj.Matrix[a+1][b]!=" "):
			self.dfs(obj, a+1, b)
		if(obj.Matrix[a-1][b]!=" "):
			self.dfs(obj, a-1, b)
		if(obj.Matrix[a][b-1]!=" "):
			self.dfs(obj, a, b-1)
		if(obj.Matrix[a+1][b-1]!=" "):
			self.dfs(obj, a+1, b-1)
		if(obj.Matrix[a-1][b+1]!=" "):
			self.dfs(obj, a-1, b+1)
		if(obj.Matrix[a-1][b-1]!=" "):
			self.dfs(obj, a-1, b-1)
		return 

	def check_fireball(self, obj):
		if config.fireball is 1:
			self.dfs(obj, self.x, self.y)

	def ball_collision_check(self, obj, obj1, obj2):
		if(self.x < 3):
			self.vx = (-1) * (self.vx)

		if(self.y < 3 or self.y > 72):
			self.vy = -1 * self.vy

		if(self.x > 30):
			logging.info('initial balls before reduction %d ', config.no_of_balls)
			logging.debug("ball crossed reducing no of ball by 1")
			config.no_of_balls -= 1
			logging.info('balls after reduction %d ', config.no_of_balls)
			if((config.no_of_balls)==0):
				logging.debug("in the if statement reducing lives by 1")
				config.lives -=1
				os.system('aplay -q ./sounds/lose_life.wav&')

				config.ball_release = 0 # paddle grab for new life
				self.on_paddle_grab = 1
				for i in range(6): # life gone make powerup array 0 
					config.powerup_array[i] = 0 
				
				# already checking for paddle length in paddle motion function
				# obj1.clear(obj)
				# #restoring back from powerup
				# obj1.shape = ["A","B","C","D","E"]
				# obj1.length = 5
				# obj1.print_paddle(obj) # printing after clearing to take expand/shrink into consideration
				
				self.thru = 0

				config.no_of_balls += 1
				self.x = obj1.get_x() - 1
				self.y = obj1.get_y() + 2
				self.vx = -1
				self.vy = 1
			else:
				self.vx = 0
				self.vy = 0
				del(self)
				logging.info('deleted self')
				# self._registry2.remove(self)
				config.ball_mul.remove(obj2)
				logging.info('removed self')
			return

		look_ahead_x = self.x + self.vx # look ahead only for paddle
		look_ahead_y = self.y
		
		if((obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "A")) or (
		obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "A"))):
			self.vy -= 2
			self.vx = (-1) * (self.vx)

			self.on_paddle_grab = 1
			# if(config.powerup_array[5] == 1):
			# 	config.ball_release = 0
			# return 
		elif((obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "B")) or (
		obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "B"))):
			self.vy -= 1
			self.vx = (-1) * (self.vx)
			
			self.on_paddle_grab = 1
			# if(config.powerup_array[5] == 1):
			# 	config.ball_release = 0
			# return
		elif((obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "C")) or (
		obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "C"))):
			# self.vy -= 2
			self.vx = (-1) * (self.vx)

			self.on_paddle_grab = 1
			# if(config.powerup_array[5] == 1):
			# 	config.ball_release = 0
			# return
		elif((obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "D")) or (
		obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "D"))):
			self.vy += 1
			self.vx = (-1) * (self.vx)

			self.on_paddle_grab = 1
			# if(config.powerup_array[5] == 1):
			# 	config.ball_release = 0
			# return
		elif((obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "E")) or (
		obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "E"))):
			self.vy += 2
			self.vx = (-1) * (self.vx)
			
			self.on_paddle_grab = 1
			# if(config.powerup_array[5] == 1):
			# 	config.ball_release = 0
			# return
		elif((obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "F")) or (
		obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "F"))):
			self.vy += 2
			self.vx = (-1) * (self.vx)
			
			self.on_paddle_grab = 1
			# if(config.powerup_array[5] == 1):
			# 	config.ball_release = 0
			# return
		elif((obj.Matrix[look_ahead_x][look_ahead_y] == (config.colour5 + "G")) or (
		obj.Matrix[look_ahead_x][look_ahead_y] == (config.shooting_paddle_color + "G"))):
			self.vy += 2
			self.vx = (-1) * (self.vx)
			
			self.on_paddle_grab = 1
			# if(config.powerup_array[5] == 1):
			# 	config.ball_release = 0
			# return
		else:
			self.on_paddle_grab = 0
		
		if(obj.Matrix[self.x][self.y] == (config.colour1+"<")):
			if(config.level == 3):
				for i in range(-1,1):
					obj.Matrix[self.x][i + self.y] = " "
				self.vx = (-1) * self.vx
				return 

			self.check_fireball(obj)
			config.no_of_bricks_hit += 1
			if(self.thru == 0):
				self.vx = (-1) * self.vx
			config.score += 1

			for i in range(0,4):
				obj.Matrix[self.x][i + self.y] = " "

			x = (random.randint(1,100) % 8) + 1 # 1-6
			if (x == 1):
				objs.append(Powerup1(obj, self.vx, self.vy))
			if (x == 2):
				objs.append(Powerup2(obj, self.vx, self.vy))
			if (x == 3):
				objs.append(Powerup3(obj, self.vx, self.vy))
			if (x == 4):
				objs.append(Powerup4(obj, self.vx, self.vy))
			if (x == 5):
				objs.append(Powerup5(obj, self.vx, self.vy))
			if (x == 6):
				objs.append(Powerup6(obj, self.vx, self.vy))
			if (x == 7):
				objs.append(Powerup7(obj, self.vx, self.vy))
			if (x == 8):
				objs.append(Powerup8(obj, self.vx, self.vy))
			objs[config.no_of_powerups].show(obj, self)
			config.no_of_powerups += 1
			
			return
		if(obj.Matrix[self.x][self.y] == (config.colour1+"%")):
			self.check_fireball(obj)
			config.no_of_bricks_hit += 1
			if(self.thru == 0):
				self.vx = (-1) * self.vx
			config.score += 1

			for i in range(-1,3):
				obj.Matrix[self.x][i + self.y] = " "

			x = (random.randint(1,100) % 8) + 1 # 1-6
			if (x == 1):
				objs.append(Powerup1(obj, self.vx, self.vy))
			if (x == 2):
				objs.append(Powerup2(obj, self.vx, self.vy))
			if (x == 3):
				objs.append(Powerup3(obj, self.vx, self.vy))
			if (x == 4):
				objs.append(Powerup4(obj, self.vx, self.vy))
			if (x == 5):
				objs.append(Powerup5(obj, self.vx, self.vy))
			if (x == 6):
				objs.append(Powerup6(obj, self.vx, self.vy))
			if (x == 7):
				objs.append(Powerup7(obj, self.vx, self.vy))
			if (x == 8):
				objs.append(Powerup8(obj, self.vx, self.vy))
			objs[config.no_of_powerups].show(obj, self)
			config.no_of_powerups += 1
			
			return
		if(obj.Matrix[self.x][self.y] == (config.colour1+"$")):
			self.check_fireball(obj)
			config.no_of_bricks_hit += 1
			if(self.thru == 0):
				self.vx = (-1) * self.vx
			config.score += 1

			for i in range(-2,2):
				obj.Matrix[self.x][i + self.y] = " "

			x = (random.randint(1,100) % 8) + 1 # 1-6
			if (x == 1):
				objs.append(Powerup1(obj, self.vx, self.vy))
			if (x == 2):
				objs.append(Powerup2(obj, self.vx, self.vy))
			if (x == 3):
				objs.append(Powerup3(obj, self.vx, self.vy))
			if (x == 4):
				objs.append(Powerup4(obj, self.vx, self.vy))
			if (x == 5):
				objs.append(Powerup5(obj, self.vx, self.vy))
			if (x == 6):
				objs.append(Powerup6(obj, self.vx, self.vy))
			if (x == 7):
				objs.append(Powerup7(obj, self.vx, self.vy))
			if (x == 8):
				objs.append(Powerup8(obj, self.vx, self.vy))
			objs[config.no_of_powerups].show(obj, self)
			config.no_of_powerups += 1
			
			return
		if(obj.Matrix[self.x][self.y] == (config.colour1+">")):
			self.check_fireball(obj)
			config.no_of_bricks_hit += 1
			if(self.thru == 0):
				self.vx = (-1) * self.vx
			config.score += 1

			for i in range(-3,1):
				obj.Matrix[self.x][i + self.y] = " "

			x = (random.randint(1,100) % 8) + 1 # 1-6
			if (x == 1):
				objs.append(Powerup1(obj, self.vx, self.vy))
			if (x == 2):
				objs.append(Powerup2(obj, self.vx, self.vy))
			if (x == 3):
				objs.append(Powerup3(obj, self.vx, self.vy))
			if (x == 4):
				objs.append(Powerup4(obj, self.vx, self.vy))
			if (x == 5):
				objs.append(Powerup5(obj, self.vx, self.vy))
			if (x == 6):
				objs.append(Powerup6(obj, self.vx, self.vy))
			if (x == 7):
				objs.append(Powerup7(obj, self.vx, self.vy))
			if (x == 8):
				objs.append(Powerup8(obj, self.vx, self.vy))
			objs[config.no_of_powerups].show(obj, self)
			config.no_of_powerups += 1
			
			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"[") and self.thru==0):
			self.check_fireball(obj)
			config.no_of_bricks_hit += 1
			self.vx = (-1) * self.vx
			config.score += 1 

			if config.fireball is 0:
				obj.Matrix[self.x][self.y] = (config.colour1+"<")
				obj.Matrix[self.x][1+self.y] = (config.colour1+"%")
				obj.Matrix[self.x][2+self.y] = (config.colour1+"$")
				obj.Matrix[self.x][3+self.y] = (config.colour1+">")
			
			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"%") and self.thru==0):
			self.check_fireball(obj)
			config.no_of_bricks_hit += 1
			self.vx = (-1) * self.vx
			config.score += 1

			if config.fireball is 0:
				obj.Matrix[self.x][-1+self.y] = (config.colour1+"<")
				obj.Matrix[self.x][self.y] = (config.colour1+"%")
				obj.Matrix[self.x][1+self.y] = (config.colour1+"$")
				obj.Matrix[self.x][2+self.y] = (config.colour1+">")
			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"$") and self.thru==0):
			self.check_fireball(obj)
			config.no_of_bricks_hit += 1
			self.vx = (-1) * self.vx
			config.score += 1
			if config.fireball is 0:
				obj.Matrix[self.x][-2+self.y] = (config.colour1+"<")
				obj.Matrix[self.x][-1+self.y] = (config.colour1+"%")
				obj.Matrix[self.x][0+self.y] = (config.colour1+"$")
				obj.Matrix[self.x][1+self.y] = (config.colour1+">")
			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"]") and self.thru==0):
			self.check_fireball(obj)
			config.no_of_bricks_hit += 1
			self.vx = (-1) * self.vx
			config.score += 1
			if config.fireball is 0: 
				obj.Matrix[self.x][-3+self.y] = (config.colour1+"<")
				obj.Matrix[self.x][-2+self.y] = (config.colour1+"%")
				obj.Matrix[self.x][-1+self.y] = (config.colour1+"$")
				obj.Matrix[self.x][0+self.y] = (config.colour1+">")
			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"[") and self.thru==1):
			self.check_fireball(obj)
			# self.vx = (-1) * self.vx
			config.no_of_bricks_hit += 1
			config.score += 1

			for i in range(0,4):
				obj.Matrix[self.x][i + self.y] = " "
			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"%") and self.thru==1):
			self.check_fireball(obj)
			# self.vx = (-1) * self.vx
			config.no_of_bricks_hit += 1
			config.score += 1

			for i in range(-1,3):
				obj.Matrix[self.x][i + self.y] = " "
			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"$") and self.thru==1):
			self.check_fireball(obj)
			# self.vx = (-1) * self.vx
			config.no_of_bricks_hit += 1
			config.score += 1

			for i in range(-2,2):
				obj.Matrix[self.x][i + self.y] = " "
			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"]") and self.thru==1):
			self.check_fireball(obj)
			# self.vx = (-1) * self.vx
			config.no_of_bricks_hit += 1
			config.score += 1

			for i in range(-3,1):
				obj.Matrix[self.x][i + self.y] = " "
			return
		if(obj.Matrix[self.x][self.y] == (config.colour3+"{")):
			self.check_fireball(obj)
			if(self.thru==1):
				config.score += 1
				for i in range(0,4):
					obj.Matrix[self.x][i + self.y] = " "
			else:
				self.vx = (-1) * self.vx
			return
		if(obj.Matrix[self.x][self.y] == (config.colour3+"%")):
			self.check_fireball(obj)
			if(self.thru==1):
				config.score += 1
				for i in range(-1,3):
					obj.Matrix[self.x][i + self.y] = " "
			else:
				self.vx = (-1) * self.vx
			
			return
		if(obj.Matrix[self.x][self.y] == (config.colour3+"$")):
			self.check_fireball(obj)
			if(self.thru==1):
				config.score += 1
				for i in range(-2,2):
					obj.Matrix[self.x][i + self.y] = " "
			else:
				self.vx = (-1) * self.vx
			
			return
		if(obj.Matrix[self.x][self.y] == (config.colour3+"}")):
			self.check_fireball(obj)
			if(self.thru==1):
				config.score += 1
				for i in range(-3,1):
					obj.Matrix[self.x][i + self.y] = " "
			else:
				self.vx = (-1) * self.vx
			return

		if(obj.Matrix[self.x][self.y] == (config.colour6+"(")):
			if(self.thru==1):
				config.score += 1
			else:
				self.vx = (-1) * self.vx
			self.dfs(obj, self.x, self.y)
			return
		if(obj.Matrix[self.x][self.y] == (config.colour6+"%")):
			if(self.thru==1):
				config.score += 1
			else:
				self.vx = (-1) * self.vx
			self.dfs(obj, self.x, self.y)
			return
		if(obj.Matrix[self.x][self.y] == (config.colour6+"$")):
			if(self.thru==1):
				config.score += 1
			else:
				self.vx = (-1) * self.vx
			self.dfs(obj, self.x, self.y)
			return
		if(obj.Matrix[self.x][self.y] == (config.colour6+")")):
			if(self.thru==1):
				config.score += 1				
			else:
				self.vx = (-1) * self.vx
			self.dfs(obj, self.x, self.y)
			return

		if(obj.Matrix[self.x][self.y] == (config.colour5+"/")):
			config.score += 1
			config.ufo_health -= 1
			if(config.ufo_health==0):
				yay()
				os.system('aplay -q ./sounds/win.wav&')
				sys.exit(0)			
			self.vx = (-1) * self.vx
			return
	def ball_movement(self, obj): # first clear then move then show
		if(obj.Matrix[self.x][self.y] == (Fore.CYAN + self._shape)):
			self.clear(obj)
		
		self.x += self.vx
		self.y += self.vy
		
		# if(self.x == 29):
		# 	self.on_paddle_grab = 1
		# else:
		# 	self.on_paddle_grab = 0
		# if(obj.Matrix[self.x][self.y] == "A" or obj.Matrix[self.x][self.y] == "B" or obj.Matrix[self.x][self.y] == "C" or obj.Matrix[self.x][self.y] == "D" or obj.Matrix[self.x][self.y] == "E"):
		# 	self.ball_collision_check(obj, obj1)
		
		if(obj.Matrix[self.x][self.y] == " "):
			obj.Matrix[self.x][self.y] = (Fore.CYAN + self._shape)

	def print_ball(self, obj, a, b):
		obj.Matrix[self.x][self.y] = (Fore.CYAN + self._shape)
		# self.clear(obj)

	def clear(self, obj):
		obj.Matrix[self.x][self.y] = " "

	def brick_clear(self, obj):
		for i in range(-4,4):
			obj.Matrix[self.x][i + self.y] = " "

	def duplicate(self, obj):
		config.no_of_balls += 1
		config.ball_mul.append(Ball(obj, self.x, self.y))

from powerup import *