# player.py
from pgzero.actor import Actor
from pgzero.keyboard import keyboard 
from config import PLAYER_SPEED, WIDTH, HEIGHT

player = Actor("player_right", (400, 500))
direction = "right"
state = "normal"   # normal | hurt | inv
def update_player(game):
    global direction, state
    player.image =  f"{game.current_skin}_right"
    if keyboard.left:
        player.x -= PLAYER_SPEED
        direction = "left"
    if keyboard.right:
        player.x += PLAYER_SPEED
        direction = "right"
    if keyboard.up:
        player.y -= PLAYER_SPEED
    if keyboard.down:
        player.y += PLAYER_SPEED
    half_w = player.width //2
    half_h  = player.height //2
    player.x = max(half_w, min(WIDTH - half_w, player.x))
    player.y = max(half_h, min(HEIGHT - half_h, player.y))
    skin = game.current_skin
    if game.invincible:
        player.image = f"{skin}_inv"
    elif state == "hurt":
        player.image = f"{skin}_hurt"
    else:
        player.image = f"{skin}_{direction}"       

def draw_player():
    player.draw()
def take_damage():
    global state
    state = "hurt"

def reset_state():
    global state
    state = "normal"
