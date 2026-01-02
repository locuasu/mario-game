# star.py
from pgzero.actor import Actor
from config import STAR_SPEED,  HEIGHT
import random

star = Actor("star", (random.randint(50,750), -50))

star.visible = True

def update_star():
    if not star.visible:
        return
    star.y += STAR_SPEED

    if star.y > HEIGHT + 50:
        respawn_star()
def draw_star():
    if star.visible:
        star.draw()

def respawn_star():
    
    star.pos = (random.randint(50,750), -50)
    star.visible = True
         
