def first_uppercase_letter(str):
  for i in str:
    if(i.isupper()):
      return i

print(first_uppercase_letter("mnindX"))

def first_uppercase_letter_recursive(str, i):
  if(str[i].isupper()):
    return str[i]
  else :
    return first_uppercase_letter_recursive(str, i+1)

print(first_uppercase_letter_recursive("mIndX", 0))