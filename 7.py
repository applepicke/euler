#!/usr/bin/env python

import sys

def isPrime(n):
  for i in range(2, int(n**0.5+1)):
    if n % i == 0:
      return False
  return True

def nthPrime(n):
  current = 1
  count = 0
  while count <= n:
    if isPrime(current):
      count += 1
    current += 1
    
  return current-1

if len(sys.argv) > 1:
  num = int(sys.argv[1])
  print nthPrime(num)
    
