#!/usr/bin/env python

import sys

def sumOfSquares(num):
  sum = 0
  for i in range(num):
    sum += (i+1)**2
  return sum

def squareOfSums(num):
  sum = 0
  for i in range(num):
    sum += i+1
  return sum**2

if len(sys.argv) > 1:
  num = int(sys.argv[1])
  print squareOfSums(num) - sumOfSquares(num)


