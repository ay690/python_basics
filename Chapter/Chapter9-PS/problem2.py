import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 67)

    #Fetch the score from hiscore.txt file
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}") 

    if(score > hiscore):
        # write this hiscore to the file
       with open("hiscore.txt", "w") as f:
           f.write(str(score))

   
    return score
 
game()   
    


