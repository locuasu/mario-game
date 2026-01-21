from shop_data import SKINS

def draw_coleccion(screen, game):
    screen.clear()
    screen.draw.text("COLECCIÓN DE SKINS", center=(300, 50), fontsize=50, color="white")

    # Si no tiene skins compradas
    if not game.owned_skins:
        screen.draw.text("Aún no tienes skins compradas", center=(300, 200), fontsize=30, color="cyan")
        screen.draw.text("Ve a la tienda y compra una 😊", center=(300, 240), fontsize=26, color="white")
    else:
        y = 120
        for skin_name in game.owned_skins:
            # Si por alguna razón el nombre no existe en SKINS, lo saltamos
            if skin_name not in SKINS:
                continue

            # Texto a mostrar (puedes renombrar bonito)
            nombre_player = skin_name.upper()

            # Marcar la que está equipada
            texto = nombre_player
            if skin_name == game.current_skin:
                texto += "  ✅ (EQUIPADA)"

            screen.draw.text(
                texto,
                center=(300, y),
                fontsize=30,
                color="yellow" if skin_name == game.current_skin else "white"
            )
            y += 45

    # Botón volver
    screen.draw.text("VOLVER", center=(300, 380), fontsize=35, color="cyan")

def equip_skin(game, skin_name):
    skin = SKINS[skin_name]

    # Ya comprada → equipar
    if skin_name in game.owned_skins:
        game.current_skin = skin_name
        return

def coleccion_mouse_down(pos, game):
    x, y_click = pos
    if 200 < x < 400 and 360 < y_click < 410:
        game.state = "menu"
    y = 120
    for skin_name in game.owned_skins:
        if skin_name not in SKINS:
            continue
        if y - 20 < y_click < y + 20:
            game.current_skin = skin_name
            print("Skin equipada:", skin_name)
            return
        y += 45