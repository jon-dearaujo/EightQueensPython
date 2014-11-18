class state(object):
    def __init__(self, positions, heuristic, cost, parent):
        self.positions = positions
        self.heuristic = heuristic
        self.cost = cost
        self.parent = parent
    
    def __repr__(self):
        board = [[x for x in range(0, len(self.positions))] for x in range(0, len(self.positions))]
        for i in range(0, len(self.positions)):
            for j in range(0, len(self.positions)):
                board[i][j] = ' '
        
        for i in range(0, len(self.positions)):
            board[self.positions[i]][i] = 'R'
        
        buffer = ''
        separator = ''
        for i in range(0, len(self.positions)):
            for j in range(0, len(self.positions)):
                buffer = separator.join([buffer, '|', str(board[i][j])])
            buffer = separator.join([buffer, '|', '\n'])
        buffer = separator.join([buffer, '\n'])
        return buffer
