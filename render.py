import pygame as pg
from math import pi, cos, sin
import numpy as np

filename = "map_layout.txt"
map_array = np.loadtxt(filename)
map_array = map_array.astype(int)

pg.init()

pg.display.set_caption("Herobrine Fanclub")
icon = pg.image.load("assets/icon.jpg")
pg.display.set_icon(icon)
window_size = (800, 600)
x = 500
y = 500
r = pi / 4


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
        r += 2 * pi
    while r >= 2 * pi:
        r - + 2 * pi

    # Detect collisions
    pass


def ray_cast(x, y, r):
    step = abs(cos(r)) if abs(cos(r)) > abs(sin(r)) else abs(sin(r))
    dx = cos(r) / step
    dy = sin(r) / step
    # DDA until wall detected
    wall = False
    while wall == False:
        x += dx
        y += dy
        print('x = %s, y = %s' % (x, y), dx, dy)
    if None:
        wall = True


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    background(window_size)
    ray_cast(x, y, r)
    collision(x, y, r)
