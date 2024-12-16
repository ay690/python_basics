f = open("file.txt")

# lines = f.readlines()

# print(lines, type(lines)) 
# ['Aniket is a good boy.\n', 'I am a seconde line\n', 'This is amazing\n', 'Twinkle Twinkle Little Star'] <class 'list'>  

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))


line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()


f.close()

'''
Aniket is a good boy.
 <class 'str'>
I am a seconde line
 <class 'str'>
This is amazing
 <class 'str'>
Twinkle Twinkle Little Star <class 'str'>
 <class 'str'>

'''

