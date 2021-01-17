import pygame as pg
import math

pg.init()

screen_size = (1000, 1000)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
grid_size = [10, 10]

screen = pg.display.set_mode(screen_size)
mouse = pg.mouse.get_pos()
screen.fill(WHITE)

rectangle_size = [screen_size[i] / grid_size[i] for i in range(2)]


def level_map():
    edited_level = map_edit(mouse, new_level)
    draw(edited_level, screen)


def map_edit(mouse, array):
    if pg.mouse.get_pressed(num_buttons=3)[0]:
        position = pg.mouse.get_pos()
        array_pos = [math.floor(position[i] / rectangle_size[i]) for i in range(2)]
        array[array_pos[0]][array_pos[1]] = 1
        return array
    elif pg.mouse.get_pressed(num_buttons=3)[2]:
        position = pg.mouse.get_pos()
        array_pos = [math.floor(position[i] / rectangle_size[i]) for i in range(2)]
        array[array_pos[0]][array_pos[1]] = 0
        return array
    else:
        return array


def draw(array, surface):
    for i in range(len(array)):
        for j in range(len(array[i])):
            rectangle = (rectangle_size[0] * i, rectangle_size[1] * j, rectangle_size[0], rectangle_size[1])
            if array[i][j] == 0:
                COLOUR = WHITE
            elif array[i][j] == 1:
                COLOUR = BLACK
            pg.draw.rect(surface, COLOUR, rectangle)


class create_grid:
    def __init__(self, grid):
        self.grid_size = grid

    def grid(self):
        grid_array = [[0 for i in range(self.grid_size[0])] for j in range(self.grid_size[1])]

        rectangle_width = screen_size[0] / self.grid_size[0]
        rectangle_height = screen_size[1] / self.grid_size[1]

        return grid_array


level = create_grid(grid_size)
new_level = level.grid()

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    level_map()
    pg.display.update()
