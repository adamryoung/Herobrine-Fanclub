import pygame as pg
from math import pi, cos, sin
import numpy as np

filename = "map_layout.txt"
map_array = np.loadtxt(filename)
map_array = map_array.astype(int)
dimensions = np.shape(map_array)

pg.init()

pg.display.set_caption("Herobrine Fanclub")
icon = pg.image.load("assets/icon.jpg")
pg.display.set_icon(icon)
window_size = (800, 600)
x = 5  # range 0-dimensions[0]
y = 5  # range 0-dimensions[1]
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
        r += 2 * pi
    while r >= 2 * pi:
        r -= 2 * pi

    # Detect collisions
    pass


def ray_cast(x, y, r, map_array):
    step = abs(cos(r)) if abs(cos(r)) > abs(sin(r)) else abs(sin(r))
    dx = cos(r) / step
    dy = sin(r) / step
    x0, y0 = x, y
    # DDA until wall detected
    while not wall_test(x, y, map_array):
        x += dx
        y += dy
    return ((y - y0) ** 2 + (x - x0) ** 2) ** 0.5 # Return distance from wall.


def wall_test(x, y, map_array):
    # Returns true if (x, y) is in a wall, false otherwise.
    if map_array[round(y) - 1][round(x) - 1] == 1:
        return True
    return False

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    background(window_size)
    for r in [r - (pi / 4), r - (pi / 8), r, r + (pi / 8), r + (pi / 4)]:
        d = ray_cast(x, y, r, map_array)
        # Nolan: >>> using d (distance) and r as inputs display the appropriately sized / coloured wall slice here. <<<
    collision(x, y, r)
