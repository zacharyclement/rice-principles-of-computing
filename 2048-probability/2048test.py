import simpletest
import TwentyFortyEight

#def test(function):

suite = simpletest.TestSuite()

board = TwentyFortyEight.TwentyFortyEight(4,4)

#suite.run_test(function(computed, expected, message=''))

#print(suite)
#print(board)
#print(board.get_grid_height())
#print(board.get_grid_width())
#print(board.set_tile(2,2,15))
#print(board.new_tile())
#print(board)
print(board.move('DOWN'))
#print(board.get_tile(2,2))
