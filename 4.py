#!/usr/bin/env python
import sys

def isPalindrome(num):
  numStr = str(num)
  length = len(numStr)
  pos = 0
  while pos < length / 2 + 1:
    if numStr[pos] != numStr[length-pos-1]:
      return False
    pos += 1
  return True

def findPal(n1, n2):
  largest = 0

  while n1 > 99:
    if n2 < 100:
      n2 = 999
      n1 -= 1
    
    if isPalindrome(n1 * n2) and (n1 * n2) > largest:
      largest = n1 * n2
    n2 -= 1

  return largest
    

if len(sys.argv) > 2:
  print findPal(int(sys.argv[1]), int(sys.argv[2]))
else:
  print findPal(999, 999)
  
