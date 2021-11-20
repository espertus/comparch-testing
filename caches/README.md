# Caches

This script generates cache performance problems.

## Learning outcomes

### M1 Calculating average memory access times (AMATs)

#### M1A Two-level cache

Sample question:

> A processor has 2 levels of caches. The L1 cache has an access time of 1 cycle and a hit rate of 87%. 
> The L2 cache has an access time of 6 cycles and a cumulative hit rate of 99%. Main memory accesses take 
> 49 cycles. All of the access times are concurrent (done in parallel). What is the average memory access 
> time in cycles? Enter a decimal number.

#### M1B Three-level cache

Sample question:

> A processor has 3 levels of caches. The L1 cache has an access time of 1 cycle and a hit rate of 87%. The L2 cache has an access time of 4 cycles and a cumulative hit rate of 96%. The L3 cache has an access time of 14 cycles and a cumulative hit rate of 99%. Main memory accesses take 75 cycles. All of the access times are concurrent (done in parallel). What is the average memory access time in cycles? Enter a decimal number.

#### M1C Two-level cache

This differs from M1A by having a base time and no L1 penalty.

> A processor has 2 levels of caches. There is a base cost of 1 cycle per memory access.
If there is an L1 cache hit, there is no additional cost; otherwise, there is a miss penalty of
3 cycles if the item is found in the L2 cache or 55 cycles if it needs to be retrieved from main memory.
Thus, access times range from 1-56 cycles. The L1 hit rate is 86%, and the cumulative L2 hit rate
is 97%. What is the average memory access time in cycles?