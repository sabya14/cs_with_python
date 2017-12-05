import random
from copy import deepcopy


def remove_values_from_list(the_list, val):
    while val in the_list:
        the_list.remove(val)
    return the_list


class Soduku:
    def __init__(self):
        self.size = 9
        self.possible_entry = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.grid = [[0 for x in range(9)] for y in range(9)]

    def make_state_from_string(self, string):
        list_of_size = string.split('\n')
        if len(list_of_size) != 9:
            raise ValueError('Invalid entry')
        for index_r in range(self.size):
            row = list_of_size[index_r].strip(" ")
            for index_c in range(self.size):
                self.grid[index_r][index_c] = int(row[index_c])

    def print_state(self):
        for index in range(self.size):
            print('-',self.grid[index])

    def find_empty_positions(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.grid[row][col] is 0:
                    return row, col
        return False

    def no_zero(self):
        for row in range(self.size):
            if 0 in self.grid[row]:
                return False
        return True

    def validate_row_column(self, row_index, column_index):
        temp_grid = map(list, zip(*soduku.grid))
        temp_grid = list(temp_grid)
        temp_row = deepcopy(self.grid[row_index])
        temp_col = deepcopy(temp_grid[column_index])
        temp_row = remove_values_from_list(temp_row, 0)
        temp_col = remove_values_from_list(temp_col, 0)
        if len(temp_row) == len(set(temp_row)) and len(temp_col) == len(set(temp_col)):
            print('t',temp_row,temp_col)
            return True
        else:
            return False

    def validate_position(self, row_index, column_index):
        if self.validate_row_column(row_index, column_index):
            cell = []
            for row in range((row_index//3)*3, (row_index//3)*3+3):
                for col in range((column_index//3)*3, (column_index//3)*3+3):
                    # if row <= row_index and column_index <=column_index:
                    cell.append(self.grid[row][col])
            if len(remove_values_from_list(cell,0)) == len(set(remove_values_from_list(cell, 0))):
                # print(row_index,column_index)
                # print(cell)
                return True
        return False



    def find_element(self, row, col):
        return random(1,10)

    def solver(self, row, col):
        if self.validate_position(row, col):
            self.print_state()
            if (not self.find_empty_positions()):
                self.print_state()
                exit()
            else:
                row, col = self.find_empty_positions()
                for i in range(1,10):
                    self.grid[row][col] = i
                    if self.solver(row, col):
                        return True
                    else:
                        self.grid[row][col] = 0
        return False

soduku = Soduku()
soduku.make_state_from_string("""400000805
                                 030000000
                                 000700000
                                 020000060
                                 000080400
                                 000010000
                                 000603070
                                 500200000
                                 104000000""")
print(soduku.solver(0, 0))

