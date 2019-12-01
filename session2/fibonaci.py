def fibonaci(n):
  if (n < 2):
    return n
  else:
    a = 0
    b = 1
    for _ in range(2, n+1):
      c = a + b
      a = b
      b = c 
    return c

print(fibonaci(4))

def fibonaci_recursion(n):
  if (n < 2):
    return n
  else:
    return fibonaci_recursion(n-1) + fibonaci_recursion(n-2)

print(fibonaci_recursion(4))