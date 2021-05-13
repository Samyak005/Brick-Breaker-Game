# Brick Breaker

### Overview
Classic brick breaker game terminal-based written in Python3. Move the paddle to prevent ball from falling on the ground. Destroy all bricks and take powerups.

### Description of Classes Created
#### Board
The board class creates a 40*80 board for gameplay, with boundaries. It also comprises of a print_board function to take a print of the board.

#### Brick
Brick print function, brick coordinate specification, strength decrementing, clearing is done here
4 types of bricks:
1. 1 hit to break
2. 2 hits to break
3. Unbreakable
4. Exploding Brick

#### Ball
Contains functions for collision handling of ball with walls, paddle and different bricks, printing, clearing, movement of ball, duplication of ball, and dfs for exploding bricks.

#### Paddle
Contains functions for printing, clearing, and movement of paddle

#### Powerup
Is of 6 different types. Contains functions for movement, printing, clearing of powerup

### OOPS:
Private variables start with _ and they can be changed only by its class member functions

1. Inheritance\
Inheritance allows us to define a class that inherits all the methods and properties from another class. 
There is one brick class and types of bricks of varied strengths are inherited from it.
Similar implementation is present in powerup class.

2. Polymorphism\
Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.

```python
class Brick():
    ...
    def print_brick(self, obj):
		for i in range (4):
				obj.Matrix[self._x][i + self._y] = (config.colour6 + config.shape4[i])
```
```python
class Brick1(Brick):
    ...
    def print_brick(self, obj):
		for i in range (4):
			obj.Matrix[self._x][i + self._y] = (config.colour1 + config.shape1[i])
```

3. Encapsulation\
The idea of wrapping data and the methods that work on data within one unit. Prevents accidental modification of data.
Brick, Paddle, Powerup, Ball have separate classes and objects. They are maintained in their respective files.

4. Abstraction\
Abstraction means hiding the complexity and only showing the essential features of the object.

In paddle class:
```python
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
				for ball in config.ball_mul:
					if(ball.on_paddle_grab == 1):  # locating which ball is on paddle
						ball.clear(obj)
						ball.x = self._x - 1
						ball.y -= 3                # dont want ball to always start from centre of paddle
						ball.print_ball(obj, 0, 0)
```
.motion() is an abstraction

### How To Play:
1. Press 'q' to quit the game
2. 'a' and 'd' are used to move the paddle left and right respectively
3. After paddle grab powerup or when a new life is started press space(" ") to launch the ball from the paddle
4. Press 'w' to shoot bullets with shooting paddle
5. Press 'p' to skip level

### Installation
```
sudo apt-get update
sudo apt-get install python3
```
### To Run:
```
python3 game.py
```