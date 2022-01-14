#bag = ["Jelly","Sandwich","Mama","Water","Pork","Chicken","Beef"]

#for i in range(0,7):
#    print(bag[i])

#import random
#pokemon = ["Freezer","Freezer","Pigey","Pigey","Pikachu","Ditto","Ditto","Psyduck","Psyduck"]
#y = random.randint(0, 8)
#print(pokemon[y])

import random
pokemon = ["Freezer","Pigey","Pikachu","Ditto","Psyduck"]
y = random.randint(0, 4)
print(y)
print()
x = 0
for i in range(5):
    b = random.randint(0, 4)
    print(b)
    if y == b:
        x = x+1
print("x =",x)
if x == 2:
    print("Pikachu")
else:
    print(pokemon[y])