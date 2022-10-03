from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """

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
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        return True
