#Pythagoras' theorem

def hypotenuse(a,b):
  c_squared = a**2 + b**2
  c = c_squared**0.5
  print('The length of the hypotenuse is ', c)

a = float(input("Enter 1st length: "))
b = float(input("Enter 2nd length: "))

hypotenuse(a,b)
