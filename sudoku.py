import numpy as np
from dokusan import generators
import copy

class Sudoku():
    def __init__(self):
        self.grid = self.generate()
        self.selected = None
        self.originalgrid = copy.deepcopy(self.grid)
        self.result = None
        self.complete = False
    
    def generate(self):
        arr = np.array(list(str(generators.random_sudoku(avg_rank=125))))
        arr = arr.reshape(9,9).tolist()
        return arr

    def select(self, row, col):
        try:
            if self.originalgrid[row][col] == '0':
                if self.selected == None:
                        self.selected = (row, col)
                else:
                    if self.selected == (row, col):
                        self.selected = None
                    else:
                        self.selected = (row, col)
            else:
                self.selected = None
        except:
            pass
    
    def checkcomplete(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == '0':
                    return False

        return True
    
    def iswin(self):
        for i in range(9):
            list1 = []
            for j in range(9):
                list.append(self.grid[i][j])
            set1 = set(list1)
            if len(set1) != 9:
                return False
        for i in range(9):
            list1 = []
            for j in range(9):
                list.append(self.grid[j][i])
            set1 = set(list1)
            if len(set1) != 9:
                return False
        
        return True