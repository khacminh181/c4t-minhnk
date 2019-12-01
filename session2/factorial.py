def factorial(n):
  if (n == 1):
    return n
  else: 
    return n * factorial(n - 1)

print(factorial(3))
  
def factorial_loop(n):
  factorial = 1
  for i in range (1, n+1):
    factorial *= i # factorial = factorial * i
  return factorial

print(factorial_loop(3))