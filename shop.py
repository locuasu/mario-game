from shop_data import SKINS, ITEMS
from pgzero.actor import Actor
from config import WIDTH, HEIGHT

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
    screen.blit("fondo_2", (0, 0))
    center_x = WIDTH // 2
    y = 120
    spacing = 40

    # 🏪 TÍTULO
    screen.draw.text(
        "TIENDA",
        center=(center_x, 50),
        fontsize=50,
        color="white"
    )

    # 💰 PUNTOS
    screen.draw.text(
        f"Puntos: {game.score}",
        center=(center_x, 95),
        fontsize=35,
        color="cyan"
    )

    # 🎭 SKINS
    for skin_name in SKINS:
        skin = SKINS[skin_name]
        text = f"{skin_name} - {skin['price']} pts"

        if skin_name in game.owned_skins:
            text += " (COMPRADA)"

        screen.draw.text(
            text,
            center=(center_x, y),
            fontsize=30,
            color="yellow" if skin_name == game.current_skin else "white"
        )
        y += spacing

    # ────────────────
    # 🧡 VIDA EXTRA
    # ────────────────
    y += 20
    item = ITEMS["vida_extra"]

    screen.draw.text(
        f"VIDA EXTRA +1 - {item['price']} pts",
        center=(center_x, y),
        fontsize=35,
        color="red"
    )

    # ────────────────
    # 🔫 BALA
    # ────────────────
    bala_x = center_x 
    bala_y = y + 70

    bala_actor.pos = (bala_x, bala_y)
    bala_actor.draw()

    screen.draw.text(
        "DISPARO",
        center=(bala_x, bala_y + 35),
        fontsize=25,
        color="yellow"
    )

    # 🔙 VOLVER
    screen.draw.text(
        "VOLVER AL MENÚ",
        center=(center_x, HEIGHT - 50),
        fontsize=35,
        color="cyan"
    )

def shop_mouse_down(pos, game):
    mx, my = pos

    center_x = WIDTH // 2
    y = 120
    spacing = 40

    # 🔙 VOLVER
    if HEIGHT - 70 < my < HEIGHT - 30:
        game.state = "menu"
        return

    # 🎭 SKINS
    for skin_name in SKINS:
        if y - 20 < my < y + 20:
            buy_skin(game, skin_name)
            return
        y += spacing

    # 🧡 VIDA EXTRA
    y += 20
    if center_x - 150 < mx < center_x + 150 and y - 25 < my < y + 25:
        buy_item(game, "vida_extra")
        return

    # 🔫 BALA
    bala_x = center_x 
    bala_y = y + 70

    if bala_x - 20 < mx < bala_x + 20 and bala_y - 20 < my < bala_y + 20:
        buy_item(game, "bala")
        return



















