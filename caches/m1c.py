#!/usr/bin/env python

"""Average Memory Access Time (AMAT) Problem Generator

This script generates problems where the student is given hit rates
and access times for L1 and L2 caches and the main memory access time
and is required to calculate the average memory access time.
"""

from random import randint

NUM_QUESTIONS = 40
BASE_TIME = 1
MIN_L1_HIT_RATE = 85
MAX_L1_HIT_RATE = 98
MIN_L2_HIT_RATE = 95  # cumulative hit rate, guaranteed to be greater than L1 hit rate
MAX_L2_HIT_RATE = 99
MIN_L2_ACCESS_TIME = 2
MAX_L2_ACCESS_TIME = 6
MIN_MEM_ACCESS_TIME = 20
MAX_MEM_ACCESS_TIME = 100

TEMPLATE = """
Type: F
Title: M1C-{0}
{0}. A processor has 2 levels of caches. There is a base cost of 1 cycle per memory access.
If there is an L1 cache hit, there is no additional cost; otherwise, there is a miss penalty of
{1} cycles if the item is found in the L2 cache or {2} cycles if it needs to be retrieved from main memory.
Thus, access times range from {3}-{4} cycles. The L1 hit rate is {5}%, and the cumulative L2 hit rate
is {6}%. What is the average memory access time in cycles?
a. {7}
"""

for index in range(NUM_QUESTIONS):
    l1_hits = randint(MIN_L1_HIT_RATE, MAX_L1_HIT_RATE)
    l2_hits = randint(max(l1_hits, MIN_L2_HIT_RATE) + 1, MAX_L2_HIT_RATE)
    l2_time = randint(MIN_L2_ACCESS_TIME, MAX_L2_ACCESS_TIME)
    mem_time = randint(MIN_MEM_ACCESS_TIME, MAX_MEM_ACCESS_TIME)
    max_time = BASE_TIME + mem_time
    amat = 100 * BASE_TIME + (l2_hits - l1_hits) * l2_time + (100 - l2_hits) * mem_time
    print(TEMPLATE.format(index, l2_time, mem_time, BASE_TIME, max_time, l1_hits, l2_hits, amat / 100))

