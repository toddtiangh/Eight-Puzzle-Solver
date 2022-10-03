#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Todd Tian
# email: toddtian@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        count = 0
        idx = 0
        idx2 = 0
        for i in range(len(digitstr)):
            self.tiles[idx][idx2] = digitstr[i]
            count += 1
            idx2 += 1
            if count == 3 or count == 6:
                idx2 = 0
                idx += 1
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c

    def __repr__(self):
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '0':
                    s += '_' + ' '
                else:
                    s += self.tiles[r][c] + ' '
            s += '\n'
        return s

    def in_bound(self, index):
        x, y = index
        if 0 <= x < 3 and 0 <= y < 3:
            return True
        return False

    def move_blank(self, direction):
        directions = {
            'up': [-1, 0],
            'down': [1, 0],
            'left': [0, -1],
            'right': [0, 1]
        }
        d = directions[direction]

        blank_index = []
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '0':
                    blank_index = [r,c]

        new_index = [blank_index[0] + d[0], blank_index[1] + d[1]]
        if self.in_bound(new_index):
            num_switch = self.tiles[blank_index[0] + d[0]][blank_index[1] + d[1]]
            self.tiles[blank_index[0] + d[0]][blank_index[1] + d[1]] = '0'
            self.tiles[blank_index[0]][blank_index[1]] = num_switch
            self.blank_c = blank_index[1] + d[1]
            return True
        return False

    def digit_string(self):
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles)):
                if self.tiles[r][c] == '_':
                    s += '0'
                else:
                    s += self.tiles[r][c]
        return s

    def copy(self):
        b2_str = self.digit_string()
        b2 = Board(b2_str)
        return b2

    def num_misplaced(self):
        goal = [['0','1','2'],['3','4','5'],['6','7','8']]
        count = 0
        for r in range(len(goal)):
            for c in range(len(goal[0])):
                if self.tiles[r][c] != '0':
                    if self.tiles[r][c] != goal[r][c]:
                        count += 1

        return count

    def distance(self):
        goal = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
        distance = 0
        x, y, x2, y2 = 0, 0, 0, 0
        for r in range(len(goal)):
            for c in range(len(goal[0])):
                if self.tiles[r][c] != goal[r][c]:
                    num = self.tiles[r][c]
                    x, y = r, c
                    print(x, y)
                    for i in range(len(goal)):
                        for j in range(len(goal[0])):
                            if num == goal[r][c]:
                                x2, y2 = i, j
                                print(x2, y2)
                                distance = abs((x - x2) + (y - y2))
        return distance

    def __eq__(self, other):
        b1 = self.digit_string()
        b2 = other.digit_string()

        if b1 == b2:
            return True
        else:
            return False
