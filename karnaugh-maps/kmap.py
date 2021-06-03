#!/usr/bin/env python
"""Karnaugh-Map Problem Generator

TODO
"""

from qm import QuineMcCluskey
import itertools
import random
import string

NUM_QUESTIONS = 40
NUM_BITS = 4 # If you change this, change VARS and TEMPLATE.
VARS = ['A', 'B', 'C', 'D']

# These limits are for the numbers of ones (and the numbers of zeroes)
# in the truth table/Karnaugh map.
MIN_ONES = 4
MAX_ONES = 7

# Limit to 3 products so we can provide answers with all 3*2*1 orderings.
# Respondus/Canvas limits us to 10 answers.
NUM_PRODUCTS = 3

TEMPLATE = """
Type: F
Title: KM1-{number}
{number}. Consider a function F with 4 1-bit inputs A, B, C, and D. We can treat those 4 bits as a number N in the range 0-15 (inclusive), where A is the most significant bit and D is the least significant bit.[html]<br/><br/>[/html]Let F(N) be 0 when N is any of {zeroes}, and let F(N) be 1 when N is any of {ones}. In all other cases, we don't care what the value of F is.[html]<br/><br/>[/html]Create a truth table and Karnaugh map for the function F and give the minimal sum-of-products formula. You may put your products in any order, but the terms within them must be alphabetized (e.g., write "A&~B", not "~B&A").

{answers}
"""

def partition_ints():
    nums = list(range(1 << NUM_BITS))
    random.shuffle(nums)
    num_zeroes = random.randint(MIN_ONES, MAX_ONES)
    num_ones = random.randint(MIN_ONES, MAX_ONES)
    zeroes = sorted(nums[0:num_zeroes])
    ones = sorted(nums[num_zeroes:(num_zeroes+num_ones)])
    dont_cares = sorted(nums[num_zeroes+num_ones:])
    return zeroes, ones, dont_cares

def tuple_to_string(tuple):
    letter, modifier = tuple
    if (modifier == '0'):
        return f"~{letter}"
    elif (modifier == '1'):
        return letter
    else:
        return None

def product_to_string(product):
    return '&'.join(filter(None, [tuple_to_string(t) for t in zip(VARS, product)]))

def generate_answer_strings(products):
    answers = ['|'.join(plist) for plist in itertools.permutations(products)]
    pairs = [f"{letter}. {ans}" for (letter, ans) in zip(string.ascii_lowercase, answers)]
    return '\n'.join(pairs) 

def print_question(num):
    while True:
        zeroes, ones, dont_cares = partition_ints()
        results = QuineMcCluskey().simplify(ones = ones, dc = dont_cares, num_bits = NUM_BITS)
        if len(results) == NUM_PRODUCTS:
            products = [product_to_string(product) for product in results]
            answers = generate_answer_strings(products)
            print(TEMPLATE.format(number = (num + 1), zeroes = zeroes, ones = ones, answers = answers))
            return

for i in range(NUM_QUESTIONS):
    print_question(i)
