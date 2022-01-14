import random
y = random.randint(0, 9)
print(y)

x = 0
for i in range(3):
    x = int(input())

    if x == y:
        break
    #else:
        if x < y:
            print("too small")
        else:
            print("too big")

    x = x+1
    
if x == y:
    print("You Won!!")
else:
    print("Game Over!!")

