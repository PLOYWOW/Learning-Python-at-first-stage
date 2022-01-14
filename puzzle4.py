import random
b = 0
for a in range(3):

    y = random.randint(0, 9)
    print(y)

    x = 0
    for i in range(3):
        x = int(input())

        if x == y:
            x = x+1
            break

    if x == y:
        print("You Won!!")
    else:
        print("Game Over!!")

    #Point
    