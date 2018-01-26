# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:33:29 2018

@author: Zachary.Clement
"""
import math
import yahtzee

#example import from yahtzee.py file
#yahtzee.run_example()
#hand = (2,2,2,4, 4, 3)
held_dice = (2,2)
num_die_sides = 6 #outcomes
num_free_dice = 1 #lengthII

def run_example():
    outcomes = set([ 1, 2, 3, 4, 5, 6])
    #outcomes = set(['green', 'blue', 'red'])

    length = 2
    seq_outcomes = yahtzee.gen_all_sequences(outcomes, length)
    print('computed', len(seq_outcomes), 'sequence of', str(length), 'outcomes')
    print('Sequences were', seq_outcomes)

#run_example()
#print(math.factorial(5)/math.factorial(5-2))

#print(yahtzee.score(hand))

print(yahtzee.expected_value(held_dice, num_die_sides, num_free_dice))
