"""A bunch of code for doing combinatorics problems on the snake game (location of food is included)"""
from Point import Point
import math
from copy import copy, deepcopy

"""Loops through all start positions and returns #of possible states for that size of a board"""
def computeStatesFromSize(size):
    counter = 0
    # i counter is how many snake parts in addition to the head there are
    for i in range(0, int(math.pow(size, 2))):
        print("Snake length: " + str(i))
        for x in range(size):
            for y in range(size):
                board = makeBoard(size)
                board[x][y] = 1
                statesAtLength = computeStatesFromHead(board, Point(x, y), i)
                counter+= statesAtLength
        print(counter)
    return counter

"""Takes a 2d array of 1s and 0s and returns the amount of 0s
-essentially the different places the food could be"""
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
"""
def computeStatesFromHead(board, head, numToPlace):
# 1 is snake part, 2 is food
    returnVal = 0
    if numToPlace is 0:
        returnVal = countOpenSpaces(board) #states found with possible food distributions
    else:
        
        # recursion
        if (head.x+1 < len(board) and board[head.x+1][head.y] is not 1):
            newBoard = deepcopy(board)
            newBoard[head.x+1][head.y] = 1
            returnVal+= computeStatesFromHead(newBoard, Point(head.x+1, head.y), numToPlace-1)
        if (head.x-1 >= 0 and board[head.x-1][head.y] is not 1):
            newBoard = deepcopy(board)
            newBoard[head.x-1][head.y] = 1
            returnVal+= computeStatesFromHead(newBoard, Point(head.x-1, head.y), numToPlace-1)
        if (head.y+1 < len(board[0]) and board[head.x][head.y+1] is not 1):
            newBoard = deepcopy(board)
            newBoard[head.x][head.y+1] = 1
            returnVal+= computeStatesFromHead(newBoard, Point(head.x, head.y+1), numToPlace-1)
        if (head.y-1 >= 0 and board[head.x][head.y-1] is not 1):
            newBoard = deepcopy(board)
            newBoard[head.x][head.y-1] = 1
            returnVal+= computeStatesFromHead(newBoard, Point(head.x, head.y-1), numToPlace-1)
    
    return returnVal


"""makes a 2d square array filled with 0s"""
def makeBoard(size):
    rows, cols = size, size
    arr = [[0 for i in range(cols)] for j in range(rows)] 
    return arr




"""NON-Essential: takes the size of the snake and the board size and returns number of possible positions for this setup"""
def computeStatesFromSingleSizes(snakeSize, boardSize):
    counter = 0
    for x in range(boardSize):
            for y in range(boardSize):
                board = makeBoard(boardSize)
                board[x][y] = 1
                statesAtLength = computeStatesFromHead(board, Point(x, y), snakeSize)
                counter+= statesAtLength
    return counter