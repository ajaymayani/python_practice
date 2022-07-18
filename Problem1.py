userInput = input("Enter your age or Date of year and we will tell when you turn 100 year old.")
currentYear = 2022

if userInput.isdigit():
    if len(userInput) == 4:
        userInput = int(userInput)

        if userInput<1900:
            print("You seem to be oldest person alive")
        elif userInput > currentYear:
            print("You are not yet born")
        else:
            print(f"You will be 100 year old in {userInput + 100}")

    elif (len(userInput) >= 1) and (len(userInput) <= 2) or (userInput=='100'):
        userInput = int(userInput)
        BirthYear = currentYear - userInput
        print(f"You will be 100 year old in {BirthYear + 100}")
    elif int(userInput) < 0:
        print("You are not yet born")
    elif int(userInput > 100):
        print("You seem to be oldest person alive")


else:
    print("input not digit")