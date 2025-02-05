import math

a = input("Type in the length of side 1: ")
b = input("Type in the length of side 2: ")

a = float(a)  
b = float(b)

c = math.sqrt(a**2 + b**2)

truncate_c = math.trunc(c * 100) / 100

print(f"The hypotenuse is {truncate_c}")
