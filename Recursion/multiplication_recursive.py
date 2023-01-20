def multiplication(num1,num2):
  if num1 == 0 or num2 == 0:
    return 0
  
  return num1 + multiplication(num1,num2-1)



# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)