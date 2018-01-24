from simpletest import TestSuite
import TicTacToe
import TTTboard

board = TTTboard.TTTboard(3)

print(TicTacToe.mc_trial(board, TTTboard.PLAYERX))
