
from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)

    elif algorithm == 'BFS':
       searcher = BFSearcher(param)
    elif algorithm == 'DFS':
       searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
       searcher = GreedySearcher(param)
    elif algorithm == 'A*':
       searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, eight_puzzle('125637084','Greedy',-1))
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    try:
        print("enter try")
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')
    print('hi')
    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, param):

    txt = open(filename, "r")
    list_of_strings = []
    for line in txt:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_strings.append(line_list)
    txt.close()
    searcher_count = 0
    moves_count = 0
    solve_count = 0

    for i in range(len(list_of_strings)):
        init_board = Board(list_of_strings[i][0])
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        if searcher == None:
            return

        soln = None
        try:
            soln = searcher.find_solution(init_state)
        except KeyboardInterrupt:
            print('Search terminated. ', end='')

        if soln == None:
            print('Failed to find a solution.')
        else:
            searcher_count += searcher.num_tested
            moves_count += soln.num_moves
            solve_count += 1
            print(init_board.digit_string() + ':', soln.num_moves, 'moves,', searcher.num_tested, 'states tested')

    print('solved', solve_count, 'puzzles')
    print('averages:',  moves_count / len(list_of_strings), 'moves,', searcher_count / len(list_of_strings), 'states tested')