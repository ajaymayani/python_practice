import random

listChoice = ["s", "w", "g"]

computerScore = 0
userScore = 0

no_of_chance = 0
chance = 10

userName = input("Enter your name : ")

while no_of_chance < chance:
    print("s Snake\nw Water\ng Gun")
    userChoice = input()
    computerChoice = random.choice(listChoice)

    if userChoice == computerChoice:
        print("try again")
    elif userChoice == "s" and computerChoice == "w":
        userScore += 1
        print(f"You choice {userChoice} and computer choice {computerChoice}")
        print(f"Your score is {userScore} and computer score is {computerScore}")
    elif userChoice == "s" and computerChoice == "g":
        computerScore += 1
        print(f"You choice {userChoice} and computer choice {computerChoice}")
        print(f"Your score is {userScore} and computer score is {computerScore}")
    elif userChoice == "w" and computerChoice == "s":
        computerScore += 1
        print(f"You choice {userChoice} and computer choice {computerChoice}")
        print(f"Your score is {userScore} and computer score is {computerScore}")
    elif userChoice == "w" and computerChoice == "g":
        userScore += 1
        print(f"You choice {userChoice} and computer choice {computerChoice}")
        print(f"Your score is {userScore} and computer score is {computerScore}")
    elif userChoice == "g" and computerChoice == "s":
        userScore += 1
        print(f"You choice {userChoice} and computer choice {computerChoice}")
        print(f"Your score is {userScore} and computer score is {computerScore}")
    elif userChoice == "g" and computerChoice == "w":
        computerScore += 1
        print(f"You choice {userChoice} and computer choice {computerChoice}")
        print(f"Your score is {userScore} and computer score is {computerScore}")
    no_of_chance += 1
    print(f"{chance - no_of_chance} chance is left out of {chance}")

print("GAME OVER!!")

if userScore > computerScore:
    print(f"{userName} score is {userScore} and computer score is {computerScore}")
    print(f"{userName} is win")
elif userScore < computerScore:
    print(f"Computer score is {computerScore} and {userName} score is {userScore}")
    print(f"{userName} is win")
else:
    print(f"Computer score is {computerScore} and {userName} score is {userScore}")
    print("Game is tie")
