#!/usr/bin/env python

import sys

def root(n):
  return int(n**0.5)

def isPythag(a,b,c):
  return (a**2 + b**2) == c**2

def findABCOf(n):
  a = 1
  b = 2
  c = 3

  while True:
    if (a + b + c) == n and isPythag(a,b,c):
      return a*b*c

    if c == n:
      c = b
      b += 1
    if b == n:
      b = a+1
      a += 1
    if a == n:
      return 0

    c += 1 

if len(sys.argv) > 1:
  num = int(sys.argv[1])
  print findABCOf(num)
