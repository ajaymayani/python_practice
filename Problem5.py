def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    list = [38,87,3,12,76,23,1]
    list1 = []
    # for i in range(len(list)):
    #     if list[i]<10:
    #         list1.append(list[i])
    #     else:
    #         list1.append(next_palindrome(list[i]))

    print(f"old list {list}")
    print(f"new list {[list[i] if list[i]<10 else next_palindrome(list[i]) for i in range(len(list))]}")
    # print([i for i in range(10,12,)])
    # map =
    # print([i for i in map(lambda x:x+10,list)])
    # for i in map:
    #     print(i,end=",")
