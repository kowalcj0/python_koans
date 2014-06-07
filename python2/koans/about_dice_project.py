#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from runner.koan import *

import random


class DiceSet(object):
    def __init__(self):
        self._values = None

    @property
    def values(self):
        return self._values

    def roll(self, n):
        # Needs implementing!
        # Tip: random.randint(min, max) can be used to generate random numbers
        self._values = [random.randint(1, 6) for x in range(n)]


class AboutDiceProject(Koan):
    def test_can_create_a_dice_set(self):
        dice = DiceSet()
        self.assertTrue(dice)

    def test_rolling_the_dice_returns_a_set_of_integers_between_1_and_6(self):
        dice = DiceSet()

        dice.roll(5)
        self.assertTrue(isinstance(dice.values, list), "should be a list")
        self.assertEqual(5, len(dice.values))
        for value in dice.values:
            self.assertTrue(
                value >= 1 and value <= 6,
                "value " + str(value) + " must be between 1 and 6")

    def test_dice_values_do_not_change_unless_explicitly_rolled(self):
        dice = DiceSet()
        dice.roll(5)
        first_time = dice.values
        second_time = dice.values
        self.assertEqual(first_time, second_time)

    def test_dice_values_should_change_between_rolls(self):
        dice = DiceSet()

        dice.roll(5)
        first_time = dice.values

        dice.roll(5)
        second_time = dice.values

        self.assertNotEqual(first_time, second_time, \
            "Two rolls should not be equal")

        # THINK ABOUT IT:
        #
        # If the rolls are random, then it is possible (although not
        # likely) that two consecutive rolls are equal.  What would be a
        # better way to test this?

        # Answer: loop it few times and compare consequent results with previous ones
        # and define a ratio how many times values can repeat

    def test_dice_multiple_time_to_check_that_were_getting_usually_random_values(self):
        """http://stackoverflow.com/questions/1267869/how-can-i-force-division-to-be-floating-point-in-python"""
        dice = DiceSet()
        no_of_rolls = 5
        target_ratio = 0.02
        curr_ratio = 0
        no_of_loops = 10

        # roll 1st time
        dice.roll(no_of_rolls)
        curr = dice.values
        for r in range(no_of_loops):
            dice.roll(no_of_rolls)
            nxt = dice.values
            #print curr, nxt
            # Due to the nature of Sets the comparison will be unordered!!!!!!
            if set(curr) == set(nxt):
                curr_ratio += (1 / no_of_loops)
                print "curr == nxt !!!"
                print curr, nxt
            curr = nxt
        self.assertTrue(target_ratio >= curr_ratio, "Duplicate Ratio=%f should be lower than target ratio=%f" % (curr_ratio, target_ratio))


    def test_you_can_roll_different_numbers_of_dice(self):
        dice = DiceSet()

        dice.roll(3)
        self.assertEqual(3, len(dice.values))

        dice.roll(1)
        self.assertEqual(1, len(dice.values))
