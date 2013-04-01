#!/usr/bin/env python

total = 0
totalEven = 0

prev1 = 0
prev2 = 1
new = 0

while new < 10**6*4:
  new = prev1 + prev2
  
  total += new
  if new % 2 == 0:
    totalEven += new 

  prev1 = prev2
  prev2 = new
  
print "Total = " + str(total)
print "Total Even = " + str(totalEven)
print "New = " + str(new)
