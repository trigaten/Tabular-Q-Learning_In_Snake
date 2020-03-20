"""StateValueNode (SSN) a type of linked list that stores a Snake board state (2D array), a floating 
point value for the evaluation of the state, and 4 arrays to store SVNs of possible next moves in the
left, right, up, down directions"""
class StateValueNode:
    def __init__(self, state, value, left = [], right = [], up = [], down = []):
        # 2D board state
        self.state = state
        # a floating point value for this 
        self.value = value
        # arrays to store potential next StateValueNodes
        self.left = left
        self.right = right
        self.up = up
        self.down = down
    
    def getState(self):
        return self.state

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getMoves(self):
        return self.left, self.right, self.up, self.down
    
    # methods to add a node to the left, right, up, or down array
    def addToLeft(self, SVN):
        self.left.append(SVN)
    
    def addToRight(self, SVN):
        self.right.append(SVN)

    def addToUp(self, SVN):
        self.up.append(SVN)
    
    def addToDown(self, SVN):
        self.down.append(SVN)

    # to String method
    def __str__(self):
        return "State: " + self.state + "\nValue " + self.value + "\nleft: " + self.left + "\nright: " + self.right + "\nup: " + self.up + "\ndown: " + self.down  