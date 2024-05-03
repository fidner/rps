import random

while True:
    userAction = input("rock paper or scissors? ")
    actions = ["rock", "paper", "scissors"]
    computerAction = random.choice(actions)
    
    print(f"\nyou chose {userAction}, computer chose {computerAction}.\n")

    if userAction == computerAction:
        print(f"tie")
    elif userAction == "rock":
        if computerAction == "scissors":
            print("win")
        else:
            print("loser")
    elif userAction == "paper":
        if computerAction == "rock":
            print("win")
        else:
            print("lose")
    elif userAction == "scissors":
        if computerAction == "paper":
            print("win")
        else:
            print("loser you loser loser loser")
    else:
        print("the hell?")
    yesplayagain = input("do you wanna play again ((loser)) y/n: ")
    if yesplayagain.lower() != "y":
        break
