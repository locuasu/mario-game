#  main.py
import pgzrun
from config import WIDTH, HEIGHT
from player import player, update_player, draw_player
from enemies import enemies, update_enemies, draw_enemies
from game_state import GameState
game = GameState()


def update():
    if not game.running:
        return   # ← DETIENE TODO EL JUEGO
    update_player()
    update_enemies()
    check_collisions()

def draw():
    
    screen.blit("fondo", (0, 0))
    draw_player()
    draw_enemies()
    # ---------------------------
    # ✨ MOSTRAR VIDAS EN PANTALLA
    # ---------------------------
    screen.draw.text(
        f"Vidas: {game.lives}",
        topleft=(10, 10),
        fontsize=40,
        color="white"
    )
    if not game.running:
        screen.draw.text(
            "GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=80,
            color="red"
        )
    
def check_collisions():
    for e in enemies:
        if player.colliderect(e):
            game.lives -= 1
            print("Colisión! Vidas restantes:", game.lives)

            # Respawn enemigo
            e.pos = (1000, -100)

            # Si se quedaron sin vidas => perder
            if game.lives <= 0:
                game.running = False


pgzrun.go()
