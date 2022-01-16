"""Module for working with playing field"""

import pygame
import numpy as np
from cell import Cell


class GameField:

    def __init__(self, background_color = (30, 125, 125),
                width = 100, height = 50, field = None):
        self.background_color = background_color
        self.width = width
        self.height = height
        if field is None:
            self.field = np.zeros((self.height, self.width), dtype = np.int8)
        else:
            self.field = field

    def __str__(self):
        return  f"""
        Game field height: {self.height}
        Game field width: {self.width}
        Game field background color (r, g, b): {self.background_color}
        """

    def get_info_about_game_field(self):
        """Print the information about the game field"""
        print(str(self))

    def draw_field_with_cells(self, visual_field, cell = Cell()):
        """Drawing cells and background"""
        y_field = 0
        for row in self.field:
            x_field = 0
            for is_cell_live in row:
                if is_cell_live == 1:
                    pygame.draw.rect(visual_field, cell.cell_color, (x_field * cell.thickness, y_field * cell.thickness, cell.thickness, cell.thickness))
                else:
                    pygame.draw.rect(visual_field, self.background_color, (x_field * cell.thickness, y_field * cell.thickness, cell.thickness, cell.thickness))
                x_field += 1
            y_field += 1

    def create_field(self):
        """The main method for creating a playing field"""
        pygame.init()
        pygame.display.set_caption(
            'THE GAME "Life"\
            Use "ESC" to exit\
            Use "r" to set a random field\
            Use "backspace" to clean up the field\
            Use "right arrow" to produce only one generation')
        visual_field = pygame.display.set_mode((1200, 600))
        return visual_field
    
    def cell_clicked(self, pixel = (0, 0), cell = Cell()):
        """Method for cell value reversal"""
        x_field = pixel[0] // cell.thickness
        y_field = pixel[1] // cell.thickness
        if cell.in_field(self.height, self.width):
            self.field[y_field][x_field] ^= 1   # Looks like magic, but it simply changes 1 -> 0 or 0 -> 1
        else:
            print("Error when selecting a cell")
    
    def update_field(self):
        """Method for updating to the next generation"""
        new_field = np.zeros((self.height, self.width), dtype = np.int8)

        for y_field, row in enumerate(self.field):
            for x_field, is_cell_live in enumerate(row):
                cell = Cell(y_field, x_field, is_cell_live)
                counter_of_neighbours = -self.field[cell.y_in_field][cell.x_in_field]
                for potential_alive_neighbour_x in range(cell.x_in_field - 1, cell.x_in_field + 2):
                    for potential_alive_neighbour_y in range(cell.y_in_field - 1, cell.y_in_field + 2):
                        """
                        The infinity of the field is implemented in such a way
                        that it is possible to pass to the other end of the map
                        if the boundaries of the field intersect
                        with one of the sides
                        """
                        counter_of_neighbours += self.field[potential_alive_neighbour_y % self.height][potential_alive_neighbour_x % self.width]
                if cell.status_in_next_generation(counter_of_neighbours):
                    new_field[cell.y_in_field][cell.x_in_field] = 1
        self.field = new_field

    def clean_field(self):
        self.field = np.zeros((self.height, self.width), dtype = np.int8)
    
    def set_random_field(self):
        new_field = np.random.randint(2, size=(self.height, self.width), dtype = np.int8)
        self.field = new_field