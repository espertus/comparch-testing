#!/usr/bin/env python

"""Decimal to IEEE single-precision FP Problem Generator

This script generates problems where the user must convert decimal
numbers into IEEE single-precision floating point notation.
"""

import fp
import random

NUM_QUESTIONS = 20

def coin_toss():
  return random.randint(1, 2) == 1

def make_num():
    """Returns a positive or negative number with absolute value in [2, 100.75]"""
    n = random.randint(2, 100)
    if (coin_toss()):
        n += .5
    if (coin_toss()):
        n += .25
    if (coin_toss()):
        n = -n
    return n
    
TEMPLATE = """
Type: F
Title: CA4-{0}

{0}. When the number {1} is converted to single-precision floating-point format, the sign bit is _, the exponent field holds the eight bits ________, and the first 8 fraction bits are ________.

a. {2:s} {3:s} {4:s}
"""

for i in range(1, NUM_QUESTIONS):
  n = make_num()
  s = fp.float32_to_string(n)
  print(TEMPLATE.format(i, n, s[0], s[1:9], s[9:17]))
  
