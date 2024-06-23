import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows=10
        self.num_cols=10
        self.cell_size=20
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors() 
    def Map(self):
        return tuple(self.grid)

    def Set(self, grid):
        max_col = 0
        num_row = 0
        num_col = 0
        for num_row,row in enumerate(grid):
            for num_col,item in enumerate(row):
                if max_col < num_col:
                    max_col = num_col
        self.num_rows = num_row + 1;
        self.num_cols = max_col + 1;
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

        for num_row,row in enumerate(grid):
            for num_col,item in enumerate(row):
                self.grid[num_row][num_col] = item

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                        column * self.cell_size + 11, 
                        row * self.cell_size + 11,
                        self.cell_size - 1,
                        self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
    

