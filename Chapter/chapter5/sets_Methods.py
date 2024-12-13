s = {1, 5, 32, 54,5, 5, 5, "Harry"}

print(s, type(s)) # {32, 1, 'Harry', 5, 54} <class 'set'>

s.add(566)
print(s, type(s)) # {32, 1, 'Harry', 5, 54, 566} <class 'set'>

s.remove(1)
print(s, type(s)) # {32, 'Harry', 5, 54, 566} <class 'set'>