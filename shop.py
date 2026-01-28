from shop_data import SKINS, ITEMS
from pgzero.actor import Actor


bala_actor = Actor("bala", pos=(550, 340))
def buy_skin(game, skin_name):
    skin = SKINS[skin_name]

    # Ya comprada → equipar
    if skin_name in game.owned_skins:
        game.current_skin = skin_name
        return

    # Comprar
    if game.score >= skin["price"]:
        game.score -= skin["price"]
        game.owned_skins.append(skin_name)
        game.current_skin = skin_name
def buy_item(game, item_name):
    item = ITEMS[item_name]

    if game.score < item["price"]:
        return

    game.score -= item["price"]

    if item_name == "vida_extra":
        game.lives += 1

    elif item_name == "bala":
        game.can_shoot = True

def draw_shop(screen, game):
    screen.clear()
    screen.draw.text("TIENDA DE SKINS", center=(300, 50), fontsize=50, color="white")
    screen.draw.text(
        "Puntos: " + str(game.score),
        center =(300, 100),
        fontsize=35,
        color="cyan"
    
    )
    
    y = 120
    for skin_name in SKINS:
        skin = SKINS[skin_name]

        text = skin_name + " - " + str(skin["price"]) + " pts"

        if skin_name in game.owned_skins:
            text += " (COMPRADA)"

        screen.draw.text(
            text,
            center=(300, y),
            fontsize=30,
            color="yellow" if skin_name == game.current_skin else "white"
        )
        y += 50
    # ────────────────
    # 🧡 VIDA EXTRA
    # ────────────────
    y += 30
    item = ITEMS["vida_extra"]

    screen.draw.text(
        "VIDA EXTRA +1 - " + str(item["price"]) + " pts",
        center=(300, y),
        fontsize=35,
        color="red"
    )
      # 🔫 BALA
    bala_actor.draw()
    screen.draw.text(
        "DISPARO",
        center=(550, 370),
        fontsize=25,
        color="yellow"
    )  
    screen.draw.text(
        "Click para comprar / equipar",
        center=(300, 450),
        fontsize=30,
        color="cyan"
    )
    # 🔙 BOTÓN VOLVER
    screen.draw.text(
        "VOLVER AL MENÚ",
        center=(300, 420),
        fontsize=35,
        color="cyan"
    )

def shop_mouse_down(pos, game):
    mx, my = pos

    # 🔙 VOLVER AL MENÚ
    if 400 < my < 450:
        game.state = "menu"
        return

    # 🎭 SKINS
    y = 120
    for skin_name in SKINS:
        if y - 15 < my < y + 15:
            buy_skin(game, skin_name)
            return
        y += 50

    # 🧡 VIDA EXTRA
    y += 40
    if 260 < mx < 340 and y - 20 < my < y + 20:
        buy_item(game, "vida_extra")
        return

    # 🔫 DISPARO (BALA)
    if 520 < mx < 580 and 320 < my < 360:
        buy_item(game, "bala")
        return



















