str = "mindX"

def reverse_string(str):
  li = list(str)
  result = []
  for _ in range(len(str)):
    result.append(li.pop())
  print(''.join(result))

reverse_string("mindx")

def reverse_string_recursive(str, i):
  length = len(str)
  if i == length // 2:
    return
  temp = str[i]
  str[i] = str[length - i - 1]
  str[length - i -1] = temp

  reverse_string_recursive(str, i + 1)

lis = list(str)
reverse_string_recursive(lis, 0)
print(''.join(lis))  

