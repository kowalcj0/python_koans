#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual("The values are one and 2", string)

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)

    def test_any_python_expression_may_be_interpolated(self):
        import math  # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5), \
            decimal_places)
        self.assertEqual("The square root of 5 is 2.2361", string)

    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("let", string[7:10])

    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual('a', string[1])

    def test_single_characters_can_be_represented_by_integers(self):
        """
        https://docs.python.org/2/library/functions.html#ord
        ord(c)
        Given a string of length one, return an integer representing the Unicode
        code point of the character when the argument is a unicode object,
        or the value of the byte when the argument is an 8-bit string.
        For example, ord('a') returns the integer 97, ord(u'\u2020')
        returns 8224. This is the inverse of chr() for 8-bit strings and
        of unichr() for unicode objects. If a unicode argument is given
        and Python was built with UCS2 Unicode, then the character’s code
        point must be in the range [0..65535] inclusive; otherwise
        the string length is two, and a TypeError will be raised.
        """
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))

    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertEqual(["Sausage","Egg","Cheese"], words)

    def test_strings_can_be_split_with_different_patterns(self):
        import re  # import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        self.assertEqual(["the","rain","in","spain"], words)

        # `pattern` is a Python regular expression pattern which matches
        # ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        self.assertEqual(r'\n', string)
        self.assertEqual(2, len(string))

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        self.assertEqual("Now is the time", ' '.join(words))

    def test_strings_can_change_case(self):
        self.assertEqual("Guido", 'guido'.capitalize())
        self.assertEqual("GUIDO", 'guido'.upper())
        self.assertEqual("timbot", 'TimBot'.lower())
        self.assertEqual("Guido Van Rossum", 'guido van rossum'.title())
        self.assertEqual("tOtAlLy AwEsOmE", 'ToTaLlY aWeSoMe'.swapcase())
