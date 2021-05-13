from __future__ import print_function
import os
import sys
from colorama import init, Fore, Back, Style
import config
import logging

logging.basicConfig(filename='log_ui',
					filemode='a',
					format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
					datefmt='%H:%M:%S',
					level=logging.DEBUG)

class Board():
	def __init__(self, board_x, board_y):
		self.Matrix = [[' ' for x in range(board_y)] for y in range(board_x)]
		self.Matrix2 = [[0 for x in range(board_y)] for y in range(board_x)]
		
	def board_make(self, board_x, board_y):
		for i in range(board_x-6):
			for j in range(board_y-4):
				if(i < 2):
					self.Matrix[i][j] = "X"
				if(i > board_x-9):
					self.Matrix[i][j] = "Z"
				if(j < 2 or j > board_y-7):
					self.Matrix[i][j] = "Y"

		# code for reading from file and assigning to matrix
		# f = open("1.txt", "r") 
		# for i in range(25):
		# 	for j in range(76):
		# 		self.Matrix[i][j] = f.read(1)

		# f.close()

		# for i in range(3, 10):
		# 	for j in range(4, 25):
		# 		self.Matrix[i][j] = f.read(1)
		# 		logging.debug(self.Matrix[i][j])

	def print_board(self, board_x, board_y):
		os.system("clear")
		for i in range(board_x-6):
			for j in range(board_y-4):
				print(Fore.RED + self.Matrix[i][j] + Style.RESET_ALL, end = " ")
			print()
	
	def ufo_defense(self):
		for i in range(3, 72):
			self.Matrix[5][i] = Fore.WHITE+"<"
			print(self.Matrix[5][i] + Style.RESET_ALL)
		
	def clear_board(self, board_x, board_y):
		self.Matrix = [[' ' for x in range(board_y)] for y in range(board_x)]
		self.board_make(board_x, board_y)
		for i in range(board_x-6):
			for j in range(board_y-4):
				print(self.Matrix[i][j], end = " ")
			print()