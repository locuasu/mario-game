#  main.py
import pgzrun
from config import WIDTH, HEIGHT, STAR_TIME, POINTS_COLLECT_STAR, POINTS_KILL_ENEMY
from player import player, update_player, draw_player, keyboard
from enemies import enemies, update_enemies, draw_enemies
from star import star, draw_star, respawn_star, update_star
from game_state import GameState
from score_system import add_score
from menu import draw_menu, update_menu, on_mouse_down as menu_mouse_down
from shop import draw_shop, shop_mouse_down
from coleccion import draw_coleccion, coleccion_mouse_down
from bullet import shoot, update_bullets, draw_bullets

game = GameState()

def disable_star():
    game.invincible = False
    print("ivencibilidad acabada:(")
def update():
    global shoot_cooldown
    if game.state == "menu":
        update_menu(game)
        return

    if game.state != "game":
        return
    

    update_player(game)
    # 🔫 DISPARO
    if game.can_shoot:
        if game.shoot_cooldown > 0:
            game.shoot_cooldown  -= 1
        elif keyboard.space:
            shoot(player)
            game.shoot_cooldown  = 15  # frames entre disparos
    update_enemies()
    update_star()
    update_bullets()
    check_collisions()

    if star.visible and player.colliderect(star):
        star.visible = False
        game.invincible = True
        add_score(game, POINTS_COLLECT_STAR)
        clock.schedule_unique(disable_star, STAR_TIME)  

def draw():
    if game.state == "menu":
        draw_menu(screen)
        return
    if game.state == "shop":
        draw_shop(screen, game)
        return
    
    elif game.state == "coleccion":
        draw_coleccion(screen, game)
        return
    if game.state == "game":

        screen.blit("fondo", (0, 0))
        draw_player()
        draw_enemies()
        draw_star()
        draw_bullets()
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
    if game.state == "game_over":
        screen.clear()
        screen.draw.text(
            "GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=80,
            color="red"
        )
        screen.draw.text(
            f"Score final: {game.score}",
            center=(WIDTH // 2, HEIGHT // 2 + 30),
            fontsize=50,
            color="white"
        )
        screen.draw.text(
            "Click para volver al menú",
            center=(WIDTH // 2, HEIGHT // 2 + 100),
            fontsize=40,
            color="yellow"
        )
from bullet import bullets 
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
                game.state = "game_over"
    # 🔫 bala vs enemigo
    for bullet in bullets[:]:
        for e in enemies:
            if bullet.colliderect(e):
                bullets.remove(bullet)
                e.pos = (1000, -100)
                add_score(game, POINTS_KILL_ENEMY)
                break

def on_mouse_down(pos, button):
    if game.state == "menu":
        menu_mouse_down(pos, button, game)

    elif game.state == "shop":
        shop_mouse_down(pos, game)

    elif game.state == "coleccion":
        coleccion_mouse_down(pos, game)
    elif game.state == "game_over":
        respawn_game()
        game.state = "menu"
        

 
def respawn_game():
    game.state = "game"
    game.lives = 3
    game.invincible= False
    respawn_star()
    game.can_shoot = False
    game.shoot_cooldown = 0

pgzrun.go()
