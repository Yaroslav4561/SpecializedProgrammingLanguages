def factorial(number):
  res = 1
  while number > 1:
      res *= number
      number -= 1
  return res
    
number = int(input("Enter a number: "))
print(factorial(number))
