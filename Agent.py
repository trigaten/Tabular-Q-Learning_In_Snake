import Combinatorics as comb
import StateScorePair as scp
import numpy as np
class Agent:
    states = []
    values = []
    """Agent types:'V-Iteration """
    def __init__(self, boardSize, agentType):
        if agentType == "V-Iteration":
            states = comb.getStatesFromSize(boardSize)
            values = [0] * len(states)
    """takes 2d board and returns integer length of snake"""
    def getLength(self, board):
        return np.amax(board)
    
    """Takes 3d array, an array of board states (2d arrays) and returns 4d array, an array of 
    arrays of boards organized by size"""
    def getStatesBySize(self, states):
        ret = [];
        for i in states:
            length = self.getLength(i)
            if len(ret) < length:
                ret.append([])
            ret[length-1].append(i)

        return ret


a = Agent(2, "V-Iteration")

print(a.getStatesBySize(comb.getStatesFromSize(2)))
# p = comb.makeBoard(3)
# p[2][1] = 3
# p[1][0] = 1
# p[0][2] = 4
# print(a.getLength(p))




        

