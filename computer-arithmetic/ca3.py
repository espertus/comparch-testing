#!/usr/bin/env python

"""Two's Complement Ordering Problem Generator

This script generates problems where the user must order 4 numbers expressed
in 8-bit two's complement notation.
"""

from random import randint
from random import shuffle

NUM_QUESTIONS = 20

TEMPLATE = """
Type: F
Title: CA3-{0}
{0}. The following numbers are in two's complement notation. Please order them from lowest (most negative) to highest (most positive). For example, if they were already correctly ordered, your answer would be ABCD.

{1}

For full credit, answer the problem without converting all of the numbers to decimal.
a. {2}
"""

def to2C(n):
  return '{:08b}'.format(n & 0b11111111)

for index in range(NUM_QUESTIONS):
  letters = ["A", "B", "C", "D"]
  shuffle(letters)
  nums = [randint(-100,-50), randint(-49, -1), randint(1,50), randint(51, 100)]
  responses = list(map(lambda i: f"{letters[i]} = {to2C(nums[i])}", range(len(letters))))
  responses.sort() # Alphabetize for printing
  print(TEMPLATE.format(index, "\n".join(responses), "".join(letters)))

  
  
  
