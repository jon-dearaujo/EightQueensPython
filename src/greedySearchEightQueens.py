from collections import deque
from src.state import state
class greedySearchEightQueens(object):
    def __init__(self, initialPositions):
        self.states = deque()
        self.visited = []
        self.initial = state(initialPositions, 42, 0, None)
    
    def execute(self):
        self.states.append(self.initial)
        found = False
        while len(self.states) > 0 and found == False:
            current = self.states.popleft()
            if current not in self.visited:
                if current.heuristic == 0:
                    found = True
                else:
                    self.expandState(current)
                    self.states = deque(sorted(self.states, key=lambda state: state.heuristic))
                    self.visited.append(current)
        if found:
            steps = []
            self.getSolutionSteps(steps, current)
            return steps
            
    def getSolutionSteps(self, steps, state):
        if state.parent != None:
            self.getSolutionSteps(steps, state.parent)
        steps.append(state)
        
    def expandState(self, state):
        for i in range(0, len(state.positions)):
            self.createPossibleStates(state, i)
    
    def createPossibleStates(self, current, index):
        for i in range(0, len(current.positions)):
            if i != current.positions[index]:
                newStatePositions = list(current.positions)
                newStatePositions[index] = i
                newHeuristic = self.calculateHeuristic(newStatePositions)
                newState = state(newStatePositions, newHeuristic, current.cost + 1, current)
                self.states.append(newState)
 
    def calculateHeuristic(self, positions):
        attacks = 0
        for i in range(0, len(positions)):
            if self.attackInSameLine(positions, i):
                attacks += 1
            if self.attacksInRightBottonDiagonal(positions, i):
                attacks += 1
            if self.attacksInRightTopDiagonal(positions, i):
                attacks += 1
        return attacks       
    def attackInSameLine(self, positions, index):
        positionsAtRight = positions[index + 1:]
        return len([x for x in positionsAtRight if x == positions[index]]) > 0
    
    def attacksInRightBottonDiagonal(self, positions, index):
        positionsAtRight = positions[index + 1:]
        positionToBeAttacked = positions[index] + 1
        for i in positionsAtRight:
            if positionToBeAttacked < len(positions) and i == positionToBeAttacked:
                return True
            positionToBeAttacked += 1
        return False
            
    def attacksInRightTopDiagonal(self, positions, index):
        positionsAtRight = positions[index + 1:]
        positionToBeAttacked = positions[index] - 1
        for i in positionsAtRight:
            if positionToBeAttacked >= 0 and i == positionToBeAttacked:
                return True
            positionToBeAttacked -= 1
        return False