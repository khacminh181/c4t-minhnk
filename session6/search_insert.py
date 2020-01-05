import math

def search_insert(lys, val):
  # lys must be a sorted_array at first
  
  first = 0
  last = len(lys)-1
  index = -1
  while (first <= last) and (index == -1):
      mid = (first+last)//2
      if lys[mid] == val:
          index = mid
          return index
      else:
          if val<lys[mid]:
              last = mid -1
          else:
              first = mid +1
  return first

print(search_insert([10,20,30,40,50,60], 15))