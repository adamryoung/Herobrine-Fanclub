import pygame as pg
from math import pi, cos, sin
import numpy as np

filename = "map_layout.txt"
map_array = np.loadtxt(filename)
map_array = map_array.astype(int)
print(map_array)
dimensions = np.shape(map_array)

pg.init()

pg.display.set_caption("Herobrine Fanclub")
icon = pg.image.load("assets/icon.jpg")
pg.display.set_icon(icon)
window_size = (800, 600)
x = 10  # range 0-dimensions[0]
y = 10  # range 0-dimensions[1]
r = 0
sensitivity = pi / 64
velocity = 0.3
win = pg.display.set_mode(window_size)

BLACK = (0, 0, 0)
WHITE =(255, 255, 255)

def background(window_size):
    pg.time.delay(100)
    width, height = window_size
    CEILING = pg.Color("#f64d12")
    FLOOR = pg.Color("#444141")
    pg.draw.rect(win, CEILING, (0, 0, width, height / 2))
    pg.draw.rect(win, FLOOR, (0, height / 2, width, height / 2))
    pg.display.update()


def ray_cast(x, y, rad, map_array):
    step = abs(cos(rad)) if abs(cos(rad)) > abs(sin(rad)) else abs(sin(rad))
    dx = cos(rad) / step
    dy = sin(rad) / step
    x0, y0 = x, y
    # DDA until wall detected
    while not wall_test(x, y, map_array):
        x += dx
        y += dy
    return ((y - y0) ** 2 + (x - x0) ** 2) ** 0.5  # Return distance from wall.


def wall_test(x, y, map_array):
    # Returns true if (x, y) is in a wall, false otherwise.
    if map_array[round(y) - 1][round(x) - 1] == 1:
        return True
    return False


def collision(x, y, r, map_array):
    # Keep r within bounds
    while r < 0:
        r += 2 * pi
    while r >= 2 * pi:
        r -= 2 * pi

    # Detect collisions
    if 'x0' not in locals():
        x0, y0 = None, None
    if wall_test(x, y, map_array):
        x, y = x0, y0
    x0, y0 = x, y


def render(screen, dis):
    length = len(dis)
    midline = window_size[1] / 2
    col_width = window_size[0] / length
    h = 2000
    for i in range(length):
        line_height = h / dis[i]
        half_height = line_height / 2
        rectangle_specs = (col_width * i, midline - half_height, col_width, line_height)
        col_val = dis[i] * 10
        if col_val >= 255:
            col_val = 255
        colour = (col_val, col_val, col_val)
        pg.draw.rect(screen, colour, rectangle_specs)


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.time.delay(100)
    background(window_size)
    d = []
    amount = range(-100, 100)
    subdivisions = [r - ((pi / 4) / len(amount) * i) for i in amount]
    for r1 in subdivisions:
        d.append(ray_cast(x, y, r1, map_array))

    collision(x, y, r, map_array)
    render(win, d)
    pg.display.update()


    keys = pg.key.get_pressed()

    if keys[pg.K_a]:
        r += sensitivity
    if keys[pg.K_d]:
        r -= sensitivity
    if keys[pg.K_w]:
        y += sin(r) * velocity
        x += cos(r) * velocity
    if keys[pg.K_s]:
        y -= sin(r) * velocity
        x -= cos(r) * velocity
