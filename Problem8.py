import random


def rohanMultiplication(n):
    randomNumber = random.randint(0, 9)

    table = [i * n for i in range(1, 11)]
    table[randomNumber] = table[randomNumber] + 5
    return table


def isCorrect(table, number):
    for i in range(1, 11):
        if table[i - 1] != i * number:
            return i - 1

    return None


if __name__ == '__main__':
    number = int(input("Enter number : "))
    rohanTable = rohanMultiplication(number)
    print(rohanTable)
    wrongIndex = isCorrect(rohanTable, number)
    print(f"The table is wrong at index {wrongIndex}")
