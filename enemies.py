# enemies.py
from pgzero.actor import Actor
from config import ENEMY_SPEED
import random

enemies = [Actor("enemy", (100, 100))]

def update_enemies():
    for e in enemies:
        e.y += ENEMY_SPEED
        if e.y > 650:
            e.pos = (random.randint(50, 750), -50)
     
def draw_enemies():
    for e in enemies:
        e.draw()
