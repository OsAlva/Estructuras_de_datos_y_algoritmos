# define the fibonacci() function below...
def fibonacci(n):
  #caso base
  if n == 0:
    return n
  elif n == 1:
    return n
  #caso recursivo
  return fibonacci(n-2) + fibonacci(n-1)





fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"
