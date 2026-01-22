from pgzero.actor import Actor

bullets = []

def shoot(player):
    bullet = Actor("bala")
    bullet.pos = player.pos
    bullets.append(bullet)

def update_bullets():
    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

def draw_bullets():
    for bullet in bullets:
        bullet.draw()