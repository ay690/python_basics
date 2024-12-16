with open("log.txt", "r") as f:
    content = f.read()

if("python" in content):
    print("Yes, python is present inside the content.")

else:
    print("No, python is not present inside the content.")    