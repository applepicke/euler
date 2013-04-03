#!/usr/bin/env python

import sys

def isPrime(n):
  for i in range(2, int(n**0.5+1)):
    if n % i == 0:
      return False
  return True

def sumOfPrimesBelow(n):
  sum = 0
  for i in range(2, n):
    if isPrime(i):
      sum += i
  return sum

if len(sys.argv) > 1:
  num = int(sys.argv[1])
  print sumOfPrimesBelow(num)
