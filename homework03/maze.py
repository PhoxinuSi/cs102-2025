from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """
    x, y = coord
    direction = choice(["up", "right"])
    if direction == "up":
        if x - 1 > 0:
            grid[x - 1][y] = " "
        elif y + 2 < len(grid[0]):
            grid[x][y + 1] = " "
    else:
        if y + 2 < len(grid[0]):
            grid[x][y + 1] = " "
        elif x - 1 > 0:
            grid[x - 1][y] = " "

    return grid


def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

    for x, y in empty_cells:
        remove_wall(grid, (x, y))

    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param grid:
    :return:
    """
    exits = []
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == "X":
                exits.append((x, y))
    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    fl = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == k:
                for elem in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    move_x, move_y = elem
                    if 0 <= move_x < len(grid) and 0 <= move_y < len(grid[0]):
                        if grid[move_x][move_y] == 0:
                            grid[move_x][move_y] = k + 1

    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    x, y = exit_coord
    k = int(grid[x][y])
    path = [(x, y)]
    while grid[x][y] != 1:
        local = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for el in local:
            if 0 <= el[0] < len(grid) and 0 <= el[1] < len(grid[0]):
                if grid[el[0]][el[1]] == k - 1:
                    k -= 1
                    path.append((el[0], el[1]))
                    x, y = el[0], el[1]
                    break
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """

    x, y = coord
    if (x == 0 and y == 0) or (x == len(grid) - 1 and y == 0) or (x == 0 and y == len(grid[0]) - 1):
        return True

    if (x == len(grid) - 1 and y == 0) or (x == len(grid) - 1 and y == len(grid[0]) - 1):
        return True

    if x == 0 and grid[x + 1][y] != " " or x == len(grid) - 1 and grid[x - 1][y] != " ":
        return True

    if y == 0 and grid[x][y + 1] != " " or y == len(grid[0]) - 1 and grid[x][y - 1] != " ":
        return True

    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """
    grid = deepcopy(grid)
    exits = get_exits(grid)
    if len(exits) == 1:
        return grid, get_exits(grid)[0]

    for elem in exits:
        if encircled_exit(grid, elem):
            return grid, None

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == " ":
                grid[x][y] = 0

    x_ent, y_ent = exits[0]
    grid[x_ent][y_ent] = 1
    x_exit, y_exit = exits[1]
    grid[x_exit][y_exit] = 0
    k = 1

    while grid[x_exit][y_exit] == 0:
        make_step(grid, k)
        k += 1

    path = shortest_path(grid, (x_exit, y_exit))

    return grid, path


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
