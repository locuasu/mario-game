# player.py
from pgzero.actor import Actor
from pgzero.keyboard import keyboard 
from config import PLAYER_SPEED, WIDTH, HEIGHT

player = Actor("player", (400, 500))

def update_player(game):
    player.image = game.current_skin
    if keyboard.left:
        player.x -= PLAYER_SPEED
    if keyboard.right:
        player.x += PLAYER_SPEED
    if keyboard.up:
        player.y -= PLAYER_SPEED
    if keyboard.down:
        player.y += PLAYER_SPEED
    half_w = player.width //2
    half_h  = player.height //2
    player.x = max(half_w, min(WIDTH - half_w, player.x))
    player.y = max(half_h, min(HEIGHT - half_h, player.y))
def draw_player():
    player.draw()
  