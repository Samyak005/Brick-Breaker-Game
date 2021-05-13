#!/usr/bin/env python
from __future__ import print_function
from board import *
from paddle import *
from getchunix import *
from alarmexception import *
from ball import *
from brick import *
from bullet import *
import sys,time
import logging
from colorama import init, Fore, Back, Style
import config
from powerup import *
from bomb import *
from ufo import *

getch = GetchUnix()

def alarmHandler(signum, frame):
	raise AlarmException

def input_to(timeout = 0.3):# 0.03, more timeout more slow the game
	signal.signal(signal.SIGALRM, alarmHandler)
	signal.setitimer(signal.ITIMER_REAL, timeout)
	try:
		text = getch()
		signal.alarm(0)
		return text
	except AlarmException:
		print("Game Over")
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return None

def input_to_space(timeout = 0.5):# 0.03, more timeout more slow the game
	signal.signal(signal.SIGALRM, alarmHandler)
	signal.setitimer(signal.ITIMER_REAL, timeout)
	try:
		text = getch()
		signal.alarm(0)
		return text
	except AlarmException:
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return None

ball_temp = 0
board = Board(config.board_x, config.board_y)
board.board_make(config.board_x, config.board_y)
board.print_board(config.board_x, config.board_y)

paddle = Paddle(board)
paddle.print_paddle(board)

def game_over():
    os.system('aplay -q ./sounds/game_over.wav&')
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     ".center(40))                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "  _____                         ____                 ".center(40))                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " / ____|                       / __ \                ".center(40))              
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ".center(40))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +"| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|".center(40))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +"| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ".center(40))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +" \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ".center(40))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     ".center(40)+Style.RESET_ALL)                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     ".center(40)+Style.RESET_ALL)                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     ".center(40)+Style.RESET_ALL)
    sys.exit(0)

ufo = UFO(board)
# bomb1 = Bomb(board, ufo, 5, 34)
# bomb2 = Bomb(board, ufo, 3, 34)
# brick addition to be removed later
#############################################################################
rainbow_coords = [(25, 45), (18, 38), (20, 60)]
def rainbow_clear():
	for a, b in rainbow_coords: 
		for i in range (4):
			board.Matrix[a][i + b] = " "

def rainbow_brick():
	if(config.level==3):
		return
	rainbow_clear()
	x = (random.randint(1,100) % 4) + 1 # 1-4
	if (x == 1):
		for a, b in rainbow_coords: 
			for i in range (4):
				board.Matrix[a][i + b] = (config.colour2 + config.shape1[i])
	if (x == 2):
		for a, b in rainbow_coords: 
			for i in range (4):
				board.Matrix[a][i + b] = (config.colour1 + config.shape2[i])
	if (x == 3):
		for a, b in rainbow_coords: 
			for i in range (4):
				board.Matrix[a][i + b] = (config.colour3 + config.shape4[i])
	if (x == 4):
		for a, b in rainbow_coords: 
			for i in range (4):
				board.Matrix[a][i + b] = (config.colour6 + config.shape3[i])

def brick_addition():
	board.clear_board(config.board_x, config.board_y)

	super_coords = [(2,2),(3,4),(4,2),(5,4),(6,2),(7,4),(8,2),(9,4),
					(2,70),(3,68),(4,70),(5,68),(6,70),(7,68),(8,70),(9,68)]
	exploding_brick = []
	k = 0
	for i,j in super_coords:
		exploding_brick.append(Super(board, i, j))
		exploding_brick[k].print_brick(board)
		k += 1

	brick1_count = 15
	brick2_count = 7
	unbreakable_count = 5

	brick1 = []
	for i in range(brick1_count):
		brick1.append(Brick1(board))
		brick1[i].print_brick(board)

	brick2 = []
	for i in range(brick2_count):
		brick2.append(Brick2(board))
		brick2[i].print_brick(board)

	unbreakable = []
	for i in range(unbreakable_count):
		unbreakable.append(Unbreakable(board))
		unbreakable[i].print_brick(board)

def level3_brick_addition():
	board.clear_board(config.board_x, config.board_y)

	unbreakable_count = 20
	unbreakable = []
	for i in range(unbreakable_count):
		unbreakable.append(Unbreakable(board))
		unbreakable[i].print_brick(board)
##############################################################################
def fresh_ball_start():
	config.ball_release = 0 # paddle grab for new life
	ball.on_paddle_grab = 1
	for i in range(6): # life gone make powerup array 0 
		config.powerup_array[i] = 0 

	ball.thru = 0

	ball.x = paddle.get_x() - 1
	ball.y = paddle.get_y() + 2
	ball.vx = -1
	ball.vy = 1

def level_up(force):
	if force==0:
		if(config.no_of_bricks_hit == config.exact_no_of_bricks):
			if(config.level==2): 
				fresh_ball_start()
				ufo.print_ufo(board)
				level3_brick_addition()
			else:	
				fresh_ball_start()
				brick_addition()
			
			config.level += 1
			config.no_of_bricks_hit = 0
	else:
		if(config.level == 3):
			game_over()

		elif(config.level==2): 
			fresh_ball_start()
			ufo.print_ufo(board)
			level3_brick_addition()
			config.level += 1
		else:	
			fresh_ball_start()
			brick_addition()
			config.level += 1

##############################################################################
curtime = time.time()

ball = Ball(board)
config.ball_mul.append(ball)
config.no_of_balls += 1

ball.print_ball(board, 29, 40)
prev_x = 29
prev_y = 40

brick_addition()

while(config.lives>0):
	level_up(0)
	rainbow_brick()

	if(config.ball_release == 0):
		while(1):
			c = input_to_space()
			if(c=='p'):
				level_up(1)
			paddle.motion(c, board)
			if(config.level == 3):
				ufo.motion(c, board)
			for powerup in Powerup:
				powerup.move(board)
				powerup.times_up(time.time(), board, paddle)
			for bullet in Bullet:
				bullet.bullet_movement(board)
				bullet.bullet_collision_check(board)
			for ball in config.ball_mul: 
			# 	if(ball.on_paddle_grab == 1):
			# 		ball.clear(board)
			# 		ball.x = paddle.x - 1
			# 		# ball.y = paddle.y + 2 # dont want ball to always start from centre of paddle
					#ball.print_ball(board, 0, 0)
				board.print_board(config.board_x, config.board_y)
				
				if(ball.on_paddle_grab != 1): # other balls continue to move and are not stopped
					ball.ball_movement(board)
					ball.ball_collision_check(board, paddle, ball) 
					board.print_board(config.board_x, config.board_y)
					print("Lives:" , config.lives)
					print("Level:" , config.level)
					print("Score:" , config.score)
					print("Time:" , time.time() - curtime)
					print("Hit Space to Start")
					print("Power-up array", config.powerup_array)
					print("Number of balls", config.no_of_balls)
					print("Number of brick hit", config.no_of_bricks_hit)
					# print(len(config.ball_mul))
			if(c== " "):
				break

		config.ball_release = 1
		
	for ball in config.ball_mul:
		ball.ball_movement(board)
		ball.ball_collision_check(board, paddle, ball) # passing paddle to check collision with it, get x,y of paddle

	for bullet in Bullet:
		bullet.bullet_movement(board)
		bullet.bullet_collision_check(board)

	for powerup in Powerup:
		powerup.move(board)
		powerup.times_up(time.time(), board, paddle)
	# if(board.Matrix[prev_x][prev_y] is "@"):
	# board.Matrix[prev_x][prev_y] = "-"
	
	board.print_board(config.board_x, config.board_y)

	print("Lives:" , config.lives)
	print("Level:" , config.level)
	print("Score:" , config.score)
	print("Time:" , time.time() - curtime)
	if(config.level==3):
		for _ in range(config.ufo_health):
			print('X', end="")
		print()
	i = 0
	for ball in config.ball_mul: # maximum print 3 otherwise game board reduces
		i += 1
		if(i==3):
			break
		print("vx" , ball.vx)
		print("vy" , ball.vy)
		print("x" , ball.x)
		print("y" , ball.y)	
		print("Hit Space to Start")
		print("Power-up array", config.powerup_array)
		print("Number of balls", config.no_of_balls)
		print("Number of brick hit", config.no_of_bricks_hit)
		# print(len(config.ball_mul))
	
	# print(board.Matrix[ball.x][ball.y]) # print element at balls position

	# prev_x = ball.x # was storing for collision detection/ ball clearing
	# prev_y = ball.y

	c = input_to()
	if(c=='p'):
		level_up(1)

	paddle.motion(c, board)
	if(config.level == 3):
		ufo.motion(c, board)
	# time.sleep(0.005)

game_over()