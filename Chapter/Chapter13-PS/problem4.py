from functools import reduce
arr  = [111, 2, 6455, 5553, 635, 65, 74, 45,55]


def greater(a, b):
    if (a > b):
        return a 
    return b

print(reduce(greater, arr))