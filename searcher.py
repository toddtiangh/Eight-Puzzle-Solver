import random
from state import *

class Searcher:
    def __init__(self, depth_limit):
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

    def add_state(self, new_state):
        self.states += [new_state]

    def should_add(self, state):
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True

    def add_states(self, new_states):
        for i in range(len(new_states)):
            if self.should_add(new_states[i]):
                self.add_state(new_states[i])

    def next_state(self):
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self, init_state):
        self.add_state(init_state)
        current_state = init_state
        while current_state.board.tiles != GOAL_TILES:
            if len(self.states) == 0:
                return None
            current_state = self.next_state()
            succ = current_state.generate_successors()
            self.add_states(succ)
            self.num_tested += 1
        return current_state

    def __repr__(self):
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


class BFSearcher(Searcher):

    def next_state(self):
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):

    def next_state(self):
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    return 0

def h1(state):

    i = state.board.num_misplaced()
    return i

class GreedySearcher(Searcher):
    def __init__(self, heuristic):
        super().__init__(depth_limit=-1)
        self.heuristic = heuristic

    def priority(self, state):
        
        return -1 * self.heuristic(state)

    def add_state(self, state):

        self.states += [[self.priority(state), state]]

    def next_state(self):
        s = max(self.states)
        self.states.remove(s)
        return s[1]

    def __repr__(self):

        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


class AStarSearcher(GreedySearcher):

    def priority(self, state):

        return -1 * (self.heuristic(state) + state.num_moves)


