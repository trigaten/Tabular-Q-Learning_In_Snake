"""A bunch of code for doing combinatorics problems on the snake game"""
from Point import Point
import math
from copy import copy, deepcopy

"""Loops through all start positions and returns #of possible states for that size of a board
foodPos is an optional parameter deciding whether the possible locations for food on a given
board count as additional board states
RETURNS integer # of states
"""
def computeStatesFromSize(size, foodPos=True):
    counter = 0
    # i counter is how many snake parts in addition to the head there are
    for i in range(0, int(math.pow(size, 2))):
        print("Snake length: " + str(i+1))
        for x in range(size):
            for y in range(size):
                board = makeBoard(size)
                board[x][y] = 1
                statesAtLength = computeStatesFromHead(board, Point(x, y), i, foodPos)
                counter+= statesAtLength
        print(counter)
    return counter

"""Takes a 2d array of 1s and 0s and returns the amount of 0s
-essentially the different places the food could be
RETURNS integer # of spaces open
"""
def countOpenSpaces(board):
    counter = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] is 0:
                counter+=1
    return counter if counter is not 0 else 1

"""takes a 2d board with zeros except for the head which has its x, y set to 1,
 a 1d aray with x/y location of head, and the number of pieces to add
returns all possible board positions for that specific head
foodPos is an optional parameter deciding whether the possible locations for food on a given
board count as additional board states
for list parameter, pass [] if you want to get a list back
RETURNS integer # of states
"""
def computeStatesFromHead(board, head, numToPlace, foodPos=True, list=None):
# 1 is snake part, 2 is food
    returnVal = 0
    if numToPlace is 0:
        # if we are taking different locations of food into position
        returnVal = countOpenSpaces(board) #states found with possible food distributions

        if foodPos is False and returnVal > 1:
            return 1
    else:
        # recursion
        if (head.x+1 < len(board) and board[head.x+1][head.y] is not 1):
            newBoard = deepcopy(board)
            newBoard[head.x+1][head.y] = 1
            returnVal+= computeStatesFromHead(newBoard, Point(head.x+1, head.y), numToPlace-1, foodPos)
        if (head.x-1 >= 0 and board[head.x-1][head.y] is not 1):
            newBoard = deepcopy(board)
            newBoard[head.x-1][head.y] = 1
            returnVal+= computeStatesFromHead(newBoard, Point(head.x-1, head.y), numToPlace-1, foodPos)
        if (head.y+1 < len(board[0]) and board[head.x][head.y+1] is not 1):
            newBoard = deepcopy(board)
            newBoard[head.x][head.y+1] = 1
            returnVal+= computeStatesFromHead(newBoard, Point(head.x, head.y+1), numToPlace-1, foodPos)
        if (head.y-1 >= 0 and board[head.x][head.y-1] is not 1):
            newBoard = deepcopy(board)
            newBoard[head.x][head.y-1] = 1
            returnVal+= computeStatesFromHead(newBoard, Point(head.x, head.y-1), numToPlace-1, foodPos)
    return returnVal


"""returns a 2d square array size by size filled with 0s
"""
def makeBoard(size):
    rows, cols = size, size
    arr = [[0 for i in range(cols)] for j in range(rows)] 
    return arr

def getPossibleFoodLocations(board):
    list = []
    counter = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] is 0:
                counter+=1
    return counter if counter is not 0 else 1

"""NON-Essential: takes the size of the snake and the board size and returns number of possible positions for this setup
foodPos is an optional parameter deciding whether the possible locations for food on a given
board count as additional board states
RETURNS integer # of states
"""
def computeStatesFromSingleSizes(numToPlace, boardSize, foodPos=True):
    counter = 0
    for x in range(boardSize):
            for y in range(boardSize):
                board = makeBoard(boardSize)
                board[x][y] = 1
                statesAtLength = computeStatesFromHead(board, Point(x, y), numToPlace, foodPos)
                counter+= statesAtLength
    return counter

"""
RETURNS 3d array - an array of states (2d arrays of size*size) possible """
def getStatesFromSize(size, foodPos=True):
    
    