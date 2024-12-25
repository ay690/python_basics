from functools import reduce

# Map
L = [1, 2, 3, 4, 5, 6, 8 , 9, 10, 302]

square = lambda x: x*x

sqList = map(square, L)

print(list(sqList))

# Filter
def even(n):
    if(n % 2 == 0):
        return True
    
    return False

onlyEven = filter(even, L)
print(list(onlyEven))

# Reduce
# def sum(a, b):
#     return a + b
# or

sum = lambda a,b: a + b

mul = lambda x,y: x * y

print(reduce(sum, L))
print(reduce(mul, L))
