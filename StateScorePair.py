class StateScoreNode:
    def __init__(self, state, score, left = [], right = [], up = [], down = []):
        self.state = state
        self.score = score
        self.left = left
        self.right = right
        self.up = up
        self.down = down
    
    def getState(self):
        return self.state

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score