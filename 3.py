#!/usr/bin/env python

import sys
from operator import mul

num = 600851475143
counter = 2
primes = []

def isPrime(num):
  for i in range(2, int(num**0.5+1)):
    if num % i == 0:
      return False
  return True

def primeFactors(num):
  if isPrime(num):
    primes.append(num)
    return
  else:
    count = 2
    while num % count != 0:
      count += 1
    newNum = num / count
    primeFactors(count)
    primeFactors(newNum)
   

if len(sys.argv) > 2:
  print isPrime(int(sys.argv[2]))
  sys.exit() 

elif len(sys.argv) > 1:
  primeFactors(int(sys.argv[1]))
else:
  primeFactors(num)

print primes
print "total is : " + str(reduce(mul, primes, 1))


