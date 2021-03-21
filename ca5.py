#!/usr/bin/env python

"""IEEE single-precision FP Ordering Problem Generator

This script generates problems where the user must order 4 numbers expressed
in IEEE floating-point notation.
"""

from random import randint
from random import shuffle
import fp
import struct

NUM_QUESTIONS = 20

TEMPLATE = """
Type: F
Title: CA5-{0}
{0}. The following numbers are in single-precision floating point format. Please order them from lowest (most negative) to highest (most positive). For example, if they were already correctly ordered, your answer would be ABCD.

{1}

For full credit, answer the problem without converting all of the numbers to decimal.
a. {2}
"""

def toFP(value):
    s = fp.float32_to_string(value)
    return f"{s[0]} {s[1:9]} {s[9:32]}"

for index in range(NUM_QUESTIONS):
    letters = ["A", "B", "C", "D"]
    shuffle(letters)
    nums = [randint(-100,-50), randint(-49, -1), randint(1,50), randint(51, 100)]
    responses = list(map(lambda i: f"{letters[i]} = {toFP(nums[i])}", range(len(letters))))
    responses.sort() # Alphabetize for printing
    print(TEMPLATE.format(index, "\n".join(responses), "".join(letters)))

  
