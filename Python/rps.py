import random

wins = 0 
loss = 0 
tie = 0
print("ROCK, PAPER, SCISSORS")
while(1):
    print("Type (r)ock, (p)aper, (s)cissors, or (q)uit")
    sResponse = input()
    computerResponse = random.randrange(1,3,1)

    #User response
    if(sResponse == 'q'):
        exit()
    elif(sResponse == 'r'):
        print("You chose rock")
        response = 1
    elif(sResponse == 'p'):
        print("You chose paper")
        response = 2
    else: 
        response = 3
        print("You chose scissors")

    #Computer choices
    if(computerResponse == 1):
        print("Computer chose rock")
    elif(computerResponse == 2):
        print("Computer chose paper")
    else: 
        print("Computer chose scissors")

# Rock = 1, Paper = 2, Scissors = 3
# Rock: 1-1 T, 1-2 == -1 L, 1-3 == -2 W 
# Paper: 2-2 T, 2-3 == -1 L, 3-1 == 2 W
# Scissors: 3-3 T, 3-1 == 2 L, 3-2  == 1 W 

    if(response - computerResponse == 0):
        print("Tie!")
        tie += 1
    elif((response - computerResponse) == 1 or (response - computerResponse) == -2 or ((response - computerResponse) == 2 and sResponse == 'p')):
        print("Win")
        wins += 1
    else:
        print("Loss")
        loss += 1
    
    print("\nScoreboard:\n" + "Wins: " + str(wins) + " Losses: " + str(loss) + " Ties: " + str(tie))




    
