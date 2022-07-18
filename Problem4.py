def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':

    n = int(input("Enter the number of test cases :\n "))
    numbersList = []
    for i in range(n):
        numbersList.append(int(input("Enter the number : \n")))

    for index in range(n):
        print(f"Next palindrome for {numbersList[index]} is {next_palindrome(numbersList[index])}")
