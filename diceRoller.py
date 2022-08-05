import random

while True:

    number = random.randint(1,6)
    if number == 1:
        print("=============")
        print("|           |")
        print("|           |")
        print("|     0     |")
        print("|           |")
        print("|           |")
        print("=============")

    elif number == 2:
        print("=============")
        print("|         0 |")
        print("|           |")
        print("|           |")
        print("|           |")
        print("|  0        |")
        print("=============")

    elif number == 3:
        print("=============")
        print("|         0 |")
        print("|           |")
        print("|     0     |")
        print("|           |")
        print("| 0         |")
        print("=============")

    elif number == 4:
        print("=============")
        print("| 0       0 |")
        print("|           |")
        print("|           |")
        print("|           |")
        print("| 0       0 |")
        print("=============")

    elif number == 5:
        print("=============")
        print("| 0       0 |")
        print("|           |")
        print("|     0     |")
        print("|           |")
        print("| 0       0 |")
        print("=============")

    elif number == 6:
        print("=============")
        print("| 0       0 |")
        print("|           |")
        print("| 0       0 |")
        print("|           |")
        print("| 0       0 |")
        print("=============")

    cont = input("Do your want to roll again? Press Y or N: ")

    while cont.lower() not in ("y", "n"):
        cont = input("Do your want to roll again? Press Y or N: ")

    if cont == "n":
        print("Break")
        break