import math

def guessNumber(n):
  # lys must be a sorted_array at first
  
  first = 1
  last = n
  while (first <= last):
      mid = first + (last - first) // 2;
      res = guess(mid)
      if res == 0:
        return mid
      elif (res < 0):
        last = mid - 1
      else:
        first = mid + 1
  return -1;
