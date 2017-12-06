import random
from copy import deepcopy

GRID = [[0 for x in range(9)] for y in range(9)]
SIZE = 9


def make_state_from_string(string, grid):
    """

    :param string: Soduku as 81 char string
    :param grid: An empty matrix representation
    :return: Filled soduku in a matrix
    """
    list_of_size = string.split('\n')
    if len(list_of_size) != SIZE:
        raise ValueError('Invalid entry')
    # simple for 2d loop, striping to remove spaces
    for index_r in range(SIZE):
        row = list_of_size[index_r].strip(" ")
        for index_c in range(SIZE):
            grid[index_r][index_c] = int(row[index_c])
    return grid


class Soduku:
    """
     Simple class to solve soduku
    """
    def __init__(self):
        self.size = SIZE
        self.possible_entry = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def print_state(self, grid):
        print('-----------')
        for index in range(self.size):
            print(grid[index])

    def find_empty_positions(self, grid):
        for row in range(0,9):
            for col in range(0,9):
                if grid[row][col] is 0:
                    return row, col
        return False

    def validate_row_column(self, grid, row_index, column_index, num):
        """
        :param grid: grid
        :param row_index: row of new element
        :param column_index: column of new element
        :param num: new element
        :return: if there is no row or column conflict return true
        """
        temp_grid = map(list, zip(grid))
        temp_grid = list(temp_grid)
        temp_row = deepcopy(grid[row_index])
        temp_col = deepcopy(temp_grid[column_index])
        if (num in temp_row) or (num in temp_col):
            return False
        else:
            return True

    def validate_cell(self, grid, row_index, column_index, num):
        """

        :param grid: grid
        :param row_index: row of new element
        :param column_index: column of new element
        :param num: new element
        :return: if there is cell conflict(9 sorrounding element) we return true
        """
        for row in range((row_index//3)*3, (row_index//3)*3+3):
            for col in range((column_index//3)*3, (column_index//3)*3+3):
                if grid[row][col] == num:
                    return False
        return True

    def validate_position(self,  grid, row_index, column_index, num):
        """
        :param grid: grid
        :param row_index: row of new element
        :param column_index: column of new element
        :param num: new element
        :return: if there is no row,column and cell conflict we return true
        """
        if self.validate_row_column(grid, row_index, column_index,num) and \
                self.validate_cell(grid, row_index,column_index, num):
            return True
        else:
            return False

    def solver(self, grid):
        # if no empty, we have solved it, return
        if not self.find_empty_positions(grid):
            self.print_state(grid)
            exit()
        else:
            # get an empty column
            # could be improved, get row, col in one col only
            row, col = self.find_empty_positions(grid)

        for i in range(1, 10):
            # get an element apply, and check validity
            if self.validate_position(grid, row, col, i):
                # if valid, save state and continue
                grid[row][col] = i
                if self.solver(grid):
                    return True
            # else revert state and try again
            grid[row][col] = 0
        return False


grid = make_state_from_string(string="""003020600
                                        900305001
                                        001806400
                                        008102900
                                        700000008
                                        006708200
                                        002609500
                                        800203009
                                        005010300""", grid=GRID)
soduku = Soduku()
soduku.solver(grid)

