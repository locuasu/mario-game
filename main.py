#  main.py
import pgzrun
from config import WIDTH, HEIGHT
from player import player, update_player, draw_player
from enemies import enemies, update_enemies, draw_enemies
from game_state import GameState
game = GameState()

def update():
    update_player()
    update_enemies()

def draw():
    
    screen.blit("fondo", (0, 0))
    draw_player()
    draw_enemies()

pgzrun.go()
