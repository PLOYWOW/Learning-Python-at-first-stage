import random
y = random.randint(0, 9)
print(y)
x = int(input())

if x == y:
    print("Yes!")
elif x < y:
    print("too small")
else:
    print("too big")
    