#1 
# 3 6 5 
# 7 10 9 
# 11 14 13 
# 15 18 17 
# 19 22 21
# +2 +3 -1 +2 +3 -1 +2 +3 -1 +2 +3 -1 +2 +3 -1

e = 1 
print(e, end = " ")
for f in range(5):
    print(e+2,e+5,e+4, end = " ")
    e = e+4

d = 1
print(d, end = " ")
while d != 21:
    d = d+2
    print(d, end = " ")
    d = d+3
    print(d, end = " ")
    d = d-1
    print(d, end = " ")

x = 1
y = 1
print(x, end = " ")
while y <= 5:
    print(x+2,x+5,x+4, end = " ")
    y = y+1
    x = x+4

