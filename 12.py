#!/usr/bin/env python

import sys

def countDivisors(n):
  count = 0
  for i in range(1, int(n**0.5+1)): 
    if n % i == 0:
      count += 2
      if n / i == i:
        count -= 1
  return count

def tranglify(n):  
  count = 1
  sum = 0

  while True:
    if countDivisors(sum) > n: 
      return sum

    sum += count    
    count += 1

if len(sys.argv) > 1:
  num = int(sys.argv[1])
  print tranglify(num)    
