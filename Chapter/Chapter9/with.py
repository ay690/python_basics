f = open("file.txt")
print(f.read())
f.close()

# this same can be achieved with the help of "with" statement

with open("file.txt") as f:
    print(f.read())


# You dont have to explicitly close the file    