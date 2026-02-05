from shop_data import SKINS
from config import WIDTH, HEIGHT

def draw_coleccion(screen, game):
    screen.clear()
    screen.blit("fondo_1", (0, 0))
    center_x = WIDTH // 2
    start_y = 120
    spacing = 45

    # Si no tiene skins
    if not game.owned_skins:
        screen.draw.text(
            "Aún no tienes skins compradas",
            center=(center_x, HEIGHT // 2),
            fontsize=30,
            color="cyan"
        )
        screen.draw.text(
            "Ve a la tienda y compra una 😊",
            center=(center_x, HEIGHT // 2 + 40),
            fontsize=26,
            color="white"
        )
    else:
        y = start_y
        for skin_name in game.owned_skins:
            if skin_name not in SKINS:
                continue

            texto = skin_name.upper()
            if skin_name == game.current_skin:
                texto += "  ✅ (EQUIPADA)"

            screen.draw.text(
                texto,
                center=(center_x, y),
                fontsize=30,
                color="yellow" if skin_name == game.current_skin else "white"
            )
            y += spacing

    # Botón volver (abajo, centrado)
    screen.draw.text(
        "VOLVER",
        center=(center_x, HEIGHT - 50),
        fontsize=35,
        color="black"
    )

def equip_skin(game, skin_name):
    skin = SKINS[skin_name]

    # Ya comprada → equipar
    if skin_name in game.owned_skins:
        game.current_skin = skin_name
        return

def coleccion_mouse_down(pos, game):
    x, y_click = pos
    center_x = WIDTH // 2
    start_y = 120
    spacing = 45

    # VOLVER
    if center_x - 100 < x < center_x + 100 and HEIGHT - 70 < y_click < HEIGHT - 30:
        game.state = "menu"
        return

    # Seleccionar skin
    y = start_y
    for skin_name in game.owned_skins:
        if skin_name not in SKINS:
            continue

        if y - 20 < y_click < y + 20:
            game.current_skin = skin_name
            print("Skin equipada:", skin_name)
            return

        y += spacing