from __future__ import print_function
import signal,copy,sys,time
from random import randint
import tty, termios

class GetchUnix:
    def __call__(self):
        
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
