import Combinatorics as comb
import StateScorePair as scp
import numpy as np
import Point as Point
from copy import copy, deepcopy
import math

class Agent:
    states = []
    values = []
    statesByLength = []
    # stateToScoreTable = {}
    
    """"""
    def __init__(self, boardSize, agentType, learningRate):
        self.states = comb.getStatesFromSize(boardSize)
        self.values = [0] * len(self.states)
        self.statesByLength = self.getStatesByLength(self.states)
        self.learningRate = learningRate
        self.boardSize = boardSize
        # sets the values of winning states
        for i in range(len(self.states)):
            curState = self.states[i]
            if self.getLength(curState) == math.pow(boardSize, 2):
                self.values[i] = 100
        
            
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
        print(self.states)
        print(self.values)
        maxChange = 0
        for i in range(len(self.states)):
            

            curBoard = self.states[i]
            if self.getLength(curBoard) != math.pow(len(curBoard), 2):
                curValue = self.values[i]
                head = self.getHeadLocation(self.states[i])

                # looking to each side (left, right, up, down) of the head, if it is not filled, it is a possible move
                left, right, up, down = self.getPossibleMoves(curBoard)

                # using inherent nature of empty list which evaluates to false
                if left:
                    adder = 0
                    for l in left:
                        # adds the value of the possible state currently being viewed
                        adder+= self.values[self.states.index(l)]
                    leftAve = adder / len(left)
                else: 
                    leftAve = -1
                
                if right:
                    adder = 0
                    for r in right:
                        # adds the value of the possible state currently being viewed
                        adder+= self.values[self.states.index(r)]
                    rightAve = adder / len(right)
                else: 
                    rightAve = -1
                
                if up:
                    adder = 0
                    for u in up:
                        # adds the value of the possible state currently being viewed
                        adder+= self.values[self.states.index(u)]
                    upAve = adder / len(up)
                else: 
                    upAve = -1

                if down:
                    adder = 0
                    for d in down:
                        # adds the value of the possible state currently being viewed
                        adder+= self.values[self.states.index(d)]
                    downAve = adder / len(down)
                else: 
                    downAve = -1

                adder = 0
                divisor = 0
                for j in [leftAve, rightAve, upAve, downAve]:
                    if j != -1:
                        adder+=j
                        divisor+=1
                if divisor != 0:
                    adder/=divisor
                prevVal = self.values[i]
                self.values[i] = adder * self.learningRate
                maxChange = max(maxChange, abs(self.values[i]- prevVal))
        print("--------")
        return maxChange

    """takes a 2d board and returns four arrays for lrud possible moves"""
    def getPossibleMoves(self, curBoard):
        left = []
        right = []
        up = []
        down = []
        head = self.getHeadLocation(curBoard)
        # left - is head.y bc head stores x, y point but it is actually in r, c format and subtracting from column goes to left
        if head.y-1 >= 0:
            # print("left")
            hasEaten = False
            nextBoard = deepcopy(curBoard)
            if curBoard[head.x][head.y-1] is 0 :
                # moving snake to next position after not eating food
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        if nextBoard[x][y] == self.getLength(nextBoard):
                            nextBoard[x][y] = 0
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                nextBoard[head.x][head.y-1] = 1
                left.append(nextBoard)
            elif curBoard[head.x][head.y-1] is -1:
                # moving snake to next position after eating food
                hasEaten = True
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        if nextBoard[x][y] == self.getLength(nextBoard):
                            nextBoard[x][y] += 1
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                        elif nextBoard[x][y] == -1:
                            nextBoard[x][y] = 1
            elif curBoard[head.x][head.y-1] == self.getLength(curBoard) and self.getLength(curBoard) >= 4: #>4 to assure that tail is not the exact next part
                # moving snake to next position after moving to former tail position
                length = self.getLength(nextBoard)
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        if nextBoard[x][y] == length:
                            nextBoard[x][y] = 1
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                left.append(nextBoard)
            if hasEaten:
                # possbile stochastic next states (just different placements of the food)
                if self.getLength(nextBoard) != math.pow(len(nextBoard), 2):
                    ps = comb.getPossibleFoodStates(nextBoard)
                    for p in ps:
                        left.append(p)
                else:
                    left.append(nextBoard)
                    


        # right - is head.y bc head stores x, y point but it is actually in r, c format and adding to column goes to right
        if head.y+1 < len(curBoard):
            nextBoard = deepcopy(curBoard)
            hasEaten = False
            if curBoard[head.x][head.y+1] is 0:
                # moving snake to next position after not eating food
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        if nextBoard[x][y] == self.getLength(nextBoard):
                            nextBoard[x][y] = 0
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                nextBoard[head.x][head.y+1] = 1
                right.append(nextBoard)
            elif curBoard[head.x][head.y+1] is -1:
                # moving snake to next position after eating food
                hasEaten = True
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        # if is tail position
                        if nextBoard[x][y] == self.getLength(nextBoard):
                            nextBoard[x][y] += 1
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                        elif nextBoard[x][y] == -1:
                            nextBoard[x][y] = 1
            elif curBoard[head.x][head.y+1] == self.getLength(curBoard) and self.getLength(curBoard) >= 4: #>4 to assure that tail is not the exact next part
                # moving snake to next position after moving to former tail position
                length = self.getLength(nextBoard)
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        if nextBoard[x][y] == length:
                            nextBoard[x][y] = 1
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                right.append(nextBoard)
            if hasEaten:
                # possible stochastic next states (just different placements of the food)
                if self.getLength(nextBoard) != math.pow(len(nextBoard), 2):
                    ps = comb.getPossibleFoodStates(nextBoard)
                    for p in ps:
                        right.append(p)
                else:
                    right.append(nextBoard)



        # up - is head.x bc head stores x, y point but it is actually in r, c format and subtracting from row goes up
        if head.x-1 >= 0:
            nextBoard = deepcopy(curBoard)
            # print("up")
            hasEaten = False
            if curBoard[head.x-1][head.y] is 0:
                # moving snake to next position after not eating food
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        if nextBoard[x][y] == self.getLength(nextBoard):
                            nextBoard[x][y] = 0
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                nextBoard[head.x-1][head.y] = 1
                up.append(nextBoard)
            elif curBoard[head.x-1][head.y] is -1:
                # moving snake to next position after eating food
                hasEaten = True
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        if nextBoard[x][y] == self.getLength(nextBoard):
                            nextBoard[x][y] += 1
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                        elif nextBoard[x][y] == -1:
                            nextBoard[x][y] = 1
            elif curBoard[head.x-1][head.y] == self.getLength(curBoard) and self.getLength(curBoard) >= 4: #>4 to assure that tail is not the exact next part
                # moving snake to next position after moving to former tail position
                length = self.getLength(nextBoard)
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        if nextBoard[x][y] == length:
                            nextBoard[x][y] = 1
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                up.append(nextBoard)

            if hasEaten:
                # possbile stochastic next states (just different placements of the food)
                if self.getLength(nextBoard) != math.pow(len(nextBoard), 2):
                    ps = comb.getPossibleFoodStates(nextBoard)
                    for p in ps:
                        up.append(p)
                else:
                    up.append(nextBoard)



        # down - is head.x bc head stores x, y point but it is actually in r, c format and adding tp column goes down
        if head.x+1 < len(curBoard[0]):
            nextBoard = deepcopy(curBoard)
            # print("down")
            hasEaten = False
            if curBoard[head.x+1][head.y] is 0:
                # moving snake to next position after not eating food
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        if nextBoard[x][y] == self.getLength(nextBoard):
                            nextBoard[x][y] = 0
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                nextBoard[head.x+1][head.y] = 1
                down.append(nextBoard)
            elif curBoard[head.x+1][head.y] is -1:
                # moving snake to next position after eating food
                hasEaten = True
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        if nextBoard[x][y] == self.getLength(nextBoard):
                            nextBoard[x][y] += 1
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                        elif nextBoard[x][y] == -1:
                            nextBoard[x][y] = 1
            elif curBoard[head.x+1][head.y] == self.getLength(curBoard) and self.getLength(curBoard) >= 4: #>4 to assure that tail is not the exact next part
                # moving snake to next position after moving to former tail position
                length = self.getLength(nextBoard)
                for x in range(len(nextBoard)):
                    for y in range(len(nextBoard[0])):
                        if nextBoard[x][y] == length:
                            nextBoard[x][y] = 1
                        elif nextBoard[x][y] > 0:
                            nextBoard[x][y] += 1
                down.append(nextBoard)

            if hasEaten:
                # possible stochastic next states (just different placements of the food)
                if self.getLength(nextBoard) != math.pow(len(nextBoard), 2):
                    ps = comb.getPossibleFoodStates(nextBoard)
                    for p in ps:
                        down.append(p)
                else:
                    down.append(nextBoard)
        return left, right, up, down

    """takes a board and returns a point (x, y) where the head is located (the head has a value of 1)"""
    def getHeadLocation(self, board):
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

    def getAverageValueOfStates(self, boards):
        ave = 0
        for i in boards:
            ave += self.values[self.states.index(i)]
        if len (boards) > 0:
            ave /= len(boards)
        return ave

    """takes 2d board and returns 0, 1, 2, 3 corresponding to movement direction that should be taken, 
    left, right, up, down. if no moves possible, returns -1"""
    def decide(self, board):
        currentDecision = -1
        currentAve = 0
        counter = 0
        if len(board) == self.boardSize:
            for direction in self.getPossibleMoves(board):
                if direction:
                    ave = self.getAverageValueOfStates(direction)
                    if ave > currentAve:
                        currentAve = ave
                        currentDecision = counter
                counter+=1
        return currentDecision
            
# a = Agent(3, "V-Iteration", 0.9)
# # # p = a.getStatesBySize(comb.getStatesFromSize(2))
# change = 1000
# while change > 0.1:
#     change = a.valueIteration()
#     print("change " + str(change))
# print(a.decide([[-1, 1, 2], [5, 4, 3], [6, 7, 8]]))

# # bo = comb.makeBoard(2)
