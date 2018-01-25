from simpletest import TestSuite
import TicTacToe
import TTTboard


new_board = TTTboard.TTTBoard(3)
print(new_board)
new_player = TTTboard.PLAYERX
print('xxxxxxxxxxxx')

player = TTTboard.PLAYERX

TicTacToe.mc_trial(new_board, new_player)

scores_for_board = [[0 for row in range(new_board.get_dim())] for column in range(new_board.get_dim())]
print('scores set to zero', scores_for_board)

TicTacToe.mc_update_scores(scores_for_board, new_board, player)
print('updated scores', scores_for_board)

print('xxxxxxxxxxxxxxxxx')
print('find best open move')

TicTacToe.get_best_move(new_board, scores_for_board)
