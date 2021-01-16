import pygame as pg

pg.init()

screen_size = (1000, 1000)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
grid_size = [20, 20]


def level_map():
    screen = pg.display.set_mode(screen_size)
    mouse = pg.mouse.get_pos()
    screen.fill(WHITE)

    level = create_grid(mouse, screen, grid_size)
    new_level = level.grid()


class create_grid:
    def __init__(self, mouse, screen, grid):
        self.mouse = mouse
        self.screen = screen
        self.grid_size = grid

    def grid(self):
        grid_array = [[0 for i in range(self.grid_size[0])] for j in range(self.grid_size[1])]

        rectangle_width = screen_size[0] / self.grid_size[0]
        rectangle_height = screen_size[1] / self.grid_size[1]

        for i in range(len(grid_array)):
            for j in range(len(grid_array[i])):
                rectangle = (rectangle_width * i, rectangle_height * j, rectangle_width, rectangle_height)
                pg.draw.rect(self.screen, BLACK, rectangle, 1)

        return grid_array


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    level_map()
