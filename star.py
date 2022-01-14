xx = "*"
for x in range(5):
    #print(x,end="")
    for y in range(x+1):
        print(xx,end="")
    print()
print()

# for x in range(5):
#     print(x,end="")
#     for y in range(x-3):
#         #print(y)
#         print(xx,end="")
#     print()
# print()

for x in range(5,0,-1):
    for y in range(x):
        print(xx,end="")
    print()
print()
