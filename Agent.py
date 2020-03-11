import Combinatorics as comb
import StateScorePair as scp
import numpy as np
import Point as Point
from copy import copy, deepcopy

class Agent:
    states = []
    values = []
    statesByLength = []
    
    """"""
    def __init__(self, boardSize, agentType):
        self.states = comb.getStatesFromSize(boardSize)
        self.values = [0] * len(self.states)
        self.statesByLength = self.getStatesByLength(self.states)
            
    """takes 2d board and returns integer length of snake"""
    def getLength(self, board):
        return np.amax(board)
    
    """Takes 3d array, an array of board states (2d arrays) and returns 4d array, an array of 
    arrays of boards organized by size"""
    def getStatesByLength(self, states):
        ret = []
        for i in states:
            length = self.getLength(i)
            if len(ret) < length:
                ret.append([])
            ret[length-1].append(i)
        return ret
    # give rewards at last state
    """Performs single value iteration of states and returns values"""
    def valueIteration(self):
        print("Starting Value Iteration")
        for i in range(len(self.states)):
            curBoard = self.states[i]
            curState = self.states[i]
            curValue = self.states[i]
            head = self.getHeadLocation(self.states[i])
            # print("heaad")
            # print(head)
            print("curBoard")
            print(curBoard)
            dict = {}
            # looking to each side (left, right, up, down) of the head, if it is not filled, it is a possible move
            left = []
            right = []
            up = []
            down = []
            if head.x-1 >= 0:
                print("left")
                nextBoard = deepcopy(curBoard)
                if curBoard[head.x-1][head.y] is 0 :
                    # moving snake to next position after not eating food
                    for x in range(len(nextBoard)):
                        for y in range(len(nextBoard[0])):
                            if nextBoard[x][y] == self.getLength(nextBoard):
                                nextBoard[x][y] = 0
                            elif nextBoard[x][y] > 0:
                                nextBoard[x][y] += 1
                    left.append(nextBoard)
                elif curBoard[head.x-1][head.y] is -1:
                    # moving snake to next position after eating food
                    for x in range(len(nextBoard)):
                        for y in range(len(nextBoard[0])):
                            if nextBoard[x][y] == self.getLength(nextBoard):
                                nextBoard[x][y] += 1
                            elif nextBoard[x][y] > 0:
                                nextBoard[x][y] += 1
                            elif nextBoard[x][y] == -1:
                                nextBoard[x][y] = 1
                    # possbile stochastic next states (just different placements of the food)
                    ps = comb.getPossibleFoodStates(nextBoard)
                    for i in ps:
                        left.append(i)
            if head.x+1 < len(curBoard):
                print("right")
                if curBoard[head.x+1][head.y] is 0:
                    pass
                elif curBoard[head.x+1][head.y] is -1:
                    pass
                
            if head.y-1 >= 0:
                print("up")
                if curBoard[head.x][head.y-1] is 0:
                    pass
                elif curBoard[head.x][head.y-1] is -1:
                    pass
                
            if head.y+1 < len(curBoard[0]):
                print("down")
                if curBoard[head.x][head.y+1] is 0:
                    pass
                elif curBoard[head.x][head.y+1] is -1:
                    pass
            


    """takes a board and returns a point (x, y) where the head is located (the head has a value of 1)"""
    def getHeadLocation(self, board):
        # print("board")
        # print(board)
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 1:
                    return Point.Point(x, y)

    """takes a snake state without food and returns a list of Point indices where there are possible next states
    in statesByLength"""
    def getFoodStateIndicesFromSnakeState(self, snakeState):
        snakeLength = self.getLength(snakeState)
        searchArr = comb.getPossibleFoodStates(snakeState)
        retArr = []
        for i in range(len(searchArr)):
            for j in range(len(self.statesByLength[snakeLength-1])):
                if searchArr[i] == self.statesByLength[snakeLength-1][j]:
                    retArr.append(Point.Point(snakeLength-1, j))
        return retArr


a = Agent(2, "V-Iteration")
# # p = a.getStatesBySize(comb.getStatesFromSize(2))
a.valueIteration()
# b = comb.makeBoard(2)
# b[0][0] = 1
# b[0][1] = 2
# dd = a.getFoodStateIndicesFromSnakeState(b)
# print(dd)
# print(len(dd))
# for i in dd:
#     print(a.statesByLength[i.x][i.y])



        

