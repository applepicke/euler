#!/usr/bin/env python

import sys

map = {
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety",
  100: "hundred",
  1000: "thousand"
}


def addLettersBetween(num):
  total = 0
  for i in range(1, num+1):
    total += len(countLetters(i))
  return total 

def countLetters(num):
  count = ""
  if num >= 1000:
    count += findThousandth(num)
    num %= 1000

  if num >= 100:
    count += findHundredth(num)
    num %= 100
  
  # Add 'and'
  if num > 0 and len(count) > 0:
    count += "and"

  if num > 0:
    count += findTenth(num)
    num %= 10
    
  return count

def findThousandth(num):
  if num < 1000:
    return 0

  pre = map[num/1000]
  post = map[1000]
  return pre + post

def findHundredth(num):
  if num < 100:
    return 0
  pre = map[num/100]
  post = map[100]
  return pre + post

def findTenth(num):
  if num < 20:
    return map[num]

  pre = map[num - num % 10]
  post = ""

  num %= 10

  if num > 0:
    post = map[num]

  return pre + post

def findOne(num):
  return map[num]

if len(sys.argv) > 1:
  num = int(sys.argv[1])
  print addLettersBetween(num)
  
