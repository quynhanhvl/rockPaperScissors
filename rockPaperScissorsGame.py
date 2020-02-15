'''
Created on Feb 1, 2020

@author: ITAUser
'''
keepPlaying = True

while (keepPlaying == True):
    print("Welcome to Rock Paper Scissors!")
    print("Rules: the game will be best of three")
    print('press q of you would like to quit')

    #rock = 1
    #paper = 2
    #scissors= 3
    
    import random
    computerScore = 0
    playerScore = 0

    while (playerScore < 2) and (computerScore < 2):
    
        computerChoice = random.randint(1,3)
        playerChoice = input("your choice: ") 
        #start checking user option
       
        if (playerChoice == "q"):
            keepPlaying = False
            break
       
        elif ((playerChoice == "rock" )and(computerChoice == 1)) or ((playerChoice == "paper") and (computerChoice == 2)) or ((playerChoice == "scissors") and (computerChoice == 3)): 
            print("DRAW!")
            print("Computer's score is: ", + computerScore)
            print("Player's score is: ", + playerScore)
       
        elif ((playerChoice == "rock") and (computerChoice == 2)) or ((playerChoice == "scissors") and (computerChoice == 1)) or ((playerChoice == "paper") and (computerChoice == 3)):
            computerScore =+1
            print("Computer's score is: ", + computerScore)
            print("Player's score is: ", + playerScore)
       
       
        elif ((playerChoice == "paper") and (computerChoice == 1)) or ((playerChoice == "scissors") and (computerChoice == 2)) or ((playerChoice == "rock") and (computerChoice == 3)):
            playerScore =+1
            print("Computer's score is: ", + computerScore)
            print("Player's score is: ", + playerScore)
       
        else:
            print("Your input was not valid, try again")
            
    print("Thanks for playing!")
     
    if (playerScore == 2):
        print("Congrats you won!")
     
    if (computerScore == 2):
        print("The computer won :(")
     
    print (playerScore and computerScore)            
    