#!/usr/bin/env python

"""Base Conversion Problem Generator

This script generates problems where the user must convert decimal numbers
into binary, octal, and hexadecimal. The problems can be imported into
Canvas using Respondus.
"""

import random

NUM_QUESTIONS = 20
MIN_DECIMAL = 70
MAX_DECIMAL = 150

TEMPLATE = """
Type: F
Title: CA1-{0}
{0}. The decimal number {1} can be represented as ________ (binary), ___ (octal) and __ (hexadecimal). Please omit leading zeroes.
a. {1:b} {1:o} {1:x}
b. {1:b} {1:o} {1:X}
c. {1:08b} {1:o} {1:x}
d. {1:08b} {1:o} {1:X}
"""

nums = list(set(random.sample(range(MIN_DECIMAL, MAX_DECIMAL), NUM_QUESTIONS)))
for index, n in enumerate(nums):
    print(TEMPLATE.format(index, n))
  
