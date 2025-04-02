#1
def product_of_digits(x):
    x = abs(x)
    if x < 10:
        return x
    else:
        return (x % 10) * product_of_digits(x // 10)
#2
def array_to_string(a, index):
    if index >= len(a):
        return ""
    else:
        if index == len(a) - 1:
            return str(a[index])
        else:
            return str(a[index]) + "," + array_to_string(a, index + 1)
#3
def log(base, value):
    if base <= 1 or value <= 0:
        raise ValueError("Value must be greater than 0 and base must be greater than 1!")
    if value < base:
        return 0
    else:
        return 1 + log(base, value // base)
