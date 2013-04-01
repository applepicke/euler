#!/usr/bin/env python

import sys

def divisibleUpTo(num):
  start = num

  while True:
    for i in range(1, num+1):
      if start % i != 0:
        start += num
        break 
      if i+1 == num:
        return start    
  
if len(sys.argv) > 1:
  print divisibleUpTo(int(sys.argv[1]))

else:
  print divisibleUpTo(20)
