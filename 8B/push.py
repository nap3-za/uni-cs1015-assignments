# 2048 Game
# 20 April 2024

import util

def push_up (grid):
    """merge grid values upwards"""
    for c in range(4):
        while True:
            shifted = False
            last_filled_row = -1 if grid[0][c] == 0 else 0

            for r in range(4):
                if grid[r][c] != 0:
                    if r-1 >= 0 and grid[r-1][c] == 0: # Cell with a previous zero
                        grid[last_filled_row+1][c] = grid[r][c]
                        grid[r][c] = 0
                        last_filled_row += 1

                        shifted = True

                    elif r-1 >= 0 and grid[r-1][c] != 0: # Non-zero Previous, shift last_filed
                        last_filled_row = r

            if not shifted: # If there wasn't any summation or only moving happened
                break

        for r in range(1, 4):  # Sum every adjacent number and perform shifts
            if grid[r][c] != 0:
                if grid[r][c] == grid[r-1][c]:
                    grid[r-1][c] = grid[r][c] * 2
                    grid[r][c] = 0

                elif grid[r-1][c] == 0:
                    grid[r-1][c] = grid[r][c]
                    grid[r][c] = 0


def push_down (grid):
    """merge grid values downwards"""
    for c in range(3, -1, -1):
        while True:
            shifted = False
            last_filled_row = 4 if grid[3][c] == 0 else 3

            for r in range(3, -1, -1):
                if grid[r][c] != 0:
                    if r+1 <= 3 and grid[r+1][c] == 0: # Cell with a previous zero
                        grid[last_filled_row-1][c] = grid[r][c]
                        grid[r][c] = 0
                        last_filled_row -= 1

                        shifted = True

                    elif r+1 <= 3 and grid[r+1][c] != 0: # Non-zero Previous, shift last_filed
                        last_filled_row = r

            if not shifted: # If there wasn't any summation or only moving happened
                break

        for r in range(2, -1, -1): # Sum every adjacent number and perform shifts
            if grid[r][c] != 0:
                if grid[r][c] == grid[r+1][c]:
                    grid[r+1][c] = grid[r][c] * 2
                    grid[r][c] = 0
                    
                elif grid[r+1][c] == 0:
                    grid[r+1][c] = grid[r][c]
                    grid[r][c] = 0


def push_left (grid):
    """merge grid values left"""
    for r in range(4):
        while True:
            shifted = False
            last_filled_col = -1 if grid[r][0] == 0 else 0

            for c in range(4):
                if grid[r][c] != 0:
                    if c-1 >= 0 and grid[r][c-1] == 0: # Cell with a previous zero
                        grid[r][last_filled_col+1] = grid[r][c]
                        grid[r][c] = 0
                        last_filled_col += 1

                        shifted = True

                    elif c-1 >= 0 and grid[r][c-1] != 0: # Non-zero Previous, shift last_filed
                        last_filled_col = c

            if not shifted: # If there wasn't any summation or only moving happened
                break

        for c in range(1, 4): # Sum every adjacent number and perform shifts
            if grid[r][c] != 0:
                if grid[r][c] == grid[r][c-1]:
                    grid[r][c-1] = grid[r][c] * 2
                    grid[r][c] = 0

                elif grid[r][c-1] == 0:
                    grid[r][c-1] = grid[r][c]
                    grid[r][c] = 0



def push_right (grid):
    """merge grid values right"""
    for r in range(3, -1, -1):
        while True:
            shifted = False
            last_filled_col = 4 if grid[r][3] == 0 else 3

            for c in range(3, -1, -1):
                if grid[r][c] != 0:
                    if c+1 <= 3 and grid[r][c+1] == 0: # Cell with a previous zero
                        grid[r][last_filled_col-1] = grid[r][c]
                        grid[r][c] = 0
                        last_filled_col -= 1

                        shifted = True

                    elif c+1 <= 3 and grid[r][c+1] != 0: # Non-zero Previous, shift last_filed
                        last_filled_col = c

            if not shifted: # If there wasn't any summation or only moving happened
                break

        for c in range(2, -1, -1): # Sum every adjacent number and perform shifts
            if grid[r][c] != 0:
                if grid[r][c] == grid[r][c+1]:
                    grid[r][c+1] = grid[r][c] * 2
                    grid[r][c] = 0

                elif grid[r][c+1] == 0:
                    grid[r][c+1] = grid[r][c]
                    grid[r][c] = 0

