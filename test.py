import Combinatorics as comb
import numpy as np

def getLength(board):
        return np.amax(board)

print(getLength(comb.makeBoard(2)))