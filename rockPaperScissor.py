print("                              RULES!!!!")
print("            This game is based on rock, paper and scissors ")
print("Rock defeats scissors, paper defeats rock and scissors defeats paper")
print("           Type r for rock, p for paper and s for scissors")
print("             First to 5 wins, wins the game. Have fun!!!")

import random

playerDict = {
    "r" : 1,
    "p" : 2,
    "s" : 3
}

compDict = {
    1 : "rock",
    2 : "paper",
    3 : "scissors"
}

compCount = 0
playerCount = 0

def playerWon(pC, cC):
    print("You win this round")
    pC +=1
    print("You -> ",pC, " Computer -> ",cC)
    return pC
    
def compWon(pC, cC):
    print("Computer wins this round")
    cC +=1
    print("You -> ",pC, " Computer -> ",cC)
    return cC

while(playerCount<5 and compCount<5):
    print()
    choice = input("Enter your choice ")
    player = playerDict[choice]
    computer = random.choice([1, 2, 3])
    print("The computer chose ", compDict[computer])

    if(computer == player):
        print("DRAW")
        
    else:
        if(computer == 1 and player == 2 ):
            playerCount = playerWon(playerCount, compCount)
        elif(computer ==1 and player ==3):
            compCount = compWon(playerCount, compCount)
        elif(computer == 2 and player ==1):
            compCount = compWon(playerCount, compCount)
        elif(computer == 2 and player == 3):
            playerCount = playerWon(playerCount, compCount)
        elif(computer==3 and player == 1):
            playerCount = playerWon(playerCount, compCount)
        elif(computer == 3 and player == 2):
            compCount = compWon(playerCount, compCount)
        else:
            print("Something went wrong")
print()
if(playerCount > compCount):
    print("CONGRATULATIONS YOU WON!! :) ")
else:
    print("Better luck next time. :(")
