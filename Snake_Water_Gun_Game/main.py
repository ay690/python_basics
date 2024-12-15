import random
'''
1 for snake
-1 for water 
0 for gun

'''
computer = random.choice([-1, 0, 1])
yourStr = input("Enter your choice: ")
yourDict = { "s": 1, "w": -1, "g": 0 }
reverseDict = { 1: "Snake", -1: "Water", 0: "Gun" }

you = yourDict[yourStr]

print(f"You chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")

# Base Case
if(computer == you):
    print("It's a Draw")

else:
    if(computer == -1 and you == 1):
        print("You win 😃😃 !!!")

    elif(computer == -1 and you == 0):
        print("You Lose 😕😕 !!!") 

    elif(computer == 1 and you == -1): 
        print("You Lose 😕😕 !!!")

    elif(computer == 1 and you == 0):
        print("You win 😃😃 !!!")
                 
    elif(computer == 0 and you == -1):
        print("You Lose 😕😕 !!!")          

    elif(computer == 0 and you == 1):
        print("You Lose 😕😕 !!!")  

    else:
        print("Something Went Wrong 😑😑😑 !!!!")
