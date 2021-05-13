from colorama import init, Fore, Back, Style

board_x = 40
board_y = 80

lives = 3
score = 0
level = 1
exact_no_of_bricks = 29
no_of_bricks_hit = 0
gravity = 0
fireball = 0
ufo_coverup = 2

colour1 = Fore.WHITE
colour2 = Fore.YELLOW
colour3 = Fore.BLUE
colour4 = Fore.MAGENTA
colour5 = Fore.GREEN
colour6 = Fore.GREEN
shooting_paddle_color = Fore.GREEN + Back.GREEN

shape1 = ["<", "%", "$", ">"]
shape2 = ["[", "%", "$", "]"]
shape3 = ["{", "%", "$", "}"]
shape4 = ["(", "%", "$", ")"]

bullet_shape = "|"
bomb_shape = "0"
ufo_health = 10

thisdict = {
  "1": "Powerup1",
  "2": "Powerup2",
  "3": "Powerup3",
  "4": "Powerup4",
  "5": "Powerup5",
  "6": "Powerup6",
}

no_of_powerups = 0
powerup_time = 10

powerup_array = [0,0,0,0,0,0,0,0]

no_of_balls = 0
ball_mul = list()
ball_release = 0

shooting_paddle = 0
bullet_list = list()
no_of_bullets = 0