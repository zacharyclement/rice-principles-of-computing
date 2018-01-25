from simpletest import TestSuite
import TicTacToe
import TTTboard

board_dems = 3
new_board = TTTboard.TTTBoard(board_dems)
print(new_board)
new_player = TTTboard.PLAYERX
print('xxxxxxxxxxxx')

player = TTTboard.PLAYERX

TicTacToe.mc_trial(new_board, new_player)

scores_for_board = [[0 for row in range(board_dems)] for column in range(board_dems)]
print(scores_for_board)

TicTacToe.mc_update_scores(scores_for_board, new_board, player)
print(scores_for_board)
