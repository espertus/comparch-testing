#!/usr/bin/env python

"""Average Memory Access Time (AMAT) Problem Generator

This script generates problems where the student is given hit rates
and access times for L1 and L2 caches and the main memory access time
and is required to calculate the average memory access time.
"""

from random import randint

NUM_QUESTIONS = 40
MIN_L1_HIT_RATE = 85
MAX_L1_HIT_RATE = 98
MIN_L2_HIT_RATE = 95  # cumulative hit rate, guaranteed to be greater than L1 hit rate1
MAX_L2_HIT_RATE = 99
MIN_L2_ACCESS_TIME = 2
MAX_L2_ACCESS_TIME = 6
MIN_MEM_ACCESS_TIME = 20
MAX_MEM_ACCESS_TIME = 100

TEMPLATE = """
Type: F
Title: M1-{0}
{0}. A processor has 2 levels of caches. The L1 cache has an access time of 1 cycle and a hit rate of {1}%. The L2 cache has an access time of {2} cycles and a cumulative hit rate of {3}%. Main memory accesses take {4} cycles. All of the acccess times are concurrent (done in parallel). What is the average memory access time in cycles? Enter a decimal number.
a. {5}
"""

for index in range(NUM_QUESTIONS):
    l1_hits = randint(MIN_L1_HIT_RATE, MAX_L1_HIT_RATE)
    l2_hits = randint(max(l1_hits, MIN_L2_HIT_RATE) + 1, MAX_L2_HIT_RATE)
    l2_time = randint(MIN_L2_ACCESS_TIME, MAX_L2_ACCESS_TIME)
    mem_time = randint(MIN_MEM_ACCESS_TIME, MAX_MEM_ACCESS_TIME)
    amat = l1_hits * 1 + (l2_hits - l1_hits) * l2_time + (100 - l2_hits) * mem_time
    print(TEMPLATE.format(index, l1_hits, l2_time, l2_hits, mem_time, amat / 100))

