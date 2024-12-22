# Using walrus operator 
if(n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long. (Total {n} elements, expected < 3)")
    



# basic way 
n = [1, 2, 3, 4, 5]
length = len(n)
if(length > 3):
    print(f"List is too long. (Total {length} elements, expected < 3)")