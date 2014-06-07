#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1, 1, 1, 5, 1]) => 1150 points
# score([2, 3, 4, 6, 2]) => 0 points
# score([3, 4, 5, 3, 3]) => 350 points
# score([1, 5, 1, 2, 4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(dice):
    def group_numbers(score):
        acc = {}
        for d in score:
            acc[d] = (acc[d] + 1) if d in acc else 1
        return acc

    nums = group_numbers(dice)
    res = 0
    if nums:
        # i could do it simpler but i wanted to play with dictionary iterations
        # a set of three numbers is worth 100 times the number
        # skip the calculation for 'ones'
        for key,times in {k:v for (k, v) in nums.iteritems() if k not in [1,]}.iteritems():
            if times >= 3:
                res += (key * 100)

        # every 1 is worth 100
        # a set of three ones is worth 1000
        if 1 in nums:
            if nums[1] < 3:
                res += (nums[1] * 100)
            elif nums[1] == 3:
                res += 1000
            elif nums[1] > 3:
                res += (1000 + ((nums[1] - 3) * 100))

        # a 5 is worth 50
        # we don't have to manage 3x5 because it's already handled earlier
        if 5 in nums:
            if nums[5] < 3:
                res += (nums[5] * 50)
            elif nums[5] > 3:
                res += ((nums[5] - 3) * 50)

    # You need to write this method
    return res


class AboutScoringProject(Koan):
    def test_score_of_an_empty_list_is_zero(self):
        self.assertEqual(0, score([]))

    def test_score_of_a_single_roll_of_5_is_50(self):
        self.assertEqual(50, score([5]))

    def test_score_of_a_single_roll_of_1_is_100(self):
        self.assertEqual(100, score([1]))

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        self.assertEqual(300, score([1, 5, 5, 1]))

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        self.assertEqual(0, score([2, 3, 4, 6]))

    def test_score_of_a_triple_1_is_1000(self):
        self.assertEqual(1000, score([1, 1, 1]))

    def test_score_of_other_triples_is_100x(self):
        self.assertEqual(200, score([2, 2, 2]))
        self.assertEqual(300, score([3, 3, 3]))
        self.assertEqual(400, score([4, 4, 4]))
        self.assertEqual(500, score([5, 5, 5]))
        self.assertEqual(600, score([6, 6, 6]))

    def test_score_of_mixed_is_sum(self):
        self.assertEqual(250, score([2, 5, 2, 2, 3]))
        self.assertEqual(550, score([5, 5, 5, 5]))
        self.assertEqual(1150, score([1, 1, 1, 5, 1]))

    def test_ones_not_left_out(self):
        self.assertEqual(300, score([1, 2, 2, 2]))
        self.assertEqual(350, score([1, 5, 2, 2, 2]))
