import math

def binary_search(lys, val):
  # lys must be a sorted_array at first
  
  first = 0
  last = len(lys)-1
  index = -1
  while (first <= last) and (index == -1):
      mid = (first+last)//2
      if lys[mid] == val:
          index = mid
      else:
          if val<lys[mid]:
              last = mid -1
          else:
              first = mid +1
  return index

# print(binary_search([10,20,30,40,50,60], 20))