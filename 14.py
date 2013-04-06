#!/usr/bin/env python

import sys

chain = {}

def collatzify(n):
  orig_num = n
  count = 1  

  while n > 1:
 
    if chain.has_key(str(n)):
      count += chain[str(n)]
      break
    
    n = (n / 2) if (n % 2 == 0) else (3*n + 1)
    count += 1
  
  chain[str(orig_num)] = count
  return count

def longestSequenceUnder(n):
  longest = 0
  longest_num = 0
  for i in range(2, n):
    num = collatzify(i)
    if num > longest:
      longest = num
      longest_num = i
     
  return longest_num
    

if len(sys.argv) > 1:
  num = int(sys.argv[1])
  print longestSequenceUnder(num)
  
    
