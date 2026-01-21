from config import WIDTH, HEIGHT 
from pgzero.rect import Rect

MENU_OPTIONS = ["Jugar", "Tienda", "Colección"]
option_rects = []

def update_menu(game):
    pass  # el menú con mouse no necesita update continuo

def draw_menu(screen):
    screen.clear()
    screen.blit("fondo2", (0, 0))
    option_rects.clear()
    screen.draw.text(
        "Mario Game",
        center=(WIDTH // 2, 100),
        fontsize=80,
        color="red"
    )
    for i, option in enumerate(MENU_OPTIONS):
            x = WIDTH // 2
            y = 250 + i * 70

            rect = Rect((x - 150, y - 30), (300, 60))
            option_rects.append(rect)

            # Hover con mouse
            color = "yellow"

            screen.draw.text(
                option,
                center=(x, y),
                fontsize=50,
                color=color
            )  
def on_mouse_down(pos, button, game):
    for i, rect in enumerate(option_rects):
        if rect.collidepoint(pos):
            if i == 0:
                game.state = "game"
            elif i == 1:
                game.state = "shop"
            elif i == 2:
                game.state = "coleccion"




























