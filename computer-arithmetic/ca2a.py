#!/usr/bin/env python

"""Decimal to Two's Complement Problem Generator

This script generates problems where the user must convert negative decimal
numbers into 8-bit two's complement notation.
"""

import random

NUM_QUESTIONS = 20
MIN_DECIMAL = -100
MAX_DECIMAL = -5

TEMPLATE = """
Type: F
Title: CA2A-{0}
{0}. Convert the decimal number {1} into 8-bit two's complement notation.
a. {2}
"""

def to2C(n):
    return bin(n & 0b11111111)[2:]

nums = list(set(random.sample(range(MIN_DECIMAL, MAX_DECIMAL), NUM_QUESTIONS)))
for index, n in enumerate(nums):
    print(TEMPLATE.format(index, n, to2C(n )))
  
  
  
