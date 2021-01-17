import pygame as pg

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


def ray_cast(x, y, r):
    fov = 90




running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    background(window_size)
    ray_cast(x, y, r)
