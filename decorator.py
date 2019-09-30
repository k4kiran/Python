
#subtract function implemented for positive subtraction
def subtract1(a,b):
  print(a - b)

#Decorator function to swap the values before function
def decor_subtract1(func):
  def inner(a,b):
    if a < b:
      a,b = b,a 
      return func(a,b)
  return inner
  
#linking both functions
subtract1 = decor_subtract1(subtract1)
num1 = input("enter first number:",)
num2 = input("enter second number:",)
subtract1(int(num1),int(num2))








