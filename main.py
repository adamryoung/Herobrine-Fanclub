import pygame as pg
import map_creation

pg.init()

screen_size = (1000, 1000)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def level_map():
    screen = pg.display.set_mode(screen_size)
    mouse = pg.mouse.get_pos()
    screen.fill(WHITE)

    level = map_creation.new_grid(mouse, screen)
    level.grid([20, 20])


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    level_map()
    pg.display.flip()
