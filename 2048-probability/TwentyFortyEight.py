import simpletest
import random
#import poc_2048_gui

"""
Clone of 2048 game.
"""

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    '''
    helper function that merges a single row or column in 2048
    '''
    lenght_of_line = len(line)

    while 0 in line:
        line.remove(0)

    for block in range(len(line)):
        if block + 1 > len(line) - 1:
            break
        if line[block] == line[block + 1]:
            line[block] *= 2
            line.remove(line[block + 1])
            line.insert(block + 1, 0)

    while 0 in line:
        line.remove(0)
    while len(line) != lenght_of_line:
        line.append(0)

    return line


def set_direction_dictionary(height, width):

    dic = {}

    keys = ['UP', 'DOWN', 'LEFT', 'Right']

    for key in keys:
        indices_list = []
        if key == 'UP':
            for x in range(width):
                indices_list.append((0, x))
                dic[key] = indices_list
        elif key == 'DOWN':
            for x in range(width):
                indices_list.append((width, x))
                dic[key] = indices_list
        elif key == 'LEFT':
            for x in range(height):
                indices_list.append((x, 0))
                dic[key] = indices_list
        else:
            for x in range(height):
                indices_list.append((x, height))
                dic[key] = indices_list


    return dic

#print(set_direction_dictionary(4,4))




class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        # reset the grid at the beginning of each game
        self.reset()
        self.direction_dictionary = set_direction_dictionary(self.grid_height, self.grid_width)

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.board = [[0 for col in range(self.grid_height)] for row in range(self.grid_width)]
        return self.board

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """

        return str(self.board)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        direction = self.direction_dictionary[direction]
        
        for x in direction:
            print(x)


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        while True:
            row, col = random.randint(0, self.grid_height - 1), random.randint(0, self.grid_width - 1)
            if self.board[row][col] == 0:
                if random.random() < .9:
                    self.board[row][col] = 2
                else:
                    self.board[row][col] = 4
                break
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.board[row][col] = value


    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.board[row][col]


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
