# Grid utilities
# 15 April 2024

def create_grid(grid):
    """create a 4x4 array of zeroes within grid"""
    for i in range(4):
        for j in range(4):
            grid[i][j] = 0

    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")

    for i in range(4):
        row = "|"

        for j in range(4):
            if grid[i][j] != 0:
                row += "{:<5}".format(grid[i][j])
            else:
                row += "{:<5}".format(" ")

        print(row+"|")

    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and there are no
    adjacent values that are equal; otherwise False"""

    # Flags for cases the presence of zero or equal adjacent values
    zero_presence = False
    equal_adjacent = False

    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                zero_presence = True
                break

            # Check for adjacent equal values
            if ((j - 1 > 0) and (grid[i][j - 1] == grid[i][j])) or ((j + 1 < 4) and (grid[i][j + 1] == grid[i][j])):
                equal_adjacent = True
                break
            elif ((i - 1 > 0) and (grid[i - 1][j] == grid[i][j])) or ((i + 1 < 4) and (grid[i + 1][j] == grid[i][j])):
                equal_adjacent = True
                break

    if not zero_presence and not equal_adjacent:
        return True
    return False

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise
    False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the given grid"""
    copy = [0, 0, 0, 0]
    for i in range(4):
        copy[i] = grid[i][:]
    return copy
    
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True
