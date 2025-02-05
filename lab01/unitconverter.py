import math

input = input("Type in a number, a space, and a unit to convert (in, cm, yd, m, oz, g, lb, kg): ")

# splits number and unit with a space
string_number, unit = input.split()

# string converts to float
number = float(string_number) 


if unit == "in":
    # converts inches to centimeters
    converted_number = number * 2.54
    truncate_number = math.trunc(converted_number * 100) / 100
    print(f"{input} = {truncate_number} cm")

elif unit == "cm":
    # converts centimeters to inches
    converted_number = number / 2.54
    truncate_number = math.trunc(converted_number * 100) / 100
    print(f"{input} = {truncate_number} in")

elif unit == "yd":
    # converts yards to meters
    converted_number = number * 0.9144
    truncate_number = math.trunc(converted_number * 100) / 100
    print(f"{input} = {truncate_number} m")

elif unit == "m":
    # convert meters to yards
    converted_number = number / 0.9144
    truncate_number = math.trunc(converted_number * 100) / 100
    print(f"{input} = {truncate_number} yd")

elif unit == "oz":
    # convert ounces to grams
    converted_number = number * 28.349523125
    truncate_number = math.trunc(converted_number * 100) / 100
    print(f"{input} = {truncate_number} g")

elif unit == "g":
    # convert grams to ounces
    converted_number = number / 28.349523125
    truncate_number = math.trunc(converted_number * 100) / 100
    print(f"{input} = {truncate_number} oz")

elif unit == "lb":
    # convert pounds to kilograms
    converted_number = number * 0.45359237
    truncate_number = math.trunc(converted_number * 100) / 100
    print(f"{input} = {truncate_number} kg")

elif unit == "kg":
    # convert kilograms to pounds
    converted_number = number / 0.45359237
    truncate_number = math.trunc(converted_number * 100) / 100
    print(f"{input} = {truncate_number} lb")

else:
    print("Unable to process unit entered, try again.")
