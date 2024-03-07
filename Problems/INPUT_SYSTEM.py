import sys

# ______________________________________________________________________________________________________
import math
from bisect import *
from heapq import *
from collections import defaultdict as dd
from collections import OrderedDict as odict
from collections import Counter as cc
from collections import deque
from itertools import groupby

sys.setrecursionlimit(20 * 20 * 20 * 20 + 10)  # this is must for dfs


# --------------- Some input functions --------------------------#
def get_ints(): return map(int, sys.stdin.readline().strip().split())


def get_list(): return list(map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


# DaRk DeveLopeR


# taking input as string
input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda: list(map(int, sys.stdin.readline().rstrip("\r\n").split()))
mod = 10 ** 9 + 7
Mod = 998244353
INF = float('inf')


# ---------------------- USER DEFINED INPUT FUNCTIONS ----------------------#
def takein():
    return int(sys.stdin.readline().rstrip("\r\n"))


# input the string

def takesr():
    return sys.stdin.readline().rstrip("\r\n")


# input int array
def takeiar():
    return list(map(int, sys.stdin.readline().rstrip("\r\n").split()))


# input string array
def takesar():
    return list(map(str, sys.stdin.readline().rstrip("\r\n").split()))


# input values for the different variables
def takeivr():
    return map(int, sys.stdin.readline().rstrip("\r\n").split())


def takesvr():
    return map(str, sys.stdin.readline().rstrip("\r\n").split())


# I have to use this for any input function:
# Personal Header
Iarr = lambda: list(map(int, input().split()))
Sarr = lambda: list(map(str, input().split()))
# End Header
