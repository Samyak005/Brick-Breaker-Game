import sys
from colorama import init, Fore, Back, Style
import config
import logging
from random import randint

logging.basicConfig(filename='logname',
					filemode='a',
					format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
					datefmt='%H:%M:%S',
					level=logging.DEBUG)

class IterRegistry3(type):
    def __iter__(cls):
        return iter(cls._registry3)

class Bullet(metaclass = IterRegistry3):
	_registry3 = []

	def __init__(self, obj,a, b, ind):#, bullet_indx):
		self._registry3.append(self)
		self.no = ind
		self.x = a
		self.y = b
		self.vx = -1
		self._shape = config.bullet_shape
		self.killed = 0

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

	def bullet_collision_check(self, obj):
		if(self.x < 3 or self.killed==1):
			# del(self)
			# del config.bullet_list[self.no]
			self.clear(obj)
			return
		if(obj.Matrix[self.x][self.y] == (config.colour1+"<")):
			config.score += 1
			self.killed = 1
			for i in range(0,4):
				obj.Matrix[self.x][i + self.y] = " "

			return
		if(obj.Matrix[self.x][self.y] == (config.colour1+"%")):
			config.score += 1
			self.killed = 1
			for i in range(-1,3):
				obj.Matrix[self.x][i + self.y] = " "

			return
		if(obj.Matrix[self.x][self.y] == (config.colour1+"$")):
			config.score += 1
			self.killed = 1
			for i in range(-2,2):
				obj.Matrix[self.x][i + self.y] = " "

			return
		if(obj.Matrix[self.x][self.y] == (config.colour1+">")):
			config.score += 1
			self.killed = 1
			for i in range(-3,1):
				obj.Matrix[self.x][i + self.y] = " "

			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"[")):
			config.score += 1 
			self.killed = 1
			obj.Matrix[self.x][self.y] = (config.colour1+"<")
			obj.Matrix[self.x][1+self.y] = (config.colour1+"%")
			obj.Matrix[self.x][2+self.y] = (config.colour1+"$")
			obj.Matrix[self.x][3+self.y] = (config.colour1+">")
			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"%")):
			config.score += 1
			self.killed = 1
			obj.Matrix[self.x][-1+self.y] = (config.colour1+"<")
			obj.Matrix[self.x][self.y] = (config.colour1+"%")
			obj.Matrix[self.x][1+self.y] = (config.colour1+"$")
			obj.Matrix[self.x][2+self.y] = (config.colour1+">")
			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"$")):
			config.score += 1
			self.killed = 1
			obj.Matrix[self.x][-2+self.y] = (config.colour1+"<")
			obj.Matrix[self.x][-1+self.y] = (config.colour1+"%")
			obj.Matrix[self.x][0+self.y] = (config.colour1+"$")
			obj.Matrix[self.x][1+self.y] = (config.colour1+">")
			return
		if(obj.Matrix[self.x][self.y] == (config.colour2+"]")):
			config.score += 1
			self.killed = 1
			obj.Matrix[self.x][-3+self.y] = (config.colour1+"<")
			obj.Matrix[self.x][-2+self.y] = (config.colour1+"%")
			obj.Matrix[self.x][-1+self.y] = (config.colour1+"$")
			obj.Matrix[self.x][0+self.y] = (config.colour1+">")
			return

		if(obj.Matrix[self.x][self.y] == (config.colour6+"(")):
			config.score += 1
			self.killed = 1				
			self.dfs(obj, self.x, self.y)
			return
		if(obj.Matrix[self.x][self.y] == (config.colour6+"%")):
			config.score += 1	
			self.killed = 1			
			self.dfs(obj, self.x, self.y)
			return
		if(obj.Matrix[self.x][self.y] == (config.colour6+"$")):
			config.score += 1	
			self.killed = 1			
			self.dfs(obj, self.x, self.y)
			return
		if(obj.Matrix[self.x][self.y] == (config.colour6+")")):
			config.score += 1	
			self.killed = 1			
			self.dfs(obj, self.x, self.y)
			return

		if(obj.Matrix[self.x][self.y] == (config.colour3+"{")):
			self.killed = 1				
			return
		if(obj.Matrix[self.x][self.y] == (config.colour3+"%")):
			self.killed = 1			
			return
		if(obj.Matrix[self.x][self.y] == (config.colour3+"$")):
			self.killed = 1			
			return
		if(obj.Matrix[self.x][self.y] == (config.colour3+"}")):
			self.killed = 1			
			return

	def bullet_movement(self, obj): # first clear then move then show
		if(self.x < 3 or self.killed==1):
			self.clear(obj)
			return

		if(obj.Matrix[self.x][self.y] == (Fore.CYAN + self._shape)):
			self.clear(obj)
		
		self.x += self.vx
		
		if(obj.Matrix[self.x][self.y] == " "):
			obj.Matrix[self.x][self.y] = (Fore.CYAN + self._shape)

	def print_bullet(self, obj, a, b):
		obj.Matrix[self.x][self.y] = (Fore.CYAN + self._shape)
		# self.clear(obj)

	def clear(self, obj):
		obj.Matrix[self.x][self.y] = " "

	def brick_clear(self, obj):
		for i in range(-4,4):
			obj.Matrix[self.x][i + self.y] = " "