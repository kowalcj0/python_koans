#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if any(v <= 0 for k,v in locals().items()):
        raise TriangleError, "All sides of the triangle has to be > 0"
    if not abs(b-c) < a < (b + c):
        raise TriangleError, "This can't be a triangle, as it doesn't matches formula: |b-c|<a<b+c"
    if a == b == c:
        return 'equilateral';
    elif (a == b) or (b == c) or (a == c):
        return 'isosceles'
    elif a != b != c:
        return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
