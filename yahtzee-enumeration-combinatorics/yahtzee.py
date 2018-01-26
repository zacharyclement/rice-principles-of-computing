# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:27:55 2018

@author: Zachary.Clement
"""

"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))

        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card. hand: full yahtzee hand
    Returns an integer score
    """
    score = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6}
    score_card = {}
    final_score = 0

    for dice_value in hand:
        if dice_value in score_card:
            score_card[dice_value] += dice_value
        else:
            score_card[dice_value] = score[dice_value]

    for key,value in score_card.items():
        final_score += value

    return final_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides. held_dice:
    dice that you will hold num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled Returns a floating point expected value
    """

    all_possible_rolls = gen_all_sequences([x for x in range(1,num_die_sides+1)], num_free_dice)
    
    total_score = 0
    score_holder = 0
    for hand in all_possible_rolls:
        score_holder = score(hand)
        total_score += score_holder

    return total_score/len(all_possible_rolls)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold. hand: full
    yahtzee hand Returns a set of tuples, where each tuple is dice to hold
    """
    #compute the set of all possible holds in a manner very similar to that of gen all sequences.
    #permutations if hold 0, if hold 1, if hold 2, etc...
    
    all_holds = [()]
    for dice in hand:
        for possible_hold in all_holds:
            all_holds = all_holds + [tuple(possible_hold) + (dice,)]
    
    return set(all_holds)



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    final_hand_score_dic = {}
    all_holds = gen_all_holds(hand)
    
    #expected value for free dice
    for single_hand in all_holds:
        hand_score = score(single_hand)
        num_free_dice = len(hand) - len(single_hand)
        free_dice_exp_value = expected_value(single_hand, num_die_sides, num_free_dice)
        total_score = hand_score + free_dice_exp_value
        final_hand_score_dic[single_hand] = total_score
        print(single_hand, ':', 'total score = ', total_score)
    max_dic_value = max(final_hand_score_dic.values())
    print('find max is ', max_dic_value)
    max_dic_key = [k for k,v in final_hand_score_dic.items() if v == max_dic_value]
    print('answer is: ', max_dic_key[0])
    return (max_dic_value, max_dic_key[0])


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)





#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
