#!/bin/python

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, sidea, sideb):
        self.sidea = sidea
        self.sideb = sideb

    def area_of_rectangle(self):
        result = self.sidea * self.sideb
        return result


class Circle:
    pi = math.pi
    def __init__(self, radius):
        self.radius = radius


    def area_of_rectangle(self):
        result = self.radius * self.pi * 0.5
        return result


# if __name__ == '__main__':

print(math.pi)