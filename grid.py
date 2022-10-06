from cell import Cell
import random, os

class Grid:
    # creates 2D list of Cell instances, of a user-defined size
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[Cell() for column in range(self.width)] for row in range(self.height)]

        self.generate()

    # NO LONGER USED -- prints the grid, pulling in the correct chars for each space
    def draw_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        for row in self.grid:
            for column in row:
                print(column.get_char(), end='')
            print()
    
    # randomly populates each grid space with either living or dead cells
    def generate(self):
        for row in self.grid:
            for column in row:
                if (random.randint(0,3)) == 1:
                    column.set_alive()

    # returns list of valid surrounding cells (i.e. those within bounds)
    def check_neighbours(self, check_row, check_column):
        check_min = -1
        check_max = 2

        neighbour_list = []

        # cycles through 3x3 grid surrounding cell, from -1 to 1 on both x & y axes
        for row in range(check_min, check_max):
            for column in range(check_min, check_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column

                # true unless changed to false
                valid_position = True

                # sets to False if grid[neighbour_row][neighbour_column] == inspected cell
                if (neighbour_row) == check_row and (neighbour_column) == check_column:
                    valid_position = False

                # sets to False is grid[neighbour_row][neighbour_column] would be out of bounds
                if (neighbour_row) < 0 or (neighbour_row) >= self.height:
                    valid_position = False
                if (neighbour_column) < 0 or (neighbour_column) >= self.width:
                    valid_position = False

                # appends if neighbour cell is within bounds, and not the inspected cell itself
                if valid_position:
                    neighbour_list.append(self.grid[neighbour_row][neighbour_column])
    
        return neighbour_list

    # updates grid state
    def update_grid(self):
        to_live = []
        to_die = []

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                # returns list of all neighbours
                check_neighbours = self.check_neighbours(row, column)

                living_count = []

                # appends all living neighbour cells to list
                for cell in check_neighbours:
                    if cell.is_alive():
                        living_count.append(cell)

                inspected_cell = self.grid[row][column]
            
                if inspected_cell.is_alive():
                    # if cell is alive and surrounded by more or less than 2-3 living cells, it dies...
                    if len(living_count) < 2 or len(living_count) > 3:
                        to_die.append(inspected_cell)
                    # ...otherwise, it survives
                    if len(living_count) == 3 or len(living_count) ==2:
                        to_live.append(inspected_cell)
                else:
                    # dead cells surrounded by exactly 3 living cells become alive
                    if len(living_count) == 3:
                        to_live.append(inspected_cell)

        # kills or makes alive the relevent cells
        for cell in to_live:
            cell.set_alive()

        for cell in to_die:
            cell.kill()