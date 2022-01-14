import random
pokemon = ["Freezer","Pigey","Pikachu","Ditto","Psyduck"]
x = 0
y = random.randint(0, 4)
print(x,"y =",y)
a = y
#score
z = 0
print("Enter for")

for i in range(10):
    if y == a:
        z = z+1

    a = y
    print(x,"a =",a, end = " ")
    x = x+1
    y = random.randint(0, 4)
    print(x,"y =",y, end = " ")
    print("z =",z)
    

print("Score =",z)

if z >= 5:
    print("Pikachu")
if z == 4:
    print("Freezer")
if z == 3:
    print("Pigey")
if z == 2:
    print("Ditto")
if z == 1:
    print("Psyduck")

    




#y = random.randint(0, 4)
#print(y)
#print()
#x = 0
#for i in range(5):
#    b = random.randint(0, 4)
#    print(b)
#    if y == b:
#        x = x+1
#print("x =",x)
#if x == 2:
#    print("Pikachu")
#else:
#    print(pokemon[y])