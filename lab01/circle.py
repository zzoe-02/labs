import math

x = input("Type the radius of the circle: ")

try:
    radius = float(x)
    
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    
    truncate_area = math.trunc(area * 100) / 100
    truncate_perimeter = math.trunc(perimeter * 100) / 100
    
    print(f"The circle with radius {radius} has an area of {truncate_area} and a perimeter of {truncate_perimeter}")
    
except:
    print("Not valid, please type another number")
