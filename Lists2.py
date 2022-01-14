data = [3,2,4,8,10,2,6,9,8,3,7,3,3]

sum = 0
for i in range(len(data)):
    sum = sum + data[i]

print(sum)

avg = sum/len(data)
print(avg)

for a in range(len(data)):
    if data[a]%2 == 1:
        print(data[a], end = " ")

print()
#dup = 0

#for b in range(len(data)):
#    d = b+1
#    for c in range(d,len(data)):
#        print("b =",data[b], end = " ")
#        print("c =",data[c])
#        if data[b] == data[c]:
#            dup = dup + 1
#            print(dup)

#print(dup)
#data = [3,2,4,8,10,2,6,9,8,3,7]
store = []
dupp = 0
for b in range(len(data)):
    dup = data.count(data[b])
    print("[data] =",data)
    print("data[b] =",data[b])
    print("dup =",dup)
    if dup >= 2:
        dupp = dupp + 1
    
    store.append(data[b])
    print("[store] =",store)
    county = store.count(store[b])
    print("store[b] =",store[b])
    print("county =",county)
    print()
    if county >= 2:
        dupp = dupp - 1

print("dup =",dupp)
