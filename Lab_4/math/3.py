import math

a = int(input("Input number of sides: "))
b = int(input("Input the length of a side: "))

P = a*b

A = b/(2*math.tan(math.pi/a))

Area = int((P*A)/2)

print("The area of the polygon is:" , Area)