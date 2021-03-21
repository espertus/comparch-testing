#!/usr/bin/env python

"""Utilities for printing floating-point big patterns

These functions were written by Mark Ransom and posted to Stack Overflow.
https://stackoverflow.com/a/16445458/631051
"""

import struct

def _float32_bit_pattern(value):
    return sum(b << 8*i for i,b in enumerate(struct.pack('f', value)))

def _int_to_binary(value, bits):
    return bin(value).replace('0b', '').rjust(bits, '0')

def float32_to_string(value):
    return _int_to_binary(_float32_bit_pattern(value), 32)

