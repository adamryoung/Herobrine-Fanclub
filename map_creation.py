import pygame as pg
import main


class new_grid:
    def __init__(self, mouse, screen, grid_size):
        self.mouse = mouse
        self.screen = screen
        self.grid_size = grid_size

    def grid(self):
        grid_array = [[0 for i in range(self.grid_size[0])] for j in range(self.grid_size[1])]

        rectangle_width = self.screen.get_size / self.grid_size[0]
        rectangle_height = self.screen.get_sizeq / self.grid_size[1]

        for i in range(len(grid_array)):
            for j in range(len(grid_array[i])):
                rectangle = (rectangle_width * i, rectangle_height * j, rectangle_width, rectangle_height)
                pg.draw.rect(self.screen, main.WHITE, rectangle)

        return grid_array


