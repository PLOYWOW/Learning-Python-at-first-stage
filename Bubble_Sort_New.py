#def sort():
BB = [14,33,27,35,10]
# x = BB[3]
# BB[3] = BB[4]
# BB[4] = x
# print(BB)
count = 0
for i in range(len(BB)-1):
    for a in range(len(BB)-1):
        if BB[a+1] < BB[a]: #สลับ
            x = BB[a]
            BB[a] = BB[a+1]
            BB[a+1] = x
            print(BB)
            count = count + 1
print(count)


    