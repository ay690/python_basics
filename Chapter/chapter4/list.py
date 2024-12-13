friends = ["Apple", "Orange", 5, 783.78, False, "Aman", "Rohit"]

print(friends[0]) # Apple
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0]) # Grapes
print(friends[1:4]) # ['Orange', 5, 783.78]