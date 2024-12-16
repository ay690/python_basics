f = open("poem.txt")

content = f.read()

if("twinkle" in content):
    print(content)
    print("The word twinkle is presnt in the content")
else:
    print("Not there, better luck next time 👎")

f.close()        