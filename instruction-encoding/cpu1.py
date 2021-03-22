#!/usr/bin/env python

"""Instruction Encoding Problem Generator

This script generates MIPS instructions for the user to encode into binary.
"""

from random import randint
from random import shuffle
import random

NUM_QUESTIONS = 40
MIN_REG = 1
MAX_REG = 20
MIN_IMM = 0
MAX_IMM = 90
# Instructions using the beq and j opcodes are not yet generated.
op_to_encoding = {'lw': '101011', 'sw': '100011', 'beq': '000100', 'j': '000010'}
funct_to_encoding = {'add': '100000', 'and': '100100', 'or': '100101', 'slt': '101010', 'sub': '100010'}
memops = ['lw', 'sw']

TEMPLATE = """
Type: F
Title: CPU1-{0}
{0}. Encode the following instruction, expressing the answer as 32 bits. If you use spaces, put one between each field.

{1}
"""

def get_reg():
  return randint(MIN_REG, MAX_REG)

def encode_rtype(index):
  opcode = random.choice(list(funct_to_encoding.keys()))
  rd = get_reg()
  rs = get_reg()
  rt = get_reg()
  inst = f"{opcode} $r{rd}, $r{rs}, $r{rt}"
  encoding = f"000000 {rs:05b} {rt:05b} {rd:05b} 00000 {funct_to_encoding[opcode]}"
  return TEMPLATE.format(index, f"{inst}\n\na. {encoding}\nb. {encoding.replace(' ', '')}")

def encode_itype(index):
  opcode = random.choice(memops)
  rs = get_reg()
  rt = get_reg()
  imm = randint(MIN_IMM, MAX_IMM)
  inst = f"{opcode} $r{rt}, {imm}($r{rs})"
  encoding = f"{op_to_encoding[opcode]} {rs:05b} {rt:05b} {imm:016b}"
  return TEMPLATE.format(index, f"{inst}\n\na. {encoding}\nb. {encoding.replace(' ', '')}")

for index in range(1, NUM_QUESTIONS, 2):
  print(encode_rtype(index))
  print(encode_itype(index + 1))


  
  
  
