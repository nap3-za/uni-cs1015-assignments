# 2048 Game
# 18 April 2024

import util

def push_up (grid):
    """merge grid values upwards"""

    for c in range(4):
        while True:
            shifted = False
            last_filled_row = -1

            for r in range(4):
                if grid[r][c] != 0:

                    # Cell equal to next cell, shift & sum
                    if r < 3 and grid[r][c] == grid[r+1][c]:
                        grid[r][c] = grid[r][c] * 2
                        grid[r+1][c] = 0
                        last_filled_row = r

                        shifted = True

                    # Cell with a previous zero
                    elif r-1 >= 0 and grid[r-1][c] == 0:
                        grid[last_filled_row+1][c] = grid[r][c]
                        grid[r][c] = 0
                        last_filled_row += 1

                        shifted = True

                    # Non-zero Previous, shift last_filed
                    elif r-1 >= 0 and grid[r-1][c] != 0:
                        last_filled_row = r

                    # Cell is the start, shift last_filled
                    elif r-1 == -1:
                        last_filled_row = 0

            # If there wasn't any summation or only moving happened
            if not shifted:
                break


def push_down (grid):
    """merge grid values downwards"""

    for c in range(3, -1, -1):
        while True:
            shifted = False
            last_filled_row = 4

            for r in range(3, -1, -1):
                if grid[r][c] != 0:

                    # Cell equal to next cell, shift & sum
                    if r > 0 and grid[r][c] == grid[r-1][c]:
                        grid[r][c] = grid[r][c] * 2
                        grid[r-1][c] = 0
                        last_filled_row = r

                        shifted = True

                    # Cell with a previous zero
                    elif r+1 <= 3 and grid[r+1][c] == 0:
                        grid[last_filled_row-1][c] = grid[r][c]
                        grid[r][c] = 0
                        last_filled_row -= 1

                        shifted = True

                    # Non-zero Previous, shift last_filed
                    elif r+1 <= 3 and grid[r+1][c] != 0:
                        last_filled_row = r

                    # Cell is the start, shift last_filled
                    elif r == 3:
                        last_filled_row = 3

            # If there wasn't any summation or only moving happened
            if not shifted:
                break


def push_left (grid):
    """merge grid values left"""

    for r in range(4):
        while True:
            shifted = False
            last_filled_col = -1

            for c in range(4):
                if grid[r][c] != 0:

                    # Cell equal to next cell, shift & sum
                    if c < 3 and grid[r][c] == grid[r][c+1]:
                        grid[r][c] = grid[r][c] * 2
                        grid[r][c+1] = 0
                        last_filled_col = c

                        shifted = True

                    # Cell with a previous zero
                    elif c-1 >= 0 and grid[r][c-1] == 0:
                        print(grid[r][c], ":cells:", grid[r][c-1])
                        print(r, ":", last_filled_col)
                        grid[r][last_filled_col+1] = grid[r][c]
                        grid[r][c] = 0
                        last_filled_col += 1

                        shifted = True

                    # Non-zero Previous, shift last_filed
                    elif c-1 >= 0 and grid[r][c-1] != 0:
                        last_filled_col = c

                    # Cell is the start, shift last_filled
                    elif c == 0:
                        last_filled_col = 0

            # If there wasn't any summation or only moving happened
            if not shifted:
                break

grid = [[0, 0, 2, 0], [0, 0, 64, 2], [0, 8, 8, 16], [0, 2, 2, 8]]
push_left(grid)
util.print_grid(grid)


def push_right (grid):
    """merge grid values right"""

    for r in range(3, -1, -1):
        while True:
            shifted = False
            last_filled_col = 4

            for c in range(3, -1, -1):
                if grid[r][c] != 0:

                    # Cell equal to next cell, shift & sum
                    if c > 0 and grid[r][c] == grid[r][c-1]:
                        grid[r][c] = grid[r][c] * 2
                        grid[r][c-1] = 0
                        last_filled_col = c

                        shifted = True

                    # Cell with a previous zero
                    elif c+1 <= 3 and grid[r][c+1] == 0:
                        grid[r][last_filled_col-1] = grid[r][c]
                        grid[r][c] = 0
                        last_filled_col -= 1

                        shifted = True

                    # Non-zero Previous, shift last_filed
                    elif c+1 <= 3 and grid[r][c+1] != 0:
                        last_filled_col = c

                    # Cell is the start, shift last_filled
                    elif c == 3:
                        last_filled_col = 3

            # If there wasn't any summation or only moving happened
            if not shifted:
                break

