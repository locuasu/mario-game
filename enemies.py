# enemies.py
from pgzero.actor import Actor
from config import ENEMY_SPEED, WIDTH, HEIGHT, LASER_SPEED

import random

enemies = [Actor("enemy", (100, 100))]
laser_from_left = True
lasers = []
LASER_HEIGHT = 40
LASER_GAP = 200          # espacio libre para pasar


def spawn_laser():
    global laser_from_left

    laser = Actor("laser")

    laser.y = -LASER_HEIGHT

    if laser_from_left:
        # ocupa izquierda → deja libre derecha
        laser.x = (WIDTH - LASER_GAP) / 2 - laser.width / 2
        laser.block_side = "left"
    else:
        # ocupa derecha → deja libre izquierda
        laser.x = (WIDTH + LASER_GAP) / 2 + laser.width / 2
        laser.block_side = "right"

    lasers.append(laser)
    laser_from_left = not laser_from_left
def update_enemies():
    dodged = 0
    for e in enemies:
        e.y += ENEMY_SPEED
        if e.y > 650:
            e.pos = (random.randint(50, 750), -50)
            dodged += 1
    # ----------------------
    # lasers
    # ----------------------
    for laser in lasers[:]:
        laser.y += LASER_SPEED

        if laser.y > HEIGHT + LASER_HEIGHT:
            lasers.remove(laser)
            dodged += 1

    # spawn laser aleatorio
    if random.randint(0, 120) == 0:
        spawn_laser()
    return dodged
              
def draw_enemies():
    for e in enemies: 
        e.draw()
    for laser in lasers:
        laser.draw()