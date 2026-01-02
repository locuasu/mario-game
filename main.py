#  main.py
import pgzrun
from config import WIDTH, HEIGHT, STAR_TIME, POINTS_COLLECT_STAR, POINTS_KILL_ENEMY
from player import player, update_player, draw_player, keyboard
from enemies import enemies, update_enemies, draw_enemies
from star import star, draw_star, respawn_star, update_star
from game_state import GameState
from score_system import add_score
game = GameState()

def disable_star():
    game.invincible = False
    print("ivencibilidad acabada:(")
def update():
    if not game.running:
        if keyboard.space:
            respawn_game()
        return   # ← DETIENE TODO EL JUEGO
    update_player()
    update_enemies()
    update_star()
    check_collisions()
    if star.visible and player.colliderect(star):
        star.visible = False
        game.invincible = True
        add_score(game, POINTS_COLLECT_STAR)
        clock.schedule_unique(disable_star, STAR_TIME)    

def draw():
    
    screen.blit("fondo", (0, 0))
    draw_player()
    draw_enemies()
    draw_star()
    # ---------------------------
    # ✨ MOSTRAR VIDAS EN PANTALLA
    # ---------------------------
    screen.draw.text(
        f"Vidas: {game.lives}",
        topleft=(10, 10),
        fontsize=40,
        color="white"
    )
    screen.draw.text(
        f"score: {game.score}",
        topright=(WIDTH - 10, 10),
        fontsize=40,
        color="cyan"
    )
    if game.invincible:
        screen.draw.text(
            "INVENCIBLE",
            center=(WIDTH // 2,50),
            fontsize=40,
            color="yellow"
        )
    if not game.running:
        screen.draw.text(
            "GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=80,
            color="red"
        )
        screen.draw.text(
            "presiona espacio para continuar",
            center=(WIDTH // 2, HEIGHT // 1.5),
            fontsize=60,
            color="white"
        )
    
def check_collisions():
    for e in enemies:
        if player.colliderect(e):
            if game.invincible:
                # Respawn enemigo
                e.pos = (1000, -100)
                add_score(game, POINTS_KILL_ENEMY)
                return
            game.lives -= 1
            print("Colisión! Vidas restantes:", game.lives)

            # Respawn enemigo
            e.pos = (1000, -100)

            # Si se quedaron sin vidas => perder
            if game.lives <= 0:
                game.running = False
            
                
def respawn_game():
    game.lives = 3
    game.running = True
    game.invincible= False
    respawn_star()
    game.score = 0

pgzrun.go()
