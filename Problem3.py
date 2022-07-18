size = int(input("Enter how many item you want to add in list : "))
userInputList = []
for item in range(size):
    userInputList.append(input(f"Enter item {item + 1} price : "))

print("first method : ", userInputList[::-1])
reverseList = []
for i in userInputList.__reversed__():
    reverseList.append(i)
print("second method : ", reverseList)


def swappinglist(list):
    # my logic
    # length = list.__len__()
    #     for i in range(1, int(length / 2) + 1):
    #         last = list[length - i]
    #         list[length - i] = list[i - 1]
    #         list[i - 1] = last
    for i in range(len(list) // 2):
        list[i], list[(len(list) - i - 1)] = list[(len(list) - i - 1)], list[i]
    return list


print("third method: ", swappinglist(userInputList))
