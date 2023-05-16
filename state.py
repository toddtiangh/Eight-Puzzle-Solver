from board import *

MOVES = ['up', 'down', 'left', 'right']

class State:
    def __init__(self, board, predecessor, move):

        self.board = board
        self.predecessor = predecessor
        self.move = move
        self.num_moves = 0
        if move != 'init':
            pred = self.predecessor
            self.num_moves = pred.num_moves + 1


    def is_goal(self):
        board = self.board
        s = ''
        for r in range(len(GOAL_TILES)):
            for c in range(len(GOAL_TILES[0])):
                s+= GOAL_TILES[r][c]
        if board.digit_string() == s:
            return True
        else:
            return False

    def generate_successors(self):
        successors = []
        for i in MOVES:
            board = self.board
            b = board.copy()
            if b.move_blank(i) != False:
                s = State(b, self, i)
                successors.append(s)

        return successors

    def print_moves_to(self):
        if self.predecessor == None:
            print('Initial State:')
            print(self.board)
        else:
            self.predecessor.print_moves_to()
            print('move the blank ' + self.move + ':')
            print(self.board)

    def __repr__(self):

        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        return True
