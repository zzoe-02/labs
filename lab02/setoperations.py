def make_set(data):
    newlist = []
    for number in data:
        if number not in newlist:
            newlist.append(number)
    return newlist


def is_set(data):
    if data is None:
        return False
    
    processed = []
    for number in data:
        if number in processed:
            return False 
        processed.append(number)
    return True


def union(setA, setB):
    if setA is None or setB is None:
        return []

    for number in setA:
        if setA.count(number) > 1:
            return []  

    for number in setB:
        if setB.count(number) > 1:
            return [] 

    newlist = []
    for number in setA + setB:
        if number not in newlist:
            newlist.append(number)
    return newlist


def intersection(setA, setB):
    if setA is None or setB is None:
        return []

    for number in setA:
        if setA.count(number) > 1:
            return []

    for number in setB:
        if setB.count(number) > 1:
            return []

    newlist = []
    for number in setA:
        if number in setB and number not in newlist:
            newlist.append(number)
    return newlist

#test
print(make_set([1, 2, 3, 4, 4, 5])) 

print(is_set([1, 2, 3, 4, 5])) 

print(is_set([5, 5])) 

print(is_set([])) 

print(is_set(None)) 

print(union([1, 2], [2, 3])) 

print(union([], [2, 3])) 

print(union([1, 1, 1], [2, 3]))  

print(intersection([1, 2], [2, 3]))  

print(intersection([], [2, 3]))  

print(intersection([1, 1, 1], [2]))  