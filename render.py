import pygame as pg
from math import pi


pg.init()

pg.display.set_caption("Herobrine Fanclub")
icon = pg.image.load("assets/icon.jpg")
pg.display.set_icon(icon)
window_size = (800, 600)
x = 500
y = 500
r = 0

def background(window_size):
    pg.time.delay(100)
    width, height = window_size
    win = pg.display.set_mode(window_size)
    CEILING = pg.Color("#f64d12")
    FLOOR = pg.Color("#444141")
    pg.draw.rect(win, CEILING, (0, 0, width, height / 2))
    pg.draw.rect(win, FLOOR, (0, height / 2, width, height / 2))
    pg.display.update()


def collision(x, y, r):
    # Keep r within bounds
    while r < 0:
        r += 2*pi
    while r >= 2*pi:
        r -+ 2*pi
    
    # Detect collisions
    pass


def ray_cast(x, y, r):
    



running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    background(window_size)
    ray_cast(x, y, r)
    collision(x, y, r)
