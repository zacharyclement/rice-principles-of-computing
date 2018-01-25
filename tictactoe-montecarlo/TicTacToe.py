"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import TTTboard

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.

NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.
def 𝚖𝚌_𝚝𝚛𝚒𝚊𝚕(𝚋𝚘𝚊𝚛𝚍, 𝚙𝚕𝚊𝚢𝚎𝚛):
    '''This function takes a current board and the next player to move. The
    function should play a game starting with the given player by making random
    moves, alternating between players. The function should return when the
    game is over. The modified board will contain the state of the game, so
    the function does not return anything. In other words, the function should
    modify the 𝚋𝚘𝚊𝚛𝚍 input'''
    while board.check_win() == None:

        empty_squares = board.get_empty_squares() #Return a list of (row, col) tuples for all empty squares

        random_index = random.randint(0, len(empty_squares) - 1)

        empty_row = empty_squares[random_index][0]
        empty_col = empty_squares[random_index][1]

        board.move(empty_row, empty_col, player)
        player = TTTboard.switch_player(player)
        print(board)

    return None



def 𝚖𝚌_𝚞𝚙𝚍𝚊𝚝𝚎_𝚜𝚌𝚘𝚛𝚎𝚜(𝚜𝚌𝚘𝚛𝚎𝚜, 𝚋𝚘𝚊𝚛𝚍, 𝚙𝚕𝚊𝚢𝚎𝚛):
    '''This function takes a grid of scores (a list of lists) with the same
    dimensions as the Tic-Tac-Toe board, a board from a completed game, and
    which player the machine player is. The function should score the completed
    board and update the scores grid. As the function updates the scores grid
    directly, it does not return anything,'''

    winner = board.check_win()

    for row in range(board.get_dim()):
        for column in range(board.get_dim()):
            whos_square = board.square(row, column)
            if winner == player:
                if whos_square == player:
                    scores[row][column] += SCORE_CURRENT
                elif whos_square == TTTboard.switch_player(player):
                    scores[row][column] -= SCORE_OTHER

            elif winner == TTTboard.switch_player(player):
                if whos_square == TTTboard.switch_player(player):
                    scores[row][column] += SCORE_CURRENT
                elif whos_square == player:
                    scores[row][column] -= SCORE_OTHER

    return None

def 𝚐𝚎𝚝_𝚋𝚎𝚜𝚝_𝚖𝚘𝚟𝚎(𝚋𝚘𝚊𝚛𝚍, 𝚜𝚌𝚘𝚛𝚎𝚜):
    ''' This function takes a current board and a grid of scores. The
    function should find all of the empty squares with the maximum score and
    randomly return one of them as a (𝚛𝚘𝚠, 𝚌𝚘𝚕𝚞𝚖𝚗) tuple. It is an error to call
    this function with a board that has no empty squares (there is no possible
    next move), so your function may do whatever it wants in that case. The
    case where the board is full will not be tested.'''
    empty_squares = board.get_empty_squares()
    if empty_squares:
        empty_square_score_dic = {}
        max_value_list = []
        for tile in empty_squares:
            empty_row = tile[0]
            empty_col = tile[1]
            empty_square_score_dic[(empty_row, empty_col)] = scores[empty_row][empty_col]
            print('score_dic = ', empty_square_score_dic)
            for key,value in empty_square_score_dic.items():
                max_value_list.append(value)
        m = max(max_value_list)
        for key,value in empty_square_score_dic.items():
            if m == value:
                best_moves = []
                best_moves.append(key)
                random_index = random.randint(0, len(best_moves)-1)
                selected_move = best_moves[random_index]
        print('selected_move = ', selected_move)

    else:
        return "No Empty Squares"

    return (selected_move[0], selected_move[1])

def 𝚖𝚌_𝚖𝚘𝚟𝚎(𝚋𝚘𝚊𝚛𝚍, 𝚙𝚕𝚊𝚢𝚎𝚛, 𝚝𝚛𝚒𝚊𝚕𝚜):
    ''' This function takes a current board, which player the machine player
    is, and the number of trials to run. The function should use the Monte
    Carlo simulation described above to return a move for the machine player
    in the form of a (𝚛𝚘𝚠, 𝚌𝚘𝚕𝚞𝚖𝚗) tuple. Be sure to use the other functions
    you have written!'''
    return (row, col)

# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# board.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
