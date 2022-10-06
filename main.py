#! /usr/bin/env python3

from grid import Grid
import time, os, pygame

def main():
    pygame.init()

    #gets grid size from user
    user_height = int(input('Height: '))
    user_width = int(input('Width: '))
    SCREEN_HEIGHT = user_height * 10
    SCREEN_WIDTH = user_width * 10

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Game O\' Life')
    
    # creates and prints initial grid state
    grid = Grid(user_height, user_width)

    # defines cell 'pixel' to be drawn where cells are living
    living_cell = pygame.Surface((10, 10))
    living_cell.fill((0, 0, 0))

    running = True
    while running:
        # creates white screen background
        screen.fill((255, 255, 255))

        # function to print cells
        print_cells(living_cell, screen, grid)
        
        time.sleep(1)
        grid.update_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


# prints 10 x 10 cells at position of living cell * 10
def print_cells(cell, screen, grid):
    for line in range(grid.height):
        for column in range(grid.width):
            if grid.grid[line][column].is_alive():
                screen.blit(cell, (column * 10, line * 10))
    pygame.display.flip()



main()