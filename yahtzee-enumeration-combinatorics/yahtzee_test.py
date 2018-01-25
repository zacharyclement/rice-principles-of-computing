# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:33:29 2018

@author: Zachary.Clement
"""
import math
import yahtzee

#example import from yahtzee.py file
#yahtzee.run_example()
hand = (2,2,3,4)


def run_example():
    #outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    outcomes = set(['green', 'blue', 'red'])
    
    length = 2
    seq_outcomes = yahtzee.gen_all_sequences(outcomes, length)
    print('computed', len(seq_outcomes), 'sequence of', str(length), 'outcomes')
    print('Sequences were', seq_outcomes)
    
#run_example()
#print(math.factorial(5)/math.factorial(5-2))


print(yahtzee.score(hand))