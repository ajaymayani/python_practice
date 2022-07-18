def getTime():
    import datetime
    return datetime.datetime.now()

def createFileForClient(clientName,fileType):
    with open(f"{clientName+fileType}.txt","a") as f:
        if fileType == "diet":
            print("what you had taken in diet ?")
            ans = input()
            content = f"[{getTime()}] {ans}\n"
            f.write(content)
        else:
            print("which exercise you had do ?")
            ans = input()
            content = f"[{getTime()}] {ans}\n"
            f.write(content)

    print("thank you")


print("Which client are you talking note?")
print("ajay,abhay,vasu")
clientName = input()

print(f"for {clientName} what you lock ?")
print("diet,exercise")
fileType = input()

createFileForClient(clientName,fileType)
