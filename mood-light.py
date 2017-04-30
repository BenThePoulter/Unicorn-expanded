from unicornExpanded import *
from random import randint


uh.brightness(0)

while True:
 R = randint(0,255)
 G = randint(0,255)
 B = randint(0,255)

 fill(R, G, B)
 fadein()
 pulse(randint(5, 30))
 fadeout()
 sleep(1)
