from simpletest import TestSuite
import TicTacToe
import TTTboard


new_board = TTTboard.TTTBoard(3)
print(new_board)
new_player = TTTboard.PLAYERX
print('xxxxxxxxxxxx')

TicTacToe.mc_trial(new_board, new_player)
