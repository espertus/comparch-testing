#!/usr/bin/env python

"""Two's Complement to Decimal Problem Generator

This script generates problems where the user must convert negative 8-bit
two's complement numbers into decimal notation.
"""

import random

NUM_QUESTIONS = 20
MIN_DECIMAL = -100
MAX_DECIMAL = -5

TEMPLATE = """
Type: F
Title: CA2B-{0}
{0}. Convert the 8-bit two's complement number {2} into decimal notation.
a. {1}
"""

def to2C(n):
    return bin(n & 0b11111111)[2:]

nums = list(set(random.sample(range(MIN_DECIMAL, MAX_DECIMAL), NUM_QUESTIONS)))
for index, n in enumerate(nums):
    print(TEMPLATE.format(index, n, to2C(n)))
  
  
