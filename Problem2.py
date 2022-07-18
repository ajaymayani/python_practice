n = int(input("How many apple harry have ? "))
mn = int(input("Enter minimum number : "))
mx = int(input("Enter maximum number : "))

for i in range(mn, mx + 1):
    if n % i == 0:
        print(f"{i} is divisor of {n}")
    else:
        print(f"{i} is not divisor of {n}")
