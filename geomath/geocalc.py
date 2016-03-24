"""
GeoMath - Analytical Geometry Module
Originally written by: Vinicius Mesel and Eduardo Mendes
Last Modification: 23/03/2016 #vmesel
"""

from math import sqrt


class Point:
    "Object type cartesian Point"

    # Defines the Point(x, y)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Defines the output of the point
    def __repr__(self):
        return (("Point(%s, %s)") % (self.x, self.y))

    # Defines the distance between two points
    def distance(self, point_two):
        return sqrt(
            pow(point_two.x - self.x, 2) + pow(point_two.y - self.y, 2)
        )

    # Defined the midpoint between two points
    def midpoint(self, point_two):
        return(
            (self.x + point_two.x) / 2, (self.y + point_two.y) / 2
        )


class Figure:

    def squarearea(a):
        return(a**2)

    def barycenter(points):
        i = 0
        arrayx = []
        arrayy = []
        for point in points:
            arrayx.append(point.x)
            arrayy.append(point.y)

        XPoint = sum(arrayx) / len(arrayx)
        YPoint = sum(arrayx) / len(arrayy)

        return(("Point(%s, %s)") % (XPoint, YPoint))


# Defining tests for the TravisCI and Build Checking
from nose import with_setup  # optional
import unittest


class PointTest(unittest.TestCase):

    def test_two(self):
        assert(Point(9, 8).distance(Point(1, 2)) == 10)

    def test_three(self):
        assert(str(Point(9, 8).midpoint(Point(1, 2)) == "(5.0, 5.0)"))

    def test_four(self):
        assert(Figure.squarearea(4) == 16)

    def test_five(self):
        assert(Figure.barycenter([Point(1, 2), Point(2, 3), Point(
            4, 5)]) == "Point(2.3333333333333335, 2.3333333333333335)")

if __name__ == '__main__':
    unittest.main()
