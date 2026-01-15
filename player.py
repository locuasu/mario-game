# player.py
from pgzero.actor import Actor
from pgzero.keyboard import keyboard 
from config import PLAYER_SPEED

player = Actor("player", (400, 500))

def update_player(game):
    player.image = game.current_skin
    if keyboard.left:
        player.x -= PLAYER_SPEED
    if keyboard.right:
        player.x += PLAYER_SPEED

def draw_player():
    player.draw()
