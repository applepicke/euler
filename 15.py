#!/usr/bin/env python

import sys

def lattice(x, y, n):
  total = 0
  if x < n:
    total += lattice(x+1, y, n)
  if y < n: 
    total += lattice(x, y+1, n)
  if x == n and y == n:
    return 1
  return total

if len(sys.argv) > 1:
  num = int(sys.argv[1])
  print lattice(1, 0, num) * 2 
