import random


def guess_game(n1, n2, actual):
    nguess = 1
    guess = int(input(f"Guess a number between {n1} and {n2} \n"))

    while guess != actual:
        nguess += 1
        if guess > actual:
            guess = int(input("Wrong guess a smaller number again\n"))
        else:
            guess = int(input("Wrong guess a bigger number again\n"))
    print(f"You guess the number in {nguess} guesses")
    return nguess


if __name__ == '__main__':
    player1 = input("Enter player 1 name : \n")
    player2 = input("Enter player 2 name : \n")
    a = int(input("Enter a value of a : \n"))
    b = int(input("Enter a value of b : \n"))

    computer_guess_number = random.randint(a, b)

    print("Player 1 : ")
    player1_guess_count = guess_game(a, b, computer_guess_number);

    print("Player 2 : ")
    computer_guess_number = random.randint(a, b)
    player2_guess_count = guess_game(a, b, computer_guess_number);

    if player1_guess_count > player2_guess_count:
        print(f"{player2} is win!")
    elif player1_guess_count < player2_guess_count:
        print(f"{player1} is win!")
    else:
        print("It's tie!")
